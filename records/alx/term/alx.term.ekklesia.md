---
id: alx.term.ekklesia
world_id: alexandria-catechetical
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells:
- F3-I
- F3-T
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
- source_id: alx.source.clement-stromateis
  locus: "VII.5 (the Church as \"the assemblage of the elect\" made holy \"through knowledge\")"
  license: public-domain
- source_id: alx.source.athanasius-festal-letters
  locus: "(annual formation calendar)"
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - what the church is here, or why formation cannot be a private, solo pursuit
  - how the school's community and the whole gathered community relate
  do_not_retrieve_when:
  - asking about a specific local congregation's practical life
  - asking primarily about the bishop's own role rather than the community as a whole (retrieve
    alx.term.episkopos)
relations:
- type: associated-with
  target: alx.term.episkopos
plain_meaning: Not a building or a members list, but the assembly gathered around the Logos who calls
  it.
world_word: ekklesia
false_friend:
- a building where Christians meet
- an organization with a membership roll
senses:
  informational: Ekklesia means the called-out assembly - people gathered because the Logos addressed
    them and they answered, not an institution someone joined by registering. The community exists
    because formation cannot happen alone.
  evidential: 'Clement treats the community as where genuine knowledge actually develops, not merely
    where it is announced: the Church is holy "through knowledge," and is "not now the place, but the
    assemblage of the elect"; Athanasius''s Festal Letters show a bishop governing the whole community''s
    shared formation life across a year, not just an organization''s calendar.'
  personal: A baptized person who never shares in the community's actual life belongs only in name; a
    catechumen not yet baptized but genuinely praying and learning with others is, in the sense that
    matters, more fully inside the church.
  translational: >-
    Isn't the church basically a building or an organization with members? This world meant something
    different - an assembly constituted by people actually gathered around the Logos, not by a roll of
    names.
quick_meaning: Not a building or a members list - the assembly gathered around the Logos.
distortion_risk: high
---
Imported from the old system's richer lexicon (alexlex043, "Church / Ekklesia") at Mark's direction, as
a draft, not a final version.

corrected 2026-09-08, records/alx audit: the evidential claim was
cited to Quis Dives Salvetur "(whole)", but that work is an exposition
on wealth and salvation with "Church" appearing only 5 times, mostly
in its closing narrative, and does not support the "genuine knowledge
and love actually develop" framing. Stromateis VII.5 ("The Holy Soul a
More Excellent Temple Than Any Edifice Built by Man") directly
supports it: "how shall we not with propriety call the Church holy,
through knowledge... For it is not now the place, but the assemblage
of the elect, that I call the Church." Sources and wording were
corrected to cite alx.source.clement-stromateis at VII.5; the Quis
Dives citation, doing no other work in this file, was removed rather
than kept for a narrower point.
