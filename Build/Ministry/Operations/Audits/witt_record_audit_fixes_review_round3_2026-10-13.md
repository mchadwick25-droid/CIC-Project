Review round 3 (final targeted recheck), witt record audit fixes, 2026-10-13, reviewer: independent Opus subagent

Verdict: BLOCKING (one item, finding 1). The other three rewritten fields are sound.

Scope: the readability rewrite of the `description` field in four records: witt.force.confessional-territorial-transformation, witt.force.imperial-frame, witt.force.territorial-princely-force and witt.gravity.promise-and-sign. HEAD (`git show HEAD:<path>`) was compared with the working tree using `git diff --word-diff`. Every hunk falls inside `description`; no other field changed. Each sentence was checked for dropped or added content, for hedges split away from their claims, and for citations moved off their claims. Cited loci were re-read in cic/texts/ (melanchthon_augsburg-confession_anon-pg275.txt, luther_large-catechism_bente-dau1921.txt, luther_works-v2-selected_jacobs-spaeth1916.txt).

Readability (engine.m1.gates.grade_text, whole description, HEAD -> working tree):

| Record | HEAD FK / FRE | Now FK / FRE |
|---|---|---|
| confessional-territorial-transformation | 9.6 / 58.5 | 8.2 / 62.0 |
| imperial-frame | 9.7 / 59.7 | 8.1 / 64.0 |
| territorial-princely-force | 9.7 / 56.9 | 8.0 / 61.4 |
| promise-and-sign | 9.8 / 56.3 | 7.9 / 61.0 |

All four pass FK <= 10 and FRE >= 60.

## Findings

1. **witt.force.imperial-frame, description para 4**: BLOCKING (qualifier moved onto a different referent)
   - Old: `The frame gave the papal force, in its initiating phase, a space where refusing the papacy could be put into practice, not just argued.`
   - New: `In its initiating phase, the frame gave the papal force a space where refusing the papacy could be put into practice, not just argued.`
   - Problem: in the old text "in its initiating phase" qualifies the papal force. That is the separate record witt.force.papal-force-initiating (1517-1521), which territorial-princely-force also cites as `enabled-by`. Fronted before "the frame", "its" now reads as the frame's own initiating phase. The imperial frame is itself `kind: initiating`, so the new reading is plausible, and it is a different claim. The phase that bounded the papal force is now a phase of the frame, and the link to the papal-force-initiating record is lost.
   - Fix: either restore the HEAD wording, or split it so the referent is fixed: `The papal force was then in its initiating phase. The frame gave it a space where refusing the papacy could be put into practice, not just argued.` Re-run grade_text after the fix.

2. **witt.force.territorial-princely-force, description para 1**: NON-BLOCKING (hedge scope narrowed, no overclaim)
   - Old: `Luther's Secular Authority, dedicated to Duke John and preached before him at Weimar, is well documented as the movement's own teaching about the state.`
   - New: `Luther's Secular Authority was dedicated to Duke John and preached before him at Weimar. It is well documented as the movement's own teaching about the state.`
   - The dedication and the Weimar preaching were inside the "well documented" sentence. They are now a bare statement. This adds no caution and loses none: "well documented" is the strongest grade, and the record's formation_confidence is Documented for the doctrine (divergence_note). The sources[0] locus covers both facts. Optional tightening: `It is well documented, as the movement's own teaching about the state.` or `All this is well documented. It is the movement's own teaching about the state.`

3. **witt.force.confessional-territorial-transformation, description para 4**: NON-BLOCKING (referent slightly widened)
   - Old: `...the pair of confessional documents and the two catechisms, which entered the Book of Concord in 1580 by reference.`
   - New: `...the pair of confessional documents and the two catechisms. These entered the Book of Concord in 1580 by reference.`
   - "These" can be read as all four documents, where "which" most naturally bound to the catechisms. Historically all four did enter the Book of Concord, so the wider reading is not false. Optional: `The two catechisms entered the Book of Concord in 1580 by reference.`

