---
id: gallic.quote.europe-will-not-yield-having-only-martin
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: >-
    Documented as Sulpitius's own text (Dialogues III.17, read at its locus for this record) - a
    speaker's direct instruction inside the Dialogues' own closing frame.
sources:
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: "Dialogues III.17 (npnf211 div ii.iv.iii.xvii, file lines 5398-5411): instructions to
    Postumianus to carry word of Martin as far as Egypt itself, claiming Europe need not yield to
    Egypt or Asia while it has Martin"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how far this world's own comparison with Egypt was pushed"
  - "participant asks whether the north conceded Egypt's superiority or contested it directly"
  prefer_instead:
  - "participant wants Postumianus's own side of the same comparison - retrieve gallic.quote.postumianus-you-have-conquered-all-the-eremites"
text: >-
  But when you have come as far as Egypt, although it is justly proud
  of the numbers and virtues of its own saints, yet let it not disdain
  to hear how Europe will not yield to it, or to all Asia, in having
  only Martin.
speaker_or_author: gallic.figure.sulpitius
license: verbatim
modern_lens_note: >-
  This does not deny Egypt's own real numbers and holiness - it grants them directly ("justly
  proud") - and still claims parity for Europe on the strength of one man alone. The comparison is
  deliberately lopsided: many Egyptian saints against a single Gallic one, offered as an even
  match.
modern_rendering: >-
  Egypt is rightly proud of the number and virtues of its own saints. But when you have come as
  far as Egypt, let it not disdain to hear this. With Martin alone, Europe will not give way to
  Egypt, or to all Asia.
relations:
- type: associated-with
  target: gallic.gravity.egypt-as-measure
use_note:
  means: "Sulpitius, in the Dialogues' closing, bids Postumianus tell Egypt that Europe, having only Martin, will not yield to it or to all Asia."
  not_for:
    - "a denial of Egypt's holiness, when the text grants that Egypt is justly proud"
    - "Cassian's view of Egypt as the measure, which sits in gallic.quote.castor-anxious-for-egyptian-institutions"
  years: {from: 404, to: 406}
  status: provisional
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"when you have come as far as Egypt"` returns line 5408; `grep -n "in having only Martin"` returns
a hit in the same passage. Read with `sed -n '5370,5411p'`, inside `<div4 ... id="ii.iv.iii.xvii">`
(Chapter XVII). The speaker is "I" in the surrounding frame ("Then said I..."), addressing
Postumianus with travel instructions; the surrounding context (`gallic.figure.sulpitius`'s own
sources[] locus, "Dialogues III.11-13, III.15 - Sulpitius as the audience within his own frame...
with Gallus as narrator") establishes Sulpitius as a named interlocutor distinct from Gallus within
this same work, and this speech, in Dialogue III's closing chapters, is his. This is a disclosed
judgment call, not a certain identification the source states by name at this exact line. The
quoted span is one complete sentence, "But when you have come..." through "...in having only
Martin.", ending at its own period.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.