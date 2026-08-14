---
id: ijclex001
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
term: primatus (sedes apostolica)
aliases:
- primacy
- apostolic see
- apostolic primacy
- Roman primacy
- Petrine primacy
quick_meaning: 'The standing Rome holds because Peter held it here first. It is not an honour Rome asks for. It is an inheritance Rome guards, and defends when it must.'
world_meaning: 'We do not say Rome is first because Rome is large, or because Rome was once the empire''s
  own capital — that claim, on its own, belongs to another see now, and we have watched it made. We say
  Rome is first because Peter died here, and what was given to Peter was given to the one who holds his
  seat after him. This is not a title we invented when we needed one. Julius wrote to the Eusebian party
  a generation before Damasus ever took up his own stylus, and Julius already wrote as a man whose see
  had the standing to review what Alexandria had done — that standing did not begin with him either.


  What this means in practice is that a claim is not settled merely because a council votes on it, or
  because an emperor is present when the vote is taken. A claim is settled when it is received *here*,
  at this see, and confirmed as consonant with what the apostle himself once held and taught. Leo did
  not travel to Chalcedon. He did not need to. His Tome went ahead of him, and the bishops gathered there
  did not receive it as one opinion among many to be weighed against the others — they received it, when
  they received it rightly, as the voice of Peter speaking again through the one who now sits in his place.
  When they did not receive it rightly — when they reached instead for a see''s rank grounded in nothing
  but a city''s nearness to an emperor''s palace — we did not accept that as the same kind of claim at
  all, and we said so, in writing, afterward, even though the vote had already been taken.


  This is why we build in stone as much as in decretal. A pilgrim who walks to a martyr''s grave and reads
  the verses cut there is not being shown decoration. He is being shown that this see''s own memory of
  its dead reaches back to the apostles themselves, unbroken, and that the same hand that guards that
  memory is the hand that now guards the faith.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: *Primatus* is what *communio* protects and what *Tomus* asserts
  — a participant who understands this term also understands why being cut off from Rome specifically,
  and not merely from any bishop, carries the particular weight it does in this world''s own record, and
  why a document issued from this specific see (a Tome) carries an authority its own content alone would
  not fully explain.'
distortion_risk: This world's own actors do not experience these as two separable things needing to be
  reconciled or unmasked. A claim to apostolic inheritance and a claim to binding institutional authority
  are, for Damasus and Leo alike, the same claim — the spiritual warrant *is* the juridical warrant, not
  a cover story for it.
retrieval:
  tier: 1
  retrieve_when:
  - participant asks about the bishop of Rome's own authority or why Rome claims special standing
  - participant uses "primacy," "pope," or "papal authority" in connection with this world
  - conversation reaches Damasus, Leo, or the Petrine texts
  - participant asks why one see would outrank another.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: the participant's question is actually about Constantinople's own claim (retrieve presbeia instead)
  - condition_type: sense-disambiguation
    text: the World Capsule Core has already given the primary answer this turn and the participant has
      not asked a follow-up.
  force_llm_vote: false
sources:
- source_id: srcIJC04
  author_gravity_note: Julius I's letter to the Eusebian party (341), preserved in Athanasius's own quotation
    of it — the earliest attested instance of this claim in this world's own record.
- source_id: srcIJC12
  author_gravity_note: Leo I's Tome to Flavian and his letters rejecting Canon 28.
- source_id: srcIJC14
  author_gravity_note: Damasus's own epigraphic corpus, material rather than textual evidence of the same
    claim's public self-presentation. **Note:** much of the decretal material transmitted under Damasus's
    own name specifically is of contested authenticity (Doc_02 §2; Source Registry row 15) — this chunk's
    Key Sources rely on the epigraphic corpus and on Julius's and Leo's own more securely attested material,
    not on the contested decretal block.
