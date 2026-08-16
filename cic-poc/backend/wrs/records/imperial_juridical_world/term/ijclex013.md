---
id: ijclex013
world_id: imperial-juridical-christianity
record_type: term
schema_version: 1
jobs:
- 1
- 2
- 4
- 6
register: emic
review_state: draft
cache_stability: static
term: pro nobis
aliases:
- for us
- for our salvation
- the creed's saving clause
quick_meaning: 'Not only who the Son is, but what he came down to do: "for us men and for our salvation... was crucified also for us... rose again." The creed we confess is a rescue, not only a formula about his nature.'
world_meaning: 'Homoousios settles who he is. This clause settles why it was ever confessed at all: "who
  for us men and for our salvation came down from heaven and was incarnate... and was made man, and was
  crucified also for us under Pontius Pilate. He suffered and was buried, and the third day he rose again
  according to the Scriptures." We did not gather at Nicaea and Constantinople to describe a nature for
  its own sake. We gathered because the Word who is of one being with the Father did something for us — came
  down, took flesh, died, and rose — and a wrong word about WHO he is would have left us unable to say what
  he actually accomplished. The councils exist to guard this clause as much as the one before it; the
  clause is why the guarding was ever worth doing.


  [Ecological Function]: This term is the missing half of what our councils and Tomes defend. ijclex006
  (homoousios) and ijclex009 (Tomus, the two natures) both state WHO Christ is; this term states WHAT he
  did and for WHOM — the content the machinery of primatus and concilium ultimately exists to protect, not
  merely the identity-formula it protects alongside it. Without this clause, the confession of his nature
  would be correct and empty.'
distortion_risk: a participant who has only heard this world discuss councils, sees, and canons may
  reasonably conclude the confession IS the institutional machinery — this clause is the record's own
  answer to that misreading, carried in the same creed the machinery exists to guard, not smuggled in from
  outside it.
retrieval:
  tier: 2
  retrieve_when:
  - participant asks what the gospel is, what this world actually believes happened, or why any of the
    councils' work matters beyond settling a formula
  - conversation has covered homoousios or the Tome and a participant presses toward "so what did he
    actually do."
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: the question is really about Christ's nature specifically (retrieve ijclex006 or ijclex009
      instead) rather than what he did.
  force_llm_vote: false
sources:
- source_id: srcIJC42
  author_gravity_note: The Niceno-Constantinopolitan Creed (381), its own soteriological clause, quoted
    in full in the source row's body.
modern_hearing: a modern participant may assume the ancient councils argued only about abstract metaphysics
  (natures, substances) and never stated in their own creed what any of it was FOR.
original_script: ὑπὲρ ἡμῶν
semantic_domain: doctrinal formula - the creed's soteriological clause
modern_sense: 'The councils as a dispute over Greek philosophical categories, disconnected from any claim
  about rescue or salvation (chunk Modern Hearing).'
period_sense: 'What the Son who is of one being with the Father came down, suffered, died, and rose to
  do - "for us men and for our salvation" - confessed in the same breath as the nature-clause, not a later
  or separate addition to it.'
prior_sense: Greek hyper hemon / Latin pro nobis - "on behalf of us, for our sake"; liturgical formula
  carried into the Latin Mass's own Credo; a builder note, UNVERIFIED as to its own further liturgical
  history beyond the creed text itself.
grounding_criterion: high
conceptual_distance_note: 'GROUNDING: the creed''s own text (srcIJC42), the same conciliar record ijclex006
  and ijclex009 already draw on. | DISTANCE: none - this is the same document''s own next clause, not an
  imported concept.'
confidence:
  citation_specificity: A
  verification_state: verified-direct
  verification_date: '2026-08-16'
  evidentiary_weight: load-bearing
  formation_confidence: Documented
voice_surface: '''For us men and for our salvation he came down, and was made man, and was crucified also
  for us, and the third day he rose again. That is not a formula about his nature alone - it is what he
  did, and for whom.'''
field_relations:
- type: presupposes
  target_id: ijclex006
  note: This term states what the one who is of one being with the Father did; saying WHAT he
    accomplished correctly depends on first saying WHO he is correctly - the confession's other half,
    in the same creed, but the dependency runs from this term back to homoousios, not the reverse.
- type: associated-with
  target_id: ijclex009
  note: The Tome's two-natures settlement and this clause's saving content are both what the councils'
    machinery (primatus, concilium) exists to guard.
contested_claim_ids: []
---
Authored 2026-08-16 (T3 gospel-question follow-on; staging at
Ministry/Technology/Pass2/VR_GOSPEL_QUESTION_STAGING_2026-08-16.md). Closes a gap the 2026-08-16 live
probe found: this world's entire record store carried Christ's NATURE (homoousios, the two natures) but
nowhere carried the creed's own statement of what he came to DO - the gap that produced Marius answering
"what is the gospel" with institutional custody language instead of the creed's actual saving clause.
Wording checked directly against this project's own vendored NPNF2-14 transcription (srcIJC42's own body;
cic/texts/npnf214_seven-ecumenical-councils.xml, div2 id="ix.iii", paragraph id="ix.iii-p6") rather than
carried from builder prior knowledge - the first source in this world's own store checked against a real
text file. Nothing invented: every clause in world_meaning is the creed's own text, quoted or paraphrased
at the same weight the creed itself carries it.

[2026-08-16 revision, per independent adversarial review]: the original draft claimed this citation
"matched the standard srcIJC46/47/48 already set on 2026-08-15" - those source IDs do not exist in this
world's own record store (they belong to a separate, parallel record tree at cic/records/, not this one)
and the claim was struck as a fabricated cross-reference. The field_relations direction to ijclex006 was
also corrected from presupposed-by to presupposes, matching the actual dependency (saying what Christ did
correctly depends on saying who he is correctly, not the reverse); ijclex006.md was updated with the
matching reciprocal entry.
