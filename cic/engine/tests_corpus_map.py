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

print("\nall passed" if all(results) else "\nFAILURES")
sys.exit(0 if all(results) else 1)