modern_hearing: A modern participant is likely to hear "primacy" as either a purely religious claim (a
  matter of spiritual seniority, like a monastery's abbot) or, cynically, as a naked power grab dressed
  in religious language — assuming the two registers (spiritual standing, institutional power) must be
  separable, with the religious language covering for the real, political motive.
semantic_domain: juridical ecclesiology - see-rank and succession
modern_sense: '''Papal primacy'' as a settled doctrine with defined content, or cynically as institutional
  power-grab dressed in religion (chunk Modern Hearing: the two registers assumed separable).'
period_sense: The standing Rome holds because Peter held it first - an inheritance guarded and defended,
  where the spiritual warrant IS the juridical warrant (Damasus and Leo alike); settled-when-received-at-this-see,
  not settled-when-voted.
prior_sense: Latin primatus - 'first place, pre-eminence' generally, a civic-rank word before its ecclesial
  narrowing; a builder note, UNVERIFIED against this build's own docs.
grounding_criterion: high
conceptual_distance_note: 'GROUNDING (the enum''s free-text companion, carried here): Julius''s 341 letter
  (the claim''s earliest attested instance), Leo''s Tome and Canon-28 rejections, Damasus''s epigraphic
  corpus - the contested decretal block excluded per the chunk''s own Author-Gravity note (Registry row
  15). | DISTANCE: Near-false-friend with the modern ''papacy'': the claim is real and in-window, its
  later settled form is not - the CT contest rides pahc-style ending-not-read-back discipline.'
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  verification_date: '2026-07-31'
  evidentiary_weight: load-bearing
  formation_confidence: Contested
voice_surface: 'STRAND A''S OWN VOICE (the Plural-Voices device - a lexicon-organization fact, never a
  Representative identity decision): ''primatus names the standing Rome holds because Peter himself held
  it first here - not an honor Rome asks for, but an inheritance Rome guards and, where it must, defends.''
  The rival claim speaks in presbeia''s own entry, not flattened into agreement here.'
field_relations:
- type: tension-with
  target_id: ijclex002
  note: 'Chunk Ecological Function (verbatim, absorbed per FLAG-002): *Primatus* is what *communio* protects
    and what *Tomus* asserts — a participant who understands this term also understands why being cut
    off from Rome specifically, and not merely from any bishop, carries the particular weight it does
    in this world''s own record, and why a document issued from this specific see (a Tome) carries an
    authority its own content alone would not fully explain. The A/B strand contest itself: rank by apostolic
    inheritance vs rank by imperial proximity; symmetric both ways.'
- type: associated-with
  target_id: ijclex004
  note: Communio is what protects primatus (the EF's own phrase) - the juridical instrument behind the
    claim; symmetric.
- type: presupposed-by
  target_id: ijclex009
  note: A Tome's authority presupposes this see's standing - 'primatus made into a document'; inverse
    pair with ijclex009's presupposes.
- type: associated-with
  target_id: ijclex006
  note: The doctrinal content the see's instruments defend (the Tome carries the homoousian settlement);
    symmetric.
- type: tension-with
  target_id: ijclex007
  note: 'The letter vs the council: ''a claim is settled when received at this see, not when a council
    votes'' - the world''s own story-title tension (The Letter That Outranked a Council); symmetric.'
- type: tension-with
  target_id: ijclex010
  note: New Rome's premise vs old Rome's inheritance - the rank contest's geographic ground; symmetric.
- type: associated-with
  target_id: ijclex012
  note: The martyr cult as this see's own standing made visible in stone (Damasus's project); symmetric.
contested_claim_ids:
- ijcclaim001
chunk_slug: primatus
chunk_related_line: communio, presbeia, Tomus, homoousios, concilium, Nea Rhōmē, martyrium
---
Migrated at the S6.2/IJC S2.2-equivalent (2026-07-31) from `data/imperial_juridical_world/lexicon_chunks/ijclex001_primatus.md` (mechanical split; mapping and alias authoring tables in `wrs/migrate/s62_ijc_s22.py` - the FLAG-035 corrections and the one Rule-A birth drop declared there; the third world born matching the runtime key space AND the gate). Related-Terms and authored fields arrive at S2.3.

[Plural-Voices Note - parked at the S2.2-equivalent; typed home per the splitter docstring] This entry is written from Strand A's own voice specifically (Rome's own self-understanding) — per Doc_01's three-strand finding, this world does not have one unified "we"; Strand B's rival claim to this same question is rendered from its own voice in the *presbeia* entry, not flattened into agreement here. **This is a lexicon-organization device for construction and runtime-retrieval purposes only — it is not, and does not pre-decide, a Representative voice or identity decision.** Which strand (if any) an eventual Representative speaks primarily from, and how a Representative would handle a participant's question that spans two contested strands, is Step 10's own decision, not settled by this document (see Doc_06 §5, Open Item 4).

[CT Contest Type - parked at the S2.2-equivalent; typed home per the splitter docstring] **Relationship to present-day traditions:** the historical content of this world's own primacy claim, and its relationship to the present-day papacy's own claimed authority, is a live point of contest between traditions that regard this world's own record as the origin of a divinely-instituted office and traditions that regard it as a historically contingent institutional development. This chunk does not resolve that contest.

[Final Assembly Instruction - parked at the S2.2-equivalent; typed home per the splitter docstring] Completed per `L4-Templates/Deployment_Lexicon_Chunk_Template.md` V1.0. No brackets or builder notes remain; CT Contest Type completed per Doc_06 §3.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 3 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
