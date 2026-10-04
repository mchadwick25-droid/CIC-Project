---
id: witt.quote.christs-return-to-judgment
world_id: lutheran-wittenberg-and-its-congregations
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F6-T
- F4-T
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Article XVII of the Augsburg Confession, the same signed 1530 confession
    witt.story.diet-of-augsburg-1530 verifies. This is a hard, harsh doctrinal claim (eternal punishment),
    fully the confession's own emic voice, and this record's own dw carries it plainly rather than
    softened, per this project's own rule against smoothing a contested or difficult claim into something
    gentler than the source states.
sources:
- source_id: witt.source.melanchthon-augsburg-confession
  locus: "Article XVII: Of Christ's Return to Judgment (cic:melanchthon_augsburg-confession_anon-pg275.txt lines 433-446): eternal life for the godly and elect, 'ungodly men and the devils He will condemn to be tormented without end'"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether we believed outsiders were going to hell"
  - "participant asks whether we believed only one way, out of all the world's ways, was the true one"
  - "participant asks what we believed about the end of the world, or anything like what they call the rapture"
  prefer_instead:
  - "participant wants pastoral comfort language for someone grieving -- this article states the doctrine's hard edge, not a comfort text; retrieve comfort or given-for-you instead"
text: >-
  Also they teach that at the Consummation of the World Christ will appear
  for judgment and will raise up all the dead; He will give to the godly
  and elect eternal life and everlasting joys, but ungodly men and the
  devils He will condemn to be tormented without end.

  They condemn the Anabaptists, who think that there will be an end to the
  punishments of condemned men and devils.

  They condemn also others who are now spreading certain Jewish opinions,
  that before the resurrection of the dead the godly shall take
  possession of the kingdom of the world, the ungodly being everywhere
  suppressed.
speaker_or_author: "the Augsburg Confession, Article XVII -- the same confession read before the Emperor at the 1530 Diet of Augsburg"
license: verbatim
modern_lens_note: >-
  A modern reader may want this softened, or may want us to explain it away. We do not soften it here: this
  article states, plainly, that the ungodly are condemned to be tormented without end, and it names two
  further positions -- that the punishment eventually ends, and that the godly will rule this present world
  before any resurrection -- and rejects both. What this article does NOT do, on its own words, is name
  which people count as "the ungodly," beyond the general contrast with "the godly and elect"; it is a
  judgment doctrine, not a census of who is outside. Nothing here characterizes any other living tradition,
  and nothing here should be read as this world's own answer to who specifically is saved -- that is a
  different question, argued elsewhere (witt.term.justification, witt.term.faith), not settled by this
  article's own words.
modern_rendering: >-
  We also teach that at the end of the world, Christ will appear to judge, and will raise all the dead. He
  will give the godly and the chosen eternal life and everlasting joy. But the ungodly, and the devils with
  them, he will condemn to be tormented without end.

  We reject the teaching of the Anabaptists, who think the punishment of the condemned will eventually
  stop.

  We also reject the teaching of others now spreading a view drawn from certain Jewish ideas -- that before
  the dead are raised, the godly will take over rule of this present world, with the ungodly put down
  everywhere.
relations:
- type: associated-with
  target: witt.dw.a-narrow-word-plainly-spoken
- type: associated-with
  target: witt.dw.a-death-begun-that-a-child-receives
use_note:
  means: "Augsburg Confession Article XVII (1530) teaches that Christ will raise all the dead, give the godly eternal life, condemn the ungodly to endless torment, and rejects two contrary views."
  not_for:
    - "a claim that the article names which people or traditions count as the ungodly"
    - "a claim that the article addresses the modern rapture doctrine, when it rejects only an earthly rule of the godly before the resurrection"
    - "the one-way and outsiders answer in the world's voice, which sits in witt.dw.a-narrow-word-plainly-spoken"
  years: {from: 1530, to: 1530}
  status: provisional
---
Verified verbatim at this step (Answer-the-Canon pass, inserted between B-7a and B-8) directly against
the vendored cic/texts/melanchthon_augsburg-confession_anon-pg275.txt. `grep -n "Article XVII\|tormented
without end\|Article XVIII"` returns the article heading at line 433, "devils He will condemn to be
tormented without end." at line 438, and the following Article XVIII heading at line 450 (confirming
Article XVII's own close). `sed -n '433,449p'` confirms the whole article: heading at 433, the judgment
teaching at 435-438 (opening "Also they teach that at the Consummation of the World" at 435, closing
"tormented without end." at 438), the first condemnation at 440-441, and the second condemnation at
443-446 (closing "the ungodly being everywhere suppressed." at 446). No word added, dropped, substituted,
or reordered.

This is the harshest single passage cited in this world's whole store as of this authoring pass, and it
is carried in full, unsoftened, per this project's own accessible-and-rigorous discipline against
flattening a hard claim into something gentler than the source states. Ground for
witt.dw.a-narrow-word-plainly-spoken (F6-T: outsiders and hell, one way among many) and, via its own
opening clause ("at the Consummation of the World Christ will appear for judgment"), for
witt.dw.a-death-begun-that-a-child-receives (F4-T: the end of the world question, alongside infant
baptism). Reciprocal associated-with declared on both.
