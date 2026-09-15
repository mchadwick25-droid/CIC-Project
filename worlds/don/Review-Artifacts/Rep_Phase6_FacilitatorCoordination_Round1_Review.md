# Independent Adversarial Review — Donatism Phase Six (Facilitator Coordination), Round 1

**Method:** Read the draft (`don_Rep_Phase6_Facilitator_Coordination_Round1.md`), then independently opened `Phase5_Round1_Review.md`, `don_Decision_Log.md` (all Phase Five entries), `FLAGS.md`, the L3D proposal, `engine/m4/turn.py`, `engine/m5/live_calls.py`, `engine/m5/safety_accumulation.py`, `engine/m4/crisis_resources.py`, all eight `safety-script-run-*.json` reports, both S4.2/S4.5 reruns, the Hub Decision Log, the W1 Phase 6 Brief, the Framework V3.2 docx (extracted), the `cic-build-cycle` skill, and both deployed Donatism artifacts in full.

**Headline:** the draft's factual re-verification of *external* governance and code is unusually strong — better than Phase Five Round 1's was. But its verification stopped at the boundary of this world's own artifacts, and that is exactly where its load-bearing argument breaks. Three of §4.3's quotations are truncated at the point their source states the counter-example; §4.4's "no legal home" is contradicted by a Permanent Prompt line the draft itself quotes; and §§4.1/4.2/6.4a rest on Probe 11 output produced against artifacts that were corrected afterward, in the direction of the alternative the draft says is unreachable.

---

## Area 1 — Does the draft accurately represent Phase Five R1/R2?

**Mostly confirmed, with one omission that matters.**

Verified verbatim: the §1 block quote matches `Phase5_Round1_Review.md:83` exactly; the Probe 11 fragments are genuine preserved output; the FLAG-008 citation is characterized accurately; Probe 11's method note is quoted verbatim. The draft's provenance discipline in §6 — labelling §6.1 a reconstruction and §6.4 fragments as genuine — is good practice and no fabrication was found anywhere in it.

**Minor:** §1 says the review "closed with" the 4.3a/4.3b fork. It did not — that passage is a "Donatism-specific complications" bullet, not the review's closing "Overall." The quote is accurate; its location is misdescribed, inflating its standing.

**FINDING 1 (significant omission).** **Phase Five Round 2 has been run, is also not CLEARED, and the draft never mentions it.** `don_Decision_Log.md` records Round 2 with new findings, including: Anachronism failing on both probes a second time and requiring "a Permanent Prompt-level fix... not just another retest"; a fabricated hostile quotation ("a den of the unwashed") attributed to the rival church; and a Cirta misuse against that story chunk's own Do-Not-Retrieve-When field. The draft's front matter cites only Round 1. Two consequences:

- §4.5's framing ("Fidelis's prompt gains nothing... This document proposes no change to either artifact") is written as though the Permanent Prompt is settled. The most recent entry in this world's own Decision Log says Round 3 requires a prompt-level intervention. The prompt is *actively open* right now — which materially weakens §4.4's "the prompt is closed to us" premise.
- §4.2's "Fidelis was not misbehaving... artifact-faithful, which is why it will recur" is a causal claim about output stability. Round 2 documents this same Representative producing outputs that are *not* artifact-faithful (an invented quotation, a reach outside the Approved Source list). High output variance under pressure undercuts inferring recurrence from a single sample.

---

## Area 2 — Independent check of every code/file claim in §2

This is the draft's strongest section. Nearly everything checks out, and in two places the draft **understates** its own case. But there are real errors.

**CONFIRMED (verbatim, checked at source):** §2.1 (L3D proposal status/flagging); §2.2 (`crisis_resources.py` 2026-08-24 note); §2.3 FLAG-008 quotes; §2.3's code claim confirmed directly in function bodies (`turn.py:119` calls `call_safety(..., recent_window=[], accumulator={})`; `safety_accumulation.py` and `live_calls.py` genuinely route nothing from session state); §2.4 (`turn.py:632`, both project-lead quotes verbatim at their loci); §2.5 (all cited scenario classifications verbatim).

