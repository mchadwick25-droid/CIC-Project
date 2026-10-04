---
id: gallic.quote.massilians-clung-to-their-views
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
voice: analytic
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted as editorial transmission history, not as this world's own primary-source voice -
    this is the NPNF editor's (Gibson's) prolegomena account of the Massilians' response to Pope
    Celestine's letter, not a passage from Cassian, Sulpitius, or Vincent themselves.
sources:
- source_id: gallic.source.npnf-editorial-apparatus
  locus: "Gibson's prolegomena to Cassian (npnf211 div iv.i.i, file lines 15767-15770): the editor's account of the Massilian response to Celestine's letter"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks how the Marseilles monks responded to Rome's intervention in the grace controversy"
  prefer_instead:
  - "participant asks for a primary-source voice from within this world - this record is the modern editor's own framing, not Cassian's, Sulpitius's, or Vincent's words"
text: >-
  Never, perhaps, was Gallican independence shown in a more striking
  manner than in the sturdy way in which the Massilians clung to their
  views in spite of the authority of the Pope now brought to bear upon
  them.
speaker_or_author: Edgar C. S. Gibson, editorial prolegomena
license: verbatim
modern_lens_note: >-
  This sentence is not Cassian's, Sulpitius's, or Vincent's voice - it is the nineteenth-century
  editor's own framing of the episode, added to introduce the letter of Pope Celestine and the
  Massilian response to it. It is carried here because it is the source apparatus's most direct
  statement of the Marseilles community's resistance to Rome, useful as evidence of the episode but
  not as an emic voice of this world.
modern_rendering: >-
  Perhaps Gallican independence was never shown more strikingly than in
  the sturdy way the Massilians clung to their views. They held on even
  though the authority of the Pope was now brought to bear on them.
relations:
- type: associated-with
  target: gallic.gravity.authority-ambivalence
- type: associated-with
  target: gallic.gravity.grace-and-effort
- type: associated-with
  target: gallic.force.africa-and-rome-pressure
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"sturdy way"` returns one hit, line 15769, inside `<div3 title="Chapter I. The Life of Cassian." ...
id="iv.i.i">`, itself within `<div2 title="Prolegomena." ... id="iv.i">`. The sentence runs lines
15767-15770: "Never, perhaps, was Gallican independence shown in a more striking manner than in the
sturdy way in which the Massilians clung to their views in spite of the authority of the Pope now
brought to bear upon them."

Normalization: line breaks joined with single spaces. No word added, dropped, substituted, or
reordered.
