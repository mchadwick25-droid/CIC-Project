---
id: gallic.quote.chaeremon-three-stages-of-grace
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F1-I
- F1-T
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Widely Accepted
  divergence_note: >-
    Documented as Cassian's own text (Conference XIII.18, read at its locus for this record). Widely
    Accepted as Cassian's report of Chaeremon's teaching; its doctrinal content is Contested [CT] for
    its meaning relative to Augustine and for the fairness of the label "semi-Pelagian" - the same
    caveat carried by this quote's companion records, gallic.quote.germanus-and-chaeremon-on-the-
    husbandman and gallic.quote.chaeremon-grace-requires-our-effort, and neither depended on nor
    resolved here. This record carries the three-stage teaching on its own, independently verified;
    Conference XIII.13's separate teaching, roughly 400 lines earlier in the same Conference, stands on
    its own in gallic.quote.chaeremon-grace-requires-our-effort, and the source does not connect the two
    passages to each other.
sources:
- source_id: gallic.source.cassian-conferences-part-ii
  locus: "Conference XIII.18 (npnf211 div iv.v.iv.xviii, file lines 38601-38624): Chaeremon's three-stage account of the Divine gift - inflaming the desire for good, enabling the practice of virtue, and preserving what is gained, each without destroying free will - and his statement that how grace and free will fit together cannot be fully grasped by the mind and reason of man"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how this world divided grace's work from the will's own part, stage by stage"
  - "participant asks whether the monks thought they had any real say in their own good actions"
  prefer_instead:
  - "participant wants the earlier statement that grace still asks something of the will in return - retrieve gallic.quote.chaeremon-grace-requires-our-effort"
  - "participant wants the argument's origin and the husbandman analogy - retrieve gallic.quote.germanus-and-chaeremon-on-the-husbandman"
  - "participant wants the doctrine argued at full theological depth - retrieve gallic.term.grace, gallic.term.free-will"
