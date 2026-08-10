# T2 — Q1 answered with evidence: what carrying 1A to the table actually touches

**Phase 2 of the multi-Representative table thread, opened 2026-08-10 on
Mark's instruction.** The thread's purpose, in his framing: Phase 1 was
the strategy to drive the 2–3 Representative table's cost down so it is
affordable to use at all; Phase 2 designs the way to keep the quality at
that lower cost — the four-voice conversation (3 Representatives + the
participant, with the Facilitator) meeting the 1A criteria without
compromising 1B or the program features (three-level transparency, safety
stack, the palette and Goodhart rules).

Everything below is measured against the Voice Rebuild branch
(`claude/cic-voice-rebuild-handoff-fjwrt4`, PR #9 head `f9f22c5`), since
that is the system Phase 2 builds on. PR #9 is open and unmerged; the
five v2 swaps remain PENDING_RECHECKPOINT; Albina's failed v2 checkpoint
sits with Mark. The interference rule therefore remains active — nothing
here touched code, the instrument, the swaps, or the PR.

---

## Q1: Representative change, Table change, or both?

**Answer: overwhelmingly a Table-layer change, concentrated in one file —
`app/prompts/table_discourse.py` — plus an instrument that does not yet
exist. The Representative-side 1A work already carries to the table by
construction.** The brief's working hypothesis is confirmed, with
evidence:

### 1. The 1A assets ride into every table turn automatically [verified in assembly code]

A table turn's prompt is built by the same `build_representative_prompt`
as a solo turn: permanent prompt + world capsule + the rebuilt, sha-
stamped `_HOW_YOU_ENGAGE` block. Since v3 of `table_discourse.py`
(Mark's own call, 2026-07-24/25), the primary-turn conversational core
was folded INTO `_HOW_YOU_ENGAGE` — so the post-1A block, the records,
the palette supply, and the guards are present in every voice at the
table exactly as they are in solo. The Facilitator's table prompts (both
handoffs, reception, bridge) are covered by the 1A `PLAIN_SPEECH` fix.
Nothing Representative-side needs re-doing for the table.

### 2. What the table ADDS is exactly what 1A never touched [measured]

`table_discourse.py` is **byte-identical between main and the rebuild
branch** — the one conversational-design surface the entire 1A pass never
entered. Re-measured independently (my FK/FRE implementation, against
the brief's figures — same verdicts):

| block | words | FK | FRE | avg words/sentence | fires on |
|---|---|---|---|---|---|
| REACTIVE_TURN_GUIDANCE | 1,810 | 14.3 | 47.1 | 30.7 | every reactive turn, every multi-world round |
| OPENING_TURN_LARGE_TABLE_GUIDANCE | 248 | 17.8 | 41.4 | 41.3 | every round-opening turn at 3+ worlds |
| CROSS_WORLD_VOCABULARY_GUIDANCE | 156 | 17.7 | 23.9 | 31.2 | every multi-world turn (dynamic prompt) |

Against the Writing Standard: B2 floor is FK ≤ 10 / FRE ≥ 60, sentence
guard avg ≤ 20. Every block breaches every measure. **At a 3-world table
under the Phase 1 cost shape (round = opening + reactive), 100% of
Representative turns are shaped by a breaching block**: the opener gets
the large-table block, the responder gets the reactive block, both get
the vocabulary block. At a 2-world table the opener escapes (small-table
openings deliberately rely on `_HOW_YOU_ENGAGE` alone — which is post-1A
and clean); the reactive turn does not.

This is the Facilitator defect repeated at worse severity: there, prompts
written at FK 11.3–11.5 taught density by example, and rewriting the
prose moved emitted turns FK 12.4 → 8.37 with every substantive
constraint kept. These blocks sit at FK 14.3–17.8.

### 3. The substance of the blocks is right — and it already teaches the cheap round [read in full]

This is the finding that joins Phase 1 to Phase 2. The blocks' content is
not the problem; read closely, REACTIVE_TURN_GUIDANCE already encodes the
economical table:

- "If what was just said has already answered the participant well, a
  sentence of real agreement in your own vocabulary — and nothing more —
  is a complete turn, **and letting the round end there is a good
  outcome, not a thin one**."
- "Rounds do not all have one shape... Do not treat your turn as a slot
  on a panel where each world files its statement."
- "One open question at the table is enough."

**The cost strategy (A3/A4: short selector-honest rounds) and the
conversation design are the same philosophy.** Phase 1 makes the
economics enforce what the prose already asks for. The rewrite's job is
to keep every one of these constraints — the naming discipline, the
we-voice under personal-feeling exchange, the disagreement shapes, the
participant-in-the-room test, the three-stage manufactured-resolution
guard (line → borrowed frame → borrowed image) — and deliver them in
prose that meets the standard the other voices now live by.

One genuine opening for shortening: several of the block's constraints
now have **runtime detectors** the block predates (S4.6/S4.7:
manufactured_resolution, misattribution, cross-world vocabulary drift,
closing_synthesis, convergence checks). The block cannot shed a
constraint just because a post-hoc detector exists (detectors only queue
guidance for a LATER turn — a failure is spoken before it is caught), but
the S5.2 finding ("guards nearest generation survive attention decay")
argues a shorter, plainer block guards better than a longer one. Where
the block spends hundreds of words teaching a failure mode the runtime
also watches, the rewrite may compress toward the rule and let the
detector carry the tail. This is a judgment call per section, made
visible in the rewrite's diff — not a blanket cut.

### 4. The instrument does not exist [verified against the branch]

The 1A bar is **per emitted turn**, and no emitted table turn of the
rebuilt fleet has ever been measured against it:

- `phase2_checkpoint.py` (the checkpoint instrument) drives solo
  conversations only.
- `s44a_table_battery.py` tests orchestration (who spoke, in what order,
  selector calls); `s47_multiworld_battery.py` tests governance detectors
  on constructed rounds. Neither scores voice quality of live table turns.
- `cross_world_probe.py` proves convergence/divergence across six SOLO
  conversations — the exact logic the table needs, but never applied
  WITHIN one conversation, which is where a table lives or dies:
  accessibility converged, witness diverged, between voices in the same
  round.
- The brief's instrument-gap finding stands: the 8-turn battery is
  adversarial and blind to conversational behaviors (measured: engagement
  demonstrations moved question-endings 0 → 0 in battery while the
  behavior appears in ordinary conversation).

### 5. The residue that is genuinely Representative-side or product-side [small, listed honestly]

- **Layer 2 demonstrations:** no world carries a demonstration of a
  reactive table turn — every demo is solo-dialogue-shaped. Whether this
  matters is an open empirical question (the battery evidence on
  demonstrations is null so far); it goes on the worklist PENDING data,
  not as assumed work.
- **Transparency verified visible at the table:** citations/gloss
  payloads flow per speaker through the shared code path, but worklist
  item 6b's discipline ("verified visible, per world, before swap") has
  never been run against the table UI — and PR #9 itself notes the
  transparency surfaces were never human-rendered. Table-mode
  verification is a work item, likely small.
- **Safety/2A:** relational safety, frame-breaker, epistemology bridge
  run per participant message and are table-aware already (facilitator-
  only turns, no Representative invoked). The adjudicators run per rep
  turn. Nothing changes; the table checkpoint must simply assert they
  fire at the table as they do solo.

---

## The coupled design constraint (Mark's reframe, 2026-08-10)

Phase 2 designs quality **at the Phase 1 cost shape**, not at the current
one. Concretely: the target conversation is a 2–3 world table where a
round is usually an answer plus one real response, rounds end when
nothing real remains, and a third voice enters on a later round when it
genuinely differs. The three quality risks that shape creates, each
measurable:

1. **The differing voice fails to enter.** The selector ends a round
   before a world that would genuinely have objected speaks. THE risk of
   A3/A4 — the measurement is §T2.4 below, and it gates the cost lever.
2. **Turns rush toward comprehensiveness.** With fewer turns per round, a
   voice may try to say everything (the opening block already guards
   this; the guard must survive the rewrite).
3. **Palette variety compresses.** Fewer turns per session = fewer moves
   observed. Session-level diversity metrics still work; they stay
   observational per the Goodhart rule.

---

## The Phase 2 worklist (grain of VR_1A_WORKLIST.md)

**T2.1 — Rewrite `table_discourse.py`'s three blocks to the Writing
Standard.** Substance-preserving, exactly like the Facilitator fix; every
constraint keeps its force, prose meets B2/FK 8–10/FRE ≥ 60, sentence
guard honored; per-section judgment on compressing what runtime detectors
also watch (visible in the diff). App-side only — cleared by the
interference rule ("table_discourse.py never enters the WRS prompt
assembly," verified 2026-08-09, re-verified byte-identical today). Lands
on the rebuild lineage after PR #9 merges. Verify: mock assembly +
readability of blocks, then T2.3's paired arm.

**T2.2 — Build the table checkpoint instrument.** A conversational (not
adversarial) probe set driving the real streaming endpoint at 2-world and
3-world tables, scoring per emitted turn: the B2 hard edge (every voice,
Facilitator included); within-conversation convergence/divergence
(cross_world_probe's logic applied between voices in one transcript —
phrase overlap, vocabulary ownership, FK/FRE spread); deterministic
conversation-shape counters (questions standing open per round,
participant-addressed gap, round shapes used); transparency payloads per
speaker (citations, glosses, name-bridge). Report-only where the 1A
design says report-only; hard where 1A is hard (readability, fabrication
0). Models: `variance_probe.py`, `cross_world_probe.py`, the s44a/s47
harness plumbing.

**T2.3 — Baseline table read (pre-arm).** Run T2.2 against the CURRENT
blocks before T2.1 lands — the pre-1A arm of a blind paired read, same
discipline as the Facilitator fix. Without this, the rewrite's effect on
emitted turns is unmeasurable. Needs a live key; no code changes.

**T2.4 — Round-shape quality measurement (gates the Phase 1 cost
lever).** Same probe set, three arms: status-quo shape (floor 2/max 6),
A3 (max 2), A4 (floor 1, selector-honest). The one question: when a
seated world genuinely differs, does it get in — this round or the next?
Scored by seeded genuine-divergence probes (s47's seeding pattern, live).
This is the measurement that lets Mark choose A3 or A4 with open eyes;
until it runs, the cost target stays A3-not-A4 by default.

**T2.5 — Transparency verified visible at the table.** Item 6b's
discipline extended: pills, citations, repository links rendered per
speaker in the table UI, checked by a human once. Small; product-side.

**T2.6 — PENDING DATA, then MARK: reactive demonstrations.** Only if
T2.3 shows reactive turns missing the shapes the block teaches does a
per-world reactive demo get authored (six worlds, authoring cost). The
demonstration evidence so far is null in batteries; do not spend the
authoring before the measurement says it is needed.

**T2.7 — Sequencing.** T2.2 and T2.3 can run now, from the rebuild
branch, against its own deployed data (all six checkpointed voices are
live there) — no interference with the swaps, Albina's ruling, or PR #9.
T2.1 lands after PR #9 merges. T2.4 wants T2.1 in place first (measuring
round shapes under the old prose measures a system about to change).
The five v2 swaps proceed on their own track and do not touch any of
this — `table_discourse.py` is outside WRS assembly.

---

## What Phase 2 does NOT reopen

The table cap question (3 now, 5 later as a gated research-tier feature)
is a pricing-thread matter, logged in the funding decision log
2026-08-09; the four VR_1A decision documents stand; the Goodhart rule
governs every diversity metric here; emitted is what ships; per-world
failure measures; the sustained bar consults matched_contested.

*Sources: PR #9 (state, body, head f9f22c5), VR_1A_WORKLIST.md and the
four decision documents (rebuild branch), table_discourse.py (both
branches, diffed byte-identical, all three blocks read in full and
re-measured), nodes.py assembly path on the rebuild branch
(_prepare_representative_turn, _cached_system_message,
LARGE_TABLE_THRESHOLD=3), representative_prompts.py
(build_representative_prompt), scripts/ inventory on the rebuild branch
(phase2_checkpoint, variance/cross_world probes, s44a, s47).*
