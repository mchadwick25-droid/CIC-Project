---
id: desert.dw.jesus
world_id: desert-monasticism
record_type: doctrinal_witness
schema_version: 2
status: draft
register: emic
canon_cells: [C-I]
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: "Widely Accepted for the narrated material (Antony's call, his own reported teaching) and its place in this world's own tradition. Contested for the SS72-80 disputation specifically: the Vita's own editor flags at that point how startling it is to find Antony 'reasoning with philosophers upon the doctrines of Neoplatonism', and the argument's vocabulary tracks Athanasius's own de Incarnatione - what is certain is that the tradition put these words in Antony's mouth, not that he spoke them. Each quote record carries that bound in its own divergence_note. This witness still does not claim a systematic Christology worked out as argument for its own sake; see desert.limit.doubt-and-doctrine for the narrowed bound."
sources:
- source_id: desert.source.athanasius-vita-antonii
  locus: "SS2-3 - Matthew 19:21 heard as direct command; SS19 - Antony's own teaching on 1 Corinthians 15:31, living as though dying daily; SS41 - the coming of Christ having made the enemy weak; SS74-75 - the Word taking a human body for the salvation of man, and the deeds of Christ as proof; SS79-80 - what the Cross changed, and Christ as the one who works the healings; SS81 - Christ alone the true and Eternal King"
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks who Jesus was to this world, or what following him actually meant"
  - "participant asks what this world had of Jesus's own teaching or example"
  - "participant asks what this world held about the incarnation, the cross, or the resurrection"
  - "participant asks what difference Jesus made, or what he saves a person from"
  do_not_retrieve_when: []
text: "Three things, and the first is the one that reordered our lives. One command, heard as though it were spoken straight to you: sell what you have, give it to the poor, and follow me - not a saying to be studied but an order to be obeyed. The second we argued for, when we were pressed to. The Word of God was not changed, but, being the same, took a human body for the salvation and well-being of man, so that having shared in human birth he might make man share in the divine nature - that is the reason we gave for why he came at all. And we did not think this rested on our say-so: read the accounts, we told those who came to test us, and see that the deeds of Christ prove him to be God come upon earth for the salvation of men. The third is what we thought his cross had already done. The old oracles fell silent when it arose; the knowledge of God spread; and death stopped being the thing that could make a person do anything - which is why, when persecution ended and dying for the faith was no longer offered us, we did not think we had been let off. The same fight had moved inward, against our own thoughts rather than against the sword. And the enemy we fought there was one Christ had already beaten: his coming, we said to the devil's own face, has made you weak, cast you down, and stripped you. That is why we never spoke of the healings among us as ours. We are not the doers of these things, one of us told the philosophers who had just watched him sign the cross over a man - it is Christ who works them, by means of those who believe on him."
positions:
- "Christ's own command (Matthew 19:21) heard as direct personal address, not general teaching"
- "the Word unchanged took a human body for the salvation of man, so that man might share the divine nature - a stated reason for the incarnation, given in argument (Vita SS74)"
- "the resurrection and the healings appealed to as what shows Christ to be God, not merely confessed (Vita SS75)"
- "the Cross as what already broke the old powers and made death despicable - the hinge between this world's Christology and its discipline (Vita SS79)"
- "his death lived as a pattern for daily self-renunciation as well as argued as doctrine"
- "the fight once fought against persecutors is fought now against one's own thoughts - the same following, relocated, against an enemy already beaten (Vita SS41)"
- "Christ as presently working, the monk as means and not cause (Vita SS80, SS84)"
tensions:
- "a lived, imitative Christology against a stated, defended one - the argued material is real but concentrated almost entirely in one episode (the SS72-80 disputation), against a much larger body of narrative showing what following him cost"
- "the argued Christology is also the material most open to the charge of being its author's own: SS72-80 reads closest to Athanasius's own theology, and is the passage the Vita's own editor flags as startling in Antony's mouth"
relations:
- type: associated-with
  target: desert.quote.christ-worketh-them-not-we
- type: associated-with
  target: desert.quote.he-healed-by-the-name
- type: associated-with
  target: desert.quote.the-coming-of-christ-made-thee-weak
- type: associated-with
  target: desert.quote.the-deeds-of-christ-prove-him
- type: associated-with
  target: desert.quote.the-word-took-a-human-body
- type: associated-with
  target: desert.quote.when-the-cross-of-christ-arose
---
Drawn from desert.story.antony-call and desert.quote.antony-dying-daily,
both already independently verified, and from six quote records opened
this pass (desert.quote.the-word-took-a-human-body,
.the-deeds-of-christ-prove-him, .when-the-cross-of-christ-arose,
.christ-worketh-them-not-we, .he-healed-by-the-name, and
.the-coming-of-christ-made-thee-weak).
desert.gravity.scriptural-engagement and
desert.force.martyrdom-unavailable are the two records this witness
draws its own structure from most directly.

CORRECTED, and the correction is the point of this revision. This
record previously said that this world "answers 'who was Jesus'
obliquely, through what following him is shown to require, rather than
through direct theological statement," and that the absence of direct
statement was "honestly named rather than filled." The compiled text
said the same thing in voice: "What we had of Jesus was mostly one
command." That was not honest thinness. It was an unchecked claim about
a source nobody had searched for it.

The witness was built from two loci (SS2-3 and SS19) and was the only
record in this world claiming C-I - one record answering all five of
that cell's canon questions. A full-text search of the vendored Vita
run this pass finds 23 occurrences of "Saviour", 36 of "the Word", 11
of "the Cross", and an entire division, SS72-80, in which Antony argues
the incarnation, the resurrection, and the effect of the Cross with
visiting philosophers. SS41 has him telling the devil to his face that
the coming of Christ has made him weak. SS81 has him telling emperors
that Christ alone is the true and Eternal King. None of it was in the
corpus.

What survives from the old reading is the ordering, not the exclusion:
the command really is the thing that reordered these lives, and the
argued Christology really is concentrated in one episode against a much
larger body of narrative. Both are now in `tensions` as a stated shape
rather than standing in for the whole. The bound in
desert.limit.doubt-and-doctrine was narrowed in the same pass for the
same reason.

Step4, Round 1 review Finding M14: this record was the only one of nine
doctrinal_witness records to carry a retrieval block, and it was empty
- removed for consistency with the other eight rather than populated
piecemeal for one record alone.
