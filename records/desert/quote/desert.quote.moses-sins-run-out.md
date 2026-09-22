---
id: desert.quote.moses-sins-run-out
world_id: desert-monasticism
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
- source_id: desert.source.apophthegmata-patrum
  locus: §542 (cic/texts/anan-isho_paradise-v2-sayings_budge1907.txt line 1160) - Budge's Syriac recension
  license: public-domain
text: '[The sands are] my sins which are running down behind me and I cannot see them, and I, even I, have
  come this day to judge shortcomings which are not mine.'
speaker_or_author: Abba Moses
license: verbatim
modern_lens_note: 'No significant modern-lens risk identified for this quote''s own vocabulary or imagery:
  sins pictured as a trail running out behind you, unseen, while you judge someone else''s - the image
  reads plainly to a modern ear the same way it read then.'
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what happened when someone did wrong and the others found out"
  - "participant asks whether they judged each other, and how forgiveness worked"
  - "participant asks whether anyone was ever put out of the community"
relations:
- type: associated-with
  target: desert.story.moses-leaking-jug
- type: associated-with
  target: desert.gravity.diakrisis
---
VERBATIM AS OF 2026-08-27, verified against the newly vendored Budge at
line 1160, §542. DISCLOSED: the file prints "[The sands are]" in square
brackets - the translator's supplement for an ellipsis in the Syriac; the
supplement is Budge's, not this world's.

Quote-verbatim gate fix (2026-09-22): the brackets themselves are restored, keeping the words exactly
as before - dropping the bracket marks (rather than the words) still left the record unable to verify
against the source's own printed form. The gate treats a bracketed span in a record's own text as a
labeled editorial insertion, so this now shows Budge's supplement exactly as flagged rather than
silently blending it into the sentence.

The narrative around it - a brother's offence at Scete, the summons Moses
first refused and then obeyed, the basket of sand carried on his
shoulders - stands at the same locus and is carried by
desert.story.moses-leaking-jug, which can now be verified against it
too.

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
