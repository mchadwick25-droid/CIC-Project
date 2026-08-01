---
id: ijclex002
world_id: imperial-juridical-christianity
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
term: presbeia (tēs timēs)
aliases:
- prerogative of honor
- primacy of honor
- New Rome's rank
quick_meaning: We hold that a see's rank follows the throne it stands beside — Constantinople is second
  only because it is where the emperor now sits, New Rome beside old Rome, and that is reason enough.
world_meaning: 'When the fathers gathered at Constantinople, they did not pretend that our own city held
  the standing it now holds because an apostle once walked its streets — no apostle did. We are not ashamed
  of that; we do not need it to be true. Our city''s standing is real for a different and, we hold, no
  lesser reason: this is where the empire itself now governs, where the councils themselves are convened,
  where the faith is defended in the same halls the law is written in. A see that stands beside the throne
  stands where the church''s own defense of the truth is actually decided and enforced. That is not a
  lesser claim than apostolic descent. It is a different claim, resting on a different and, in our own
  time, no less real foundation.


  This is why, when the fathers gathered again at Chalcedon, we asked only that the ruling already made
  in our favor at the earlier council be confirmed and carried further — that our own rank, second only
  to Rome, be settled beyond dispute, precisely because we are New Rome. Rome''s own delegate did not
  agree, and the bishop of Rome himself, once he heard of it, refused to receive what we had settled.
  We do not think this refusal changes what is true. A city''s nearness to the throne is not a claim that
  needs Rome''s permission to be real; it is a fact about where the empire''s own weight now rests, and
  we hold that the church''s own order should follow that weight honestly rather than pretend the world
  has not moved since the apostles'' own day.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: *Presbeia*, grounded in *Nea Rhōmē*''s own political-geographic
  fact, is the rival claim *primatus* must be understood alongside, never in isolation — a participant
  who understands this term also understands why this world''s own record shows no single, settled answer
  to the question of which see ranks where, and why *communio* itself becomes contested precisely at the
  seam between these two claims.'
distortion_risk: This world's own Constantinopolitan actors do not experience their own claim as religiously
  hollow. For them, the empire's own defense of orthodoxy is itself a religious fact, not merely a political
  convenience, and a see's proximity to where that defense is actually conducted is, on their own understanding,
  a genuine spiritual as well as institutional standing — not a lesser substitute for apostolic descent,
  but a different, equally serious ground.
retrieval:
  tier: 1
  retrieve_when:
  - participant asks about Constantinople's own claim to rank
  - participant asks about Canon 3 or Canon 28
  - participant asks why a see's importance would follow the emperor's own residence
  - conversation touches the dispute at Chalcedon over rank.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: the participant's question is actually about Rome's own claim, grounded differently (retrieve
      primatus instead)
  - condition_type: sense-disambiguation
    text: the participant has not yet encountered the world's own founding alliance with Constantine and
      would not yet have the frame to place this term.
  force_llm_vote: false
sources:
- source_id: srcIJC13
  author_gravity_note: Canon 3 of the Council of Constantinople (381); Canon 28 of the Council of Chalcedon
    (451); Leo I's own letters rejecting Canon 28, used here as evidence of the claim's contested reception,
    not of its own content. **Note:** this world's own record of Constantinople's own self-understanding
    survives primarily through conciliar acts rather than through an individual advocate's own extended
    writing, in contrast to *primatus*'s richer individual-voice record (Leo, Damasus) — a different,
    thinner kind of evidentiary base, named here rather than papered over.
modern_hearing: A modern participant is likely to hear "rank follows the emperor's residence" as an obviously
  cynical, purely political claim with no genuine religious content — assuming a claim grounded in political
  geography must be religiously hollow by definition.
