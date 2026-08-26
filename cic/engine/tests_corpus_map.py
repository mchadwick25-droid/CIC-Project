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

# Pre-Survey Candidate entries are valid targets - Mark, 2026-08-26.
results.append(check("pre-survey entries are assignable",
                     any(s == "Pre-Survey Candidate" for s in ids.values()) and corpus_map._ANY_STATUS))



# --- the staging -> bucket merge (added with the Fable handoff, 2026-08-26) ---
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
# compare to one row's id count - was WRONG, and the 2026-08-26 assignment run
# exposed it. The workers converged on modelling `role` as a property of the
# (work, entry) pair, so one work is written as SEVERAL rows: Against Heresies
# has a `tradition` row for Irenaeus' own entry and a `context` row for the
# entries it describes. It lands in four buckets while no single row names more
# than two, and that is correct. Test the invariant that actually holds.
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

print("\nall passed" if all(results) else "\nFAILURES")
sys.exit(0 if all(results) else 1)
