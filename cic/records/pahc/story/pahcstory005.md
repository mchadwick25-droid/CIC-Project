---
id: pahcstory005
world_id: post-apostolic-house-church
record_type: story
schema_version: 1
jobs:
- 1
- 2
- 3
register: emic
key_line: "not so much of the crime of arson as of hatred of the human race"
review_state: draft
cache_stability: static
title: Nero's Fire and the First Scapegoating
narrative_tier:
  tier: 1
  justification: A specific, dated historical event, from a named, datable historian, describing named
    individuals in the surrounding narrative (Nero) though no Christian individual by name. Widely Accepted
    as basically authentic to Tacitus's own text; Contested is the live scholarly dispute (associated
    with Brent Shaw's 2015 argument and the responses to it, including Christopher Jones) over whether
    a discrete, fire-linked, named-group persecution of "Christians" actually occurred in 64 CE as Tacitus
    describes, or whether this reflects a later, more general memory of scapegoating retrojected onto
    the fire.
text: 'The Roman historian Tacitus wrote about this roughly fifty years after it happened. He records what
  happened after the great fire of Rome in 64 CE. Rumors spread that the emperor Nero himself had ordered
  the burning. Nero shifted blame onto a group he calls Chrestiani (Christians), "hated for their abominations."
  Tacitus tells us that those arrested named others. A great multitude was convicted - "not so much of
  the crime of arson as of hatred of the human race." They were executed with cruelty that was public
  and deliberate. They were wrapped in animal skins and torn apart by dogs, crucified, or set alight as
  human torches to light Nero''s gardens at night.


  No Christian individual is named. The account comes entirely from outside. It was written decades later
  by a historian with his own reasons for painting Nero as a monster.'
attested_occasion: 'Rome, 64 CE, told c. 116: Tacitus''s account of Nero''s scapegoating after the fire
  - a great multitude convicted ''not so much of arson as of hatred of the human race,'' the theatrical
  cruelty, no Christian named. The Shaw/Jones dispute (whether a discrete fire-linked persecution of Christians
  as a named group occurred, or later memory retrojected) carried at full strength per the chunk.'
tellable_as: background-fact
owner_figure_id: pahcfig007
voice_surface: 'We tell our own beginning-condition through an outsider''s pen, because our own record
  keeps no account of it: the fire, the blame shifted onto us, the deaths made into spectacle. No name
  of ours survives from it. Whether it happened as one event or was remembered into one, even those who
  study it cannot settle - and we hold that openness rather than claiming a certainty no one has. Usage
  guidance (chunk, verbatim): The Representative may offer this as historical background explaining why
  this world''s formation logic developed the way it did — argued and transmitted deliberately, in the
  absence of direct living memory of the founding generation. If pressed for detail beyond what the account
  itself supports — whether this was truly a discrete, named-group persecution, or a scattering of individual
  deaths remembered afterward as one event — the Representative should hold that uncertainty honestly,
  in-world, rather than presenting either version as the settled shape of what happened.


  Additional guidance: no Christian individual is named in this account. It should not be used to imply
  any specific person''s martyrdom under Nero — that would exceed what the source itself supports.'
confidence_line: Widely Accepted (the passage's basic authenticity) / Contested (whether a discrete, fire-linked
  persecution of Christians as a named group actually occurred)
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks why this world's formation logic is "argued, not inherited"
  - participant asks about this world's origin or generative starting point
  - participant asks about G03 (State Pressure) background or the loss of an eyewitness generation.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: Participant needs specific internal community detail — this story is entirely outside/etic and
      names no Christian individual
  - condition_type: sense-disambiguation
    text: pair with an internal-voice story rather than using it alone as a full answer.
  force_llm_vote: false
sources:
- source_id: srcPAHCP08
  locus: Tacitus, *Annals* 15.44 (Registry P08), written c. 116 CE describing events of 64 CE.
gravity_links:
- gravity_id: pahcgrav001
  note: 'CO-P2-04: the chunk''s Formation Ecology Connection, verbatim (the S2.4 parking, converted at S2.5): The
    closest thing we have to an origin story, though it is not a practice. It is the condition the whole of
    our life grows out of: the eyewitness generation gone, and the name Christian suddenly visible, public
    and dangerous. That is a large part of why what we hold has to be argued and handed on deliberately
    rather than simply remembered by those who were there.'
- gravity_id: pahcgrav003
  note: Named in the same FEC (full text on this record's first gravity link).
chunk_slug: nero-scapegoating
---
Migrated at the S6.2/PAHC S2.4-equivalent (2026-07-31) from `data/pahc_world/story_chunks/pahcstory005_nero-scapegoating.md` (mapping in `wrs/migrate/s62_pahc_s24.py`; Story Text / Tier Justification / Usage Guidance / Confidence line verbatim; sources extracted mechanically from the Source line's own Registry tags; occasion/owner/frame authored per the fleet S2.4 conventions).

[Formation Ecology Connection - parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] This is the closest thing this world has to a generative origin story — not a formation practice, but the structural condition Doc_01 and Doc_08 both treat as this whole world's own generative trigger. Doc_08 names this event as generative for G01 (Authority Consolidation): the loss of an eyewitness generation and the sudden, violent visibility of "Christian" as a named, targetable category are part of why this world's formation logic must be argued and transmitted deliberately rather than simply inherited by direct memory.

UPDATE 2026-08-16 (T3 readability follow-on): gate_voice_readability flagged the original text field at
FK grade 16.9 / FRE 33.0 - the first paragraph was one 90-word sentence stacking a participial opener, a
rumor clause, an em-dash-set-off quotation, and a colon-introduced list of execution methods. Per Mark's
decision to extend the readability pass to story records, the long sentence is split into short ones along
its own existing clause boundaries (one clause per sentence, in the same order), plus a couple of plain-synonym
swaps ("illuminate" -> "light," "portraying" -> "painting"). Both embedded direct quotations ("hated for
their abominations," "not so much of the crime of arson as of hatred of the human race") are untouched,
word for word. No fact, hedge, or attribution is dropped - Tacitus's roughly-fifty-year gap, the rumor
about Nero's own role, the Chrestiani name, the multitude convicted, and each named method of execution
are all still stated in full, and no Christian individual is named, as before. Re-scored: FK 8.0 / FRE
60.9, clearing both thresholds.
