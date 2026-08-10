# T3 — The Table build blueprint (for the Opus build sessions)

**2026-08-10. The design is `T3_design_2026-08-10.md`; this is its work
list, at the grain of `Ministry/Technology/Pass2/VR_1A_WORKLIST.md`.
Every item names its gate. The build discipline at the bottom is part of
the blueprint, not advice.**

Branch state at handoff: `claude/fable-table-cost-analysis-ynunno`
carries everything — the T1/T2/T3 documents, the six run artifacts, the
instruments (`table_checkpoint.py`, `table_checkpoint_probes.json`,
`table_read_pack.py`), and two experimental patches (the guard-slot
measure clause and the fabrication gate, both in
`app/graph/nodes.py`, both marked experimental at the wiring site).
PR #9 is merged; the six worlds are live and byte-identical; the
interference rule's conditions are cleared.

## B1 — Graduate the two experimental patches — GATE: batteries green

The guard-slot measure clause moves from the wiring site into each
world's `POST_HISTORY_GUARDS` export via candidates (the assembly's own
gated path — never a hand-edit of deployed prompts). The fabrication
gate stays app-code but gains: a config flag (`FABRICATION_GATE_MODELS`
or equivalent, default haiku-only per the ruling), a unit test on the
flag/regenerate/fail-open path (mock LLM), and its log line joining the
structured logging the way `length_ceiling_logging.py` did.

## B2 — Round cap 6 → 4 — GATE: s44a re-run green

`MAX_MULTI_WORLD_TURNS = 4` in `app/main.py`, plus a
`wrs/parameters.yaml` entry recording provenance (design T3 §3, Mark's
delegation 2026-08-10) so the number is never a mystery constant again.

## B3 — Deploy configuration: Haiku voices at the table — GATE: B1+B2 landed, B5 green

`LLM_MODEL` set for table generation; solo stays Sonnet until B4
passes. Whatever mechanism carries the split (env at deploy, or a
per-mode model setting — implementer's choice), the setting must be
visible in one place and the cost log must show which model served
which turn (it already does via `[llm_usage] model=`).

## B4 — Solo Deep Interview Haiku checkpoint — GATE for moving solo to Haiku; NOT a gate for B3

The existing per-world checkpoint instrument (`phase2_checkpoint.py`),
all six worlds, `LLM_MODEL=haiku`, full hard bars. Fabrication-0
applies per the standing rule; the fabrication gate (B1) should be
enabled for the run so the shipping config is what's measured. Blind
read optional per Mark's table precedent — but the artifacts go to him
either way. Solo is the free tier's whole surface: no swap without this.

## B5 — Battery re-runs on the shipping stack — GATE for deploy

- `s44a_table_battery.py` (orchestration: direct address, "each of
  you", rep-to-rep, floor behavior) — must hold at cap 4.
- `s47_multiworld_battery.py` (governance seeded cases incl. the
  genuine-divergence round that must NOT be flagged) — must hold.
- `table_checkpoint.py --arm ship-regression` on the fixed probe set —
  compare against the cell-6 artifact; no hard-bar regressions.

## B6 — Harness 1B capture (the Albina instrument gap, third sighting)

Drift records gain the rationale and a turn reference so a fabrication
flag can be audited from its own artifact. Touches
`check_drift_for_message`'s record shape and the checkpoint/table
instruments' artifacts. The side-by-side ruling pack this thread built
by log-position reconstruction becomes unnecessary — that
reconstruction was the workaround, not the fix.

## B7 — Sonnet trigger recalibration — only where Sonnet remains

`RETRY_TRIGGER_MULTIPLES` to ~1.3 for solo-mode Sonnet (56% of its
fires were marginal ≤1.3×; its retries work, so the marginal band is
pure waste). Do NOT apply to Haiku (its fires are structural; the
ceilings still pull toward measure). Re-derive if B4 moves solo to
Haiku first.

## B8 — Table transparency verified visible — GATE: human render check

Worklist 6b's discipline extended to the table UI: citations, glosses,
name-bridge pills rendered per speaker in a real browser, once, by a
human. PR #9's honest note stands: three transparency surfaces have
never been human-rendered.

## B9 — Metering (SH-12 scope, separate workstream)

Rounds-based monthly caps per the funding log's tier decision
(2026-08-09). Referenced here so the build doesn't invent a second
metering; not this blueprint's deliverable.

## B10 — Cost re-baseline

After deploy: `cost_baseline_runner.py --run` on the untouched fixed
set, plus one run of the table checkpoint probes, so the standing cost
record reflects the shipped stack. Note for the record: the fixed set's
scripted table conversation understates conversational round length
(2.6 vs 3.4–4.8 rep turns/round measured) — keep both instruments,
never edit either probe set.

## Build discipline (part of the blueprint)

- Candidates and checkpoints, never hand-edits of deployed prompts;
  emitted is what ships; per-world failure measures.
- The Goodhart rule: every diversity/shape metric stays observational.
- Fixed probe sets (`cost_baseline_conversations.json`,
  `table_checkpoint_probes.json`) are immutable; new questions go in
  new files.
- Report what does not work, with its evidence — this thread's most
  load-bearing findings were corrections (the run-notes pricing slip,
  the teaching-density hypothesis, the guard null result, the retry
  comparison). A brief that only reports wins is not usable.
- Every quality claim gets a number or a named human read.
