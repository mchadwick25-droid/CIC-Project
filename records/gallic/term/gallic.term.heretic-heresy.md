---
id: gallic.term.heretic-heresy
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-P
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Cross-voice tension [PV]: Vincent's heretic is a doctrinal category (novelty "under a definite
    name, at a definite place, at a definite time"); Sulpitius's is a man about to be executed by the
    state at bishops' urging, whom Martin defends; Cassian's is a hazard of the monk's reading. The
    Priscillianist affair is used only as evidence of the north's stance on state jurisdiction, not
    for its own content, which is another world's territory (Doc_01 section 8.4). Sacred History
    II.46-51 only was read. No Latin lemma sought.
sources:
- source_id: gallic.source.vincent-commonitory
  locus: 'ch. 2 [4] ("the falsehood of heretical pravity"); ch. 8 [23] ("separated, segregated, excluded"); ch. 24 [63] ("under a definite name, at a definite place, at a definite time"; "dissever himself from the consentient agreement of the universality and antiquity of the Catholic Church")'
  license: public-domain
- source_id: gallic.source.sulpitius-sacred-history
  locus: 'II.46-47 ("the infamous heresy of the Gnostics"; the Synod at Saragossa); II.50 ("declared heretics by a sentence of the bishops"; "a foul and unheard-of indignity, that a secular ruler should be judge in an ecclesiastical cause") - II.46-51 only read'
  license: public-domain
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: 'III.11 ("to protect even heretics themselves")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-i
  locus: 'I.20 ("enticed by the grace of style ... into the errors of heretics")'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - what made someone a heretic, or how heresy was recognized
  - what happened to heretics
  - why Martin defended the Priscillianists
  - participant uses "heretic," "heresy," "orthodox," "Priscillian," "Arian," "persecution"
  - Vincent's "definite name ... place ... time"; Trier and the sword; Cassian's monk enticed by "grace of style"
  prefer_instead:
  - the question is about the rule that detects heresy (retrieve the rule)
  - the question is about the specific foil (retrieve Pelagians as foil)
  - Priscillianism's own content - another world's territory
  - the excommunication formula (retrieve anathema)
relations:
- type: associated-with
  target: gallic.term.bloodless-martyrdom-confessor
- type: associated-with
  target: gallic.term.the-rule
- type: associated-with
  target: gallic.term.novelty-antiquity
- type: associated-with
  target: gallic.term.monk-bishop
- type: tension-with
  target: gallic.term.catholic
- type: illustrated-by
  target: gallic.term.pelagians-as-foil
- type: presupposed-by
  target: gallic.term.anathema
- type: associated-with
  target: gallic.term.trial
- type: associated-with
  target: gallic.term.council-synod
- type: associated-with
  target: gallic.term.communion
- type: associated-with
  target: gallic.term.doctor-expositor
plain_meaning: >-
  One who has left the consent of the universal and ancient Church under his own name. To be
  cast out by bishops - but not killed. The state's sword in a Church cause is "a foul and
  unheard-of indignity."
world_word: heretic / heresy ("heretical pravity")
false_friend:
- '"heretic" as a slur for any dissenter, or as the Inquisition''s category'
- heresy as intellectual nonconformity
- Martin's defence of the Priscillianists as religious toleration
senses:
  informational: >-
    Vincent defines the heretic by what he leaves: "What heresy ever burst forth save under a
    definite name, at a definite place, at a definite time? Who ever originated a heresy that did
    not first dissever himself from the consentient agreement of the universality and antiquity of
    the Catholic Church?" Heresy is novelty with a birthday; the remedy is antiquity; the sanction
    is Paul's - "separated, segregated, excluded." Cassian's elders know the heretic as a hazard of
    reading: monks "enticed by the grace of style" are drawn "into the errors of heretics." At Tours
    the heretic is a man with a body. Sulpitius does not doubt Priscillian's followers are heretics;
    but when the affair goes to the emperor's court, Martin's position is fixed: it "was quite
    sufficient punishment that, having been declared heretics by a sentence of the bishops, they
    should have been expelled from the churches," and "a foul and unheard-of indignity, that a
    secular ruler should be judge in an ecclesiastical cause." He goes to Trier "to protect even
    heretics themselves," and the bishops who urged the sword are the ones he will not sit with
    again.
  evidential: >-
    Attested in all three founding voices: Vincent (Comm. 2, 8, 24), Sulpitius (Sacred History
    II.46-50; Dial. III.11), Cassian (Conf. I.20). The three referents - a category, a man, a
    danger to reading - are documented separately. What Priscillian actually taught is not this
    world's evidence.
  personal: >-
    We could anathematize a doctrine and defend the life of the man who taught it. The heretic is
    to be cast out of the Church; he is not to be killed; and an emperor has no business judging a
    Church's cause. That is what our saint would not forgive the bishops for forgetting.
  translational: >-
    A modern hearer may hear "heretic" as the Inquisition's word, or read Martin's defence of the
    Priscillianists as toleration. Neither is ours. A heretic is excluded, anathematized, and kept
    from the monk's reading - and judged by bishops, not emperors; expelled, not executed.
quick_meaning: >-
  One who has left the consent of the ancient, universal Church under his own name. Cast out by
  bishops' sentence - never by an emperor's sword. Martin went to Trier to protect even
  heretics.
distortion_risk: high
use_note:
  means: "A heretic was one who left the consent of the universal and ancient Church under his own name, to be cast out by bishops and never put to the sword."
  not_for:
    - "a slur for any dissenter, or the Inquisition's category"
    - "Martin's defence of the Priscillianists as religious toleration"
    - "the rule that detects heresy, which sits in gallic.term.the-rule"
    - "the excommunication formula, which sits in gallic.term.anathema"
  years: {from: 397, to: 434}
  status: reviewed
---
Built from Doc_06 entry 060 (`galliclex060_heretic-heresy.md`, Tier 2, tags SC DR RT PV; Doc_03
7.10). The [PV] (category / man / reading-hazard) is carried in divergence_note and every sense.
canon_cells: F3-P because Trier and Martin's refusal are this world's own direct answer to the
question of a church using power against Christians who disagreed.

Relation typing: `tension-with` gallic.term.catholic (its opposite); `illustrated-by`
gallic.term.pelagians-as-foil (the one heresy named in the grace argument); `presupposed-by`
gallic.term.anathema (the sanction presupposes the category).

Related-Terms also names the rule, novelty vs. antiquity, and bishop / the monk-bishop - cross-batch
at authoring time, added as relations (typed associated-with) at the reconciliation pass once all 81
term records existed. The chunk also names Apostolic See / Pope and the devil / demons (in-batch);
not made relations, since no dependency is stated.
