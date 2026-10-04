---
id: syr.term.qyama
world_id: syriac-edessa-nisibis
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-I
- F3-I
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
- source_id: syr.source.aphrahat-select-demonstrations
  locus: VI (Of Monks - the covenant teaching; the direct contemporary source)
  license: public-domain
- source_id: syr.source.harvey-voiced-silence
  locus: the daughters-of-the-covenant findings
  license: in-copyright-consultation
- source_id: syr.source.griffith-qyama-studies
  locus: the qyama-specific studies
  license: in-copyright-consultation
- source_id: syr.source.malki-qyama
  locus: whole article (used with the pre-/post-410 stratification caution)
  license: in-copyright-consultation
retrieval:
  tier: 1
  retrieve_when:
  - participant asks about celibacy, asceticism, or vowed life in this world
  - participant asks how this world's ascetics differ from desert monks
  - participant uses 'monk', 'nun', or 'monastery' in a way that imports desert assumptions
  - Aphrahat's Demonstration 6 or authority-alongside-office questions come up
claim_guards:
- participant asks specifically whether Ephrem personally led the women's choirs - that claim is later
  hagiography and this record must not be used to confirm it
relations:
- type: associated-with
  target: syr.gravity.covenant-life
- type: associated-with
  target: syr.term.ihidaya
- type: associated-with
  target: syr.term.tahwyata
- type: associated-with
  target: syr.contested.qyama-structure
plain_meaning: 'The covenant: our own vowed order. Its members - the sons and daughters of the
  covenant - promised a celibate life for good. But they did not leave for the desert. They stayed in
  town, among their own kin, and served the congregation: the fast, the watch, the vigil, the singing.'
world_word: qyama (bnay qyama / bnat qyama)
false_friend:
- monk or nun (desert withdrawal, cloister, formal rule)
- covenant (a legal contract between parties)
senses:
  informational: A lifelong vowed order of celibate men and women (bnay/bnat qyama, sons and daughters
    of the covenant) living inside the ordinary congregation and serving it - this world's native asceticism,
    older than and different from desert monasticism.
  evidential: Aphrahat's Demonstration 6 (337 CE) is the earliest firmly dated source and addresses the
    order as already established; Ephrem's hymns attest the daughters of the covenant as the choirs that
    performed them. The order's formal internal structure (rule, enclosure, hierarchy) is thinly and contestedly
    documented - existence and character are solid, structural detail is not.
  personal: 'For someone who feels a calling but not a withdrawal: this world''s committed life was lived
    in the middle of town, among family and neighbors - refusal within the world, not flight from it.'
  translational: '''Were they monks and nuns?'' - no monastery, no desert, no later rule: a vow taken
    for life, lived at home, in the congregation''s daily service.'
quick_meaning: 'The covenant: our vowed order of celibate men and women. They stayed in town
  and served the congregation, rather than leave for the desert.'
distortion_risk: high
use_note:
  means: "The qyama, or covenant, was a lifelong order of celibate men and women who stayed in town and served the congregation; its existence is solid but its formal structure is thinly documented."
  not_for:
    - "a claim that the covenanters were monks or nuns under a rule or in a cloister"
    - "a claim that Ephrem personally led the women's choirs"
    - "a claim that the order had a settled rule, enclosure or hierarchy in this window"
  years: {from: 337, to: 410}
  status: provisional
---
A Tier 1, CT-tagged entry, grounding the C2 Primary gravity. The CT
contest (historical scope: internal structure thin/contested) is
carried in the evidential sense and in syr.contested.qyama-structure.
The Ephrem-choir-leadership claim is excluded from the evidentiary
basis (later hagiography, outside the window), enforced here by the
do_not_retrieve_when rule. What IS in-window: that choirs of the bnat
qyama performed the madrashe.
