Simulated review — informational only, not an Article 31 substitute.
Review round 3 (targeted recheck), cappadocian record audit fixes, 2026-10-13, reviewer: independent Opus subagent

Round: 3
Reviewer model: Opus
Reviewer agent: independent subagent, fresh context, read-only, not the round 1 or round 2 reviewer
Drafter model: Opus
Drafter agent: the session's own Opus thread made the record edits; this reviewer did not draft them
Truncation check, method 1: the file ends on the Verdict line, a complete sentence
Truncation check, method 2: the body below this header is 3027 characters, the same length as the reviewer's returned message, counted separately before saving
Scope: the two items round 2 left blocking, text fields only.

**Round-3 targeted recheck (read-only, no model calls; `text` fields only)**

**1. `cappadocian.dw.not-a-death-wish`: CLEARED.** The text is now faithful to Sozomen and no longer uses Eupsychius as an example of refusing to deny the faith.
- **Matches the source.** Sozomen V.11 (npnf202 ~36048–56) says "I believe that Eupsychius was condemned in consequence of the demolition of the temple of Fortune… all the actors in this transaction were condemned." The new wording "A later church writer believed he was condemned for his part in pulling down the temple of Fortune" matches it. "Believed" carries Sozomen's own hedge, and "his part in" matches "all the actors."
- **Eupsychius is no longer the refusal example.** The closing line now reads "The virtue we named in the Forty was refusing to deny the faith…". That ties the refusal to the Forty's bath-on-the-shore scene, which the sources support. Eupsychius stays only as a martyr whose feast the world kept.
- **No false or post-window claim.** "A later church writer" names a later source as a source, without speaking past 394. That is an attribution device, not a horizon breach.
- **Minor clarity point, not blocking.** "the Forty" is never set up earlier in this text. The story only says "soldiers" and "the number stayed the same," so a participant may not know who "the Forty" are. It could be a one-word clarity fix later.

**2. `cappadocian.dw.catholic-and-its-rivals`: CLEARED.** The text now stays inside the world's horizon (ends 394) for canon cell F3-T, and it is accurate.
- **Post-window sentence is gone.** The line about teachers becoming "curriculum, liturgy, and law for the traditions…" has been removed.
- **New wording follows the fleet precedent.** It tracks `records/alx/doctrinal_witness/alx.dw.one-church.md` lines 38–40 almost word for word: "Whether any present-day church is 'our church' reaches past what we can see. We speak from before the splits that made today's map."
- **Facts are right and in-window.**
  - "We lived through one great council, at Constantinople" refers to 381, inside the window.
  - "finally condemned with the rest" is accurate: canon 1 of Constantinople 381 anathematizes the Eunomians, Arians/Eudoxians and Semi-Arians/Pneumatomachians.
  - "finally established under a later emperor" refers to Theodosius in 380–381, also inside the window.
- **Side effect outside this pass's scope.** The `sources[]` entry `cappadocian.force.canonization-sieve`, with locus "corpus becoming curriculum, liturgy, and law…", no longer has a matching sentence in the text. That falls under the sources/locus items you've already logged in Open_Gaps, so it is not blocking here.

**Readability** (`engine.m1.gates.grade_text`, target FK ≤ 10 and FRE ≥ 60): both texts pass.
| Record | FK | FRE |
|---|---|---|
| not-a-death-wish | 6.55 | 74.99 |
| catholic-and-its-rivals | 6.40 | 70.81 |

**Verdict:** both round-2 blocking items are cleared in their `text` fields. Nothing blocking remains in the scope you set for this pass.

Disposition: the clarity point on "the Forty" was applied ("those soldiers"). The canonization-sieve locus is logged in Open_Gaps with the other out-of-scope metadata.
