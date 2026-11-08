# Review — Step 0 Era 10 V2.0, after Round 1

Reviewer: independent Opus 5.5 review · 2026-11-08 · Round 2 (targeted recheck)

**Object:** `CiC_Step0_Era10_V2_0.md` and `CiC_Step0_Era10_V2_0_Proposed_Edits.json` as revised after Round 1 (commits 15f522a2 and 119fdf9b, diffed from e6e74392).
**Scope:** a targeted recheck only. It covers the Round 1 findings, the new material in the revision, and the counts. It is not a full re-review.
**Cap:** this is round 2 of a three-round cap. Every review file on this document counts toward the three.

**Method.**
- I copied the reviser's `apply2.py`, `scan2.py` and `allow.json` to `review-2/work/` and ran them against census release 19.
- Result: 430 substring edits applied exactly once, 19 structural operations matched, 0 problems. The raw scan count is 146. The widened scan gives POST2010 0, CHECK 0, DATED 73 and ALLOWED 80 (17 LATER and 63 others).
- I also applied the file with every gated or conditional substring edit left out (`nogate.json`). All 420 remaining edits still apply, so the conditional edits are independent of the others.
- I ran the repo's own census validator, `tools/validate-census.mjs`, on the result. This was not part of the reviser's check.
- I diffed the edit list against the Round 1 version (81 added or changed, 61 removed) and read every non-split change.
- I sampled 20 of the 57 splits in place (`splits.py`) and read all 80 `allow.json` exemptions with their full sentences.
- I read all 73 DATED auto-passes, which the scanner accepts without a reason.
- I ran a further present-tense sweep on verbs the scanner's regex does not cover (`is read`, `are sung`, `have used since`, `ever since` and similar).
- I re-measured readability with the reviser's `readab3.py`, using a true count of sentences over 25 words.
- No model calls were made.

---

## Round 1 findings: status

| Finding | Status | Evidence |
|---|---|---|
| R1-S1 orphaned story content | **Fixed, with a new defect in the fix (R2-S1)** | All seven stories, four voices and seven source items are now `removeItem` operations, and each matches exactly one item. No register edit touches a removed item. IX.36's Mars Hill story is added. `retireEntry`, however, produces a census that fails the repo validator (R2-S1). |
| R1-S2 removals the gate cannot see | Fixed | The Summary, G-13 and G-39 list all seven, and they match the JSON gates (G-13 ×3, G-11, G-39 ×3). |
| R1-S3 post-2010 and present-tense lines | **Partly fixed (R2-S2)** | Every line the review named is fixed as given or better: IX.36 caveat, IX.48, IX.40, IX.28, the "living person" caveats, IX.5, IX.43. Other undated present-tense claims remain in fields the edits touch, and the revision log says none remain. |
| R1-S4 IX.20 text | Fixed | The JSON carries D-P7's text. IX.20 Q1, G-21 and §1E agree. The census has no Ethiopian entry for 1650–1855 (VI.25 ends 1650; VIII.49 starts 1855). |
| R1-S5 G-4 against the edits | Fixed | G-4(a) now states the rule the edits follow. Hummel 2023, Bowler 2013 and *Let Them Not Return* 2017 are restored and labeled as later. The IX.30 caveat matches G-4. The record does not date the conduct the 2019 report examined, so removing that report is consistent with the rule. |
| R1-S6 entries on a thin base | Fixed | D-E2 and D-E3 are skeletons. B2 is "not yet assessable". D-E2's Tier 1 signal is gone, and so is D-E3's placeholder `why`. G-31 and G-32 recommend naming them as gaps. The Summary reads "1 ready". |
| R1-S7 missing local questions | Fixed | G-40 to G-49 cover every listed item, plus three more. |
| R1-M1 | Fixed | One new ambiguity in the fixed text: R2-M3. |
| R1-M2 | Fixed | IX.18, IX.23, IX.26, IX.29 and IX.32 are clean. |
| R1-M3 | Fixed | §4 and §7 labels are correct, the §5 references are gone, and the `proposed_entries.json` references are gone. |
| R1-M4 | Fixed | "Carries no default" is gone. One name, with naming as a sub-option. There is an id note. Eight anchors, seven verified, matching §3's list. |
| R1-M5, R1-M6, R1-M7, R1-M9 | Fixed | |
| R1-M8 readability | Accepted as stated | Re-measured: 5 sentences over 25 words; FRE 59.6; FK grade 8.0. These match the log. The reason given for stopping short of 60 (the grade floor, and the remaining gap being word length) is sound. |
| R1-C1, C2, C3 | Fixed | |

