---
id: syr.quote.warned-before-baptism
world_id: syriac-edessa-nisibis
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-T
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Aphrahat's own instruction in Hallock's English, both halves read directly in the vendored file. Hallock's transcription carries in-line markers ('~1~' for a footnote, '~' for a space) which are not reproduced; the translator's parenthetical glosses and his '(wishing to. become)' typo are kept as they stand. THIS IS A LOCUS CORRECTION: syr.dw.born-again-endtimes cites Demonstration VI for 'the second birth; the Spirit received in baptism', and VI (Of Monks) does not carry it. It stands in VII, in this world's other vendored Aphrahat file.
sources:
- source_id: syr.source.aphrahat-demonstrations-hallock
  locus: >-
    Demonstration VII (On Penitents), sec. 20 (cic/texts/aphrahat_demonstrations-2-7_hallock1932.txt)
  license: public-domain
text: >-
  For this reason it is fitting for the sounders of trumpets, the preachers of the Church, to warn all (who are in) the covenant of God before baptism, and to those who choose for themselves virginity and holiness, young men and virgins and those (wishing to. become) holy; and for the preachers to warn them and say: "He who sets his heart upon the natural state of fellowship (i.e.~in matrimony), let him become united before baptism lest, perhaps, he fall in the conflict and be killed. And he who is afraid of this part of the struggle let him turn back lest, perhaps, he break the heart of his brethren as well as his own heart. And he who loves possessions let him turn back from the army lest, perhaps, when the battle shall prevail against him he should remember his possessions and turn back to them, for there is disgrace to him who turns back from the conflict".
modern_rendering: >-
  For this reason it is right for the preachers of the Church - the ones who
  sound the trumpet - to warn everyone in God's covenant before baptism: those
  who choose for themselves virginity and holiness, the young men and the
  virgins, and those wishing to become holy. The preachers are to warn them
  and say this. If your heart is set on marriage, then marry before your
  baptism. Otherwise you may fall in the fight and be killed. And if you are
  afraid of this part of the fight, turn back now, so that you do not break
  your brothers' hearts along with your own. And if you love your
  possessions, turn back from the army too - or else, when the battle grows
  fierce, you may remember what you own and retreat to save it, and that is
  a disgrace.
speaker_or_author: Aphrahat, Demonstration VII.20
license: verbatim
modern_lens_note: >-
  This settles the infant-baptism question by making it unaskable: nobody warned here is a baby. A herald stands up before the baptism and tells the candidates that anyone who wants marriage should marry FIRST, anyone frightened should withdraw now, and anyone attached to property should leave the line - and says it is no disgrace to turn back before enlisting, only after. Baptism is being described as enlistment, with the whole passage built on Gideon sending the fearful home. So 'were you born again' would land oddly: the decisive moment is a public choice with a cost stated in advance and an exit offered, which is nearer to taking vows than to a conversion experience.
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks whether babies were baptised or only adults who chose it"
  - "participant asks what baptism actually required of a person here"
  - "participant asks whether they would call what happened to them being born again"
relations:
- type: associated-with
  target: syr.dw.born-again-endtimes
---
Opened 2026-08-27 for F4-T, the second of two for this cell, and a locus corrected rather than
copied. syr.dw.born-again-endtimes cites Demonstration VI twice for the baptism material; VI is Of
Monks and carries the covenant teaching, not this. The passage the record describes is at VII.20, in
syr.source.aphrahat-demonstrations-hallock - a source this world already holds and this record was not
citing.

Quote-verbatim gate fix (2026-09-22): the record's own quotation opened with a quote mark it never
closed, silently dropping the third parallel clause of the preachers' own warning ("And he who loves
possessions let him turn back...") - the exact clause modern_lens_note below already describes
("anyone attached to property should leave the line"). Restored through the source's own closing
quotation mark; modern_rendering extended to match. The record still cannot verify past "God" earlier
in the same sentence: the source's own footnote marker there ("God~1~before") uses this edition's
tilde convention (disclosed above), which the gate doesn't currently strip - flagged for Mark alongside
the other footnote/pagination-apparatus findings in this PR.

MODERN RENDERING AUTHORED (2026-08-29, syr register pass; Mark's standing quote ruling 2026-08-28: spoken form is a modern-English translation, not a summary - the original wording stays as this record's text and is shown at Level 3). Rendered from this record's own text field only; nothing added from the source beyond it.

BAR SWEEP (2026-08-29, Mark: "much better thats the bar" - see Ministry/Technology/CiC_Register_Bar_2026-08-29.md): rendering rewritten to the approved sample's level - short sentences, everyday words, translation fidelity kept; original stays as text for Level 3.
