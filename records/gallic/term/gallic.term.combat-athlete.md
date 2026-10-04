---
id: gallic.term.combat-athlete
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: >-
    Weighted to Cassian: the systematic combat-order is his and framed as Egypt's ("according to their
    traditions"); Sulpitius uses the word once, of Martin's whole life. Institutes VI (fornication, the
    second combat) is omitted from the edition entirely, so the second combat cannot be read in our
    English text. The Latin lemma is not supplied against the text.
sources:
- source_id: gallic.source.cassian-institutes
  locus: 'Institutes V.1 ("the struggle against the eight principal faults"); V.3 ("the first conflict we must enter upon is that against gluttony"); V.11 ("one postern however small"); V.12-13 ("the Olympic and Pythian games"; "a full belly"; "a slight skirmish"); X.1 ("Our sixth combat"); X.5 ("the true Christian athlete ... in the lists of perfection")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-ii
  locus: 'Conferences XIII.14 (Job "His well tried athlete ... single combat")'
  license: public-domain
- source_id: gallic.source.sulpitius-letters
  locus: 'Letter II ("those daily struggles which he carried on against the various conflicts with human and spiritual wickedness")'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - why the faults are described as battles, or what an "athlete" has to do with monks
  - in what order the vices were fought
  - participant uses "spiritual warfare," "struggle," "athlete," "training," or "contest"
  - the order of the eight faults, the full belly and the inner combat, Job as athlete, or the Olympic scrutiny
  prefer_instead:
  - the soldier image as a whole and its literal origin at Tours (retrieve soldier of Christ)
  - a particular fault (retrieve the eight principal faults, accidie)
  - real military service
relations:
- type: associated-with
  target: gallic.term.soldier-of-christ
- type: associated-with
  target: gallic.term.purity-of-heart
- type: associated-with
  target: gallic.term.free-will
- type: associated-with
  target: gallic.term.anchorite-hermit
- type: associated-with
  target: gallic.term.bloodless-martyrdom-confessor
- type: associated-with
  target: gallic.term.discretion
- type: associated-with
  target: gallic.term.perfection
- type: associated-with
  target: gallic.term.thoughts
- type: associated-with
  target: gallic.term.eight-principal-faults
- type: associated-with
  target: gallic.term.accidie
- type: associated-with
  target: gallic.term.mortification
- type: associated-with
  target: gallic.term.co-operation
- type: associated-with
  target: gallic.term.the-devil-demons
- type: associated-with
  target: gallic.term.trial
plain_meaning: >-
  For us the monk's interior life is a sequence of single combats - "our first conflict ... against
  gluttony," "our sixth combat ... accidie" - fought in a fixed order. They are the trials of "the
  true Christian athlete who desires to strive lawfully in the lists of perfection," so that no one
  "is worthy to be tried in harder battles, who can be overcome in a slight skirmish."
world_word: combat / athlete
false_friend:
- spiritual warfare as a loose metaphor for inner struggle
- athlete as fitness or self-improvement
- the sequence of faults as a psychology of vices to be understood rather than an order of battle to be fought
senses:
  informational: >-
    Cassian's fifth book turns from the customs of the house "to the struggle against the eight
    principal faults," each a combat with its number: "the first conflict we must enter upon is that
    against gluttony"; "our sixth combat is with what the Greeks call akedia." The order is a
    soldier's and an athlete's: the youth who wants "to enter the highest struggle in the contest,
    should first in the Olympic and Pythian games give evidence of his abilities"; "it is impossible
    for a full belly to make trial of the combat of the inner man"; a fortress is "laid waste by the
    giving up of one postern however small." And when the question of grace is raised, the same figure
    carries it: God "provided for in the case of Job His well tried athlete, when the devil had
    challenged him to single combat" - an athlete who fights "not with his own strength, but with the
    grace of God alone." At Tours the word is used once, of the whole life: Sulpitius counts "those
    daily struggles which he carried on against the various conflicts with human and spiritual
    wickedness" as Martin's martyrdom.
  evidential: >-
    Cassian, Institutes V.1-13, X.1, X.5 and Conferences XIII.14 (systematic, framed as Egypt's);
    Sulpitius, Letter II (once). Institutes VI is absent from the edition. The Latin lemma is not
    supplied against the text.
  personal: >-
    The combat is real, ordered, and never won alone. Gluttony is fought first because no one who loses
    a skirmish is fit for harder battles; and at the summit the athlete's own effort still counts
    under the general's protection - which is why we argue about grace with a wrestler's picture. The
    north has the fight; the south has its order of battle.
  translational: >-
    'Isn't "spiritual warfare" just a figure of speech for temptation?' - for us it was numbered
    single combats in a fixed order, entered only after the lighter ones were won, an athlete's
    scrutiny before the great games, a fortress lost at one small gate - and, at the summit, a combat
    God's grace alone wins, with Tours counting the daily struggles as a bloodless martyrdom.
quick_meaning: >-
  The monk's inner life as single combats, numbered and fought in order, gluttony first. He fights
  like an athlete in the lists, and never wins alone.
distortion_risk: medium
use_note:
  means: "The combat idiom meant the monk's inner life as numbered single combats fought in order, gluttony first, by an athlete who never wins alone."
  not_for:
    - "spiritual warfare as a loose metaphor for private struggle"
    - "athlete as fitness or self-improvement"
    - "the soldier image and its literal Tours origin, which sit in gallic.term.soldier-of-christ"
    - "a particular fault, which sits in gallic.term.eight-principal-faults"
  years: {from: 397, to: 426}
  status: provisional
---
Built from Doc_06 entry 023 (Tier 2; chunk galliclex023_combat-athlete.md; Doc_03 2.2). Register
emic. Quotations verified at locus by the build's own Doc_06 pass; not re-read here. The Greek at
Inst. X.1 is transliterated (akedia) in senses.informational rather than reproduced in Greek script.
Canon cells left empty: F2-P (frightening violence) is already carried by soldier of Christ, whose
discharge-that-forbids-fighting is the substantive answer; this term adds the order, not the answer.

Related-Terms also names the devil / demons and trial - cross-batch at authoring time, added as
relations (typed associated-with) at the reconciliation pass once all 81 term records existed.
