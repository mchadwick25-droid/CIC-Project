# P2-G89b handover — 2026-11-10

**Closed (2026-11-10).** The work below was carried out as data release 33; see `README.md`.

The worker session for P2-G89b (carrying out Mark's rulings on the eras 8 and 9 global sweep)
stops here. Every subagent was cancelled at about 15:28, when a push stuck on a permission prompt
was interrupted, and the session cannot relaunch them. A fresh session takes over from this file.
The census has not changed. No data release has been built.

## Read first

- The worker brief (from the coordinator, session_01JMNsSDbFsmawtDvuAiukNQ): the ruling, the work
  (steps 1 to 6) and the limits. Its rules are restated in `Drafting_Brief.md` and `Review_Brief.md`.
- `Drafting_Brief.md` (what each drafter does), `Slices.md` (the eight slices, the existing rows
  each may edit, and the **fixed IDs** for every new row, so slices can link to each other's rows),
  `Review_Brief.md` (Opus adversarial review), `check_draft.py` (reading scores and quote check:
  Library files at their lines, raw texts through `raw_file`), and `apply_g89b.py` (merges
  `drafts/<slice>/Draft.json` for all eight slices into the census as one release; strips drafting
  keys; assigns atlasIds by era and start; it writes `apply_log.json`).

## State of each slice

| slice | draft | state |
|---|---|---|
| AF | `drafts/AF/Draft.json` | complete. 5 rows (AF-1 to AF-5), 8 links, 1 link retired (IV.26 → VIII.13, replaced through AF-2), 3 neighbor changes, 7 holds. Checker clean (172 quotes). Review round 1 never finished: rerun from scratch. |
| RV-A | `drafts/RVA/Draft.json` | complete. RV-1 (Jesuits 1650-1814), RV-3 (era 8 part only, 1650-1815); VI.11 `continuesAs`; lines in VII.19 and VIII.29; 4 links; 8 holds. Checker clean except the frozen first paragraphs of VII.19 and VIII.29, carried unchanged. Review round 1 never finished: rerun from scratch. |
| LA | `drafts/LA/Draft_partial.json` | mostly done: both rows, 1 link, 3 neighbor changes, 9 holds. One READ-FAIL to fix: IX.63 `longDescription[1]` (FRE 49). Links look short (1): finish them. |
| AS2 | `drafts/AS2/Draft_partial.json` | mostly done: AP4 in two segments, AP5, AP6; 2 links; 2 neighbor changes; 4 holds. VIII.27 `longDescription[0]` fails (FRE 27); check whether it is frozen text carried unchanged. |
| RV-B | `drafts/RVB/Draft_partial.json` | mostly done: RV-4, RV-5; 7 links; 3 neighbor changes; 7 holds. VIII.7 `longDescription[0]` fails (FRE 43); check whether frozen. Confirm VII.4, VII.32 (RV-2), VIII.7 (RV-6) lines are all there. |
| ME1 | `drafts/ME1/Draft_partial.json` | partial: ME-1 only. The rest of the slice (ME-2, ME-3, the ME-4 line in VII.23, ME-13/17/18/19 lines, the VI.30 → ME-1 → VIII.40 re-route, holds) is not drafted. |
| AS1 | none; `drafts/AS1/make.py`, `make2.py`, `lib.py` (the drafter's build scripts, partial) and `SOURCES.json` | not drafted. |
| ME2 | none | not drafted. |

Each draft's own `flags` list carries the drafter's open points; read them before revising.

**Raw texts are not on the branch** (about 80 MB, in the old session's scratch). Each slice's
`SOURCES.json` lists the URL of every raw text it quoted. ME1's raw files (no SOURCES.json) were
Catholic Encyclopedia pages `cathen_03559a`, `05230a`, `07547a`, `09683c`, `10157b` (newadvent.org)
and `churchill`, `dowling`, `malan` texts. ME2's were `bauhofer-hungary-1854`, CE "Eastern
Churches", "Hungary", "Poland", "Rumania", "Transylvania", Nilles *Symbolae* 1885, and Bunea and
Grama on the Romanian union. To re-run `check_draft.py` on an online quote, re-fetch the URL with
`curl` into `<scratch>/raw/` under the `raw_file` name. That re-fetch is also the reviewer's
independent second check.

## Decisions made so far

- **The ruling.** Mark answered "all recommended". The coordinator's two Decision-Log commits are
  cherry-picked onto this branch (entry "P2-G89 gate ruled: all recommendations"). Do not write a
  second entry for the ruling. When the release is applied, add the "carried out" entries to the
  CFT Decision-Log and the Atlas World Map Decision-Log (newest first there), the way P2-E10h was
  recorded, naming each admitted item as a change order (G89-6 a: one register).
- **AF-2 starts at 1517,** by Mark's leave for that one row to begin in era 7. 1300-1517 is logged
  for the era 6 owner. There is no 1650 variant; `apply_g89b.py`'s `variants` hook is unused.
  The drafter set AF-2's `era` to 8 (with era 7 its "continued as" to VIII.13 would break the
  one-era rule); the reviewer should judge it.
- **VIII.52 runs to 1911,** past era 9's end. The record only flags it (§10) and no gate question
  covers it: register it in Open-Gaps as open (coordinator agreed).
- **The Scottish church after 1650 and the Swedenborgians after 1815** stay in Open-Gaps as open.
- **Evidence.** The sweep's own rule for these eras: Library first, then public-domain editions
  opened raw (curl). A link resting on a raw online text is `verified-online` with `url` and
  `accessed`, capped at Widely Accepted (the validator enforces it). Documented needs a Library
  quote. This is the conservative reading; tell the coordinator in the final report.
- **Main is merged in up to release 30** (P2-V). Main has since taken 31 and 32 (a people worker).
  Merge main again before building; take the next free number and re-check it just before merging.
  The release number in `apply_g89b.py` is a command argument.

## Living (P2-V's rule, release 30)

The validator now needs, on every living row, `livingEvidence.basis` plus either a `carrier` (a
living entry in its line that holds its own dated evidence, not itself carried) or its own `grade`
(CD, CR or none). See the method page, "What the living mark means", and
`Build/Ministry/Operations/Audits/2026-11-10_living/`. Drafters were told to leave living to one
pass by the coordinator. The plan:

1. Set `livingEvidence` on every new row: `group: "line"` with a `carrier` where its line reaches
   a living holder (for example AF-1 → `modern-ethiopian-and-eritrean-christianity`; AF-2 →
   `the-coptic-monastic-and-sunday-school-revival`; ME-1 → `the-sayfo-and-the-syriac-diaspora`),
   or its own dated evidence moved from its predecessor where the new row is now the latest entry.
2. Update the predecessor rows whose P2-V basis says the tree has no later entry, because the new
   rows close those gaps: VI.11 (Jesuits, "no Jesuit entry after 1650" → RV-1), VII.7 (Old
   Believers, "no entry after 1815" → ME-5), VII.4 (Moravians, "no entry after 1815" → RV-5),
   VI.13c (China, "no entry for Chinese Catholics between 1650 and 1906" → AP2), VI.13a (Kongo,
   "no Kongo entry after 1650" → AF-3, which ends in the 1880s), and VI.3 if VII.32's end moves
   (RV-2). Where the new row is the latest entry, it takes the dated evidence and the older row
   names it as carrier.
3. RV-1 was drafted `living: false`; VI.11 now carries its own evidence (the Jesuits' 2022
   figures), so RV-1 can be living, with VI.11's evidence moved to it.
4. Tell the coordinator which new rows carry a living mark, for P2-V's check.

## What the reviews must cover

`Review_Brief.md`, plus these flags the drafters raised:
- **AF:** AF-1 and AF-2 living on neighbors' evidence; an added source (Catholic Encyclopedia 1907
  "Abyssinia", read raw, not cited by the record); empty `modernCountries` for AF-3 to AF-5 (no
  census row carries Angola, DR Congo, South Africa or Lesotho IDs); AF-2's era; DMR grades on
  IV.26 → AF-2 → VIII.13; the AF-1 to AF-2 "in contact with" link made major by an outcome.
- **RV-A:** Wikidata IDs the drafter looked up online (Paraguay Q733, Bosnia and Herzegovina Q225,
  Croatia Q224, Slavonia Q681964), where the brief says IDs are copied from census entries only;
  the Documented "argued against" VII.19 → RV-1 reusing the quotes of the existing VII.19 → VI.11
  link (and whether that old link should be re-pointed); Inferential-Thin links carrying outcomes;
  RV-3 entering for 1650-1815 with Bosnia and Slavonia only; pointer sentences in RV-1 to AP2 and
  ME-8, to cut if those rows do not enter; the RV-1 → AP2 link not drafted (no text read names the
  Society at Peking).
- **All:** frozen rows changed beyond the ruled lines; every quote re-checked by a fresh fetch or at
  its Library lines; the cross-slice links (AP1 ↔ ME-1, LA8-1 ↔ RV-5, VIII.13 → RV-4, ME-8 ↔ RV-1)
  drafted once only.

## Lessons

- Push only with the bare `git push -u origin claude/p2-g89b-rulings` (no flags, no pipes, no
  `-C`); anything else prompts, and a stuck prompt here cancelled every subagent.
- Pushing to the branch triggers no CI (CI runs on pull requests and `live`); only open the draft PR
  once local checks pass.
- `check_draft.py` scores the whole new value of a neighbor's field, so a frozen paragraph that
  already failed shows up as READ-FAIL; that is not the drafter's to fix.

## Still to do (worker brief steps)

1. Finish LA, AS2, RV-B, ME1; draft AS1 and ME2 (Sonnet, own scratch each).
2. Opus review of all eight, rounds capped at three; at the cap, escalate to the coordinator.
3. The living pass above, reviewed with the rest.
4. Holds into Open-Gaps (append-only, numbered), with VIII.52's 1911 end and the two North Europe
   breaks as open.
5. Merge main, apply as one release (`apply_g89b.py`), `python -m engine.m6.cli atlas-sync`,
   `node Build/tools/generate_tree_pages.mjs`, `node tools/build_tree_site.mjs`,
   `node tools/validate-census.mjs --base <main's census> --atlas cft-website/index.html --tree cft-website/tree`,
   `python3 tools/check_live_commentary.py --base origin/main --enforce`, `python3 tools/check_spelling.py`.
6. Audit README, Build-Plan line, Decision-Log entries; one draft PR, pushed once, marked ready,
   merged on green; check that www.churchfamilytree.com serves the new release. Report to the
   coordinator: rows, lines, links, re-homings, holds, release number, PR, deploy check, new
   Open-Gaps items, and the rows carrying a living mark.
