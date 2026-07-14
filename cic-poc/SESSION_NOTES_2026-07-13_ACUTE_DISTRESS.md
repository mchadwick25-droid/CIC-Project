# Session Notes — 2026-07-13, Acute-Distress/Harmful-Dynamic mechanism implementation

**Branch:** `claude/cic-poc-acute-distress-mechanism`, based on `claude/cic-poc-backend-facilitator-upgrade` (commit `b29f421`).
**Remote:** `origin` → `https://github.com/mchadwick25-droid/CIC-Project.git`

Scope of this branch is strictly `cic-poc/` and this notes file, same discipline as the branch it's based on. `World-Builds/`, `L1-Foundation/`, `L3B-World-Build-Methodology/`, `L3C-Representative-Methodology/`, and `L3D-Encounter-Methodology/` were not touched, committed, or pushed from here — this branch's checkout of those files is stale relative to `claude/vigilant-babbage-a04f38` (the content-review branch, which has since applied real fixes on top), and that staleness is deliberately not carried into any commit made from this branch.

**Design source, read in full before writing any code:**
- `CiC_L3D_AcuteDistress_HarmfulDynamic_Mechanism_Proposal_DRAFT.md` (repo root)
- `CiC_L3D_RelationalSafety_ResourceNaming_Decision_Options.md` (repo root)
- The corrected-design live test transcript: `World-Builds/01-Post-Apostolic-House-Church/CiC_W1_Phase5_RelationalSafety_LiveAdversarialTest_CorrectedDesign_Round1.md` (read via `git show origin/claude/vigilant-babbage-a04f38:...` without switching branches, since this branch's own working copy predates that file)

## The two decisions this mechanism depends on — already resolved, not re-litigated here

Both decisions the design doc reserves to the project lead (CO-022) were already made and corrected earlier in the same session that produced the design doc, **not** the original recommended defaults:

1. **Resource-naming: none of Options A/B/C adopted.** No resource is named, no course of action is suggested. The project lead's own words, quoted in `CiC_L3D_RelationalSafety_ResourceNaming_Decision_Options.md`: *"i dont want to be suggesting solutions, we are not a clinic, a pastor or a resource center... we may pause for a check-in if needed, but not an intervention."*
2. **Routing: strict decoupling, not the doc's original §4.3a dual-presence default.** The Representative never sees the triggering message once a track fires — Facilitator alone speaks. Project lead's own words: *"the user doesn't need two voices responding. it is an interuption to the conversation."*

This implementation follows both corrections. It does **not** implement the doc's original (superseded) §4.3a/Option C design.

## What was built

Same classify-then-route-then-generate architecture as the frame-breaker mechanism (`classify_frame_breaker`/`stream_frame_breaker_response`), reused deliberately rather than reinvented:

- **`app/graph/state.py`**: session-level accumulator fields — `track_a_active`, `track_a_severity` ("A1"/"A2"), `track_b_active`, `relational_safety_tags` (list), `relational_safety_deescalation_count`.
- **`app/prompts/facilitator_prompts.py`**:
  - `FACILITATOR_RELATIONAL_SAFETY_CLASSIFIER_PROMPT` — the 5-way taxonomy (NO_SIGNAL, HISTORICAL_OTHERNESS_DISORIENTATION, ACUTE_DISTRESS[:A1/A2], HARMFUL_DYNAMIC_SIGNAL[:tag], AMBIGUOUS_LOW_CONFIDENCE[:tag]), with the design doc's own worked contrastive examples reproduced verbatim, including the explicit anti-false-positive rule (turn count/session length/"I want to keep exploring" must never by themselves trip a signal).
  - `FACILITATOR_ACUTE_DISTRESS_A1_PROMPT`, `FACILITATOR_ACUTE_DISTRESS_A2_PROMPT`, `FACILITATOR_ACUTE_DISTRESS_CONTINUATION_PROMPT`, `FACILITATOR_HARMFUL_DYNAMIC_PROMPT`, `FACILITATOR_HARMFUL_DYNAMIC_CONTINUATION_PROMPT` — template-anchored (§4.5's recommended default, not the fully-generated alternative), built directly from the corrected-design transcript's own final wording (including the A2 cold-review addition: one bare, non-directive "is there someone you could reach tonight" question, no resource named).
- **`app/graph/nodes.py`**:
  - `classify_relational_safety(state, message)` — the classifier call, same fail-open-to-NO_SIGNAL discipline as `classify_frame_breaker`'s fail-open-to-False.
  - `update_relational_safety_state(state, classification)` — pure logic, no LLM: Track A firing/escalation (severity only ratchets up, never down, within a session), Track B's accumulator and threshold (2 pooled CONFIDANT_LANGUAGE/AFFIRMATION_DEPENDENCE tags, or 1 RETURN_COMPULSION, per the design doc's own stated starting threshold), and de-escalation (this implementation's own calibration choice — 2 consecutive NO_SIGNAL turns while a track is active clears it; the design doc doesn't specify a number, so this is disclosed as unvalidated, not silently assumed).
  - `relational_safety_should_fire(...)` — decides whether the current turn routes to the Facilitator instead of the Representative, covering both fresh-fire and sustained-attention (§4.4) cases.
  - `stream_relational_safety_response(...)` — selects and streams the right template based on category/severity/fresh-fire-vs-continuation.
- **`app/main.py`**: wired into both `/message` and `/message/stream`, immediately after the frame-breaker check (frame-breaker takes priority on any overlap — it's the already-tested mechanism). Same withholding discipline: the Representative is structurally never invoked on a firing turn.

## What was NOT done — testing status, disclosed plainly

**No live testing has been run against this implementation.** This checkout has no `.env`, no working Anthropic API credentials, and (at commit time) no installed dependencies — none of that is available in this branch's environment. What's here is:

- Syntax-checked (`py_compile` clean on all five modified files).
- Architecturally reviewed against the design doc and its corrected transcript by the implementer, but not executed.

**Not done, and required before this can be trusted in any live session, per the design doc's own §7 and Section 15 Known-Limits framing:**
- The classifier's sharpest distinction (`HISTORICAL_OTHERNESS_DISORIENTATION` vs. `ACUTE_DISTRESS`) has never been run against a live model with this exact prompt text.
- The design doc's own 7 trials (from the corrected-design transcript) have not been re-run as actual API calls — they were hand-traced against the specification, not executed.
- The anti-false-positive rule (long/curious conversation should never trip Track B) has not been exercised live.
- De-escalation's 2-turn threshold (this implementation's own choice, not the doc's) has not been calibration-tested at all.
- The A2 severity-escalation path (A1 fires, then a later turn escalates to A2 within the same session) has not been exercised live.

**Handoff:** per the project lead's direction, live adversarial testing of this branch will be run from a separate, already-credentialed session (the one that ran and verified the frame-breaker classifier tonight, 12/12), rather than provisioning new credentials into this checkout. That session should: pull this branch, restart both servers clean, run the design doc's own worked contrastive examples plus adversarial variants (direct API calls, not casual click-through), confirm the accumulator doesn't false-positive on long/curious conversation, and confirm de-escalation actually clears `track_a_active`/`track_b_active`. Results should be folded back into this notes file or a dedicated test-results file before this mechanism is marked validated.
