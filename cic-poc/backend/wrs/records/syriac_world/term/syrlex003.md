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
---
Migrated at the S6.2/SYR S2.2-equivalent (2026-07-28) from `data/syriac_world/lexicon_chunks/syrlex003_tahwyata.md` (mechanical split; mapping in `wrs/migrate/s62_syr_chunk_split.py`). Related-Terms and new-authoring fields arrive at the S2.3-equivalent.

[Related-Terms Reciprocity Note - parked at the S2.2-equivalent; absorbed into field_relations notes at the S2.3-equivalent] Cross-referenced with qyama (Demonstration 6 is a taḥwîṯâ) and Iḥidaya (attested within the taḥwyāṯā, e.g. Dem. 6:8, Dem. 7:20). Both entries list this term back.
