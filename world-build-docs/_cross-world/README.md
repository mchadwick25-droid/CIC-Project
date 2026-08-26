# `_cross-world` — fleet-level, not per-world

Every other directory under `world-build-docs/` belongs to one world and
carries that world's own build history. This one belongs to no world: it
holds the work that can only be done by looking at all six at once.

| file | what it is |
|---|---|
| `CiC_Cross_System_Consistency_Audit_2026-08-26.md` | The audit. The pipeline map, the identical-by-design vs allowed-to-vary line for each of its six stages, and 22 findings with evidence and disposition. |
| `pipeline-drift-map.svg` | The system/data-flow diagram: the governed path (records → compiler → package → runtime → API → app), the ungoverned one (the Atlas census straight to the app), and the three points where divergence enters. |
| `CONSISTENCY-MATRIX.md` | Every invariant against every world. Generated, never hand-written. |
| `gen_matrix.py` | Regenerates the matrix from the live tree: `python world-build-docs/_cross-world/gen_matrix.py`. |

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
