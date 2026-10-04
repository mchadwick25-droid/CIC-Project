---
id: cappadocian.story.basil-death-funeral
world_id: cappadocian-trinitarian
record_type: story
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: "Widely Accepted that Basil died and was given a major public funeral; Contested and unsettled even among this world's own governing documents exactly when - see this record's own body note for the Doc_09/Doc_02 discrepancy this record does not silently resolve. Encomium-flagged: the claim of a city-wide, cross-religious mourning crowd is Gregory of Nazianzus's own, in a funeral oration built to argue for his friend's largest possible stature, and is not independently corroborated by any other witness."
sources:
- source_id: cappadocian.source.gregory-nazianzus-oration-43-funeral-encomium-basil
  locus: "the death and the crowd at the bier"
- source_id: cappadocian.source.maraval-pouchet-basil-death-redating
  locus: "the modern redating argument for 377"
- source_id: cappadocian.source.gregory-nyssa-general-dogmatic-ascetic-corpus
  locus: "Gregory of Nyssa's own memorial preaching, at work level"
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how Basil died, or what happened at his funeral"
  - "participant asks whether this world's leaders were respected beyond their own community"
relations:
- type: associated-with
  target: cappadocian.figure.basil
- type: associated-with
  target: cappadocian.figure.gregory-of-nazianzus
- type: associated-with
  target: cappadocian.gravity.martyrs-land
- type: illustrates
  target: cappadocian.gravity.bishop-patron
narrative_tier: 1
narrative_tier_justification: "Tier 1: Basil's death itself, and the fact of a major public funeral, are Documented historical events. The exact date is genuinely Contested. The scene-level claim of a universal, cross-religious mourning crowd is the encomiast's own, flagged as such rather than treated as an independent census of who actually grieved."
tellable_as: "Basil dies, and the friend who eulogizes him claims the whole city grieved - Christian, Jewish, and pagan alike."
text: >-
  Basil died bishop of Caesarea. Different reckonings of our own
  record place his death in either January 379 or September 378; the
  modern redating literature argues instead for 377, a full year or more
  earlier than either traditional date, since much of Basil's own
  chronology is computed backward from the year he died. Gregory of
  Nazianzus's funeral oration for him describes a crush of mourners at the
  bier so great that people were injured in the press, and claims the
  mourning reached beyond the Christian community itself - that Jews and
  pagans grieved alongside the church, each in their own fashion, moved by
  what the man had been to the city. That claim of near-universal mourning
  belongs to Gregory, the encomiast, making the largest possible case for
  his friend's public significance; no other witness independently
  confirms it. Gregory of Nyssa, Basil's own brother, also preached in his
  memory, continuing after his death the fight over the Spirit's divinity
  the two brothers had shared.
absent_detail: "No account of the funeral survives from outside Basil's own circle; the claim that Jews and pagans mourned specifically is Gregory's own, made in a funeral oration built to argue for his friend's largest possible significance, and is not independently corroborated."
modern_contrast: >-
  A modern reader might take a claim of city-wide, cross-religious mourning
  at face value, the way an obituary's stated attendance figures might be
  taken. This world's own record is a friend's eulogy with a case to make
  about his friend's stature - real grief, almost certainly, but a
  specific, checkable crowd count is not what a funeral oration is built to
  supply.
use_note:
  means: "Basil died as bishop of Caesarea on a date contested between 377 and 379, and only Gregory of Nazianzus claims that Jews and pagans mourned him."
  not_for:
    - "a settled death date for Basil"
    - "the cross-religious mourning as independently confirmed, when it is the encomiast's claim"
    - "a crowd count, which a funeral oration is not built to supply"
    - "Basil's life and work in full, which sits in cappadocian.figure.basil"
  years: {from: 377, to: 379}
  status: reviewed
---
Derived from Doc_09 entry #9 (Tier 1). FLAGGED, NOT SILENTLY RECONCILED:
Doc_09's own current text states this event as "Jan 379, or Sept 378...
date Contested — 378/379 redating carried" - but Doc_02 §1.1, in its own
already-revised and independently-reviewed form, explicitly corrects
Basil's death to 377 ("death redated to 377, not 378... the actual
redating literature (Maraval 1988; Pouchet 1992) argues for 377... not a
rounding error"), with a dedicated source record
(cappadocian.source.maraval-pouchet-basil-death-redating) built for
exactly this claim. Doc_09's own entry #9 never mentions 377 at all and
frames "378/379" as the redating itself, which inverts what Doc_02 says
the redating actually concluded. This record follows Doc_02's more
carefully sourced correction (naming 377 as the redating argument's own
conclusion) rather than silently adopting Doc_09's narrower "378/379"
framing, and names the discrepancy here explicitly per this step's own
instruction not to work around an inconsistency quietly. Reported in this
step's own final summary as well.

FEC / GRAVITY LINKAGE (parked for B-5; see cappadocian.story.famine-open-
barns's body note for the full statement of this project precedent):
illustrates Supporting Gravity 5 (the martyrs' land, Doc_04 §4) only by
contrast - Basil dies of natural causes, not martyrdom, and this world's
own memory of him is civic and doctrinal rather than a martyr-cult - and
is a documented instance of Supporting Gravity 7 (the bishop as public
patron, Doc_04 §4) at its closing.

CONVERTED AT B-5: real relations[] entries added above - associated-with
cappadocian.gravity.martyrs-land (the contrast link named above, carried
as associated-with rather than illustrated-by since it illustrates only
by contrast) and illustrates cappadocian.gravity.bishop-patron (the direct
instance named above), with reciprocal back-edges declared on both
gravity records.
