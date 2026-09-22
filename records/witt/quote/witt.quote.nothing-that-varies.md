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
  locus: "Conclusion, following Article XXI (cic:melanchthon_augsburg-confession_anon-pg275.txt lines 1540-1550): 'nothing has been received on our part against Scripture or the Church Catholic'"
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
  said. We want it understood: in what we teach, and in how we worship, we have not taken up anything
  against Scripture. We have not taken up anything against the universal Church. We have, in fact, taken
  the greatest care. We have worked to keep new or godless teaching from creeping into our churches.
relations:
- type: associated-with
  target: witt.dw.nothing-against-scripture-or-the-church-catholic
---
Verified verbatim at this step (Answer-the-Canon pass, inserted between B-7a and B-8) directly against
the vendored cic/texts/melanchthon_augsburg-confession_anon-pg275.txt. `grep -n "nothing has been received
on our part\|no new and\|Article XXI: Of the Worship"` returns the Article XXI heading at line 618 (the
article this Conclusion immediately follows), "been received on our part against Scripture or the Church
Catholic. For" at line 1548, and "it is manifest that we have taken most diligent care that no new and" at
line 1549. `sed -n '1540,1550p'` confirms the passage read in its own paragraph: opening "right,
confessions, burials, sermons on extraordinary occasions, and" at 1540 (the end of the prior sentence,
left outside `text`) through "ungodly doctrine should creep into our churches." at 1550. The `text` field
begins at "Nor has anything been here said" (line 1543) rather than at 1540, since 1540-1542 continue an
unrelated prior sentence about specific abuses (confessions, burials, sermons) that is not part of the
continuity claim itself; the quoted span runs from "Nor has anything" (1543) through "creep into our
churches." (1550) as one continuous, self-contained paragraph. No word added, dropped, substituted, or
reordered within that span.

Ground for witt.dw.nothing-against-scripture-or-the-church-catholic (F4-E: how do you know your practices
went back to the apostles and weren't later inventions). Kept distinct from
witt.quote.congregation-of-saints (Article VII's own definition of what a church is, F3-T) -- this record
is the Confession's own argument that ITS OWN teaching does not depart from that universal Church or from
Scripture, the continuity claim rather than the definition. Reciprocal associated-with declared on
witt.dw.nothing-against-scripture-or-the-church-catholic.

CORRECTION (Phase C recon, 2026-09-19): speaker_or_author's own raw reference to
"witt.story.diet-of-augsburg-1530" replaced with plain prose ("the confession signed at the 1530 Diet of
Augsburg") -- caught by engine.m1.cross_world's check_quote_speaker_labels, which correctly flags this
field as one both the Level-3 citation card and the compiled prompt's quote index print verbatim to a
participant. Substance unchanged, only the internal record-id reference removed.
