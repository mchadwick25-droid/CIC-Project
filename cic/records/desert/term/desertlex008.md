---
id: desertlex008
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
register: emic-unavailable
review_state: draft
cache_stability: static
term: Apophthegma (Saying)
aliases:
- apophthegma
quick_meaning: The terse, memorable saying that is this world's primary vehicle of teaching.
plain_explanation: 'A short, sharp saying was this world''s main way of teaching. An elder gave it to one
  person, for one moment, face to face. Its shortness was on purpose. A few words could be carried and
  turned over during long hours of work. The famous collections came later, made by editors after this
  world''s own time — and it is those editors, not this world''s own contemporary idiom, who supply this
  record''s own headword. "Apophthegma" is the editors'' Greek rhetorical label for the collected genre,
  applied after the fact; it is not a word this build''s own voice material ever puts in an elder''s or a
  disciple''s own mouth. What this build''s own voice material consistently calls the thing itself, before
  any editor named the genre it became part of, is plainer — a disciple came and asked an elder for a word,
  and the elder gave one. That plain idiom is this record''s own voice_surface below, is how desertstory009
  and desertstory010 (Amma Syncletica, Amma Theodora) each describe what the tradition kept of them ("tested
  words the Apophthegmata kept" / "the tradition kept"), and is how Papnoute himself uses it in deployment
  (LiveTest_Transcripts_2026-07-11.md, Turn 4 — "A word given by a stranger... we gave them a word we had
  watched proven"). No Greek-language formula for the request itself (e.g. a specific incipit phrase) is
  attested anywhere in this world''s own source records in this build — srcDES005 names the corpus and its
  compilers but preserves no such formula — so none is supplied here; "a word" stands as the attested
  English-register idiom actually used across this build''s own material, not a reconstructed Greek phrase.
  Today the sayings read like general wisdom for anyone. Each one was actually aimed counsel for a single
  case. The book form hides the aim.'
world_meaning: This world produced almost no sustained theological treatise outside one notably systematic
  teacher; teaching that could not be reduced to a portable saying largely does not survive in this world's
  own idiom. The form's brevity is itself a formation technique — something turned over in the mind during
  solitary labor — not merely a container for content.
distortion_risk: World Hearing — each saying was originally occasion-bound, given by a specific elder
  to a specific disciple's specific situation; its later collection into a general-purpose anthology by
  unnamed compilers is a distinct editorial layer, not a transparent window onto original context.
retrieval:
  tier: 1
  retrieve_when:
  - participant asks about how teaching was passed down, or quotes/references a "saying"
  do_not_retrieve_when: []
  force_llm_vote: false
sources:
- source_id: srcDES005
  author_gravity_note: 'The *Apophthegmata Patrum* (Alphabetical and Systematic collections) — Widely
    Accepted as to the corpus''s general origin in this world''s own oral teaching tradition; Contested
    as to how faithfully any individual saying preserves its original strand-specific context versus reflecting
    later compilers'' own arrangement, since the collection was compiled after this world''s own closing
    boundary by editors whose selection criteria and possible harmonization across strands remain a live
    methodological question. Genre note: a collected-sayings genre oriented toward terse, practically
    applicable teaching rather than narrative or chronicle — its own brevity is itself a formation technique,
    and the collection''s form does not merely describe but performs the oral, elder-to-disciple transmission
    mechanism this world used to teach.'
modern_hearing: Modern Hearing — a "quote" or aphorism in the modern decontextualized, quotable-content
  sense.
period_sense: The terse, memorable, occasion-bound saying — given by a specific elder to a specific disciple's
  situation — that is this world's primary teaching vehicle; its brevity is itself a formation technique,
  turned over in the mind during solitary labor. The collected form postdates the world's own boundary
  and is a distinct editorial layer (Doc_06 §1.8).
prior_sense: 'Classical Greek rhetorical vocabulary: the pointed memorable saying (apophthegma) of collections
  and anecdote. Lexical background beyond the build''s documents: UNVERIFIED against a registry source.'
modern_sense: Heard today as a decontextualized quote or aphorism — quotable content (Doc_06 §1.8 Modern
  Hearing).
conceptual_distance_note: 'Moderate-to-sharp gap: each saying was occasion-bound counsel, and the anthology
  that makes it feel general-purpose is later compilers'' work, not a transparent window (Doc_06 §1.8
  World Hearing; Doc_02 §§1.5, 2.3).'
semantic_domain: authority-and-transmission
voice_surface: When we repeat a word of the old men, we tell you also to whom it was said, if we know
  it — a word given to one man's case is not a law for every man.
grounding_criterion: standard
eviction_priority: 2
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  verification_date: '2026-07-26'
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
field_relations:
- type: presupposes
  target_id: desertlex006
  note: 'The saying presupposes the elder relationship that produced it; the primary carrier of elder
    authority and of practical, situational scriptural engagement (Doc_06 §1.8 Ecological Function, absorbed
    per FLAG-002). Chunk Ecological Function (verbatim, absorbed per FLAG-002): The primary carrier of
    elder authority and of practical, situational scriptural engagement (scripture deployed within sayings
    occasion-by-occasion rather than expounded systematically).'
chunk_slug: apophthegma
---
S2.2 mechanical split + S2.3 new authoring (2026-07-26). Sense fields condensed from and cited to Doc_06; prior senses not developed in the build's documents are marked UNVERIFIED in-line. EF parking (FLAG-002) restructured into typed field_relations; Related-Terms entries with no Desert chunk (Xeniteia, Kellion, Apatheia, Theōria, Nēpsis, Penthos, Synaxis, Antirrhēsis) are S2.9 Change-Order material, not records invented here.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 1 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).

[Register Correction (2026-08-05, Rigor P1-5 fix)]: `register` corrected from `emic` to `emic-unavailable`. This world's own doc 13-named defect: "Apophthegma" is the editors' Greek rhetorical label for the collected genre (5th-6th c.), not this world's own contemporary idiom, and this record's own `plain_explanation` already said so before this fix without the record's `register` field reflecting it. `plain_explanation` expanded to name the etic label as such and to point to the attested emic idiom already present elsewhere in this build's own voice material — a disciple asking an elder for "a word" (this record's own `voice_surface`; desertstory009/desertstory010; Papnoute's own usage, LiveTest_Transcripts_2026-07-11.md Turn 4) — rather than inventing a Greek-language formula no source record in this build attests. `aliases` deliberately left unchanged (not adding "word" as a highlight-key alias: it is on the alias-safety gate's generic-word blocklist for good reason, and this fix is a register/explanation correction, not a retrieval change).
