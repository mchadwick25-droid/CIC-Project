---
id: gallic.quote.secular-ruler-judge-in-ecclesiastical-cause
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
    Documented as Sulpitius's own account (Sacred History II.50) of Martin's intervention with Maximus
    on behalf of the condemned Priscillianists. The wording is Sulpitius's report of Martin's argument
    in indirect discourse, not a direct quotation of Martin's own words - carried here as Sulpitius's
    own characterization of the position Martin took.
sources:
- source_id: gallic.source.sulpitius-sacred-history
  locus: "Sacred History II.50 (npnf211 div ii.vi.ii.l, file lines 11655-11660): Martin's intervention with Maximus over the condemned"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what Martin thought about secular rulers judging Church matters"
  - "participant asks why Martin opposed a state-run trial of the Priscillianists"
  prefer_instead:
  - "participant asks about the Priscillianist affair itself - that is another world's territory; this record carries only Martin's stated objection to the court's jurisdiction"
text: >-
  He maintained that it was quite sufficient punishment that, having
  been declared heretics by a sentence of the bishops, they should have
  been expelled from the churches; and that it was, besides, a foul and
  unheard-of indignity, that a secular ruler should be judge in an
  ecclesiastical cause.
speaker_or_author: Sulpitius Severus, narrating Martin's argument to Maximus
license: verbatim
modern_lens_note: >-
  Sulpitius reports this as Martin's own reasoning, in indirect speech, not as a direct quotation.
  The argument has two parts: the bishops' own sentence of expulsion was punishment enough, and a
  secular court trying an ecclesiastical case at all was itself the deeper wrong. Both halves matter -
  Martin is not defending the accused as innocent, only denying the emperor's court any standing to
  judge them.
modern_rendering: >-
  He held that it was punishment enough for them to be expelled from the
  churches, once the bishops had sentenced them as heretics. He
  held, too, that it was a foul indignity, never heard of before, for a
  secular ruler to judge a church case.
relations:
- type: associated-with
  target: gallic.gravity.authority-ambivalence
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"unheard-of indignity"` returns one hit, line 11659, inside `<div4 title="Chapter L." ...
id="ii.vi.ii.l">`. The sentence runs lines 11655-11660: "He maintained that it was quite sufficient
punishment that, having been declared heretics by a sentence of the bishops, they should have been
expelled from the churches; and that it was, besides, a foul and unheard-of indignity, that a
secular ruler should be judge in an ecclesiastical cause."

Normalization: line breaks joined with single spaces. No word added, dropped, substituted, or
reordered.
