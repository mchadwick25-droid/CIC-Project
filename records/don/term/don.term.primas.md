---
id: don.term.primas
world_id: donatism
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells:
- F3-I
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: 'The succession itself is Documented -- Donatus, then Parmenian, then Primian at Carthage against
    the rival Caecilianist line (Doc_05 SS4) -- and undisputed by the hostile sources that report it. What no
    source supplies is the office from inside: how a primate was chosen, what his authority over the other bishops
    actually consisted of in practice, and how the office understood itself. Monceaux''s remark that in this communion
    ''only the primate spoke in the party''s name'' (Doc_02 SS1) is a modern characterisation, not a quoted Donatist
    statement of the office''s own powers.'
sources:
- source_id: don.source.optatus-against-the-donatists
  locus: the succession at Carthage from Majorinus and Donatus onward
  license: public-domain
- source_id: don.source.augustine-contra-epistulam-parmeniani
  locus: Parmenian's primacy, seen through the refutation of his letter
  license: public-domain
- source_id: don.source.augustine-contra-cresconium
  locus: Primian's primacy and the Maximianist challenge to it
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - a participant asks who led this communion, or whether it had a head
  - a participant asks about Donatus, Parmenian or Primian by name
  do_not_retrieve_when:
  - the question is about later Western primacy or the papacy
relations:
- type: associated-with
  target: don.term.episcopus
- type: associated-with
  target: don.term.concilium
plain_meaning: Our senior bishop sits at Carthage. Donatus held it, then Parmenian, then Primian. Our rival claims
  the same see for its own man at the same time. So there are two primates in one city, as there are two bishops
  in every town.
world_word: primas
false_friend:
- a pope or a patriarch with jurisdiction over a wider church
- an uncontested office, when the rival hierarchy claims the same see in parallel
- a purely honorary title -- the primate's rulings had real disciplinary force here
senses:
  informational: 'The senior bishop of Carthage on this side of the division, claimed in parallel by the rival''s
    own occupant of the same see. The office is where the Maximianist crisis focused: Maximian was elected a rival
    primate against Primian at Cebarsussi in 393, and the Bagai council of 394 condemned that election.'
  evidential: 'Documented as a line of names and as the focus of a documented crisis. Undeveloped as an office:
    nothing in the vendored corpus describes its election procedure, its formal powers, or how its holders understood
    the role, and this build did not develop the term beyond Doc_03''s one-line entry and Doc_05''s passing treatment.'
  personal: The primate is where the parallel hierarchy comes to a point. Two men hold the same chair in the same
    city, and each communion's whole claim is visible in which one it obeys.
  translational: '''Was there a pope of this church?'' -- no. The primate is the senior African bishop of this
    communion, not a universal head, and his counterpart across the street claims exactly the same standing.'
quick_meaning: Our senior bishop at Carthage -- with the rival's man claiming the same chair.
distortion_risk: low
---
Built from Doc_06 SS1 entry 016 (Tier 2, no promotion forwarded). No deployment chunk built this cycle. Development is genuinely modest: Doc_03's one-line entry plus Doc_05 SS4's succession list is the whole of the source material, and the record says so rather than filling the office out.
