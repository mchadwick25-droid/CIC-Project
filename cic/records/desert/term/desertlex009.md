---
id: desertlex009
world_id: desert-monasticism
record_type: term
schema_version: 1
jobs:
- 1
- 2
- 4
- 5
- 6
- 7
register: emic
review_state: draft
cache_stability: static
term: Koinōnia (Communal Rule)
aliases:
- koinonia
- communal rule
quick_meaning: The founder Pachomius's own name for his federated network of monasteries under a single
  Rule and spiritual authority.
plain_explanation: 'Koinonia was Pachomius''s own name for his network of houses. One written Rule and
  one authority governed them all. Property was shared. Offices like housemaster and steward ordered daily
  life. By his death there were nine men''s houses and two for women. This pattern belonged to his branch
  alone; hermits and cell-dwellers had nothing like it. Today it can look like the elder''s way, just
  written down. Those inside knew it as a different kind of authority: a way to form many people at once,
  not one.'
world_meaning: 'A New Testament term for fellowship, adopted as a technical proper name for a specific
  institutional innovation: multiple houses under common property, formal offices (housemaster, steward),
  and a written Rule. Plural-voices flag: this is the clearest strand-bound term in this world''s whole
  vocabulary — this world''s more solitary and semi-communal ascetics have no equivalent institutional
  referent.'
distortion_risk: 'World Hearing — a genuine institutional innovation solving a specific problem: how total
  ascetic formation scales beyond one extraordinary individual''s own solitary path. Experienced by participants
  as a different kind of authority than the elder-model, not a formalized version of the same thing.'
retrieval:
  tier: 1
  retrieve_when:
  - participant asks about communal/rule-based monastic life specifically
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: this world's more solitary ascetics are the topic — koinōnia does not apply to them
  force_llm_vote: false
sources:
- source_id: srcDES002
  author_gravity_note: Pachomian corpus — the Rules (surviving complete only in Jerome's Latin translation,
    404 CE, made from a Greek intermediary itself translated from Coptic, with partial Coptic originals
    also extant) and the *Lives of Pachomius* (multiple, only partially overlapping Sahidic, Bohairic,
    and Greek recensions) — Widely Accepted as to the corpus's existence, general content, and Pachomian
    origin; Contested as to specific incident-level historical reliability and version-priority. The relative
    priority and historical reliability of the different *Life* versions for specific incident-level detail
    remains a genuinely live scholarly question; this entry does not adjudicate that debate and draws
    on the corpus only for claims consistent across versions.
modern_hearing: Modern Hearing — generically monastic in an undifferentiated, timeless sense.
period_sense: Pachomius's own proper name for his federated network of monasteries under one written Rule
  and spiritual authority — common property, formal offices (housemaster, steward), nine men's and two
  women's houses by his death. Strand B's institution specifically, with no Strand A/C equivalent — the
  clearest strand-bound term in the lexicon (Doc_06 §1.9).
prior_sense: The New Testament term for fellowship, adopted as a technical proper name (Doc_06 §1.9, verbatim
  clause) — the one entry whose prior sense the build's own documents state directly.
modern_sense: Heard today as generically monastic — 'communal rule' in an undifferentiated, timeless sense
  (Doc_06 §1.9 Modern Hearing).
conceptual_distance_note: 'Real gap: participants experienced the koinōnia as a different KIND of authority
  than the elder-model — an institutional innovation solving how total formation scales beyond one extraordinary
  solitary — not a formalized version of the same thing (Doc_06 §1.9 World Hearing). Plural-voices hazard:
  strand-bound, must not be voiced as the whole world''s pattern.'
semantic_domain: communal-institution
voice_surface: Among the brothers of the koinōnia — and I speak of them as neighbors, not as my own strand
  — the Rule holds what, among us, an elder's word holds. Ask which house a man belongs to before you
  ask who commands him.
grounding_criterion: high
eviction_priority: 2
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  verification_date: '2026-07-26'
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
field_relations:
- type: presupposes
  target_id: desertlex002
  note: 'Membership presupposes codified renunciation — the Rule specifies surrender of personal property
    as a condition (Doc_06 §§1.2, 1.9); organizes Strand B''s entire social structure (Ecological Function,
    absorbed per FLAG-002). Chunk Ecological Function (verbatim, absorbed per FLAG-002): Organizes the
    communal-rule strand''s entire social structure; stands in documented, named tension against the elder-model''s
    person-based authority — a genuine, unresolved difference in what "legitimate authority" means, not
    a stylistic variation.'
- type: tension-with
  target_id: desertlex006
  note: Stands in documented, named tension against person-based elder authority — an unresolved difference
    in what legitimate authority means, not a stylistic variation (Doc_06 §1.9 Ecological Function, absorbed
    per FLAG-002; symmetric edge).
chunk_slug: koinonia
---
S2.2 mechanical split + S2.3 new authoring (2026-07-26). Sense fields condensed from and cited to Doc_06; prior senses not developed in the build's documents are marked UNVERIFIED in-line. EF parking (FLAG-002) restructured into typed field_relations; Related-Terms entries with no Desert chunk (Xeniteia, Kellion, Apatheia, Theōria, Nēpsis, Penthos, Synaxis, Antirrhēsis) are S2.9 Change-Order material, not records invented here.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 1 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
