---
id: desert.quote.pachomius-angel-tablet
world_id: desert-monasticism
record_type: quote
schema_version: 2
status: draft
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
text: "Thou shalt allow each man to eat and drink according to his strength; and proportionately to the strength of the eaters appoint to them their labours. And prevent no man either from fasting or eating."
speaker_or_author: "an angel"
license: verbatim
modern_lens_note: "No significant modern-lens risk identified: this is administrative rule-language (eating, drinking, labor proportioned to strength), plain in any era."
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what the rule actually required of a member day to day"
  - "participant asks how food, work and prayer were apportioned"
  do_not_retrieve_when: []
relations:
- type: associated-with
  target: desert.story.pachomius-founding
- type: associated-with
  target: desert.figure.pachomius
- type: associated-with
  target: desert.quote.ethiopic-rule-eat-and-drink
---
Verified verbatim 2026-08-22 against the vendored file (ch. XXXII, line
397). Added per Step 4 Round 1 review Finding S6, which found
desert.story.pachomius-founding's own body citing this record before it
existed - the gap the review pointed at was real, and this is the fix
rather than a removal of the reference: the tablet's own opening clause
genuinely is verbatim-quotable and no quote record carried it.

Step4, Round 2 review Finding S7: speaker_or_author previously read "an
angel, as Palladius reports Pachomius's own account of the vision" -
checked directly against ch. XXXII, which narrates entirely in
Palladius's own third person ("to him as he sat in his cave an angel
appeared and said...") and names no informant, unlike ch. XXII, where
Palladius explicitly names Cronius and Hierax as his sources. There is
no textual basis for attributing this account to Pachomius's own
telling specifically - corrected to name only what the text itself
supports, the angel as the speaker within Palladius's narration. The
same finding noted that this field, like `text`, compiles directly into
`quotes.json` (`build_quotes_json()` emits `sources` as well, so
`sources[].locus` also compiles - a correction to how this step's own
STEP4-INDEX.md described the M8 fix elsewhere in this record set, not a
claim specific to this record).
