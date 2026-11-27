# Batch 12: era 1 people, then the era 1 brief

The group: the 20 era 1 people graded F or D in `Build/Ministry/Operations/Audits/2026-11-25_person-council-grades/Rebuild_Order.csv`, through `Brief-Kit/kinds/person.md`, then the era 1 brief through `Brief-Kit/kinds/era.md`. Mark set this as the next step (Decision-Log, "What 'era 1 complete' means", 2026-11-26; Mark, 2026-11-26: "5. yes this is the next step before 3 and 4." and "3. i want to fully finish all content for era one before moving on"). No story approved before the kit is reviewed here. Kit: `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`.

Each folder `<slug>/` holds `<slug>.brief.live.txt`, the live `longDescription` as it stood on 2026-11-26 (`main` at `54b4a738`). `Overlap_Report_Old_Texts.txt` is the one run of `tools/check_tree_overlap.py` on the twenty live texts: all clear. A hand check of their quotes under five words found two short spans shared with other stories ("two Gods", Hippolytus and `roman-church-third-century`; "every race of people", Justin and `marcion-of-pontus`), listed on the slate.

Stops go to Mark through the coordinator session (`session_01JMNsSDxiDjhkPh1K48BmfL`) with send_message; his words come back verbatim. The card-site build runs alongside and changes the census schema (`meta`), `cft-website/index.html` and the tree page generator: bring the branch up to date with `main` before merging. No recording in this batch (Decision-Log, "No person or story recordings until a new voice", 2026-11-26); each live recording stays until a new one replaces it (change order, 2026-11-26).

## The twenty (approved)

| Census id | Part | Grade (overall, rigor/craft) | Research order |
|---|---|---|---|
| `tacitus` | A | F, F/C | first |
| `suetonius` | A | F, F/D | after Tacitus's outline |
| `josephus` | A | F, F/B | first |
| `justin-martyr` | A | D, B/D | first |
| `tatian` | A | F, F/B | after Justin's outline |
| `ignatius-of-antioch` | B | D, D/B | first |
| `valentinus` | B | D, B/D | first |
| `bardaisan-of-edessa` | B | D, D/C | after Valentinus's outline |
| `hippolytus-of-rome` | B | F, F/B | first |
| `clement-of-alexandria` | B | D, B/D | first |
| `tertullian-s-voice` | C | D, D/C | first |
| `cyprian-of-carthage` | C | D, D/C | after Tertullian's outline |
| `pontius-the-deacon` | C | F, F/C | after Cyprian's outline |
| `lactantius` | C | F, F/C | after Tertullian's and Cyprian's outlines |
| `origen` | D | D, B/D | after Clement's outline |
| `methodius-of-olympus` | D | F, B/F | after Origen's outline |
| `pamphilus-of-caesarea` | D | D, D/B | after Origen's outline |
| `eusebius-of-caesarea` | D | F, F/C | after Pamphilus's outline |
| `anatolius-of-alexandria-and-laodicea` | D | F, F/C | first |
| `peter-of-alexandria` | D | F, F/B | first |
| era 1 brief | E | — | after the twenty outlines |

Jobs, homes and direct lines, siblings, the live stories beside each, and quote bars: the slate, https://claude.ai/artifact/5VuWiHRad1q1gPoEXnwzFz (version 1).

Earlier research, as pointers only (decision 2): batch 3 (`justin-martyr`), batch 4 (`clement-of-alexandria`), batch 6 (`josephus`, `tatian`, `hippolytus-of-rome`, `suetonius`, `tacitus`, `ignatius-of-antioch`, `valentinus`, `bardaisan-of-edessa`), batch 7 (the rest), and for `origen` and `methodius-of-olympus`, `2026-11-16_eight-standard-v1`.

