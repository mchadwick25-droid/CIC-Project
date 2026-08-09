---
id: syrstory004
world_id: syriac-edessa-nisibis
record_type: story
schema_version: 1
jobs:
- 1
- 2
- 3
register: emic
review_state: draft
cache_stability: static
title: The Correspondence of King Abgar, the Mission of Addai, and the Founding Succession
narrative_tier:
  tier: 3
  justification: 'Modern scholarship (Griffith 2003; J.W. Drijvers 1997) dates the Doctrina Addai''s composition,
    in the developed form told here, to the late 4th or, more likely, early 5th century — plausibly during
    Bishop Rabbula''s own episcopate (411–435), which falls just past this world''s own 410 boundary but
    squarely within its immediate successor community, the allowance Tier 3 explicitly makes for hagiographic
    and attributed material. This is flagged explicitly rather than smoothed over: the fuller text used
    here postdates this world''s own closing edge by up to roughly two decades. A shorter, earlier version
    of the core correspondence (without Addai''s own name, the portrait, or the Protonike/succession material)
    is independently attested by Eusebius, writing in the early 4th century (Historia Ecclesiastica 1.13),
    squarely within this world''s own window — meaning the correspondence-legend''s own earliest kernel
    is genuinely in-window, even though the fuller narrative told above reflects later elaboration. This
    is textbook Tier 3 material: attributed to specific named figures (Abgar, Addai, Aggai, Palut), shaped
    by recognizable legendary/hagiographic convention (a healing, a miraculous cross-discovery interpolated
    as a set-piece, a martyred second bishop), and valuable as evidence of what this community believed
    about its own legitimacy rather than as a report of what happened.'
text: 'This is the account this world tells of its own beginning. King Abgar, ailing, sends his archivist
  Hanan to Jerusalem, where Hanan witnesses the works of Jesus and brings back a report. Abgar writes
  to Jesus, asking him to come and heal him, and offering Edessa as a refuge from those who seek his life.
  Jesus, in reply, declines to come himself, but promises that after he has ascended he will send one
  of his own to Abgar — and blesses the city itself, so that "no enemy shall ever rule over it." Hanan,
  who is also the king''s painter, makes a portrait of Jesus and carries it back, and Abgar receives it
  with great honor.


  After the ascension, the apostle Judas Thomas sends Addai — one of the seventy-two — to Edessa. Addai
  lodges with a Jew named Tobia, heals Abgar and the nobles of the city, and is received openly. He preaches
  to the king, telling among other things the story of how the empress Protonike, wife of the emperor
  Claudius, discovered the true cross at Jerusalem; and he preaches to the people, denouncing the old
  gods of the city — Bel, Nebo, and the goddess Tar''atha — and calling them to the one true God. Before
  he dies, Addai appoints Aggai as his successor. Aggai is later killed — struck down for refusing to
  make ceremonial hats demanded of him by a rival claimant to authority — before he can himself ordain
  a successor. It falls to Palut to travel to Antioch, where he is ordained by Serapion of Antioch, tying
  Edessa''s own church, through this ordination, to the wider apostolic succession running back through
  Antioch to Peter.'
attested_occasion: 'The Doctrina Addai''s foundation account (the received text): Abgar''s correspondence
  with Jesus, the mission of Addai, the succession Addai-Aggai-Palut with Palut''s ordination at Antioch
  under Serapion - this world''s own telling of its beginning, Contested as formation-account and Inferential-Thin
  for any specific event (chunk front matter; composition scholarship rides srcSYR047).'
tellable_as: scene
owner_figure_id: syrfig005
voice_surface: 'This is the account our city tells of its own beginning - the king''s letter, the promise,
  the teacher sent. We tell it as the kept founding story, carried for its weight among us, not for its
  documentation. Usage guidance (chunk, verbatim): The Representative may offer this as the tradition''s
  own account of its own beginning: "This is how we tell of our own founding — how the King himself wrote
  to the Lord, and how Addai came after, and how the succession was carried forward even through Aggai''s
  death, to Palut, and from Palut outward to Antioch." The Representative must not present the specific
  events — the correspondence, Addai''s mission, Protonike''s discovery of the cross — as verified historical
  fact if a participant asks directly; the formation ideal (this world''s own conviction of legitimate
  origin) is what is being offered, not confirmed history.


  **Additional guidance:** Do not introduce the miraculous "image not made by hands" (the later Mandylion
  tradition) into this story. That specific belief is first attested only in the 6th century (Evagrius
  Scholasticus, c. 593 CE), nearly two centuries past this world''s own close, and is not part of the
  account rendered here — only Hanan''s ordinary painted portrait belongs to this world''s own record.
  See Absent Stories.'
confidence_line: Contested (as an account of what a formed life/community founding looks like); Inferential/Thin
  (for any specific event claimed as historical)
retrieval:
  tier: 3
  retrieve_when:
  - participant asks how this world tells its own founding story
  - participant asks about King Abgar, Addai, or this world's claimed apostolic origin
  - participant asks why this world believes its own community reaches back to the apostles.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant asks whether this actually happened as history (it does not — see Tier Justification
      and Doc_01, Section 2)
  - condition_type: sense-disambiguation
    text: participant asks about a miraculous, self-formed image of Christ ("image not made by hands")
      — that specific tradition is not part of this account and postdates this world's own close (see
      Absent Stories).
  force_llm_vote: false
sources:
- source_id: srcSYR020
  locus: Doctrina Addai (Teaching of Addai). Ed./trans. George Howard, The Teaching of Addai (Scholars
    Press, 1981); Jacob A. Lollar, The Doctrine of Addai (Cascade Books, 2023).
gravity_links:
- gravity_id: syrgrav004
  note: 'CO-P2-04: the chunk''s Formation Ecology Connection, verbatim (the S2.4 parking, converted at S2.5):
    This is our own foundation story, not a source of fact about how we actually began. What it shows
    directly is how we understood and justified our own legitimacy: an origin reaching back to Christ''s own
    lifetime, a founding by direct apostolic commission, and a succession secured in the end by tying
    ourselves to Antioch''s apostolic line rather than resting on Addai alone. Even our most confident claim
    to legitimacy resolves itself by reaching outward. That never-quite-self-sufficient pattern runs through
    our whole span, not only through this legend.'
---
Migrated at the S6.2/SYR S2.4-equivalent (2026-07-28) from `data/syriac_world/story_chunks/syrstory004_doctrina-addai.md` (mapping in `wrs/migrate/s62_syr_s24.py`; Story Text / Tier Justification / Usage Guidance / Confidence line verbatim; occasion/owner/frame authored per Desert-ALX S2.4 conventions).

[Formation Ecology Connection - parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] This is this world's own foundation myth, not a source of historical fact about its origin (Doc_01, Section 2 already established the actual beginning point as c. 200 CE, using the Chronicle of Edessa and Bardaisan's own attested career, not this account). What it reveals directly is how this world understood and justified its own legitimacy: an origin reaching back to Christ's own lifetime, a founding by direct apostolic commission, and an institutional succession secured, in the end, by tying itself to Antioch's own apostolic line rather than resting on Addai's authority alone. This connects to C4 (Authority-Structure Ambiguity): even this world's own most confident claim to legitimacy resolves its founding succession by reaching outward, to Antioch, rather than resting on a purely local chain of authority — a pattern of never-quite-self-sufficient legitimation this world lived with across its whole span, not only in this legend.
