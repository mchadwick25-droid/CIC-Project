---
id: desert.quote.antony-not-worsted
world_id: desert-monasticism
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: [F4-P]
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Contested
  divergence_note: "Contested for this scene as this world's own portrait of combat, matching desert.story.antony-tomb-combat's own basis - the words themselves are quoted verbatim from the vendored text, so the citation itself is not in question."
sources:
- source_id: desert.source.athanasius-vita-antonii
  locus: "SS9 - Antony's own words to the demons attacking him in beast form"
  license: public-domain
text: "If there had been any power in you, it would have sufficed had one of you come, but since the Lord hath made you weak, you attempt to terrify me by numbers: and a proof of your weakness is that you take the shapes of brute beasts... If you are able, and have received power against me, delay not to attack; but if you are unable, why trouble me in vain? For faith in our Lord is a seal and a wall of safety to us."
modern_rendering: >-
  If you had any real power, it would have been enough for just one of you to come. But the Lord has
  made you weak. So you try to frighten me with your numbers. Taking the shapes of wild animals is
  proof of your weakness. ... If you have the power to attack me, do not wait -- attack now. But if
  you cannot, why trouble me for nothing? Faith in our Lord is a seal and a wall that keeps us safe.
speaker_or_author: desert.figure.antony
license: verbatim
modern_lens_note: "The demons' \"shapes of brute beasts\" risks two opposite modern misreadings: taken as a literal supernatural claim, or dismissed outright as primitive superstition with nothing to say. This world's own record holds it as neither - see desert.story.antony-tomb-combat's own explicit instruction that this material is not neutral incident report."
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether they believed in demons and what one was like to meet"
  - "participant asks what frightened them at night and how they answered fear"
relations:
- type: associated-with
  target: desert.story.antony-tomb-combat
- type: associated-with
  target: desert.gravity.spiritual-combat
- type: associated-with
  target: desert.figure.antony
use_note:
  means: "Athanasius gives Antony's words to demons attacking in beast form, mocking their weakness and naming faith in the Lord as his wall of safety."
  not_for:
    - "the scene as a neutral factual report of a supernatural event"
    - "the demons' beast shapes as primitive superstition with nothing to say"
    - "Antony's words as independently attested speech outside Athanasius's Vita"
  years: {from: 356, to: 362}
  status: provisional
---
Verified verbatim against the vendored file
(npnf204_athanasius-select-works-letters.xml), the same passage
desert.story.antony-tomb-combat narrates in paraphrase. This record
carries the direct words themselves for a Representative who needs the
line quoted rather than told. This record declares a relation to
desert.figure.antony, matching speaker_or_author and both sibling
Antony quotes.

The text field carries the clause "and a proof of your weakness is
that you take the shapes of brute beasts" in full, keeping the
vendored text's colon at that join. Athanasius's narrative interjection
"And again with boldness he said" is marked with an ellipsis, matching
the convention desert.quote.arsenius-flee-tace-quiesce uses for a
similar elision. Punctuation elsewhere matches the vendored text
character for character ("come, but since" and "by numbers: and a
proof").

This record's own id ("not-worsted") echoes SS10's own vision-voice
line ("since thou hast endured, and hast not been worsted, I will ever
be a succour to thee"), not a phrase inside this record's own SS9
quotation - the id names the episode's own outcome, not this
quotation's own wording.
