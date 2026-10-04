---
id: witt.term.repentance
world_id: lutheran-wittenberg-and-its-congregations
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F1-I
- F4-P
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: 'Documented at every register we speak in, from the first Thesis to the household''s
    catechism: the confessional definition (two parts, terror and faith), the founding sentence, and the
    daily baptismal form are each attested in their own voice, not inferred from one another.'
sources:
- source_id: witt.source.luther-disputation-on-the-power-and-efficacy
  locus: the Ninety-Five Theses, Theses 1-2
  license: public-domain
- source_id: witt.source.luther-babylonian-captivity-of-the-church
  locus: Babylonian Captivity's account of penance -- contrition, confession, satisfaction
  license: public-domain
- source_id: witt.source.luther-large-catechism
  locus: the Large Catechism, cited among this entry's Registry rows (Doc_06 SS5 entry 1.2)
  license: public-domain
- source_id: witt.source.luther-small-catechism
  locus: the Small Catechism on baptism -- daily drowning of the old Adam
  license: public-domain
- source_id: witt.source.melanchthon-augsburg-confession
  locus: the Augsburg Confession XII, repentance's two parts
  license: public-domain
- source_id: witt.source.melanchthon-apology-of-the-augsburg-confession
  locus: the Apology XII, read to 5234 this pass -- contrition and faith, and 'before the writings of
    Luther appeared, the doctrine of repentance was very much confused'
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - repentance or penance
  - contrition, confession, or satisfaction as parts of penance
  - why we kept confession but refused indulgences
  - what baptism means daily
  prefer_instead:
  - the participant means contrition alone (retrieve contrition)
  - the participant means the sacrament of confession's own mechanics (retrieve confession/absolution)
relations:
- type: associated-with
  target: witt.term.indulgence
- type: associated-with
  target: witt.term.contrition
- type: associated-with
  target: witt.term.satisfaction
- type: associated-with
  target: witt.term.the-keys
- type: associated-with
  target: witt.term.faith
- type: associated-with
  target: witt.term.law-and-gospel
- type: associated-with
  target: witt.term.conscience
- type: associated-with
  target: witt.term.baptism
- type: associated-with
  target: witt.term.confession-and-absolution
- type: associated-with
  target: witt.term.assurance
plain_meaning: 'Repentance is not one ritual handled by a priest. It is a whole life turned toward God.
  It has two parts: fear under God''s Law, then trust in his promise.'
world_word: repentance -- 'the whole life of believers should be repentance'
false_friend:
- '''penance'' heard as a punishment or penalty a priest hands down'
- '''repentance'' heard as a single feeling of regret or a one-time conversion'
- the Latin left untranslated as though the meaning were self-evident -- our own translators had to argue
  for 'repent' against 'do penance'
senses:
  informational: 'The first thing we said in public was a sentence about this word: ''Our Lord and Master
    Jesus Christ, when He said Poenitentiam agite, willed that the whole life of believers should be repentance''
    -- and the second was that this could not mean ''the sacramental penance, confession and satisfaction,
    administered by the priests.'' We used to speak of penance as having three parts, contrition, confession
    and satisfaction; we re-founded each one. By 1530 we held to two parts only: ''one is contrition,
    that is, terrors smiting the conscience through the knowledge of sin; the other is faith, which is
    born of the Gospel, or of absolution.'' We even say the word had been dark before us: ''before the
    writings of Luther appeared, the doctrine of repentance was very much confused.'' In the household
    it is daily and bodily -- baptism means ''the old Adam in us should be drowned by daily sorrow and
    repentance, and die with all sins and evil lusts, and, in turn, a new person daily come forth.'''
  evidential: Attested in every register we use, from the founding Theses through the household catechism
    to the confession signed before the Emperor; the Apology names the founder by name as the one who
    cleared the word's confusion.
  personal: This word explains, in one breath, why we kept private confession and refused the sale of
    pardons at the same time -- both answer to the same two-part shape, terror then comfort, that our
    whole doctrine runs on.
  translational: 'Do not hear ''repentance'' as an episode of feeling sorry, and do not hear ''penance''
    as a penalty a priest assigns: we hold one word, a lifelong turning with two parts, daily in baptism
    and sacramental in absolution, never a work that earns anything.'
quick_meaning: A whole-life turning, not a single ritual. First comes fear under the Law. Then comes trust
  in the promise.
distortion_risk: high
use_note:
  means: "Repentance meant a whole life turned to God in two parts, fear under the Law then trust in the promise, not one ritual handled by a priest."
  not_for:
    - "'penance' as a punishment a priest hands down"
    - "repentance as a single feeling of regret or a one-time conversion"
    - "contrition alone, which sits in witt.term.contrition"
  years: {from: 1517, to: 1531}
  status: reviewed
---
Built from Doc_06 §5 entry 1.2 (repentance / penance, Tier 1, confirmed at Doc_03's own estimate). Register emic. Doc_06 tags: [SC][DR][TC][RT]. Author Gravity: none -- both voices, every register from the first Thesis to the Apology. Quotations carried from Doc_06's own script-verified base (§10), not independently re-opened against the vendored files by this authoring pass.

Relations above are this batch's own reading of Doc_06's own Related Terms line for this entry, closed for structural reciprocity by this script's close_reciprocity() (see module docstring, disclosed-scope item 1) -- not Doc_06's own §7 candidate-return-link reconciliation pass, which was not separately re-run here.
