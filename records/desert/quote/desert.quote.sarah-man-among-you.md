---
id: desert.quote.sarah-man-among-you
world_id: desert-monasticism
record_type: quote
schema_version: 2
status: draft
register: emic
canon_cells: [F6-P]
confidence:
  citation_specificity: C
  verification_state: verified-via-authority
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
  divergence_note: "Widely Accepted for the saying's own place in the tradition, matching desert.story.sarah-answer's own rating - Inferential/Thin for any claim beyond what the surviving saying itself states, matching desert.source.apophthegmata-patrum's own unconditional bound. No vendored edition exists for this source; license is paraphrase-only for that reason, per that source's own hard rule that no citation of it may claim verbatim status."
sources:
- source_id: desert.source.apophthegmata-patrum
  locus: "Sarah, Alphabetical Collection - a widely attested saying of Amma Sarah's, given here in plain English rather than a specific published translation's own wording"
text: "By nature I am a woman, but not by my own thoughts. It is I who am the man here, and you who are the women."
speaker_or_author: desert.figure.sarah
license: paraphrase-only
relations:
- type: associated-with
  target: desert.story.sarah-answer
- type: associated-with
  target: desert.gravity.elder-authority
---
Paraphrase, not verbatim quotation - desert.source.apophthegmata-patrum
carries no vendored edition, and this build's own hard rule bars any
verbatim-quote claim against it. The wording restates the saying's
substance rather than reproducing a specific published translation's
own English, consistent with desert.figure.sarah's own identical
discipline for the same saying.

Step4, Round 1 review Finding S10: divergence_note carried only the
"Widely Accepted" half of desert.source.apophthegmata-patrum's own
confidence pairing - the unconditional Inferential/Thin bound added
above, matching desert.figure.sarah's own full statement of it.

Step4, Round 2 review Finding M8: `sources[].locus` compiles into
`quotes.json` (`build_quotes_json()` emits `sources` verbatim), which
this build's own field map for the record type had not previously
flagged - the locus above previously named two sibling record ids and
described itself in build-process terms ("in this record's own words
rather than a verbatim rendering"); reworded to a plain description
carrying the same information without either.

Step4, Round 3 review Finding M6: the M8 fix still left "vendored" and
a licence-mechanics gloss in this compiled field - reworded above to
plain description with neither.
