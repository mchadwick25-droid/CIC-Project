# `_cross-world` — fleet-level, not per-world

Every other directory under `world-build-docs/` belongs to one world and
carries that world's own build history. This one belongs to no world: it
holds the work that can only be done by looking at all six at once.

## The audit

| file | what it is |
|---|---|
| `CiC_Cross_System_Consistency_Audit_2026-08-26.md` | The audit. The pipeline map, the identical-by-design vs allowed-to-vary line for each of its six stages, and 25 findings with evidence and disposition. |
| `pipeline-drift-map.svg` | The system/data-flow diagram: the governed path (records → compiler → package → runtime → API → app), the ungoverned one (the Atlas census straight to the app), and the three points where divergence enters. |
| `CONSISTENCY-MATRIX.md` | Every invariant against every world. Generated, never hand-written. |

## The corpus question

Findings F-23 to F-25 all turned out to be the same problem — worlds answering
from one record because nothing had ever asked what the corpus held — so it
has its own set of documents.

| file | what it is |
|---|---|
| `BRIEF-corpus-assignment-thread.md` | **The live brief.** The whole assignment job, every ruling settled, for the separate thread that does it. Start here. |
| `CORPUS-USE.md` | What each world actually draws on, and each world's verifiability share (`pahc 99% · alx 96% · hal 93% · ijc 91% · syr 87% · desert 76%`). Generated. |
| `WANTS-REGISTER.md` | Sources the fleet already depends on and cannot read, ranked by how many records depend on each. Generated. |
| `CORPUS-PARTITION-BRIEF.md` | **Superseded** by `BRIEF-corpus-assignment-thread.md`. Kept for its reasoning, not as instructions — it predates Mark's ruling that the map lives outside the built worlds, and the `corpus_review` record type it describes no longer exists. |

## Regenerating

Three of these are generated from the live tree and should never be
hand-edited:

```
python world-build-docs/_cross-world/gen_matrix.py          # CONSISTENCY-MATRIX.md
python world-build-docs/_cross-world/gen_corpus_table.py    # CORPUS-USE.md
python world-build-docs/_cross-world/gen_wants_register.py  # WANTS-REGISTER.md
```

## The standing check

The audit's own standing check lives in the engine, beside the gate battery
it complements, not here:

```
python -m engine.m1.cross_world          # report; exit 1 on new drift
python -m engine.m1.cross_world --all    # also print the accepted-open detail
```

**A world build should run it before it asks to be admitted.** The M1 gates
say whether a world is well-formed on its own; this says whether it is the
same shape as its siblings. Every finding in the audit was invisible to the
first question and obvious to the second.

The corpus map has its own validator, on the same footing:

```
python cic/engine/corpus_map.py            # validate cic/corpus-map/*.yaml
python cic/engine/corpus_map.py --coverage # also list vendored files with nothing assigned
```
