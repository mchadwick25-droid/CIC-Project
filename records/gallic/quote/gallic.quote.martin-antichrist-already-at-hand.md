---
id: gallic.quote.martin-antichrist-already-at-hand
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
    Documented as Sulpitius's own text (Vita ch. XXIV, read at its locus for this record) - his
    own inference from a run of false prophets, not an independent report of Martin's own words.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: "Life of St. Martin ch. XXIV (npnf211 div ii.ii.xxv, file lines 1784-1788): Sulpitius's
    inference, from false prophets claiming to be Elias, Christ, and John, that Antichrist's coming
    is near"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks why this world thought the end was close"
  - "participant asks what evidence convinced Sulpitius that Antichrist was coming"
  prefer_instead:
  - "participant wants Martin's own reported teaching on the same subject - retrieve gallic.quote.martin-antichrist-already-born"
text: >-
  We may infer from this, since false prophets of such a kind have
  appeared, that the coming of Antichrist is at hand; for he is already
  practicing in these persons the mystery of iniquity.
speaker_or_author: Sulpitius Severus, narrating
license: verbatim
modern_lens_note: >-
  This is Sulpitius's own reasoning, not a claim he attributes to Martin: a rash of men falsely
  claiming to be Elias, Christ, and John convinces him, by inference, that Antichrist himself must
  be near - already active, on this reading, inside the deceivers themselves.
modern_rendering: >-
  False prophets of this kind have appeared. From this we may infer that the coming of Antichrist
  is near. For he is already putting the mystery of iniquity into practice in these people.
relations:
- type: associated-with
  target: gallic.gravity.judgment-imminent-present
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"coming of Antichrist is at hand"` returns line 1786; read with `sed -n '1778,1789p'`, inside
`<div3 ... id="ii.ii.xxv">` (Chapter XXIV, printed heading "Chapter XXIV.", the div-id-vs-printed-
number offset this corpus's records consistently note). The quoted span is one complete sentence,
"We may infer..." through "...the mystery of iniquity.", ending at its own period.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.

speaker_or_author is a plain string, not a figure id: this is Sulpitius's own narratorial
inference, not reported speech from Martin or anyone else.

This span was previously carried, unresolved, inside gallic.gravity.judgment-imminent-present's
own `description` field. The host record now paraphrases it in its own voice
and points here for the verbatim wording.