4. **witt.force.territorial-princely-force, description para 2**: NON-BLOCKING, carried and outside this rewrite
   - `Yet the same petition names the hunger this force could cause. That is the case when nobles "let the parishes decay... " (LC 92-97).` The quotation is verbatim at LC l.95-97, and the citation still sits with it. But LC 92-97 is the Large Catechism's preface, not the Fourth Petition. So "the same petition" was already wrong at HEAD; this rewrite did not introduce it. Suggest `The catechism's preface names the hunger...` the next time the record is opened, or register it in Open_Gaps_Tracking.

## Changes checked and found sound

- **territorial-princely-force para 1**: the corrected facts are kept: `In 1522 Duke George banned the September Testament. In March 1523 he complained to the Elector about Luther's Secular Authority. These events are widely accepted.` "These events" follows straight after and still covers both events. "is also widely accepted" (Teutonic Order) and "is well documented" (the Council's call) each stay in their own sentence with their claim.
- **territorial-princely-force para 2**: `this was no market at work. It was a sin against the neighbour's bread.` keeps "Seen from inside this world" on the first sentence, which carries the claim. The quotes and citations are unchanged and verbatim: v2 14764-14765 ("obtained the aid of the authorities"), AC 411-428 ("lawful civil ordinances are good works of God"), LC 3535-3541 ("bad coin ... raising of prices").
- **territorial-princely-force para 3**: `was for. By then the territorial church had parishes to inspect` and `marriage. The ban on the German Testament...`: these are clean splits, and "unattested" is kept.
- **imperial-frame para 1**: a clean split. "eventual legal shape was territorial. It was settled prince by prince" adds nothing.
- **imperial-frame para 2**: `the Confession's nine signatories (AC 1557-1567). These are an Elector, princes, and two city senates.` The citation moved from after "senates" to after "signatories". It still covers the whole list: AC l.1559-1567 has John, Elector, five more princes, and the Senate of Nuremberg and Senate of Reutlingen. That is nine. "the Christian Nobility of the German Nation" is kept verbatim (v2 l.1797, l.1881).
- **imperial-frame para 4, second half**: `the loaf. With the loaf came the household's daily prayer` is a clean split.
- **confessional-territorial-transformation paras 2-4**: "rather than" became "not", and two splits were made at "so" and "When". "This record does not claim ...", "harder to pin down" and "is limited to" are all untouched. `legitimate. When it matters most, the world's public voice belongs to princes.` keeps the condition on its claim. The 1520 quotation is kept.
- **promise-and-sign**: the corrected sacrament citation (v2 6695-6701; 10362-10364) sits in an unchanged sentence and is verified: "deny that there are seven sacraments, and hold for the present to but three" (l.6695-6696), and "but two sacraments ... baptism and bread" (l.10362). The split sentences keep every qualifier on its claim:
  - "at least as the movement itself described that practice" and "only a thin inference" are untouched.
  - `It strengthens vows, chastity, and marriage too, though only thinly.` still carries "only thinly".
  - `The doctrine and the movement's own claimed practice are well documented, while the one witness who took part, Johann Walter, is widely accepted.` keeps both grades on their own subjects.
  - `the evidence is as strong as what we claim. Both are well documented.` is sound, as is `The evidence for parish practice is still thin`.
  - `We also have one participant, writing late. We have nothing from any parish outside Wittenberg.` is sound.
  - `The Reformed rival pressed on it from outside. In the library that rival shows up only through the bodily presence in the Supper.` drops "though", but the limit ("only through") stays on its claim.
  - "Much else rests on it. These are the five parts ..." and "It explains why ..." each restate the colon list they replace. Neither adds an item.
  - "abolition. By 1530 it had become a defense of a retained Mass" keeps the quoted "retained" (AC 787-799 locus unchanged).
- No new name, date, number or inference was found in any of the four fields.

## Resolution

The blocking item (the orphaned "its initiating phase" in witt.force.imperial-frame) was fixed after this round by the split the review proposed. The non-blocking notes are registered in OG-69.
