# Library Access Gate — the design sandbox workstream

**Charter (Mark, 2026-09-15):** as the fleet scales toward 100+ worlds
sharing one massive library, ensure every world is confined to only its
own tradition's source material — a state-of-the-art library/access
architecture, built through the divergent/struggle/convergent process
(`CLAUDE.md`, "How we work"), the same model already worked for
Website V2. **Design and build the confinement mechanism only.**
Judging which works belong to which tradition is `cic/corpus-map/`'s
job and stays out of scope here.

## Baseline (what already exists, measured 2026-09-15)

- **D5 decision** (`Ministry/Operations/Standing/CiC_Repo_Structure_Tracking.md`):
  "Venn by shelf, with a gate at the door" — one flat, tradition-organized
  library (`cic/texts/` + `cic/corpus-map/`), each world gets a generated
  shelf drawn from its tradition via `census_id`, enforced by a
  build-time gate (WO-4). Chosen over library-only (no per-world view)
  and sources-duplicated-inside-each-world.
- **`tools/gen_shelf.py`** exists and is real (committed `997802250`) —
  generates a world's `SHELF.md` from its corpus-map bucket. It has
  never been run in anger: no `SHELF.md` is committed anywhere yet, and
  nothing calls it in CI.
- **WO-4** (the actual enforcement gate) is specified as three
  compile-time checks — work resolves to the world's shelf; every
  quote/story `address` falls inside that work's locus;
  `context`/`antecedent`/`transmission` works are citable as evidence
  but never voiced — but **not implemented**. `engine/m1/gates.py`
  today checks license validity and verbatim presence, not which
  section or whose voice.
- **The backfill WO-4 needs is largely missing**: `work_id` on 10 of
  343 source records, machine-resolvable `address` on 5 of ~330
  quote/story records, `WORKS.yaml` has 4 seed entries.
- Corpus-map itself is non-exclusive by design: 677 staged works, only
  47 (7%) assigned to a single tradition, median work claimed by 4.

## The funnel

D0 **Immersion** (Fable reads the baseline above, `cic/corpus-map/`,
`engine/m1/gates.py`, the `engine/m2`/`engine/m6` build patterns) → D1
**DIVERGE** (Fable: 3–5 genuinely different confinement-architecture
directions, each argued on correctness, build cost, and scaling to
100+ worlds over a much larger library — "harden and finish WO-4 as
already specified" is a legitimate direction but must be argued for
like any other, not defaulted to) → D2 **STRUGGLE** (Opus adversarial
review of every direction, filed as a document, not a verdict) → Mark
picks → D3 **CONVERGE** (frozen design doc) → D4 **BUILD** (increments,
each read by Mark before merge — same discipline as every other build
this session, never self-merged).

## Model routing (Mark, 2026-09-15)

Sonnet coordinates, keeps the ledger, and carries the converged design
to build. Fable does the deep research and design synthesis. Opus runs
the critical/adversarial review. Nothing here evaluates source
content — that stays corpus-map's job, unchanged.

Decisions land in `Decision-Log.md`, here, workstream-local.
