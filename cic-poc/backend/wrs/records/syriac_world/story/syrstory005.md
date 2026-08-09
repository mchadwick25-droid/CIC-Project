---
id: syrstory005
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
title: The Martyrdom of Simeon bar Sabbae
narrative_tier:
  tier: 3
  justification: This is hagiographic martyrdom narrative by genre — consensus among Syriac scholars (Smith
    2014; Brock 2008; Van Rompay, GEDSH) is essentially unanimous on this point. The final redaction is
    dated to the early 5th century for the shorter Martyrdom text, and later still — well into the 5th
    century — for the longer History, meaning decades to over a century separate the narrative's composition
    from the events (persecution beginning c. 339–344) it describes; this alone places it at Tier 3, not
    Tier 1 or 2. The core claim — that Simeon was executed, and that this was tied to a fiscal dispute
    with the Sasanian state — is treated by modern scholarship (Smith 2016) as resting on genuine historical
    footing; the specific scene-by-scene narrative (the royal audiences, Gushtazad's specific words and
    actions, the exact circumstances of the beheading) follows hagiographic convention and is not to be
    taken as verified reporting. Smith's own scholarship further argues the narrative's framing of this
    as religious persecution specifically provoked by Constantine's conversion is itself a later, 5th-century
    East Syrian theological construction rather than a straightforward 4th-century reality — a scholarly
    point this document carries rather than smooths over.
text: Under Shapur II, amid war with Rome and suspicion that Christians favored the Roman side, a double
  poll-tax was laid on the Christians of Persia. Simeon, bishop of Seleucia-Ctesiphon, refused to collect
  it on the king's behalf. He was arrested and brought before the king at Karka d-Ledan. Among those brought
  with him was Gushtazad, a royal eunuch who had years before renounced his own faith under pressure;
  seeing Simeon stand firm, Gushtazad returned to the faith he had abandoned, and was put to death before
  Simeon's own eyes — the first to die, going ahead of the bishop he had once failed to imitate. Simeon
  himself was given more than one occasion to recant, to bow to the sun as the king demanded, and refused
  each time. He was beheaded, along with priests named Ḥananya and Abdhaykla, for holding to the confession
  he would not set down.
attested_occasion: 'The Persian martyr act (Smith''s edition): under Shapur II''s double poll-tax, Simeon
  bishop of Seleucia-Ctesiphon refuses to collect, is tried at Karka d-Ledan, sees the returned apostate
  Gushtazad die first, and is beheaded with the priests Hananya and Abdhaykla; the traditional 341 date
  is actively disputed (Kosinski/Burgess c. 344, Doc_02 SS11), and the narrative is hagiographic in genre
  (Tier 3).'
tellable_as: scene
owner_figure_id: syrfig004
voice_surface: 'We tell Simeon''s dying as the martyr-record keeps it - the tax refused, the eunuch who
  had once fallen going ahead of him, the confession held to the end. It is the community''s kept martyr
  memory, told in its own dress, and we say so. Usage guidance (chunk, verbatim): The Representative may
  offer this as the tradition''s own account of what a formed life looks like under the gravest pressure:
  "This is how we remember Simeon our bishop, and Gushtazad who returned to stand with him at the end."
  The Representative must not claim the specific narrated scenes — the exact words exchanged, the precise
  sequence of the royal audiences — as verified historical reporting; the formation ideal (faithful refusal
  under threat of death) is the evidence this story carries, not the narrated particulars.


  **Additional guidance:** This story should not be extended to imply that all six named Persian martyrs
  (Shahdost, Barba''shmin, Milles of Susa, Acepsimas, Mareas, Bicor) have comparably developed narratives
  available to this Representative — several exist only as named entries in the martyrological record,
  without verified narrative content available to this construction (see Absent Stories). Do not improvise
  comparable scenes for them by analogy to Simeon''s account.'
confidence_line: Contested (as an account of what faithful endurance under persecution looked like); Inferential/Thin
  (for the specific events narrated)
retrieval:
  tier: 3
  retrieve_when:
  - participant asks how this world remembers those who died under Shapur II's persecution
  - participant asks what it looked like to refuse the state under threat of death
  - conversation reaches C6 (Endurance Under State Persecution) directly.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant wants a contemporary, eyewitness account of the persecution (this narrative was
      composed decades to over a century after the events it describes — see Tier Justification)
  - condition_type: sense-disambiguation
    text: participant is asking about the twenty-year vacancy that followed Barba'shmin's death specifically
      (see the Absent Stories note — no comparable narrative exists for that silence).
  force_llm_vote: false
sources:
- source_id: srcSYR046
  locus: The Martyrdom and History of Blessed Simeon bar Ṣabbaʿe. Ed./trans. Kyle Smith, Persian Martyr
    Acts in Syriac, vol. 3 (Gorgias Press, 2014).
gravity_links:
- gravity_id: syrgrav006
  note: 'CO-P2-04: the chunk''s Formation Ecology Connection, verbatim (the S2.4 parking, converted at S2.5):
    This is the fullest account we have of endurance under state persecution as a formation ideal. It gives
    named, specific shape to what is elsewhere only a structure: a community that watched its own bishop die
    rather than break, and remembered a companion''s return to faith at the very moment of highest cost.
    Gushtazad''s turning back renders in story exactly what our vocabulary elsewhere describes abstractly -
    a return to undivided standing under the gravest pressure there is.'
---
Migrated at the S6.2/SYR S2.4-equivalent (2026-07-28) from `data/syriac_world/story_chunks/syrstory005_martyrdom-simeon-bar-sabbae.md` (mapping in `wrs/migrate/s62_syr_s24.py`; Story Text / Tier Justification / Usage Guidance / Confidence line verbatim; occasion/owner/frame authored per Desert-ALX S2.4 conventions).

[Formation Ecology Connection - parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] This is the fullest attested narrative account of C6 (Endurance Under State Persecution) as a formation ideal — it gives specific, named shape to what Doc_05 (Section 1.2) and Doc_08 (Force 2A-1) could only describe structurally: a community that watched its own bishop die rather than break, and remembered a companion's return to faith at the very moment of highest cost. Gushtazad's reconversion in particular renders, in narrative form, exactly the formation aim this world's own vocabulary elsewhere describes abstractly — a return to undivided standing under the gravest possible pressure.
