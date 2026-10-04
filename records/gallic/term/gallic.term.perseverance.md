---
id: gallic.term.perseverance
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F1-I
- F1-T
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Cross-voice. Cassian's monastic usage (the novice's perseverance at the door, Inst. IV.3; the
    third stage of the Divine gift, Conf. XIII.18) and Augustine's report of what the Gallic
    brethren objected to (Persev. ch. 10, quoting Hilary's letter - Letters 225-226 themselves are
    unvendored) do not speak in unison. The ordinary northern sense (Vita XXVI, Martin's
    "perseverance and self-mastery") is unrelated to the argument. The Latin perseverantia is
    corpus-supported only in Roberts's editorial footnote on the Doubtful Letters. Faustus's De
    gratia is unread beyond grep. "Perseverance of the saints" is a modern-hearing gap, carried as
    distortion risk, not as a recorded live contest (Doc_06 section 3; no CT tag).
sources:
- source_id: gallic.source.cassian-institutes
  locus: 'Institutes IV.3 ("an evidence of his perseverance and desire"); IV.36 ("not he who begins these things, but he who endures in them to the end, shall be saved")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-ii
  locus: 'Conferences XIII.17 ("grants both the commencement of a good work and perseverance in it"); XIII.18 (the three stages of the Divine gift); XIV.5 ("On perseverance in the line that has been chosen")'
  license: public-domain
- source_id: gallic.source.augustine-on-the-gift-of-perseverance
  locus: 'ch. 1; ch. 10 ("these brethren will not have this perseverance so preached as that it cannot be obtained by prayer or lost by obstinacy") - context only'
  license: public-domain
- source_id: gallic.source.augustine-on-rebuke-and-grace
  locus: 'Argument (Warfield''s editorial summary) - context only'
  license: public-domain
- source_id: gallic.source.sulpitius-vita-martini
  locus: 'ch. XXVI ("his perseverance and self-mastery in abstinence and fastings") - the ordinary sense, Tours'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - whether a monk could be sure of holding on to the end
  - whether perseverance was a gift or an achievement
  - what the "third stage" of the Divine gift is
  - what the Gallic brethren objected to in Augustine's preaching of perseverance
  - participant uses "perseverance," "endurance," "holding on," "falling away," "eternal security," "perseverance of the saints"
  - the ten days at the door; "he who endures to the end"; Conf. XIII.18's three stages; Hilary's letter as Augustine quotes it
  prefer_instead:
  - the question is about the first stage of grace (retrieve beginning of a good will)
  - the question is about the cooling that is perseverance's failure (retrieve lukewarmness)
  - the Reformed doctrine of "the perseverance of the saints" as such - a modern-hearing gap, not our vocabulary
  - any attempt to source it from Salvian
relations:
- type: associated-with
  target: gallic.term.conversion
- type: associated-with
  target: gallic.term.free-will
- type: associated-with
  target: gallic.term.grace
- type: associated-with
  target: gallic.term.lukewarmness
- type: associated-with
  target: gallic.term.junior-novice
- type: associated-with
  target: gallic.term.profession
- type: associated-with
  target: gallic.term.humility
- type: associated-with
  target: gallic.term.monk-solitary
- type: presupposes
  target: gallic.term.beginning-of-a-good-will
- type: associated-with
  target: gallic.term.predestination
- type: associated-with
  target: gallic.term.co-operation
- type: associated-with
  target: gallic.term.massilians
plain_meaning: >-
  Holding on to the end - both the endurance a newcomer proves at the door and God's gift of
  keeping us in the good we have begun.
world_word: perseverance
false_friend:
- '"the perseverance of the saints" - a later Reformed doctrine of eternal security'
- perseverance as sheer willpower
- the Gallic objection as a denial that perseverance is a gift
senses:
  informational: >-
    In our houses perseverance is the first thing tested and the last thing required. The newcomer
    waits outside the doors ten days or longer to give "an evidence of his perseverance and desire";
    the charge given when he is received warns that "not he who begins these things, but he who
    endures in them to the end, shall be saved." Then Chaeremon sets it inside the teaching on
    grace: the first stage of the Divine gift is to be inflamed with desire for the good, the second
    is to be able to perform it, and the third "also belongs to the gifts of God, so that it may be
    held by the persistence of the goodness already acquired, and in such a way that the liberty may
    not be surrendered." A gift, and the monk's own holding, with the will kept free.
  evidential: >-
    Directly attested in Cassian (Inst. IV.3, IV.36; Conf. XIII.17-18, XIV.5), received from
    Egypt. What our brethren of Marseilles refused is known through Augustine's quotation of
    Hilary's letter - "these brethren will not have this perseverance so preached as that it cannot
    be obtained by prayer or lost by obstinacy" - which is context only; Hilary's own letter is
    unvendored. At Tours the word is ordinary praise of Martin's fasting and has nothing to do with
    the argument.
  personal: >-
    We learned the word at the door before we ever heard it argued. A gift we pray for, and a thing
    we must not let go - the same word in one sentence. What we would not have was a preaching of
    the gift that made prayer and effort pointless.
  translational: >-
    A modern hearer may reach for "eternal security" or "once saved, always saved" - or its
    opposite. Neither is ours. For us perseverance is God's gift and our holding at once,
    something we can pray for and can lose by obstinacy; the later confessional label
    "perseverance of the saints" is not our vocabulary.
quick_meaning: >-
  Holding on to the end. The endurance a newcomer proves at our door, and the third stage of
  God's gift - a gift that can still be lost by giving up.
distortion_risk: high
use_note:
  means: "Perseverance meant holding on to the end, both the endurance a newcomer proves at the door and, in the grace argument, God's gift of keeping us in the good begun."
  not_for:
    - "the later Reformed perseverance of the saints as eternal security"
    - "perseverance as sheer willpower"
    - "the first stage of grace, which sits in gallic.term.beginning-of-a-good-will"
    - "the cooling that is its failure, which sits in gallic.term.lukewarmness"
  years: {from: 397, to: 429}
  status: provisional
---
Built from Doc_06 entry 043 (`galliclex043_perseverance.md`, Tier 2, tags SC TC DR; Doc_03 5.4).
CT tag not applied per Doc_06 section 3 (the "perseverance of the saints" gap is a distortion
risk, not a recorded contest) - carried here as false_friend and distortion_risk: high rather than
as a Contested formation_confidence.

Relation typing: perseverance is the third stage against the beginning of a good will as the
first, so this record `presupposes` gallic.term.beginning-of-a-good-will (the chunk's own
"the end of the grace argument as 042 is its start").

Related-Terms also names grace (of God), free will, lukewarmness, junior / novice, profession,
humility, and monk / solitary - cross-batch at authoring time, added as relations (typed
associated-with) at the reconciliation pass once all 81 term records existed.
