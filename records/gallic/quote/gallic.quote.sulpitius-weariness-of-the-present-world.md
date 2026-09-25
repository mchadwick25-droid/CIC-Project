---
id: gallic.quote.sulpitius-weariness-of-the-present-world
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: >-
    Documented as Sulpitius's own text (Letter II, read at its locus for this record) - his own
    first-person account of his state of mind before a vision of Martin.
sources:
- source_id: gallic.source.sulpitius-letters
  locus: "Letter II, to the Deacon Aurelius (npnf211 div ii.iii.ii, file lines 2148-2154):
    Sulpitius's own state of mind - hope, weariness, dread of judgment - before his vision of
    Martin"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how judgment felt from the inside, in this world's own north"
  - "participant asks what Sulpitius himself was thinking or feeling in his own letters"
  prefer_instead:
  - "participant wants the vision the letter goes on to describe - retrieve the fuller Letter II narrative, not this opening state of mind alone"
text: >-
  After you had departed from me in the morning, I was sitting alone
  in my cell; and there occurred to me, as often happens, that hope of
  the future which I cherish, along with a weariness of the present
  world, a terror of judgment, a fear of punishment, and, as a
  consequence, indeed as the source from which the whole train of
  thought had flowed, a remembrance of my sins, which had rendered me
  worn and miserable.
speaker_or_author: gallic.figure.sulpitius
license: verbatim
modern_lens_note: >-
  Sulpitius names four things together, in one breath - hope, weariness, dread, fear - and then
  traces them back to a single root: his own remembrance of his sins. Judgment here is not an
  abstract doctrine; it is a mood he describes feeling, alone in his cell, on an ordinary morning.
modern_rendering: >-
  You left me in the morning, and after that I was sitting alone in my cell. Then, as often
  happens, the hope of the future that I cherish came to my mind. With it came a weariness of the
  present world, a terror of judgment, and a fear of punishment. As a result came a remembrance
  of my sins, which had left me worn and miserable. Indeed, that remembrance was the source from
  which this whole train of thought had flowed.
relations:
- type: associated-with
  target: gallic.gravity.judgment-imminent-present
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"After you had departed"` returns line 2148; `grep -n "rendered me worn and miserable"` returns
line 2154. Read with `sed -n '2145,2156p'`, inside `<div3 ... id="ii.iii.ii">` ("Letter II. To the
Deacon Aurelius."). The quoted span is one complete sentence, "After you had departed..." through
"...worn and miserable.", ending at its own period.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.

This span was previously carried, unresolved, inside gallic.gravity.judgment-imminent-present's
own `description` field. The host record now paraphrases it in its own voice
and points here for the verbatim wording.
