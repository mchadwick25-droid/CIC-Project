---
id: desert.story.kellia-day
world_id: desert-monasticism
record_type: story
schema_version: 2
status: draft
register: emic
canon_cells: [F4-I, F5-E]
confidence:
  citation_specificity: C
  verification_state: verified-via-authority
  evidentiary_weight: illustrative
  formation_confidence: Inferential-Thin
  divergence_note: "Inferential/Thin throughout, per the prior build's cleared Story Repository Chunk Template's own rule: a Tier 4 reconstruction always carries this level regardless of individual element quality, since the reconstruction itself - assembling several independently attested elements into one day - is not itself independently attested as a single account."
sources:
- source_id: desert.source.apophthegmata-patrum
  locus: "the constant/near-constant Psalter recitation this world's own tradition attests as the substrate of prayer"
- source_id: desert.source.kellia-excavations
  locus: "the cell as basic architectural unit - single cells to multi-room hermitages, each with an attached oratory"
- source_id: desert.source.athanasius-vita-antonii
  locus: "SS3 - working with his hands from the start of his own withdrawal"
  license: public-domain
- source_id: desert.source.palladius-lausiac-history
  locus: "ch. VII - Nitria's linen-manufacture, self-supporting labor, matching desert.gravity.manual-labor's own registered evidence (a comparable settlement, not Kellia itself); the same chapter's church-attendance passage desert.term.synaxis registers for the weekly gathering"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks what an ordinary day actually looked like in this world"
  - "participant asks about the cell, the settlement, or what physical remains would show"
  - "participant asks how prayer, work, and communal gathering fit together in the daily rhythm"
  do_not_retrieve_when: []
relations:
- type: associated-with
  target: desert.gravity.withdrawal
- type: associated-with
  target: desert.gravity.manual-labor
- type: associated-with
  target: desert.term.synaxis
narrative_tier: 4
narrative_tier_justification: "Tier 4 (Historically Grounded Reconstruction), explicitly marked as reconstruction, every element separately sourced below - per the Story Repository Chunk Template's own rule, an element this document cannot source to a specific attested passage is removed from the text rather than retained with a caveat; a general diet clause from the prior build's own first draft was removed for exactly that reason and is not reinstated here."
tellable_as: "a typical day at Kellia - not one person's own recorded day, but what the settlement's own evidence lets us reconstruct together"
text: >-
  In a typical day at a settlement like Kellia, the day opened and closed with
  the Psalms. They were recited through the daylight hours alongside manual
  work - handwork done both to make a living and as a discipline in its own
  right, as we did from the very first day we took up this life. The work was
  done in the cell's own workspace. The cell itself might be a single small
  room, or a larger dwelling with several rooms, each with its own attached
  place of prayer. It was not a barracks room, but not always one person
  living entirely alone either. Once a week, on the turn from Saturday to
  Sunday, we left the cell and walked to the settlement's gathering place for
  the synaxis: a vigil, worship, and a meal eaten together. Then we returned
  to the week's own solitude.
absent_detail: "This is not a single person's own recorded day but a reconstruction from several independently attested elements; no surviving source narrates one specific day this way. An earlier draft of this account included a general note about spare or limited meals; no specific attested passage could be found to source that detail, and per this build's own rule it was removed rather than kept with a caveat."
modern_contrast: "A modern reader may hear \"a typical day\" and reach for the contemporary genre of routine-optimization content - a schedule to adopt for its own productivity value. This world's own record frames the same rhythm (Psalms, manual work, the cell) as formation, not efficiency: the labor was itself a discipline as much as a livelihood (desert.gravity.manual-labor), not a productivity technique borrowed from elsewhere."
---
Re-derived from the prior build's cleared Doc_09a Story 4.1, including
its own Round 1 fix (the unsourced diet element removed rather than
retained-and-flagged, per the Story Repository Chunk Template's own
rule) - carried forward as already corrected rather than reintroducing
the removed element.

Step4, Round 1 review Finding S3: this record's own body previously
claimed the weekly synaxis element "is not independently re-sourced to
a registered record in this build," used to justify retaining an
element the Tier 4 rule this same field quotes says must be removed if
unsourced. That claim was false: desert.term.synaxis is a registered,
cleared, verified-direct term record anchored to vendored Palladius ch.
VII ("They occupy the church only on Saturday and Sunday"), which this
record now cites directly (relations[], sources[]) rather than treating
as absent. The manual-labor element, also previously unsourced despite
the field's own "every element separately sourced" claim, is sourced to
Vita SS3 and Palladius ch. VII. Finding M13: "solitude here meant a
household of one, not a shared cell" overclaimed against
desert.source.kellia-excavations's own "single cells to multi-room
hermitages" - corrected to state both configurations. Finding M11: the
declared relation to desert.gravity.diakrisis was justified as "the
discipline of a fixed daily rhythm," which that gravity's own
description (judging rightly between thoughts, practices, and counsels)
does not support - removed; this record's relations are now limited to
what its own text actually illustrates.

Step4, Round 2 review Finding S8: the Round 1 fix above had written
"weaving rope or baskets" into the compiled text and "linen-manufacture
and weaving" into the Palladius locus - "weaving," "rope," and "basket"
occur zero times in ch. VII, which names only "linen-manufacture."
desert.gravity.manual-labor's own registered evidence for the identical
claim is likewise "linen-manufacture," not weaving, rope, or baskets;
the Round 1 fix note's claim that the two records now matched was
false. Corrected above to the manual-labor discipline itself, as that
gravity record's own description states it ("hand-work done both to
live and as a discipline in its own right"), rather than a specific
craft the corpus does not attest for this settlement. Also noted: ch.
VII describes Nitria, not Kellia; the locus above now states this
explicitly rather than implying the same settlement.

Formation significance: synthesizes desert.gravity.withdrawal and
desert.gravity.manual-labor, together with desert.term.synaxis's own
weekly rhythm, into one reconstructed day. Answers F4-I ("How did a
person actually become one of you? Walk me through it.") and F5-E ("If
archaeologists dug up the place you met, what would they find?")
together - the architectural and the practiced day read as one account.

BAR SWEEP (2026-08-29, Mark: "much better thats the bar"): text rewritten to the approved sample's level - short sentences, everyday words; every claim, name, quote, hedge, and reviewed constraint kept.
