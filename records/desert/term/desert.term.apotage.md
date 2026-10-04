---
id: desert.term.apotage
world_id: desert-monasticism
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells: [F4-I, F5-T]
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
- source_id: desert.source.athanasius-vita-antonii
  locus: "SS2-3 (Antony gives his inherited land to the villagers, sells the movable rest and gives the proceeds to the poor, then - hearing 'be not anxious for the morrow' - gives away even the small reserve he had kept for his sister and places her in the care of known virgins)"
  license: public-domain
- source_id: desert.source.pachomian-corpus
  locus: "the Rule's property renunciation as entry condition, via the Latin Rule tradition (Jerome's Latin, itself two stages removed from the Coptic through a Greek intermediary, reaching this build only through consult-only modern scholarship) - not carried by the vendored one-remove witnesses (Palladius ch. XXXII, Sozomen III.14), which report the community's tablet-rule and three-year probation but not this specific condition"
- source_id: desert.source.rousseau-pachomius
  locus: "the named modern authority for Rule-content claims resting on consult-only scholarship, per this world's standing rule"
retrieval:
  tier: 2
  retrieve_when:
  - how a person actually joined this life
  - questions about money, property, and giving things up
relations:
- type: associated-with
  target: desert.term.anachoresis
- type: associated-with
  target: desert.term.koinonia
- type: associated-with
  target: desert.quote.three-years-a-servant
plain_meaning: "Renunciation: you give up property, family claims, and standing to enter this life."
world_word: apotage
false_friend:
- a one-time vow after which normal attachments quietly resume
senses:
  informational: "The entry act: giving up property, family ties, and worldly standing at the threshold of ascetic life. The Pachomian communities made it a formal condition of membership; the solitary and semi-solitary strands practiced it as an assumed threshold without comparable paperwork."
  evidential: "Antony's own story opens with it - the Life records him giving away his inherited land, selling what could be moved and giving the money to the poor. He first kept back a small reserve for his sister's sake; hearing the Gospel read again, he gave that away too and placed her with virgins who would care for her. Renunciation, on the Life's own telling, was not one gesture but a resolve that kept finding more to give up. For the Pachomian rule-form, this specific condition rests on modern scholarship on the Latin Rule tradition - itself two stages removed from the Coptic, through a Greek intermediary before Jerome's Latin - not on Palladius's or Sozomen's own reports, which give the community's tablet-rule and its three-year probation but not this condition by name."
  personal: "Renunciation was not a transaction completed at the door. It was re-enacted daily - in labor, in obedience, in owning nothing worth defending - so that a person's grip on things loosened for good, not for a season."
  translational: "Closer to a divestment that keeps costing than to a pledge or a resolution. The modern picture of a single dramatic gesture misses that the tradition treated the ongoing practice, not the moment, as the real renunciation."
quick_meaning: "Giving up property and standing to enter this life - and keeping it given up."
distortion_risk: medium
use_note:
  means: "Apotage meant giving up property, family claims, and standing at the threshold of ascetic life, and the tradition counted the ongoing practice as the real renunciation."
  not_for:
    - "Hearing it as a one-time vow after which ordinary attachments resume"
    - "Presenting the formal Pachomian entry condition as the form it took among solitary monks"
  years: {from: 270, to: 430}
  status: provisional
---
Re-derived from Doc_06 SS1.2 (Tier 1 there on the central-conceptual-
clusters criterion, not a gravity anchor - Doc_06's Tier-composition
note; retrieval tier 2 here reflects supporting rather than core
retrieval weight, recorded as a deliberate divergence from the old
lexicon tier). Strand-B codification vs A/C assumed-threshold contrast
carried.

The evidential sense gives the fuller sequence from Vita SS2-3
(verified against npnf204 lines 31248-31267): the land was given to
the villagers, not sold - only the movable goods were sold, with the
proceeds given to the poor - and Antony's reserve kept back for his
sister was itself given away on hearing "be not anxious for the
morrow," with no time interval stated between the two moments (the
Life's own text says only "again"). The fuller sequence is better
evidence for this record's own thesis: renunciation re-enacted, not
completed at the door.

The property-renunciation-as-entry-condition claim is carried by the
Latin Rule tradition (per desert.source.pachomian-corpus's own standing
rule that a Rule-content claim must name its actual channel), not by
Palladius ch. XXXII or Sozomen III.14, which give the Tabennesiot
angel-tablet rule and a three-year probation but not this condition.
desert.source.rousseau-pachomius is registered as the named modern
authority for that claim. The Rule's own transmission chain is Coptic
to Greek to Jerome's Latin - two stages, not three - so "two stages
removed from the Coptic" attaches to Jerome's Latin translation itself,
with the further stage of modern scholarly rendering carried in the
locus rather than the evidential sense.
