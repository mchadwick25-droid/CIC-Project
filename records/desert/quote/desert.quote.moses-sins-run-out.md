---
id: desert.quote.moses-sins-run-out
world_id: desert-monasticism
record_type: quote
schema_version: 2
status: draft
register: emic
canon_cells: [F4-P]
confidence:
  citation_specificity: C
  verification_state: verified-via-authority
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
  divergence_note: "Widely Accepted for the saying's own place in the tradition, matching desert.story.moses-leaking-jug's own rating - Inferential/Thin for any claim beyond what the surviving saying itself states, matching desert.source.apophthegmata-patrum's own unconditional bound. No vendored edition exists for this source; license is paraphrase-only, per that source's own hard rule."
sources:
- source_id: desert.source.apophthegmata-patrum
  locus: "Moses, Alphabetical Collection - a widely attested saying of Abba Moses's, given here in plain English rather than a specific published translation's own wording"
text: "My own sins run out behind me the same way, and I do not see them - and today I am coming to judge another man's fault."
speaker_or_author: "Abba Moses"
license: paraphrase-only
modern_lens_note: "No significant modern-lens risk identified for this quote's own vocabulary or imagery: sins pictured as a trail running out behind you, unseen, while you judge someone else's - the image reads plainly to a modern ear the same way it read then."
relations:
- type: associated-with
  target: desert.story.moses-leaking-jug
- type: associated-with
  target: desert.gravity.diakrisis
---
Paraphrase, not verbatim quotation, per desert.source.apophthegmata-
patrum's own hard rule - no vendored edition exists for this source.
No figure record exists for Abba Moses in this corpus (no comparable
individually-verified biographical basis to desert.figure.sarah's own),
so speaker_or_author names him as a plain string rather than an id.

Step4, Round 1 review Finding S10: divergence_note carried only the
"Widely Accepted" half of desert.source.apophthegmata-patrum's own
confidence pairing - the unconditional Inferential/Thin bound added
above, matching the Step3a Round 8/Step3c Round 2 discipline for this
exact source. Finding M8: speaker_or_author carried a parenthetical
provenance tag ("(Apophthegmata Patrum)") that would compile directly
into build_quotes_json() - removed; the source is already carried in
sources[] and divergence_note.

Step4, Round 2 review Finding M8: `sources[].locus` also compiles into
`quotes.json` (`build_quotes_json()` emits `sources` verbatim) - the
locus above previously named a sibling record id and described itself
in build-process terms ("in this record's own words rather than a
verbatim rendering"); reworded to a plain description carrying the same
information without either.

Step4, Round 3 review Finding M6: the M8 fix still left "vendored" and
a licence-mechanics gloss ("rather than a verbatim rendering") in this
compiled field - "vendored" is the head of the jargon family Step 3a
spent five rounds excising from compiled-facing fields. Reworded above
to plain description with neither.
