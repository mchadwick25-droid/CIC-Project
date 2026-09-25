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
    text (Vita ch. III, read at its own locus for this record). "The city of Amiens" is Roberts's own
    main-text rendering of Sulpitius's Latin "Ambianensium civitas," quoted here as part of that main
    text - the endnote at this point only glosses the underlying Latin and an alternate ancient name
    ("Samarobriva"); it does not mark "Amiens" itself as editorial or absent from the translation's own
    sentence, matching the host record's own corrected treatment of the same place-name.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: "Life of St. Martin ch. III (npnf211 div ii.ii.iv, file lines 766-805): the beggar at the gate, the division of the cloak, and Martin's vision of Christ"
  license: public-domain
- source_id: gallic.source.npnf-editorial-apparatus
  locus: 'Roberts''s footnote glossing "Ambianensium civitas" (Sulpitius''s Latin) and its alternate ancient name "Samarobriva" - editorial, named as such, not the source of the "Amiens" wording, which comes from the main translated text itself'
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
  extreme cold was proving fatal to many, he happened to meet at the gate of the city of Amiens a poor
  man destitute of clothing. He was entreating those that passed by to have compassion upon him, but all
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
  with a clear voice to the multitude of angels standing round—"Martin, who is still but a catechumen,
  clothed me with this robe." The Lord, truly mindful of his own words (who had said when on
  earth—"Inasmuch as ye have done these things to one of the least of these, ye have done them unto me),
  declared that he himself had been clothed in that poor man;
speaker_or_author: "Sulpitius Severus, narrating Martin's vision, in which Christ speaks the two quoted lines"
license: verbatim
modern_lens_note: >-
  A modern reader is likely to know this story as an act of charity confirmed by a private, comforting
  vision. Sulpitius's own emphasis is sharper: Christ does not thank Martin, he identifies himself with
  the beggar outright - "clothed me with this robe" - and grounds that claim in his own earlier words,
  quoted a second time inside the vision itself. The cloak is the act; the vision is Christ attaching
  his own name to the man who received it.
modern_rendering: >-
  At one point, he owned nothing but his weapons and his plain soldier's uniform. It was midwinter,
  and that winter was harsher than usual - the bitter cold was killing people. At the gate of the city
  of Amiens, he met a poor man who had no clothes at all. The man was begging everyone who passed to
  take pity on him, but they all walked by without a glance. Martin, that man full of God, realized
  that since no one else showed the man pity, this one was left for him to help. But what could he
  do? He had nothing left but the cloak on his back. He had already given the rest of his clothes away
  for the same kind of need. So he drew the sword at his belt and cut his cloak into two equal halves.
  He gave one half to the poor man, and put the other half back on himself. Some of the bystanders
  laughed at this, because he now looked ridiculous, only half dressed. But many with better judgment
  groaned deeply, because they had done nothing like it themselves. This stung most because they owned
  more than Martin did - they could have clothed the poor man without leaving themselves bare. The
  following night, once Martin had fallen asleep, he had a vision. He saw Christ wearing the half of
  his cloak that he had given the poor man. He studied the Lord closely. He was told to recognize the
  cloak he had given away as his own. Soon he heard Jesus say, in a clear voice, to the crowd of
  angels standing around him: "Martin, who is still only a candidate for baptism, clothed me with this
  robe." The Lord truly remembered his own words. He had said, while on earth, "Whatever you did for
  one of the least of these, you did for me." And now he declared that he himself had been clothed in
  that poor man.
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

Correction (post-PR#579 Opus review): the `text` field previously read "the gate of the city ... a poor
man," with an ellipsis standing in for "of Amiens." That was wrong. In the source, "of Amiens" sits
directly in the main translated sentence - "he happened to meet at the gate of the city of Amiens
<note n="8">...</note> a poor man destitute of clothing" (lines 770-773) - immediately before the
endnote tag, not inside it. The endnote at that point (note 8) only glosses the underlying Latin place
name ("Ambianensium civitas") and gives its alternate ancient name ("Samarobriva"); it does not say
"Amiens" is absent from, or only editorial to, the main text. "The city of Amiens" is Roberts's own
main-text rendering of Sulpitius's "Ambianensium civitas," and belongs in this record's `text` field
verbatim, with no ellipsis at that point. The `text` field has been corrected accordingly, matching the
host record gallic.story.the-cloak-at-amiens's own corrected treatment of the same place-name.

Normalization: line breaks joined with single spaces. The source marks the two spoken lines with a dash
before an opening curly quotation mark; the first is closed with a curly closing mark, the second is
not closed in the source at all before the sentence continues into "), declared that..." - both are
rendered here as normal, properly-paired quotations, the mechanical presentation of the marks rather
than the words being what is normalized, consistent with this world's existing quote record for the
same author (gallic.quote.martin-on-the-christ-with-wounds). No word was added, dropped, substituted,
or reordered.

`modern_rendering` re-authored (post-PR#579 Opus review): the previous rendering carried the same bare
"..." gap as the old `text` field ("at the gate of the city ... a poor man") and was rejected for it.
With the `text` field now a complete, continuous verbatim passage, the rendering has been rewritten
from scratch as continuous natural prose with no ellipsis and no gap of any kind. Every clause of the
corrected `text` field is rendered; both of Christ's quoted lines appear as direct modern-English
quotations ("catechumen" rendered as "candidate for baptism" - a plain, non-misleading modern
equivalent; "robe" kept as Roberts's own word in that one line, not silently harmonized with "cloak"
elsewhere in the narration). Sentences were kept short (one thought each, none past ~25 words) and
nothing was added beyond what the verbatim text licenses.
