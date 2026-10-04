---
id: gallic.term.progress-vs-alteration
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-E
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Single-voice (Vincent, Lerins), by definition of the [AS] tag. Cassian's new morning service
    argued for "after long discussion" and Martin's refusal of an unattested cult are parallels
    without the word, not attestations. CT tag (Relationship to present-day traditions) carried from
    Doc_06 section 3: the contest is over the passage's afterlife - Newman's theory of development,
    and later Roman Catholic, Anglican, and Orthodox argument about whether Vincent licenses
    "development" or forbids it; the in-file locus is Heurtley's editorial footnote at ch. 17 [44]
    quoting Newman (about Origen, not Vincent). Nothing in Vincent's own text knows that afterlife,
    and the Representative must not. Latin profectus / permutatio are not attested in the vendored
    translation.
sources:
- source_id: gallic.source.vincent-commonitory
  locus: 'ch. 23 [54-59] ("Shall there, then, be no progress in Christ''s Church? Certainly; all possible progress"; "real progress, not alteration of the faith"; "enlarged in itself ... transformed into something else"; "in the same doctrine, in the same sense, and in the same meaning"; "the same number of joints"; "designating an old article of the faith by the characteristic of a new name")'
  license: public-domain
- source_id: gallic.source.cassian-institutes
  locus: 'III.4 (the new Mattins "after long discussion") - cross-voice parallel, not an attestation'
  license: public-domain
- source_id: gallic.source.sulpitius-vita-martini
  locus: 'ch. XI (the unattested cult refused) - cross-voice parallel, not an attestation'
  license: public-domain
- source_id: gallic.source.npnf-editorial-apparatus
  locus: 'Heurtley''s footnote at Comm. ch. 17 [44] quoting Newman on Development - editorial only; the in-file locus of the CT'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - whether doctrine can develop, or whether the Church can learn anything new
  - what Vincent means by progress
  - how a council can use a new word
  - participant uses "development," "progress," "change," "evolve," "growth," "Newman"
  - Comm. ch. 23; the child and the man; the seed and the harvest; "an old article of the faith ... a new name"
  prefer_instead:
  - the question is about what is kept (retrieve the deposit)
  - the question is about the test (retrieve the rule)
  - Newman's theory of development as such - that is this term's afterlife, not its world meaning
relations:
- type: associated-with
  target: gallic.term.the-rule
- type: associated-with
  target: gallic.term.tradition
- type: associated-with
  target: gallic.term.the-fathers-elders
- type: presupposes
  target: gallic.term.the-deposit
- type: illustrated-by
  target: gallic.term.theotocos
- type: associated-with
  target: gallic.term.council-synod
- type: associated-with
  target: gallic.term.doctor-expositor
- type: presupposes
  target: gallic.term.novelty-antiquity
plain_meaning: >-
  Vincent's answer to "Shall there be no progress in the Church?" All possible progress - but real
  progress, not alteration. The grown man has the same joints he had as a child.
world_word: progress, not alteration
false_friend:
- '"development of doctrine" as Newman''s theory, or Vincent as a charter for change'
- Vincent as a proof-text against all change
- '"progress" as improvement or novelty'
senses:
  informational: >-
    Vincent asks the objection himself and answers it without flinching. "Shall there, then, be no
    progress in Christ's Church? Certainly; all possible progress. ... Yet on condition that it be
    real progress, not alteration of the faith. For progress requires that the subject be enlarged
    in itself, alteration, that it be transformed into something else." Knowledge and wisdom ought
    "in the course of ages and centuries, to increase and make much and vigorous progress; but yet
    only in its own kind; that is to say, in the same doctrine, in the same sense, and in the same
    meaning." The pictures: the body, which grows from infancy to age and yet "men when full grown
    have the same number of joints that they had when children"; the seed, from which the harvest
    springs true to kind. And the practice: councils have done nothing more than commit to writing
    what they received, "often, for the better understanding, designating an old article of the
    faith by the characteristic of a new name."
  evidential: >-
    Directly attested in Vincent alone (Comm. 23). Cassian's added morning office and Martin's
    refusal of a cult are progress and refused alteration in this sense, without the word; the
    distinction and the body's joints are the Commonitory's. The passage's later life in Newman
    is present in our files only in an editor's footnote.
  personal: >-
    Growth is enlargement; a new word may serve an old truth; a new truth is alteration, and
    alteration is the heretic's work. That is how we could accept a council's new word and reject a
    teacher's new doctrine in the same breath.
  translational: >-
    A modern hearer arrives with Newman's "development of doctrine" and wants Vincent either as its
    charter or as its refutation. Neither is in his text. What he sanctions is enlargement without
    transformation - the same body grown, the same faith under a clarifying name - refused the
    moment it becomes "something else."
quick_meaning: >-
  Vincent's rule for growth. All possible progress, but never alteration. The faith may be
  enlarged like a body growing, or given a clearer name; it may not become something else.
distortion_risk: high
use_note:
  means: "Progress meant, for Vincent, enlargement like a growing body or a clearer name for the same faith, never alteration into something else."
  not_for:
    - "development of doctrine as Newman's theory, or Vincent as a charter for change"
    - "Vincent as a proof-text against all change"
    - "what is kept, which sits in gallic.term.the-deposit"
    - "the test of the faith, which sits in gallic.term.the-rule"
  years: {from: 434, to: 434}
  status: provisional
---
Built from Doc_06 entry 057 (`galliclex057_progress-vs-alteration.md`, Tier 2, tags AS TC DR CT;
Doc_03 7.5). The CT (Relationship to present-day traditions) is carried in divergence_note;
formation_confidence stays Documented because the contest is over the passage's afterlife, not
over what Vincent meant - the chunk's own CT section draws that line. The ch. 17 [44] footnote
locus follows the Round-2 spot-check correction (it quotes Newman on Origen, not Vincent).

Relation typing: `presupposes` gallic.term.the-deposit (growth-form of the deposit);
`illustrated-by` gallic.term.theotocos (one of the "new names" the passage has in view, per the
chunk's Ecological Function).

Related-Terms also names the rule, novelty vs. antiquity, tradition, and the Fathers / elders -
cross-batch at authoring time, added as relations (typed associated-with except as stated here) at
the reconciliation pass once all 81 term records existed. Relation typing: `presupposes`
gallic.term.novelty-antiquity follows the chunk's own "the positive face of novelty vs. antiquity
(012)" - the same shape as the rule's presupposes toward the axis (011: the procedure presupposes
the value it runs on). The chunk also names Catholic and heretic / heresy (in-batch); not made
relations, since no dependency is stated.
