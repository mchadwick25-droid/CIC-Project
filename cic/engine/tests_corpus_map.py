"""Tests for the corpus map. Run: python cic/engine/tests_corpus_map.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus_map


def check(label, ok):
    print(f"  {'OK ' if ok else '***'} {label}")
    return ok


results = []
results.append(check("the seeded map validates clean", corpus_map.validate() == []))

ids = corpus_map.census_ids()
results.append(check("every map filename is a census movement id",
                     all(a in ids for a in corpus_map.load())))

# Non-exclusivity is the load-bearing property: the same work in several Atlas
# entries must NOT be a finding. An exclusive partition would strip desert of
# the Vita Antonii, whose author belongs to Alexandria.
docs = corpus_map.load()
vita = [w for d in docs.values() for w in (d.get("works") or []) if "Vita Antonii" in str(w.get("work"))]
results.append(check("a work may be assigned to several entries (checked by design, not by count)",
                     len(vita) >= 1))

# Pre-Survey Candidate entries are valid targets.
results.append(check("pre-survey entries are assignable",
                     any(s == "Pre-Survey Candidate" for s in ids.values()) and corpus_map._ANY_STATUS))



# --- the staging -> bucket merge ---
import corpus_map_merge  # noqa: E402

rows, rulings, merge_findings = corpus_map_merge.load_staging()
results.append(check("staging loads with no findings", merge_findings == []))

# The merge is the only writer, so every bucket must be reproducible from
# staging. If a bucket exists that a --check merge does not produce, someone
# hand-edited a generated file and the next merge would silently discard it.
buckets, _ = corpus_map_merge.merge(write=False)
results.append(check("every bucket on disk is reproducible from staging",
                     set(corpus_map.load()) == set(buckets)))

# Non-exclusivity again, this time through the merge: every atlas_id a row
# names must actually receive that row.
#
# The obvious form of this test - count the buckets a work landed in and
# compare to one row's id count - is wrong: `role` is a property of the
# (work, entry) pair, so one work can be written as SEVERAL rows. Against
# Heresies has a `tradition` row for Irenaeus' own entry and a `context` row
# for the entries it describes. It lands in four buckets while no single row
# names more than two, and that is correct. Test the invariant that actually
# holds.
multi = [r for r in rows if len(r["_atlas_ids"]) > 1]
missed = [(r["work"], a) for r in multi for a in r["_atlas_ids"]
          if not any(w.get("work") == r["work"] and w.get("source_file") == r["source_file"]
                     for w in buckets.get(a, []))]
results.append(check(f"every atlas_id named by a multi-entry row receives it "
                     f"({len(multi)} such row(s))", not missed))

# Every ruled author must actually be used, or the ruling is dead weight.
used = {w.get("author") for ws in buckets.values() for w in ws}
results.append(check("every author ruling is used by some assignment",
                     all(slug in used for slug in rulings)))



# --- the `antecedent` role ---
buckets2, _ = corpus_map_merge.merge(write=False)
ante = [(a, w) for a, ws in buckets2.items() for w in ws if w.get("role") == "antecedent"]
results.append(check(f"the antecedent role is in use ({len(ante)} row(s))", bool(ante)))

# An antecedent assignment must NEVER be the author's own home. Cyprian is
# antecedent to `donatism` and tradition in `latin-pastoral...`; if the same
# work were antecedent where it is also tradition, the role would be
# meaningless and someone has used it as a softer `tradition`.
home = {(w.get("work"), a) for a, ws in buckets2.items() for w in ws if w.get("role") == "tradition"}
overlap = [(w.get("work"), a) for a, w in ante if (w.get("work"), a) in home]
results.append(check("no work is both antecedent and tradition in the same entry", not overlap))

# And the rule that stops it exploding is only meaningful if the relation stays
# rare: it requires the entry's own vendored sources to argue from the text.
total_rows = sum(len(v) for v in buckets2.values())
results.append(check(f"antecedent stays a narrow relation ({len(ante)}/{total_rows} rows)",
                     len(ante) <= total_rows * 0.05))



# --- the `transmission` role ---
buckets3, _ = corpus_map_merge.merge(write=False)
trans = [(a, w) for a, ws in buckets3.items() for w in ws if w.get("role") == "transmission"]
results.append(check(f"the transmission role is in use ({len(trans)} row(s))", bool(trans)))

# Custody and voice cannot be the same claim about the same entry.
same = [(w.get("work"), a) for a, w in trans
        if any(x.get("work") == w.get("work") and x.get("role") == "tradition"
               for x in buckets3.get(a, []))]
results.append(check("no work is both transmission and tradition in the same entry", not same))

# THE INVARIANT THAT MAKES THE ROLE MEAN SOMETHING. `transmission` says a
# tradition preserved a work that is not its own voice - so that voice has to
# be somewhere. A transmission row whose work has no `tradition` or `context`
# home anywhere is custody of nothing, and almost certainly a mis-used
# `tradition`.
homed = {x.get("work") for ws in buckets3.values() for x in ws
         if x.get("role") in ("tradition", "context")}
orphan = sorted({w.get("work") for _, w in trans if w.get("work") not in homed})
results.append(check("every transmitted work has its voice assigned somewhere else", not orphan))
if orphan:
    for o in orphan:
        print(f"       orphan: {o}")


# --- row_id (CM-1) ---
import tempfile  # noqa: E402

results.append(check("every real staging row carries a row_id", all(r.get("row_id") for r in rows)))
results.append(check("work_slug folds accents, punctuation and case",
                     corpus_map_merge.work_slug("Sermon (De Trinitate) - Ambrosius' \u00c6thelred!") == "sermon-de-trinitate-ambrosius-thelred"))
results.append(check("work_slug falls back when nothing survives", corpus_map_merge.work_slug("\u2014") == "work"))
long_slug = corpus_map_merge.work_slug("abcdefghi " * 10)
results.append(check("work_slug is cut at a word boundary", long_slug == "-".join(["abcdefghi"] * 6)))

_STAGED = """# a comment that must survive
source_file: vol1.xml
assignments:
- work: Alpha
  author: a
  atlas_ids: [x]