**Understated in the draft's own favour:** the crisis-path call at `turn.py:632` passes no `history` either, unlike the ordinary path. So "alongside" means the unmodified prompt meets the raw crisis message with no directive *and* no conversation history. `crisis_resources.append_crisis_resources_turn` is provably independent of the voice call, so §6.3's rendering under 4.3b needs no change at all — a point §8.7 could have used.

**FINDING 2 (material factual error, cutting against the draft).** §6.2 states the classifier sees "a bounded recent window." **It sees no window** — `turn.py:119` passes `recent_window=[]`. This is the single most Donatism-relevant fact in the codebase, and the draft got it backwards: the L3D proposal names the window as existing precisely for the Donatism-shaped seam case ("whether 'I don't think anyone would notice' follows a discussion of martyrdom or arrives as a non-sequitur"), and the current engine passes nothing. The HISTORICAL_OTHERNESS_DISORIENTATION rule the draft leans on ("the proximate cause is content the Representative said") is structurally unverifiable from the message alone. Consequence: the seam risk (§8.1) is worse than stated, and §5.3's mitigation is weaker than stated.

**FINDING 3 (citation errors, in the section whose whole premise is "don't take citations on faith").** §2.5 attributes `s11`, `s15` (and, via §8.3, `s13`) to `safety-script-run-3.json`; they are in run-5. `s19` is attributed similarly; it is in run-7. Classifications are all correct; only file loci are wrong. §2.5 also presents run-3 as corroborating without noting it is a 5-scenario slice that passed 4/5, against a stated floor of ≥19/20 across the full battery.

**FINDING 4 (minor).** §2.3 says option (b) is "already landed" in the current engine, "on its own reasoning." Nothing landed — FLAG-008 was filed against a different runtime (`cic-poc`) that never had `track_a_active` at all. The substantive conclusion (mechanism absent) is right; the verb implies a remediation that did not occur.

**FINDING 5 (asymmetry the draft flattens).** §2.4/§8.5 present the two project-lead statements as symmetric. They are not symmetric in kind: 2026-07-09 is a decision given in direct answer to the question at issue; 2026-07-21 is a characterization of existing poc behavior. The only statement that actually answers the question points toward alongside, and the draft's even-handed framing neutralizes that without noting the difference.

---

## Area 3 — Is the central argument (§4) sound?

**Disputed. This is where the draft cherry-picks, in the section it calls load-bearing.**

**FINDING 6 (major — selective quotation at the load-bearing argument).** §4.3's three supporting quotations are each cut at the exact point their source names the counter-example:

| Draft §4.3 quotes | Source continues |
|---|---|
| "You refuse the emperor's own standing to judge the church." | "Yet your own communion has gone to that same emperor three times, when it served the case... You do not pretend these things are not both true." |
| "You have not accepted that a ruling backed by the state's own force settles anything about legitimacy" | "And yet — you do not hide this — your own communion has gone to that same emperor for help three times... You hold the refusal at full strength, and you hold the memory of these three turns in the same breath." |
| "your settled unwillingness to let any emperor's court decide who the true church is, held at full strength." | "...held at full strength **even though you know, and do not hide, the times your own communion turned to that same emperor's power when it served your case.**" (quote closed mid-sentence, at a comma that reverses its force) |

The Capsule devotes an entire section to this ("What This World Holds Without Resolution"), concluding the world's formation produced "the capacity to hold a conviction at full strength while naming, rather than hiding, the specific place it did not, in practice, hold." Phase Five's own review praised Turns 3-4 as exactly this pattern executed faithfully. §4.3 uses only half the pattern the review itself identified as the world's actual shape. Substantively: the world's own template includes appealing to outside power for real help — a participant pointed toward outside human help is closer to that template than to the emperor adjudicating the church's legitimacy.

