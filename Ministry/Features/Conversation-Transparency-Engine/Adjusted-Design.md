# Adjusted, Opus-Compliant Design

Adjusts the converged synthesis (three parallel Fable research threads:
Library & Build, Conversation/Transparency Engine, Facilitator) against the
Opus adversarial review and the live tree. This is the converged-with-
adjustments design, not a rewrite. Phase: convergent on the engineering
items; divergent-with-recommendation on every governance item in `Rulings-
Pending.md`, which Mark rules on one at a time.

Reviewable summary published as an Artifact:
`https://claude.ai/artifact/N8jiwbkB7kqsdH1jiq8622`

**Read `Decision-Log.md` entry 3 before treating anything below marked
S1, S2, or item 16–20 as open.** Written before Mark's 2026-09-19 scope
correction, this document still lays out the Facilitator-safety options
as live design choices. They aren't. Mark's ruling closed them as
resolved: the mechanism is a single fixed step (signal → check in →
encourage seeking real human help), not open design space. What's below
in §3's "Safety" and "Facilitator" subsections is historical record of
the reasoning that led to that closure — not a menu Mark or a build
thread should still be picking from.

## 0. Ground truth this design stands on (verified in the tree)

- The three live safety fixes are merged (`1c522e918`): `engine/m5/failure.py`
  routes on safety alone when the reader fails and safety is decisive;
  `engine/m4/crisis_resources.py` `ACUTE_DISTRESS_CONTINUATION` now carries
  the redirect sentence; `engine/prose.py` excludes `do_not_retrieve_when`
  from `_NON_PROSE_KEYS`. 567 tests pass; `engine.m1.cross_world` and
  `engine.m9.enforce` clean. The `already_fired`-always-wins rule in
  `resources_for_signal()` is untouched and explicitly open (→ R2).
- The D1 residual is **structural, not a missing exclusion**: the Brictio
  story's own `text` contains "Brictio", "Martin", "bishop", so a
  fabricated "Brictio succeeded Martin as bishop" still scores 0.80 on
  `grounding_ratio()` against `WITHHOLD_FLOOR` (0.40). No exclusion list can
  close that. The net verifies *vocabulary provenance*, not *propositional
  truth*. This reframes items 1–3 and the system-nature promise (N3).
- `check_turn()` in `engine/m4/grounding_net.py` has two pass paths a
  fabrication can ride: the ratio path (needs a proper-noun/number/
  enumeration marker, floor 0.40) and the "tag is the claim" path (no
  marker: passes on *one* shared content word). §4's measurement reports
  both separately.
- Record status: **1,917 `status: draft`, 26 `status: ready`** fleet-wide;
  all 26 `ready` are in `records/fix` (25) and `_fleet` (1). Every record
  in every real world is draft. Nothing in `engine/` reads `status` except
  the schema enum. D11 confirmed (rzg added since Opus counted 1,809).
- `voice_turn` `REQUIRED_KEYS` = `{speaker, text, citations, glosses,
  figures_used, quote_offers, attempts_meta, output_defects}`
  (`engine/m4/events.py:33`). A new `transparency` key is purely additive.
  Transcript replay (`_replay_text` in `engine/api/wiring.py`) rebuilds
  history from `citations` only, so a plan stored beside `citations` cannot
  disturb session memory.
- The frontend has **no test runner** (`package.json`: dev/build/lint/
  preview only); CI's only frontend coverage is `docker-build` running
  `npm run build`. `VoiceTurnBody.tsx` is the only untested logic in the
  pipeline.
- Two sealed Haiku gate calls run sequentially in `run_gate()`
  (`engine/m4/turn.py:119-122`), 4s timeout each, `recent_window=[]`,
  `accumulator={}`.
