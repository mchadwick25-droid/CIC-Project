# Relational Safety Redirect: Resource-Naming Decision

**Portfolio-level decision under CO-022, escalation category 2** ("portfolio-level or cross-world strategic decisions") **— escalated directly to the project lead, not self-disposed by this build thread.**

This decision sets the pattern every future formation world's Facilitator-governed relational-safety redirect inherits. It is not specific to World #1, and it is not a construction judgment this thread has standing to make on its own — CO-022 reserves exactly this category of decision to the project lead directly, and B7 (World #1's own Phase Six Facilitation Brief) already anticipated this exact question without resolving it.

---

## What's Actually Being Decided

`Build/reference/L3D-Encounter-Methodology/CiC_L3D_AcuteDistress_HarmfulDynamic_Mechanism_Proposal_DRAFT.md` drafts the Facilitator's crisis-redirect content (§5) with a placeholder everywhere a concrete resource would go: `[RESOURCE REDIRECT — pending decision]`. This document is that decision. It does not have to be answered all at once — a phased answer (Option C below) is one of the three options.

The question, stated plainly: **when the mechanism fires because a participant has disclosed acute personal crisis, self-harm risk, or another emergency, what — if anything — does the Facilitator's redirect actually point the participant toward?**

## Option A — General Redirect, No Named Resource

The Facilitator names the limit honestly and encourages the participant to reach out to real support — a crisis line, a trusted person, local emergency services — without naming a specific number, organization, or service.

*Example redirect language:* "Please reach out to a crisis line, a trusted person in your life, or emergency services where you are — right now, before we go any further."

**In favor:** Works identically everywhere in the world, with no jurisdiction logic to build or maintain. Carries no institutional-endorsement exposure — the architecture is not vouching for any specific organization's quality, availability, or accuracy. Lowest ongoing maintenance burden for a sole-builder project (Constitution Article 36) — nothing to verify stays correct as hotline numbers, names, or ownership change over time.

**Against:** Weakest in the moment it matters most. A generic phrase requires the participant to already know what to search for or call — someone outside the US may not know "988" exists to look for, and someone inside the US in acute crisis may not reliably think to search for it either. General crisis-response guidance treats naming a concrete, dialable resource as materially more likely to produce actual contact than a generic pointer. This option is the most defensible on paper and the least likely to actually connect a specific participant to help in the moment.

## Option B — Named Resource(s), With Jurisdiction Caveat

The Facilitator names a specific resource — for example, the 988 Suicide & Crisis Lifeline for a US-based participant — paired with an explicit caveat for anyone outside that jurisdiction ("if you're outside the US, please contact your local emergency number or search for a crisis line where you are").

**In favor:** Most actionable — gives the participant something concrete to act on immediately, which is the whole point of the redirect existing at all. Matches how crisis-response is typically handled in comparable conversational AI contexts, where naming a real number materially increases the odds someone actually uses it over a generic pointer.

**Against:** Requires knowing or guessing the participant's jurisdiction, which this architecture has no reliable way to do (no verified location signal is part of anything reviewed for this task) — a wrong-jurisdiction number is actively unhelpful at exactly the wrong moment. Requires ongoing maintenance: hotline numbers, names, and even which organization operates a given line change over time (988 itself is a recent US consolidation of what used to be a different number), and a sole-builder project has to actually sustain that upkeep or the resource degrades silently. Naming a specific organization is a form of institutional endorsement this project has not otherwise made anywhere in its governance documents, and raises a real question of whether that endorsement should be made lightly.

## Option C — Tiered: General Floor Now, Named Resource for Known Testers, Public-Scale Answer Deferred

Recognizes that this project's current phase and its eventual public phase are not the same problem. Constitution Article 36 already establishes that prototype and internal testing may proceed before the minor-caution mechanism exists at all, and Article 12 already gates any live invisible-register operation on real participants in public availability behind that same unbuilt mechanism — meaning the hard version of this question (an unknown, unvetted, potentially global participant population) is already out of scope for right now regardless of what this document decides. At prototype scale, the people actually testing this are known, recruited, and informed in advance that this is a prototype (Article 36's own testing-participant transparency requirement).

Under this option: the redirect always carries Option A's general language as an unconditional floor. During prototype and internal testing specifically, it additionally names one concrete, jurisdiction-appropriate resource selected because the known testing population's jurisdiction is actually known in advance (unlike Option B's general case) — removing Option B's core objection for this phase specifically. The question of what a public-availability version of this redirect should say — full Option B with jurisdiction detection, Option A alone, or something else — is explicitly deferred to whenever public availability is actually being planned, rather than decided now for a population this project isn't serving yet.

**In favor:** Matches the actual shape of this project's own phased deployment gating rather than solving a harder version of the problem than currently exists. Gets a concrete, actionable resource to the small number of real people actually testing this right now, without committing to a specific public-scale answer before public scale is a real question with real facts (participant volume, actual jurisdiction spread) available to decide it against.

**Against:** Two-part answers are more to build and to keep straight than a single fixed one — the redirect content needs to know which phase it's operating in, which is a small but real additional piece of state. Defers a question that will eventually need answering anyway; if not revisited deliberately when public availability planning actually starts, there's a real risk the prototype-phase answer simply ships by default without the fuller Option B tradeoffs (jurisdiction detection, maintenance ownership) ever getting a real decision.

---

## What Would Help This Decision Get Made

Not asked as this document's own decision, but worth having in view: who is expected to actually test this prototype (a small known group Mark recruits directly, versus a broader semi-public beta) bears directly on whether Option C's "known jurisdiction" premise holds, and whether anyone besides Mark has capacity to own ongoing accuracy of a named resource if Option B or C is chosen.

This document takes no position among the three. Whichever is chosen, `Build/reference/L3D-Encounter-Methodology/CiC_L3D_AcuteDistress_HarmfulDynamic_Mechanism_Proposal_DRAFT.md` §5's placeholder text gets replaced with the resulting concrete language, and that replacement should go through the same review discipline as any other safety-critical content in this project (§4.5 of that document).

---

## Decision (2026-08-05)

**Option A shipped as the unconditional floor**, effective immediately in
`Build/reference/L3D-Encounter-Methodology/CiC_L3D_AcuteDistress_HarmfulDynamic_Mechanism_Proposal_DRAFT.md` §5 and
`cic-poc/backend/app/prompts/facilitator_prompts.py` (A1, A2, Harmful Dynamic
templates). This closes the standing contradiction with Facilitator Governance V3.6
§12 that the project's own ALX battery graded MARGINAL twice and called "a hard
pre-freeze fix item" (`Archive/Technology-Pass2-2026-08/Pass2/batteries/S6.2_ALX_battery_A_grading.md`,
`S6.2_ALX_battery_B_grading.md`).

**Option C's tiered addition (a named, jurisdiction-appropriate resource for known
testers) is not shipped tonight.** It needs an actual answer to this document's own
open question — who is testing, and is their jurisdiction actually known — before it
can be built responsibly, and that is Mark's call, not a default to assume. Treat
Option C as separately-scoped follow-up work, not blocked on Option A, not implied by
it.

Full detail on what changed and why: see the 2026-08-05 entry in
`Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`.
