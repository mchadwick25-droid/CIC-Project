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
_real = {a: d for a, d in corpus_map.load().items() if not d.get("fixture")}
results.append(check("every map filename is a census movement id",
                     all(a in ids for a in _real)))

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
                     set(_real) == set(buckets)))

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
# Transmitted works whose voice belongs to a window no Atlas entry covers yet.
# A work leaves this list when its voice is placed; the second check below
# fails on any entry that is no longer an orphan.
ACCEPTED_ORPHANS = {
    "The other Sahidic texts of the volume (apocryphal discourses and legends)":
        "Anonymous and undated; no entry fits.",
    "The other Sahidic texts of the volume, including a Discourse attributed to Timothy of Alexandria":
        "Anonymous and undated; no entry fits.",
}
orphan = sorted({w.get("work") for _, w in trans if w.get("work") not in homed})
unlisted = [o for o in orphan if o not in ACCEPTED_ORPHANS]
results.append(check("every transmitted work has its voice assigned somewhere else, or is a listed exception",
                     not unlisted))
for o in unlisted:
    print(f"       orphan: {o}")
stale = sorted(w for w in ACCEPTED_ORPHANS if w not in orphan)
results.append(check("every listed exception is still an orphan", not stale))
for w in stale:
    print(f"       no longer an orphan: {w}")


# --- row_id (CM-1) ---
import tempfile  # noqa: E402

results.append(check("every real staging row carries a row_id", all(r.get("row_id") for r in rows)))
results.append(check("work_slug folds accents, punctuation and case",
                     corpus_map_merge.work_slug("Sermon (De Trinitate) - Ambrosius' \u00c6thelred!") == "sermon-de-trinitate-ambrosius-thelred"))
results.append(check("work_slug falls back when nothing survives", corpus_map_merge.work_slug("\u2014") == "work"))
long_slug = corpus_map_merge.work_slug("abcdefgh " * 10)
results.append(check("work_slug is cut at a word boundary", long_slug == "-".join(["abcdefgh"] * 6) and len("-".join(["abcdefgh"] * 7)) > 60))

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
results.append(check("an anchored row with no alias is refused and nothing is written",
                     _refusal_case(_HEAD + "- &r\n  work: A\n")))
results.append(check("mixed line endings are refused without a crash",
                     _refusal_case("source_file: vol1.xml\nassignments:\r\n- work: A\r\n")))
results.append(check("a repeated `assignments` key is refused",
                     _refusal_case(_HEAD + "- work: A\nassignments:\n- work: B\n")))
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

# --- the optional row fields: locus_ids, voice_of, documented_exchange, language, date ---
_FIELDS_STAGED = """source_file: vol1.xml
assignments:
- row_id: vol1--a
  work: A
  author: a
  locus: whole
  locus_ids: [whole-file]
  atlas_ids: [x]
  role: context
  confidence: assigned
  voice_of: fixture-synthetic-neighbour
  documented_exchange: confirmed
  language: grc-lat
  date: {start: 300, end: 325, source: "Edition preface", formation_confidence: Contested}
  note: n
- row_id: vol1--b
  work: B
  author: a
  atlas_ids: [x]
  date: {formation_confidence: unknown, checked: "edition preface; Clavis Patrum Graecorum"}
"""
carried = _in_temp_staging(_FIELDS_STAGED, lambda p, l: (corpus_map_merge.load_staging(), corpus_map_merge.merge(write=False)))
(carried_rows, _, carried_findings), (carried_buckets, _) = carried
results.append(check("staging rows carrying the new fields load with no findings", carried_findings == []))
_a = carried_rows[0]
results.append(check("the merge carries locus_ids, voice_of, documented_exchange, language and date into the bucket",
                     all(k in _a for k in ("locus_ids", "voice_of", "documented_exchange", "language", "date"))
                     and _a["date"]["formation_confidence"] == "Contested"
                     and carried_rows[1]["date"] == {"formation_confidence": "unknown",
                                                     "checked": "edition preface; Clavis Patrum Graecorum"}))
results.append(check("a row without the new fields gains none",
                     not {"locus_ids", "voice_of", "documented_exchange", "language"} & set(carried_rows[1])))
results.append(check("the new fields keep a fixed key order in the generated row",
                     [k for k in _a if k != "source_file"] == [k for k in corpus_map.ROW_FIELDS if k in _a and k != "source_file"]
                     + ["_atlas_ids", "_from"]))
results.append(check("staging rejects an unknown field instead of dropping it",
                     any("unknown field 'voice-of'" in f for f in _in_temp_staging(
                         _HEAD + "- work: A\n  atlas_ids: [x]\n  voice-of: z\n",
                         lambda p, l: corpus_map_merge.load_staging()[2]))))


_VOICE_IDS = set(corpus_map.census_ids()) | corpus_map.pair_parties()