## Steps
0. Slate: sent to Mark through the coordinator, 2026-11-26. Paused by Mark the same day, as the coordinator relayed it: "i want everything else done with batch 11 and other system work before starting batch 12". The slate is not approved; no research starts. The coordinator brings it back to Mark when he is ready.
   Pause lifted (Mark, 2026-11-27, as the coordinator relayed it): "we can also start batch 12 work". He gives his slate ruling directly in this session. Before it, on 2026-11-27: `main` (`556d8243`) merged into the branch, cleanly. None of the twenty census entries changed (text, card, home), no edge was added or removed, and `check_tree_overlap.py` on the twenty live texts gives the same all-clear. Each quote the slate bars still stands where the slate says. The slate holds as sent. The era 1 cards thread (`session_01JMNsS9jvf8MiuJ4c5BaFtq`) is writing these twenty people's cards now; bring `main` in again right before release, and raise any person both threads touch through the coordinator.
   Approved (Mark, 2026-11-27: "approve the slate as recommended"; Decision-Log, "Batch 12: the slate approved").
1. Research (`<slug>/Researcher_Prompt.filled.md`, each a filled `roles/researcher.md`, all twenty written 2026-11-27; `<slug>/Card.existing.json` is the census card as it stood then). The parts run in fresh hands: each researcher is a fresh Opus agent started from its prompt file alone, so this coordinating session carries only their replies. First wave started 2026-11-27: Tacitus, Josephus, Justin, Ignatius, Valentinus, Hippolytus, Clement, Tertullian, Anatolius, Peter. Waiting: Suetonius (Tacitus), Tatian (Justin), Bardaisan (Valentinus), Cyprian (Tertullian), Origen (Clement), then Pontius (Cyprian), Lactantius (Tertullian, Cyprian), Methodius and Pamphilus (Origen), Eusebius (Pamphilus), the era brief (all twenty).
   Outlines done: Valentinus (2026-11-27; about 525 words; gaps: Clement's Greek not held, ANF prints quote 3's speaker as "Valentinian", the Hippolytus psalm damaged and sent to the card). Bardaisan started.
   Anatolius (2026-11-27; about 600 words, Cut first to about 525; Founder or leader; quote 1 runs about 90 words, for the outline check; gaps: no dates for birth, death, ordination or siege; Stephen's Life of Wilfrid not held; Columbanus to the Gallic bishops told in narration; it reports no reading of the census `longDescription`).
   Tacitus (2026-11-27; about 530 words after Cut first; Outside witness; Latin held in Mirbt 1911 from Halm; not held: the fire chapters, the Histories; a census search showed two fragments of the live text, nothing taken). **For the outline check and the hearts page:** its connection names Bradlaugh's 1876 doubt of the passage. The live text's grade faulted the 1876 debate, and the kit bars a modern view told as the record: the check rules whether it can stand as an event or goes to the card. Suetonius started.
   **For the reviews (prompt gap):** the first ten prompts barred the live story's files but not the census `longDescription`, which is the live story. The Valentinus researcher read it by accident while pulling census fields and says nothing came from it; the reviewer checks that brief for echoes of the live text. The ten later prompts bar it. The other nine first-wave researchers may have done the same: each reply is checked for it.


## The slate's six decisions (approved as recommended)
1. Four parts (A to D) plus the era as E, each in its own fresh session, in place of the kit's two halves of about six.
2. A new source sheet and outline for each person; the old ones are pointers only; the live wording is not kept.
3. No census change: Valentinus's break, Tatian's Encratites, the Melitian break with Peter's church, Pamphilus's home (Caesarea), Hippolytus's rival church. The Melitian line and Pamphilus's home are noted in Open-Gaps for a later census pass.
4. At release, a person whose recording is of an older text keeps the file, manifest entry and times, and the player is hidden (as Open-Gaps 413); nothing is removed.
5. The era brief is part E; its heart and length are ruled on the hearts page; where it lives in the census is settled with the card-site thread at its card step.
6. No quote reuse. The barred quotes are listed on the slate.

## Rulings
- "Batch 12: the slate approved" (Mark, 2026-11-27: "approve the slate as recommended"): decisions 1 to 6 above, the twenty jobs and the research order. This batch only.
- For the release: Open-Gaps entries for the Melitian break line and Pamphilus's census home (decision 3).
- Cards (Mark, 2026-11-26, as the coordinator relayed it): "this thread does what it has and when batch 12 runs it then does the card refinements like now on new material". A separate era 1 card thread writes cards for every era 1 person, these twenty included, from their current briefs. When batch 12 runs, it rebuilds each brief, then refines that person's card (the card thread's version, as it then stands in the census) on the new material, with the same card role (`roles/card.md`) and checks. Batch 12 stays paused.
