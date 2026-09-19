---
id: witt.quote.article-ix-of-baptism
world_id: lutheran-wittenberg-and-its-congregations
record_type: quote
schema_version: 2
status: draft
register: emic
canon_cells:
- F4-T
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Article IX of the Augsburg Confession, the same signed 1530 confession
    witt.story.diet-of-augsburg-1530 verifies. Consistent with witt.term.baptism's own attested content
    (the Large and Small Catechisms' baptism sections), read here at its own distinct locus -- the
    confessional voice's own article, not the household catechism's.
sources:
- source_id: witt.source.melanchthon-augsburg-confession
  locus: "Article IX: Of Baptism (cic:melanchthon_augsburg-confession_anon-pg275.txt lines 307-315): 'children are to be baptized who, being offered to God through Baptism are received into God's grace'"
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks whether we baptized babies, or only adults who chose it for themselves"
  do_not_retrieve_when:
  - "participant means the sacrament's general meaning apart from the age question -- retrieve the baptism term instead"
text: >-
  Of Baptism they teach that it is necessary to salvation, and that
  through Baptism is offered the grace of God, and that children are to
  be baptized who, being offered to God through Baptism are received into
  God's grace.

  They condemn the Anabaptists, who reject the baptism of children, and
  say that children are saved without Baptism.
speaker_or_author: "the Augsburg Confession, Article IX -- the same confession read before the Emperor at the 1530 Diet of Augsburg"
license: verbatim
modern_lens_note: >-
  A modern reader who has grown up around adult believer's baptism may expect a faith community to describe
  baptism chiefly as a personal decision, made once a person is old enough to choose it. That is exactly
  the position this article names and rejects -- "the Anabaptists, who reject the baptism of children" are
  named directly, as our own live boundary, not a hypothetical. Our own claim runs the other way: baptism
  is God's own act of offering grace, received here by an infant who has chosen nothing yet, which is, for
  us, the point rather than the problem -- the same claim witt.quote.article-ii-of-original-sin makes from
  the other side, that no one, of any age, is born already trusting God, and that the remedy is God's gift
  before it is anyone's own choice.
modern_rendering: >-
  We teach this: baptism is necessary for salvation. Through baptism, God offers his grace. Children
  should be baptized. A child is offered to God through baptism. By that, the child is received into
  God's grace.

  We reject what the Anabaptists teach. They say children should not be baptized. They say children are
  saved without it. We do not agree.
relations:
- type: associated-with
  target: witt.dw.a-death-begun-that-a-child-receives
---
Verified verbatim at this step (Answer-the-Canon pass, inserted between B-7a and B-8) directly against
the vendored cic/texts/melanchthon_augsburg-confession_anon-pg275.txt. `grep -n "Article IX: Of
Baptism\|children are to\|reject the baptism of children"` returns the article heading at line 307,
"through Baptism is offered the grace of God, and that children are to" at line 310, and "They condemn
the Anabaptists, who reject the baptism of children, and" at line 314. `sed -n '307,316p'` confirms the
whole article: heading at 307, the article's own teaching at 309-312 (opening "Of Baptism they teach that
it is necessary to salvation" at 309, closing "God's grace." at 312), and the condemnation at 314-315
(opening "They condemn the Anabaptists" at 314, closing "children are saved without Baptism." at 315). No
word added, dropped, substituted, or reordered.

This locus is distinct from witt.term.baptism's own citations (the Large and Small Catechisms' baptism
sections, the household's own "die Taufe" material), which do not separately name the infant-baptism
question or the Anabaptist boundary; this record verifies that specific claim at the confessional voice's
own distinct article rather than editing the existing term record. Ground for
witt.dw.a-death-begun-that-a-child-receives (F4-T: infant baptism, alongside the born-again question),
read together with witt.quote.article-ii-of-original-sin's own baptism/new-birth clause. Reciprocal
associated-with declared on that record.

CORRECTION (Phase C recon, 2026-09-19): speaker_or_author's own raw reference to
"witt.story.diet-of-augsburg-1530" replaced with plain prose ("read before the Emperor at the 1530 Diet
of Augsburg") -- caught by engine.m1.cross_world's check_quote_speaker_labels, which correctly flags this
field as one both the Level-3 citation card and the compiled prompt's quote index print verbatim to a
participant. Substance unchanged, only the internal record-id reference removed.
