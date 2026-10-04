---
id: gallic.quote.aloof-from-assemblies-of-bishops
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
    Documented as spoken within Sulpitius's Dialogues (Book III), in the voice of the character
    recounting Martin's later life to the assembled company. The episode described - Martin's forced
    communion with the Ithacian party and his subsequent withdrawal from synods - is Widely Accepted;
    the wording is Documented to this Dialogues text.
sources:
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: "Dialogues III.13 (npnf211 div ii.iv.iii.xiii, file lines 5217-5219): the aftermath of Martin's coerced communion with the Ithacian bishops"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether Martin ever regretted a compromise, or how he responded to it"
  - "participant asks why this world's monks might distrust synods and assemblies of bishops"
  prefer_instead:
  - "participant asks for the Ithacian communion episode itself in detail - this record carries only its lasting effect on Martin's own practice"
text: >-
  He lived sixteen years after this, but never again did he attend a
  synod, and kept carefully aloof from all assemblies of bishops.
speaker_or_author: Sulpitius Severus, in the voice of Gallus (Dialogues III)
license: verbatim
modern_lens_note: >-
  This sentence follows directly on Martin's own confession - reported a few lines earlier in the same
  chapter - that he felt his healing power diminished after being pressured into communion with
  bishops he judged unworthy. The withdrawal from synods is presented as the lasting consequence: not
  a single act of protest but a permanent change in how Martin spent the rest of his life among
  bishops.
modern_rendering: >-
  He lived sixteen years after this. But he never again went to a synod,
  and he carefully kept away from every gathering of bishops.
relations:
- type: associated-with
  target: gallic.gravity.authority-ambivalence
use_note:
  means: "Gallus says in the Dialogues that Martin lived sixteen years after the coerced communion and never again attended a synod or assembly of bishops."
  not_for:
    - "the coerced communion and the angel's rebuke themselves, which sit in gallic.quote.gallus-on-the-forced-communion-and-the-angel"
    - "a claim that Martin rejected bishops or the episcopate as such"
    - "a date for the Treves affair computed from Gallus's sixteen years"
  years: {from: 404, to: 406}
  status: provisional
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"kept carefully aloof"` returns one hit, line 5218, inside `<div4 title="Chapter XIII." ...
id="ii.iv.iii.xiii">`. The sentence runs lines 5217-5219: "He lived sixteen years after this, but
never again did he attend a synod, and kept carefully aloof from all assemblies of bishops." This
chapter is part of a first-person speech within the Dialogues (opens mid-quotation at the chapter's
own start), recounting Martin's coerced communion with the Ithacian party and its aftermath; the
narrating voice is one of Sulpitius's interlocutors (Gallus), not Sulpitius speaking in his own
person as in the Vita.

Normalization: line breaks joined with single spaces. No word added, dropped, substituted, or
reordered.