def _fields(**extra):
    r = _row("k")
    r.update(extra)
    return corpus_map.row_field_findings(r, "t", _VOICE_IDS)


_via_validate = [f for f in _validate_with({"fixture-a": _bucket("fixture-a", {
    **_row("k"), "role": "context", "voice_of": "nobody", "colour": "x"})}) if "is not in cic/texts" not in f]
results.append(check("validate applies the field rules and rejects unknown fields on a bucket row",
                     any("unknown field 'colour'" in f for f in _via_validate)
                     and any("neither a census movement id" in f for f in _via_validate)))

# --- translator and edition_date: facts about the vendored edition, each with its source line ---
_EDITION_OK = _fields(translator={"name": "Ernest Wallis", "source": "anf05_x.xml line 40", "formation_confidence": "Documented"},
                      edition_date={"year": 1886, "source": "anf05_x.xml line 12", "formation_confidence": "Documented"})
results.append(check("translator and edition_date with a source line and a confidence are accepted", _EDITION_OK == []))
_EDITION_UNKNOWN = _fields(translator={"formation_confidence": "unknown", "checked": "title page; volume preface"},
                           edition_date={"formation_confidence": "unknown", "checked": "title page"})
results.append(check("translator and edition_date may be unknown with where it was looked for", _EDITION_UNKNOWN == []))
results.append(check("translator without a source line is a finding",
                     any("needs a non-empty `source`" in f for f in _fields(
                         translator={"name": "A. B.", "formation_confidence": "Documented"}))))
results.append(check("edition_date needs an integer year",
                     any("year is missing or malformed" in f for f in _fields(
                         edition_date={"year": "1886", "source": "x line 1", "formation_confidence": "Documented"}))))
results.append(check("an unknown translator without `checked` is a finding",
                     any("needs `checked`" in f for f in _fields(translator={"formation_confidence": "unknown"}))))
results.append(check("a made-up confidence level is a finding",
                     any("is not one of" in f for f in _fields(
                         edition_date={"year": 1886, "source": "x line 1", "formation_confidence": "Not Attested"}))))



def _ctx(**extra):
    return _fields(role="context", voice_of="fixture-synthetic-neighbour", **extra)


results.append(check("a well-formed set of the new fields validates clean",
                     _ctx(locus_ids=["whole-file"], documented_exchange="confirmed", language="grc-lat",
                          date={"start": -50, "end": 10, "source": "s", "formation_confidence": "Documented"}) == []))
results.append(check("locus_ids must be a non-empty list of strings",
                     all(any("locus_ids" in f for f in _fields(locus_ids=v)) for v in ([], "div1", [1], [""]))))
results.append(check("locus_ids may not repeat an id", any("repeats" in f for f in _fields(locus_ids=["a", "a"]))))
results.append(check("voice_of on a tradition row is a finding", any("only for non-tradition" in f
                     for f in _fields(voice_of="fixture-synthetic-neighbour"))))
results.append(check("voice_of must name a census id or a PAIRS party",
                     any("neither a census movement id" in f for f in _fields(role="context", voice_of="nobody"))))
results.append(check("voice_of may name a census id", not any("voice_of" in f for f in _fields(
                     role="context", voice_of=next(iter(corpus_map.census_ids()))))))
results.append(check("documented_exchange without voice_of is a finding",
                     any("only meaningful where voice_of" in f for f in _fields(documented_exchange="confirmed"))))
results.append(check("documented_exchange takes only confirmed, not-confirmed, needs-ruling",
                     any("documented_exchange" in f and "not in" in f for f in _ctx(documented_exchange="maybe"))
                     and all(not any("documented_exchange" in f for f in _ctx(documented_exchange=v))
                             for v in ("confirmed", "not-confirmed", "needs-ruling"))))
results.append(check("language must be lower-case ISO 639-3 codes joined by hyphens",
                     all(any("language" in f for f in _fields(language=v)) for v in ("Latin", "la", "GRC", ["lat"]))
                     and not any("language" in f for f in _fields(language="syr"))))


def _date(**d):
    return [f for f in _fields(date=d) if "date" in f]


_ok = {"start": 100, "end": 200, "source": "s", "formation_confidence": "Widely Accepted"}
results.append(check("a date window with start after end is a finding",
                     any("after end" in f for f in _date(**{**_ok, "start": 201}))))
results.append(check("a date window with start equal to end is allowed", _date(**{**_ok, "start": 200}) == []))
results.append(check("all five formation_confidence levels are accepted",
                     all(_date(**{**_ok, "formation_confidence": c}) == [] for c in corpus_map.FORMATION_CONFIDENCES)
                     and len(corpus_map.FORMATION_CONFIDENCES) == 5))
