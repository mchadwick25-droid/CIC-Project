# Church in Conversation
## Table Process — Three Representatives (Four-Party Table)
### Version 1.0

**Governed by:** CiC_L3D_The_Table_Design_Document_V2.3, CiC_L3D_Facilitator_Governance_V3.6.
**Scope:** This document specifies the process for a Table configured with exactly three worlds — the Facilitator and the Participant, in conversation with three Representatives. This is the maximum table size for the Prototype and Phase 1 releases (see Section 7). It specifies what is distinct about turn-taking, drift monitoring, and conversational shape at this table size; it does not restate general principles already covered by the parent documents.

---

## 1. Party Structure

Four parties are present in the conversation proper: the Participant and three Representatives. The Facilitator hosts and governs but does not take conversational turns except at the threshold or on the rare Section 12 triggers.

At every point after the first turn, there are up to two alternative voices to the one who just spoke — the turn-selector's judgment is a genuine three-way (or, once someone has spoken, two-way-among-those-eligible) choice, not the near-binary decision the two-Representative table presents.

---

## 2. Turn Management

**Minimum:** 3 turns per round — the same floor as the two-Representative table: one direct answer (the opening turn) plus at least two further rounds of exchange. At this table size, 3 turns does not guarantee all three voices have spoken; it guarantees only that genuine back-and-forth occurred. This is intentional — Facilitator Governance V3.6 Section 8 is explicit that turn allocation is not rotation and not equal time, and forcing every round to visit all three Representatives regardless of relevance would reintroduce the "everyone states their position" pattern this design was built to avoid.

**Maximum:** 4 turns per round (see Section 6 for why this is capped at 4 rather than higher, despite three voices arguably warranting more room than two).

**Selection guidance specific to this table size:** When the Participant's question is genuinely open to all three worlds ("what do each of you think"), the turn-selector should weight toward bringing in a Representative who has not yet spoken this round over returning to one who has already contributed, all else being roughly equal — this is what lets the Participant "witness the same question received and answered by genuinely different ways of thinking" (Table Design Document Section 8) within the turn budget available. This is a preference, not a rule: a Representative with a real, specific response to what was just said should still be selectable over an as-yet-silent one when the moment genuinely calls for it. The turn-selector prompt's existing "most directly positioned" framing already permits this judgment; this section makes explicit that breadth-of-voice is one legitimate factor among the several the selector already weighs.

**Return visits:** Identical rule to the two-Representative table — no immediate self-repeat, otherwise any Representative may return once something new has been said since their last turn.

---

## 3. Drift Monitoring Scope

All six core signals plus all five multi-world signals apply, as at the two-Representative table. Two additional considerations at this table size:

- **Dominance** is measured as cumulative word-share across the whole conversation, not just the current round (see `check_dominance`). With three voices, the 65% single-Representative threshold is reached faster in absolute terms if two voices are quiet, so this check is at least as important here as at the two-Representative table, not less.
- **Competitive recruitment drift** (a Representative positioning against the others rather than witnessing its own tradition) has more surface area to occur with three voices than two, since there are more pairwise relationships in which it could arise. No additional mechanism beyond the existing signal is specified here; this is named as something to watch in live review.

---

## 4. Conversational Shape

With three voices and a 3-4 turn budget, most rounds will not include all three Representatives every time, and that is by design (Section 2). A round might run A → B → A, entirely excluding C, if the question was specific enough that C's formation had nothing distinct to add — this is a correct outcome, not a failure, per the Table Design Document's own instruction that "a round does not need to include every representative every time."

The reactive-turn guidance (naming what was actually said, agreeing before diverging, asking rather than only answering) applies at full strength regardless of which two (or all three) voices are active in a given round.

---

## 5. Cost and Latency Profile

Per round: up to 4 representative-generation calls (each preceded by its own retrieval pass), up to 4 turn-selector calls, one dominance check, one convergence check, and the standard facilitator-monitoring pass — the same shape as the two-Representative table, since the cap is on turns, not on representatives present. The per-call cost of the turn-selector is marginally higher here (more candidates to reason about per prompt), and full-round latency for three Representatives ran roughly 60-90 seconds in live testing at the 4-turn cap.

