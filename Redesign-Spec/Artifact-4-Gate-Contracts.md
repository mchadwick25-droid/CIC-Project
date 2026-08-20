# Artifact 4 — The Facilitator Gate: Contracts, Timeouts, Failure Semantics

Companion to `CiC-Program-Spec.md` (Stage 0.5.4). One pass, two calls: the sealed safety call and the unified reader, run concurrently. Both are small monitoring-tier model calls (Haiku-class), `max_tokens` sized to the schema, structured output enforced.

## 1. Call A — safety (SEALED)

Never shares a prompt, code path, or deploy with anything that gets iterated on. Any change to it triggers the full live safety rerun (19/20 floor). Input: the participant message + the narrow recent window + the persisted accumulator (from `safety_state`).

```json
// output schema (all fields required)
{
  "signal": "NO_SIGNAL | HISTORICAL_OTHERNESS_DISORIENTATION | ACUTE_DISTRESS | HARMFUL_DYNAMIC_SIGNAL | AMBIGUOUS_LOW_CONFIDENCE",
  "acute_level": "none | a1 | a2",
  "dynamic_tags": ["CONFIDANT_LANGUAGE","AFFIRMATION_DEPENDENCE","RETURN_COMPULSION","DISTRESS_ADJACENT"],
  "confidence": "high | medium | low"
}
```

`acute_level`: a1 = distress/passive ideation; a2 = plan or intent. Both route identically (Facilitator safety turn, resources appended by code); the level is recorded for audit priority. Standing rules carried: engagement length/depth/turn count NEVER increment the accumulator; historical-otherness disorientation is the encounter working; crisis resources are appended by code, never asked of any model.

## 2. Call B — unified reader

```json
// output schema (every field ALWAYS filled — a box per dimension; nothing competes for one slot)
{
  "asks": [ { "order": 1, "text": "how a person became one of you" } ],      // 1..n, participant's own framing
  "register": "informational | evidential | personal_wound | translational",
  "clarity": "clear | ambiguous",
  "ambiguity_options": [],            // non-empty iff ambiguous — feeds the voice's in-world clarifying question
  "out_of_scope": { "class": "none | system_nature | later_age | other_tradition" },
  "modern_terms": [ { "term_id": "_fleet.modern.sola-fide", "display": "faith alone" } ]
}
```

`pressed` is NOT a model output: code computes it from the event log (`escalation_pressed` events and prior `gate_decision`s) and merges it into the routing decision — the model never guesses history.

## 3. Routing (deterministic merge, in priority order)

1. `safety.signal ∈ {ACUTE_DISTRESS, HARMFUL_DYNAMIC_SIGNAL}` → Facilitator safety turn (immediate, no ladder); Track A/B behavior per spec §8; message withheld from the voice while safety has the floor (with Mark's empathy-routing nuance as specified).
2. `out_of_scope.class == system_nature` → Facilitator answers plainly, immediately: "we use AI to …".
3. `modern_terms` non-empty and anachronistic for this world (computed from the registry time window) → bridge: Facilitator frames; voice receives the term-free `underlying_subject`.
4. `out_of_scope.class ∈ {later_age, other_tradition}` and `pressed == false` → pass to voice (in-world first answer); `pressed == true` → Facilitator etic explanation.
5. Otherwise → pass to voice with the **private directive**: asks in order, register note (personal_wound ⇒ witness-before-answer license; register statement 1 suspended for the turn), ambiguity options if any.

The directive is assembled by code from the schema — never free-composed by a model (corrections-selected-never-composed, generalized).

## 4. Timeouts and failure semantics

- Budget: both calls dispatched concurrently; **p95 ≤ 2.5 s, hard timeout 4 s** each.
- **Reader fails/times out** → pass-through: the voice answers the raw message with no directive (the pre-guard state); `gate_decision.degraded = true`; turn flagged for priority audit.
- **Safety call fails/times out** → the turn proceeds (fail open toward the pre-guard state — the ruled direction), AND: `degraded = true`, the message is re-classified async immediately after; if the retro-classification fires acute, the Facilitator interjects on the next event with the safety turn and resources. This is the stated answer to "a gate failure is a safety question": the participant is never blocked by our failure, and the failure is never silent.
- **Both fail** → plain pass-through + audit flag; two consecutive degraded turns page the operator (Artifact 6).
- Structured-output parse failure = failure (no salvage parsing).

## 5. Deploy discipline

Gate prompts/models are versioned artifacts; changes roll out **canary-first** (a cohort of new sessions) before 100% — the gate is a deliberate fleet-wide single point, so it gets staged rollout and one-line rollback. Reader changes re-run the reader battery (compound/ambiguity/wound fixtures); safety changes re-run the live safety script. Cost envelope: ~$0.003/turn for both calls combined at current prices.
