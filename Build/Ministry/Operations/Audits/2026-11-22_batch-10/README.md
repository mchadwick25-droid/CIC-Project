# Batch 10: era 2, Antioch to Chalcedon and the edges of the empire

The group: Mark's approval in the batch 8 slate (Decision-Log, "Batch 8: the slate approved", 2026-11-21, item 3), with John Chrysostom and Ephrem the Syrian reviewed under "Change order: the stories approved before the kit go through review in their era's batch" (2026-11-19). Quote rule: "A quote may be used in more than one story where its author influenced more than one tradition or person" (2026-11-21). Kit: `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, as it stands after "Brief kit change for batch 10" (2026-11-22). The slate as Mark approved it: https://claude.ai/artifact/Vko3AEdprCTWnU717L7LFk (version 1); Decision-Log, "Batch 10: the slate approved" (2026-11-23).

Every story already has a census entry; none needs a new one. `Overlap_Report_Old_Texts.txt` is the one run of `tools/check_tree_overlap.py` on the twelve old texts (ten clear; Cassian and Priscillian each share a quote that the slate lists as a reuse).

## The twelve and their jobs (approved)

| Census id | Half | Shape | Siblings and order |
|---|---|---|---|
| `council-of-ephesus-431` | A | Council | Live: `nestorius`, `cyril-of-alexandria` (each tells Ephesus from its side). In the batch: `theodoret-of-cyrrhus`, `pelagius` (a clause each way). |
| `eutyches` | A | Teacher or thinker | `theodoret-of-cyrrhus` (449). Live: `leo-of-rome`, `council-of-chalcedon-451`. Home kept for now; tested in research. |
| `theodoret-of-cyrrhus` | A | Teacher or thinker | Researched after the Ephesus and Eutyches outlines. |
| `pelagius` | A | Teacher or thinker | Links: Ephesus, Cassian. Live: `augustine-of-hippo`, `jerome`. |
| `john-cassian` | A | Monk or ascetic | Links: Chrysostom, Pelagius, Ephesus. Live: `evagrius-ponticus`, `leo-of-rome`. |
| `john-chrysostom` | A | Reviewed | Approved before the kit; joins at review. |
| `rufinus-of-aquileia` | B | Missionary or translator | `frumentius` (shared text). Live: `jerome`, `pamphilus-of-caesarea`. |
| `frumentius` | B | Missionary or translator | Researched after Rufinus's outline. |
| `mesrop-mashtots` | B | Missionary or translator | Later: `koriun`, `eznik-of-kolb`. Koriun held in French only. |
| `ulfila` | B | Missionary or translator | Live: `arius`, `eusebius-of-nicomedia`. Later: `auxentius-of-durostorum`. |
| `priscillian` | B | Martyr | Live: `martin-of-tours`. Later: `sulpicius-severus`. |
| `ephrem-the-syrian` | B | Reviewed | Approved before the kit; joins at review. |

Each story's job line, direct line and siblings as approved are in its `<slug>/Researcher_Prompt.filled.md` header, copied from the slate. Each folder holds `Card.existing.json`, the census `card` (or `council`) field.

## Quotes
Lifted for the job the slate names, one per line in `Allowed_Reuse.txt`: Ulfila's creed ("alone unbegotten", "subject and obedient in all things", from `arius`); Sulpicius on Priscillian's accusers (`sulpicius-severus`); Gennadius's "brands as injurious" and "which the church of God finds salutary" for Cassian; Socrates's "that more credit was due to him who had suffered" for Rufinus; Cyril's "one incarnate nature of the Word" for Eutyches, only where his own appeal calls on it; Theodoret's History lines in `alexander-of-alexandria` and `ossius-of-cordoba`. Barred: every quote in `nestorius` and `cyril-of-alexandria` for Ephesus; Leo's two "robbery" lines and Chalcedon's text for Eutyches and Theodoret; Rufinus's "Who but you" (`jerome`, Mark kept the bar) and "is said to have written" (`pamphilus-of-caesarea`); Martin's plea at Trier (`martin-of-tours`) for Priscillian; Evagrius's lines for Cassian; editors' verdicts; every quote in Chrysostom's and Ephrem's live texts. Inside the batch, no quote is shared.

