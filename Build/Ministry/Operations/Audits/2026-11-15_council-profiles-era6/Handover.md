# Handover after round 1: era 6 council profiles (2026-11-15)

Written by the first worker (session_01JMNsSCUucVKrh6uv3T7bC7) at the coordinator's request, at a clean break after the round 1 fixes. The coordinator is session_01JMNsSCeHv3rWkarHUsXAWg. A fresh worker runs rounds 2 and 3, writes the records, and merges.

## The job (unchanged)

Council profiles for era 6 (1300-1517), the two councils marked major in the era 6 rows of `Build/Ministry/Operations/Audits/2026-11-12_major-events-scan/Councils_Scan.md`: the Council of Constance (1414-1418) and the Council of Basel–Ferrara–Florence (1431-1445, one joined row). Mark: "yes to era 6 councils" and "lift all holds" (2026-11-14); "dont sacrafice quality, expecially the quality of writing." Model: era 5 (PR #1667), the pattern `Build/Ministry/Features/Church-Family-Tree/Council_Profile_Pattern.md`, era 4 (PR #1665). Opus drafts; fresh Opus agents review at full effort; three rounds at most, every review file counts; minor round 3 fixes to reader-facing text follow Mark's standing cap ruling of 2026-11-14 (apply as worded, then one targeted check of only those strings by a fresh Opus agent). No paid calls. Push only to `claude/cft-councils-era6`. No census, site, `cft-website/`, `Who-Profiles/` or `cic/texts/` change.

## State

Branch `claude/cft-councils-era6`, pushed; no PR yet (open one draft PR at the end, push once after the local checks, mark ready, merge on green).

Files in `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era6/`: `README.md` (says how the gatherings join and that Pisa is told in Constance), the two briefs, `audio/` (both equal brief plus tags; regenerate with `working/mkaudio.py` after any brief change), the two entries and `records.json` (both keys; Constance 135 claims, Florence 114 after round 1).

| Council | Words | Spoken | FK | Flesch | Longest sentence |
|---|---|---|---|---|---|
| Council of Constance (1414-1418) | 400 | 2:30 | 7.03 | 69.73 | 23 |
| Council of Basel–Ferrara–Florence (1431-1445) | 400 | 2:30 | 6.53 | 70.83 | 20 |

Both are below grade 8 because the spoken lines are short; joining them would run sentences past 25 words or pad. This is the Clermont call of era 5. Say so in the Decision-Log entry, or improve it in round 2 only if it can be done without padding.

Commits: drafts before review are `ef16f168` (Constance) and `d583e23e` (Florence); round 1 fixes are `35213989`, `cf3e26b9`, `6bc3146a`. Round 2 diff: `git diff d583e23e HEAD -- Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era6/`.

## Rounds

- **Round 1** (full review, two fresh Opus agents): `R1_review.md` (Part A Constance, Part B Florence), `R1_changes.md`. 5 blocking, 12 substantial, 13 minor. Blocking: Constance, three false absences (Benedict XIII's own reply in Mansi 27; Hefele on "conciliariter ... et non aliter"; Harasiewicz's "Gregorius Semivlach"); Florence, a false absence (Basel's own letters and documents in Mansi 31) and the transfer told from the papal side only (now gives Basel's view). All applied; the fixers applied eight in corrected form after re-reading sources (listed in `R1_changes.md`).
- **Round 2: next.** A targeted recheck by fresh Opus agents (one per council), at full effort (Mark: full effort in every round): every round 1 finding, everything changed since `d583e23e`, including any sentence the fixes split or joined (check each claim still sits with its witness: the era 5 round 3 blocking point). Use `working/review_brief_r1.md` for the standard, adapted to a recheck. Write `R2_recheck.md` and `R2_changes.md`.
- **Round 3**, if needed, the same way; then stop and report to the coordinator for Mark's cap ruling if a blocking point is open.

## Still to do after the reviews

1. **Decision-Log** (`Build/Ministry/Features/Church-Family-Tree/Decision-Log.md`): an entry "Major councils, era 6", in the era 5 entry's shape (era 5 is at about l.3362): Decided; the two councils with words, FK, Flesch and the main witnesses; worker's calls (rivers as the scan gives them; the join of Basel–Ferrara–Florence in one profile, as the scan; Pisa told inside Constance; the Who click rule; the low grade; American spelling; Opus drafted every profile); Review; What is still open.
2. **Open-Gaps** (`Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md`): one numbered entry, taking the next free number just before merging (268 was the last on main at the start; others take numbers too). Only real gaps. Gather them from `R1_changes.md` ("Census differences for Open-Gaps" in Part A; B-M6 and the notes in Part B) and from the round 2 and 3 reviews. Known so far:
   - Census text to check (Constance): the Hussite story's "the emperor Sigismund presiding" (the acts name Jean de Brogny; Mladoňovice the king, not yet emperor) and "seven bishops" (the sentence names six); "the Council burned him" (it handed him to the secular court); the Latin papal entry's "deposed the rivals" (Gregory XII resigned); "by the 1440s settled in the papacy's favor" (stronger than Bannwart's note); "In 1870 Vatican I turned the claim down once more" (the held Vatican I text does not name Constance); the Hussite story's "Peter attended every session" (not checked).
   - Census text to check (Florence): `byzantine-church-palaiologan` "Mark alone ... refused" (Syropoulos: Isaias of Stauropolis and both Georgian envoys slipped away); "in exchange for military help" (a witness's view; no decree states it); the story's "Syropoulos suspects" the patriarch's note "was written for him" (no held Syropoulos line found) and "eighteen months of debate" (the narrator's own sum); `armenian-cilicia-after-the-kingdom` does not mention the Armenian union of 1439.
   - Census parties with no tradition at the date: Constance, the Greek-rite metropolis of Kiev under Lithuania (Gregory), Benedict XIII's obedience, the Dominicans (`the-dominican-order` ends 1300), the Bridgettines; Florence, the Georgian church, the Copts in era 6, the Syrian Orthodox, the Melkite patriarchates, Moldo-Wallachia and Trebizond, the Basel party; `church-of-the-east-timur-to-hakkari` is only an approximate fit for the Chaldeans of Cyprus. No census place ids for Constance, Basel, Ferrara, Florence or Lausanne.
   - People shown NOT SCORED (list them from the two entries' `people`), owner the coordinator for a Who verdict; and the scan inconsistency on Isidore of Kiev (STORY in the era 6 main table, LISTED in its event rows and the supplement), Part B notes.
   - Library: Mansi 31's header gives the decree *Laetentur caeli* at l.73472, which is Cyril's letter; the decree is at l.96226-97420. Mansi 29-30 (Basel's acts) are not held. The scan's "Mansi tomus 31 names the Armenian envoys" is not borne out (Raynaldus names two). Basel's session acts not held is not a wanted row: the held sources carry the profile.
3. **Wanted rows:** none. The held sources carry both profiles.
4. **Checks**, as PR #1667: `grade_text` (or `working/grade.py`), `python tools/check_live_commentary.py --base origin/main --enforce`, `python tools/check_spelling.py --base origin/main --enforce`, `python tools/check_paths.py`; JSON valid; audio equals brief plus tags; merge origin/main into the branch before merging and check no conflict markers are left.
5. **Report** to the coordinator: each council with words, spoken time and FK/Flesch, and any wanted rows (none).

## Working files

`working/` holds the two research dossiers (`dossier_constance.md`, `dossier_florence.md`, with file:line for nearly every fact and the absence searches), the research, drafting and review briefs, and two scripts (`grade.py`, `mkaudio.py`). Their scratchpad paths point to a folder that will not survive this session; use the copies here, and the census at `origin/main:cic-website/data/world-census.json`. The era 6 Who verdicts are in `Build/Ministry/Operations/Audits/2026-11-12_who-scan-era6/Who_Scan_Era6.md` and `2026-11-12_who-scan-supplement/Who_Scan_Supplement.md` (the supplement scores John XXIII, Gregory XII, Benedict XIII, Sigismund, Eugenius IV as STORY and Fillastre, d'Ailly, Aeneas Silvius as WHO).

## Lessons from round 1

- Most blocking points were again false absences, found in files the dossier already used (Mansi 27 for Benedict, Mansi 31 for Basel) or in a held history the searches missed (Hefele, Harasiewicz's spelling "Semivlach"). Search the whole Library with variant spellings before writing any absence.
- An editor's judgment is the editor's: Doukas's "on the union's side" rests on his editor Boulliau's preface and on Doukas's own words about the anti-unionists; keep both cited.
- A modern editor's tally is the editor's, by name, in the brief too ("by František Palacký's count").
- A dossier's line numbers can drift by a few lines; cite the lines you read.
- Two agents editing `records.json` at once must each re-read it just before writing and replace only their own key.