---

## 6. Known Limits — the Turn-Cap Incident

This table size was where the round-length reliability issue was actually found and diagnosed, so the record belongs here in full.

Live testing initially used a 6-turn maximum. At that length, later turns in a round began truncating mid-sentence or returning completely empty. Diagnosis (isolated script reproduction, direct HTTP testing against the running server, and raw API response inspection) found two compounding issues:

1. **Cumulative round latency.** A 6-turn round at this table size chains 15+ sequential API calls (turn-selector plus generation per turn, plus dominance/convergence/monitor checks), running 90+ seconds end to end in a single streamed HTTP request. The turn cap was lowered to 4 as a mitigation.
2. **Extended-thinking token-budget interaction (the actual root cause of truncation, found after lowering the cap did not fully resolve the symptom).** The underlying model was found to emit an interleaved extended-thinking content block on every reactive (token-capped) call by default, with unpredictable length. When that internal reasoning ran long, it consumed most of the reactive turn's token budget before any visible answer text was written, causing the visible response to hit the cap and cut off — sometimes with no visible text at all. This was confirmed by inspecting raw response chunk types across repeated trials (a `thinking` block was present in every trial; its size, not the visible text, correlated with truncation) and fixed by explicitly disabling extended thinking (`thinking: {"type": "disabled"}`) on every token-capped call. Eight consecutive trials after the fix completed cleanly with no thinking block and no premature truncation.

**Re-tested 2026-07-13, cap restored to 6.** A separate integration pass re-verified the 4-turn cap against the original 6-turn ceiling with the thinking-disable fix in place, per this section's own recommendation. Two live three-world-table trials: one ended naturally at 4 turns (the selector chose to close the round, not a cap being hit); a second was pushed to the full 6-turn ceiling and completed cleanly — all six turns substantial (1,800–2,400 characters each), no truncation, no empty responses, no error events across the round. `MAX_MULTI_WORLD_TURNS` in `cic-poc/backend/app/main.py` has been restored to 6. This is a lighter-weight re-test than the eight-trial verification that confirmed the original thinking-disable fix itself (two trials here, not eight) — reasonable given it is re-confirming an already-fixed mechanism at a new ceiling, not diagnosing a new failure mode, but a further round or two of testing would still strengthen confidence before treating 6 as load-bearing for production traffic. Full round latency at the 6-turn cap ran approximately 150 seconds end to end in this test, up from the 4-turn cap's ~60–90 seconds — a real cost, not a reliability problem, and worth weighing against the value of a longer round when deciding whether 6 is the right default going forward.

---

## 7. Table Size Ceiling — Prototype and Phase 1 Scope

CiC_L3D_The_Table_Design_Document_V2.3 Section 2 specifies a design ceiling of five worlds per table. For the Prototype and Phase 1 releases, the project lead has set the operative ceiling at three worlds, not five, to keep cost and conversational complexity manageable while the turn-management mechanism described in this document family is still being validated live. This is a scope decision for the current implementation phase, not a revision to the design document's own ceiling — CiC_L3D_The_Table_Design_Document_V2.3 Section 11 (Phase Implementation) already anticipates Prototype Alpha operating at "one to three worlds"; this document extends that same three-world ceiling through Phase 1 as well, ahead of any future phase where the full five-world ceiling might be revisited.

---

## Constitutional and Design Grounding

This document specifies implementation detail within the scope already granted by CiC_L3D_The_Table_Design_Document_V2.3 Sections 2-8 and Facilitator Governance V3.6 Sections 8 and 10. It introduces the concrete minimum (3) and maximum (4) turn counts per round for this table size, the breadth-of-voice selection preference in Section 2, and documents the turn-cap/extended-thinking incident as the empirical basis for the current maximum. It also records, in Section 7, the project lead's scope decision capping table size at three worlds through Phase 1, distinct from the design ceiling of five that CiC_L3D_The_Table_Design_Document_V2.3 specifies for the completed vision.
