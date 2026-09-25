---
id: gallic.quote.the-soldier-who-served-his-servant
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F1-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Widely Accepted
  divergence_note: >-
    The wording is Widely Accepted as Sulpitius's own text (Vita ch. II, read at its own locus for
    this record) describing Martin's years in the army before his baptism. Inferential-Thin for the
    specific claim that Martin literally cleaned his one servant's boots himself; Sulpitius did not
    witness Martin's army years and says he had his information "partly from himself... and partly
    from those who had lived with him" (Vita ch. XXV) - the same caution the host record's own
    divergence_note states for the chapters this record is drawn from.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: "Life of St. Martin ch. II (npnf211 div ii.ii.iii, file lines 727-741): Martin's conduct toward his own servant, and how his fellow-soldiers regarded him"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what Martin was like as a soldier, before the cloak or the discharge"
  - "participant asks how his fellow-soldiers regarded him"
  - "Representative needs the exact wording behind 'regarded not so much as being a soldier as a monk'"
  prefer_instead:
  - "participant wants the cloak and the vision themselves - retrieve gallic.quote.the-cloak-divided-and-the-vision-of-christ"
  - "participant wants the whole episode told as a story - retrieve gallic.story.the-cloak-at-amiens, which this record is drawn from"
text: >-
  And even to him, changing places as it were, he often acted as though, while really master, he had
  been inferior; to such a degree that, for the most part, he drew off his [servant's] boots and
  cleaned them with his own hand; while they took
  their meals together, the real master, however, generally acting the part of servant. During nearly
  three years before his baptism, he was engaged in the profession of arms, but he kept completely free
  from those vices in which that class of men become too frequently involved. He showed exceeding
  kindness towards his fellow-soldiers, and held them in wonderful affection; while his patience and
  humility surpassed what seemed possible to human nature. There is no need to praise the self-denial
  which he displayed: it was so great that, even at that date, he was regarded not so much as being a
  soldier as a monk.
speaker_or_author: "Sulpitius Severus, narrating"
license: verbatim
modern_lens_note: >-
  A modern reader may expect "he was regarded... as a monk" to describe someone withdrawn or solitary.
  Sulpitius's own evidence is the opposite: comrades, affection, a shared table, a soldier who "drew
  off his servant's boots" himself. The monastic quality the passage names is expressed entirely inside
  ordinary army life, in how one man treats a subordinate, before there is any monastery for him to
  belong to.
modern_rendering: >-
  And even toward him, it was as if the two had changed places. He was really the master, yet he often
  acted as though he were the lower one. It went so far that, most of the time, he pulled off the other
  man's boots and cleaned them with his own hand. They ate their meals together, yet the real master
  usually played the part of servant. For nearly three years before his baptism he served as a soldier.
  But he kept completely free of the vices that men of that trade too often fall into. He showed great
  kindness to his fellow soldiers and held them in remarkable affection. His patience and humility went
  beyond what seemed humanly possible. There is no need to praise the self-denial he showed. It was so
  great that, even then, people saw him less as a soldier than as a monk.
relations:
- type: associated-with
  target: gallic.story.the-cloak-at-amiens
- type: associated-with
  target: gallic.figure.martin
- type: associated-with
  target: gallic.figure.sulpitius
- type: associated-with
  target: gallic.quote.the-cloak-divided-and-the-vision-of-christ
---
Verified against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n "generally
acting the part of servant"` returns one hit, line 732; `grep -n "not so much as being a soldier as a
monk"` returns one hit, line 740. The chapter div is `<div3 title="Chapter II. Military Service of St.
Martin." ... id="ii.ii.iii">` (line 691). Read lines 727-741 directly: one continuous paragraph in the
source, nothing skipped, from "And even to him, changing places as it were..." through "...as a monk."

Normalization: line breaks joined with single spaces. "[servant's]" is kept as the source itself
brackets it (the translator's conventional marking of a word supplied for clarity, not this record's
own addition). The source's curly apostrophe is rendered as a straight one, consistent with this
world's other quote records. No word was added, dropped, substituted, or reordered.