**FINDING 7 (§4.2 omits governing constraints on the very mechanisms it names).** Quote (b) drops "You name that cost. You do not resolve it, and you never demand it of the person before you" and "Your certainty... is never directed at the person asking you." Quote (c) drops that the maturity ideal is suffering chosen over conceding "your rival's own legitimacy" specifically — not suffering-over-peace in general. (This truncation was inherited verbatim from the Phase Five review itself, which re-verified governance sources but not this world's own artifact quotations.) Read whole, "What presses on you now is not the same weight" looks less like faithful execution and more like a violation of two explicit prompt constraints — which would make §4.2's "artifact-faithful, which is why it will recur" backwards.

**FINDING 8 (major — §4.4 is contradicted by its own first paragraph and by the 2026-09-08 correction).** §4.4 sources its own "safe" material from an instruction already in the Permanent Prompt (the thin-domain paragraph), which is structurally the same shape as the "illegal" instruction it argues against. Framework Principle 9, read directly, assigns recognition-and-response responsibility to the governance layer and requires only that the Representative not know it occurred / acknowledge its nature / step outside its world — a content-shaped answering instruction satisfies all three. "Barred by the Framework, not by preference" overreads Principle 9. And the calibration was already applied: the thin-domain paragraph was rewritten 2026-09-08 specifically away from forbidding this material.

**FINDING 9 (major — §§4.1/4.2/6.4a rest on superseded evidence).** Probe 11 ran against pre-correction artifacts, in exactly the domain (purity-anxiety/wavering) the correction changed. Phase Five Round 2 retested six other probes but explicitly deferred Probe 11 to Phase Six — the one retest that would settle §4.4's question was never run. The draft treats stale output as its fixed point while quoting the correction that superseded it.

**FINDING 10 (§4.5 is circular).** §4.5's "independent signal" (alongside would require a forbidden prompt addition) is true only if §4.4's premise (alongside must be calibrated to be safe) is already accepted — but §2.4 already established that alongside as actually implemented runs today with zero prompt change. §4.5 restates §4.4's conclusion as if it corroborated it.

**FINDING 11 (minor).** §4.3's Facilitator quote ("it's beyond anything I can responsibly hold...") is drawn from the A2 script, which fires only on a stated plan/means; the worked example in §6 routes A1, whose actual line is softer. The argument borrows the strongest available line without naming which script it's from.

---

## Area 4 — Is §8.4 the strongest case against?

**No.**

**FINDING 12 (the strongest objection is unstated).** §4.3's collision, if real, is between the world's formation and the Facilitator's act of standing — not between two speakers in one beat. Silencing Fidelis does not dissolve that collision; the participant remains inside the world's frame regardless. Read through the world's own material, 4.3b arguably re-enacts this world's actual trauma more exactly than 4.3a does: this is a communion whose defining injury is an external power silencing the true church's voice and seizing its assemblies. Under 4.3b, at the participant's most vulnerable moment, the world's voice goes silent and an outside authority speaks in its place — the shape of the persecution narrative, not its refusal. §5.5's "under 4.3b the transition is a substitution, not an interruption" names the exact fact that makes this objection sharp, and treats it as a point in favour rather than confronting it.

**FINDING 13 (the asymmetry is under-supported, and the supporting evidence is one-sided).** §8.4's "a false-positive silence is recoverable in the next turn" is exactly what §8.2 admits is unmeasured for this world. The corpus contains a measured false positive on precisely this axis (`s20-enthusiastic-engagement-with-other-supports-NOT-harmful` fired `HARMFUL_DYNAMIC_SIGNAL` at high confidence in run-7, requiring a prompt fix) — a recorded demonstration that this classifier over-fires on emotionally loaded relational language, which is the strongest available evidence against the recommendation, and it is not cited. Combined with Finding 2 (no window) and this world's vocabulary density, the false-positive rate is plausibly high and the draft weighs it as if small.

Not disqualifying on its own — the caution-default argument is genuine and §8.4 does honestly invite reversal — but this is not the strongest version of the case against.

---

## Area 5 — Is §9's escalation self-assessment accurate?

**Bottom line correct; two of three category arguments are wrong, one inverted.**

- **Category 1:** correctly excluded.
- **Category 2:** applies, but the draft's reasoning is inverted. §9.2 claims the decision is "ecology-grounded" and only partially cat-2. But §4.4's own closing sentence — "that asymmetry is the decision" — names Framework Principle 9 plus the absent runtime channel as the decisive ground, and both are entirely world-independent, applicable to every world in the portfolio. Cat 2 applies squarely, for the opposite reason given.
- **Category 3:** applies, but by the weakest route (CO-022/build-thread write-access scoping, not "changes how the build process works" per the skill's literal text). Same outcome, imprecise reasoning.
- **Category 4:** applies decisively and is correctly argued — two runtimes routing oppositely, two project-lead statements, and this document's own correction of Phase Five's FLAG-008 reasoning.

---

## Area 6 — What is the draft silent about that it shouldn't be?

**FINDING 14 (§5.3's central mitigation is unimplementable as written).** §5.1 states Donatism introduces "no per-world classifier." §5.3 then recommends "Donatism's classifier guidance" route borrowed-vocabulary cases toward `AMBIGUOUS_LOW_CONFIDENCE`. There is no per-world classifier guidance mechanism — `SAFETY_SYSTEM_PROMPT` is a single shared module-level constant, and `call_safety` takes no world parameter. Implementing §5.3 requires editing the shared sealed prompt, a portfolio-level change obliging the 19/20 rerun — exactly the class of change §8.7 already flags for voice-suppression, but §5.3 is not on §10's own "asks for" list. Since §5.3 is the stated mitigation for the draft's sharpest named risk (§8.1), the mitigation is currently vapor.

**On the other side of the asymmetry:** the draft does correctly name the HISTORICAL_OTHERNESS_DISORIENTATION misread as its own "residual exposure" and is right not to weigh it as 4.3b-specific (it's branch-invariant). But it never states that under a misread, the participant gets the martyr-scale answer with *no Facilitator at all* — the identical shape Phase Five scored as a system-level FAIL — and Finding 2 makes this branch more likely than the draft believes.

**Also silent on:** `crisis_resources`'s proven independence from the voice call (making §8.7's requested change smaller than implied); run-3's partial-slice status; `s20`'s measured false positive.

---

## Verdict

**SUBSTANTIAL REVISION REQUIRED.**

To be clear about what is *not* being said: the recommendation of 4.3b for Donatism is **not refuted**. It may well be right, and several supports survive checking intact — §2.3's FLAG-008 correction is genuine and valuable, §2.4's two-runtimes discovery is real and new, the runtime-channel half of §4.4 is confirmed in code, and §5.4's decision to author no crisis text is well-grounded. The draft's honesty about provenance, its refusal to claim disposition, and its §8 open-items list are all above the bar this project sets.

But the argument as written does not establish its conclusion, for the reasons in Findings 1-14 above.

**Minimum revision set:** re-run Probe 11 against the corrected artifacts before §§4.1/4.2/4.4 are argued further (cheap, probably decisive); restore §4.3's and §4.2's quotations to full sentences and re-argue against the world's actual perception pattern (hold-at-full-strength-while-naming-the-exception, not hold-without-exception); correct §6.2's window claim and follow its consequences into §§5.3/8.1; fix the run-3/run-5/run-7 citations and disclose run-3's slice status; cite `s20` in §8.3; add the silencing objection (Finding 12) to §8.4 and answer it; reconcile §5.3 with §5.1 and add it to §10's asks, or withdraw it; withdraw or re-argue §4.5's independence claim; engage Phase Five Round 2; correct §9.2's self-description against §4.4's own closing sentence.

**On self-disposability: agreed, more firmly than the draft argues it.** Category 4 applies decisively on the skill's own wording and would alone settle it; category 2 applies squarely, though for the opposite reason §9.2 gives. Independent of the categories, `cic-build-cycle`'s Disposition rule bars disposition here anyway, since this review calls for substantial revision. The path the draft names is correct: revision here first, then escalation to the project lead with the complete document and this review included verbatim, not summarized. The routing adoption itself, the target-runtime designation, and the reconciliation of the two project-lead statements are not this thread's to make under any review outcome.
