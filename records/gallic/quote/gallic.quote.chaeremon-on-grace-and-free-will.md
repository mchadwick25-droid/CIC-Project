---
id: gallic.quote.chaeremon-on-grace-and-free-will
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
    Documented as Cassian's own text (Conferences XIII.13 and XIII.18, read at their loci for this
    record). Widely Accepted as Cassian's report of Chaeremon's teaching; its doctrinal content is
    Contested [CT] for its meaning relative to Augustine and for the fairness of the label
    "semi-Pelagian" - the same caveat carried by this quote's companion record,
    gallic.quote.germanus-and-chaeremon-on-the-husbandman, and neither depended on nor resolved here.
sources:
- source_id: gallic.source.cassian-conferences-part-ii
  locus: "Conferences XIII.13 and XIII.18 (npnf211 divs iv.v.iv.xiii and iv.v.iv.xviii, file lines 38200-38202 and 38622-38624): two summary statements later in the same Conference, on grace co-operating with the will, and on how the two relate"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how this world held together grace and free will, without collapsing either one"
  - "participant asks whether the monks thought they had any real say in their own good actions"
  prefer_instead:
  - "participant wants the argument's origin and the husbandman analogy - retrieve gallic.quote.germanus-and-chaeremon-on-the-husbandman"
  - "participant wants the doctrine argued at full theological depth - retrieve gallic.term.grace, gallic.term.free-will"
text: >-
  And so the grace of God always co-operates with our will for its advantage, and in all things assists,
  protects, and defends it ... for how God works all things in us and yet everything can be ascribed to
  free will, cannot be fully grasped by the mind and reason of man.
speaker_or_author: "Abbot Chaeremon, as Cassian records him (Conference XIII.13, XIII.18)"
license: verbatim
modern_lens_note: >-
  Chaeremon does not resolve the tension between grace and free will; he names it as a limit. Grace
  "co-operates with our will" rather than replacing it, and yet how the two fit together, he says
  directly, "cannot be fully grasped by the mind and reason of man." The teaching ends in an admitted
  limit to understanding, not a formula that settles the question.
modern_rendering: >-
  And so the grace of God always works together with our will for its good. In all things it helps,
  protects, and defends our will ... For the human mind and reason cannot fully grasp how God works all
  things in us, and yet everything can be credited to free will.
relations:
- type: associated-with
  target: gallic.story.germanus-scruple-at-morning-service
---
Verified verbatim directly against the vendored
cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n "co-operates with our will"`
returns one hit, line 38201, inside `<div4 title="Chapter XIII. How human efforts cannot be set against
the grace of God." ... id="iv.v.iv.xiii">` (line 38193). `grep -n "cannot be fully grasped by the mind"`
returns one hit, line 38624, inside the same Conference's Chapter XVIII (`id="iv.v.iv.xviii"`, confirmed by
the surrounding "it is laid down by all the Catholic fathers" at line 38602).

The `text` field joins two sentences from these two, non-adjacent chapters with one ellipsis marking the
real gap between them (roughly 400 lines of further teaching, not flagged in the host record and not
carried here). The first sentence, `sed -n '38200,38202p'`, opens "And so the grace of God..."; the second,
`sed -n '38622,38624p'`, closes "...cannot be fully grasped by the mind and reason of man." Normalization:
hard-wrapped lines joined with single spaces. No word was added, dropped, substituted, or reordered within
either kept sentence.

speaker_or_author is a plain string, not a figure id: no gallic.figure record exists for Chaeremon, and
these are his words as Cassian gives them, not Cassian's own.
