---
id: gallic.quote.institutes-opening-soldier-of-christ
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Cassian's own text (Institutes I.1, read at its locus for this record) - the
    second sentence of Book I, chapter 1, after one introductory sentence, setting the soldier
    idiom as the frame for everything that follows about dress and discipline.
sources:
- source_id: gallic.source.cassian-institutes
  locus: "Institutes I.1 (npnf211 div iv.iii.i.i, file lines 16571-16573): the second sentence of
    Book I, chapter 1, right after its own preface, on the monk as a soldier of Christ"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how Book I of the Institutes opens, after its own preface"
  - "participant asks why a monk's dress is described using military language"
  prefer_instead:
  - "participant wants the same idiom used of a fault instead of dress - retrieve gallic.quote.deserter-from-his-service"
text: >-
  A monk, then, as a soldier of Christ ever ready for battle, ought
  always to walk with his loins girded.
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  This is the second sentence of the Institutes' own Book I, chapter 1, opening a chapter titled
  "Of the Monk's Girdle," right after one sentence of introductory framing. The military comparison
  is not decoration added later - it is the frame Cassian chooses before he says anything else
  about a monk's actual dress.
modern_rendering: >-
  A monk, then, as a soldier of Christ always ready for battle, ought always to walk with his belt
  fastened around his waist.
relations:
- type: associated-with
  target: gallic.gravity.soldier-of-christ
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"ought always to walk with his loins"` returns line 16572; read with `sed -n '16568,16574p'`, inside
`<div4 title="Chapter I..." ... id="iv.iii.i.i">`, subtitled "Of the Monk's Girdle" - the opening
chapter of Book I, itself the opening book of the Institutes. The quoted span is one complete
sentence, "A monk, then, as a soldier of Christ..." through "...walk with his loins girded.",
ending at its own period; it is the second sentence of Book I, chapter 1, immediately following
one sentence of Cassian's own introductory framing ("As we are going to speak of the customs and
rules of the monasteries, how by God's grace can we better begin than with the actual dress of the
monks..."). Book I, ch. 1 itself comes after the Institutes' own separate Preface (carried in
gallic.quote.castor-anxious-for-egyptian-institutions and gallic.quote.cassian-adapts-egypt-to-gaul),
so this is not the work's own opening sentence.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.
