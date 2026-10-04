---
id: gallic.quote.augustine-in-darkness-on-predestination
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted as the outside report's own wording, read directly at its locus for this
    record - Augustine's own description of the brethren's state, not this world's own voice.
    Carried here only to show what the outside report actually said, distinct from what the world
    itself held (Conf. XIII).
sources:
- source_id: gallic.source.augustine-on-predestination
  locus: "ch. 2 (npnf105 div xxi.ii.ii, file line 20836): Augustine's own description of the
    Massilian brethren's state on the question of predestination"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks what Augustine himself said about the brethren in Gaul, not what the world said about itself"
  - "participant wants the outside report's own wording, distinct from Cassian's own Conference XIII"
  prefer_instead:
  - "participant wants the world's own position on grace and effort - retrieve gallic.quote.grievous-blasphemy-not-all-men-to-be-saved or gallic.quote.not-i-but-the-grace-of-god-with-me"
text: >-
  For as yet they are in darkness on the question concerning the
  predestination of the saints, but they have that whence, "if in
  anything they are otherwise minded, God will reveal even this unto
  them," if they are walking in that to which they have attained.
speaker_or_author: "Augustine of Hippo, On the Predestination of the Saints"
license: verbatim
modern_lens_note: >-
  This is Augustine's own report about the brethren in Gaul, not their own voice - the world's own
  text (Conf. XIII) never answers Augustine by name and never uses this language about itself. The
  nested quotation inside this sentence is Augustine's own citation of Philippians, not a second
  layer of the world's own speech.
modern_rendering: >-
  They are still in darkness on the question of the predestination of the saints. But they already
  have grounds for this promise to apply to them: "if in anything they think differently, God will
  reveal even this to them." The promise holds if they are walking in what they have already
  reached.
relations:
- type: associated-with
  target: gallic.force.africa-and-rome-pressure
use_note:
  means: "Augustine writes in On the Predestination of the Saints that the Massilian brethren are still in darkness on predestination but may yet be shown the truth."
  not_for:
    - "the Gallic monks' own voice or self-description, when it is an outside African report"
    - "Chaeremon's teaching on grace, which sits in gallic.quote.chaeremon-three-stages-of-grace"
    - "a condemnation of the brethren as heretics"
  years: {from: 428, to: 429}
  status: reviewed
---
Verified directly against cic/texts/npnf105_augustine-anti-pelagian-writings.xml. `grep -n "For as
yet they are in darkness"` returns line 20836; read with `sed -n '20828,20838p'`, inside `<div3
type="Chapter" title="To What Extent the Massilians Withdraw from the Pelagians." ... id="xxi.ii.ii">`
(A Treatise on the Predestination of the Saints, ch. 2). The quoted span is one complete sentence,
"For as yet they are in darkness..." through "...to which they have attained.", ending at its own
period; the nested quotation inside it ("if in anything...unto them") is Augustine's own citation of
Phil. iii. 15, carried whole as part of his sentence, not narrowed around.

Normalization: line breaks joined with single spaces; the source's own curly quotation marks around
the nested citation are rendered here as straight double quotes, the same marks in a different
Unicode form. No word was added, dropped, substituted, or reordered.
