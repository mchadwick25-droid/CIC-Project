---
id: syrlex003
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
term: 'taḥwyāṯā (singular: taḥwîṯâ)'
aliases:
- '"Demonstrations" (conventional English title)'
- '"Letters" (Aphrahat''s own alternate self-designation)'
quick_meaning: A taḥwîṯâ (plural taḥwyāṯā) is Aphrahat's own term for his twenty-three doctrinal treatises
  — conventionally titled "Demonstrations" in English, corresponding to the Greek apodeixis — several
  built on the twenty-two-letter Syriac acrostic so the alphabet itself scaffolds the argument in memory;
  he also calls the same works "Letters" on occasion, so this was not his only way of naming them.
world_meaning: 'A taḥwîṯâ (plural taḥwyāṯā) is Aphrahat''s own term for the twenty-three doctrinal and
  exhortatory treatises conventionally titled "Demonstrations" in English, corresponding to the Greek
  apodeixis — a reasoned, sustained demonstration of a point rather than a homily or a letter in the ordinary
  sense, though Aphrahat also refers to his own works as "Letters" on occasion, and this alternate self-designation
  should be carried alongside taḥwyāṯā rather than treated as though the demonstration-title were his
  sole way of naming his own work. Each taḥwîṯâ works systematically through its subject, several of them
  built on the twenty-two-letter Syriac acrostic, so that the alphabet itself becomes a scaffold for holding
  an argument in the memory across its full length.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: This is Aphrahat''s own genre self-designation, load-bearing
  specifically for how his corpus should be described and cited, and it is the textual home of Demonstration
  6 (the qyama''s primary evidentiary source) and of the Iḥidaya title as Aphrahat uses it. A participant
  who understands this term understands that Aphrahat''s own writings carry their own native name distinct
  from the modern English "Demonstrations" convention.'
distortion_risk: '**Modern Hearing / World Hearing:** A modern reader who encounters "Demonstrations"
  as a title may assume this is simply an English descriptor with no native-language equivalent, or may
  assume it is Aphrahat''s only way of naming his own work; in this world, taḥwîṯâ is Aphrahat''s own
  genre-term corresponding to the Greek apodeixis, and he also called the same works "Letters" on occasion
  — the naming was not fixed to one term even in his own usage.'
retrieval:
  tier: 2
  retrieve_when:
  - participant asks about Aphrahat's writings by name
  - participant asks what genre or kind of text a "Demonstration" is
  - conversation reaches Aphrahat's own authorial self-understanding.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking about Ephrem's writings (this term is exclusively Aphrahat's own genre-designation
      and does not apply to his corpus).
  force_llm_vote: false
sources:
- source_id: srcSYR010
  author_gravity_note: 'Jean Parisot, *Patrologia Syriaca* I/1–2 (1894/1907), the Doc_02/Registry edition
    of record (Source Registry #10).'
- source_id: srcSYR030
  author_gravity_note: 'Adam Lehto, *The Demonstrations of Aphrahat, the Persian Sage* (Gorgias Press,
    2010) (Source Registry #10, #30).


    Open flag carried from Doc_03: a "Valavanolickal 2005" translation date could not be independently
    reconfirmed in this pass — only a 2011 Gorgias edition was found. Reconcile with a direct check of
    the original Kottayam printing before this citation is relied upon for a precise date claim.'
original_script: ܬܚܘܝܬܐ
period_sense: Aphrahat's own genre-term for his twenty-three doctrinal treatises (Greek apodeixis; conventionally
  'Demonstrations'), several built on the twenty-two-letter Syriac acrostic so the alphabet scaffolds
  the argument in memory; he also called the same works 'Letters' - the naming was not fixed to one term
  even in his own usage (chunk Quick/World Meaning).
prior_sense: The word's ordinary sense - a showing, a reasoned demonstration or proof, corresponding to
  the Greek apodeixis (the chunk's own gloss) - which Aphrahat's usage applies as a self-designation rather
  than transforms.
modern_sense: '''Demonstrations'' assumed to be simply an English descriptor with no native-language equivalent,
  or assumed to be Aphrahat''s only name for his own work (chunk combined Modern/World Hearing).'
conceptual_distance_note: 'A naming-convention gap rather than a conceptual chasm: the corrective is that
  the corpus carries its own native name AND that Aphrahat''s own naming was plural (taḥwyāṯā and ''Letters'').
  Standard grounding: the entry is load-bearing for citation practice, not for a lived-concept distortion.'
semantic_domain: genre-self-designation
grounding_criterion: standard
voice_surface: Aphrahat called his own works taḥwyāṯā - demonstrations, a showing of the thing - and sometimes
  letters; each works through its subject in order, several strung on the twenty-two letters of the alphabet
  so that memory itself has a rail to hold the argument by.
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  verification_date: '2026-07-28'
  evidentiary_weight: corroborating
  formation_confidence: Documented
field_relations:
- type: material-source-of
  target_id: syrlex002
  note: 'Demonstration 6, the qyama entry''s primary evidentiary source, is itself one of Aphrahat''s
    taḥwyāṯā (both chunks'' Reciprocity Notes). Chunk Ecological Function (verbatim, absorbed per FLAG-002):
    This is Aphrahat''s own genre self-designation, load-bearing specifically for how his corpus should
    be described and cited, and it is the textual home of Demonstration 6 (the qyama''s primary evidentiary
    source) and of the Iḥidaya title as Aphrahat uses it. A participant who understands this term understands
    that Aphrahat''s own writings carry their own native name distinct from the modern English "Demonstrations"
    convention.'
- type: material-source-of
  target_id: syrlex007
  note: The taḥwyāṯā are the textual home of the Iḥidaya title as Aphrahat uses it (Dem 6:8, 7:20 - chunk
    EF and both Reciprocity Notes).
- type: material-source-of
  target_id: syrlex010
  note: The anti-Jewish material is a subset of this same corpus - roughly four of the twenty-three Demonstrations
    (syrlex010's own scope statement; its front-matter Related-Terms points here one-directionally, typed
    at authoring rather than left untyped).
- type: presupposed-by
  target_id: syrlex002
  note: Mirror of syrlex002's presupposes edge (Dem 6 is one of the taḥwyāṯā).
- type: presupposed-by
  target_id: syrlex007
  note: Mirror of syrlex007's presupposes edge (Dem 6:8, 7:20 are the Iḥidaya title's textual home).
- type: presupposed-by
  target_id: syrlex010
  note: Mirror of syrlex010's presupposes edge (the anti-Jewish subset presupposes the corpus).
---
Migrated at the S6.2/SYR S2.2-equivalent (2026-07-28) from `data/syriac_world/lexicon_chunks/syrlex003_tahwyata.md` (mechanical split; mapping in `wrs/migrate/s62_syr_chunk_split.py`). Related-Terms and new-authoring fields arrive at the S2.3-equivalent.

[Related-Terms Reciprocity Note - parked at the S2.2-equivalent; absorbed into field_relations notes at the S2.3-equivalent] Cross-referenced with qyama (Demonstration 6 is a taḥwîṯâ) and Iḥidaya (attested within the taḥwyāṯā, e.g. Dem. 6:8, Dem. 7:20). Both entries list this term back.
