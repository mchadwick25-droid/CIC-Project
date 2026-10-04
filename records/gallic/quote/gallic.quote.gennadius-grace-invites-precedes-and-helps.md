---
id: gallic.quote.gennadius-grace-invites-precedes-and-helps
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
voice: analytic
register: etic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted as Gennadius's own summary of Faustus's book On the Grace of God (read at its
    locus for this record), not a passage from Faustus's own text - Gennadius describes the book,
    he does not quote it.
sources:
- source_id: gallic.source.gennadius-de-viris-illustribus
  locus: "ch. LXXXVI (npnf203 div v.iv.lxxxvii, file lines 43695-43699): Gennadius's own summary of
    Faustus's book On the Grace of God"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what Faustus's own book on grace actually taught, in outside summary"
  - "participant wants Gennadius's own words for the doctrine, not this record's paraphrase"
  prefer_instead:
  - "participant wants the same idea from inside the south's own formation literature - retrieve gallic.quote.not-i-but-the-grace-of-god-with-me or gallic.quote.perfection-not-gained-without-grace"
text: >-
  He published also an excellent work, On the grace of God, through
  which we are saved, in which he teaches that the grace of God always
  invites, precedes and helps our will, and whatever gain that freedom
  of will may attain for its pious effect, is not its own desert, but
  the gift of grace.
speaker_or_author: Gennadius of Marseilles, De Viris Illustribus
license: verbatim
modern_lens_note: >-
  This is Gennadius describing Faustus's book from the outside, in Gennadius's own words - it is not
  a quotation of Faustus's own text. The three verbs Gennadius uses for grace ("invites, precedes and
  helps") describe how Gennadius read the book's argument, not a phrase Faustus himself is known to
  have written this way.
modern_rendering: >-
  He also published an excellent work, On the Grace of God, Through Which We Are Saved. In it he
  teaches that God's grace always invites our will, goes before it, and helps it. He teaches too
  that whatever gain our free will may make toward a devout result is not something it has earned.
  It is the gift of grace.
relations:
- type: associated-with
  target: gallic.force.synodal-commission
---
Verified directly against cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml. `grep -n "in
which he teaches that the"` matches two locations; the one needed is line 43696, inside `<div3
type="Chapter" title="Faustus the bishop." ... id="v.iv.lxxxvii">` (printed heading "Chapter
LXXXVI," one lower than the div id's own "lxxxvii" per this file's own numbering offset) - confirmed
by reading with `sed -n '43688,43701p'`, not the unrelated Corinthians letter at line 40076. The
quoted span is one complete sentence, "He
published also an excellent work..." through "...the gift of grace.", ending at its own period. The
source's own mid-word page-break tag splitting "invites, pre|cedes" (pagination markup, `<pb
n="400".../>`) is removed and the word rejoined as "precedes" - no letters added, dropped, or
changed.

Normalization: line breaks joined with single spaces; the source's own italic markup around the
work's title is dropped, the words themselves unchanged. No word was added, dropped, substituted, or
reordered.
