# Batch 11: era 1 traditions

The group: Mark's ruling "Era 1 traditions: thirteen rebuilt now, seven pushed off" (Decision-Log, 2026-11-25), through `Brief-Kit/kinds/tradition.md`. The three built worlds (`alexandria-catechetical`, `syriac-edessa-nisibis`, `post-apostolic-house-church`) also rebuild their census `entry` texts (`tile`, `intro`, `summary`, `recordHolds`), Open-Gaps 416. Each live `longDescription` was approved before the kit and is reviewed here. The writer keeps its wording wherever it passes. Grades: `Build/Ministry/Operations/Audits/2026-11-25_tradition-grades/Grades.csv`. Kit: `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`.

Each folder `<slug>/` holds `<slug>.brief.approved.txt`, the live `longDescription` as it stood on 2026-11-25. `Overlap_Report_Old_Texts.txt` is the one run of `tools/check_tree_overlap.py` on the thirteen old texts: all clear. A hand check of the House Church's five quotes under five words found none elsewhere on the tree either.

## The thirteen (approved)

| Census id | Half | Grade | Research order |
|---|---|---|---|
| `alexandria-catechetical` | A | F | first |
| `syriac-edessa-nisibis` | A | F | first |
| `antiochene-church-third-century` | A | F | first |
| `apocryphal-and-pseudepigraphal-literature` | A | F | first (shape question on the slate) |
| `greek-apologists-second-century` | A | F | first |
| `roman-church-third-century` | A | F | after Antioch's outline |
| `ebionite-nazoraean-current` | A | F | after Apocryphal's outline |
| `latin-pastoral-congregational-christianity` | B | F | after Roman Church's outline |
| `latin-apologists` | B | F | first in B |
| `post-apostolic-house-church` | B | D | after Greek Apologists' outline |
| `manichaeism` | B | F | after Latin Pastoral's outline |
| `marcion-marcionism` | B | F | after Latin Apologists' outline |
| `montanism-the-new-prophecy` | B | F | after Latin Apologists' outline |

Jobs, direct lines, siblings, the live stories beside each one, and quote bars: the slate, https://claude.ai/artifact/DsZbVTkmK5mK4YtSbe1mer (version 1).

## Steps
0. Slate: approved by Mark (2026-11-25, "Approve as recommended"; Decision-Log, "Batch 11: the slate approved").
1. Research (`<slug>/Researcher_Prompt.filled.md`, each a filled `roles/researcher.md`; all thirteen written). Half A first wave started 2026-11-25: Alexandria, Syriac, Antioch, Apocryphal, Greek Apologists. Roman Church waits on Antioch's outline, Ebionites on Apocryphal's. Half B (Mark, 2026-11-25: "Keep going on half B too"): Latin Apologists started 2026-11-25 (its header's Greek Apologists line reads that outline if done, otherwise the live text). House Church waits on Greek Apologists' outline, Latin Pastoral on Roman Church's, Manichaeism on Latin Pastoral's, Marcionism and Montanism on Latin Apologists'. Outlines done (2026-11-25): Alexandria, Syriac, Antioch, Apocryphal, Greek Apologists, Ebionites, Roman Church, Latin Apologists, House Church, Marcionism, Montanism. Latin Pastoral running; Manichaeism after it.

## Open items
- (Ruled) Slate decision 3: the Apocryphal entry is not a community. Recommended: tell it through the people who wrote, read, copied and judged the books (Serapion and the Gospel of Peter, Eusebius HE 6.12, held in `npnf201`; the presbyter of the Acts of Paul, Tertullian On Baptism 17, held in `anf03`).
- (Ruled, no change) Slate decision 4: three census lines the stories may touch, with no change recommended. Ebionites: Epiphanius's descent from the Pella believers. House Church: no continued-as line to the third-century churches of Antioch and Anatolia. Alexandria: the Contested gave-rise-to link to Desert Monasticism.
- `Story-Ledger.md` does not track traditions: `tools/list_story_status.py` counts only persons and councils (`KINDS`). For Open-Gaps at release, unless Mark rules otherwise.
- Pushed-off traditions (Open-Gaps 417, 418) come into these stories only as clauses: `novatianism`, `bardaisanite-current`, `modalist-monarchianism`, `valentinian-and-other-gnostic-christianities`, `anatolian-church-third-century`, `palestinian-church-pre-constantinian`.
- For the card step: the Montanism card's errors found at research (`montanism-the-new-prophecy/Source_Sheet.md`, G7): "after me…" credited to Eusebius (it is Epiphanius); Zoticus at Pepuza on the wrong witness; "proved" where the text reads "probed".
- For the hearts page (overlaps inside the slate's ruling, each to show Mark): House Church opens on Pliny's dawn hymn, which `pliny-the-younger` tells in narration, and quotes Justin's Sunday, which `justin-martyr` summarises; Marcionism quotes Theodoret on his eight Marcionite villages, which `theodoret-of-cyrrhus` tells in narration (not on the slate); Greek Apologists and Ebionites run witness by witness, the roll-call fault to watch; Roman Church's ending (251, or on to Dionysius of Rome) is Mark's call; Latin Apologists' "no words for it yet" is only partly held, and Tertullian coining the words is modern only.
- Before the pull request: bring `main` into this branch once #1806 has merged.

## Rulings
- "Batch 11: the slate approved" (Mark, 2026-11-25: "Approve as recommended"): the thirteen jobs and halves, the research order, Apocryphal told through the people who met the books, no census direct-line change, no quote reuse (the House Church drops the leopards scene), every story kept with its job split. This batch only.
