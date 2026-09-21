---
id: witt.quote.the-poor-man-who-comes-to-you
world_id: lutheran-wittenberg-and-its-congregations
record_type: quote
schema_version: 2
status: draft
register: emic
canon_cells:
- F5-T
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: >-
    Documented at a single work, the Large Catechism's own Seventh Commandment explanation (household
    catechesis register); no other register in this library's built records was checked for money and
    poverty material by this authoring pass, disclosed rather than smoothed.
sources:
- source_id: witt.source.luther-large-catechism
  locus: "the Seventh Commandment, on theft (cic:luther_large-catechism_bente-dau1921.txt lines 1946-1959): 'when the poor man comes to you... beware... as of the devil himself'"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how we looked at money and poverty, or whether we would call anyone among us rich"
  prefer_instead:
  - "participant wants our own account of a specific rich or poor person -- our library names no individual by wealth"
text: >-
  But beware of this: When the poor man comes to you (of whom there are
  so many now) who must buy with the penny of his daily wages and live
  upon it, and you are harsh to him, as though every one lived by your
  favor, and you skin and scrape to the bone, and, besides, with pride
  and haughtiness turn him off to whom you ought to give for nothing, he
  will go away wretched and sorrowful, and since he can complain to no
  one he will cry and call to heaven, -- then beware (I say again) as of
  the devil himself. For such groaning and calling will be no jest, but
  will have a weight that will prove too heavy for you and all the
  world. For it will reach Him who takes care of the poor sorrowful
  hearts, and will not allow them to go unavenged.
speaker_or_author: "the Large Catechism, the Seventh Commandment's own household explanation"
license: verbatim
modern_lens_note: >-
  A modern reader may expect a catechism's teaching on wealth to be an abstract principle -- almsgiving as
  a virtue, stated in general. This passage is not abstract. It names a specific figure, "the poor man...
  who must buy with the penny of his daily wages," and threatens the one who turns him away with contempt,
  in the sharpest language this household book uses anywhere: "beware... as of the devil himself." We do
  not, in this passage, call any named person among us rich; we name instead a household duty toward
  whoever among the neighbors is poor, and a warning fixed on the household's own pride and harshness, not
  on wealth itself as a category.
modern_rendering: >-
  But be careful of this. A poor man comes to you -- there are so many now -- someone who buys his daily
  bread with a day's wage and lives on that. Say you treat him harshly. Say you act as though everyone
  lived only by your favor. Say you squeeze him to the bone, then turn him away with pride, when you owed
  him help for nothing. He will go away wretched and sorrowful. He has no one else to complain to, so he
  will cry out to heaven. Be careful of that, I say again, the way you would be careful of the devil
  himself. That cry is no small thing. It carries a weight too heavy for you, and for the whole world
  besides. It reaches the one who cares for the poor and the sorrowful. He will not let it go unanswered.
relations:
- type: associated-with
  target: witt.dw.the-poor-man-at-the-door
---
Verified verbatim at this step (Answer-the-Canon pass, inserted between B-7a and B-8) directly against
the vendored cic/texts/luther_large-catechism_bente-dau1921.txt. `grep -n "when the poor man comes to
you\|as of the devil himself\|will reach Him who takes care of the poor"` returns "But beware of this:
When the poor man comes to you (of whom there are" at line 1946, "one he will cry and call to heaven, --
then beware (I say again) as of" at line 1952, and "will have a weight that will prove too heavy for you
and all the / world. For it will reach Him who takes care of the poor sorrowful" at lines 1954-1955.
`sed -n '1944,1970p'` confirms the passage read in its own paragraph: the prior sentence closing at 1944
("nevertheless have enough, and you injure yourself more than another.") left outside `text`; the quoted
span opening at "But beware of this" (line 1946) and closing at "will not allow them to go unavenged."
(line 1956); the paragraph continues afterward (1957-1959, "But if you despise this and become defiant...
call God and me a liar") into a second warning this record does not need and leaves out, cutting cleanly
at a full stop. No word added, dropped, substituted, or reordered within the quoted span.

Ground for witt.dw.the-poor-man-at-the-door (F5-T: money and poverty). This world's own library was not
searched beyond this one locus for money-and-poverty material by this authoring pass -- disclosed at
illustrative weight and single-work citation_specificity rather than claimed as fuller coverage than one
grep pass into one commandment's explanation can support. Reciprocal associated-with declared on
witt.dw.the-poor-man-at-the-door.
