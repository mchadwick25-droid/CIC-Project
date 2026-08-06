# Launch prompt — Pilot spend/usage limit, thought through fresh

Paste this into a brand-new thread, separate from System Hub and separate from any prior
tier/pricing work. **This is a real-time thinking-through conversation with Mark, run as a Sam
Kaner Diamond of Participatory Decision-Making: divergent first, through the groan zone, to a
converged decision — done interactively with Mark's own words shaping each stage, not
self-administered.** The Atlas v3 rebuild's design-convergence session is the model to follow for
*how* to run this (ten interactive rounds, Mark's own phrasing quoted and worked with directly,
including at least one genuine "not at convergence yet" correction along the way) — match that
posture, not a solo pass dressed up as if Mark were in the room.

## The actual question

The pilot needs *some* limit on it before real traffic hits it — Mark's own framing: "setting a
limit." What kind of limit, on what dimension, enforced how — that's genuinely open, and finding
that out together is this thread's whole job. Don't arrive with a mechanism already picked.

**Explicit and important: do not start from, extend, or reference the existing tier-system work.**
SH-12 (a free tier vs. a $15/mo paid tier, gated behind real sign-in and a live Stripe
subscription-status check at session-start) already exists as a design direction in the Task
Board, deliberately deferred until real pilot traffic data exists. **This thread is not that
thread.** Mark wants this thought through with genuinely fresh eyes, unconstrained by the
sign-in-page shape that design already committed to — not a variation on it, not a simplified
version of it, a different starting point entirely. If divergent thinking leads back to something
resembling SH-12, that's a legitimate outcome to name — just don't start there.

## Grounding — real numbers already gathered, don't re-derive these

- **What's actually live right now, and what isn't:** the account/sign-in layer (Supabase) is
  built but deliberately switched off for this stage — small audience, informal access, Mark's own
  2026-07-20 call. The only backstop currently enforced is a **60-turn cap on a single
  conversation** — real, but it protects against one runaway session, not total traffic. There is
  **no cap today on how many separate conversations any one visitor, or all visitors combined, can
  start.**
- **Real, converged cost basis** (cross-checked twice already in this project, two independent
  models agreeing): roughly **$0.28–1.10 per user per month** at light-to-heavy usage, or
  **$0.20–0.35 per typical 1:1 interview conversation.** Living Table rounds (2–3 Representatives
  each responding) cost more per turn — realistic per-conversation range **$0.30–0.75**, held
  conservative rather than optimistic pending real usage data. Full model:
  `Ministry/Funding/CiC_Go_Live_Cost_Model_V0_1.md`.
- **The one global backstop already planned, not yet set:** the Anthropic Console spending
  limit — a hard, settable ceiling on the API key itself that stops all calls once crossed,
  independent of any per-user logic. A **$100–150 initial ceiling** covers roughly **150–500 real
  conversations** at the cost basis above. This is infrastructure-level, not product-level — it
  protects the bill, not the experience, and it says nothing about what a genuinely well-designed
  per-visitor or per-day limit inside the product should look like.
- **Founder-capital context:** a $40 transfer into the operating account is the real, current
  budget reality this sits inside (Dashboard's "waiting on you" list) — worth having in the room as
  the actual scale of what's being protected, not an abstract number.

## How to run this

Kaner-style, for real: open divergent — generate genuinely different shapes a "limit" could take
(examples to make the breadth concrete, not a menu to pick from: a global spend ceiling alone with
no per-visitor logic at all; a lightweight non-account mechanism like a browser-local or
IP-scoped conversation counter; a soft limit that degrades gracefully — e.g. shorter sessions or a
waitlist message — rather than a hard stop; a time-window cap instead of a count cap; something
that uses the already-built-but-dormant Supabase layer for *only* a minimal identity check without
the full tier/paywall UX; or genuinely nothing beyond the Console spending ceiling, argued for on
its own honest terms). Let the groan zone be real — surface the tradeoffs each shape forces
(fairness across visitors vs. simplicity vs. built-not-reused-work vs. how much friction a pilot
participant should ever feel) rather than resolving them prematurely. Converge only once Mark's
own words show actual convergence, the same discipline the Atlas thread's log demonstrates.

No design doc, no code, no locked decision required to end this thread — if a direction converges,
name it clearly and stop there; a real design/build pass is separate, later work, in its own
thread, same as every other workstream in this project.

Model tier: Sonnet, per the project's standing model-tier policy (Sonnet for live
conversation/exploration; Opus reserved for deeper evaluation passes; Fable capped at 2/week for
the largest comprehensive passes).
