---
id: don.term.episcopus
world_id: donatism
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-I
- F1-E
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: 'The bare institutional fact of a complete parallel hierarchy is undisputed even by the hostile
    sources reporting it (Doc_04 SS5, G4''s Cross-Voice pass). What remains hostile-mediated is everything beyond
    that bare fact -- individual bishops'' conduct and motives reach this record through Optatus''s and Augustine''s
    characterisation (Doc_02 SS2). The 411 Conference seated
    279 Donatist bishops against 286 Catholic (Doc_01 SS2, Doc_04 SS3.4); the deployment chunk `donlex015_bishop-episcopus.md` still says 284 in its own World Meaning
    and Distortion Risk sections while its Key Sources note states 279, and this record follows the
    279 figure.'
sources:
- source_id: don.source.gesta-collationis-carthaginiensis-411
  locus: the 411 Conference -- 279 Donatist against 286 Catholic bishops seated
  license: public-domain
- source_id: don.source.augustine-on-baptism-against-the-donatists
  locus: "I.1.2 and I.5.7 - the Maximianist condemnation and the reception of Felicianus without repetition; the edition's note on I.1.2 names the 393 synod at Cebarsussi and the 394 council of Bagai, and I.5.7 and II.12 quote the council's own words ('sacrilegiously' baptized in schism; 'the truthful voice of a plenary Council'). The shipwreck sentence is not quoted in On Baptism"
  license: public-domain
- source_id: don.source.augustine-answer-to-petilian
  locus: "the Bagai decree quoted word for word, then Optatus Gildonianus advancing with a military force to bring Felicianus and Praetextatus back (Answer to the Letters of Petilian I.10, section 11; cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml lines 15508-15513; a shorter rendering at II.7, line 15875)"
  license: public-domain
- source_id: don.source.optatus-against-the-donatists
  locus: the rival consecration of Majorinus and the doubling of the see of Carthage
  license: public-domain
- source_id: don.source.numidian-basilica-archaeology
  locus: the physical footprint of a doubled church order in Numidia
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - a participant asks how these churches were organised, or why one city had two bishops
  - a participant asks about a specific council, the Maximianist affair, or the 411 Conference
  - the conversation reaches who holds legitimate church office
  prefer_instead:
  - the office of bishop is being asked about generically, with no bearing on the rival-hierarchy situation
relations:
- type: presupposes
  target: don.term.ecclesia
- type: associated-with
  target: don.term.traditor-traditio
- type: associated-with
  target: don.term.primas
- type: precondition-for
  target: don.term.concilium
plain_meaning: Where our rival has a bishop, so do we. Two men claim one office over one city. It is a whole church
  order, see for see, across Roman North Africa. At the great Conference at Carthage, 279 of our bishops sat facing
  286 of theirs.
world_word: episcopus
false_friend:
- a loose protest movement or a breakaway current without real institutional structure
- '''the'' bishop of a city as a single settled fact that nobody contests'
- a rival claimant who is understood by all sides to be irregular or provisional
senses:
  informational: 'Not one office per see but two, from Carthage down to the smallest town. The see of Carthage
    was held across the window by Donatus, Parmenian and Primian against the rival Caecilianist line; Cirta was
    Petilian''s. Government ran through councils, and it was precisely because that machinery was real that the
    sharpest internal crisis was possible: Cebarsussi (393) elected Maximian a rival primate, and the much larger
    council at Bagai (394) condemned him and later received his clergy back without repeating ordination or baptism.'
  evidential: 'Documented at the institutional level and cross-voice attested: hostile sources report the parallel
    hierarchy without disputing that it existed, and the 411 Conference''s own acts record the seated counts precisely.
    Beyond that bare fact the record thins fast -- what individual bishops were like, how they were chosen, what
    a small-town episcopate felt like from inside, survives mainly as Optatus''s and Augustine''s characterisation
    of opponents.'
  personal: To hold this office is to hold a real, functioning charge that the state itself refuses to recognise
    as one. Buildings were confiscated, clergy exiled, unity enforced by troops. Every see is held under continuing
    legal jeopardy, and that is simply the ordinary condition of the office.
  translational: '''Wasn''t this a fringe movement with a few self-appointed leaders?'' -- 279 bishops facing
    286 in one room is not a fringe. It is one whole church answering another whole church, with its own primate,
    its own councils, and its own discipline for its own dissidents. The parallel is total, which is why there
    was no neutral ground from which to ask who was right.'
quick_meaning: Two bishops for one city. A whole rival church order, see for see.
distortion_risk: high
use_note:
  means: "Donatists had a bishop wherever their rival did, see for see across North Africa; at the 411 Conference 279 of theirs faced 286."
  not_for:
    - "a claim that the Donatists were a loose protest movement without institutional structure"
    - "a claim that there was a single settled bishop of a city whom nobody contested"
    - "a claim that the rival claimant was understood by all sides to be irregular or provisional"
    - "a claim about the rival hierarchy as a supporting pattern of this world, which sits in don.gravity.parallel-hierarchy"
  years: {from: 311, to: 439}
  status: reviewed
---
Built from Doc_06 SS1 entry 015 (Tier 1, confirmed at Doc_04 SS7) and `Lexicon-Chunks/donlex015_bishop-episcopus.md`. NOTE: the chunk's World Meaning and Distortion Risk sections still carry the superseded 284 figure for Donatist bishops seated at the 411 Conference while its own Key Sources note records the correction to 279 (Doc_01 SS2, Doc_04 SS3.4, Doc_05 SS1). This record uses 279 and flags the chunk-internal inconsistency for a deployment-layer fix.
