---
id: alexlex034
world_id: alexandria-catechetical
record_type: term
schema_version: 1
jobs:
- 1
- 2
- 4
- 6
register: emic
review_state: draft
cache_stability: static
term: Household / Oikos
aliases:
- oikos
- household church
- the Christian home
- domestic formation
- household formation
quick_meaning: For us the household is not the private nuclear family — the oikos is the extended social
  and economic unit (householder, spouse, children, enslaved and freed persons, dependent relatives) that
  was the primary formation environment for most of the community, the space in which formation reached
  those who could not enter the catechetical school, and the daily setting in which our convictions were
  either practiced or exposed as merely nominal.
world_meaning: 'For most of us, the catechetical school is not where formation mainly happens. For most,
  the assembled Eucharist is one day in seven and the bishop''s Festal Letters are seasonal. The place
  where most formation occurs, for most believers, most of the time, is the household — the oikos, the
  extended social and economic unit that is daily life.


  The oikos has to be understood plainly, because the word will be misread at once. It is not the nuclear
  family of two parents and their children in a private home. It is the extended household: the householder,
  the spouse, the children, the enslaved persons, the freedpersons, the dependent relatives, the employees,
  sometimes lodgers. A substantial household might hold fifteen to forty people; a modest artisan''s household
  is smaller but still spans several social positions. The householder and the enslaved person who serves
  at the table share one oikos. The freeborn daughter and the household freedwoman share one domestic
  space. The Christian oikos is socially mixed in a way the modern private family is not.


  That mixture is where our convictions are tested. We claim the soul is being genuinely reoriented toward
  God, and that this reordering changes what a person wants, how they love, what they do. Nowhere is that
  claim tested more sharply than in the daily relations of a household. A householder who treats the enslaved
  person with contempt has not absorbed what we say about the soul and its capacity for God, whatever
  they profess. A household where prayer is kept, where Scripture is heard in whatever form its members
  can reach it, where children are formed in the faith''s basic commitments, and where the relationships
  across social positions are being reshaped by the transformation we pursue — that household is a genuine
  formation environment, and it forms everyone in it at whatever depth each has reached.


  The household is often where a catechumen is first formed. Many come to the school after years of household
  formation — already shaped by household prayer, by hearing Scripture read, by the example of members
  further along. For many, household formation is all the formation there will be: they will not enter
  the school, they will share in the Eucharistic assembly, and they will live out their formation chiefly
  in the household''s daily rhythm. Entry into the community''s life often comes as a household — the
  householder baptized "with the whole household," the oikos received together.


  We can say with confidence *that* the household was the primary formation ground for those least visible
  in what survives — enslaved persons, whose formation happened where they lived rather than in a school
  their position barred them from; women, some of whom engaged the formal structures but most of whom
  were formed in the domestic space; children, for whom the household was the first formation environment
  of all; rural believers, reached through household networks more than through the school. What we cannot
  do is narrate the inside of that formation for them. The record we have of household Christian life
  comes overwhelmingly from the educated householder — the one who wrote the letters and the instructions
  on managing a house. What formation felt like from the subordinate positions of the oikos is largely
  beyond our recovery, and we do not fill that silence with invention.'
distortion_risk: '**World Hearing:**

  The oikos is not a private space. It is a social and economic unit spanning multiple social positions,
  embedded in the community''s wider networks, and one of the main places the ecology reaches those who
  cannot enter its formal structures. It is not where believers retreated to practice a private faith
  apart from the community; it is where most of the community''s formation life actually happened, because
  most of life happened there — the daily prayer, the Scripture heard, the household relationships lived
  under real moral demand, the forming of children, the witness of members at different stages to one
  another.'
retrieval:
  tier: 1
  retrieve_when:
  - participant uses "household" or "oikos" in a formational sense
  - participant asks where formation happens for ordinary believers, or about family life and Christian
    formation
  - participant asks where women's, enslaved persons', or rural believers' formation occurred
  - participant asks how the formation ecology reached those who could not access the catechetical school,
    or about the relation between formal formation structures and everyday life.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking about the catechetical school as a formal structure (retrieve Catechesis)
  - condition_type: sense-disambiguation
    text: about household churches as an early-Christian phenomenon beyond this world's horizon
  - condition_type: sense-disambiguation
    text: or about marriage as a theological category rather than the household as a formation environment.
  force_llm_vote: false
sources:
- source_id: srcALX001
  author_gravity_note: Clement of Alexandria, *Paedagogus* II–III — the fullest surviving instruction
    on household life (eating, drinking, entertainment, possessions, relationships within the household);
    the ecology addressing the householder about how transformation operates in daily domestic life.
- source_id: srcALX002
  author_gravity_note: Origen, *Commentary on Romans* and correspondence — references to household Christian
    life and the formation of those at various positions within the oikos. Acts 16:15, 31–34; 18:8 — household
    baptism accounts, the oikos as the unit of formation entry. 1 Corinthians 1:11, 16:19; Colossians
    3:18–4:1 — the household as the social unit within which the ecology's moral claims are applied.
