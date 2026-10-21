---
id: pahc.story.martyrdom-of-polycarp
world_id: post-apostolic-house-church
record_type: story
schema_version: 2
status: ready
register: emic
canon_cells:
- F6-E
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: contested
  formation_confidence: Contested
  divergence_note: "Contested on dating (c. 155-156 traditional vs. Eusebius's Chronicon 167 CE) and on whether this reflects a single-layer account (chs. 20-22 are widely regarded as later redactional additions) - see pahc.contested.martyrdom-polycarp-dating. Inferential-Thin for specific narrated details shaped by hagiographic and martyrological convention; the formation ideal the text conveys is the evidence, not the staged details as historical reporting."
sources:
- source_id: pahc.source.martyrdom-polycarp
  locus: "6, 9, 12, 15-16, 18"
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks what a formed life looks like when tested to its limit"
  - "participant asks about martyrdom as an ideal within this tradition"
  prefer_instead:
  - "participant needs this presented as verified historical reporting of specific events"
  - "participant is in a state where martyrdom content requires particular pastoral caution"
relations:
- type: associated-with
  target: pahc.gravity.martyrdom-meaning
- type: associated-with
  target: pahc.story.quintus-recantation
narrative_tier: 3
narrative_tier_justification: "This world's clearest Tier 3 case. Attributed to a specific figure and moment - Polycarp's arrest and death - and transmitted by the receiving community, framed within its own text as a letter from Smyrna to Philomelium, rather than direct documentation by Polycarp himself or a contemporaneous outside witness. Shaped throughout by recognizable hagiographic and martyrological convention (the theatrically staged arrest and death, the dies natalis framing, the bone-collection scene at ch. 18 explicitly echoing relic-veneration language). The text's own concluding chapters (20-22) are independently regarded as later additions - not smoothed over here."
tellable_as: The church at Smyrna remembers its aged bishop Polycarp refusing to curse Christ before the
  crowd. He was burned, then finished with a dagger. Afterward the church hoped to gather each year at
  the place where his bones were laid.
text: 'This is how the tradition remembers Polycarp. It is what the community that had known him believed
  a life fully given to our formation could become, even at its very end. The church at Smyrna tells of
  Polycarp, an aged bishop, urged by his own community to go into hiding. He withdrew briefly at their
  urging, and was then betrayed by someone in his own household, under torture. Brought before the proconsul,
  he was pressed to swear by Caesar''s fortune, curse Christ, and be spared. Polycarp answered: ''Eighty
  and six years have I served Him, and He never did me any injury: how then can I blaspheme my King and
  my Saviour?'' The tradition tells us the crowd first cried out for a lion to be loosed on him. But the
  games were already finished, and it was not lawful. So they cried out instead that he should be burned
  alive. When the fire was lit, it is said to have shaped itself into an arch, ''like the sail of a ship
  when filled with the wind,'' encircling him without touching him. An executioner was sent to finish
  him with a dagger - and at this, the account says, so much blood came out that it quenched the fire
  itself. The community gathered his bones afterward, ''more precious than the most exquisite jewels,
  and more purified than gold,'' to keep in a fitting place. There they would gather, ''as opportunity
  is allowed us,'' to celebrate the anniversary of his martyrdom - in memory of those who had already
  finished the course, and to prepare those still to walk it. This is the tradition''s own witness to
  what it believed formation could produce, told in the style the tradition used to honor its martyrs.
  No outside account survives to check it.'
telling: "This is how the church at Smyrna remembered Polycarp, its aged bishop, in a letter to the church at Philomelium. It is told in the style our tradition used to honor its martyrs, and no outside account survives to check it.\n\nHis community urged Polycarp to hide, and he withdrew for a time, until someone in his own household gave him away under torture. Before the proconsul he was pressed to swear by Caesar's fortune, curse Christ and be spared. Polycarp answered that he had served Christ for eighty-six years, and Christ had never done him any wrong. How then, he asked, could he blaspheme his King and his Savior?\n\nThe crowd first cried out for a lion, but the official in charge said it was not lawful, because the wild-beast shows were already over. So they cried out that he should be burned alive. When the fire was lit, the account says it formed an arch around him, like the sail of a ship filled by the wind. An executioner was sent to finish him with a dagger, and the account says so much blood came out that it put out the fire.\n\nAfterward the community gathered his bones, which they held more precious than the finest jewels, and laid them in a fitting place. There they hoped to gather each year, as they were able, to keep the day of his martyrdom. They would remember those who had finished the course and prepare those still to walk it."
absent_detail: "No independent, contemporaneous outside account of Polycarp's death survives to check this community's own memory against - this world has no Strand B counterpart of comparable narrative weight, and this inventory does not manufacture one to appear symmetrical."
modern_contrast: >
  A modern reader often hears the bone-collection and annual gathering
  as medieval-style relic veneration, and the fire/dove details as
  documented fact. This world's own record frames it differently: this
  is the tradition's own hagiographic memory (Tier 3), shaped by
  convention rather than transcript, and the bone-gathering is an early,
  much simpler instance of a practice - not yet the developed relic
  cult later centuries built from it.
use_note:
  means: "The church at Smyrna remembers Polycarp refusing to curse Christ, his burning, and its hope to gather each year at the place where his bones were laid."
  not_for:
    - "medieval-style relic veneration"
    - "the fire and dove details as documented fact"
    - "an independent outside account of his death"
  years: {from: 155, to: 156}
  status: reviewed
---
Re-derived from the approved Doc_09 Story 008. Every quotation checked
directly against cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml,
div1 iv, section iv: ch. 9 ("Eighty and six years..."); ch. 12 (the
crowd's demand for a lion, refused since "the shows of wild beasts
were already finished," followed by the cry to burn him alive); ch. 15
("like the sail of a ship when filled with the wind"); ch. 16 (the
dagger and "there came forth a dove... and a great quantity of blood,
so that the fire was extinguished" - the dove's own textual status is
independently disputed even in the ANF edition's own footnote, and is
not asserted here as settled); ch. 18 ("more precious than the most
exquisite jewels, and more purified than gold"). canon_cells: F6-E (f6-e-02) reinforces pahc.
force.martyrdom-meaning and pahc.gravity.martyrdom-meaning, the same
cell both already claim.

The narrative prose follows the project's approved register: short sentences, everyday words; every quotation kept character-exact; all hedges and outside-account framing kept.

A reciprocal `associated-with` edge connects this record to
`pahc.story.quintus-recantation` (same underlying letter, chs. 4-7, a
different passage and a different point). Checked directly against
that record for consistency: no contradiction found, and this record's
own "betrayed
by someone in his own household, under torture" already agrees with
the new record's more granular "two young men... one of them,
tortured."
