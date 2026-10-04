---
id: cappadocian.quote.basil-on-his-retreat
world_id: cappadocian-trinitarian
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: cappadocian.source.basil-letters-general-corpus
  locus: "Letter XIV (To Gregory his friend, on his choice of a Pontic retreat) (npnf208_basil-letters-select-works.xml)"
  license: public-domain
text: >-
  What need to tell of the exhalations from the earth, or the breezes
  from the river? Another might admire the multitude of flowers, and
  singing birds; but leisure I have none for such thoughts. However,
  the chief praise of the place is, that being happily disposed for
  produce of every kind, it nurtures what to me is the sweetest
  produce of all, quietness; indeed, it is not only rid of the bustle
  of the city, but is even unfrequented by travellers, except a
  chance hunter.
speaker_or_author: cappadocian.figure.basil
license: verbatim
modern_lens_note: >-
  A modern reader might take this letter as proof that Basil actually
  found what he was looking for - a settled hermit at last, done with
  church business. The record's own irony cuts the other way. This is
  the letter of a man who had only just finished escaping a promising
  secular career; within a few years he would be ordained priest, then
  made bishop of Caesarea, and would spend most of the rest of his life
  running a diocese, building a poorhouse-hospital complex, and fighting
  doctrinal battles by letter - dragged back, again and again, to
  exactly the kind of public office this passage is written to escape.
  The quiet by the river was not a way of life Basil achieved and kept;
  it was a real desire he named once, vividly and beautifully, and then
  mostly did not get to live.
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether this world's way of life has anything for someone who can't quiet their
    own head"
relations:
- type: associated-with
  target: cappadocian.dw.stillness-and-the-summons
modern_rendering: >-
  Why bother describing the scents rising off the earth, or the
  breezes from the river? Someone else might go on about the flowers
  and the birdsong, but I have no leisure for that. The real glory of
  this place is that, fertile as it is for every kind of produce, the
  sweetest crop it grows me is quiet. It isn't just free of the city's
  noise - hardly anyone even passes through, except the occasional
  hunter.
use_note:
  means: "Basil's Letter XIV to Gregory praises his Pontic riverside retreat for its quietness, far from the city and travellers."
  not_for:
    - "the era's classic defence of fleeing church office, which is Gregory of Nazianzus's Oration 2, not this letter"
    - "proof that Basil found and kept a settled hermit's life"
    - "a method for quieting an anxious mind, which neither this letter nor cappadocian.dw.stillness-and-the-summons supplies"
  years: {from: 358, to: 359}
  status: reviewed
---
Verified verbatim directly against the vendored
npnf208_basil-letters-select-works.xml. `grep -n "Calypso"` located the
letter's div block ("To Gregory his friend," div id="ix.xv") at line
24000; its printed heading "Letter\nXIV." appears at lines 23973-23974
(the div id's own "xv" is a structural/XML numbering artifact, not the
printed letter number - the printed text reads "Letter XIV," i.e.
fourteen). A first `grep -n -i "sweetest produce"` across the file
returned nothing because the phrase itself wraps mid-word across a line
break in the source ("...is the sweetest\nproduce of all..."); a
follow-up `grep -n -i "sweetest"` found it at line 24029, confirmed by
reading lines 23971-24041 directly. The quoted text runs lines
24024-24032 of the vendored file (from "What need to tell of the" through
"except a chance hunter.").

Normalization applied: the source uses a non-breaking-space-plus-space
pair (rendered as literal U+00A0 followed by a regular space) after
several sentence-final periods within this span - collapsed here to a
single regular space, matching this build's standing convention for
NPNF's double-spacing. No footnote markers, endnote anchors, or
`<pb>` page-break tags fall within the chosen span itself, though both
occur nearby in the same letter (an endnote anchor on "Letter XIV" at
line 23974, and a `<pb n="125".../>` page-break tag at line 24010,
inside the earlier landscape-description paragraph this excerpt does
not draw from); nothing was stripped from the quoted text because
nothing of that kind falls inside it. No wording added, dropped, or
reordered.

This excerpt was chosen over the letter's earlier, longer landscape
description (the mountain, the river "impassable as a wall," the gorge,
the comparison to Calypso's Island and to the Strymon at Amphipolis) on
purpose: that material is vivid but is about the place's beauty for its
own sake, whereas this later, shorter span is where Basil himself names
what the place is actually for - not scenery, but "quietness," called
outright the "sweetest produce of all" - and pairs that naming with the
plainest statement of its seclusion ("rid of the bustle of the city...
unfrequented by travellers, except a chance hunter"). That combination, in one contiguous, well-bounded span, is what backs
cappadocian.dw.stillness-and-the-summons's claim that this world's teachers
longed for stillness: here is Basil's own praise of the quiet he chose, at the
moment he is choosing the retreat rather than being called back from it. The
letter is not the era's classic defense of fleeing church office. That defense is
Gregory of Nazianzus's Oration 2 (see cappadocian.term.hesychia), and this letter
only praises the retreat's quiet. The dw's irony (that Basil served in office
anyway, called back again and again) is carried in this record's modern_lens_note
rather than in the quote itself, since the letter's own text is a portrait of the
desire for stillness, not of its later, repeated failure.

No source record in records/cappadocian/source/ specifically covers
this individual letter; cappadocian.source.basil-letters-general-corpus
(the general corpus record for Basil's Letters) is used instead, per
this build's own convention of falling back to the general corpus
record when no letter-specific source record exists.

The spoken form is a modern-English translation, never the archaic original; the original stays as the record's own text field, shown at Level 3.
