---
id: gallic.quote.martin-raises-the-catechumen
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F1-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Widely Accepted
  divergence_note: >-
    The wording is Widely Accepted as Sulpitius's own text (Vita ch. VII, read at its own locus for
    this record). The narrated event - a resurrection - is Inferential-Thin, carried here as the
    tradition's own account, not as this record's independent finding; the host record's own
    divergence_note and narrative_tier_justification (Tier 3, "the story is the wonder") state this at
    length and are not repeated in full here.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: "Life of St. Martin ch. VII (npnf211 div ii.ii.viii, file lines 977-1006): the monastery near Tours, the catechumen's death, and Martin's prayer over the body"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how Sulpitius himself tells the resurrection of the catechumen"
  - "participant asks what Martin actually did with the body - the bolted door, the posture, the waiting"
  - "Representative needs the exact wording behind virtus as 'power present,' not owned"
  prefer_instead:
  - "participant is asking whether the miracle 'really happened' - this record carries Tier 3 register and does not assess that"
  - "participant wants the catechumen's own later testimony about the tribunal - retrieve gallic.quote.the-catechumens-testimony"
  - "participant wants the whole episode told as a story - retrieve gallic.story.raising-of-the-catechumen, which this record is drawn from"
text: >-
  As Hilarius had already gone away, so Martin followed in his footsteps; and having been most
  joyously welcomed by him, he established for himself a monastery not far from the town. At this
  time a certain catechumen joined him, being desirous of becoming instructed in the doctrines and
  habits of the most holy man. But, after the lapse only of a few days, the catechumen, seized with a
  languor, began to suffer from a violent fever. It so happened that Martin had then left home, and
  having remained away three days, he found on his return that life had departed from the catechumen;
  and so suddenly had death occurred, that he had left this world without receiving baptism. The body
  being laid out in public was being honored by the last sad offices on the part of the mourning
  brethren, when Martin hurries up to them with tears and lamentations. But then laying hold, as it
  were, of the Holy Spirit, with the whole powers of his mind, he orders the others to quit the cell in
  which the body was lying; and bolting the door, he stretches himself at full length on the dead limbs
  of the departed brother. Having given himself for some time to earnest prayer, and perceiving by
  means of the Spirit of God that power was present, he then rose up for a little, and gazing on the
  countenance of the deceased, he waited without misgiving for the result of his prayer and of the
  mercy of the Lord. And scarcely had the space of two hours elapsed, when he saw the dead man begin to
  move a little in all his members, and to tremble with his eyes opened for the practice of sight. Then
  indeed, turning to the Lord with a loud voice and giving thanks, he filled the cell with his
  ejaculations. Hearing the noise, those who had been standing at the door immediately rush inside. And
  truly a marvelous spectacle met them, for they beheld the man alive whom they had formerly left dead.
speaker_or_author: "Sulpitius Severus, narrating"
license: verbatim
modern_lens_note: >-
  A modern reader looking for the moment of the miracle itself may expect drama - an incantation, a
  visible sign. Sulpitius gives the opposite: silence, a bolted door, a man lying full length on a
  corpse, and a wait "without misgiving." The power is "perceived" as present before anything visibly
  changes; the two hours pass in stillness, not spectacle. What the passage stages is not a display of
  power but a posture toward it - present, not summoned.
relations:
- type: associated-with
  target: gallic.story.raising-of-the-catechumen
- type: associated-with
  target: gallic.figure.martin
- type: associated-with
  target: gallic.figure.sulpitius
- type: associated-with
  target: gallic.quote.the-catechumens-testimony
---
Verified against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n "As Hilarius
had already"` returns one hit, line 977; `grep -n "power was present"` returns one hit, line 996-997
(split across a footnote insertion in the XML, "power was present,<note.../>"); `grep -n "whom they had
formerly left dead"` returns one hit, line 1006. The chapter div is `<div3 title="Chapter VII. Martin
restores a Catechumen to Life." ... id="ii.ii.viii">` (line 971). Read lines 977-1006 directly: one
continuous paragraph, nothing skipped, from the chapter's opening sentence through "the man alive whom
they had formerly left dead."

Normalization: line breaks joined with single spaces. The footnote marker after "power was present" (a
translator's endnote giving the Latin "adesse virtutem") was dropped as apparatus, not text; it is
separately disclosed in the host record's own sources[] entry for the editorial apparatus. No word was
added, dropped, substituted, or reordered.
