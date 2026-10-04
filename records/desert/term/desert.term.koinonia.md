---
id: desert.term.koinonia
world_id: desert-monasticism
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells: [F3-I]
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
- source_id: desert.source.pachomian-corpus
  locus: "the Rule and Lives (as reported; no vendored text)"
- source_id: desert.source.palladius-lausiac-history
  locus: "ch. XXXII (the Tabennesiot rule as Palladius reports it)"
  license: public-domain
- source_id: desert.source.sozomen-historia-ecclesiastica
  locus: "III.14 (the rule summary at one remove)"
  license: public-domain
- source_id: desert.source.rousseau-pachomius
  locus: "the named modern authority for Rule-content or Lives-incident claims resting on consult-only scholarship, per this world's standing rule (here, the federation's house count, a Lives-incident claim)"
retrieval:
  tier: 1
  retrieve_when:
  - questions about the organized communities, their rule, and their offices
  - how authority worked in the Pachomian houses
  prefer_instead:
  - questions about the solitary or semi-solitary life - this term is the Pachomian federation's own name for its own institution, not the whole world's
relations:
- type: associated-with
  target: desert.term.apotage
- type: associated-with
  target: desert.term.geron-abba-amma
- type: associated-with
  target: desert.gravity.koinonia
plain_meaning: "The Koinonia: Pachomius's own name for his linked houses. They lived under one written rule and one leader."
world_word: koinonia
false_friend:
- fellowship in the loose modern church sense
- any monastery whatever
senses:
  informational: "The New Testament word for fellowship, taken by Pachomius as the proper name of a real institution: a federation of houses under one written rule, common property, formal offices (housemaster, steward), and a single head. By his death in 346 it held nine men's houses and two women's houses. It names the Pachomian federation alone - the solitary and semi-solitary life has no equivalent institution or word for it."
  evidential: "The Rule survives complete only in Jerome's Latin translation; no English of it can be quoted here directly. What can be told directly are the reports of it - Palladius's and Sozomen's rule summaries, both wrapped in the angel-tablet legend - alongside modern scholarship on the Latin."
  personal: "Joining the Koinonia meant a different obedience than sitting at an elder's feet: obedience to an office, whoever held it, inside a common life with a fixed rhythm. Those who joined it felt a different kind of authority, not a formalized version of the same one."
  translational: "'Communal rule' undersells it: this was an institutional invention answering a real problem - how total formation could scale past one extraordinary hermit - and it sat in unresolved tension with the elder-model for this world's whole span."
quick_meaning: "Pachomius's linked houses: one written rule, one head."
distortion_risk: medium
use_note:
  means: "Koinonia was Pachomius's own name for his federation of linked houses under one written rule, common property, and a single head."
  not_for:
    - "Hearing it as loose Christian fellowship or any monastery whatever"
    - "Applying it to the solitary or semi-solitary life, which had no equivalent institution"
    - "Presenting Rule or Lives details as verified when they rest on consult-only scholarship"
  years: {from: 318, to: 346}
  status: provisional
---
Re-derived from Doc_06 SS1.9 (Tier 1 for Strand B specifically, per
Doc_03 SS1.19 and gravity 6; tags SC TC RT PV). The strand-bound
discipline lives in the do-not-retrieve fence. The authority contrast
with geron/abba/amma is gravity 10's territory; the relation carries it.

The evidential sense names its two channels (Palladius's and Sozomen's
rule summaries, and modern scholarship on the Latin) in plain in-world
evidence talk. desert.source.rousseau-pachomius is registered as the
named authority for the federation's house count (nine men's houses,
two women's) - federation history, not Rule content, which neither
Palladius XXXII nor Sozomen III.14 carries (both give population
figures, no house count) - matching that source's own coverage of
"Rule-content or Lives-incident claims." The informational sense and
do_not_retrieve fence name the Pachomian federation directly rather
than this build's own lettered taxonomy.
