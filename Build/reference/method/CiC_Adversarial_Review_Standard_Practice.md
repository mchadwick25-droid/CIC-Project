# CiC Adversarial Review — Standard Practice

A standard practice for adversarial review of any document whose claims matter.

**When to use it:** before spending a capped, expensive pass on a document whose claims matter, such as a design brief, a research synthesis, anything where a wrong citation or an inverted argument would propagate into what gets built next.

## The practice

**1. Source-level verification, not plausibility-checking.** Every factual claim in the document under review gets checked against its cited primary source directly — read the claim, read the source, confirm they actually say the same thing, not just that they're in the same neighborhood. The reviewer re-verifies the most severe findings itself rather than trusting its own earlier summarization of a source.

**2. A fixed severity vocabulary.** P0 = blocks sending / must fix before the pass is spent. P1 = materially improves the result but isn't disqualifying. P2 = polish. Same three tiers, same meaning, every round — so findings triage the same way regardless of which round produced them.

**3. Specific structural checks, counted, not eyeballed.** Cross-reference integrity (does every internal pointer resolve to the section it claims to). Completeness mapping (does every stated objective have a corresponding deliverable, and vice versa). A measured balance ratio (word count of diagnosis/framing vs. word count of the actual ask) — a heavy framing share predicts an excellent re-diagnosis with a thin design attached. These are things the reviewer counts, not impressions it forms.

**4. Read what the last review found before hunting for new problems.** Each round reads the prior round's findings (and what was actually fixed) first, so it isn't re-litigating settled ground — it's calibrating, then aiming its skepticism specifically at whatever's new and has never been checked.

**5. Explicit adversarial framing, naming the actual failure mode to hunt for.** The dispatch tells the reviewer what kind of error this specific process has caught before — not "review this for quality" but "an assistant has produced a fabricated composite quote, a mechanism misattribution, and an overclaimed data pool in this kind of document; assume the same risk is present until you've checked."

**6. A genuine bottom-line verdict, stated plainly, regardless of how many rounds already happened.** "Ready to send" or "not ready, here's exactly what's wrong" — not softened toward approval because this is the third pass on the same document and everyone would like to be done.

## What it catches

It catches mechanism misattributions, fabricated composite quotes, claimed data that does not exist, clauses that invert their source, and misattributed statistics. A read-for-tone pass misses all of these. Opening the cited source and checking the claim against it directly catches them.

## Model tier

Opus 5.5 runs every review pass, and the reviewer is never the drafter. Sonnet 5.5 and Fable 5.1 draft as Build Process V2.0, Section 2, routes them. A document gets its Opus adversarial pass before any capped, expensive pass it is headed for, and not after.
