---
id: witt.term.hymn
world_id: lutheran-wittenberg-and-its-congregations
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F5-I
- F5-P
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: 'Documented at the hymnal prefaces and the confessional statement of purpose alike;
    evidential weakness disclosed, not used to hold down the tier: no hymn text beyond a few openings
    has been read in this build, every English line is a single translator''s rendering, and no tune or
    parish record is in our library -- what any parish actually sang is Inferential/Thin. This record
    carries Reported-Experience Status for the same reason.'
sources:
- source_id: witt.source.luther-large-catechism
  locus: the Large Catechism, cited among this entry's Registry rows (Doc_06 SS5 entry 4.9)
  license: public-domain
- source_id: witt.source.luther-small-catechism
  locus: the Small Catechism -- 'go about your work and perhaps sing a song'
  license: public-domain
- source_id: witt.source.luther-deutsche-geistliche-lieder-the-hymns
  locus: the hymn texts (Bacon's composite English; tunes absent from the file)
  license: public-domain
- source_id: witt.source.luther-four-hymnal-prefaces-to-walters-gesangb
  locus: the four hymnal prefaces -- 'to make a good beginning and to encourage others'
  license: public-domain
- source_id: witt.source.melanchthon-augsburg-confession
  locus: the Augsburg Confession XXIV -- German hymns 'added to teach the people'
  license: public-domain
- source_id: witt.source.melanchthon-apology-of-the-augsburg-confession
  locus: the Apology XV, XXIV, read this pass
  license: public-domain
- source_id: witt.source.johann-letter-of-reminiscence-on-luther-as
  locus: Walter's late reminiscence -- 'he kept me three weeks long at Wittenberg... until the first German
    Mass was sung'
  license: public-domain
- source_id: witt.source.cyriacus-preface-to-the-cithara-lutheri
  locus: Spangenberg's preface, cited among this entry's Registry rows (Doc_06 SS5 entry 4.9)
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - hymns, or singing in German
  - what our hymns were for
  - '''A Mighty Fortress'''
  prefer_instead:
  - the participant wants a specific hymn's full text -- our library holds only openings and fragments
relations:
- type: associated-with
  target: witt.term.the-word
- type: associated-with
  target: witt.term.catechism
- type: associated-with
  target: witt.term.the-devil
- type: associated-with
  target: witt.term.daily
- type: associated-with
  target: witt.term.the-mass
- type: associated-with
  target: witt.term.death
- type: associated-with
  target: witt.term.sects-and-new-spirits
- type: associated-with
  target: witt.term.the-turk
- type: associated-with
  target: witt.term.martyr
- type: associated-with
  target: witt.term.pastor
plain_meaning: Hymns are songs in our own language, written to teach ordinary people who cannot read Latin.
  We sing them at work, at burial, and inside our services. Old tunes often carry new, Christian words.
world_word: hymn -- German song, 'to make a good beginning,' teaching the unlearned
false_friend:
- hymns heard as mere ornament or mood in a service
- the German hymn heard as a total break with Latin, when we kept both side by side
- '''A Mighty Fortress'' heard as a battle-anthem sung defiantly at Worms -- our own translator''s footnote
  refuses that legend'
senses:
  informational: '''To make a good beginning and to encourage others who can do it better, I have myself,
    with some others, put together a few hymns, in order to bring into full play the blessed Gospel''
    -- so that our young people might turn from carnal songs. Our confession says what the songs are for:
    ''the parts sung in Latin are interspersed here and there with German hymns, which have been added
    to teach the people,'' keeping Latin ''on account of those who are learning.'' In the house: ''with
    joy go about your work and perhaps sing a song.'' The hymn carries our memory too -- at burial ''no
    dirges nor lamentations, but comforting songs,'' old tunes kept with new words: ''the notes and melodies
    are of great price; it were pity to let them perish; but the words to them were unchristian and uncouth,
    so let these perish.'''
  evidential: Attested at the hymnal prefaces, the confession, and one late reminiscence (Walter) -- the
    fullest non-founder voice in our library, though evidentially thin (no tune, one witness, decades
    on).
  personal: This is the register with the widest reach among our own people -- teaching set to old tunes
    so the unlearned may learn or pray while the learned keep their Latin.
  translational: 'Do not hear our hymns as mere ornament, or the German hymn as abolishing Latin, or ''A
    Mighty Fortress'' as a defiant anthem at Worms: we mean teaching set to memorable tunes, a household
    work-song, a burial comfort, and a weapon against the devil.'
quick_meaning: Songs in our own language, teaching those who cannot read Latin.
distortion_risk: high
---
Built from Doc_06 §5 entry 4.9 (hymn / German singing, Tier 1 ↑ from Doc_03's estimate of 2). Register emic. Doc_06 tags: [SC][RT][DR]. Author Gravity: none -- both voices, plus the fullest non-founder attestation in the build. Source Registry rows cited: R25, R26, R27, R28, R37, R38, R45, R47. Quotations carried from Doc_06's own script-verified base (§10), not independently re-opened against the vendored files by this authoring pass.

Reported-Experience Status (Doc_06 §5 entry 4.9): reported as our own self-understanding, not assessed for historical accuracy; the hymn's formative work is central by our own account and by the register's reach, while what was actually sung, where, and to what tune is thinly attested -- one late participant, no tune, no parish record.

Relations above are this batch's own reading of Doc_06's own Related Terms line for this entry, closed for structural reciprocity by this script's close_reciprocity() (see module docstring, disclosed-scope item 1) -- not Doc_06's own §7 candidate-return-link reconciliation pass, which was not separately re-run here.
