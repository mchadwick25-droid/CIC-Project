---
id: hal.corpus.review
world_id: hieronymian-ascetic-literary
record_type: corpus_review
schema_version: 2
status: draft
register: etic
declinations:
- file: addai_doctrine-of-addai.txt
  rank: deferred
  reason: not yet reviewed by this world
- file: anf01_apostolic-fathers-justin-irenaeus.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: anf03_tertullian.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: anf04_tertullian4-minucius-felix-commodian-origen1-2.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: anf05_hippolytus-cyprian-caius-novatian.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: anf06_gregory-thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: anf07_lactantius-apostolic-constitutions-didache-liturgies.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: anf09_gospel-of-peter-diatessaron-origen-commentaries.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: aphrahat_demonstrations-2-7_hallock1932.txt
  rank: deferred
  reason: not yet reviewed by this world
- file: chronicle-of-edessa_cowper.txt
  rank: deferred
  reason: not yet reviewed by this world
- file: ephraim_prose-refutations_mitchell1912-1921.txt
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf102_augustine-city-of-god-christian-doctrine.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf103_augustine-holy-trinity-doctrinal-moral-treatises.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf104_augustine-anti-manichaean-anti-donatist.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf105_augustine-anti-pelagian-writings.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf107_augustine-homilies-john-soliloquies.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf108_augustine-exposition-psalms.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf109_chrysostom-priesthood-ascetic-homilies-statutes.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf110_chrysostom-homilies-matthew.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf111_chrysostom-homilies-acts-romans.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf112_chrysostom-homilies-corinthians.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf113_chrysostom-homilies-galatians-philemon.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf114_chrysostom-homilies-john-hebrews.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf201_eusebius-church-history-life-of-constantine.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf202_socrates-sozomen-ecclesiastical-histories.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf204_athanasius-select-works-letters.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf205_gregory-nyssa-dogmatic-treatises.txt
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf207_cyril-jerusalem-gregory-nazianzen.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf208_basil-letters-select-works.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf209_hilary-poitiers-john-damascus.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf210_ambrose-select-works-letters.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf212_leo-great-gregory-great.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf213_gregory-great-ephraim-syrus-aphrahat.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: npnf214_seven-ecumenical-councils.xml
  rank: deferred
  reason: not yet reviewed by this world
- file: optatus_against-the-donatists.txt
  rank: deferred
  reason: not yet reviewed by this world
- file: origen_philocalia_lewis1911.txt
  rank: deferred
  reason: not yet reviewed by this world
---

Seeded 2026-08-26 by the cross-system consistency audit, in response to
Mark's standard: every world should reach every available resource; they
can be ranked, but not ignored.

EVERY entry below is `deferred` with the same reason, and that is the
honest state, not a placeholder to be embarrassed about: before this record
existed nothing anywhere said whether this world had considered a given
volume, and the only way to ask was to infer it backwards from whether the
world happened to name an author - a proxy this audit measured wrong.
`deferred` says the true thing: relevance not yet ruled on.

This record is this world's to complete, not the audit's. Converting an
entry means replacing `deferred` with a real rank and a reason a reviewer
can disagree with:

  out-of-region           this volume's ecology is not this world's
  out-of-window           its contents fall outside this world's time window
  beyond-doctrinal-floor  its subject is a movement the census places
                          outside the tradition (Constitution Art. 4;
                          `beyondFloor` in world-census.json)
  no-relevant-content     in scope on paper, nothing this world needs

An entry is DELETED, not re-ranked, when the world takes the volume up: a
source record naming the file is what "sourced" means, and
gate_corpus_accounted (engine/m1/gates_experimental.py) reports a volume
that is both sourced and declined as a stale declination.

Ranking suggestions - never rulings - are in
world-build-docs/_cross-world/CORPUS-USE.md, which ranks each volume
against this world by coverage dates and region. Those tables are one
session's assertion and exist to order the work, not to make the call.
