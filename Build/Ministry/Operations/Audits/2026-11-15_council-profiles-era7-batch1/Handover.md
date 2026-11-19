# Handover after round 3: era 7 council profiles, batch 1 (2026-11-15)

Written by the first worker (session_01JMNsSAWJPbHpgiXLD56iFg) at a clean break, with its context near the 400k limit. The coordinator is session_01JMNsSCeHv3rWkarHUsXAWg. One blocking point is open at the review cap and waits for Mark's cap ruling.

## The job

Era 7 major councils, batch 1 of 3: Diet of Worms (1521), Marburg Colloquy (1529), Diet of Augsburg (1530), Synod of Chanforan (1532). Pattern `Build/Ministry/Features/Church-Family-Tree/Council_Profile_Pattern.md`; model era 6 (PR #1670). Length ceiling 2:30 (Mark: "Keep 2:30 for councils"), never a target. Full-effort review in every round. No paid calls. Push only to `claude/cft-councils-era7-batch1`. No census, site, `cft-website/`, `Who-Profiles/` or `cic/texts/` change. Before merging the PR, send the coordinator one line and wait for its go (it sequences merges).

## State

Branch `claude/cft-councils-era7-batch1`, pushed; origin/main (release 44, 1959c7f2) already merged in, no conflicts. No PR yet.

- **Marburg held back** (coordinator agreed): no held text tells the debate or prints the signed articles. Wanted rows added in `Build/Ministry/Features/Source-Library/CFT-Wants.md`, new "Era 7" section (Marburg: Schirrmacher 1876 first choice; Worms: Reichstagsakten II / Kidd 1911, not blocking).
- Files in `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/`: README (with why each runs its length), three briefs, `audio/` (regenerate with `working/mkaudio.py`), three entries, `records.json` (merged from `working/records_<id>.json`; edit those, then re-merge: the snippet is in this session's history, or json.dump the three into one object keyed by id).

| Council | Words | Spoken | FK | Flesch | Longest |
|---|---|---|---|---|---|
| Diet of Worms 1521 | 399 | 2:30 | 7.12 | 67.17 | 23 |
| Diet of Augsburg 1530 | 400 | 2:30 | 7.91 | 60.26 | 25 |
| Synod of Chanforan 1532 | 400 | 2:30 | 6.93 | 66.84 | 25 |

## Rounds

- **R1** (full review, three fresh Opus): `R1_review.md`, `R1_changes.md`. Worms 3B/4S/12M; Augsburg 3B/3S/12M; Chanforan 4B/4S/5M.
- **R2** (targeted): `R2_recheck.md`, `R2_changes.md`. Worms 1B/2S/3M; Augsburg 0B/1S/7M; Chanforan 1B/0S/3M. Note: R2_changes' preface says only Augsburg's audio changed; Chanforan's changed too (worker's brief edit). B2-M7: R1_changes' preface says one word was cut; three were ("two", Waterworth's "J.", "church").
- **R3** (last, targeted): `R3_recheck.md`. Worms PROCEED, 2 minor (A3-M1 records ranges; A3-M2 absence note hits), NOT yet applied. Augsburg PROCEED, 1 minor (B3-M1), applied. Chanforan REVISE: **C3-B1 blocking, open at the cap**, plus C3-M1 and C3-M2 (minor), not applied.

### C3-B1 (for Mark's cap ruling)
Brief p.8 now reads "Léger wrote in 1669 that the valleys changed nothing at the Reformation, except that later they took up arms." Léger (LEG l.23072-23086) says their old rule already allowed self-defense "en toute extrémité", kept through the war of 1560-61; Gilles tells that war fought defensively (GIL81 l.8768-8789, 8276-8278). What changed later was going beyond self-defense. Reviewer's fix: "Léger wrote in 1669 that the valleys changed nothing at the Reformation, but later went beyond self-defense." With C3-M2 ("the historians" restored before Muston and Montet) the brief stays at 400 words; scratch copy in the R3 part. C3-M1: entry `uncertain[12]` and records contested claim 3 should read "changed nothing in doctrine or discipline through their talks with the reformers".

## Still to do after the ruling

1. Apply the ruling; write `R3_changes.md`; if Mark orders a check, one fresh Opus agent of only those strings (name its file in a "Cap ruling" Decision-Log entry, as era 6 did). Apply A3-M1, A3-M2, C3-M1 (and C3-M2 with the brief fix). Regenerate audio, re-merge records, validate JSON.
2. Decision-Log entry "Major councils, era 7, batch 1" in the shape of "Major councils, era 6" (Decision-Log.md about l.3446): Decided; the three councils with words, FK, Flesch, main witnesses; Marburg held back; worker's calls (rivers as the scan; Who click rule; low grade under 8 for Worms and Chanforan, not padded; Buchheim's side worded "on Luther's side" as no held line gives his church; American spelling; Opus drafted); Review; What is still open. Plus the cap ruling entry if any.
3. Open-Gaps: one entry, next free number re-checked on origin/main just before merging (270, 271 taken; batch 10 Whos take 272 onward). Items: the "For Open-Gaps" lists in `R1_changes.md` (Parts A, B, C), `R2_changes.md`, and C-S4 in R1_review Part C; plus Who-scan fix (Who_Scan_Era7 l.76 calls LHYM 651 an editor's note; it is Carlyle's); people shown NOT SCORED in the three entries' `people`, owner the coordinator; no census place ids for Worms, Augsburg, Angrogna; `waldensians-in-the-alps` ends 1517 so is not listed; Marburg held for its record.
4. Checks as PR #1670: `working/grade.py` (or grade_text), `python tools/check_live_commentary.py --base origin/main --enforce`, `python tools/check_spelling.py --base origin/main --enforce`, `python tools/check_paths.py`; JSON valid; audio equals brief plus tags. Merge origin/main again, check no conflict markers.
5. One draft PR, push once after checks, mark ready; tell the coordinator and wait for its go; merge on green.
6. Report to the coordinator: words, spoken time, FK/Flesch per profile, PR link.

## Lessons

- Two of the blocking points in rounds 2 and 3 came from fix wording, including the worker's own (Léger twice): read the whole source sentence, including its "bien que" and "si ce n'est" clauses, before rewording.
- Names: the drafts gave first names no held line had ("Christian Beyer", "Joseph Waterworth", "Carl Buchheim"); check every name in the brief against a held line.
- A partisan label needs a held line ("Protestant editor" for Buchheim was blocking at Worms); keep the label the same across councils.
- Chanforan's name and Farel's presence rest on a 1535 deposition (Gilles); keep Muston's 1532 link as Muston's.
