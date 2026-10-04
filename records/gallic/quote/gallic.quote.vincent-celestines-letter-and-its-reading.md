---
id: gallic.quote.vincent-celestines-letter-and-its-reading
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Vincent's own text (Commonitory ch. 32 [85], read at its locus for this record) -
    his own quotation of Pope Celestine's letter and his own reading of it. Whether this reading
    shows Vincent held the Massilian position is Contested (carried in the host record's own
    divergence_note), but the wording itself, and that Vincent reads it this way, is Documented.
sources:
- source_id: gallic.source.vincent-commonitory
  locus: "ch. 32 [85] (npnf211 div iii.xxxiii, file lines 14615-14631): Vincent's own quotation of
    Pope Celestine's letter and his reading of its final clause"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what Pope Celestine actually wrote, in Vincent's own quotation of it"
  - "participant asks how Vincent read Celestine's letter for his own side of an argument"
  prefer_instead:
  - "participant wants the letter's own original addressees and direction, from the volume's own editorial note - retrieve gallic.quote.heurtley-celestines-letter-addressed-to-gaul"
text: >-
  Holy Pope Celestine also expresses himself in like manner and to the
  same effect. For in the Epistle which he wrote to the priests of
  Gaul, charging them with connivance with error, in that by their
  silence they failed in their duty to the ancient faith, and allowed
  profane novelties to spring up, he says: "We are deservedly to blame
  if we encourage error by silence. Therefore rebuke these people.
  Restrain their liberty of preaching." But here some one may doubt who
  they are whose liberty to preach as they list he forbids,—the
  preachers of antiquity or the devisers of novelty. Let himself tell
  us; let himself resolve the reader's doubt. For he goes on: "If the
  case be so (that is, if the case be so as certain persons complain to
  me touching your cities and provinces, that by your hurtful
  dissimulation you cause them to consent to certain novelties), if the
  case be so, let novelty cease to assail antiquity." This, then, was
  the sentence of blessed Celestine, not that antiquity should cease to
  subvert novelty, but that novelty should cease to assail antiquity.
speaker_or_author: "Vincent of Lérins, quoting Pope Celestine's letter"
license: verbatim
modern_lens_note: >-
  Vincent does not just quote Celestine - he stops to settle, in his own voice, which side the
  letter is against. His own question ("who they are whose liberty to preach... he forbids") and
  his own answer are part of the passage, not added by this record. His closing line states his own
  reading as a fact: novelty, not antiquity, is the one Celestine's letter silences.
modern_rendering: >-
  Holy Pope Celestine also speaks in the same way and with the same meaning. He wrote a letter to
  the priests of Gaul, charging them with turning a blind eye to error. By keeping silent, they had
  failed in their duty to the ancient faith and let unholy novelties spring up. In that letter he
  says: "We deserve blame if we encourage error by our silence. So rebuke these people. Restrain
  their freedom to preach." But here someone may be unsure whom he means. Whose freedom to preach as
  they please is he forbidding: the preachers of antiquity, or the inventors of novelty? Let him
  tell us himself. Let him settle the reader's doubt himself. For he goes on: "Certain people
  complain to me about your cities and provinces. They say that by your harmful pretence you lead
  them to agree to certain novelties. If this is the case, that is, if it is as they complain, if
  this is the case, let novelty stop attacking antiquity." This, then, was blessed Celestine's
  ruling: not that antiquity should stop overturning novelty, but that novelty should stop attacking
  antiquity.
relations:
- type: associated-with
  target: gallic.force.contest-over-antiquity
- type: associated-with
  target: gallic.force.africa-and-rome-pressure
use_note:
  means: "Vincent quotes Pope Celestine's letter rebuking the priests of Gaul and reads it as silencing novelty rather than antiquity."
  not_for:
    - "a settled finding that Vincent held the Massilian position, which is contested"
    - "Celestine's own interpretation rather than Vincent's reading of the letter"
    - "Pope Stephen's rule, which sits in gallic.quote.pope-stephen-no-innovation"
  years: {from: 434, to: 434}
  status: provisional
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"85\.\] Holy Pope Celestine"` returns line 14615; read with `sed -n '14614,14632p'`, inside `<div2
title="Chapter XXXII..." id="iii.xxxiii">`. The quoted span is one continuous paragraph
(`<p id="iii.xxxiii-p5">`), from "Holy Pope Celestine also expresses himself..." through "...novelty
should cease to assail antiquity.", ending at its own period, immediately before a translator's
endnote citing the letter's location in the Benedictine edition. Vincent's own rhetorical
question-and-answer ("But here some one may doubt...let himself resolve the reader's doubt") sits
inside this same paragraph, with no paragraph break, and is carried whole rather than narrowed
around it - it is Vincent's own connective argument, not an unrelated interruption.

Normalization: line breaks joined with single spaces; the source's own curly quotation marks around
Celestine's two quoted sentences are rendered here as straight double quotes, the same marks in a
different Unicode form - these are Celestine's own words quoted inside Vincent's sentence, not this
record's own added structure. No word was added, dropped, substituted, or reordered.