## Steps
0. Slate: approved by Mark (2026-11-23).
1. Research (`<slug>/Researcher_Prompt.filled.md`): eight started 2026-11-23; Theodoret after the Ephesus and Eutyches outlines, Frumentius after Rufinus's. All ten outlines done (2026-11-23); independent count in `Length_Count.md` (all ten over). Hearts and lengths approved by Mark (2026-11-23; `Hearts.md`). All ten Cut first lists added (each brings the count under the approved length).
2a. Outline check (`<slug>/Checker_Prompt.filled.md`), fix pass (`Fixes.md`) and recheck (`Recheck.md`, with `Recheck_Applied.md` where its replacements were applied word for word): all ten through (2026-11-23).
2. Outline check.
3. Write (`<slug>/Writer_Prompt.filled.md`, Opus): all ten drafted 2026-11-23 (`<slug>/Writer_Reply.md`). Four fit; six run past 675 (Theodoret 817, Cassian 788, Rufinus 740, Priscillian 734, Pelagius 733, Ulfila 722). To Mark with Ulfila's creed: https://claude.ai/artifact/7MQqQakPhBCKbugYP8zojp (version 1).
4. Review (`<slug>/Reviewer_Prompt.filled.md`, Opus): `Variety_Report.txt` and `Overlap_Report.txt` run (no shared quote; one name note); all twelve reviews started 2026-11-23, Chrysostom and Ephrem with them (`<slug>.brief.approved.txt` is each live text). The six long drafts' reviews name the cuts to 675.
5. One revision (`Reviser_Prompt.filled.md`, `Revision.md`) and one fresh read (`Fresh_Read_Prompt.filled.md`, `Fresh_Read.md`) for all twelve, with the reference reads (`Reference_Read.md`). Seven pass; Eutyches, Rufinus, Pelagius, Priscillian and Theodoret still fail. To Mark: https://claude.ai/artifact/6DyYNuqkn5Yh6ENxLZ5z56 (version 1).
5a. After Mark's ruling (2026-11-23): the fresh reads' fixes applied word for word (`<slug>/Fresh_Read_Applied.md`); four trimmed to length by their own fresh readers; Pelagius's craft pass checked (`pelagius/Craft_Pass_Check.md`); every change verified twice (`Fresh_Read_Fixes_Verified.md`, all twelve VERIFIED). Final briefs: persons 667-675 words, the council 585, Chrysostom 353, Ephrem 338.
6. Card (`<slug>/Card_Prompt.filled.md`, then `Card_Check_Prompt.filled.md`): started 2026-11-23.
7. Second readings.
8. Release.
9. Recording, with Mark's approval in his own words and a credit cap.

## Open items
- For Open-Gaps at release: the `aksumite-christianity-conversion-era` card's "shipwrecked" and "tutor" are not in Rufinus (Frumentius outline); Theodoret's card says the Religious History is not held, but it is, in Greek (PG 82).
- Eutyches's home tradition: the researcher tests the editors' claim against a primary text; it comes back to Mark on the hearts page if it holds.

- Ulfila: the creed sentence his outline quotes is also rendered, differently, on the `homoian-arian-christianity` tradition page, which `check_tree_overlap.py` does not scan. The outline check weighs it under the quote rule.
- At release: Eutyches's census `toldWithin` is removed (the river, Greek East), per the hearts ruling.
- Priscillian: the lifted Sulpicius line is rendered afresh from the Latin, so it no longer matches the wording on `sulpicius-severus`; the outline check weighs that.
- For batch 11 on, with Mark: why the outlines keep running long, and three fixes at research (https://claude.ai/artifact/MzbUJjBWpsjZJ377yUm3vX, version 1). This batch keeps the hearts ruling.

## Rulings
- "Batch 10: the slate approved" (Mark, 2026-11-23: "Approve as recommended"): the twelve and halves, the research order, Eutyches's home kept for now, the quotes, no direct-line change. This batch only.
- "Batch 10 hearts approved, with the lengths and a cut-first line in the kit" (Mark, 2026-11-23: "Approve as recommend"): the ten hearts; 4:30 at most with a Cut first list; Eutyches to the river; Priscillian not "the first". The cut-first line now lives in Kit Part 3, Length, and `roles/researcher.md` item 2; the rest, this batch only.
- "Batch 10: six drafts past 4:30, and Ulfila's creed" (Mark, 2026-11-23: "Approve as recommend"): the reviewer names the cuts to 675 for the six long drafts, the reviser makes them; Ulfila's creed sentence stays barred. This batch only.
- "Batch 10: the fresh read, and the fixes after it" (Mark, 2026-11-23: "Approve as recommended"): the five failing stories get the fresh reads' exact changes; meaning-changing minors applied, optional ones left; Chrysostom only the law's year; Pelagius's changes are its checked craft pass. This batch only.
