---
id: desert.quote.arsenius-flee-tace-quiesce
world_id: desert-monasticism
record_type: quote
schema_version: 2
status: draft
register: emic
canon_cells: [F4-I]
confidence:
  citation_specificity: C
  verification_state: verified-via-authority
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
  divergence_note: "Widely Accepted for the saying's own place in the tradition, matching desert.story.arsenius-flee's own rating - Inferential/Thin for any claim beyond what the surviving saying itself states, matching desert.source.apophthegmata-patrum's own unconditional bound. No vendored edition exists for this source; license is paraphrase-only, per that source's own hard rule."
sources:
- source_id: desert.source.apophthegmata-patrum
  locus: "Arsenius, Alphabetical Collection - a widely attested saying attributed to Arsenius, given here in plain English rather than a specific published translation's own wording"
text: "Flee the company of men, and you will be saved... Flee, be silent, be still - these are the roots of a life without sin."
speaker_or_author: "a voice Arsenius reports having heard"
license: paraphrase-only
modern_lens_note: "\"Flee\" risks a modern misreading as anxious avoidance - running from a problem rather than facing it, the opposite of what contemporary therapeutic language usually recommends. In this world's own idiom it names a disciplined strategy, not evasion, matching the same risk desert.term.anachoresis's own translational note names for \"withdrawal.\""
relations:
- type: associated-with
  target: desert.story.arsenius-flee
- type: associated-with
  target: desert.gravity.withdrawal
---
Paraphrase, not verbatim quotation, per desert.source.apophthegmata-
patrum's own hard rule. The Latin systematic collection's own
three-word form ("fuge, tace, quiesce") is well known outside this
corpus but is not itself vendored or independently verified here; this
record carries the saying in English paraphrase only, matching
desert.story.arsenius-flee.

Step4, Round 1 review Finding S10: divergence_note carried only the
"Widely Accepted" half of desert.source.apophthegmata-patrum's own
confidence pairing - the unconditional Inferential/Thin bound added
above. Finding M8: speaker_or_author carried a parenthetical provenance
tag that would compile directly - removed; the source is already
carried in sources[] and divergence_note.

Step4, Round 2 review Finding M8: `sources[].locus` also compiles into
`quotes.json` (`build_quotes_json()` emits `sources` verbatim) - the
locus above previously named a sibling record id and described itself
in build-process terms ("in this record's own words rather than a
verbatim rendering"); reworded to a plain description carrying the same
information without either.

Step4, Round 3 review Finding M6: the M8 fix still left "vendored" and
a licence-mechanics gloss in this compiled field - reworded above to
plain description with neither.