- Table round cap is 3 (`engine/m4/round.py:205`); `TableRoom.tsx:144` says
  five (Opus #9). "Leave for now" is `disabled={disabled}` in
  `ChatInput.tsx:73`; wrappers pass `isLoading` (Conversation) /
  `isLoading || roundOpen` (TableRoom) — Leave is dead during every
  in-flight turn in both modes (Opus #8).
- Logged live corpus available at zero model cost: **36 turns / 546
  sentences / 55 withheld / 346 ok-tagged / 125 with a ratio** across
  `engine/m4/reports/live-turn-report-*.json` and `live-table-*.json`, each
  sentence carrying verdict, tags, ratio, reason.
- `do_not_retrieve_when` appears 828 times in `records/`;
  `_FALLBACK_EXCLUDED_KEYS` in `evidence.py` already excludes it from
  Stage A2.
- Safety model resolves from pattern `us.anthropic.claude-haiku-4-5` via
  `resolve_model_id()` (exactly-one-match; a same-id revision underneath
  would not be noticed). Battery runs live in numbered batches
  (`engine/m5/reports/safety-script-run-1..8.json`); no single all-batches
  tally exists.
- Golden sets exist for 6 of 10 worlds (`engine/m4/reports/bench/`: alx,
  desert, hal, ijc, pahc, syr). cappadocian, don, gallic, rzg have none,
  against Completion Standard §B.

## 1. The two hard constraints, made operational

**Constraint A — no added per-turn cost for the ordinary turn.** Admissible
only if, on a non-crisis, non-failure turn, an element adds: zero model
calls, zero network calls in the critical path, zero new reads of retained
state the turn does not already load, no increase to the evidence-block or
prompt budgets already in force. Deterministic string work over data
already in memory (`history`, `SessionState`, the compiled package) is
fine. Behavior that changes only inside an already-rare branch (safety
fire, check-in follow-up, call failure) is fine. One-time build-time spend
is fine. Retrieval tuning that changes *which* records fill *existing*
slots is fine, subject to the bench.

**Constraint B — modularity.** The Library report's three seams are the
house rule: Library → Build (shelf, holdings), Build → Package (schemas,
compiled artifacts), Package → Engine (`assemble_evidence` signature
stable; new information as new keys). Fourth seam, already implicit:
Engine → UI (`voice_turn` additive keys only; UI renders, never
re-derives). Facilitator rule: the sealed classifier's inputs change only
by a named decision with a battery rerun.

## 2. Struck items

| Struck | Source | Why |
|---|---|---|
| **Shared "recent-turns window" between retrieval and safety** | Synthesis §2 bullet 2, §1 runtime sentence | Opus D6 / blocking fix #3: welds the sealed classifier to retrieval tuning. |
| **Item 16 — windowed safety classifier** | Synthesis §4; Facilitator §3.2 B | Constraint A: a window on *every* turn adds input tokens to every sealed call and changes its input shape on every turn (full re-cert, rewritten corpus). Standalone twin of D6. Zero-ordinary-cost replacement offered as R3. |
| **Runtime embeddings as a retrieval tier** (Library Options A/B; CE Stage B3) | Library §3.3; CE §3.5 | Constraint A: a query embedding is a network call inside every turn. Compile-time Option C and deterministic `retrieval.json`/BM25 survive. Embeddings return only as a named change order. |
| **"N sentences could not be checked" as a displayed element** | CE §3.3; item 3 | Opus D3: `apply_net`'s own measurement (25% withheld, 39% of those honest prose) means the count mislabels honest prose. Struck as designed; reconsidered only after §4 with a false-positive rate Mark has seen. May be *computed* for M7; may not render. |
| **"Streaming can move earlier if wanted"** | Synthesis §5 step 5 | Opus D2 / fix #4: blocked behind item 19, full stop. |
| **§2 framing "one gap wearing two costumes"** | Synthesis §2 | Two differently-shaped mechanisms with different certification regimes. Retrieval-side conversation awareness survives alone (reads `history` already in memory). |

## 3. The decision list, reconciled

Legend: KEEP / ADJUST (driver cited) / STRIKE / BLOCKED / RULING (options in
`Rulings-Pending.md`). Engineering items the reports or Opus already
settled get a stated resolution.

### Safety
- **S1** — KEEP as governance; RULING R1. D4 changed the adjacent case, not
  this one: a *safety* timeout still routes to the voice with no directive.
- **S2** — ADJUST. D5 content fix live; Opus fix #5 open. RULING R2. Folds
  in: (a) the interim continuation text was drafted by the fix thread and
  lacks Mark's word; (b) the "a moment ago can mean days" decay (W7) is the
  same rule.

### Confidence & honest transparency
- **1** — BLOCKED (Opus §2/fix #1; D11; D8). Design kept (hollow glyph, no
  new color or verb). RULING R9 after §4, R16, R17.
- **2** — BLOCKED on the same plus item 4. CE candidate wording is the
  draft for Mark.
- **3** — ADJUST: both options off the table today; inline already not
  recommended, count struck per D3.
- **4** — RULING R8. Recommend: "Not Attested" is the disposition of an
  *absent* claim (`honest_limit`/`absent_detail`/`kind: absence`), not a
  `formation_confidence` level; amend CLAUDE.md's sentence.
- **5** — ADJUST, D1 raised the stakes. Resolution: split
  `do_not_retrieve_when` into `retrieval.prefer_instead` (redirect) and
  envelope `claim_guards: [{claim, note}]` (guard); category guards fold
  into `false_friend`/`modern_contrast`. Guards render as a rider on the
  candidate line **inside the existing evidence budget** (upstream
  prevention — the mechanism that actually works); `claim_guards` goes into
  `_NON_PROSE_KEYS` and `_FALLBACK_EXCLUDED_KEYS` *before* any record
  carries it. Schema change → one-line confirm R11, not a groan zone.

### Marking & citation grammar
- **6** — RULING R10 (Mark ruled this surface twice: 2026-08-25,
  2026-08-30). The plan carries both `run_start` and `run_end` anchors so
  the renderer choice is a flag.
- **7** — Resolved: yes, complete list, collapsed behind one line. Label
  text is Mark's; propose with the renderer.
- **8** — Resolved: yes (honours the 2026-08-30 ruling; foreign/technical
  fire on sight; ordinary-English forms citation-gated). `gloss_forms`
  additive; the authoring rule is a template edit → flagged when it
  happens.
- **9** — Resolved: keep per-world; build nothing. No ruling needed.

### Retrieval & library
- **10** — Resolved: wire `tier` as a small Stage-B prior behind
  no-regression on all ten golden sets (four written first). Do not
  rename.
- **11** — ADJUST per A: `retrieval.json` + compile-time Option C approved
  in principle; runtime embeddings struck; conversation-aware and
  return-turn queries survive on bench + live-table no-regression.
- **12** — RULING R12, one line. Recommend live provenance resolution
  only; fix the topology sentence.
- **13** — RULING R13, one line. Recommend report-only one cycle, then
  blocking for new worlds with m9-shaped waivers.

### Build process & content
- **14** — RULING R6. ADJUST folding Opus #6 and #7: the 2×-exemplar
  threshold catches only gallic (don at the margin) of four drifted
  worlds; and the project holds a real tension — `gate_readability`
  already gates FK ≤ 10 in the CI-blocking battery while the Register Bar
  doc and Completion Standard §B say "no number gates" the register-bar
  *read*. Resolution to propose: absolute per-field ceilings from the
  Register Bar's own properties (sentences mostly under ~20 words;
  `tellable_as` is a phone-width title); exemplar comparison becomes an
  observation. Whether `register-profile` gates or advises is N4.
- **15** — RULING R7, blocked on 14.

### Facilitator
- **16** — STRIKE (§2). Replacement R3: *conditional* context only on the
  turn after a check-in (optionally after a Track A fire), from the
  transcript already in memory; empty window on ordinary turns as today.
  Still changes the sealed input shape on those turns → windowed battery
  batch authored before any call.
- **17** — RULING R4. Add the mode inconsistency; recommend the voice
  never sees Facilitator turns in either mode (a voice reading "crisis
  line or other real human support" in its own history is the don/rzg
  defect class).
- **18** — ADJUST: split. "Leave never disabled" = Opus #8, just fix (both
  modes). The round interrupt changes Mark's 2026-08-29 round design →
  RULING R5.
