---
id: gallic.term.illusion
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells:
- F1-P
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: >-
    A genuinely shared narrative type - Sulpitius (Tours) and Cassian (Marseilles) tell the same
    kind of story with different remedies (the false robe brought to the saint; the thought brought
    to the elder). Coverage limit, stated not filled: Cassian's own conference on the subject,
    Conf. XXII "On Nocturnal Illusions," is absent from this world's English text ("This Conference
    is omitted"); Gennadius attests the title. Brictio's sneer is the inside voice of skepticism.
    The historicity of the northern episodes falls under virtus / power's Reported-Experience
    Status. No Latin lemma supplied against the text.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: 'ch. XXIII (Anatolius; "the devil could no longer dissemble or conceal his own deception"); ch. XXIV (the purple-robed "Christ"; "I will not believe that Christ has come, unless he appears with that appearance and form in which he suffered")'
  license: public-domain
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: 'III.15 (Brictio: "ridiculous fancies about visions")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-i
  locus: 'I.21 ("Of the illusion of Abbot John"; "a filthy Ethiopian"); II.5 (Heron, "cast down by an illusion of the devil"; "an angel of Satan as an angel of light")'
  license: public-domain
- source_id: gallic.source.cassian-institutes
  locus: 'II.13 ("lest our envious adversary ... by some illusion in a dream")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-xii-xxii-absence
  locus: 'Conf. XXII "On Nocturnal Illusions" - "This Conference is omitted"; coverage limit, stated'
  license: public-domain
- source_id: gallic.source.gennadius-de-viris-illustribus
  locus: 'ch. LXII (attests the title of Conf. XXII)'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - how the monks knew a vision was true
  - whether they trusted dreams and revelations
  - why Martin refused a Christ in purple
  - what "nocturnal illusions" were
  - participant uses "illusion," "delusion," "false vision," "deception," "dream," "discernment of spirits"
  - Anatolius's robe; the crowned Christ; Heron's angel; Abbot John's illusion; the missing Conference XXII
  do_not_retrieve_when:
  - the question is about the faculty that detects it (retrieve discretion)
  - the question is about the devil in general (retrieve the devil / demons)
  - the content of Conf. XXII - absent from our English text; state the absence, do not fill it
relations:
- type: associated-with
  target: gallic.term.cell
- type: associated-with
  target: gallic.term.disclosure-of-thoughts
- type: associated-with
  target: gallic.term.discretion
- type: associated-with
  target: gallic.term.thoughts
- type: associated-with
  target: gallic.term.virtus
- type: associated-with
  target: gallic.term.novelty-antiquity
- type: associated-with
  target: gallic.term.eight-principal-faults
- type: associated-with
  target: gallic.term.sign-of-the-cross
- type: presupposes
  target: gallic.term.the-devil-demons
- type: associated-with
  target: gallic.term.trial
- type: associated-with
  target: gallic.term.angels
- type: associated-with
  target: gallic.term.antichrist
plain_meaning: >-
  A false show by which the devil ruins a monk. A robe said to come from heaven, a crowned Christ,
  an angel's promise at a well. This is the danger our discretion exists to meet.
world_word: illusion (of the devil)
false_friend:
- hallucination or delusion as psychology
- '"discernment" as a private test'
- Martin's refusal of the purple Christ as skepticism about miracles in general
senses:
  informational: >-
    At Tours the devil's deceptions are exposed by being brought before Martin. The youth
    Anatolius claims angels speak with him and produces a robe "from heaven" - which vanishes when
    the brethren insist on taking him to Martin, "so that the devil could no longer dissemble or
    conceal his own deception." Then the devil himself comes "clothed in purple, and with a
    glittering crown," saying he is Christ; Martin, dazzled at first, keeps a long silence until the
    Spirit reveals it, and answers: "I will not believe that Christ has come, unless he appears with
    that appearance and form in which he suffered." At Marseilles the same stories come from Egypt
    with the rule attached: Abbot John's illusion, the Ethiopian who claimed credit for his fast;
    Heron, who "received with the utmost reverence an angel of Satan as an angel of light" and
    threw himself into a well - each the fruit of trusting one's own judgment against the elders.
    The night has its illusions too; a whole conference was written on them, and our English text
    says only, "This Conference is omitted."
  evidential: >-
    Attested in both nodes: Sulpitius (Vita XXIII, XXIV; Dial. III.15) and Cassian (Conf. I.21,
    II.5; Inst. II.13). The south's own full treatment, Conf. XXII, is absent from this world's
    English text - a stated coverage limit, not filled from elsewhere. Brictio's "ridiculous fancies
    about visions" is our own house's skeptic, on the record.
  personal: >-
    Neither at Tours nor at Marseilles do we trust a vision on its own account. At Tours the false
    robe is brought to the saint; at Marseilles the thought is brought to the elder. The one test the
    devil cannot pass is the crucified form with its wounds.
  translational: >-
    A modern hearer may read this as hallucination, or make Martin's refusal of the purple Christ
    into skepticism about the miraculous. It is the reverse: a real deception by a real deceiver,
    exposed by the saint's presence or the elders' judgment - a danger we wrote a whole conference
    on, which a later English hand removed.
quick_meaning: >-
  A false show by which the devil ruins a monk - a robe "from heaven," a crowned Christ, a
  promise at a well. Tours brings it to the saint; Marseilles brings it to the elder.
distortion_risk: medium
---
Built from Doc_06 entry 052 (`galliclex052_illusion.md`, Tier 2, tags SC DR TC; Doc_03 6.7). The
Conf. XXII excision (Registry row 11) is this term's own coverage limit and is cited as a source
entry pointing at the absence record, per the chunk's Key Sources.

Relation typing: `presupposes` gallic.term.the-devil-demons (an illusion is the deceiver's work).

Related-Terms also names discretion, thoughts, virtus / power, disclosure of thoughts, cell, novelty
vs. antiquity, and the eight principal faults - cross-batch at authoring time, added as relations
(typed associated-with) at the reconciliation pass once all 81 term records existed.
