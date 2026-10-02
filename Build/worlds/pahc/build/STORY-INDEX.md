# pahc Story Index

**GENERATED from records/pahc/story/ — do not hand-edit.** Regenerate with `python3 Build/worlds/pahc/build/generate_story_index.py` after any story change. Companion to Doc_09 (Story Inventory), re-derived from the approved `CiC_W1_Doc09_Story_Inventory.md` and its 13 deployment chunks under the new records regime.

**Total stories:** 13 (Tier 1: 7, Tier 2: 0, Tier 3: 1, Tier 4: 5) - matches Doc_09's own catalog (seven Tier 1, one Tier 3, five Tier 4, zero Tier 2).

## No Tier 5 check

CONFIRMED: no story carries a narrative_tier outside 1-4.

## Story catalog

| id | tier | canon_cells | formation_confidence | gravity/force connections |
|---|---|---|---|---|
| pahc.story.day-under-bishop-and-presbyters | 4 (Historically Grounded Reconstruction) | F3-I | Inferential-Thin | G:authority-consolidation, G:liturgical-practice, G:translocal-network |
| pahc.story.didache-eucharist | 4 (Historically Grounded Reconstruction) | F4-I | Inferential-Thin | G:liturgical-practice |
| pahc.story.first-clement-corinthian-dispute | 1 (Documented Historical Narrative) | F3-P | Widely Accepted | G:authority-consolidation, G:translocal-network |
| pahc.story.hermas-visions | 1 (Documented Historical Narrative) | F4-I | Widely Accepted | G:authority-consolidation |
| pahc.story.ignatius-guarded-journey | 1 (Documented Historical Narrative) | F6-E | Widely Accepted | G:translocal-network, G:martyrdom-meaning, G:boundary-drawing, G:authority-consolidation, G:liturgical-practice |
| pahc.story.justin-sunday-gathering | 1 (Documented Historical Narrative) | F4-I | Widely Accepted | G:liturgical-practice |
| pahc.story.martyrdom-of-polycarp | 3 (Attributed Tradition) | F6-E | Contested | G:martyrdom-meaning |
| pahc.story.mutual-aid-prisoner | 4 (Historically Grounded Reconstruction) | F5-T | Inferential-Thin | - |
| pahc.story.nero-scapegoating | 1 (Documented Historical Narrative) | F3-I | Widely Accepted | F:neronian-persecution, G:authority-consolidation |
| pahc.story.one-eucharist-under-bishop | 4 (Historically Grounded Reconstruction) | F3-T | Inferential-Thin | G:liturgical-practice, G:authority-consolidation, G:boundary-drawing |
| pahc.story.pliny-interrogation | 1 (Documented Historical Narrative) | F6-E | Documented | G:state-pressure |
| pahc.story.polycarp-forwards-letters | 1 (Documented Historical Narrative) | F5-P | Documented | G:translocal-network |
| pahc.story.two-ways-catechumen | 4 (Historically Grounded Reconstruction) | F4-I | Inferential-Thin | F:two-ways-catechetical-inheritance, T:two-ways |

## Story-to-gravity connection summary (mechanically derived from relations[])

- **pahc.gravity.authority-consolidation**: pahc.story.day-under-bishop-and-presbyters, pahc.story.first-clement-corinthian-dispute, pahc.story.hermas-visions, pahc.story.ignatius-guarded-journey, pahc.story.nero-scapegoating, pahc.story.one-eucharist-under-bishop
- **pahc.gravity.boundary-drawing**: pahc.story.ignatius-guarded-journey, pahc.story.one-eucharist-under-bishop
- **pahc.gravity.liturgical-practice**: pahc.story.day-under-bishop-and-presbyters, pahc.story.didache-eucharist, pahc.story.ignatius-guarded-journey, pahc.story.justin-sunday-gathering, pahc.story.one-eucharist-under-bishop
- **pahc.gravity.martyrdom-meaning**: pahc.story.ignatius-guarded-journey, pahc.story.martyrdom-of-polycarp
- **pahc.gravity.state-pressure**: pahc.story.pliny-interrogation
- **pahc.gravity.translocal-network**: pahc.story.day-under-bishop-and-presbyters, pahc.story.first-clement-corinthian-dispute, pahc.story.ignatius-guarded-journey, pahc.story.polycarp-forwards-letters