original_script: πρεσβεῖα
semantic_domain: juridical ecclesiology - see-rank by imperial proximity
modern_sense: '''Constantinople''s honor'' heard as empty ceremony or as naked politics - the religious
  register assumed hollow (chunk Modern Hearing).'
period_sense: A see's rank follows the throne it stands beside - New Rome second because the emperor sits
  there, 'and that is reason enough'; the empire's own defense of orthodoxy itself a religious fact on
  this strand's own understanding.
prior_sense: Greek presbeia - 'seniority, precedence, an embassy's dignity' - the ordinary rank-word Canon
  3 puts to juridical work; a builder note, UNVERIFIED.
grounding_criterion: high
conceptual_distance_note: 'GROUNDING (the enum''s free-text companion, carried here): Canon 3 (381) and
  Canon 28 (451) as the claim''s own conciliar form; Leo''s rejection as direct evidence the claim was
  contested AT THE TIME (the chunk''s own CT note). | DISTANCE: The claim survives primarily in conciliar
  acts, not an individual advocate''s corpus - the chunk''s own contrast with primatus; the S2.1b Dagron
  gap rides here.'
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  verification_date: '2026-07-31'
  evidentiary_weight: load-bearing
  formation_confidence: Contested
voice_surface: 'STRAND B''S OWN VOICE (the Plural-Voices device): ''a see''s rank follows the throne it
  stands beside - Constantinople is second only because it is where the emperor now sits, New Rome beside
  old Rome, and that is reason enough.'' Neither entry speaks for the world as a whole.'
field_relations:
- type: tension-with
  target_id: ijclex001
  note: 'Chunk Ecological Function (verbatim, absorbed per FLAG-002): Presbeia, grounded in Nea Rhome''s
    own political-geographic fact, is the rival claim primatus must be understood alongside, never in
    isolation - a participant who understands this term also understands why this world''s own record
    shows no single, settled answer to the question of which see ranks where. Symmetric mirror of the
    A/B contest.'
- type: presupposes
  target_id: ijclex010
  note: The rank claim rests on the New-Rome premise (the EF's own 'grounded in Nea Rhome's political-geographic
    fact'); inverse pair - ijclex010 carries presupposed-by.
- type: associated-with
  target_id: ijclex004
  note: Rank exercised through communion standing - whose fellowship counts; symmetric.
- type: associated-with
  target_id: ijclex006
  note: The orthodoxy the empire defends is the same settlement both strands claim to guard; symmetric.
- type: presupposes
  target_id: ijclex007
  note: 'The claim exists IN canon form - Canon 3, Canon 28: without the council there is no presbeia
    claim to cite; inverse pair with ijclex007.'
contested_claim_ids: []
---
Migrated at the S6.2/IJC S2.2-equivalent (2026-07-31) from `data/imperial_juridical_world/lexicon_chunks/ijclex002_presbeia.md` (mechanical split; mapping and alias authoring tables in `wrs/migrate/s62_ijc_s22.py` - the FLAG-035 corrections and the one Rule-A birth drop declared there; the third world born matching the runtime key space AND the gate). Related-Terms and authored fields arrive at S2.3.

[Plural-Voices Note - parked at the S2.2-equivalent; typed home per the splitter docstring] This entry is written from Strand B's own voice specifically (Constantinople's own self-understanding) — the deliberate counterpart to *primatus*'s own Strand A voice, per Doc_01's three-strand finding. Neither entry speaks for the world as a whole; each speaks for its own strand's own contested claim. **This is a lexicon-organization device only — see the same caution recorded in the *primatus* entry and Doc_06 §5, Open Item 4: it does not pre-decide a Representative voice or identity question.**

[CT Contest Type - parked at the S2.2-equivalent; typed home per the splitter docstring] **Meaning:** whether Canon 3 and Canon 28's "New Rome" reasoning describes an already-accepted fact about Constantinople's status or asserts a novel juridical claim dressed as description is itself contested — Leo's own rejection is direct evidence the claim was contested at the time it was made, not only by later historians assessing it retrospectively.

[Final Assembly Instruction - parked at the S2.2-equivalent; typed home per the splitter docstring] Completed per `L4-Templates/Deployment_Lexicon_Chunk_Template.md` V1.0. No brackets or builder notes remain; CT Contest Type completed per Doc_06 §3.
