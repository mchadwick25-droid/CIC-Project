---
id: gallic.quote.paphnutius-bubalis-and-the-brothers-envy
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
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted as Piamun's own telling, carried by Cassian for Gaul (Conferences XVIII.15). The
    wording is Documented at its locus in the vendored edition; the boyhood admiration and the brother's
    jealousy are the tradition's own account of Paphnutius's youth, decades before Piamun told it, not an
    eyewitness claim.
sources:
- source_id: gallic.source.cassian-conferences-part-iii
  locus: "Conferences XVIII.15 (npnf211 div iv.vi.ii.xv, file lines 43004-43012): the nickname Bubalis
    and its stated reason; the Elders' admiration of the young Paphnutius; the brother's envy, likened to
    Joseph's brothers"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks how the Paphnutius story opens, or why the desert called him Bubalis"
  - "participant asks about envy among brothers, or wants the Joseph comparison the tradition itself draws"
  prefer_instead:
  - "participant wants the whole story in the world's own accessible voice - retrieve gallic.story.paphnutius-and-the-hidden-book"
text: >-
  because he always delighted in dwelling in the desert as if with a sort of innate liking. And so as
  even in boyhood he was so good and full of grace that even the renowned and great men of that time
  admired his gravity and steadfast constancy, and although he was younger in age, yet put him on a
  level with the Elders out of regard for his virtues, and thought fit to admit him to their order, the
  same envy, which formerly excited the minds of his brethren against the patriarch Joseph, inflamed one
  out of the number of his brethren with a burning and consuming jealousy.
speaker_or_author: "Abbot Piamun, as Cassian records his own telling"
license: verbatim
modern_lens_note: >-
  Piamun reaches for Joseph before he tells the reader what the brother actually did - the comparison
  comes first, the plot second. That ordering tells a listener how to read what follows: this is not a
  strange local grudge but the oldest shape of envy the tradition knows, a virtuous younger man raised
  above his elders and resented for exactly the grace that raised him.
relations:
- type: associated-with
  target: gallic.story.paphnutius-and-the-hidden-book
modern_rendering: >-
  because he always loved to live in the desert, as though he had a kind of inborn liking for it. And
  so, even as a boy, he was so good and full of grace that the famous, great men of that time admired
  him. They admired his seriousness and his steady, unshaken firmness. He was younger than they were.
  Yet out of respect for his virtues they ranked him with the Elders, and thought it right to admit him
  to their order. Then the same envy that once stirred up the brothers of the patriarch Joseph against
  him took hold of one of his fellow monks. It set that man on fire with a burning, consuming jealousy.
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"because he always"` returns line 43004; `grep -n "burning and consuming jealousy"` returns line 43012,
inside `<div4 title="Chapter XV. Of the example of patience given by Abbot Paphnutius." ...
id="iv.vi.ii.xv">` (line 42992). Quoted span read with `sed -n '42999,43012p'`, from "because he always
delighted..." through "...burning and consuming jealousy."

Normalization: the source hard-wraps prose; line breaks were joined with single spaces. The endnote
marker after "Bubalis," (n="2090", Gibson's gloss "i.e., the Buffalo") sits inside the source's own prose
at that point and is not part of the quoted sentence; it is dropped, as is any other in-line note anchor.
No word was added, dropped, substituted, or reordered.

speaker_or_author names Piamun, not Cassian: the host record's own sources[] locus identifies this
chapter as "the Conference of Abbot Piamun," and the chapter's opening ("Now let us give the other
instance...") is part of Piamun's own discourse as Cassian transcribes it. No figure record exists for
Piamun in this world's build, so a descriptive string is used rather than a fabricated id.
