---
id: desert.quote.pachomius-angel-tablet
world_id: desert-monasticism
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: [F4-I]
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
  divergence_note: "Widely Accepted for the vision's own place in this world's founding narrative, matching desert.story.pachomius-founding's own basis - vendored, hagiographic frame, per desert.source.pachomian-corpus's own standing channel-naming rule and desert.source.palladius-lausiac-history's own AUTHOR GRAVITY note (a hagiographic summary at one remove, not the Rule's own text)."
sources:
- source_id: desert.source.palladius-lausiac-history
  locus: "ch. XXXII - the angel's own opening instruction, in Clarke's translation"
  license: public-domain
text: "Thou shalt allow each man to eat and drink according to his strength; and proportionately to the strength of the eaters appoint to them their labours. And prevent no man either from fasting or eating..."
modern_rendering: >-
  You shall let each man eat and drink according to his own strength. In proportion to
  the strength of those eating, assign them their labors. Do not prevent any man, either
  from fasting or from eating...
speaker_or_author: "an angel"
license: verbatim
modern_lens_note: "No significant modern-lens risk identified: this is administrative rule-language (eating, drinking, labor proportioned to strength), plain in any era."
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what the rule actually required of a member day to day"
  - "participant asks how food, work and prayer were apportioned"
relations:
- type: associated-with
  target: desert.story.pachomius-founding
- type: associated-with
  target: desert.figure.pachomius
- type: associated-with
  target: desert.quote.ethiopic-rule-eat-and-drink
---
Verified verbatim against the vendored file (ch. XXXII, line
397). desert.story.pachomius-founding cites this record for the
tablet's own opening clause, which is verbatim-quotable and carried
here in full.

speaker_or_author names only what the text itself supports: ch. XXXII
narrates entirely in Palladius's own third person ("to him as he sat in
his cave an angel appeared and said...") and names no informant, unlike
ch. XXII, where Palladius explicitly names Cronius and Hierax as his
sources. The angel is the speaker within Palladius's narration; this
record does not attribute the account to Pachomius's own telling.
`sources[].locus`, like `text`, compiles directly into `quotes.json`
(`build_quotes_json()` emits `sources` as well).

This record carries only the tablet's own opening clause, marked with a
trailing ellipsis; the tablet's own text continues with further
instructions (task assignment, cell arrangements) not carried here.
Verification cannot yet clear past "labours" partway through: the
source has a page-break marker ("labours. |113 And prevent") that the
automated verification gate does not strip.