- **19** — RULING R14. Now explicitly gates item 21 (Opus #4). The
  deterministic check is string-only, zero cost, buildable report-only
  now.
- **20** — RULING R15. `risk_subject` already routed; only the text/choice
  is open.

### Engineering priority
- **21** — ADJUST per D2: BLOCKED on R14 and Stage 3. Concurrent gate calls
  separated out and go now.

### New items
- **N1 (D11)** — RULING R16. Confidence display cannot ship while the data
  calls its records unfinished.
- **N2 (D8)** — RULING R17 on numbers; mechanism is engineering: an M7
  instrument counting Level-1 elements per turn, a renderer fixture test
  asserting the cap, and a house rule — *no new Level-1 element kind
  beyond the (possible) quiet Contested variant; all confidence language
  at Level 2/3; riders never reach the UI; the unverified count never
  renders.*
- **N3 (D1 + W10)** — `SYSTEM_NATURE` (`engine/m4/facilitator_turns.py:
  65-75`) says "every specific claim in it is checked against the record
  it came from; what it can't ground, it's built to tell you it doesn't
  have." The mechanism checks vocabulary provenance and silently drops a
  mark. RULING R18; recommend reword now.
- **N4 (Opus #7)** — RULING R6b, with item 14.
- **N5 (W8)** — Resolved: one command runs every batch and prints one
  tally; model id pinned by env var to the full inference-profile id;
  tally re-run and committed on every prompt/input-shape edit.

## 4. The D1 measurement — methodology (Opus blocking fix #1)

Purpose: a number for "how often can the check be fooled by a plausible
fabricated claim, and how often does it withhold honest prose." Zero model
calls required; one optional one-time labeling pass.

**Corpus A — real logged turns.** 36 turns / 546 sentences from the m4
reports. Re-run `check_turn()` against current packages (verdicts should
reproduce, shifting slightly for guard-bearing records post-`prose.py`
fix). Label all 55 withheld + ~120 stratified ok-tagged (by world and pass
path): *is this sentence actually supported by the record(s) it tags?*
Output FP rate (withheld but supported), FN rate (ok but unsupported), by
path and record type. One-time Sonnet labeling with Mark spot-checking 20.

**Corpus B — constructed fabrications (deterministic).** For every
guard-species `do_not_retrieve_when` line ("does not say", "must not
supply", "not attested", "do not invent"), every `honest_limit.statement`,
`contested_claim.claim`, story `absent_detail`: build the barred
proposition as a flat assertion tagged to that record (template first;
optional one-time Sonnet phrasing). Run `check_turn()`. Fooling rate by
path and world; list every record whose barred claim passes. Brictio is
row one.

**Corpus C — the one-shared-word hole.** Pair sampled records with a
sentence from a different record in the same world sharing exactly one
content word and no proper noun; tag to the wrong record; measure passes
on the "tag is the claim" branch.

**Deliverable.** `engine/m4/reports/grounding-fooling-<date>.json` + plain
write-up with the structural statement: provenance, not truth; mitigations
are upstream (riders, guards, honest-limit records) and reporting; any UI
element implying per-sentence truth verification overclaims. No thresholds
self-set; numbers go to Mark as an Artifact.

## 5. Revised build sequence

**NOW (self-governing):** Stage 0 hygiene (concurrent gate calls; Leave
never disabled; round cap exposed by API; battery tally + model pin;
`observe_outside_help_guard`). Stage 1 D1 measurement. Stage 2 Library/
build foundations (`spoken_fields.py` + AST seal; `bar_screen`;
`register-profile` as OBSERVATION; holdings report report-only; four
golden sets). Stage 3 engine half (`transparency_plan.py`, completeness
invariant, confidence data computed not rendered, `world_key`; renderer
built against fixtures, switched on after R10 + label copy). Stage 4 most
of it (`retrieval.json`; Stage B2; tier prior behind bench; exclusion-list
hygiene; report-only `guard_proximity` and `safety_boundary` families).

**BLOCKED PENDING STAGE 1:** items 1, 2, 3; any rendering of confidence or
verdicts (Stage 6); any `WITHHOLD_FLOOR` change; any reconsideration of the
count.

**BLOCKED PENDING MARK:** S1 (R1), S2 + decay + interim text (R2), item-16
replacement (R3), 17 (R4), round interrupt (R5), 14 + N4 (R6), 15 (R7), 4
(R8), 1 (R9), 6 → renderer switch-on (R10), 5 split → migration (R11), 12
(R12), 13 (R13), 19 → streaming (R14), 20 (R15), N1 (R16), N2 numbers
(R17), N3 copy (R18), per-world voice_craft guards (R19).

**Order once unblocked:** 5 (safety, own timeline, never bundled) → 6
(confidence display) → 7 (streaming) → 8 (table interrupt/return-turn) →
9 (fleet `tellable_as` cleanup).

Full ruling text (options + recommendation, one at a time) is in
`Rulings-Pending.md`. Full stage-by-stage build instructions are in
`Build-Plan.md`.
