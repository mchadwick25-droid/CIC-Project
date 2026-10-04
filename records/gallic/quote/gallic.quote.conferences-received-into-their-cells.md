---
id: gallic.quote.conferences-received-into-their-cells
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
    Documented as Cassian's own text (Conferences Part III Preface, read at its locus for this
    record) - his own description of how Gallic monks were to use the Conferences he had already
    written.
sources:
- source_id: gallic.source.cassian-conferences-part-iii
  locus: "Preface III (npnf211 div iv.vi.i, file lines 42305-42325): Cassian's description of
    Gallic monks receiving the authors of the Conferences into their own cells, as living
    instruction"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks how Gallic monks actually used the written Conferences"
  - "participant asks what it meant for a text to stand in for an absent Egyptian teacher"
  prefer_instead:
  - "participant wants Cassian's own broader adaptation method - retrieve gallic.quote.cassian-adapts-egypt-to-gaul"
text: >-
  And to this your previous efforts and labours have especially
  contributed this, that, as they are already prepared and practiced in
  these exercises, they can more readily receive the precepts and
  institutes of the Elders, and receiving into their cells the authors
  of the Conferences together with the actual volumes of the
  Conferences and talking with them after a fashion by daily questions
  and answers, they may not be left to their own resources to find that
  way which is difficult and almost unknown in this country, but full
  of danger even there where well-worn paths and numberless instances
  of those who have gone before are not wanting, but may rather learn
  to follow the rule of the anchorite's life taught by their examples,
  whom ancient tradition and industry and long experience have
  thoroughly instructed.
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  "Receiving into their cells the authors of the Conferences" is not literal - the Egyptian elders
  themselves never traveled to Gaul. Cassian means the written volumes stand in for the living
  teacher, read and talked with, in a country where the anchorite's road has no well-worn path of
  its own to follow yet.
modern_rendering: >-
  Your earlier efforts and labours have made a special contribution to this. The brothers are
  already prepared and practiced in these exercises. So they can more readily receive the
  precepts and institutes of the Elders. They can receive into their cells the authors of the
  Conferences, together with the actual volumes of the Conferences. In a way, they can talk with
  them through daily questions and answers. So they will not be left to their own resources to
  find that way. That way is difficult and almost unknown in this country. But it is full of
  danger even there, where well-worn paths and countless examples of those who went before are
  not lacking. Instead, they may learn to follow the rule of the anchorite's life, taught by the
  examples of the Elders. Ancient tradition, diligence, and long experience have thoroughly
  instructed these Elders.
relations:
- type: associated-with
  target: gallic.gravity.egypt-as-measure
use_note:
  means: "Cassian writes in the Part III preface that Gallic monks may receive the Conferences' authors into their cells through the books and learn the anchorite's rule from them."
  not_for:
    - "a claim that Egyptian elders physically came to Gaul"
    - "a well-trodden anchorite path in Gaul, when Cassian calls the way almost unknown there"
  years: {from: 426, to: 435}
  status: provisional
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"receiving into their cells the authors"` returns line 42316; read with `sed -n '42300,42326p'`,
inside `<div2 ... id="iv.vi">` (Conferences Part III, its own Preface, immediately before the
div3 for Conference XVIII begins). The quoted span is one continuous sentence, "And to this your
previous efforts..." through "...thoroughly instructed.", ending at its own period.

Normalization: line breaks joined with single spaces; the source's own curly apostrophe in
"anchorite's" is rendered here as a straight apostrophe, the same mark in a different Unicode form.
No word was added, dropped, substituted, or reordered.