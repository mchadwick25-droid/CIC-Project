---
id: witt.figure.brussels-martyrs-john-and-henry
world_id: lutheran-wittenberg-and-its-congregations
record_type: figure
schema_version: 2
status: draft
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: 'Documented that two named monks, John and Henry, were burned at Brussels for refusing
    to recant an evangelical teaching; the event is Tier 1 in Doc_09''s own classification, datable and
    attested by a near-contemporary author. Contested to Inferential-Thin for anything beyond the bare
    fact of their names and their deaths: the ballad that is this library''s only source for them is composed
    in a hagiographic, commemorative register, and supplies no family name, age, or biographical detail
    for either man beyond "John" and "Henry." "Augustinian" does not occur anywhere in the vendored text
    in connection with them; the Registry''s own technical correction (2026-09-15) fixed an earlier, unverified
    "Augustinian friars" wording to what the text actually supports (Doc_09 witt-S04; Source Registry
    R30).'
sources:
- source_id: witt.source.luther-ein-neues-lied-wir-heben
  locus: Hymn V's own heading and stanzas 1-6, naming "one of these youths... called John, and Henry was
    the other," their burning at Brussels, and the ballad's own commemorative account of their end
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - a participant asks who the two Brussels martyrs were
  - a participant asks whether this world can name anyone who died for its teaching
  prefer_instead:
  - drawing any individual distinction between John and Henry - the vendored text gives them no individually
    distinguishing detail beyond their two names and their shared fate
  - narrating either man's age, family, or personal history - none is attested
names:
- name: John and Henry, the two young monks burnt at Brussels
  tag: in-world
- name: Hendrik Vos and Johann van Esschen (identification made outside this library's own vendored text;
    not this text's own naming)
  tag: scholarly
dates:
  display: Burned at Brussels 1 July 1523 - the year Hymn V's own printed heading gives as "MDXXII," corrected
    by Bacon's own bracketed editorial note to "[July 1, 1523]," the date this record follows. No vendored
    source gives either man's birth date or age.
narratable: true
bridge_line: Two young monks, John and Henry, burned at Brussels in 1523 for refusing to recant - the
  only two people in this whole library's record whom the movement's own teaching is shown to have cost
  their lives, and the subject of Luther's only martyr-ballad.
relations:
- type: associated-with
  target: witt.story.brussels-martyrs
- type: associated-with
  target: witt.gravity.justified-by-faith-alone
- type: associated-with
  target: witt.gravity.estate-office-and-calling
---
Narratable: true as a pair, and only as a pair - the boundary this record holds to deliberately, per
this project's own discipline against inventing individual distinction the source does not supply. The
vendored ballad names both men and states plainly that they died together, for the same refusal, on the
same day; it gives no line, image, or reported word that belongs to one of them rather than the other.
Building two separate figure records, or narrating one as somehow more central than the other, would
manufacture a distinction the source itself never draws. This single record accordingly stands for both
men together, exactly as the ballad itself presents them.

What is documented: two named monks, burned at Brussels on 1 July 1523, after examination by Louvain
theologians, for refusing to give up an evangelical teaching. What is not documented, anywhere in this
library: either man's age, family name, order beyond what the ballad itself implies ("their monkish
garb... and gown of ordination" taken from them before the burning - the vendored text's own words,
not a stated religious order by name), or any individually attributed word, thought, or action. The
scholarly identification sometimes given outside this library (Hendrik Vos and Johann van Esschen, as
Augustinian friars) is not this library's own text and is carried here, in names[], only as a disclosed
external identification - never narrated as though the vendored ballad itself supplied it.

FEC / GRAVITY LINKAGE (closed at B-5): the connection this record's own Doc_09 entry named above is now a real relations[] entry in this file's frontmatter -- associated-with to G1 (Justified by faith alone [PRIMARY]), G7 (Estate, office, and calling: "we are all priests" [SUPPORTING]) -- with the reciprocal edge declared on each gravity record itself (witt.gravity.*), exactly as this note said it would when B-5 ran. No longer parked.

CORRECTION (Phase C recon, 2026-09-19): dates.display's own "Doc_09 and" removed -- caught by
engine.m1.cross_world's check_participant_field_leaks, which correctly flags this field as one the
doorway's Level-3 panel prints verbatim to a participant. The citation was accurate but belonged in this
body note, not in a field a participant reads; substance unchanged, only the internal build-document
reference removed.
