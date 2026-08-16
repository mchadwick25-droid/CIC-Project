---
id: pahcstory004
world_id: post-apostolic-house-church
record_type: story
schema_version: 1
jobs:
- 1
- 2
- 3
register: emic
key_line: "sang a hymn to Christ"
signature: true
review_state: draft
cache_stability: static
title: Pliny's Interrogation in Bithynia-Pontus
narrative_tier:
  tier: 1
  justification: 'A specific, dated, named-author account of a real interrogation, written to a named
    recipient (the emperor) who replied in writing — an unusually well-documented exchange for this period.
    Contested points: whether the "ordinary meal" Pliny describes was itself a Eucharist, an agape meal,
    or something else; and whether Pliny''s account reflects a general legal condition applying across
    the empire or scattered, locally-triggered exposure specific to Bithynia-Pontus.'
text: 'In his letter to the emperor Trajan, Pliny the Younger, governor of Bithynia-Pontus, records that
  he was unsure how to handle charges against Christians brought before him. He asked the emperor directly
  for guidance. He describes questioning those accused. He executed those who persisted in the name after
  repeated warning. He reserved Roman citizens for trial in Rome instead. He wanted to learn more about
  what these people actually did. So he tells us he tortured two enslaved women, called *ministrae*, to
  get information. Some read *ministrae* as a functional title, "ministers" or "deaconesses," though this
  is contested.


  What Pliny reports learning was, in his own words, "nothing else than depraved, excessive superstition."
  These were people who met before dawn on a fixed day. They sang a hymn to Christ "as to a god." They
  bound themselves by oath not to commit theft, adultery, or breach of trust. Later they met again to
  share an ordinary, harmless meal.


  Trajan''s reply, also preserved, instructs Pliny not to seek out Christians actively, and not to act
  on anonymous charges. But he was to punish those who were rightly accused and refused to recant.'
attested_occasion: 'Bithynia-Pontus, c. 111-113: Pliny''s own letter to Trajan - executions after warning,
  citizens reserved for Rome, two ministrae tortured for information, ''nothing else than depraved, excessive
  superstition'' found; Trajan''s rescript (no seeking out, no anonymous accusations) preserved with it.
  The sole non-Christian eyewitness account of a gathering, its oath, and its meal.'
tellable_as: scene
owner_figure_id: pahcfig006
voice_surface: 'We tell this in the governor''s own words, because they are the only outside eyes that
  ever looked closely at us and wrote down what they saw: the fixed day before dawn, the hymn to Christ
  as to a god, the oath against theft and adultery and broken trust, the ordinary and harmless meal. And
  we do not pass over what it cost: two women of ours, tortured for it. The word for them - ministrae
  - is his, not ours. Usage guidance (chunk, verbatim): **This story requires particular care.** It must
  not be offered as if it were the *ministrae*''s own story — it is Pliny''s report, filtered through
  elite Roman prejudice and produced by a method ancient jurists themselves distrusted as unreliable.
  If this story is used, the Representative should name plainly that these two women have no surviving
  voice of their own: what survives is what their torturer chose to record, not their own account of their
  formation or their community. Doc_02 §7 states this directly: "no surviving voice of their own." See
  also Section 4, Item 4 of Doc_09.


  The Representative may offer the surrounding detail (Pliny''s uncertainty, Trajan''s cautious reply,
  the oath and meal description) as historically Documented content, with the *ministrae* detail handled
  only with the above disclosure, and only where the conversation''s context makes that level of content
  appropriate.'
confidence_line: Documented (the letter and its basic content) / Contested (what the "ordinary meal" was;
  whether this reflects one standing legal condition or scattered local exposure)
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks how Roman authorities actually treated Christians in this period
  - participant asks about G03 (State Pressure/Legal Precarity)
  - participant asks what outside, non-Christian evidence exists for this world at all.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: Participant is vulnerable around themes of torture, sexual violence, or slavery, or has not
      signaled readiness for content of this weight
  - condition_type: sense-disambiguation
    text: conversation does not need the specific detail of the *ministrae* — a lighter reference to Pliny's
      general uncertainty about how to handle Christians may suffice instead.
  force_llm_vote: false
sources:
- source_id: srcPAHCP07
  locus: Pliny the Younger, *Letters* 10.96–97 (Registry P07), c. 111–113 CE.
gravity_links:
- gravity_id: pahcgrav003
  note: 'CO-P2-04: the chunk''s Formation Ecology Connection, verbatim (the S2.4 parking, converted at S2.5): Our
    clearest evidence of what pressure from the state actually looked like: not a systematic empire-wide
    persecution, but real, local, lethal exposure, under legal uncertainty that reached the officials
    themselves. It is also the only description we have of our own practice from outside - the sole
    non-Christian eyewitness account of a gathering, its oath and its shared meal. It does work no inside
    source can do. It shows how our practices looked to a man with the power of life and death over us, and
    what he found alarming - and, just as tellingly, what he did not.'
chunk_slug: pliny-interrogation
---
Migrated at the S6.2/PAHC S2.4-equivalent (2026-07-31) from `data/pahc_world/story_chunks/pahcstory004_pliny-interrogation.md` (mapping in `wrs/migrate/s62_pahc_s24.py`; Story Text / Tier Justification / Usage Guidance / Confidence line verbatim; sources extracted mechanically from the Source line's own Registry tags; occasion/owner/frame authored per the fleet S2.4 conventions).

[Formation Ecology Connection - parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] This is this world's clearest evidence for G03 (State Pressure/Legal Precarity, Supporting) — not a systematic empire-wide persecution, but real, local, lethal exposure operating under genuine legal uncertainty even among Roman officials themselves. It also supplies this world's only outside description of internal practice — however filtered, it is the sole non-Christian eyewitness account of a gathering, its oath, and its shared meal.

This story does formation work no internal source can do: it shows how this world's own practices looked to an outsider with the power of life and death, and what that outsider found alarming (or, notably, did not).

UPDATE 2026-08-16 (T3 readability follow-on): gate_voice_readability flagged the original text field at
FK grade 21.2 / FRE 23.0 - the first paragraph was one 90-word sentence stacking a parenthetical aside
inside an em-dash aside, and the second paragraph was a single em-dash-joined enumeration of four practices.
Per Mark's decision to extend the readability pass to story records, both long sentences are split into
short ones along their own existing clause boundaries (one clause per sentence, in the same order), plus
a few plain-synonym swaps ("uncertain" -> "unsure," "accusations" -> "charges," "extract information" ->
"get information," "reassembled" -> "met again," "properly accused" -> "rightly accused"). All three
embedded direct quotations ("nothing else than depraved, excessive superstition," "sang a hymn to Christ"
"as to a god," "ministers"/"deaconesses") are untouched, word for word, and the *ministrae* term and its
contested-reading hedge are unchanged. No fact, hedge, or attribution is dropped - the torture of the two
enslaved women, the reservation of Roman citizens for trial in Rome, and Trajan's own instructions are
all still stated in full. Re-scored: FK 7.8 / FRE 61.9, clearing both thresholds.
