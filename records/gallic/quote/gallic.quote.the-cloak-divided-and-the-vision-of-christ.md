---
id: gallic.quote.the-cloak-divided-and-the-vision-of-christ
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
  formation_confidence: Contested
  divergence_note: >-
    Contested for the narrated event and the vision that follows it - the whole tradition's claim
    about Martin's youth, corroborated by no independent witness inside this world's own Native corpus,
    matching the host record's own divergence_note. The wording itself is Widely Accepted as Sulpitius's
    text (Vita ch. III, read at its own locus for this record). "At the gate of the city" omits the
    translation's own "of Amiens" - a translator's rendering of Sulpitius's Latin "Ambianensium civitas"
    that this world's own No-Tier-5 audit (Doc_09 §4) treats as editorial rather than Sulpitius's own
    word, matching the host record's own established treatment of the same place-name.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: "Life of St. Martin ch. III (npnf211 div ii.ii.iv, file lines 766-805): the beggar at the gate, the division of the cloak, and Martin's vision of Christ"
  license: public-domain
- source_id: gallic.source.npnf-editorial-apparatus
  locus: 'Roberts''s footnote identifying "Ambianensium civitas" with the modern Amiens - editorial, named as such, not adopted into this record''s text'
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks for Sulpitius's own words for Martin's most famous act"
  - "participant asks exactly what Christ said in the vision, or what the surrounding angels heard"
  - "Representative needs the precise wording tying the beggar's cloak to Matt. xxv. 40"
  prefer_instead:
  - "participant wants Martin's conduct as a soldier before this scene - retrieve gallic.quote.the-soldier-who-served-his-servant"
  - "participant is asking whether the vision 'really happened' - this record carries Tier 3 register and does not assess that"
  - "participant wants the whole episode told as a story - retrieve gallic.story.the-cloak-at-amiens, which this record is drawn from"
text: >-
  Accordingly, at a certain period, when he had nothing except his arms and his simple military dress,
  in the middle of winter, a winter which had shown itself more severe than ordinary, so that the
  extreme cold was proving fatal to many, he happened to meet at the gate of the city ... a poor man
  destitute of clothing. He was entreating those that passed by to have compassion upon him, but all
  passed the wretched man without notice, when Martin, that man full of God, recognized that a being to
  whom others showed no pity, was, in that respect, left to him. Yet, what should he do? He had nothing
  except the cloak in which he was clad, for he had already parted with the rest of his garments for
  similar purposes. Taking, therefore, his sword with which he was girt, he divided his cloak into two
  equal parts, and gave one part to the poor man, while he again clothed himself with the remainder.
  Upon this, some of the by-standers laughed, because he was now an unsightly object, and stood out as
  but partly dressed. Many, however, who were of sounder understanding, groaned deeply because they
  themselves had done nothing similar. They especially felt this, because, being possessed of more than
  Martin, they could have clothed the poor man without reducing themselves to nakedness. In the
  following night, when Martin had resigned himself to sleep, he had a vision of Christ arrayed in that
  part of his cloak with which he had clothed the poor man. He contemplated the Lord with the greatest
  attention, and was told to own as his the robe which he had given. Ere long, he heard Jesus saying
  with a clear voice to the multitude of angels standing round: "Martin, who is still but a catechumen,
  clothed me with this robe." The Lord, truly mindful of his own words (who had said when on earth:
  "Inasmuch as ye have done these things to one of the least of these, ye have done them unto me"),
  declared that he himself had been clothed in that poor man.
speaker_or_author: "Sulpitius Severus, narrating Martin's vision, in which Christ speaks the two quoted lines"
license: verbatim
modern_lens_note: >-
  A modern reader is likely to know this story as an act of charity confirmed by a private, comforting
  vision. Sulpitius's own emphasis is sharper: Christ does not thank Martin, he identifies himself with
  the beggar outright - "clothed me with this robe" - and grounds that claim in his own earlier words,
  quoted a second time inside the vision itself. The cloak is the act; the vision is Christ attaching
  his own name to the man who received it.
modern_rendering: >-
  So, at one time, he had nothing but his weapons and his plain soldier's clothes. It was the middle
  of winter, a winter harsher than usual, and the bitter cold was killing many people. He happened to
  meet at the gate of the city ... a poor man with nothing to wear. The man was begging passers-by to
  take pity on him, but everyone walked past the wretched man without a glance. Then Martin, that man
  full of God, saw that this man, shown no pity by the others, had been left to him. But what should
  he do? He had nothing except the cloak he wore, for he had already given away the rest of his
  clothes for the same kind of need. So he drew the sword at his side and cut his cloak into two equal
  halves. He gave one half to the poor man and wrapped himself again in the rest. At this, some of the
  bystanders laughed, because he now looked unsightly and stood out as only half-dressed. But many
  with better sense groaned deeply, because they themselves had done nothing like it. They felt this
  most of all because they had more than Martin. They could have clothed the poor man without
  stripping themselves bare. The next night, when Martin had given himself up to sleep, he had a
  vision. He saw Christ dressed in the half of his cloak that he had given the poor man. He gazed at
  the Lord with the closest attention, and was told to own as his the cloak he had given away. Soon he
  heard Jesus say in a clear voice to the crowd of angels standing around: "Martin, who is still only
  a catechumen, clothed me with this cloak." The Lord truly remembered his own words. On earth he had
  said: "When you did these things to one of the least of these, you did them to me." He declared that
  he himself had been clothed in that poor man.
relations:
- type: associated-with
  target: gallic.story.the-cloak-at-amiens
- type: associated-with
  target: gallic.figure.martin
- type: associated-with
  target: gallic.figure.sulpitius
- type: associated-with
  target: gallic.quote.the-soldier-who-served-his-servant
---
Verified against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n "meet at the
gate of the city"` returns one hit, line 770; `grep -n "clothed me with this robe"` returns one hit,
line 794; `grep -n "Inasmuch"` returns one hit, line 796 (in this chapter). The chapter div is `<div3
title="Chapter III. Christ appears to St. Martin." ... id="ii.ii.iv">` (line 760). Read lines 766-805
directly: one continuous passage, from "Accordingly, at a certain period..." through "...clothed in
that poor man."

The ellipsis after "the gate of the city" marks the omission of "of Amiens," the translation's own
rendering of "Ambianensium civitas" - present in the main translated text, not only in the footnote,
but treated here as the translator's identification rather than Sulpitius's own word, matching this
world's existing treatment of the same place-name in gallic.story.the-cloak-at-amiens's own trailer
(the No-Tier-5 audit rule that no editorial place-name enters narrative as the source's own word).

Normalization: line breaks joined with single spaces. The source marks the two spoken lines with a dash
before an opening curly quotation mark; the first is closed with a curly closing mark, the second is
not closed in the source at all before the sentence continues into "), declared that..." - both are
rendered here as normal, properly-paired quotations, the mechanical presentation of the marks rather
than the words being what is normalized, consistent with this world's existing quote record for the
same author (gallic.quote.martin-on-the-christ-with-wounds). No word was added, dropped, substituted,
or reordered.
