---
id: gallic.quote.abundance-of-power-not-granted-as-bishop
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
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted as Gallus's own report, in Sulpitius's Dialogues (II.4, read at its locus for
    this record), of what Martin was accustomed to say about his own power as bishop compared to
    before. Reported speech at one remove, addressed by Gallus to Sulpitius within the dialogue.
sources:
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: "Dialogues II.4 (npnf211 div ii.iv.ii.iv, file lines 4038-4041): Gallus telling Sulpitius
    what Martin used to say about having less power as bishop than he remembered having before"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether Martin's own power changed after he became bishop"
  - "participant asks how this world's own literature registers office as a cost, not only a gain"
  prefer_instead:
  - "participant wants the coerced-communion diminution instead - retrieve a Dial. III.13 record where one exists"
text: >-
  I have often noticed this, Sulpitius, that Martin was accustomed to
  say to you, that such an abundance of power was by no means granted
  him while he was a bishop, as he remembered to have possessed before
  he obtained that office.
speaker_or_author: "Gallus, addressing Sulpitius, in Sulpitius's Dialogues"
license: verbatim
modern_lens_note: >-
  This is Gallus's own report of a habitual remark Martin made, not a single dated statement - "was
  accustomed to say" marks it as something Martin returned to more than once. The comparison is
  Martin's own: less power felt present as bishop than he remembered having as a monk, before the
  office.
modern_rendering: >-
  I have often noticed this, Sulpitius, that Martin was accustomed to say to you, that such an
  abundance of power was by no means granted him while he was a bishop, as he remembered to have
  possessed before he obtained that office.
relations:
- type: associated-with
  target: gallic.gravity.virtus
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"such an abundance"` returns line 4038; read with `sed -n '4034,4042p'`, inside `<div4 ...
id="ii.iv.ii.iv">` (Dialogues II, Chapter IV, opening sentence). The quoted span is one complete
sentence, "I have often noticed this, Sulpitius..." through "...obtained that office.", ending at
its own period.

Normalization: line breaks joined with single spaces; a translator's endnote glossing "such an
abundance [of power]" as Latin "eam virtutum gratiam" sits inside the source's own sentence and is
apparatus, excluded per the fleet's own `<note>`-stripping convention. No word was added, dropped,
substituted, or reordered.

speaker_or_author is a plain string, not gallic.figure.martin: the words are Gallus's own report of
what Martin used to say, addressed to Sulpitius within the dialogue, not Martin's own direct speech.
