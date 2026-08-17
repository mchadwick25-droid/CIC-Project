---
id: syrlex008
world_id: syriac-edessa-nisibis
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
term: Mar (ܡܪܝ)
aliases:
- '"my lord" (loose parallel honorific)'
quick_meaning: >-
  A title placed before a name, meaning my lord. Syriac Christians use it for
  bishops, for saints, and for teachers they revere - close to what Saint does
  in English. It is well attested in our years: a note copied in 510 calls
  Aphrahat "Mar Jacob, the Persian sage." Whether anyone called Ephrem by it
  while he lived is not confirmed.
world_meaning: ''
distortion_risk: '**Modern Hearing / World Hearing:** A participant may assume "Mar Ephrem" was a form
  of address already in use during Ephrem''s own lifetime (d. 373) or immediately after. No source confirms
  this specific compound within that window; it may reflect a later, veneration-driven convention, and
  should not be asserted as a contemporary usage without further check.'
retrieval:
  tier: 3
  retrieve_when:
  - participant uses "Mar" as a title prefix (e.g., "Mar Ephrem," "Mar Aphrahat")
  - participant asks what "Mar" means.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking about a specific bishop's formal office or title of authority rather than
      the honorific prefix itself (see Catholicos entry for office-title anachronism risk).
  force_llm_vote: false
sources:
- source_id: srcSYR010
  author_gravity_note: 'Aphrahat, Demonstrations (ed. Parisot, PS I/1-2). Licenses the record''s one
    concrete attestation: the 510 CE colophon of the Demonstrations'' own manuscript tradition calling
    Aphrahat "Mar Jacob, the Persian sage" (quick_meaning already states this; the source line was
    missing, not the source - gap closed 2026-08-14, redesign execution step 4). The broader
    "broadly attested honorific" claim rides the corpus-wide emic usage, and the distortion_risk
    caution (no confirmed "Mar Ephrem" within the window) stands unchanged.'
original_script: ܡܪܝ
period_sense: An honorific title-prefix, 'my lord,' used across Syriac Christianity for bishops, saints,
  and revered teachers (roughly parallel to 'Saint') - broadly attested for this world, but NOT confirmed
  as attached to Ephrem's own name during his lifetime (chunk Quick Meaning).
prior_sense: The ordinary Aramaic address 'my lord' (mar + first-person suffix) - a secular honorific
  whose ecclesial use is a specialization of everyday deference, per the chunk's own gloss.
modern_sense: '''Mar Ephrem'' assumed to be a form of address already in use during Ephrem''s own lifetime
  or immediately after (chunk combined Modern/World Hearing).'
conceptual_distance_note: 'A dating caution on a compound, not a conceptual gap: the honorific is real
  and low-controversy as a linguistic fact (Aphrahat called ''Mar Jacob, the Persian sage'' in a 510 CE
  colophon - itself post-window), but the specific compound ''Mar Ephrem'' within the window is unconfirmed
  and may be a later veneration-driven convention. Low grounding: included for runtime recognizability,
  the chunk says, not because it organizes the ecology.'
semantic_domain: honorific
grounding_criterion: low
voice_surface: Mar is how we say 'my lord' - for a bishop, a holy one, a teacher whose word is weighed.
  Whether anyone said 'Mar Ephrem' while Ephrem lived, our record does not show.
confidence:
  citation_specificity: B
  verification_state: unverified
  verification_date: '2026-07-28'
  evidentiary_weight: illustrative
  formation_confidence: Widely Accepted
field_relations:
- type: associated-with
  target_id: syrlex009
  note: 'Same semantic field of leadership address: Mar is the living honorific prefix; Catholicos
    the later office-title laid back over the same Persian church leadership. Symmetric mirror of
    syrlex009''s edge (gap closed 2026-08-14, redesign execution step 4).'
chunk_slug: mar
---
Migrated at the S6.2/SYR S2.2-equivalent (2026-07-28) from `data/syriac_world/lexicon_chunks/syrlex008_mar.md` (mechanical split; mapping in `wrs/migrate/s62_syr_chunk_split.py`). Related-Terms and new-authoring fields arrive at the S2.3-equivalent.

[Related-Terms Reciprocity Note - parked at the S2.2-equivalent; absorbed into field_relations notes at the S2.3-equivalent] No reciprocal cross-reference asserted. This is a general honorific, real and low-controversy as a linguistic fact, but not itself structurally tied to another lexicon entry — included for completeness and runtime recognizability rather than because it organizes the ecology.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `unverified`, cross-checked against this term's own linked sources[] and their discovery_channel disclosures. **Flagged as a judgment call**: no sources[] linkage at all in this record; cannot confirm any verification was performed; this record's own prose does not independently state its verification story, so the grade rests on inference from source-linkage metadata rather than an explicit first-person statement — noted here rather than re-asserted as settled fact.
