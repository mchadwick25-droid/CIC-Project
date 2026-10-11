---
id: desert.story.kellia-day
world_id: desert-monasticism
record_type: story
schema_version: 2
status: ready
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
absent_detail: "This is not a single person's own recorded day but a reconstruction from several independently attested elements; no surviving source narrates one specific day this way. No specific attested passage was found to support a general note about spare or limited meals, so none is given."
modern_contrast: "A modern reader may hear \"a typical day\" and reach for the contemporary genre of routine-optimization content - a schedule to adopt for its own productivity value. This world's own record frames the same rhythm (Psalms, manual work, the cell) as formation, not efficiency: the labor was itself a discipline as much as a livelihood (desert.gravity.manual-labor), not a productivity technique borrowed from elsewhere."
use_note:
  means: "This is a reconstruction, not a recorded day, assembling attested elements of psalms, hand-work, cell life, and the weekly gathering into a typical Kellia day."
  not_for:
    - "Presenting it as one person's own recorded day"
    - "Adding details such as spare meals, which no attested passage supports"
    - "Presenting the Nitria linen evidence as Kellia's own, or applying the day to Pachomian houses"
  years: {from: 320, to: 430}
  status: reviewed
---
The unsourced diet element is not included.

The weekly synaxis element is sourced to desert.term.synaxis, a
registered, verified-direct term record anchored to vendored Palladius
ch. VII ("They occupy the church only on Saturday and Sunday"), cited
directly in relations[] and sources[]. The manual-labor element is
sourced to Vita SS3 and Palladius ch. VII. The text states both
configurations desert.source.kellia-excavations attests ("single cells
to multi-room hermitages"), rather than a household of one alone. This
record's relations are limited to what its own text actually
illustrates.

The compiled text names the manual-labor discipline itself, as
desert.gravity.manual-labor's own description states it ("hand-work
done both to live and as a discipline in its own right"), rather than a
specific craft ("weaving," "rope," "basket") that occurs zero times in
ch. VII, which names only "linen-manufacture." Ch. VII describes
Nitria, not Kellia; the locus states this explicitly rather than
implying the same settlement.

Formation significance: synthesizes desert.gravity.withdrawal and
desert.gravity.manual-labor, together with desert.term.synaxis's own
weekly rhythm, into one reconstructed day - the architectural and the
practiced day read as one account.
