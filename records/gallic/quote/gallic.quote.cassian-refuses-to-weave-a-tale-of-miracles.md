---
id: gallic.quote.cassian-refuses-to-weave-a-tale-of-miracles
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
    Documented as Cassian's own programmatic statement, opening the Institutes (Preface, read at
    its locus for this record) - his own declared reason for refusing miracle-narrative, load-
    bearing for the south's own refusal of the north's virtus economy.
sources:
- source_id: gallic.source.cassian-institutes
  locus: "Preface (npnf211 div iv.ii, file lines 16503-16517): Cassian's refusal to narrate
    miracles, and his stated purpose instead"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks why Cassian's own writing has so few miracle stories"
  - "participant asks what Cassian thought writing about monks was actually for"
  prefer_instead:
  - "participant wants Cassian's fuller case against miracle-fame as vainglory - retrieve gallic.quote.humility-mistress-of-virtues-not-exorcism"
text: >-
  Nor certainly shall I try to weave a tale of God's miracles and
  signs, although we have not only heard of many such among our elders,
  and those past belief, but have also seen them fulfilled under our
  very eyes; yet, leaving out all these things which minister to the
  reader nothing but astonishment and no instruction in the perfect
  life, I shall try, so far as I can, with the help of God, faithfully
  to explain only their institutions and the rules of their
  monasteries, and especially the origin and causes of the principal
  faults, of which they reckon eight, and the remedies for them
  according to their traditions,—since my purpose is to say a few
  words not about God's miracles, but about the way to improve our
  character, and the attainment of the perfect life, in accordance with
  that which we received from our elders.
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  Cassian does not deny that he has seen real wonders - he says so directly. He refuses to write
  about them anyway, because a miracle astonishes a reader without teaching one anything about how
  to live. The refusal is deliberate and stated, not an absence of material.
modern_rendering: >-
  I will certainly not try to weave a tale of God's miracles and signs. It is true that we have
  heard of many such things among our elders, things beyond belief. We have also seen them
  fulfilled before our very eyes. Yet I will leave out all these things. They give the reader
  nothing but astonishment, and no instruction in the perfect life. Instead, as far as I can and
  with God's help, I will try to explain faithfully only their institutions and the rules of
  their monasteries. Above all, I will explain the origin and causes of the principal faults.
  They count eight of these. I will also explain the remedies for them, following their
  traditions. For my purpose is to say a few words, not about God's miracles, but about how to
  improve our character and reach the perfect life. In this I follow what we received from our
  elders.
relations:
- type: associated-with
  target: gallic.force.power-displayed-disowned
- type: associated-with
  target: gallic.gravity.virtus
use_note:
  means: "Cassian declares in the Institutes preface that he will not narrate the miracles he has heard and seen, but only the fathers' rules and remedies for faults."
  not_for:
    - "a denial that miracles happened, when Cassian says he saw some"
    - "Nesteros's teaching that humility outranks wonder-working, which sits in gallic.quote.humility-mistress-of-virtues-not-exorcism"
    - "an attack by name on Sulpitius or Martin"
    - "Cassian's admission that no one in Gaul kept Egypt's perseverance even a year, which sits in gallic.gravity.egypt-as-measure"
  years: {from: 415, to: 426}
  status: reviewed
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"weave a tale"` returns line 16503; `grep -n "received from our elders"` returns line 16515. Read
with `sed -n '16500,16517p'`, inside `<div2 ... id="iv.ii">` (the Institutes Preface). The quoted
span is one continuous sentence, "Nor certainly shall I try..." through "...received from our
elders.", read through to its own period, not cut mid-thought - it was the host record's own prior
wording that used a bare "..." here, dropping the middle of the sentence; this record restores it
in full.

Normalization: line breaks joined with single spaces; a translator's footnote on "veritate/
veritatem" was excluded as apparatus; the source's own curly apostrophes in "God's" (both
occurrences) are rendered here as straight apostrophes, the same mark in a different Unicode form.
No word was added, dropped, substituted, or reordered.