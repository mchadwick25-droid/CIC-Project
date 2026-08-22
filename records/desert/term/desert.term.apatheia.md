---
id: desert.term.apatheia
world_id: desert-monasticism
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells: [F4-P]
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: corroborating
  formation_confidence: Contested
  divergence_note: null
sources:
- source_id: desert.source.evagrius-praktikos
  locus: "the praktike-apatheia-theoria scheme (consult-only; vendored excerpt witness via Socrates IV.23)"
- source_id: desert.source.rubenson-letters
  locus: "the contested Antony-literacy scope of the term's founding association (consult-only)"
- source_id: desert.source.gould-desert-fathers
  locus: "the named counter-position to Rubenson's Origenist-influence reading (consult-only)"
retrieval:
  tier: 2
  retrieve_when:
  - questions about the goal of all this discipline
  - questions about freedom from anger, craving, or compulsion
  do_not_retrieve_when:
  - do not let the term stand unglossed - the apathy false-cognate is near-certain
relations:
- type: associated-with
  target: desert.term.logismoi
- type: associated-with
  target: desert.term.theoria
- type: associated-with
  target: desert.term.antirrhesis
- type: associated-with
  target: desert.term.puritas-cordis
plain_meaning: "Freedom from the passions that drive a person. In Evagrius's plan, the goal of the working stage of this life. Not apathy."
world_word: apatheia
false_friend:
- apathy (not caring)
senses:
  informational: "In Evagrius's systematized scheme, the achieved state the practical life aims at: freedom from disordered passion, preceding contemplation. In this technical sense it is Strand C's vocabulary - the wider movement hoped for interior peace without this word's philosophical machinery."
  evidential: "The systematized sense rests on Evagrius's own writings, which survive but have no English rendering to quote directly here; his works are named and described by the historian Socrates, who quotes some of his sentences. A live scholarly contest touches the term's deepest root: Rubenson reads the Letters of Antony as philosophically literate and Origenist-leaning - which would put this register near the movement's founder - while Gould's published counter-position holds that reading overreaches. The contest stands open, unsettled either way."
  personal: "The opposite of not caring: the capacity to be fully engaged without being owned by your reactions - reached, if at all, through years of combat with the thoughts, never assumed at the start."
  translational: "Never translate as apathy. 'Freedom from compulsion' is closer; Cassian, translating for the West, deliberately replaced the word itself with 'purity of heart' to dodge exactly this misreading."
quick_meaning: "Freedom from the passions that drive you. Won slowly - and it is not apathy."
---
Re-derived from Doc_06 SS2.2 (Tier 2; tags AS TC DR PV CT). The [CT]
contest is carried exactly as that document's twice-corrected form has
it: contested as to HISTORICAL SCOPE (whether Antony himself possessed
the philosophical literacy this register presupposes - Rubenson vs
Gould), not as to whether apatheia-vocabulary belongs in this world at
all; Doc_04 SS3 routes the same tension to gravities 1 and 3 without
threatening their cross-strand attestation; apatheia itself is not
rated in Doc_02 (the Letters' authenticity and Origenist reading are).
formation_confidence Contested carries that live status. Full contest
detail: desert.contested.antony-literacy (step 3c).

Step3a Review Round 1, Finding 7: Gould's counter-position was named in
the evidential sense but not registered in sources[] - added
(desert.source.gould-desert-fathers), so the load-bearing name does
not float unregistered here either.

Step3a Review Round 2, Finding 1 / New Finding 2: the Round 1 fix had
removed "vendored"/"consult-only" but written in "this corpus can
quote directly," the same banned family - reworded again to plain
in-world evidence talk with no corpus self-reference.
