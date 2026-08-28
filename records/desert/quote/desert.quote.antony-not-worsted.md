---
id: desert.quote.antony-not-worsted
world_id: desert-monasticism
record_type: quote
schema_version: 2
status: draft
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
speaker_or_author: desert.figure.antony
license: verbatim
modern_lens_note: "The demons' \"shapes of brute beasts\" risks two opposite modern misreadings: taken as a literal supernatural claim, or dismissed outright as primitive superstition with nothing to say. This world's own record holds it as neither - see desert.story.antony-tomb-combat's own explicit instruction that this material is not neutral incident report."
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether they believed in demons and what one was like to meet"
  - "participant asks what frightened them at night and how they answered fear"
  do_not_retrieve_when: []
relations:
- type: associated-with
  target: desert.story.antony-tomb-combat
- type: associated-with
  target: desert.gravity.spiritual-combat
- type: associated-with
  target: desert.figure.antony
---
Verified verbatim 2026-08-22 against the vendored file
(npnf204_athanasius-select-works-letters.xml), the same passage
desert.story.antony-tomb-combat narrates in paraphrase. This record
carries the direct words themselves for a Representative who needs the
line quoted rather than told.

Step4, Round 1 review Finding M16: no relation to desert.figure.antony
had been declared despite speaker_or_author naming that record and both
sibling Antony quotes declaring it - added above.

Step4, Round 1 review Finding S5: this text had silently spliced two
distinct sentences from SS9 into one, dropping the clause "and a proof
of your weakness is that you take the shapes of brute beasts" entirely
and converting the vendored text's colon to a full stop at the join,
between "And again with boldness he said" (a narrative interjection,
not Antony's own words). The dropped clause is restored above; the
narrative interjection is marked with an ellipsis, matching the
convention desert.quote.arsenius-flee-tace-quiesce already uses for an
elision within the same step.

Step4, Round 2 review Finding M1: two further unmarked punctuation
alterations survived that fix - "come; but since" for the vendored
"come, but since," and "by numbers, and a proof" for the vendored "by
numbers: and a proof." Character-compared against the file directly
this pass and corrected above.

Step4, Round 1 review Finding C1 (naming note, not a content fix): this
record's own id ("not-worsted") echoes SS10's own vision-voice line
("since thou hast endured, and hast not been worsted, I will ever be a
succour to thee"), not a phrase inside this record's own SS9 quotation
- the id names the episode's own outcome, not this quotation's own
wording. Left as is; renaming would break existing cross-references for
a cosmetic mismatch only.