**Allow-list spot-check (all 80 read; well over the 20 asked).** None of the exemptions hides a post-2010 claim.
- All 17 LATER entries carry a "later" label in the sentence itself.
- The three CTX entries date correctly:
  - IX.7: "in 2010", in the sentence before.
  - IX.16: "in 2010", four sentences earlier in the same field.
  - IX.34: a hundred years after 1896, which is 1996.
- IX.10's "still patriarch a quarter-century later" works out to 1985 + 25 = 2010.
- Two exemptions are loose but harmless:
  - IX.25 `documentedStories[1].teaser`, "The founder remains the pastor.", is the historical present of a 2002–05 story (see C-2).
  - IX.21's caveat, "remain disputed", describes the state of the question in map-voice.

The 73 DATED auto-passes were all read and are sound. Each sits in a sentence anchored to a year of 2010 or earlier.

---

## SUBSTANTIAL

**R2-S1. `retireEntry`, as specified, produces a census that fails the repo's own validator. The `_meta` also misstates census practice.**
- *Location:* JSON `_meta.structuralOps.retireEntry`; IX.31 `structuralOps`; G-8(a); revision log, "Check after revision".
- *Evidence:*
  - `_meta` says retireEntry "moves the whole movement object for this atlasId, unchanged, from movements[] to retiredMovements[], as the census does for a dropped row."
  - Release 19's `retiredMovements` is empty, so the census has never dropped a row. That makes "as the census does" untrue.
  - The census contract is in `tools/validate-census.mjs`, lines 142–147. A retired record needs `id`, `date` and `reason`, and may carry `redirectTo`. Compare `retiredLinks`, which use `{id, date, reason, replacedBy}`.
  - Running the validator on the applied census gives `ERROR retiredMovements[0]: needs id, date and reason`, plus `meta.totalEntries 301 != 300` and `statusCounts["Pre-Survey Candidate"] 220 != 219`. Release 19 itself validates with 0 errors.
  - The reviser's check reported "0 problems" only because `apply2.py` never runs the validator.
  - The `reason` string is published data. As written, whoever runs the census pass would draft it outside review.
- *Fix:*
  1. Redefine retireEntry in `_meta`: "removes the movement from movements[] and appends to retiredMovements[] the record {id, date, reason, redirectTo?} required by tools/validate-census.mjs; meta.totalEntries and meta.statusCounts are recomputed at the census pass."
  2. Delete "as the census does for a dropped row".
  3. Give IX.31's operation its own fields: `id: "deconstruction-and-ex-vangelical-communities"`, `date` set at the release, and a drafted `reason`. A suggested reason: "Every dated anchor of this movement falls after 2010, where the tree's history ends." Add a `redirectTo` choice to G-8: none under (a), or IX.28's id under (b).
  4. Add the validator run to the revision log's "Check after revision".

**R2-S2. R1-S3 is not fully closed. Undated present-tense claims about today remain, four of them in fields the edits touch, and the revision log says there are none.**
- *Location:* revision log, "Check after revision" ("finds no year after 2010 and no undated present tense"). The fields are listed below.
- *Evidence:* `scan2.py`'s word list has no reception verbs. A sweep for them finds the lines below. Every one breaks "What follows 2010" rule 1 ("makes no claim about where it stands today"). None is false as of 2010.
- *Touched fields:*
  - IX.6 `legacy`: "whenever a church has had to say what it will not concede to a state"; "that other churches have used since".
  - IX.10 `longDescription`: "wrote a body of spiritual work that is read well outside Egypt".
  - IX.11 `legacy`: "The scholarship has followed: Anderson, Martin, Kalu and others have made this the central subject of world Christianity".
  - IX.49 `relationsSummary`: "the two traditions' own publications draw that distinction themselves".
