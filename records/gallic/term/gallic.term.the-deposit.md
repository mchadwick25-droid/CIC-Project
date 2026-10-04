---
id: gallic.term.the-deposit
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F2-T
- F4-E
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Single-voice (Vincent, Lerins), by definition of the [AS] tag - this is our own signature
    vocabulary, not received from a reported Egyptian conference, and Vincent is the only Lerins
    voice read in English. Cassian's "the Institutes which are not mine but the fathers'" is a
    cross-voice parallel, not an attestation of the word. The Latin depositum is not attested in the
    vendored translation; Heurtley's English gives "deposit."
sources:
- source_id: gallic.source.vincent-commonitory
  locus: 'ch. 21 [51] ("O Timothy, keep the deposit, shunning profane novelties"); ch. 22 [53] ("What is ''The deposit''? ... not an author but a keeper"; "Preserve the talent of Catholic Faith inviolate"; "Thou hast received gold; give gold in turn"; "O Timothy! O Priest! O Expositor! O Doctor!"); chs. 23-24 (the exposition continued)'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-i
  locus: 'Preface I ("the Institutes which are not mine but the fathers''") - cross-voice parallel, not an attestation'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - what "the deposit of faith" means, or where the phrase comes from
  - what a teacher is allowed to add
  - participant uses "deposit," "deposit of faith," "entrusted," "hand on," "keep"
  - 1 Timothy 6:20; "not an author but a keeper"; "gold for gold"
  prefer_instead:
  - the question is about the three-part test (retrieve the rule)
  - the question is about legitimate growth (retrieve progress vs. alteration)
  - the later dogmatic phrase "deposit of faith" as a technical term of a living tradition - outside our window
relations:
- type: associated-with
  target: gallic.term.novelty-antiquity
- type: associated-with
  target: gallic.term.the-rule
- type: associated-with
  target: gallic.term.tradition
- type: associated-with
  target: gallic.term.the-fathers-elders
- type: associated-with
  target: gallic.term.disciple-master
- type: presupposed-by
  target: gallic.term.progress-vs-alteration
- type: associated-with
  target: gallic.term.catholic
- type: associated-with
  target: gallic.term.doctor-expositor
- type: associated-with
  target: gallic.term.commonitory-peregrinus
plain_meaning: >-
  The faith as a thing held in trust. What the Apostle told Timothy to keep - received gold, to be
  given back as gold, by one who is "not an author but a keeper."
world_word: the deposit ("keep the deposit")
false_friend:
- '"the deposit of faith" as a later dogmatic-theology term - a defined body of doctrine administered by a magisterium'
- '"deposit" as a bank balance'
senses:
  informational: >-
    Vincent takes one verse and turns it over for three chapters. "What is 'The deposit'? That
    which has been intrusted to thee, not that which thou hast thyself devised: a matter not of wit,
    but of learning; not of private adoption, but of public tradition; a matter brought to thee, not
    put forth by thee, wherein thou art bound to be not an author but a keeper, not a teacher but a
    disciple." Then the charge: "Thou hast received gold; give gold in turn. Do not substitute one
    thing for another." And the address widens from Timothy to every teacher - "O Timothy! O Priest!
    O Expositor! O Doctor!" - who may engrave and polish the gems of doctrine so that what was
    believed imperfectly is clearly understood, but must change nothing.
  evidential: >-
    Directly attested in Vincent alone (Comm. 21-24). Cassian says the same of the monastery's
    customs, and Martin of an unattested cult, but the word "deposit" and its gold are Vincent's.
    The word belongs to Lerins.
  personal: >-
    Our most authoritative writer calls himself a keeper, not an author. We learn the faith as a
    talent to be returned, not a possession to be improved. The keeper's whole excellence is
    fidelity of transmission.
  translational: >-
    A modern hearer may know "the deposit of faith" as a later technical term - a defined body of
    doctrine under a magisterium. For us it is one verse read as a charge to a young bishop, and
    through him to every teacher, by a monk writing against his own forgetfulness: gold received,
    gold returned, nothing substituted.
quick_meaning: >-
  The faith held in trust. Gold received, gold to be given back - by one who is a keeper, not an
  author. Vincent's reading of the Apostle's charge to Timothy.
distortion_risk: medium
use_note:
  means: "The deposit meant the faith held in trust, gold received and gold to be returned, by one who is a keeper and not an author, in Vincent's reading of Timothy."
  not_for:
    - "the later dogmatic deposit of faith administered by a magisterium"
    - "a bank balance"
    - "the three-part test, which sits in gallic.term.the-rule"
    - "legitimate growth, which sits in gallic.term.progress-vs-alteration"
  years: {from: 434, to: 434}
  status: reviewed
---
Built from Doc_06 entry 056 (`galliclex056_the-deposit.md`, Tier 2, tags AS TC; Doc_03 7.4).
Tagged [AS] in Doc_06 (not traceable to any reported Egyptian conference); the single-voice status
is stated in divergence_note. canon_cells: F4-E because "not an author but a keeper" is this
world's own answer to whether its faith was received or invented; F2-T because the deposit is
"public tradition," not Scripture alone.

Relation typing: `presupposed-by` gallic.term.progress-vs-alteration (growth is the deposit's
own enlargement; progress presupposes something kept).

Related-Terms also names the rule, tradition, novelty vs. antiquity, the Fathers / elders, and
disciple / master - cross-batch at authoring time, added as relations (typed associated-with) at the
reconciliation pass once all 81 term records existed. The chunk also names heretic / heresy
(in-batch); not made a relation, since no dependency is stated.
