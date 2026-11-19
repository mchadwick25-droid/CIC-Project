# Fixes R50: Dhuoda

Ruling: Mark, 2026-11-17 ("yes no softening, we are a witness not a judge … for this round 1 but also the should fixes too"). Released text kept as `dhuoda.r50.brief.txt`.

## Fix-list items

1. **MUST: the 1923 catechism point is the translators' own claim, without the narrator's "because it showed" and without "ordinary people".**
   - Old: "In 1923, two translators of the Catholic catechism named "the manual of Dhuoda" among the works of Christian instruction from the ninth century on. With it they answered the claim that the catechism began with Luther, because it showed the faith taught to ordinary people before him."
   - New: "In 1923, two translators of the Catholic catechism set out to answer the claim that the catechism began with Luther. Among their examples of Christian instruction from the ninth century on, they named "the manual of Dhuoda"."
   - Source: I5 — `cic/texts/council-of-trent_roman-catechism_mchugh-callan1923.txt` lines 812–830 (opened: "the further claim that the catechism originated with Luther?" … "From the ninth century on, there have come down to us numerous works of popular instruction" … "the manual of Dhuoda to his son"). The narrator now says only what they did; no claim about who was taught.

2. **Keep one fact from her later reception, not three; prefer not to carry the 1887 claim.** Cut the 1700s Benedictine praise and the 1887 "oldest writing by a woman born in France" claim; kept the 1923 point (item 1), the outline's *Defended* item that bears on the book as a handbook of faith.
   - Cut: "Benedictine scholars of the 1700s called it "a monument of literature and piety worthy of respect". When the whole book was printed in 1887, its editor called it the oldest writing by a woman born in France to reach us."
   - The copying-and-authenticity sentence (I1) stays, as the book's survival, not as a reception fact (see across-the-set, "Yet").

3. **Make plain the baby was taken from her before baptism.**
   - Old: "In 841 she bore a second son, but before the child was baptized, Bernard had the baby brought to him with the bishop of Uzès."
   - New: "In 841 she bore a second son at Uzès. Before the child was baptized, Bernard had him taken from her and brought to him in Aquitaine, with the bishop of Uzès. When she wrote, she did not yet know the baby's name."
   - Source: E4 — DH (`cic/texts/dhuoda_liber-manualis_bondurand1887.txt`) 2232–2234, 2256–2261 (opened: born "in Uzecia urbe"; "antequam baptismatis accepisset gratiam … cum Elefanto, praedictae civitatis episcopo … in Aquitaniae partibus ad suam fecit adduci praesentiam"); E6 — DH 3172–3175 (opened: "cujus modo inscia sum nominis"). "Taken from her" is the plain fact the fix asks for; it follows the outline's Do not say (no "snatched", "stole" or "tore", and no complaint put in her mouth). The added name sentence is the outline's allowed form (E6).

4. **Recast "Hers, a noblewoman's, is one of very few voices…" as a plain contrast.**
   - Old: "Hers, a noblewoman's, is one of very few voices from the church of Charlemagne's heirs that does not belong to the clergy, and she claims her place as his teacher."
   - New: "Nearly every voice that survives from the church of Charlemagne's heirs belongs to one of the clergy. Hers belongs to a noblewoman, and she claims her place as his teacher."
   - Source: Outline Thread; S7 (CEN 42325, "one of very few lay voices to survive from the period"; CEN 42303–42305, "an aristocratic voice, not a non-elite one"). No further than the outline: "nearly every" restates "very few … not … clergy".

5. **Untangle the dictated-and-sent sentence.**
   - Old: "That November she began a handbook for William, which she dictated and had written out and sent, to be read as often as one looks in a mirror."
   - New: "That November she began a handbook for William. She dictated it and had it written out and sent to him, and she asked him to read it as often as one looks in a mirror."
   - Source: E8, E9 (DH 1895–1896, 11527–11529); T2 (DH 2155–2168, "ita te opto ut … hunc libellum a me tibi directum frequenter legere … velut in speculis").

## Across-the-set items

- **Setting stack:** "written in the 840s, at Uzès, a town in the south of France, in the Frankish empire that Charlemagne had built" → "written in the 840s at Uzès, a town in the south of France that was then part of the Frankish empire Charlemagne had built." Source: S2, S3, S6, S7.
- **"Yet" opening the impact:** "Yet the book was copied and kept, and because an early copy, now in fragments, agrees with a later one, scholars could show the text is hers." → "The book was copied and kept. An early copy survives in fragments, and a later one agrees with it, so her editors could show the text is hers." Source: I1 (DH 208–228; DH 402–410, opened: "N et P n'offrent entre eux aucune différence essentielle … hors de toute discussion").
- **No softening:** item 3 states the taking of the baby plainly; Bernard's execution and William's death stay as released.
- **Witness line / uncertainty tags:** none of the barred lines present; no change.

## Readability

`python -m engine.m1.profile_readability …/dhuoda.brief.txt`: 408 words (was 431; −5%), grade 6.9 (names out 6.2), reading ease (names out) 82.2, 17.7 words a sentence, longest sentence 29 words — pass, with the tool's note that grade 6.9 is under 8 and goes to the listener read.

## Quotations added or changed

None added. Removed: the Benedictine phrase "a monument of literature and piety worthy of respect" (with the cut in item 2). Q1, Q3, "in discord", "at my lord's command" and "the manual of Dhuoda" unchanged.
