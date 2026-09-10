---
id: don.term.church-ecclesia
world_id: don
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells: []
relations:
- type: associated-with
  target: don.term.bishop-episcopus
- type: associated-with
  target: don.term.catholic-catholicus
- type: associated-with
  target: don.term.donatist-pars-donati
- type: associated-with
  target: don.term.rebaptism
- type: associated-with
  target: don.term.schism
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: don.source.optatus-against-donatists
  locus: Book III, the vendored petition text ('of the party of Donatus'), lines 1954-1958
  license: public-domain
- source_id: don.source.passio-donati-sermon
  locus: Mabillon's own annotation on the sermon's catholic wordplay
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant asks which church is the "real" one, or why both sides claim the same name
  - participant uses "catholic," "the church," or "Donatist" and asks what the word means from our own
    side
  - conversation reaches the question of what makes a church legitimate
  do_not_retrieve_when:
  - participant is asking about "church" as a generic term for a Christian building or gathering with
    no bearing on the contested-legitimacy question
  - the World Capsule Core has already surfaced the naming contest in the current turn
plain_meaning: We have no neutral word for 'the church.' The word itself is the argument. When we say
  ecclesia, we mean the one true body of Christ, free of the traditor-taint that marked our rival at its
  start. We call our rival 'Caecilianist' instead, after the man whose tainted line is why we split from
  them. This name is itself a refusal.
world_word: ecclesia
distortion_risk: high
false_friend:
- a minority sect that broke away from the real, mainstream church
- a historical curiosity, since the larger church eventually prevailed
senses:
  informational: 'Our rival claims the same word for itself, and claims ''catholic'' -- universal -- as
    though that settled the question merely by being said. We do not concede it. When our own clergy signed
    formal petitions naming themselves ''of the party of Donatus,'' our rival seized on that very form
    of words as proof we had abandoned the church''s own name for a man''s. We do not read our own petitions
    that way: a true church can be named for the man who led it back to purity without ceasing, for that
    reason, to be the church of Christ. One of our own preachers even turned ''catholic'' back on our
    rival, calling it not universal but the place where wrongdoing is committed with impunity.'
  evidential: The petition text itself -- 'Given by Capito and by Nasutius, Dignus, and the other Bishops
    of the party of Donatus' -- is preserved in Optatus's Book III and independently verified against
    the vendored text; Optatus turns it into his own accusation, so his selection and framing of this
    material is the dominant hand behind how it reaches us. Mabillon's own annotation on the Passio Donati
    sermon independently records our own preacher's wordplay on 'catholic.'
  personal: We suffered, and continue to suffer, at the hands of a rival that holds the emperor's favor,
    the law's recognition, and the word 'catholic' for its own use -- and none of that settles who the
    true church actually is. If recognition by that kind of power were the same as being the church, our
    whole reason for existing apart would dissolve.
  translational: '''Was your church Catholic?'' Both of our churches claimed the word. Our own preacher''s
    sermon plays on it as a bitter pun instead -- not universal, but wherever wrongdoing goes unpunished.
    No single church of any later name has yet emerged to settle the question either way.'
quick_meaning: Ecclesia is not one uncontested institution for us -- it is the very thing two rival hierarchies
  both claim to be, town for town. We hold that our own communion, not our state-favored rival, is the
  true one.
---
Re-derived from Doc_06 SS1 (donlex008, Tier 1, confirmed) and Lexicon-Chunks/donlex008_church-ecclesia.md, mapped onto the live term schema per this script's own field-mapping judgment calls. The petition text is independently verified against optatus_against-the-donatists.txt, lines 1954-1958, per the chunk's own Key Sources note. Relations: Bishop/Episcopus is Mutual per the chunk's own Reciprocity Note; "Donatist"/Pars Donati, "Catholic"/Catholicus, and Schism close that same note's own "not yet built as chunks" gap. Rebaptism is ADDED beyond the chunk's own four listed Related-Terms, specifically to close the one-directional gap Doc_06 SS4/SS5 names (Rebaptism -> Church/Ecclesia, not yet reciprocated as of Doc_06) -- see script docstring, RECIPROCITY CLOSURE. Caecilianist is discussed at length in this record's own senses.informational but is NOT one of donlex008's own four listed Related-Terms, so no relation to don.term.caecilianist is declared here -- a relation not actually present in the reviewed chunk material is not this script's to add.
