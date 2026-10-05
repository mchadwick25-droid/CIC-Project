---
id: hal.quote.they-have-left-untold-the-name
world_id: hieronymian-ascetic-literary
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F6-E
- F6-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Innocent's own letter in the standard English of the NPNF Jerome volume, read directly at the letter cited. It reaches us inside Jerome's correspondence; the report it answers - Paula's and Eustochium's own account of the attack - is lost, and survives only as this reply.
sources:
- source_id: hal.source.attack-letters-416
  locus: >-
    Letter CXXXVII, Innocent of Rome to John of Jerusalem, a.d. 417 (npnf206_jerome-principal-works.xml, file lines 28468-28474)
  license: public-domain
text: >-
  The holy virgins Eustochium and Paula have deplored to me the ravages, murders, fires and outrages of all kinds, which they say that the devil has perpetrated in the district belonging to their church; for with wonderful clemency and generosity they have left untold the name and motive of his human agent.
modern_rendering: >-
  The holy virgins Eustochium and Paula have told me about the ravages. They speak of
  murders, fires, and outrages of every kind, which they say the devil did in their
  church's district. Yet with remarkable clemency and generosity, they have left untold
  the name and motive of his human agent.
speaker_or_author: Innocent of Rome, Letter to John of Jerusalem (Jerome, Ep. CXXXVII)
license: verbatim
modern_lens_note: >-
  This world's only violent deaths are in that sentence, and almost everything about them is missing. The killers were other Christians. The dead are not named. The man behind it is not named either - not because the record failed, but because the two women who reported it CHOSE not to name him, and a pope wrote down that they had chosen. Their own letter is lost; this survives because it was filed with Jerome's correspondence. So the martyr question does not land here: nobody in this world died at the hands of a hostile empire, and the deaths it did suffer arrive as one clause in someone else's rebuke to a third party.
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks whether anyone here was martyred, or died for the faith"
  - "participant asks about violence suffered by this community"
  - "participant asks how reliable this world's account of its own worst events is"
  - "participant asks whether they were ever attacked, and who intervened"
  - "participant asks what happened to the women of the household in a raid"
relations:
- type: associated-with
  target: hal.limit.martyrdom
- type: associated-with
  target: hal.limit.f5-women-own-words
use_note:
  means: "Innocent's letter to John of Jerusalem records that Eustochium and the younger Paula reported murders and fires but chose not to name the man behind them."
  not_for:
    - "a claim that anyone in this world was martyred by a hostile state; the violence came from fellow Christians"
    - "a claim identifying the attackers or naming the dead"
    - "the women's own account; their letter is lost"
    - "a claim that this Paula is the elder Paula, who died in 404"
  years: {from: 416, to: 417}
  status: reviewed
---
Verified verbatim against the vendored npnf206 (Ep. 137, div
v.CXXXVII); 'Paula' here is the younger Paula, Eustochium's niece, per the
volume's own note. This is the trace of the women's lost letter: the
fullest surviving account of the 416 attack is a pope's summary of the
report they wrote, and his praise records their restraint. Serves F6-P as
well as F6-E, and grounds hal.limit.f5-women-own-words's sharpest fact.

Opened for F6-E, which the rewritten classifier moved out of LIMIT-ONLY: hal.limit.martyrdom
is the cell's only serving record and cites Ep. 137 specifically, so the limit can be voiced by the
passage it points at.

The limit's hardest sentence - 'even their names were not kept' - had nothing standing behind it. This
is the sentence it was describing.
