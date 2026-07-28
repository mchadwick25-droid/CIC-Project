---
id: syrstory006
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
title: Jacob of Nisibis and the Deliverance of the City
narrative_tier:
  tier: 3
  justification: 'This is unambiguous hagiographic/legendary material by genre and by direct textual evidence:
    Theodoret, writing in the 5th century — roughly 130 to 160 years after the sieges (338, 346, or 350
    CE) — is the earliest source for the specific miracle, and his own text is explicit and unambiguous
    about who performs it. Per Theodoret (Historia Ecclesiastica II.26/30, NPNF2 translation): "the excellent
    Ephraim... besought the divine Jacobus to mount the wall... So the divine man consented and climbed
    up into a tower... he discharged no other curse than that mosquitoes and gnats might be sent forth
    upon them... The Persians abandoned their camp and fled headlong." This attributes the miracle to
    Jacob, with Ephrem as the one who urges him to act — a distinction this document holds deliberately,
    because the alternative (crediting Ephrem himself with the miracle) is a documented misattribution
    this project''s own research explicitly checked and rejected, cross-confirmed independently by two
    separate research passes against the same primary-source quotation. Ephrem''s own genuine hymnic corpus
    (Beck''s critical edition of the Carmina Nisibena) does commemorate the deliverance of Nisibis, which
    is why Ephrem legitimately belongs in this story at all — but as witness and hymnodist, never as the
    wonder-worker.'
text: 'During one of the Persian sieges of Nisibis, with Shapur II''s army encamped against the walls,
  Ephrem urged the aged bishop Jacob to climb the ramparts and look out upon the besieging army — to let
  his prayer, not the city''s own strength, be its defense. Jacob consented, mounted a tower, and looking
  upon the Persian camp asked God to send not death upon them, but the smallest of afflictions: mosquitoes
  and gnats. The insects came upon the Persian camp in such numbers that the men and even the elephants
  and horses could not bear it, and the army broke camp and withdrew, Shapur himself reportedly deceived
  into believing a kingly figure on the battlements to be the Roman emperor. Ephrem, who did not himself
  perform the deliverance, went on to commemorate it afterward in verse, in the hymns of his Carmina Nisibena.'
attested_occasion: 'The siege-deliverance tradition: Theodoret (HE II.26/30; HR I, 5th c.) tells of Jacob''s
  prayer from the ramparts at Ephrem''s urging and the plague of gnats and mosquitoes that broke the Persian
  camp; Ephrem''s own Carmina Nisibena commemorate the sieges in verse (the chunk''s own corroboration
  note) - tradition Contested, the specific event Inferential-Thin (Tier 3).'
tellable_as: scene
owner_figure_id: syrfig003
voice_surface: 'We tell the deliverance as the tradition sings it - the old bishop on the wall, the smallest
  of afflictions asked for and sent. Our own teacher put the city''s survival into hymns; the story''s
  marvels we carry as the tradition''s own telling, not as the record''s proof. Usage guidance (chunk,
  verbatim): The Representative may offer this as the tradition''s own memory of the city''s deliverance,
  careful to preserve the correct roles: "It is said that when the enemy camped against our walls, Ephrem
  himself urged Jacob our bishop to climb the tower and pray, and that Jacob''s prayer, not our own strength,
  sent the enemy from the field — and it was left to us to sing of it after." The Representative must
  never present Ephrem as the one who performed the miracle; if a participant states or assumes this,
  the Representative should gently correct the roles within the story rather than let the misattribution
  stand uncorrected.


  **Additional guidance:** This story should be handled with the same care given to any Tier 3 miracle
  account — offered as the tradition''s own memory of deliverance, not as verified historical fact about
  mosquitoes routing an army.'
confidence_line: Contested (as tradition); Inferential/Thin (as a specific historical event)
retrieval:
  tier: 3
  retrieve_when:
  - participant asks how Nisibis was remembered as having survived Shapur II's sieges
  - participant asks about Jacob of Nisibis's standing as a holy man
  - participant asks about Ephrem's own relationship to Jacob or to the Nisibis sieges specifically.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant asks whether Ephrem himself performed this miracle — he did not, in this tradition
  - condition_type: sense-disambiguation
    text: attributing it to him would be a documented misattribution this world's own record does not
      support (see Tier Justification). Do not retrieve where the participant's question concerns Ephrem's
      own theological or hymnic corpus in general (use the raza/shrara or heresiology material instead).
  force_llm_vote: false
sources:
- source_id: srcSYR043
  locus: Theodoret of Cyrrhus, Historia Ecclesiastica II.26/30 and Historia Religiosa I (5th c.); corroborating
    detail from Ephrem's own Carmina Nisibena, ed. Edmund Beck, CSCO 218-219 (1961)
- source_id: srcSYR004
  locus: Theodoret of Cyrrhus, Historia Ecclesiastica II.26/30 and Historia Religiosa I (5th c.); corroborating
    detail from Ephrem's own Carmina Nisibena, ed. Edmund Beck, CSCO 218-219 (1961)
---
Migrated at the S6.2/SYR S2.4-equivalent (2026-07-28) from `data/syriac_world/story_chunks/syrstory006_jacob-nisibis-deliverance.md` (mapping in `wrs/migrate/s62_syr_s24.py`; Story Text / Tier Justification / Usage Guidance / Confidence line verbatim; occasion/owner/frame authored per Desert-ALX S2.4 conventions).

[Formation Ecology Connection - parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] This story gives narrative shape to how this world's own record remembers surviving under the contested Roman-Persian Mesopotamian frontier condition Doc_08 documents structurally as Force 1A-2, which names Nisibis specifically as occupying "a third, unstable position — contested repeatedly through the 3rd century, fixed as Roman only from 298 (Peace of Nisibis), and ceded to Persia in 363." **Correction (Round 1 review):** an earlier draft of this paragraph cited Force 2A-1 for this connection; Force 2A-1 is Doc_08's own name for Sasanian state persecution of Christians inside Persia (the poll-tax campaign, Simeon bar Sabbae, the twenty-year primatial vacancy) — a related but distinct phenomenon from the military sieges of Nisibis this story concerns. Doc_08 does not document the sieges themselves as a named force; Force 1A-2 is the closest structural antecedent it actually contains, and is cited here instead. It also illuminates the qyama-adjacent, non-episcopal teaching role this world's Representative construction has settled on (a teacher who urges and commemorates, rather than a bishop who acts with singular authority) — Ephrem's own place in this story is exactly that of the teacher who prompts and later sings of deliverance, not the one who works it. **Correction (2026-07-08, Doc_09 Validation Layer):** an earlier draft of this sentence used "malpana" as a settled descriptor of this role; Doc_03, Section 3.1 found no direct textual attestation of Ephrem holding this specific title within this world's own 200–410 window, tracing the association instead to later hagiographic tradition. "Teacher" is used here without that title, consistent with Doc_03's finding.
