---
id: witt.term.household
world_id: lutheran-wittenberg-and-its-congregations
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-I
- F5-P
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: 'Documented as prescription -- the household program exactly as our own catechisms
    set it down -- and Inferential/Thin as any actual house''s practice; Luther-only, cross-register,
    for the mechanism itself (our confession never uses the word ''household'' at all). This record carries
    Reported-Experience Status: our formation is centrally this site by our own account, while whether
    any household held it is not something our library answers.'
sources:
- source_id: witt.source.luther-large-catechism
  locus: the Large Catechism -- weekly examination and the day's three prayers
  license: public-domain
- source_id: witt.source.luther-small-catechism
  locus: the Small Catechism, whole file -- 'the simple way a father should present them to his household'
  license: public-domain
- source_id: witt.source.luther-selections-from-the-table-talk
  locus: the Table Talk -- 'we are very cold and careless in praying' (Contested as verbatim)
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - household, or 'father of a family'
  - who examines whom, and how often
  - the shape of a Christian house among us
  prefer_instead:
  - the participant means the catechism's own content rather than its household setting (retrieve catechism)
relations:
- type: associated-with
  target: witt.term.catechism
- type: associated-with
  target: witt.term.daily
- type: associated-with
  target: witt.term.neighbor
- type: associated-with
  target: witt.term.we-are-all-priests
- type: associated-with
  target: witt.term.spiritual-and-temporal-estate
- type: associated-with
  target: witt.term.calling
- type: associated-with
  target: witt.term.marriage
- type: associated-with
  target: witt.term.prayer
- type: associated-with
  target: witt.term.worthy-unworthy
- type: associated-with
  target: witt.term.pastor
- type: associated-with
  target: witt.term.obedience
- type: associated-with
  target: witt.term.the-two-governments
- type: associated-with
  target: witt.term.chastity
plain_meaning: The household is where our catechism is taught. A father questions his family and servants
  every week. He leads prayer three times a day. This is how ordinary people learn the faith.
world_word: the household -- father, wife, children, servants; the catechism's own site
false_friend:
- '''household'' heard as the modern nuclear family'
- the father's examination and food-withholding heard as domestic abuse rather than a formation duty commanded
  of him
- the program described here heard as a fact about how any actual house lived
senses:
  informational: 'Every part of our little book is headed the way a father should present it -- ''the
    simple way a father should present them to his household.'' ''It is the duty of every father of a
    family to question and examine his children and servants at least once a week and to ascertain what
    they know of it''; the parts are recited morning, table and night, ''and until they repeat them, they
    should be given neither food nor drink.'' Why the house: because through baptism we are all consecrated
    to the priesthood, so a father is a priest in his own house, and because the three parts must be known
    by ''the ordinary Christian, who cannot read the Scriptures.'' The household''s economy, its table,
    its prince, its own coldness in prayer, are each confessed there too.'
  evidential: Luther-only, cross-register, for the mechanism itself -- our confession never once uses
    this word; the catechization practice generally is both voices.
  personal: 'This is our own chosen site of formation: the place where the Word is recited, the Sacrament
    prepared for, the conscience examined, the prince prayed for, the devil driven off.'
  translational: 'Do not hear ''household'' as the modern nuclear family, and do not hear the father''s
    weekly examination as abuse: we mean a stratified house of kin and servants under one head answerable
    to God, prescribed as the place where every Christian is formed -- stated as a duty, unattested as
    any actual house''s practice.'
quick_meaning: 'The house where the catechism is taught: father, wife, children, servants, examined weekly.'
distortion_risk: high
use_note:
  means: "The household meant father, wife, children and servants as the catechism's own site, where the father taught, questioned and led daily prayer."
  not_for:
    - "'household' as the modern nuclear family"
    - "the father's examination and withholding of food as domestic abuse, which is a modern sense"
    - "the catechism's content apart from its household setting, which sits in witt.term.catechism"
    - "the prescribed routine as attested practice, since witt.story.household-catechism-lesson-typical-practice holds the prescription only"
  years: {from: 1529, to: 1546}
  status: reviewed
---
Built from Doc_06 §5 entry 4.2 (household / 'father of a family', Tier 1, confirmed at Doc_03's own estimate). Register emic. Doc_06 tags: [AS][RT][DR]. Author Gravity: Luther-only, cross-register, for the mechanism -- confirmed. Quotations carried from Doc_06's own script-verified base (§10), not independently re-opened against the vendored files by this authoring pass.

Reported-Experience Status (Doc_06 §5 entry 4.2): reported as our own self-understanding, not assessed for historical accuracy; the household is formationally central -- our own chosen site -- while whether any household held it is Inferential/Thin. We speak the program as we set it down and keep the two axes apart.

Relations above are this batch's own reading of Doc_06's own Related Terms line for this entry, closed for structural reciprocity by this script's close_reciprocity() (see module docstring, disclosed-scope item 1) -- not Doc_06's own §7 candidate-return-link reconciliation pass, which was not separately re-run here.