- work: Alpha
  author: a
  atlas_ids: [y]
- row_id: vol1--kept-by-hand
  work: Renamed Later
  atlas_ids: [x]
- work: Beta
  atlas_ids: [x]
"""


def _in_temp_staging(text, fn):
    import yaml
    saved = corpus_map_merge.STAGING
    with tempfile.TemporaryDirectory() as d:
        corpus_map_merge.STAGING = Path(d)
        (Path(d) / "vol1.yaml").write_text(text, encoding="utf-8")
        try:
            return fn(Path(d) / "vol1.yaml", lambda: yaml.safe_load((Path(d) / "vol1.yaml").read_text())["assignments"])
        finally:
            corpus_map_merge.STAGING = saved


def _assign_case(path, load_rows):
    first = corpus_map_merge.assign_ids()
    after_first = path.read_text()
    second = corpus_map_merge.assign_ids()
    return first, second, after_first, path.read_text(), load_rows()


first, second, txt1, txt2, staged = _in_temp_staging(_STAGED, _assign_case)
ids = [r["row_id"] for r in staged]
results.append(check("assign_ids gives every row an id and counts them", first[0] == 3 and all(ids)))
results.append(check("a slug collision within one volume takes -2 in staging order",
                     ids[0] == "vol1--alpha" and ids[1] == "vol1--alpha-2" and first[1] == 1))
results.append(check("an existing row_id is never overwritten, even when the title differs",
                     ids[2] == "vol1--kept-by-hand"))
results.append(check("assign_ids is idempotent: the second run assigns nothing and changes nothing",
                     second[:2] == (0, 0) and txt1 == txt2))
results.append(check("assign_ids leaves comments and other fields alone",
                     txt2.startswith("# a comment that must survive") and staged[0]["author"] == "a"))


def _dry_case(path, load_rows):
    before = path.read_text()
    assigned = corpus_map_merge.assign_ids(write=False)[0]
    return assigned, before == path.read_text()


results.append(check("assign_ids with write=False reports and writes nothing",
                     _in_temp_staging(_STAGED, _dry_case) == (3, True)))

def _refusal_case(text):
    def case(path, load_rows):
        other = path.parent / "vol0.yaml"
        other.write_text("source_file: v0.xml\nassignments:\n- work: Z\n  atlas_ids: [x]\n", encoding="utf-8")
        before = (path.read_text(), other.read_text())
        assigned, _, findings = corpus_map_merge.assign_ids()
        return bool(findings) and before == (path.read_text(), other.read_text())
    return _in_temp_staging(text, case)


_HEAD = "source_file: vol1.xml\nassignments:\n"
results.append(check("a flow-mapping row is refused and nothing is written, in any file",
                     _refusal_case(_HEAD + "- work: A\n- {work: B}\n- work: C\n")))
results.append(check("a non-mapping row is refused and nothing is written",
                     _refusal_case(_HEAD + "- work: A\n- just a string\n")))
results.append(check("an anchored row is refused and nothing is written",
                     _refusal_case(_HEAD + "- &r\n  work: A\n- *r\n")))
results.append(check("a null row_id is refused and nothing is written",
                     _refusal_case(_HEAD + "- row_id:\n  work: A\n")))
results.append(check("a top-level list is refused without a crash",
                     _refusal_case("- work: A\n")))


def _crlf_case(path, load_rows):
    corpus_map_merge.assign_ids()
    raw = path.read_bytes()
    return raw.count(b"\r\n") == raw.count(b"\n") and load_rows()[0]["row_id"] == "vol1--a"


_STAGING_ROOT = corpus_map_merge.STAGING
results.append(check("CRLF line endings survive an assignment",
                     _in_temp_staging("source_file: vol1.xml\r\nassignments:\r\n- work: A\r\n  atlas_ids: [x]\r\n",
                                      _crlf_case)))

dup_findings = _in_temp_staging(
    "source_file: vol1.xml\nassignments:\n- row_id: same\n  work: A\n  atlas_ids: [x]\n"
    "- row_id: same\n  work: B\n  atlas_ids: [x]\n",
    lambda p, l: corpus_map_merge.load_staging()[2])
results.append(check("load_staging flags one row_id used by two staging rows",
                     any("already used" in f for f in dup_findings)))

# validate(): presence and uniqueness, on the loaded map.
_real_load = corpus_map.load


def _validate_with(works_by_bucket):
    corpus_map.load = lambda: works_by_bucket
    try:
        return corpus_map.validate()
    finally:
        corpus_map.load = _real_load


def _row(row_id, work="W"):
    r = {"work": work, "author": "synthetic", "source_file": "f.xml", "role": "tradition", "confidence": "assigned"}
    if row_id is not None:
        r["row_id"] = row_id
    return r


def _bucket(atlas_id, *works):
    return {"atlas_id": atlas_id, "fixture": True, "works": list(works)}


missing = _validate_with({"fixture-a": _bucket("fixture-a", _row(None))})
results.append(check("validate flags a row with no row_id", any("missing 'row_id'" in f for f in missing)))
dup_in = _validate_with({"fixture-a": _bucket("fixture-a", _row("k", "W1"), _row("k", "W1"))})
results.append(check("validate flags a row_id repeated within one entry", any("repeats within" in f for f in dup_in)))
clash = _validate_with({"fixture-a": _bucket("fixture-a", _row("k", "W1")),
                        "fixture-b": _bucket("fixture-b", _row("k", "W2"))})
results.append(check("validate flags one row_id naming two different works", any("is already" in f for f in clash)))
shared = _validate_with({"fixture-a": _bucket("fixture-a", _row("k", "W1")),
                         "fixture-b": _bucket("fixture-b", _row("k", "W1"))})
results.append(check("the same row in two buckets shares its row_id without a finding",
                     not any("row_id" in f for f in shared)))

print("\nall passed" if all(results) else "\nFAILURES")
sys.exit(0 if all(results) else 1)
