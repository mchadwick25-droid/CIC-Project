---
id: ijc.quote.the-rudiments-of-the-creed
world_id: imperial-juridical
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F2-T
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Leo's own words in the standard English of the NPNF Leo volume, read directly at the line cited. One editorial footnote stands inside the quoted run in the vendored file and is dropped; nothing else is altered.
sources:
- source_id: ijc.source.leo-letters
  locus: >-
    Letter XXVIII (the Tome), sec. 1 (npnf212_leo-great-gregory-great.xml, from line 5099)
  license: public-domain
text: >-
  For what learning has he acquired about the pages of the New and Old Testament, who has not even grasped the rudiments of the Creed? And that which, throughout the world, is professed by the mouth of every one who is to be born again , is not yet taken in by the heart of this old man.
modern_rendering: >-
  This man has not even grasped the basics of the Creed. So what has he learned about the
  pages of the New and Old Testament? That which, throughout the world, is spoken by the
  mouth of everyone who is about to be born again is not yet taken into the heart of this
  old man.
speaker_or_author: Leo of Rome, Letter XXVIII (the Tome), sec. 1
license: verbatim
modern_lens_note: >-
  The order is the argument. Leo is not saying scripture is insufficient - a few lines later he faults Eutyches for not searching 'the length and breadth of the Holy Scriptures.' He is saying that a man who has not taken in the Creed is not equipped to read the Testaments at all, and the sequence he has in mind is baptismal rather than academic: 'every one who is to be born again' professes the confession before being baptised, so it is the first thing anyone learns and the frame every later reading happens inside. Asked whether the Bible was the only authority, this world would not have recognised the question: scripture and the confession were not two authorities to rank, they were a text and the mind you had to bring to it.
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks whether scripture was the only authority here"
  - "participant asks what a person had to know before they could read the Bible well"
  - "participant asks how the creed stood in relation to the Bible"
relations:
- type: associated-with
  target: ijc.term.tomus
use_note:
  means: "Leo's Tome faults Eutyches as unequipped to read the Testaments because he has not grasped the creed every baptismal candidate professes."
  not_for:
    - "a claim that Leo held scripture insufficient or subordinate"
    - "a claim that scripture and the creed were two competing authorities to be ranked"
  years: {from: 449, to: 449}
  status: provisional
---
Opened for F2-T, served by ijc.term.tomus alone. The instrument ruled this NEEDS READING
and was wrong: the record's locus is 'Ep. XXVIII (npnf212 line 5099)', which names a letter AND a line
number. The classifier's specific-locus pattern had no case for 'Ep.' and none for a bare line
reference, so it read one of the most precise loci in the corpus as vague.

The text carries the source's own space before the comma ("again ,").
No wording is changed.
