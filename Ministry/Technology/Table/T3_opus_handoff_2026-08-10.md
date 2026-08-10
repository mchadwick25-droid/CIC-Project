# Opus build brief — the Table ships on Haiku: build to the blueprint

Written 2026-08-10 at the close of the Fable table thread (Phases 1–2:
cost strategy, quality evidence, design, blueprint — all complete).
Paste this into the Opus build session. It carries the settled
decisions so nothing gets re-litigated, the measured facts so nothing
gets re-derived, and the work list so the build starts at the first
item, not at a discussion.

## Read these, in this order

1. `Ministry/Technology/Table/T3_design_2026-08-10.md` — what ships and why
2. `Ministry/Technology/Table/T3_blueprint_2026-08-10.md` — the work list, B1–B10, each with its gate
3. `Ministry/Technology/Table/T2_read_ruling_2026-08-10.md` and
   `T2_fabrication_side_by_side_2026-08-10.md` — Mark's rulings, verbatim

Supporting record (consult, don't reread whole):
`T1_cost_feasibility_2026-08-09.md` (cost architecture),
`T2_quality_Q1_evidence_2026-08-10.md` (why this was a Table-layer
change), `T2_read_key_2026-08-10.md` (the five-arm instrument numbers
and cost table), `runs/*.json` (six measured cells on the fixed probe
set).

## Already decided — carry, do not reopen

- **Haiku voices at the table**, ruled on Mark's blind read (he could
  not distinguish; "not an integrity or trust problem"); pilot group is
  the live quality instrument. The 90% criterion is met by the ruled
  instrument (the human read; Goodhart rule governs all metrics).
- **The fabrication ruling:** every flagged class passes EXCEPT the
  invented vignette (particular people/relationships/events spoken as
  communal memory with no record behind them). That class is blocked by
  the pre-emission fabrication gate, Haiku voices only, fail-open.
- **v4 table blocks; round cap 4; floor 2; ceilings unchanged; solo
  stays Sonnet until B4 passes.** All per the design §3, under Mark's
  delegation.
- Table cap 3 seats (5 is a gated research-tier feature — funding log
  2026-08-09); table is paid-tier (SH-12); the four VR_1A decision
  documents; readability is a hard edge per emitted turn.

## Measured facts you will need (do not re-derive)

- Haiku table ≈$0.12/round; Sonnet $0.29/round at Sept-1 standard
  pricing. Sonnet's intro pricing ends 2026-08-31 — B3's deploy wants
  to land before that.
- Conversational tables run 3.4–4.8 rep turns/round uncapped; ceilings
  fire on ~80–90% of turns on both models; Sonnet's fires are marginal
  and its retries work; Haiku's are structural and retries/guard-slot
  prompting do NOT fix them (clean null result — do not respin prompt
  fixes for Haiku length; the design accepts the cost for pilot).
- Zero B2 breaches in six cells; divergence held everywhere. The
  teaching-density-by-example hypothesis did NOT transfer to emitted
  turns — recorded correction; don't cite the old expectation.

## State of the branch you're building on

`claude/fable-table-cost-analysis-ynunno`, pushed. It carries all
documents and artifacts above, the instruments
(`scripts/table_checkpoint.py`, `table_checkpoint_probes.json`,
`table_read_pack.py`), and two experimental patches in
`app/graph/nodes.py` awaiting B1's graduation: the guard-slot measure
clause and the fabrication gate (marked in comments, log lines
`[fabrication_gate]`). The working tree also has the v4
`app/prompts/table_discourse.py` committed. PR #9 merged 2026-08-10;
all six worlds live and byte-identical; `PENDING_RECHECKPOINT` empty.
Cell 6 (`haiku-v4-guard-fabgate-table`) is the shipping-stack
verification artifact.

## How to work

- Build in blueprint order; every item's gate is named — a gate is a
  measurement or a battery, never an assertion.
- Measure before proposing; report failures with their evidence; every
  quality claim gets a number or a named human read.
- Fixed probe sets are immutable. Candidates, never hand-edits.
- When something here proves wrong in the building, say so loudly and
  record the correction — this thread's record shows exactly how.