## Absent Stories (reconciled: pahc.core.house-church x Doc_09 Section 4)

world_core's own trailing body already reconciles the count difference between its own 11-item list and Doc_09's own 12-item list: Doc_09's old item 8 (two then-unregistered Ignatius citations) was a citation-discipline housekeeping note, resolved by this build's own letter-level source scope, and "was never an absent STORY" - so 11 items is the correct, reconciled count, not a discrepancy. Restated here as a single generated list, cross-referencing both records so neither has to be read to get the full picture.

1. **No Strand B (Rome) martyrdom account exists.** (world_core item 1; Doc_09 item 1)
   Actively tested (Doc_05 SS10 Open Item 6), came up empty. Whether this reflects genuine lived difference or a transmission accident stays open - not resolved by inventing a Strand B counterpart to pahc.story.martyrdom-of-polycarp.
2. **No enslaved member's narrative survives in their own voice.** (world_core item 2; Doc_09 item 4)
   The two ministrae Pliny tortured (pahc.story.pliny-interrogation) are the closest approach, and they speak only through their torturer's report.
3. **No ordinary, non-elite member's story exists at all, in either strand.** (world_core item 3; Doc_09 item 5)
   Every story in this repository is authored by, or filtered through, a literate leadership-tier voice or a hostile outside observer.
4. **No woman's own told story survives.** (world_core item 4; Doc_09 item 9 (the named household salutations - Tavia/Gavia, the wife of Epitropus - are the only place an ordinary individual is named at all, and even there nothing survives beyond a name and a greeting))
   This inventory does not construct a narrative for either named woman where none survives.
5. **No genuine Tier 2 (Collected and Traditional Material) story exists for this world.** (world_core item 5; Doc_09 item 6)
   No sayings-collection or anecdotal-tradition genre, distinct from direct correspondence and hagiographic attribution, survives in this world's own Native evidentiary base. Structural, not an oversight.
6. **No household-based ("house church") story can be grounded in this world's own primary voices.** (world_core item 6; Doc_09 item 7)
   G06 (household as basic unit) did not reach gravity status (see GRAVITY-INDEX.md's own Not-Advanced section) and Doc_03 independently confirmed no primary voice uses oikos as a technical self-designation for a meeting unit.
7. **No material-culture or archaeological story is possible.** (world_core item 7; Doc_09 item 10)
   This world's window is archaeologically invisible across all three regions - the same finding pahc.limit.f5-e-material-remains answers as an honest_limit.
8. **No institutional-record story is possible.** (world_core item 8; Doc_09 item 11)
   No membership rolls, council minutes, or administrative documents survive; every institutional story in this repository is reconstructed from occasional, persuasive, or polemical correspondence.
9. **Marcion, Valentinus, and Montanism appear nowhere in this repository as protagonists, and should not.** (world_core item 9; Doc_09 item 12)
   Live, contemporary, undefeated rival movements (pahc.contested.rivals-undefeated) - referenced as antagonist backdrop in pahc.story.ignatius-guarded-journey and pahc.story.one-eucharist-under-bishop, never narrated from inside.
10. **G04 and G05 are both Strand-A-only, and both are severely thin even within Strand A.** (world_core item 10; Doc_09 item 2)
   G04 rests on exactly two data points (pahc.story.ignatius-guarded-journey's own martyrdom references, plus pahc.story.martyrdom-of-polycarp); G05 rests on exactly one voice, Ignatius alone. No third story is added to thicken either beyond what the gravity records themselves support.
11. **This world's most narratively vivid material is overwhelmingly Strand A, and this repository does not smooth that imbalance.** (world_core item 11; Doc_09 item 3)
   Strand A supplies the journey, the martyrdom, the one-eucharist program - vivid, high-stakes, individually attributed. Strand B supplies institutional correction and visionary report, genuinely different in kind. pahc.story.day-under-bishop-and-presbyters is this repository's own attempt to hold both strands in explicit parallel, not to manufacture vividness Strand B's evidence does not supply.

## Relation reciprocity check (mechanical, story records only)

All story relations reciprocate.

---
<!-- generated by generate_story_index.py -->
