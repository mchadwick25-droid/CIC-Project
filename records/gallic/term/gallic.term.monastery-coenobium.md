---
id: gallic.term.monastery-coenobium
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: >-
    The word itself is the best-shared place-term in the lexicon (Sulpitius, Cassian, Salvian,
    Gennadius; both nodes). The coenobium / monastery distinction and the three kinds are single-voice
    (Cassian) and, by his own framing, Piamun's Egyptian teaching received. Two women's houses are
    attested (Tours, Marseilles) with no woman's voice from either. Lerins's internal layout is the
    least-documented house and is not described.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: 'Life of St. Martin ch. VI ("a monastery for himself at Milan"); ch. VII (Poitiers); ch. X (Marmoutier: "about two miles outside the city," "the solitude of a hermit," the narrow passage, "a cell constructed of wood," the caves); ch. XIII ("either churches or monasteries")'
  license: public-domain
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: 'Dialogues II.11 ("the nunnery of the young women")'
  license: public-domain
- source_id: gallic.source.cassian-institutes
  locus: 'Institutes Preface ("the brethren in your new monastery"; "at present without monasteries")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-iii
  locus: 'Conferences XVIII.4, 7, 10 (the three kinds; "their own masters"; "monastery is the title of the dwelling ... Coenobium describes the character of the life")'
  license: public-domain
- source_id: gallic.source.gennadius-de-viris-illustribus
  locus: 'ch. LXII ("founded two monasteries, that is to say one for men and one for women, which are still standing")'
  license: public-domain
- source_id: gallic.source.salvian-on-the-government-of-god
  locus: 'VIII.4 ("they in evil dens, these in monasteries"; "the monasteries of Egypt")'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - what a monastery was, or how a house was laid out or governed
  - whether there were women's houses
  - what "coenobium" means
  - participant uses "monastery," "abbey," "convent," "cloister," or "community"
  - Marmoutier's caves, Castor's new house, Gennadius's "two monasteries," or the coenobite-then-anchorite sequence
  do_not_retrieve_when:
  - who counts as a monk (retrieve monk / solitary)
  - the solitary's own dwelling (retrieve cell)
  - the received customs kept inside the house (retrieve the customs of the monasteries)
  - a Benedictine abbey, cloister, or later "convent"
relations:
- type: associated-with
  target: gallic.term.monk-solitary
- type: associated-with
  target: gallic.term.customs-of-the-monasteries
- type: associated-with
  target: gallic.term.monk-bishop
- type: associated-with
  target: gallic.term.anchorite-hermit
- type: associated-with
  target: gallic.term.cell
- type: associated-with
  target: gallic.term.elder-senior-abbot
- type: associated-with
  target: gallic.term.junior-novice
plain_meaning: >-
  A monastery, for us, is simply the place where monks dwell. Martin's wooden cell and the caves
  around it; a bishop's "new monastery" in a province without one; a house "for women" at Marseilles.
  Coenobium, the word Cassian brings from Egypt, names not the place but the kind of life kept in it.
  A congregation "governed by the direction of a single Elder."
world_word: monastery / coenobium
false_friend:
- an abbey or cloister - a walled precinct with a church, a written Rule, an abbot, enclosure, and a charter
- convent for the women's version
- an institution with a constitution
senses:
  informational: >-
    At Tours the word names wherever Martin stops - Milan, Poitiers, and then Marmoutier, "about two
    miles outside the city," shut in by precipice and river, "approached only by one, and that a very
    narrow passage," where he "possessed a cell constructed of wood" and the brethren hollowed caves
    from the rock; eighty disciples under one master, and a "nunnery of the young women" besides. At
    Marseilles the word opens a book written for a house that does not yet exist, and the book is
    careful to say the word guarantees nothing: "monastery is the title of the dwelling, and means
    nothing more than the place ... while Coenobium describes the character of the life and its
    system." Coenobites live "in a congregation and are governed by the direction of a single Elder";
    anchorites go out after training there; Sarabaites build "monasteries" too and remain "their own
    masters." Cassian's own two houses at Marseilles, "one for men and one for women," were still
    standing a lifetime later.
  evidential: >-
    The word is attested by Sulpitius (Life chs. VI, VII, X, XIII; Dialogues II.11), Cassian
    (Institutes Preface), Gennadius and Salvian; the coenobium distinction by Cassian alone
    (Conferences XVIII.4-10), framed as Piamun's. The Latin monasterium is supplied by the editor's
    footnote at Dial. II.11. Nothing lets anyone hear the inside of either women's house, and Lerins's
    layout is undocumented.
  personal: >-
    What we measure a house by is not the building but whether one elder governs a congregation in it.
    Marmoutier is a place and a person before it is a program; the churches come to it for their
    priests. And when Martin pulled down a temple, there he built either a church or a monastery.
  translational: >-
    'You mean an abbey - walls, a church, an abbot, a Rule?' - no: for us "monastery" meant nothing
    more than "the habitation of monks," a wooden hut and hollowed caves or a bishop's new foundation,
    and since even the false monks had "monasteries," the south reached for coenobium - one elder over
    a congregation - when it wanted to say what mattered.
quick_meaning: >-
  Simply where monks dwell - a wooden cell and caves, or a bishop's new house. The coenobium is the
  life kept there: one Elder over a congregation.
distortion_risk: medium
---
Built from Doc_06 entry 014 (Tier 2; chunk galliclex014_monastery-coenobium.md; Doc_03 1.2). Register
emic. Quotations verified at locus by the build's own Doc_06 pass; not re-read here. Canon cells left
empty: the term describes the house, not any canon question's substance.

Related-Terms also names Sarabaite (069), brethren (070), virgin / virginity (064) and Gaul (068) -
all batch 2; relations deferred, to be added once those term records exist.
