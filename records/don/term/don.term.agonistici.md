---
id: don.term.agonistici
world_id: don
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells: []
relations:
- type: associated-with
  target: don.term.persecution
- type: associated-with
  target: don.term.refusal-of-imperial-legitimacy
confidence:
  citation_specificity: B
  verification_state: verified-direct
  evidentiary_weight: contested
  formation_confidence: Dominant Modern Reconstruction
  divergence_note: Existence is Documented (Codex Theodosianus 16.5.52, directly verified this build).
    The self-designation term itself reaches this record only through Augustine's own report -- the law's
    own text never uses the word agonistici. Character, scale, and typical conduct are the live CT contest
    (Frend vs. Shaw); Doc_04 SS4 rates this component 'DMR at best... the sharpest divergence in this
    document, across three tiers' (Doc_06 SS3, quoted directly, not re-judged).
sources:
- source_id: don.source.codex-theodosianus-book-16
  locus: law XVI.5.52 (412), 'circumcelliones argenti pondo decem,' confirmed verbatim
  license: public-domain
- source_id: don.source.augustine-answer-to-letters-of-petilian
  locus: Augustine's own report of the group's self-designation, agonistici, within his wider anti-Donatist
    corpus
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant uses "Circumcellion" or "agonistici," or asks about our own rural, itinerant members and
    their reputation for violence
  - participant asks whether the hostile portrait of this group is accurate
  - conversation reaches Numidia specifically or the group's own relationship to the wider hierarchy
  do_not_retrieve_when:
  - participant is asking about ordinary Numidian believers generally without reference to this specific,
    contested group
  - the World Capsule Core has already surfaced the D-A regional scope-qualification in the current turn
plain_meaning: In the Numidian countryside, some of us call ourselves agonistici -- strivers, those who
  fight for the truth. Our opponents call us Circumcellions instead -- those who linger at the martyrs'
  shrines -- and say that lingering turns to violence. We do not pretend this reputation came from nowhere;
  the empire has named us in its own law. But we do not accept our opponents' account of us, or how typical
  that violence was, as the last word.
world_word: agonistici
distortion_risk: high
false_friend:
- '"Circumcellion," taken as our own accepted self-description rather than an outsider''s label'
- a violent fringe faction whose reputation can be taken at face value from hostile sources alone
senses:
  informational: 'What is certain is this: we exist, as a recognized body, concentrated in Numidia''s
    countryside specifically -- not invented by hostile pens out of nothing. What is far less certain
    is how much of the character our opponents give us is true to the whole of us, and how much is the
    picture a hostile hand naturally paints of country people it already despises. In Numidia specifically,
    our strength runs deep -- for many there, belonging to us was simply belonging to the ordinary church
    of one''s own village. What is contested is narrower: whether the vivid, often violent character our
    opponents attribute to us describes that whole regional strength, or only ever described a smaller,
    more provocative element the hostile record chose to make stand for the rest.'
  evidential: 'Our bare existence is Documented independently of any hostile literary characterization:
    the Codex Theodosianus, law 16.5.52 (412), names us by imperial legislation, directly confirmed to
    read ''circumcelliones argenti pondo decem.'' Augustine''s own report is our only access to the self-designation
    term agonistici itself -- the law''s own text never uses that word. Our reported character, scale,
    and typical conduct beyond bare existence carry HIGH Author-Gravity risk, reaching this record substantially
    through Optatus''s and Augustine''s own hostile framing.'
  personal: We are not the whole of Numidia, and not the whole of this church. What we were actually like,
    on any given day, in any given place, is a harder question than either our opponents or, honestly,
    we ourselves can now fully settle from what survives.
  translational: '''So Circumcellion is just what you called yourselves?'' No -- agonistici is our own
    name; Circumcellion is our opponents''. The violent, itinerant character attached to that outsider
    name reaches the record almost entirely through the people who had every reason to make us look as
    dangerous as possible. Our bare existence, in Numidia specifically, is beyond real doubt; what we
    were actually like beyond that is a live, unresolved question.'
quick_meaning: We call ourselves agonistici -- 'contestants,' those who strive for the truth. Our opponents
  call us Circumcellions instead, and paint us as itinerant fanatics.
---
Re-derived from Doc_06 SS1-SS3 (donlex018, Tier 1 CT, confirmed) and Lexicon-Chunks/donlex018_agonistici.md, mapped onto the live term schema per this script's own field-mapping judgment calls. `term` has no dedicated CT-Contest-Type field, so the contest itself (Frend vs. Shaw, per Doc_06 SS2's own text, which is the authority for this contest, not Doc_03's own earlier framing) is folded into senses.informational/plain_meaning rather than dropped -- a schema-forced placement decision, named here. confidence.formation_confidence = 'Dominant Modern Reconstruction' is Doc_06 SS3's own words ('DMR at best'), extracted, not re-judged. Relations: Refusal of Imperial Legitimacy is Mutual per the chunk's own Reciprocity Note; Persecution closes that same note's own "not yet built as chunks" gap.
