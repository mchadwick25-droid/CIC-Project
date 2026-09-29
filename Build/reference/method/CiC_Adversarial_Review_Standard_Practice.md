# CiC Adversarial Review — Standard Practice

Not a rubric that was designed up front — a practice that emerged the same way across three real rounds on the same document (`Build/Ministry/Technology/CiC_System_Redesign_Fable_Brief_2026-07-25.md`, reviewed in `Build/Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/11_...md` and `18_...md`, with a second round logged but not separately filed — see the Decision Log's 2026-07-25 "later" entry). Written down here because it kept working and Fable should be able to see it too, not just infer it from three review artifacts.

**When to use it:** before spending a capped, expensive pass (Opus for a deep pass, Fable for the largest comprehensive ones — see the model-tier note below) on a document whose claims matter — a design brief, a research synthesis, anything where a wrong citation or an inverted argument would propagate into what gets built next.

## The practice

**1. Source-level verification, not plausibility-checking.** Every factual claim in the document under review gets checked against its cited primary source directly — read the claim, read the source, confirm they actually say the same thing, not just that they're in the same neighborhood. The reviewer re-verifies the most severe findings itself rather than trusting its own earlier summarization of a source.

**2. A fixed severity vocabulary.** P0 = blocks sending / must fix before the pass is spent. P1 = materially improves the result but isn't disqualifying. P2 = polish. Same three tiers, same meaning, every round — so findings triage the same way regardless of which round produced them.

**3. Specific structural checks, counted, not eyeballed.** Cross-reference integrity (does every internal pointer resolve to the section it claims to). Completeness mapping (does every stated objective have a corresponding deliverable, and vice versa). A measured balance ratio (word count of diagnosis/framing vs. word count of the actual ask) — round 1 found this at ~68/32 and named the specific failure mode it predicts: "an excellent re-diagnosis with a thin design attached." These are things the reviewer counts, not impressions it forms.

**4. Read what the last review found before hunting for new problems.** Each round reads the prior round's findings (and what was actually fixed, per the Decision Log) first, so it isn't re-litigating settled ground — it's calibrating, then aiming its skepticism specifically at whatever's new and has never been checked.

**5. Explicit adversarial framing, naming the actual failure mode to hunt for.** The dispatch tells the reviewer what kind of error this specific process has caught before — not "review this for quality" but "this document was written by an assistant that has produced a fabricated composite quote, a mechanism misattribution, and an overclaimed data pool in this exact project; assume the same risk is present until you've checked." Round 3 caught a fourth instance of the same class: an inverted causal claim (§4's certainty-distortion clause) that would have flipped a live safety bias if shipped as written.

**6. A genuine bottom-line verdict, stated plainly, regardless of how many rounds already happened.** "Ready to send" or "not ready, here's exactly what's wrong" — not softened toward approval because this is the third pass on the same document and everyone would like to be done.

## Why it earns its keep

Three rounds, three real catches, each a different flavor of the same underlying risk (a claim that sounds right but doesn't survive being checked against its own source):

- Round 1: a mechanism misattribution and a fabricated composite quote, both in brand-new brief prose.
- Round 2 (logged, not separately filed): a claimed real multi-world transcript pool that didn't exist — confirmed by opening the actual transcript files rather than trusting the finding's own wording.
- Round 3: a certainty-distortion clause that inverted the direction of the source it cited, plus a measurement-plan deliverable with a misattributed statistic and an unsourced "industry-standard" framework.

None of these were visible from a read-for-tone pass. All four were caught by the specific discipline of opening the cited source and checking the claim against it directly.

## Model tier

Opus 5.5 runs every review pass, and the reviewer is never the drafter. Sonnet 5.5 and Fable 5.1 draft as Build Process V2.0, Section 2, routes them. A document gets its Opus adversarial pass before any capped, expensive pass it is headed for, and not after.
