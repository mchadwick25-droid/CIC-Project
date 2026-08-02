# Build Scope — Cost Reduction, from the Funding Strategy Thread's Cost Study Arc

**Dispatched 2026-08-02.** Confirmed direction from live work in the Funding Strategy thread —
two research passes (`CiC_Cost_Study_Per_Transaction_V0_1.md`,
`CiC_Cost_Reduction_Feasibility_Study_V0_1.md`, both in `Ministry/Features/Funding-Strategy/`)
plus real decisions made live with Mark. This thread's own launch brief keeps it out of
`cic-poc`/`cic-website` code — this is the handoff to wherever that build actually happens.

**The constraint driving all of this:** if blended cost can't come down from ~$2/hour toward
~$0.50/hour, the funding model doesn't work at the already-validated giving amounts. The
feasibility study found $0.50/hour is reachable for 1:1 conversation through the items below,
before touching anything speculative. Living Table remains structurally 2–3× that regardless of
these fixes — a separate, already-logged product decision (table size, not time, gates the free
tier) handles that, not an engineering fix.

---

## Item 1 — Cache TTL fix (lowest risk, do first)

Three `cache_control` sites in `graph/nodes.py` (the static prompt, the reactive-turn guidance
block, the adjudication prefix) currently use the bare 5-minute ephemeral default. Switch to
`{"type": "ephemeral", "ttl": "1h"}` — GA, no beta header, no behavioral risk (this only changes
billing/latency, never what the model produces, confirmed in the feasibility study).

Also: `repair_adjudication` (`graph/repair_classifier.py:226`) builds a plain `SystemMessage`
instead of using the `_cached_adjudication_message` helper its two siblings already use — same
fix, one more site.

**Directly measured impact:** takes a reflective-pace (6 turns/hr) 1:1 conversation from
$0.77/hour to $0.50/hour on this change alone.

## Item 2 — Response-length regeneration bug

A world's draft response exceeding its length ceiling triggers a full second Sonnet generation.
Root cause: no deployed prompt states the actual numeric word limit — the model only learns the
real number after already breaking it, on the retry. Affects most or all six worlds, not just
Desert (the two that measured 0% were added to the ceiling list after the measurement run — a
documented artifact, not a clean result).

A remedy is already scoped with real options and risk analysis:
`S6.2_length_ceiling_retry_cost_investigation_2026-07-31.md` §5. **Needs live battery testing
before shipping** — the leading option (an in-voice exemplar at the ceiling) has a real parroting
risk this project's own prior testing flagged as a live concern, not a hypothetical one. Re-run
the cost baseline with `length_ceiling_logging.py` active (built for this, never yet produced a
production record) to get real fire rates across all six worlds before deciding which option to
ship.

## Item 3 — Answer Bank: inference-based semantic matching, hidden auto-serve

**Real decision, made live, overriding a prior one:** the existing design doc
(`Ministry/Features/Guided-Questions/CiC_Answer_Bank_Full_System_Design_V0_1.md` §3.4)
recommends against inference-based serving matching, on values grounds. Mark has explicitly
rescinded that recommendation — inference-based matching is now the confirmed direction, not a
ruled-out option. **That document still states the old recommendation in writing** — needs a
dated correction note there (don't rewrite the history, add what changed and why, same convention
as every other correction in this project), whenever the Guided-Questions thread is next active.

**What to build:**
- A per-world semantic index over a curated bank of canonical questions and answers, using the
  local embeddings and retrieval infrastructure already running in `rag/` (confirmed reusable —
  zero API cost). The existing cross-encoder reranker is mechanically reusable but was calibrated
  for a different task (passage relevance, not question-paraphrase equivalence) and needs its own
  calibration pass for this use, not a direct reuse of its existing threshold.
- **Auto-serve, hidden.** No participant-visible indication that a match occurred, a suggestion
  exists, or an answer might be prepared rather than live. `answer_bank.py`'s existing
  `stream_answer_bank()` already replays a banked answer token-by-token so it reads as live —
  reuse that mechanism.
- **Pre-generated response variations**, not live rephrasing: ~5 natural phrasings per canonical
  answer, generated once, offline, via Haiku (batch cost ~$3.40–6.75 for the full catalog), served
  on rotation at zero marginal runtime cost. **Guardrail: variations may re-word, never
  re-content** — every variation must pass the same citation/entailment check the fabrication
  tooling already uses elsewhere. Note: this project's own recent testing (RM-8, 2026-07-22) found
  register-invariance not yet reliable (3 of 5 probes failed on content-invariance) — human review
  of a sample of generated variations stays mandatory before they go live, not a rubber stamp.
- **Launch with a conservative, high-confidence-only match threshold.** Loosen later based on real
  pilot data, not before. With no tap-confirm step catching a bad match before the participant
  sees it, a cautious starting threshold is the actual safety mechanism, not the calibration
  testing described below (which still needs to happen, just isn't gating this launch).
- **Log every match decision silently, regardless of UI state:** the question asked, the canonical
  entry matched (if any), the confidence score, and which variation was served. This is what makes
  "test in pilot" a real test rather than just hoping — review this log directly for real
  mismatches rather than waiting only for a participant to say "that didn't answer my question,"
  which is a real but lagging and incomplete signal.

**Rollout philosophy, Mark's explicit call:** test in the real pilot, not a separate offline
calibration study first. The threshold-calibration test design and blind tone-comparison test
design from the feasibility study (`CiC_Cost_Reduction_Feasibility_Study_V0_1.md`, Item 1) remain
available as a fallback path — if pilot logging shows a real mismatch pattern (repeated "didn't
answer my question" signals, or the match log itself showing bad matches getting served), add a
verify-the-question step at that point, using those already-designed tests to figure out what
needs tightening, rather than guessing.

---

## What this dispatch does NOT include

The feasibility study's other levers (retrieval-depth trim, over-settling screen recalibration)
are real and low-effort but were not explicitly confirmed for this build pass — worth a look
later, not held up as blocking this scope. The Living Table's structural cost gap is a product/
business decision already logged in the Funding Strategy thread, not an engineering task.

## Completion criteria

Same convention as every other dispatch from this project: a dated log entry wherever this build
actually lands, listing what shipped and what's still open, and the Guided-Questions design-doc
correction noted explicitly rather than left silently inconsistent with the live decision.
