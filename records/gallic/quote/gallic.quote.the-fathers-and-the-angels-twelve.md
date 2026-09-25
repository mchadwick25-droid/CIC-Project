---
id: gallic.quote.the-fathers-and-the-angels-twelve
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-E
- F4-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted for the tradition and its transmission - Documented as Cassian's own text
    (Institutes II.5-6, read at its locus for this record), written for Castor's new Gallic house.
    Contested for the specific attribution: the angel's appearance is the tradition's own claim about
    its origin, and Cassian does not claim to have seen it or heard it from a named witness - he refers
    the reader elsewhere to "ecclesiastical history." The wording is what the fathers of Egypt are said
    to have handed on; the event itself is not independently attested here.
sources:
- source_id: gallic.source.cassian-institutes
  locus: "Institutes II.5-6 (npnf211 divs iv.iii.ii.v-vi, file lines 17140-17232): the fathers' meeting, the dispute over fifty or sixty psalms, the chanter's twelve and his disappearance, and the decree that followed"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks why the monks sang twelve psalms, where the office came from, or whether the monks made their own rule"
  - "participant asks about the fathers' dispute over the number of psalms, or an angel fixing a monastic custom"
  prefer_instead:
  - "participant is asking about Martin's angels (retrieve gallic.term.angels)"
  - "participant wants the desert's own founding narratives as such - this is Egypt's story, and the origin must be disclosed, never presented as Gaul's"
text: >-
  when only a few, and those the best of men, were known by the name of monks, ... when the perfection
  of the primitive Church remained unbroken ... and when the fervent faith of the few had not yet grown
  lukewarm by being dispersed among the many, the venerable fathers with watchful care made provision
  for those to come after them, and met together to discuss what plan should be adopted for the daily
  worship throughout the whole body of the brethren, ... send forth a poisonous root of error or
  jealousy or schism among those who came after. ... in proportion to his own fervour--and unmindful of
  the weakness of others, ... some were for fifty, others sixty, and some, not content with this
  number, thought that they actually ought to go beyond it. ... such a holy difference of opinion in
  their pious discussion on the rule of their religion that the time for their Vesper office came
  before the sacred question was decided. ... One rose up in the midst to chant the Psalms to the Lord.
  And while they were all sitting ... with their minds intently fixed on the words of the chanter, when
  he had sung eleven Psalms, separated by prayers introduced between them, verse after verse being
  evenly enunciated, he finished the twelfth with a response of Alleluia, and then, by his sudden
  disappearance from the eyes of all, put an end at once to their discussion and their service.
  Whereupon the venerable assembly of the Fathers understood that by Divine Providence a general rule
  had been fixed for the congregations of the brethren through the angel's direction, and so decreed
  that this number should be preserved both in their evening and in their nocturnal services; ... they
  added ... simply as extras and of their own appointment.
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  A modern reader assumes a community's rule of prayer is something its founders decided. The fathers
  of Egypt, as Cassian tells it, could not decide - they argued past sundown, "some were for fifty,
  others sixty" - and the number that held is the one nobody chose. The two extra lessons the fathers
  added afterward, by contrast, are named plainly as human work: "simply as extras and of their own
  appointment." The distinction is the point - between what the fathers received and what they merely
  arranged.
modern_rendering: PENDING_OPUS_RENDERING
relations:
- type: associated-with
  target: gallic.story.the-angel-and-the-twelve-psalms
---
Verified directly against the vendored cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml.
The chapter divs are `<div4 title="Chapter V. How the fact that the number of the Psalms was to be
twelve was received from the teaching of an angel." ... id="iv.iii.ii.v">` (line 17133) and `<div4
title="Chapter VI. Of the Custom of having Twelve Prayers." ... id="iv.iii.ii.vi">` (line 17219).
`grep -n "only a few, and those the best"` returns one hit, line 17141. Each clause of the excerpt was
read in place across lines 17140-17232 and matches the source exactly; the ellipses mark connective
narration omitted between clauses - the Evangelist Mark and the primitive Jerusalem church (lines
17142-17171), "and was still preserved fresh in the memory by their followers and successors" (line
17172-17173), the reasons the fathers feared a dispute (lines 17178-17184), "And when each man ...
thought that that should be appointed which he judged was quite easy..." (lines 17184-17191), "there
was" before "such a holy difference" (line 17193), "and, as they were going to celebrate their daily
rites and prayers," before "One rose up" (lines 17196-17197), the parenthetical "(as is still the
custom in Egypt)" (line 17198), and "them" before "simply as extras" (line 17231). No word was added,
substituted, or reordered within any retained clause.

Normalization: the source hard-wraps prose at fixed widths; line breaks were joined with single spaces.
The em dashes around "and unmindful of the weakness of others" are the source's own punctuation and are
kept.

speaker_or_author is gallic.figure.cassian: this is Cassian's own narration throughout, not a quoted
elder's speech; no individual father or the chanter is named.
