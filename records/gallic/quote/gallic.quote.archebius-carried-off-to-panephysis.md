---
id: gallic.quote.archebius-carried-off-to-panephysis
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F6-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted: this is Cassian's own first-person account - "when we arrived there ... God
    gratified our wishes" - in a work Widely Accepted as to authorship, addressees, and date (not later
    than 426). No independent witness to Archebius exists outside Cassian's own writings (Gibson,
    editorial). The interval between the journey and the writing down of this Conference is not stated
    in the text and not computed here.
sources:
- source_id: gallic.source.cassian-conferences-part-ii
  locus: "Conferences XI.2 (npnf211 div iv.v.ii.ii, file lines 36807-36825): Cassian and Germanus's arrival at Thennesus and the bishop who met them"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how Cassian describes meeting Bishop Archebius, or what an Egyptian monk-turned-bishop's story sounded like"
  - "participant uses 'reluctant bishop', 'carried off', or 'unworthy'"
  prefer_instead:
  - "participant wants Archebius's own words to the travelers - retrieve gallic.quote.archebius-see-the-old-men instead, or alongside"
  - "participant is asking about Gallic bishops as such - this is an Egyptian bishop's story, told by the man who founded Marseilles's houses"
text: >-
  And when we arrived there, God gratified our wishes, and had brought about the arrival of that most
  blessed and excellent man Bishop Archebius, who had been carried off from the assembly of anchorites
  and given as Bishop to the town of Panephysis, and who kept all his life long to his purpose of
  solitude with such strictness that he relaxed nothing of the character of his former humility, nor
  flattered himself on the honour that had been added to him (for he vowed that he had not been
  summoned to that office as fit for it, but complained that he had been expelled from the monastic
  system as unworthy of it because though he had spent thirty-seven years in it he had never been able
  to arrive at the purity so high a profession demands);
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  A modern reader hears "reluctant bishop" as a pious convention, a modesty formula. Archebius's
  complaint, as Cassian records it, is not modesty: he counts thirty-seven years in the monastic life
  and names his consecration an expulsion from it "as unworthy" - a loss, not an honor, even after he
  has held the office his whole remaining life without relaxing his old strictness.
modern_rendering: >-
  When we got there, God granted our wishes. He had brought that most blessed and excellent man,
  Bishop Archebius, to the same place. Archebius had been carried off from the community of hermits
  and given as bishop to the town of Panephysis. All his life he kept to his commitment to solitude,
  so strictly that he loosened nothing of his old humility. Nor did he flatter himself over the honor
  that had been added to him. He insisted that he had not been called to that office because he was
  fit for it. Instead he complained that he had been thrown out of the monks' way of life as unworthy
  of it. For though he had spent thirty-seven years in it, he had never reached the purity so high a
  calling demands.
relations:
- type: associated-with
  target: gallic.story.bishop-archebius
use_note:
  means: "Cassian recounts meeting Bishop Archebius, taken from the anchorites to be bishop of Panephysis, who kept his solitary strictness and called his election an expulsion."
  not_for:
    - "Archebius's own words to the travellers, which sit in gallic.quote.archebius-see-the-old-men"
    - "a claim independently attested outside Cassian's own writings"
    - "a modesty formula, when Cassian presents the complaint as a real loss"
  years: {from: 426, to: 426}
  status: provisional
---
Verified directly against the vendored cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml.
`grep -n "Archebius"` locates the passage at `<div4 title="Chapter II. Of Bishop Archebius." ...
id="iv.v.ii.ii">` (line 36801), paragraph `iv.v.ii.ii-p2` (lines 36807-36839). The quoted span runs
verbatim and unbroken from "And when we arrived there, God gratified our wishes" (line 36807) through
"the purity so high a profession demands)" (line 36825), where the parenthesis closes the sentence. One
editorial endnote (n. 1687, on Archebius's other appearances in Cassian, and the note that he is "not
known to us from any other source") falls inside the phrase "Bishop Archebius" and is dropped as
apparatus.

Normalization: the source hard-wraps prose at fixed widths; line breaks were joined with single spaces.
No word was added, dropped, substituted, or reordered. The remainder of the sentence - Cassian's own
account of being received "kindly and most graciously" and Archebius's spoken reply - continues
directly after and is carried in gallic.quote.archebius-see-the-old-men.

speaker_or_author is gallic.figure.cassian: this is Cassian's own first-person narration of the
encounter, not Archebius's reported speech.
