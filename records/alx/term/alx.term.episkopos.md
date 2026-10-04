---
id: alx.term.episkopos
world_id: alexandria-catechetical
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-I
- F3-T
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
- source_id: alx.source.athanasius-festal-letters
  locus: "(annual formation calendar)"
  license: public-domain
- source_id: alx.source.athanasius-de-decretis
  locus: 19-20
  license: public-domain
- source_id: alx.source.clement-stromateis
  locus: VI.13
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - what a bishop's role is, or what grounds episcopal authority here
  - Athanasius as a formation figure, or the bishop's relationship to the Eucharist
  prefer_instead:
  - asking primarily about the teacher's formation function (retrieve alx.term.didaskalos)
  - asking about the Eucharist's own formation function rather than who presides at it
relations:
- type: associated-with
  target: alx.quote.the-grades-here-in-the-church
- type: tension-with
  target: alx.term.didaskalos
- type: associated-with
  target: alx.term.ekklesia
plain_meaning: Not a church manager. The bishop governs how the community is formed and guards what it received.
world_word: episkopos (overseer)
false_friend:
- a diocesan executive who manages clergy and finances
- the teacher's organizational superior
senses:
  informational: Episkopos means overseer, but what is overseen is formation, not budgets or buildings.
    The bishop guards what the community received, presides at the Eucharist, and governs the community's
    formation life across the year.
  evidential: Athanasius's Festal Letters show a bishop setting the whole Egyptian church's annual
    formation rhythm; his De Decretis shows the same office guarding the Nicene confession against the
    Arian alternative; Clement treats the bishop as a human participant in the community's divine
    governance.
  personal: 'Clement''s Alexandrian voice grounds the office in the life, not the title: one is "not
    regarded righteous because a presbyter, but enrolled in the presbyterate because righteous" - the
    office does not confer the standing on its own; the person''s own righteousness is what the office
    recognizes.'
  translational: >-
    Isn't a bishop just a church administrator, the executive of a diocese? This world located the
    office somewhere else - the governor of the community's formation life, not a manager of an
    institution.
quick_meaning: Not an administrator. The bishop governs formation, not budgets.
distortion_risk: high
use_note:
  means: "The bishop as governor of the community's formation and guardian of what it received, not a manager of clergy and finances."
  not_for:
    - "describing the bishop as a diocesan executive"
    - "presenting the bishop as the teacher's organizational superior"
    - "projecting Athanasius's fourth-century episcopal role back onto Clement's time"
  years: {from: 190, to: 373}
  status: provisional
---
Imported from the old system's richer lexicon (alexlex030, "Bishop / Episkopos") at Mark's direction,
as a draft, not a final version. The old record's citation of Ignatius of Antioch's Letters is omitted
here since no corresponding source record exists yet in the new registry.

The personal sense matches what Stromateis VI.13 argues: "Such an one is
in reality a presbyter of the Church... not as being ordained by men, nor
regarded righteous because a presbyter, but enrolled in the presbyterate
because righteous" (anf02, Book VI ch. XIII, lines 47856-47867) - the
office is grounded IN the person's own righteousness, not in something
that outlasts it. The associated evidential claim about "the grades here
in the Church" matches alx.quote.the-grades-here-in-the-church.
