---
id: pahclex002
world_id: post-apostolic-house-church
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
term: presbyteros (πρεσβύτερος)
aliases:
- presbyter
- priest
quick_meaning: The *presbyteroi* are the elders who share the community's governance — in some households
  as a council that holds the full trust themselves, in others gathered around a bishop whose leadership
  they support but do not replace.
world_meaning: 'We call them presbyteroi, elders, and what they do among us depends on where we stand.
  In Rome, when the church there wrote to Corinth to settle a quarrel, they spoke of presbyters removed
  from their office — not of a bishop deposed. The whole weight of that letter''s correction fell on the
  wrongness of removing faithful presbyters, and nothing in it suggests a single presiding figure was
  missing. That was not many generations ago, and those of us who know that letter know a church governed
  by its presbyters together.


  In other places — in Antioch, in the cities of Asia Minor — the presbyters are gathered around a bishop,
  supporting his oversight rather than holding it in common. Ignatius speaks of the presbyterion, the
  council of elders, as something that should be tuned to the bishop the way strings are tuned to a harp.
  Even so, Polycarp — whom Ignatius addresses as bishop — calls himself in his own letter to the Philippians
  "one of the presbyters," as though the distinction is not yet one he claims for himself in writing.


  We hold both patterns in our correspondence without either side declaring the other wrong.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: This term works with episkopos to anchor the Authority Consolidation
  question (G01). Where episkopos carries the fuller Strand A/B institutional argument, presbyteros reveals
  the counterweight: the council model that existed before, alongside, and in some places instead of the
  single-bishop pattern.'
distortion_risk: 'In this world, presbyteros names those who carry the community''s governance — sometimes
  in a council that holds full authority, sometimes around a bishop who presides. The term''s meaning
  is still being shaped, not yet fixed.


  **Living Tradition Note:**

  This entry describes this world''s own formation ecology (c.70–200 CE). It makes no claim about how
  any present-day tradition currently defines or understands the office of presbyter or elder.


  **Confidence:**

  Contested. Whether Polycarp''s own self-designation as "one of the presbyters" reflects institutional
  humility within an already-secured monarchical system, or genuine evidence that the Strand A episkopos
  program had not yet been locally adopted even by the men Ignatius himself addressed as bishops, is not
  resolved by this world''s own evidence (see CT Contest Type below).'
retrieval:
  tier: 1
  retrieve_when:
  - participant asks about elders, presbyters, church leadership, the council of elders, or Polycarp's
    self-designation.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking about priestly ordination in a later sacramental sense with no connection
      to this period.
  force_llm_vote: false
sources:
- source_id: srcPAHCP02
  author_gravity_note: 1 Clement 44, 47, 54, 57 (Rome to Corinth — presbyteral governance).
- source_id: srcPAHCP05
  author_gravity_note: Hermas, Vision 2.4.3 (Rome, Strand B — "presbyters who preside over the Church,"
    reinforcing the plural-college reading).
- source_id: srcPAHCP04
  author_gravity_note: Polycarp, Letter to the Philippians 5–6 (self-designation as presbyter).
- source_id: srcPAHCP03
  author_gravity_note: 'Ignatius of Antioch, Letters to the Ephesians 4, Magnesians 2–7, Trallians 2–3
    (presbyterion around the bishop).


    Note: this entry does not repeat the Author-Gravity caution already disclosed under episkopos''s own
    Key Sources — Ignatius''s single-witness, under-guard circumstances for the Strand A monarchical claim
    apply equally here; see that entry for the fuller disclosure.'
modern_hearing: A modern reader hears "presbyter" or "elder" and may assume either a purely advisory role
  subordinate to a bishop, or a Protestant lay-elder model.
---
Migrated at the S6.2/PAHC S2.2-equivalent (2026-07-31) from `data/pahc_world/lexicon_chunks/pahclex002_presbyteros.md` (mechanical split; mapping in `wrs/migrate/s62_pahc_s22.py`; aliases parsed under the VG-1a semantics with the preflighted Rule-A drops at birth - the second world born matching the runtime key space AND the gate). Related-Terms and authored fields arrive at S2.3.

[CT Contest Type - parked at the S2.2-equivalent; home arrives with the contested_claim records (S2.6-equivalent) / S2.3 authoring] **Meaning** — whether Polycarp's self-designation as presbyter reflects institutional humility within an already-secured system or evidence the monarchical program had not yet been locally adopted.
