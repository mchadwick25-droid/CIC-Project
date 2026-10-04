---
id: witt.quote.nothing-that-varies
world_id: lutheran-wittenberg-and-its-congregations
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-E
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as the Augsburg Confession's own Conclusion, read before the Emperor at the same 1530 Diet
    witt.story.diet-of-augsburg-1530 already verifies. This is the confession's own closing argument for
    its own continuity, addressed to the Emperor directly, not a later apologetic claim made about it.
sources:
- source_id: witt.source.melanchthon-augsburg-confession
  locus: "Conclusion, following Article XXVIII (cic:melanchthon_augsburg-confession_anon-pg275.txt lines 1543-1550): 'nothing has been received on our part against Scripture or the Church Catholic'"
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks how we know our own practices go back to the apostles, or are not later inventions"
  - "participant asks whether we broke with the ancient Church or only with certain abuses"
  prefer_instead:
  - "participant wants a specific practice defended point by point -- this is the Confession's own summary claim, not an item-by-item case"
text: >-
  Nor has anything been here said
  or adduced to the reproach of any one. Only those things have been
  recounted whereof we thought that it was necessary to speak, in order
  that it might be understood that in doctrine and ceremonies nothing has
  been received on our part against Scripture or the Church Catholic. For
  it is manifest that we have taken most diligent care that no new and
  ungodly doctrine should creep into our churches.
speaker_or_author: "the Augsburg Confession's own Conclusion -- the same corporate voice and the same signatories as the confession signed at the 1530 Diet of Augsburg"
license: verbatim
modern_lens_note: >-
  A modern reader may expect a reform movement to claim it is doing something new, correcting the past by
  replacing it. This confession claims almost the opposite: that "nothing has been received on our part
  against Scripture or the Church Catholic," and that its own diligence has been spent keeping new and
  ungodly doctrine OUT, not bringing it in. We are not claiming a direct chain of ordination back to the
  apostles the way some other traditions argue continuity; we are claiming a continuity of teaching -- that
  what is taught agrees with Scripture and with the universal Church's own older custom, not that no
  practice changed at all. The abuses this same document elsewhere names as corrected are real changes;
  the claim here is that correcting them is not the same thing as inventing a new religion.
modern_rendering: >-
  Nothing here has been said to shame or blame anyone. We have only set out what we thought needed to be
  said, so that it would be understood: in what we teach and in how we worship, we have received nothing
  on our part against Scripture or the universal Church. It is clear that we have taken the most diligent
  care that no new and ungodly doctrine should creep into our churches.
relations:
- type: associated-with
  target: witt.dw.nothing-against-scripture-or-the-church-catholic
use_note:
  means: "The Augsburg Confession's closing Conclusion (1530) claims nothing in its doctrine or ceremonies was received against Scripture or the Church Catholic, and no new doctrine admitted."
  not_for:
    - "a claim of an unbroken chain of ordination back to the apostles"
    - "a claim that no practice changed, when the same document names abuses it corrected"
    - "the definition of what a church is, which sits in witt.quote.congregation-of-saints"
    - "the Article XXI summary that our doctrine varies from neither Scripture, the Church Catholic, nor Rome's writers, a separate passage carried in witt.term.scripture-against-tradition"
  years: {from: 1530, to: 1530}
  status: reviewed
---
The quoted span is checked against cic/texts/melanchthon_augsburg-confession_anon-pg275.txt. The Conclusion
heading is at line 1531, after Article XXVIII (line 1271), the last article of the confession. The span runs
from "Nor has anything been here said" (line 1543, mid-line) through "creep into our churches." (line 1550).
Lines 1540-1543 hold two earlier sentences, about disputes between pastors and monks, and are left outside `text`.
No word is added, dropped, substituted or reordered within the span.

The id is a historical label. The words "nothing that varies from the Scriptures, or from the Church
Catholic" are from the end of Article XXI (line 632), a separate passage. This record quotes the Conclusion,
which follows Article XXVIII.

Ground for witt.dw.nothing-against-scripture-or-the-church-catholic (F4-E: how do you know your practices
went back to the apostles and weren't later inventions). Kept distinct from
witt.quote.congregation-of-saints (Article VII's own definition of what a church is, F3-T) -- this record
is the Confession's own argument that ITS OWN teaching does not depart from that universal Church or from
Scripture, the continuity claim rather than the definition. Reciprocal associated-with declared on
witt.dw.nothing-against-scripture-or-the-church-catholic.