text: >-
  And therefore it is laid down by all the Catholic fathers who have taught perfection of heart not by
  empty disputes of words, but in deed and act, that the first stage in the Divine gift is for each man
  to be inflamed with the desire of everything that is good, but in such a way that the choice of free
  will is open to either side: and that the second stage in Divine grace is for the aforesaid practices
  of virtue to be able to be performed, but in such a way that the possibilities of the will are not
  destroyed: the third stage also belongs to the gifts of God, so that it may be held by the persistence
  of the goodness already acquired, and in such a way that the liberty may not be surrendered and
  experience bondage. For the God of all must be held to work in all, so as to incite, protect, and
  strengthen, but not to take away the freedom of the will which He Himself has once given. If however
  any more subtle inference of man's argumentation and reasoning seems opposed to this interpretation, it
  should be avoided rather than brought forward to the destruction of the faith (for we gain not faith
  from understanding, but understanding from faith, as it is written: "Except ye believe, ye will not
  understand" ) for how God works all things in us and yet everything can be ascribed to free will, cannot
  be fully grasped by the mind and reason of man.
speaker_or_author: "Abbot Chaeremon, as Cassian records him (Conference XIII.18)"
license: verbatim
modern_lens_note: >-
  Chaeremon does not resolve the tension between grace and free will here; he names it as a limit. He
  lays out three stages - grace kindles the desire for good, grace makes the practice of virtue possible,
  grace holds what has been gained - and insists at each stage that free will is never destroyed or taken
  away by it. Yet how the two actually fit together, he says directly, "cannot be fully grasped by the
  mind and reason of man." The teaching ends in an admitted limit to understanding, not a formula that
  settles the question, and it warns against trusting "subtle inference" over what "all the Catholic
  fathers" have taught in practice.
modern_rendering: >-
  And so all the Catholic fathers have laid this down. They taught perfection of heart not by empty
  arguments over words, but in deed and action. The first stage of God's gift is that each person is set
  on fire with desire for everything good. But the choice of free will stays open to either side. The
  second stage of God's grace is the power to carry out those practices of virtue. But what the will is
  able to do is not destroyed. The third stage also belongs to God's gifts, so that it may be held
  by the persistence of the goodness already gained. But freedom is not handed over, and it does not fall into
  slavery. For the God of all must be understood to work in all. He works to stir up, protect, and
  strengthen. But he does not take away the freedom of the will that he himself once gave. Some more
  subtle conclusion of human argument and reasoning may seem to oppose this view. If so, it should be
  avoided, not brought forward to destroy the faith. (For we do not gain faith from understanding. We gain
  understanding from faith, as it is written: "Unless you believe, you will not understand.") For the
  human mind and reason cannot fully grasp how God works all things in us, and yet everything can be
  credited to free will.
relations:
- type: associated-with
  target: gallic.story.germanus-scruple-at-morning-service
- type: associated-with
  target: gallic.gravity.egypt-as-measure
- type: associated-with
  target: gallic.gravity.grace-and-effort
use_note:
  means: "Cassian reports Chaeremon teaching that grace kindles desire, enables virtue and preserves it without destroying free will, and that their union exceeds human reason."
  not_for:
    - "a settled verdict that the teaching is semi-Pelagian, when that label is contested"
    - "the claim that grace looks for human effort, which sits in gallic.quote.chaeremon-grace-requires-our-effort"
    - "a complete theory of how grace and free will fit together, when Chaeremon calls that beyond human grasp"
    - "a statement on infants or guilt inherited from birth, which this passage does not contain"
  years: {from: 426, to: 426}
  status: reviewed
---
Verified verbatim directly against the vendored
cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n "cannot be fully grasped by the
mind"` returns one hit, line 38624, inside `<div4 title="Chapter XVIII. The decision of the fathers that
free will is not equal to save a man." ... id="iv.v.iv.xviii">` (line 38564). `grep -n "And therefore\s*$"`
at line 38601 (closing the previous chapter's own Ezekiel citation) opens the sentence this record's `text`
begins with, `sed -n '38601,38624p'`: "And therefore it is laid down by all the Catholic fathers ...
cannot be fully grasped by the mind and reason of man." - three sentences (the three-stage teaching, the
sentence on God working in all without destroying free will, and the sentence on subtle inference and the
final admitted limit), read through to their own shared period, not cut mid-thought.

The `text` field carries a literal space between the closing quotation mark and the closing parenthesis
("understand" )" rather than "understand")") - not a difference from the source's own words, but the
space the fleet's quote-verbatim tooling itself leaves when it strips the translator's endnote (below)
out of the running text before matching; the gate's own `gate_quote_verbatim` run confirmed this record
verifies with this space present and fails without it. No word was added, dropped, substituted, or
reordered.

A translator's endnote (`<note n="1864" ...>`, citing Isaiah vii. 9) sits inside the source's own
parenthetical, between "understand" and the closing paren; it is apparatus, not Chaeremon's words, and is
excluded exactly as the fleet's quote-verbatim tooling strips every `<note>` block before matching.
Normalization: hard-wrapped lines (including one page-break tag, `<pb n="435" .../>`, falling mid-word-
run between "subtle" and "inference of") joined with single spaces; the source's curly quotation marks
around "Except ye believe, ye will not understand" are rendered here as straight double quotes, the same
mark in a different Unicode form. No word was added, dropped, substituted, or reordered.

This record carries the passage on its own, independently verified, joined to nothing. Conference
XIII.13's own, separate sentence is carried on its own in gallic.quote.chaeremon-grace-requires-our-effort,
not joined to this one - the two are two summary statements roughly 400 lines apart in the same
Conference, not one continuous argument.

speaker_or_author is a plain string, not a figure id: no gallic.figure record exists for Chaeremon, and
these are his words as Cassian gives them, not Cassian's own.

modern_rendering: authored against the verbatim `text`, then independently checked clause by clause in a
separate pass - every clause of all three sentences accounted for (the three stages, the sentence on God
working in all without destroying free will, and the sentence on subtle inference, the nested Scripture
quotation, and the final admitted limit), nothing added, no misleading modern sense, each sentence at or
under roughly 25 words. No bracketed span appears in this quote's `text`, so the bracket-voicing rule
for finishing a true ellipsis does not arise here.
