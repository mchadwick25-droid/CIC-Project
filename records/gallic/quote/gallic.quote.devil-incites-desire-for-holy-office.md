---
id: gallic.quote.devil-incites-desire-for-holy-office
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Abbot Moses's teaching within Cassian's First Conference (Conf. I.20), part of a
    catalogue of the devil's disguises. The teaching is presented in Cassian's own text as Moses's
    direct instruction to Cassian and Germanus.
sources:
- source_id: gallic.source.cassian-conferences-part-i
  locus: "Conference I, ch. XX (npnf211 div iv.iv.ii.xx, file lines 26944-26947): Abbot Moses on the devil's disguised temptations, illustrated by a good money-changer"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks why this world's monks were suspicious of wanting Church office"
  - "participant asks how Egyptian monastic teaching treated the desire for ordination"
  prefer_instead:
  - "participant asks about a specific historical case of a monk drawn into office - this record carries the general teaching, not a named case"
text: >-
  Or else when he incites a man to desire the holy office of the clergy
  under the pretext of edifying many people, and the love of spiritual
  gain, by which to draw us away from the humility and strictness of
  our life.
speaker_or_author: Abbot Moses, as Cassian records him (First Conference)
license: verbatim
modern_lens_note: >-
  "He" here is the devil, named a few sentences earlier in the same passage as the one who works
  through disguised, plausible-seeming suggestions rather than open temptation. Moses is not saying
  ordination itself is evil - he is warning that the wish for it can arrive dressed as a wish to do
  good for others, which is exactly what makes it dangerous to a monk trying to test his own motives.
modern_rendering: PENDING_OPUS_RENDERING
relations:
- type: associated-with
  target: gallic.gravity.authority-ambivalence
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"edifying many people"` returns one hit, line 26946, inside `<div4 title="Chapter XX. About
discerning the thoughts, with an illustration from a good money-changer." ... id="iv.iv.ii.xx">`, itself
within `<div3 title="Conference I. First Conference of Abbot Moses." ... id="iv.iv.ii">`. The
sentence runs lines 26944-26947: "Or else when he incites a man to desire the holy office of the
clergy under the pretext of edifying many people, and the love of spiritual gain, by which to draw
us away from the humility and strictness of our life." "He" refers to "the devil," named at line
26921 several sentences earlier in the same passage.

Normalization: line breaks joined with single spaces. No word added, dropped, substituted, or
reordered.
