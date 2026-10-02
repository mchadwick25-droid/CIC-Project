# syr — Story index (Doc_09 record-native)

Derived from `records/syr/story/` (nine records re-expressing the approved Doc_09 Story Inventory, 2026-07-07/08, three review rounds + Validation Layer). One row per story.

| story record | legacy chunk | narrative tier | canon cells | source(s) | usage register |
|---|---|---|---|---|---|
| `ephrem-famine-death` | syrstory001 | 2 (reclassified from 1 at legacy Round 1 — carried) | F5-I | Palladius (vendored) + Sozomen III.16 (vendored); Gennadius noted | remembered history |
| `edessa-flood-201` | syrstory002 | 2 | F2-E | Chronicle of Edessa (vendored; verbatim-verified) | archival memory; Bauer/Barnard dispute carried |
| `jacob-nicaea` | syrstory003 | 2 | F1-I | Theodoret + Nisibene hymns (vendored) | community memory; never blended with the siege legend |
| `abgar-addai-legend` | syrstory004 | 3 | F4-E, F2-E | Doctrina Addai (vendored) + Eusebius I.13 kernel | foundation legend, told as legend; no image-not-made-by-hands, no Protonike-as-fact |
| `simeon-martyrdom` | syrstory005 | 3 | F6-E, F3-I | Sozomen II.9–10 (vendored); Smith's acts consult-only | hagiographic tradition; no improvised scenes for other martyrs |
| `jacob-deliverance` | syrstory006 | 3 | F3-I | Theodoret II.26 (vendored; gnats line verbatim-verified) + Nisibene hymns | miracle-as-tradition; Jacob prays, Ephrem urges — never reversed |
| `choirs-tradition` | syrstory007 | 3 (later-reception, per Doc_04's forward reference) | — (deliberate: later reception, not in-window fact) | Jacob of Serug memra (consult-only dossier) | two evidentiary layers never blended |
| `basil-legend` | syrstory008 | 3 (documented mistaken identity) | — (deliberate: retrieved only when raised) | Vita tradition (consult-only) + Sozomen III.16 kernel | correction attached in the telling |
| `qyama-morning` | syrstory009 | 4 (the one Tier 4; composite, element-sourced) | F5-I, F3-I | Dem 6 + hymns + harmony + calendar finding | typical practice, reconstruction stated in-frame |

**No-Tier-5 audit:** every record's `narrative_tier` ∈ 1–4 (gate `narratability` enforces the range mechanically); no invented narrative — the one composite (Tier 4) carries element-by-element sourcing and names its reconstruction character inside the telling. **Tier distribution: 0×T1, 3×T2, 5×T3, 1×T4** — the zero-Tier-1 finding is the approved repository's own conclusion (structurally literary-theological source ecology), carried, not compensated.

**Absent Stories (the required question):** answered substantively in `syr.core.syriac`'s trailing body (seven named absences with reasons: no ordinary believer's story, no covenant-daughter's own story, no child's story, no enslaved person's story, no Jewish interlocutor's story, no ordinary conversion story, near-nothing 373–410), each tied to the honest_limit records and the transmission force.

**Source cross-reference:** every story's sources resolve to registered `syr.source.*` records (gate `referential`); the two consult-only-sourced stories (7, 8) cite the registered later-reception dossier record, never vendored text.