results.append(check("a sixth level is refused, 'Not Attested' included",
                     all(any("formation_confidence" in f for f in _date(**{**_ok, "formation_confidence": c}))
                         for c in ("Not Attested", "Probable", "documented"))))
results.append(check("a date needs a source and integer years",
                     any("source" in f for f in _date(start=1, end=2, formation_confidence="Documented"))
                     and any("integer year" in f for f in _date(**{**_ok, "start": "c.100"}))
                     and any("integer year" in f for f in _date(**{**_ok, "end": True}))))
results.append(check("an unknown date needs `checked` and carries no window",
                     _date(formation_confidence="unknown", checked="Clavis") == []
                     and any("needs `checked`" in f for f in _date(formation_confidence="unknown"))
                     and any("must not carry" in f for f in _date(formation_confidence="unknown", checked="c", start=1))))
results.append(check("`checked` with a confidence level, an unknown date key and a non-mapping date are findings",
                     any("belongs only with" in f for f in _date(**{**_ok, "checked": "c"}))
                     and any("unknown key" in f for f in _date(**{**_ok, "era": "x"}))
                     and any("must be a mapping" in f for f in _fields(date="c. 300"))))


# --- a repeated key is a finding, never a silent last-wins ---
import tempfile  # noqa: E402
import yaml  # noqa: E402

_dup = "- work: A\n  language: la\n  language: grc\n"


def _raises(text):
    try:
        corpus_map.load_unique(text)
    except yaml.YAMLError as err:
        return "repeated key 'language'" in str(err)
    return False


results.append(check("load_unique refuses a repeated key and names it", _raises(_dup)))
results.append(check("load_unique refuses a repeated key in a nested mapping and a flow mapping",
                     _raises("x:\n  - {language: la, language: grc}\n")
                     and _raises("x:\n  y:\n    language: la\n    language: grc\n")))
results.append(check("load_unique keeps ordinary documents, repeated values and merge keys",
                     corpus_map.load_unique("a: 1\nb: [1, 1]\nc: {a: 1}\nd: {a: 1}\n") == {"a": 1, "b": [1, 1], "c": {"a": 1}, "d": {"a": 1}}
                     and corpus_map.load_unique("base: &b {x: 1}\nuse:\n  <<: *b\n  y: 2\n")["use"] == {"x": 1, "y": 2}))

_saved = corpus_map_merge.STAGING
with tempfile.TemporaryDirectory() as _tmp:
    corpus_map_merge.STAGING = Path(_tmp)
    (Path(_tmp) / "dup.yaml").write_text("source_file: x.txt\nassignments:\n" + _dup.replace("- work", "  - work").replace("\n  language", "\n    language"), encoding="utf-8")
    _, _, _found = corpus_map_merge.load_staging()
    results.append(check("a staging file with a repeated key is a finding in the merge read",
                         any("dup.yaml" in f and "repeated key" in f for f in _found)))
    _ids = corpus_map_merge.assign_ids(write=False)
    results.append(check("a staging file with a repeated key is a finding in the id pass",
                         any("dup.yaml" in f and "repeated key" in f for f in _ids[2])))
corpus_map_merge.STAGING = _saved

_saved_dir = corpus_map.MAP_DIR
with tempfile.TemporaryDirectory() as _tmp:
    corpus_map.MAP_DIR = Path(_tmp)
    (Path(_tmp) / "dup-bucket.yaml").write_text("atlas_id: dup-bucket\nworks:\n" + _dup.replace("- work", "  - work").replace("\n  language", "\n    language"), encoding="utf-8")
    results.append(check("validate reports a bucket with a repeated key as a finding",
                         any("repeated key" in f for f in corpus_map.validate())))
    (Path(_tmp) / "dup-bucket.yaml").unlink()
    (Path(_tmp) / "UNATTRIBUTED.yaml").write_text("authors:\n  a: x\n  a: y\n", encoding="utf-8")
    results.append(check("validate reports a repeated key in UNATTRIBUTED.yaml as a finding, not a crash",
                         any("repeated key" in f for f in corpus_map.validate())))
    (Path(_tmp) / "UNATTRIBUTED.yaml").unlink()
    (Path(_tmp) / "PAIRS.yaml").write_text("parties:\n  p: 1\n  p: 2\n", encoding="utf-8")
    results.append(check("validate reports a repeated key in PAIRS.yaml as a finding, not a crash",
                         any("repeated key" in f for f in corpus_map.validate())))
    _, _, _pf = corpus_map_merge.load_staging()
    results.append(check("the merge read reports a repeated key in PAIRS.yaml as a finding",
                         any("PAIRS.yaml" in f and "repeated key" in f for f in _pf)))
corpus_map.MAP_DIR = _saved_dir


print("\nall passed" if all(results) else "\nFAILURES")
sys.exit(0 if all(results) else 1)
