---
id: alexlex043
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
term: Church / Ekklesia
aliases:
- ekklesia
- the assembly
- the congregation
- the Christian community
- the body of Christ
- the gathered community
quick_meaning: For us the church is not an institution with a membership roll — it is the formation community
  gathered around the Logos who gives himself to be shared, within which the soul is formed toward God
  through Scripture, sacramental participation, common life, and the authority of teacher and bishop;
  it is both the school's formation community and the whole community gathered in worship, held together
  in the genuine tension between the two.
world_meaning: 'Ekklesia means the called-out assembly — not a building, not an organization, not an institution
  with entry requirements. It is the assembly of those called out from one life into another, gathered
  around the Logos who called them and who is the center they are gathered around. Every time we gather
  — in the catechumens'' instruction, in the Eucharistic assembly, in the bishop''s governance of the
  whole community''s formation life — we are the ekklesia: the community that exists because the Logos
  addresses us and we answer.


  The church exists because formation cannot be private. The soul is not formed alone and then added to
  a community; it is formed *through* belonging to the community that catechizes, worships, prays, gathers
  around the Eucharist, and shows in its own common life what formation toward God looks like among actual
  people. The catechumen is formed by belonging to the community that catechizes. The school''s students
  are formed not by solitary study but through the teacher''s accompaniment in the company of other students
  and of the whole inheritance. The community is not where the already-formed assemble; it is the environment
  within which formation happens at all.


  The ekklesia holds within itself two genuinely different ways of being a formation community, and it
  does not resolve them. There is the school''s formation community — relatively small, literate, gathered
  around the teacher''s reading of Scripture at depth. And there is the whole community gathered in worship
  — including the non-literate majority, gathered around the bishop''s presidency at the Eucharist, reaching
  everyone baptized through sacramental participation. Both are the ekklesia. Neither is the full ekklesia
  without the other: the school without the gathered community is an intellectual enterprise cut off from
  the community''s full life, and the gathered community without the school lacks the interpretive depth
  the school carries. We live that tension as a standing feature of who we are, not as a problem awaiting
  solution.


  What gathers the ekklesia most fundamentally is the Eucharist. When the bishop presides at the table,
  he gathers the community around the Logos who gives himself to be shared, and in that gathering the
  ekklesia is most fully itself — the community of those participating together in the life of the one
  they are gathered around. We are the Eucharistic community before we are anything else; our structures,
  our governance, our catechetical work, our school all serve that gathering.


  And belonging to the church is not holding membership in an organization. It is being incorporated into
  the formation community — through baptism, through ongoing share in the community''s formation life,
  through accountability to the Rule of Faith the community carries. A baptized person who never shares
  in the community''s formation life belongs only nominally. A catechumen not yet baptized but genuinely
  sharing in the community''s formation — hearing Scripture, praying with us, being formed by the catechesis
  — is more fully within the church than the merely nominal member. Belonging is constituted by genuine
  participation, not by registration.'
distortion_risk: '**World Hearing:**

  The ekklesia is the assembly, not its location, and a formation community, not a voluntary association
  — constituted not by shared opinion or mutual membership but by genuine participation in the Logos''s
  life through the practices the community enacts together. It does not merely hold a correct concept
  of itself; it is actually gathered around the Logos who gives himself to be shared, actually being formed
  toward participation in divine life. It includes both the school''s literate community and the whole
  gathered community in one genuinely tensional reality, and belonging in it is genuine participation,
  not a name on a list.'
retrieval:
  tier: 1
  retrieve_when:
  - participant uses "church" in a theological or formational sense
  - participant asks what the church is and what it is for, or why formation cannot be private
  - participant asks about the relation between an individual's formation and the community
  - participant asks about the church as both school tradition and whole gathered community, what gathers
    it, or whether it is primarily an institution or something else.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking about a specific local congregation's practical life
  - condition_type: sense-disambiguation
    text: about church governance structures beyond this world's scope
  - condition_type: sense-disambiguation
    text: or primarily about the bishop's role (retrieve Bishop).
  force_llm_vote: false
sources:
- source_id: srcALX028
  author_gravity_note: Clement of Alexandria, *Stromateis* VII.5 and *Quis Dives Salvetur* — the community
    gathered around the Logos; the church as the formation community within which genuine knowledge and
    love develop.
- source_id: srcALX002
  author_gravity_note: Origen, *Against Celsus* III.29–30 and *Commentary on Matthew* — the church as
    the community of genuine formation rather than nominal membership; the tension between the school's
    community and the whole gathered community.
