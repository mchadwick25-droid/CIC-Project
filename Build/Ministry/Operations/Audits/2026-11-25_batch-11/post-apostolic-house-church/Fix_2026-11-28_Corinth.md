# Fix 2026-11-28: Corinth's request and Dionysius

## Mark's ruling (2026-11-28, "yes")

1. Do not say Corinth asked Rome to write. The ANF of 1 Clement 1, "the points respecting which you consulted us" (anf01 522–535), and its editor's note stressing "asked", rest on Greek (peri ton epizetoumenon par' hymin pragmaton) that can also mean "the matters in dispute among you". Say "The church of Rome wrote to Corinth", on the brief and on every card field.
2. Dionysius (Eusebius, Church History IV.23.11, npnf201 25106–25117) says only that they read the letter in church and "shall always be able to draw advice" from it. Do not say his church drew counsel from it "in the quarrel".

This story only. Both wrong wordings are on the outline's Do not say list.

## Old beside new

| Where | Old | New |
|---|---|---|
| Brief, paragraph 2 | At Corinth's request, the church of Rome wrote. | The church of Rome wrote to Corinth. |
| Brief, Dionysius sentence | ...that his church still drew counsel from Rome's letter in the quarrel, written through Clement. | ...that his church still read Rome's letter, written through Clement, and drew advice from it. |
| Card `entry.tile` | ...the church of Rome wrote, at Corinth's request. | ...the church of Rome wrote to Corinth. |
| Card `timeline[0].lines[0]` | The church at Corinth asks Rome's church for its counsel. Rome's letter says sudden troubles at Rome have delayed its answer. | Rome's letter says sudden troubles at Rome have slowed it in turning to the matters at Corinth. |
| Card `timeline[7].lines[2]` (final check, word for word) | ...and will always draw counsel from it, as from the earlier letter written through Clement. | ...and will always be able to draw advice from it, as from the earlier letter written through Clement. |
| Outline, Beat 2 | Reason for the letter: Corinth had asked (anf01 525–528). | Reason for the letter: not held; say only that Rome wrote to Corinth. |
| Outline, Do not say | "the quarrel spreading" → Corinth's request only | → no reason given; two entries added for the ruled wordings. |

## The check

A fresh Opus hand read each changed sentence and card line against 1 Clement 1 and Eusebius IV.23.11, with the sentences on either side, and checked every other card field (`roles/final-check.md`, card list). PASS, nothing blocking. One MINOR exact change (timeline[7].lines[2]), applied word for word. Findings: `Final_Check_2026-11-28_Corinth.md`.

## Checks

- Census validator: 629 movements, 736 edges, 10 eras, 0 errors, 4 warnings (the existing shortName warnings).
- Readability, names out: grade 6.6, reading ease 75.9, pass (was 6.6 / 75.7).
- Rebuild: atlas-sync, `generate_tree_pages.mjs`, `corpus_coverage.py`, `build_tree_site.mjs` (0 mismatched). Changed: the story's tree page and the atlas index.

## Recording

The brief's recording no longer matches the text. Per the Stage Two Kit, section 4, it stays until a new recording replaces it. Nothing was recorded.
