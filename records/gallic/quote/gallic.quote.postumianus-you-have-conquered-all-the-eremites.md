---
id: gallic.quote.postumianus-you-have-conquered-all-the-eremites
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: >-
    Documented as Sulpitius's own text (Dialogues II.5, read at its locus for this record) - a
    character's direct speech inside the Dialogues, not an independent report about Postumianus.
sources:
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: "Dialogues II.5 (npnf211 div ii.iv.ii.v, file lines 4100-4108): Postumianus conceding,
    to Gallus, that Martin outdoes every hermit and anchorite of the East"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks for the Dialogues' own comparative claim, in a character's own voice"
  - "participant asks whether the north's comparison with Egypt was one-sided"
  prefer_instead:
  - "participant wants the fuller comparative claim, extended all the way to Egypt itself - retrieve gallic.quote.europe-will-not-yield-having-only-martin"
text: >-
  You have conquered, although certainly not me, who am, on the
  contrary, an upholder of Martin, and who have always known and
  believed all these things about that man; but you have conquered
  all the eremites and anchorites.
speaker_or_author: "Postumianus, in Sulpitius's Dialogues"
license: verbatim
modern_lens_note: >-
  Postumianus, the Dialogues' own traveler just back from Egypt, concedes the comparison himself -
  he is not being argued into it, and he says plainly he already believed it before hearing
  Gallus's stories. The concession is staged as willing, not won.
modern_rendering: >-
  You have conquered - though certainly not me. On the contrary, I am a supporter of Martin. I
  have always known and believed all these things about that man. But you have conquered all the
  hermits and anchorites.
relations:
- type: associated-with
  target: gallic.gravity.egypt-as-measure
use_note:
  means: "Postumianus, a speaker in Sulpitius's Dialogues, concedes to Gallus that Martin has outdone all the hermits and anchorites of the East."
  not_for:
    - "an independent traveller's judgment, when the speech belongs to Sulpitius's literary dialogue"
    - "a measured comparison of Gaul and Egypt rather than partisan praise of Martin"
    - "the claim that Europe needs only Martin, which sits in gallic.quote.europe-will-not-yield-having-only-martin"
  years: {from: 404, to: 406}
  status: reviewed
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"all the eremites and anchorites"` returns line 4107. Read with `sed -n '4100,4108p'`, inside
`<div4 ... id="ii.iv.ii.v">` (Chapter V). Postumianus's speech in the source is interrupted mid-
sentence by the narrator's own tag - `"You have conquered, O Gaul," said Postumianus, "you have
conquered, although certainly not me, ..."` - so a `text` field that read straight through both
halves as one continuous quotation would silently splice across that interruption, a real
difference `engine.m1.quote_verbatim` correctly refuses to pass. This record's `text` field
therefore begins after the interruption, at the second, continuous half of the speech ("you have
conquered, although certainly not me..." through "...all the eremites and anchorites."), rather
than joining across "said Postumianus" or force-fitting an ellipsis where the source has a real
narrator tag, not an elision. The dropped opening clause ("You have conquered, O Gaul, you have
conquered,") is not load-bearing on its own - the record's own load-bearing claim ("you have
conquered all the eremites and anchorites") is carried whole.

Normalization: the source's curly quotation marks opening and closing the speech are dropped, the
edition's own punctuation marking speech, not part of the quoted prose; the first word ("you") is
capitalized here to open the record's own `text` field, a case difference
`engine.m1.quote_verbatim` tolerates (a quote opening mid-sentence, capitalized to open a sentence
here). No word was added, dropped, substituted, or reordered within the quoted span itself.

speaker_or_author is a plain string: no gallic.figure record exists for Postumianus.