- source_id: srcALX003
  author_gravity_note: 'Athanasius, *Festal Letters* — the bishop governing the whole Egyptian church''s
    formation life through the annual calendar; the church as the whole community the bishop gathers.
    1 Corinthians 12:12–27 — the body of Christ as the ekklesia, the community constituted by participation
    in the one body. Matthew 16:18; 18:17 — the Logos constituting the ekklesia as his own gathered community.


    Note: that the ekklesia is a formation community rather than an institution or building, that the
    Eucharist is what most fundamentally constitutes it, that the Learning-Community tension is operative
    in its very structure, and that belonging is genuine participation rather than nominal membership,
    are all Widely Accepted (the participation-not-registration reading and the school-vs-gathered-community
    tension are Widely Accepted specifically for the school tradition''s self-understanding).'
modern_hearing: '**Modern Hearing:**

  "Church" most commonly means either a building or an institution — the place where Christians meet,
  or an organization with membership, governance, programs, and a budget, a voluntary association of like-minded
  people who share beliefs. Even the more sophisticated hearing — the church as the body of Christ, the
  people of God — can be held abstractly, as a fine theological concept laid over what is functionally
  still an institution.'
period_sense: Ekklesia, the called-out assembly - not a building or an institution with a membership roll
  but the formation community gathered around the Logos who gives himself to be shared; the environment
  within which the whole ecology operates (chunk Quick/World Meaning and EF).
prior_sense: 'The chunk''s own etymology: ekklesia, the called-out assembly - the ordinary Greek civic-assembly
  word received and re-centered on the one who calls.'
modern_sense: Either a building or an institution - the place where Christians meet, or an organization
  with membership (chunk Modern Hearing).
conceptual_distance_note: 'The modern church is a place or organization; the ekklesia is the assembly
  itself, constituted by its center, not its roll (chunk World Hearing). Sharp gap of referent: high grounding
  criterion by rule.'
semantic_domain: community-formation
grounding_criterion: high
voice_surface: Ekklesia means the called-out assembly - not a building, not an organization. The assembly
  of those called out from one life into another, gathered around the Logos who called them.
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  verification_date: '2026-07-27'
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
field_relations:
- type: presupposes
  target_id: alexlex026
  note: 'Gathered around the one who gives himself to be shared - the Eucharistic center constitutes the
    assembly (chunk QM/WM). Chunk Ecological Function (verbatim, absorbed per FLAG-002): The church is
    the formation community within which the whole ecology operates — the environment in which the soul''s
    formation toward God occurs and which the Primary gravities organize. It anchors formation''s communal
    necessity (the ecology is the community''s shared life, not a set of private practices reported back
    to the community); the Eucharist''s community-constituting function (the church is constituted by
    the recurring, enacted participation in the Logos''s self-giving — remove it and the church is a voluntary
    association); the ecclesial form of the Teacher–Bishop tension (both the school''s community and the
    whole gathered community are the ekklesia, and the tension between them is the church''s live structural
    reality); and the carrying of the Rule of Faith across generations (the church is the community that
    carries the Rule, and the Rule is what marks its continuity through time).'
- type: presupposed-by
  target_id: alexlex034
  note: The household is the majority's formation space within it (alexlex034 EF).
- type: associated-with
  target_id: alexlex030
  note: 'CO-P2-13 (Mark, 2026-07-28): the chunks'' own mutual Related-Terms cross-reference, typed as
    symmetric association - no hierarchy claimed (both sides'' Reciprocity Notes, verbatim in the record
    bodies, attest the pair).'
- type: associated-with
  target_id: alexlex007
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex025
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex029
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex031
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
---
Migrated at the S6.2 S2.2-equivalent (2026-07-27) from `data/alexandria_world/lexicon_chunks/alexlex043_church-ekklesia.md` (mechanical split; mapping in `wrs/migrate/s62_alx_chunk_split.py`). Related-Terms and new-authoring fields arrive at the S2.3-equivalent.

[Related-Terms Reciprocity Note — parked at the S2.2-equivalent; absorbed into field_relations notes at the S2.3-equivalent] Cross-referenced with Bishop/Episkopos, Eucharist, Baptism, Rule of Faith, Teacher/Didaskalos, Participation. **Mutual** (each lists this term back): Bishop/Episkopos. **One-directional** (this term lists them; they do not list it back yet — deployment-layer reciprocity-completion items, per Doc_06 §4 flag-don't-hide): Eucharist, Baptism, Rule of Faith, Teacher/Didaskalos, Participation. **Not yet built as chunks** (Tier-2 / governed-CT entries): none.

CO-P2-13 (2026-07-28): the Reciprocity Note's mutual cross-references now carry typed associated-with edges; see wrs/migrate/s62_alx_s29_co13.py.

CO-P2-14 (2026-07-28): the Reciprocity Note's one-directional completion items completed as associated-with pairs; see wrs/migrate/s62_alx_s29_co14.py.
