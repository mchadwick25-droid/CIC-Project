---
id: don.term.pars-donati
world_id: donatism
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-T
- F3-E
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: The petition wording itself is verified directly (Optatus Book III, `optatus_against-the-donatists.txt`
    lines 1954-1958). Two things are not settled and are carried as such. First, the wording survives only because
    Optatus quoted it in order to attack it, so what a formal legal self-designation meant to its own signers
    has to be read through a frame built to make it look like a confession. Second, Doc_03 SS6 and Doc_05 SS6.1
    both leave open an unfinished check -- whether Augustine uses 'Donatist' of them, or 'the party of Donatus',
    or something else, and in which contexts -- which would strengthen or complicate the plural-voices framing
    here. It has still not been done, and this record does not pretend otherwise.
sources:
- source_id: don.source.optatus-against-the-donatists
  locus: Book III -- 'Given by Capito and by Nasutius, Dignus, and the other Bishops of the party of Donatus'
  license: public-domain
- source_id: don.source.augustine-psalmus-contra-partem-donati
  locus: the rival's own naming of the group in a popular song
  license: public-domain
- source_id: don.source.monceaux-histoire-litteraire-tome5
  locus: the literary history of the earliest Donatist writers
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - a participant asks what this group called itself, or whether 'Donatist' is its own name
  - a participant asks about Donatus himself and what naming a church after a man meant
  - the conversation reaches the naming contest between the two African hierarchies
  prefer_instead:
  - '''Donatist'' is being used as a neutral historical shorthand and the naming question is not in play'
relations:
- type: associated-with
  target: don.term.ecclesia
- type: associated-with
  target: don.term.caecilianist
plain_meaning: Our clergy signed a formal petition as bishops 'of the party of Donatus'. Our rival seized on that
  and said we had named a man instead of Christ's church. We do not read our own petition that way. A church may
  be named for the man who led it back to purity.
world_word: pars Donati
false_friend:
- '''Donatist'' as a neutral scholarly label with no side taken'
- a personality cult built around a founder, in the modern sectarian sense
- a settled self-description -- the preferred self-naming appears to have run the other way
senses:
  informational: 'Optatus preserves Donatist bishops signing a formal petition to Constantine as ''of the party
    of Donatus'', and turns that phrase into an accusation: that they acknowledged belonging not to the Church
    of Christ but to a man''s faction. The phrase is a legal self-designation in a document addressed to an emperor,
    which is not the same thing as the name a community uses of itself in worship -- and Optatus''s own eagerness
    to make the point implies the ordinary self-description ran the other way.'
  evidential: 'Documented as text and checked directly; genuinely plural in voice, which is why Doc_03 tags it
    [PV]. What is thin is the other side of the pair: no vendored source gives this communion''s own everyday
    self-naming in its own words. Augustine''s usage, named twice in the construction record, has not
    been checked.'
  personal: The name a movement is remembered by was given to it by the people who defeated it. That is not an
    incidental irony here; it is the same asymmetry that governs almost everything else that survives.
  translational: '''Didn''t they call themselves Donatists?'' -- in a legal petition, in a sense, once. Whether
    that was how they named themselves among themselves is a question the surviving record cannot answer, because
    the only voice that preserved the phrase preserved it as an accusation.'
quick_meaning: The party of Donatus -- the phrase our rival turned into a charge against us.
distortion_risk: medium
use_note:
  means: "Donatist bishops signed a petition 'of the party of Donatus'; Optatus read it as naming a man instead of Christ's church, which Donatists did not accept."
  not_for:
    - "a claim that Donatist is a neutral scholarly label with no side taken"
    - "a claim that it was a founder-centred personality cult in the modern sectarian sense"
    - "a claim that it was the settled self-description, when the preferred self-naming appears to have run the other way"
  years: {from: 311, to: 439}
  status: reviewed
---
Built from Doc_06 SS1 entry 005 (Tier 2, no promotion forwarded; naming-contest content carried at Doc_05 SS6.1). No deployment chunk built this cycle. Whether Augustine's own usage differs (Doc_03 SS6) is unchecked; divergence_note holds that point.