- *Untouched fields, same class:*
  - IX.5 `documentedStories[1].teaser`: "whose books are read across the world".
  - IX.9 `voices[4]`: "are read far outside Orthodoxy".
  - IX.10 `voices[2]`: "are read outside Egypt".
  - IX.14 `voices[3]`: "are sung far outside Scotland".
  - IX.19 `voices[3]`: "are the community's continuing record of itself".
  - IX.22 `documentedStories[1].caveat`: "the argument the church has had with itself ever since".
  - IX.48 `voices[2]`: "is among the convert literature's best-known books".
- *Fix (exact replacements; all are mechanical):*
  - IX.6: "whenever a church had to say what it would not concede to a state"; "that other churches used in the decades that followed".
  - IX.10 longDescription: "that came to be read well outside Egypt". IX.10 voices[2]: "came to be read outside Egypt".
  - IX.11: "The scholarship followed. Anderson, Martin, Kalu and others made this the central subject of world Christianity rather than its margin."
  - IX.49: "drew that distinction themselves".
  - IX.5 teaser: "whose books would be read across the world".
  - IX.9 voices[4]: "came to be read far outside Orthodoxy". IX.14 voices[3]: "came to be sung far outside Scotland".
  - IX.19 voices[3]: "were the community's continuing record of itself".
  - IX.22 caveat: "the argument the church went on having with itself, still open in 2010". This matches IX.22's own legacy.
  - IX.48 voices[2]: "became one of the convert literature's best-known books".
  - Add `read|sung|used since|ever since|has had|have made` to `scan2.py`. Re-word the log line to "no undated present tense found by the widened scan".

---

## MINOR

**R2-M1. G-49 rests on a premise the census does not bear out.**
- G-49 and the §1G row (D-P8) say both IX.29 and IX.33 "open their `why` on the Niagara conferences".
- In release 19, IX.33's `why` opens "The name arrived in 1920, when Curtis Lee Laws…" and moves straight to *The Fundamentals* (1910–15).
- Niagara is already in IX.33's relationsSummary ("grew out of the Niagara Bible Conference of the 1870s") and its teaser ("the Niagara Creed"). Option (a) asks Mark to approve a state that already holds.
- *Fix:* withdraw G-49 and close D-P8 as "already true in release 19". If the point is the teaser, re-word G-49 to name the teaser.

**R2-M2. The G-46 recast moves the archive-decay claim past 2010 instead of removing it. One more such line is not gated.**
- IX.28 `voices[4]` ", kept on platforms that later decayed" and `legacy` "kept an archive that decayed with them" (both G-46) still assert the decay. That decay is post-2010: the sources item dates the blog layer 2002–2012.
- IX.28 `why` ("its record was kept mostly on blogs, which later decayed with their platforms") makes the same claim. It is ungated, so it stays even under G-46(a).
- G-46(a) ("keep them as present-day sourcing notes") breaks ruling 1, but unlike G-40(b) it is not marked as doing so.
- *Fix:*
  - voices[4]: ", kept on fragile platforms".
  - legacy: "It also left a preservation problem. A movement that documented itself almost entirely on platforms kept its archive on them."
  - why: "…and its record was kept mostly on blogs and other fragile platforms."
  - Gate the `why` edit under G-46.
  - Mark G-46(a) "which breaks the 'What follows 2010' ruling".