- source_id: srcALX009
  author_gravity_note: 'Eusebius, *Church History* V–VI — references to prominent Alexandrian Christian
    households.


    Note: that the oikos was the extended social and economic unit (not a nuclear family) is Widely Accepted
    as historical fact, and household baptism as the entry mode for non-literate and dependent members
    is Widely Accepted; that the ecology explicitly addressed household life (Clement''s *Paedagogus*)
    is Widely Accepted. That the household was the primary formation environment for the community''s
    majority, and specifically for enslaved persons, women, and rural believers, is the structural claim
    and is held at Dominant Modern Reconstruction. The *interior* formation experience of the subordinate
    members of the household is Inferential/Thin — the surviving evidence is the educated householder''s,
    and per the stratum-bias constraint (OG-4) this chunk gives what the world attests without narrating
    the non-literate majority''s interior. Eusebius carries HIGH Author-Gravity risk for his selective
    institutional and biographical perspective.'
modern_hearing: '**Modern Hearing:**

  "Household" most naturally evokes the nuclear family — parents and children in their own private home,
  a sphere set apart from the community''s institutions. On this hearing the household is the private
  domestic space, and household formation is individual devotion, family values, children''s religious
  education at home. This is not wrong about *that* the household forms; it misses the scale, the social
  complexity, and the community-formation weight of what the oikos was.'
period_sense: The oikos - not the private nuclear family but the extended social and economic unit (householder,
  spouse, children, enslaved and freed persons, dependents) that is the primary formation environment
  for the community's majority (chunk Quick/World Meaning and EF).
prior_sense: Ordinary Greek oikos, the extended household unit - the chunk's own definition carries the
  social-historical sense directly.
modern_sense: The nuclear family in its own private home, a sphere set apart from economy and public life
  (chunk Modern Hearing).
conceptual_distance_note: 'The modern household is private and small; the oikos is a social and economic
  unit spanning multiple positions, embedded in the community - and it is where most formation happened
  for most believers (chunk World Hearing/WM). Sharp scale-and-privacy gap: high grounding criterion by
  rule.'
semantic_domain: community-formation
grounding_criterion: high
voice_surface: For most of us, the catechetical school is not where formation mainly happens. The place
  where most formation occurs, for most believers, most of the time, is the household.
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  verification_date: '2026-07-27'
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
field_relations:
- type: presupposes
  target_id: alexlex043
  note: 'The household is the majority''s formation space within the called-out community (chunk EF).
    Chunk Ecological Function (verbatim, absorbed per FLAG-002): The household is the primary formation
    environment for the community''s majority — the space in which the ecology reaches those the formal
    channels cannot. It anchors formation''s reach beyond formal structures (the school reaches the literate,
    the Eucharist reaches the baptized weekly, the household reaches everyone continuously in daily life);
    the ecology''s whole-community claim (that it forms the whole community and not only its educated
    members rests substantially on the household as a real formation environment); and the stratum populations''
    primary access point (for enslaved persons, women, and rural believers, the household is where formation
    chiefly occurred). School, martyrdom, and household together make the ecology''s claim to whole-community
    reach — intellectual depth, acute faithful response, and daily formation environment respectively.'
- type: associated-with
  target_id: alexlex033
  note: 'CO-P2-13 (Mark, 2026-07-28): the chunks'' own mutual Related-Terms cross-reference, typed as
    symmetric association - no hierarchy claimed (both sides'' Reciprocity Notes, verbatim in the record
    bodies, attest the pair).'
- type: associated-with
  target_id: alexlex003
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex007
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex010
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex026
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
---
Migrated at the S6.2 S2.2-equivalent (2026-07-27) from `data/alexandria_world/lexicon_chunks/alexlex034_household.md` (mechanical split; mapping in `wrs/migrate/s62_alx_chunk_split.py`). Related-Terms and new-authoring fields arrive at the S2.3-equivalent.

[Related-Terms Reciprocity Note — parked at the S2.2-equivalent; absorbed into field_relations notes at the S2.3-equivalent] Cross-referenced with Soul/Psyche, Catechesis, Eucharist, Martyrdom/Witness, Participation. **Mutual** (each lists this term back): Martyrdom/Witness. **One-directional** (this term lists them; they do not list it back yet — deployment-layer reciprocity-completion items, per Doc_06 §4 flag-don't-hide): Soul/Psyche, Catechesis, Eucharist, Participation. **Not yet built as chunks** (Tier-2 / governed-CT entries): none.

CO-P2-13 (2026-07-28): the Reciprocity Note's mutual cross-references now carry typed associated-with edges; see wrs/migrate/s62_alx_s29_co13.py.

CO-P2-14 (2026-07-28): the Reciprocity Note's one-directional completion items completed as associated-with pairs; see wrs/migrate/s62_alx_s29_co14.py.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 3 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
