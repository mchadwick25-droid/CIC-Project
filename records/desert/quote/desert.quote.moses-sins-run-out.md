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
modern_rendering: >-
  [The sands are] my sins, running down behind me. I cannot see them. And I -- I myself -- have come
  this day to judge faults that are not my own.
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
use_note:
  means: "In Budge's Syriac Sayings, Abba Moses says his own sins run out unseen behind him while he comes to judge another's faults."
  not_for:
    - "the words \"The sands are\" as Moses's, when they are Budge's bracketed supplement"
    - "the saying as securely datable to Moses rather than transmitted in a collection compiled after 430"
    - "a formal disciplinary procedure, which Moses refuses here"
  years: {from: 320, to: 430}
  status: reviewed
---
Checked against the vendored Budge at line 1160, §542. The file prints "[The sands are]"
in square brackets. The brackets are the translator's supplement for a gap in the Syriac, so
the words are Budge's and not Moses's. The text field keeps the brackets to show this.

The narrative around the saying is at the same locus and is carried by
desert.story.moses-leaking-jug: a brother's offence at Scete, the summons Moses first
refused and then obeyed, and the basket with a hole in it, filled with sand and carried on his
shoulders.

The text is verbatim for Budge's edition. Whether the saying reaches back to Moses himself is
the compilers' claim, not something the edition shows. No figure record exists for Abba Moses
in this corpus, so speaker_or_author names him as a plain string.