**R2-M3. Two splits or fixes read in a way that changes their sense.**
- IX.24 `legacy`: "By 2010 'integral mission', evangelism and social action held together, had become mainstream evangelical language." With commas in place of the dashes, this reads as a list of three things. *Fix:* "By 2010 'integral mission' (evangelism and social action held together) had become mainstream evangelical language."
- D-E1 `why`: "By its own counts it was the largest church founded in the Philippines in 2010." This reads as "founded in 2010". *Fix:* "In 2010, by its own counts, it was the largest church founded in the Philippines."
- The other 19 splits sampled keep their words and claims. They are IX.4 floorNote, IX.7 floorNote and statusDescription, IX.9, IX.11, IX.14 (×2), IX.16 (×2), IX.18 (×2), IX.20 (×2), IX.23, IX.26 story, IX.29, IX.32 sourcing, IX.39 why and story, IX.41, IX.46 and IX.48. Their tense changes are all to the past, and none adds a claim.

---

## COSMETIC

- **C-1.** §2 IX.14 says "9 edits"; the JSON has 10, the extra being the assembly fact-fix. §2 IX.33's Section B line still says "nothing in the row passes 2000"; it should say 2010.
- **C-2.** IX.25 `documentedStories[1].teaser`, "The founder remains the pastor.", reads as today. Use "The founder stays on as pastor."
- **C-3.** G-21 names only the relationsSummary text. The matching conditional teaser edit ("continuing the re-founded empire church of the century before") is named in IX.20 Q1 but not in G-21. Add it.

---

## New material: checks that came out clean

- **No fabrication.** Every new token in the changed edits traces to the census entry or the V1.0 research files. Checked:
  - IX.19's "standard scholarly study, David Gaunt's of 2006, built on archives and the survivors' oral histories" (the census source note: "seminal study … archives together with oral histories");
  - IX.13's "from the 1960s on" (the entry's own dates);
  - IX.7's "from 1964";
  - IX.10's "to 2010";
  - G-43's *The Fundamentals* 1910–15 and 1920 naming (IX.33's `why`);
  - G-48's 1931 and 1980 texts (IX.44 floorNote);
  - D-E6's Reed "first executive director" (Survey_Research_E, verified).
- **G-6 and §8** follow the "What follows 2010" ruling. Mark's line is treated as ruled; only the wording of the "living" sentence is open. §8's follow-ups match G-5, G-6, G-27 and §7.
- **G-39 to G-49** each give options and a recommendation, and none decides something that is Mark's. Their facts match the record, except G-49 (R2-M1).
- **Conditional edits (G-42, G-43, G-46)** are tagged by `gate`. Leaving them out leaves every other edit applicable. G-42(a) adds no claim. G-43's status copy matches the Tier 1 pattern of IX.1, IX.6 and IX.23.
- **Restored later-scholarship labels** are explicit: "came later, in 2023"; "(2013) later did the same"; "followed later, in 2017"; "a later account"; "was published later, in 2011".
- **Counts.**
  - 430 substring edits and 19 structural operations (7 stories + 4 voices + 7 sources + 1 retire).
  - G-1 to G-49: 49 distinct, no gaps.
  - The seven removals agree across the Summary, G-13, G-11, G-39 and the JSON. The seven G-26 source items match the JSON.
  - New entries: 1 ready, 4 skeletons, 1 held = the 6 in `newEntries`.
  - JSON gate tags match the meaning of the G-numbers they cite.
- **Outside this recheck, noted for the census pass only (not a finding).** Several `sources[]` notes and works carry post-2010 years or present tense. Examples: IX.16's 2022 plea clause; "The current standard works" on IX.3 and IX.20; "No standard monograph yet treats" on IX.32. G-26 explicitly defers these mixed items to the census pass.

## Verdict

**GATE-ELIGIBLE AFTER FIXES.**
- No fabrication found.
- Two substantial findings, both mechanical, with exact fixes given:
  - the retire operation does not meet the census contract (R2-S1);
  - R1-S3's present-tense sweep is incomplete, and the log overstates it (R2-S2).
- This is round 2 of 3. A round 3 should be a narrow check of R2-S1, R2-S2 and the three minors: rerun `validate-census.mjs` on the applied census, and rerun the widened scan with the added verbs. If round 3 still finds a substantial defect, the cap requires escalation to Mark rather than a fourth round.
