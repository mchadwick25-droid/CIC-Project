# Handoff — question coverage design — 2026-10-26

From session: https://claude.ai/code/session_01Sb4EENRKNZtmouh2wJod6B · World or workstream: question-coverage (all worlds, read-only) · Branch / PR: `claude/question-coverage-2026-10-26`, no PR opened

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| Visitor-side question repository: 12 visitor kinds, 17 clusters, 129 sub-questions, 465 wordings | `Build/Ministry/Features/Question-Coverage/Repository/render.py` validates unique ids and places every question in exactly one sub-question; it printed no errors |
| Independent Opus review of the repository against Pew, PRRI, Gallup, Barna, Lifeway, Springtide, Theos and peer-reviewed grief work; 40 sourced additions accepted | `Review/opus-research-review.md`; sources table with weights; figures traceable to a named study. Not re-verified by this thread |
| Coverage maps for 16 clusters across the 12 built worlds, with a cross-cluster summary | `Coverage-Maps/`; every quote record cited as rendered was matched to its vendored file. Totals in each report (for example C4 30 of 30, C14 121 citations, C16 22 of 23) |
| Acquisition list (165 works) and Bible commentary surveys for Eras 1 to 10; record worklists (742 rows) | `Worklists/`; 469 carried file paths checked to exist, none missing. Hosts and licences in the commentary surveys are from memory, marked unverified |
| Chrysostom mapping written as a change list (17 works) | `Worklists/chrysostom-mapping-change-list.md`; not applied |
| Everything saved to the repo; Library thread launched with the full Step 0 to 2 remit | commits `686de185` and `f9554c09` on the branch; Library session `session_01BoUDEU6u247QUj79JqrVzQ` |
| Published pages | Question repository https://claude.ai/artifact/G4StgntbMvk1vxjH8oeq6z · Research review https://claude.ai/artifact/LJMDxmCXu8NDSHxYBoisqh · Coverage maps https://claude.ai/artifact/MAXm3iXAo36QC5r92CsKVT · Acquisition list https://claude.ai/artifact/QQdKonBL7njVYtqU3AsXVA · Record worklists https://claude.ai/artifact/9YEfbpB9Z8xDeewELevBFU |

## 2. Not done

- No record, corpus-map file, world gap file or method document was changed. The per-world gaps are in `Worklists/records-by-world.*` and have not been entered in any `Open_Gaps_Tracking.md`; each world's thread owns that.
- No change order for the build method. Mark's instruction: no quiet change; the priority is answering from sources.
- No passage index for commentaries. Design is the Library thread's fourth job.
- Real visitor questions are not in the repository. Mark has not pasted the dashboard list.
- The Latin pastoral thread (`session_01PdSKYEGnPNVAntVFg5ZReR`) had not answered the Augustine commentary and passage-access message when this thread stopped.
- No pull request. The branch is pushed so the Library thread can read it.

## 3. Re-check before you trust it

- Research review figures (Pew, PRRI, Barna and others) — several came from press coverage, not the primary page; the review lists which. Check before quoting any number.
- Commentary survey editions, hosts and licences — from memory because the sandbox blocks the text hosts. Verify before any download.
- Priority scores for Eras 7 to 10 — the four worlds with no records (Hussite, Jesuit, Methodist, Old Believers) count every cell as open, so whole-Bible sets score about 76 each. They show emptiness, not quality.
- C15 counts in the cross-cluster totals — C15 was counted as 240 wordings, not sub-questions.
- Cluster reports from C2 onward were finished on Sonnet from an earlier agent's saved runs; a second reader has not checked them.
- Earlier statement in this thread that Syriac's slavery limit is contradicted was wrong: the contradicted Syriac limits are the two on marriage and women (C8, Aphrahat and the Book of the Laws of Countries).

## 4. Waiting on Mark

- Whether the Chrysostom `context` role is acceptable for Jerome's, Gallic and Cappadocian worlds, since the README defines `context` as the outside view — options in `Worklists/chrysostom-mapping-change-list.md`.
- Whether to open a pull request for the branch `claude/question-coverage-2026-10-26` so the folder reaches `main`.
- Whether the question-coverage pass joins the build cycle, and how — by change order if so.
- The five honest limits that vendored text contradicts, and the three Jewish-visitor records with unguarded edges — fixes belong to the owning world threads; the list is in `Coverage-Maps/00-summary-all.md`.
- The eight "what are you" questions that fall through to the Representative, and the privacy page, which omits that scores and flags are kept without text — product and Facilitator-governance decision (`Coverage-Maps/C16-coverage.md`, Part B).

## 5. Next step

Open `Build/Ministry/Features/Question-Coverage/README.md`, then `Coverage-Maps/00-summary-all.md`. New design work starts in a fresh thread after the Friday reset.

## 6. Spend

Allowance share used: about half of the week by Sunday evening, per Mark. Metered: none; no model calls, live tests or paid services were run by this thread.
