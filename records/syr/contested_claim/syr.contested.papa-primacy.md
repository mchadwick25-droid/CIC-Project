---
id: syr.contested.papa-primacy
world_id: syriac-edessa-nisibis
record_type: contested_claim
schema_version: 2
status: ready
register: etic
canon_cells:
- F3-I
confidence:
  citation_specificity: C
  verification_state: named-not-rechecked
  evidentiary_weight: contested
  formation_confidence: Contested
  divergence_note: null
sources:
- source_id: syr.source.gedsh
  locus: s.v. Papa bar Aggai
  license: in-copyright-consultation
- source_id: syr.source.bar-hebraeus-chronicon-ecclesiasticum
  locus: "entries 10-11 (Papa bar Aggai, Simeon bar Sabbae), file lines 1670-2189 - the primary
    chronicle text itself, standing alongside GEDSH's secondary consultation"
  license: public-domain
relations:
- type: associated-with
  target: syr.figure.papa-bar-aggai
- type: associated-with
  target: syr.gravity.authority-ambiguity
claim: By the early fourth century Persia had its own settled, parallel episcopal hierarchy under Papa
  bar Aggai of Seleucia-Ctesiphon.
held_against:
- Papa's claim to primacy over other Persian bishops was fiercely contested in his own lifetime - by Miles
  of Susa and Aqib-Alaha of Karka d'Baith Slok, at a synod c. 315
- the succession narratives are chronicle-derived and hagiographically inflected (Chronicle of Seert,
  Bar Hebraeus tradition), not contemporary attestation; the earliest vector for the 'Catholicos' claim,
  the Acts of Mari, is dated sixth to eighth century
- the title 'Catholicos' is anachronistic before the fifth century
- the succession's own anchor date (Simeon bar Sabbae's martyrdom, 341) is actively disputed (c. 344 argued),
  shifting every chained date
concedes: 'A genuinely multi-see Persian episcopal structure existed - bishops, plural, real enough to
  fight over precedence - but its continuity was fragile (a twenty-year primatial vacancy under persecution)
  and its early shape is knowable only through later tradition. Neither ''settled parallel hierarchy''
  nor ''no real structure'' survives scrutiny; the honest position is the third picture: real, contested,
  and disrupted.'
divergence_partners: []
use_note:
  means: "The claim that Papa bar Aggai headed a settled parallel Persian hierarchy by the early fourth century is contested: his primacy was disputed and the structure fragile."
  not_for:
    - "a claim that Papa was an undisputed Catholicos"
    - "a claim that no real Persian episcopal structure existed"
    - "a claim that the Simeon bar Sabbae anchor date of 341 is secure"
  years: {from: 315, to: 344}
  status: reviewed
---
Grounds the F3-I answer's honesty and the tensional gravity's
Persian-side pole, with both caveats carried: the Simeon bar Sabbae
redating dispute, and the anachronism of the title "Catholicos" before
the fifth century.

This claim's `held_against` line - "the succession narratives are
chronicle-derived... (Chronicle of Seert, Bar Hebraeus tradition), not
contemporary attestation" - cites that tradition's own primary text
directly (syr.source.bar-hebraeus-chronicon-ecclesiasticum), alongside
Doc_02 SS11's secondary (Fiey-mediated) account and GEDSH's
in-copyright encyclopedia entry. This does not touch the claim's own
substance or resolve the Simeon bar Sabbae redating dispute, which the
chronicle cannot itself adjudicate. See
syr.source.bar-hebraeus-chronicon-ecclesiasticum's own trailing note
for exactly what was and was not verified.

The chronicle itself, not only the modern secondary literature,
corroborates this claim's `held_against` line "Papa's claim to
primacy... was fiercely contested in his own lifetime": entry 11
states of Simeon bar Sabbae "Ferunt hunc Simeonem, Papa adhuc vivente,
ab episcopis qui ab isto recesserant ordinatum fuisse" ("They say this
Simeon, while Papa was still alive, was ordained by bishops who had
withdrawn from him") - file line 2062, Latin, per
syr.source.bar-hebraeus-chronicon-ecclesiasticum. A rival ordination
proceeding against a sitting primate, while he still lived, is direct
primary-text evidence of contest in Papa's own lifetime, independent of
the Miles-of-Susa/Aqib-Alaha synod tradition already cited. It does not
itself date the episode or resolve the Simeon bar Sabbae redating
dispute.
