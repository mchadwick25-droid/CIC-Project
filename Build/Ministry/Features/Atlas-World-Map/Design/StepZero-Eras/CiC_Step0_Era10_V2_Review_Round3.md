# Review — Step 0 Era 10 V2.0, after Round 2

Reviewer: independent Opus 5.5 review · 2026-11-08 · Round 3 (targeted recheck, final round of the cap)

**Object:** `CiC_Step0_Era10_V2_0.md` and `CiC_Step0_Era10_V2_0_Proposed_Edits.json` as revised after Round 2 (commit 0c93d80e), diffed from "Era 10 V2 Review Round 2" (6b771c7d).
**Rules:** the change order at the top of the Atlas Decision-Log, as re-amended today: era 10 ends "c. 2010"; the living marker means alive today, under the addendum's R2, R3 and R4 only; and an entry outside church bodies must be "a defined movement, not just a trend".
**Scope:** a targeted recheck only. It covers Round 2's findings, the new material and the counts.
**Cap:** this is round 3 of 3. If a substantial defect stood here, the document would go to Mark.

## Method

- I copied `apply3.py`, `scan3.py` and `allow.json` to `review-3/work/` and ran them on census release 19.
  - Under G-8 (a): 448 substring edits applied exactly once; 19 structural operations matched exactly one item; 0 problems.
  - Under G-8 (b): the same.
  - With the 9 gated edits left out: 439 edits applied; 0 problems.
  - In all three runs the repo validator, run as CI runs it (`--base` release 19, `--atlas`, `--tree`), gives **0 errors**. Its 2 warnings are earlier-era shortName lengths, the same as release 19 itself.
  - I also checked the output by hand. It has 300 movements, down from 301, and `meta.totalEntries` is 300. `Pre-Survey Candidate` is 219. `retiredMovements[0]` is `{id, date, reason}`, with `redirectTo` present only under (b). The (b) target is IX.28's real id.
- `scan3.py` with the six drafts gives a raw count of 204, then POST2010 0, CHECK 0, DATED 98 and ALLOWED 114.
- I diffed the edit list against Round 2's version. There are 22 changed or added edits and 4 removed. That is 18 net new, and I read all of them.
- I ran my own wider present-tense sweep on the applied census. It adds `stands`, `survive(s)`, `keeps`, `has been`, `is known` and kin.
- I spot-checked 23 living flags against the V1.0 research files and the census: IX.1, 4, 5, 7, 10, 11, 13, 14, 15, 16, 19, 20, 21, 28, 29, 30, 32, 36, 39, 40, 44, 48 and 49.
- I checked the §2d table against every JSON `livingReason` by script: flag, grade and group, for all 48 rows. I also checked each §2 entry's living line against the JSON.
- I checked every factual claim in §4D and §4E against the census and the research files.
- I re-measured readability with `readab3.py`.
- No model calls were made.

---

## Round 2 findings: status

| Finding | Status | Evidence |
|---|---|---|
| R2-S1 retireEntry fails the validator | **Closed** | `_meta` now carries the review's text, and "as the census does" is gone. IX.31's record has its own id and the drafted reason, with `redirectTo` set for each G-8 option. The validator passes under (a) and (b). The counts are recomputed, and the log records the validator run. |
| R2-S2 undated present tense | **Closed** | All eleven named lines read as the review gave them. The three extra lines (IX.8 ×2, IX.22 legacy) are fixed the same way. The scan's word list is widened. Some lines of the same kind are left that no scan word catches; see M-1. None is a line Round 2 named. |
| R2-M1 G-49 | Closed | G-49 is withdrawn and keeps its number. D-P8 is closed. |
| R2-M2 IX.28 archive decay | Closed | `voices[4]`, `legacy` and `why` carry the review's texts under G-46. The ungated `why` edit now only removes *Love Wins* (2011), which is the right split. `sourcing` is gated too. G-46 (a) is marked as breaking the ruling. |
| R2-M3 two readings | Closed | IX.24 uses the parenthesis. D-E1 reads "In 2010, by its own counts, it was the largest church founded in the Philippines." |
| C-1, C-2, C-3 | Closed | IX.33 says "passes 2010". IX.25 reads "stays on as pastor". G-21 names the teaser edit. IX.14's count is stale again; see C-1 below. |

## New material: what checks out

- **Living flags (§2d, JSON).** Every one of the 23 spot-checked evidence items is in the repo, and none is invented. Each one traces to the census or the V1.0 research files, and its [S] or verified status matches. Checked: Pew 2011 (c. 67 million, verified); WCE 3rd ed. 2019 (verified); Anderson 2nd ed. (verified); the 2021 WCC exclusion (survey, "verified"; census floorNote); Suriel 2017 (verified); Hanegraaff, 9 Apr 2017 (verified); Slagle 2011 (verified); *K.S. Varghese*, 3 July 2017 (census source; survey "verified"); the Taizé succession of 2023 [S]; L'Arche 22 Feb 2020 and 30 Jan 2023 (census); the Seoul Statement 2024 [S]; Traditionis Custodes 2021 [S]; Adogame 2013 [S]; Acts 29, Aug 2014 (verified); Cosper 2021 (verified); Vermurlen [S]; Hummel [S]; Marsden 3rd ed. (verified); the Zacharias report, 9 Feb 2021 (census); the LLDM sentencing record, 8 Jun 2022 ("verified-adjacent", not counted as verified); Ford d. 2019 (census story); the Orthodox History 2022 article (research, about 1917); Datsko and Horiacha 2014 (census); FFOZ statements 2010–11 (census source). No [S] item is treated as verified.
- **Grades follow R3.** CD appears only where a verified source independent of the body is present: IX.1, 4, 5, 11, 15 and 39, and IX.50's draft. Own-voice acts are CR (IX.10, IX.46, IX.48). So are journalism (IX.36) and unverified independent sources (marked "CD if verified"). R3(iii), "no promotion", holds. Putting an unverified independent source at CR rather than CD is stricter than R3's wording, and §2d states that it does so.
- **Agreement.** Flag, grade and group agree between the §2d table, the JSON `livingReason`s and the §2 entry lines for all 48 rows. The JSON shows 44 true, 4 false and 1 n/a. Seven are settled. The groups are B 23, C1 12, C2 9 and C3 3, for 47 uncertain. No `livingReason` ties the mark to 2010.
- **§4D.** Every quoted line is in the census once:
  - "start of the third wave" and 11 May 1980;
  - "prayed for the sick" and "changed what congregational worship sounds like";
  - "the related prosperity-gospel movement" and "the prosperity-gospel current";
  - Hillsong 1983 and "Shout to the Lord" 1993.

  Latter Rain, healing revivals, Promise Keepers and the Toronto Blessing are in neither the census nor the research files, as the record says.
- **§4E.** The facts are right:
  - VIII.25's legacy has "two movements" and "dates its own start to that room in Edinburgh".
  - Stanley (2009) is on VIII.25.
  - Walls (1996) is [S] in the sources research.
  - McGavran, Herald of Truth and Vesper Chimes are present.
  - The "liturgical movement" is named once, and nothing is on L'Abri.

  The verdict that only the ecumenical movement passes all four tests follows from the repo. So does each "folded" verdict. The counts are right: 24 = 1 + 9 + 14, and 11 + 3 of the 14. The label on the verdicts is a problem; see M-2.
- **"c. 2010".** 33 rows in the JSON end "c. 2010" (32 from "present", plus IX.28 from 2015), and so do all six drafts: 39 in all. The numeric `end` is 2010 everywhere. No era 1–9 row is touched.
- **G-50 to G-55** each give options and a recommendation, and none decides something that is Mark's. G-50 names IX.28's flag change as a change order to V1.0's ruling, as it must.
- **The 18 new substring edits.** Every one is past tense or dated. None adds a claim or changes a meaning, and all apply in place.
- **No fabrication found.** I found no post-2010 year and no new present-tense claim in any field the new edits write.
- **Readability.** The participant-facing edit text scores Reading Ease 59.8 and grade 8.0, unchanged from the level Round 2 accepted. The only sentence over 25 words is D-E6's quotation. The new record prose (§2d, §4D, §4E, G-50 to G-55) reads at Reading Ease 72 to 77, grade 5 to 7.
- **Summary counts match the JSON.**
  - 448 substring edits and 19 structural operations (7 stories, 4 voices, 7 sources and 1 retirement).
  - 48 kept rows: 44 yes and 4 no; 7 settled and 41 uncertain. The six drafts are yes and uncertain.
  - The one flag change is IX.28.
  - 32 rows move from "present" to "c. 2010", plus IX.28's date change.
  - G-1 to G-55, with G-49 withdrawn.
  - 1 ready draft, 4 skeletons and IX.50 held.
  - §4E: 24 tested.

---

## SUBSTANTIAL

None.

## MINOR

**M-1. Undated present tense remains in six fields that no scan word catches.** None is a line Round 2 named, and none is false as of 2010. Each still breaks the ruling that an entry "makes no claim about where it stands today". Mechanical fixes:
- IX.3 `documentedStories[1].text`: "Luwum's statue stands over the west door of Westminster Abbey." → "In 1998 Luwum's statue was set over the west door of Westminster Abbey." The 1998 date is from IX.3's own source, "Westminster Abbey martyrs 1998".
- IX.26 `voices[1]`: "part of the record it keeps of itself" → "part of the record it kept of itself".
- IX.26 `documentedStories[1].caveat`: "The retelling has been remarkably stable." → "The retelling stayed remarkably stable."
- IX.49 `sourcing`: "Much of the record lives on platforms that can disappear." → "Much of the record was kept on fragile platforms." This uses G-46's wording, so gate it under G-46 too.
- IX.13 `legacy`: "the question it keeps open rather than the institutions it has built" → "the question it kept open rather than the institutions it built".
- Add `keeps|has been|stands over|lives on` to `scan3.py`. Leave out "survive(s)" and "is known", which in this record describe the sources.

**M-2. §4E's verdict column calls unsourced movements "trends", against its own reasons.**
- The problem:
  - Every row that fails the test is labeled "trend: left out or folded".
  - But M1's reason says "unsourced, not shown to be diffuse". M5's says "Unsourced on carriers, not diffuse". M5 meets tests 1, 3 and 4.
  - The preamble itself separates the two cases: "So, under the rule, does a real movement whose sources the repo does not hold yet."
  - Labeling the independent mission movement or Bible translation a "trend" tells Mark something the record does not find.
- *Fix:* use three verdict values:
  - "folded" for the 9 rows whose reason says folded, or already a row;
  - "left out: no source" for the 11;
  - "left out: partial base" for M2, M5 and M11 (liturgical).

  Reserve "trend" for a candidate the sources show to be diffuse. No row in the table is shown to be one. The counts do not change.

**M-3. IX.10's "settled" flag rests on an item the record's own evidence rule excludes.**
- The problem:
  - §2d says: "A later study of earlier history does not count unless the repo records that it describes the present." The rule is applied to IX.3 (2012 studies), IX.9 (Arjakovsky 2013), and IX.29 and IX.33 (Marsden 2022, verified, yet "none verified").
  - IX.10 is settled on Suriel, *Habib Girgis* (2017). That is a biography of a man who died in 1951.
  - Its other items are [S]: the 2013 canonization, the 2015 synaxarium and Mosebach 2019.
- *Fix:* move IX.10 to uncertain, group B / L-1, grade CR (2019) as now, and recount: 6 settled and 48 uncertain (B 24). Update:
  - the Summary row (6 settled, 42 uncertain among the 48 kept rows);
  - §2d's result lines, table row and L-1 list (24; 15 with a dated item);
  - G-5's list;
  - IX.10's `livingReason` and §2 line.

  If the reviser holds that a sitting bishop's 2017 book is the church's own dated voice under R2, write that reason into §2d's rule instead. Either way, the rule and IX.10 must agree.

**M-4. G-50's stated reason for IX.28 is a reason the record rejects for 19 other rows.**
- The problem:
  - Option (a) says "the repo holds no dated evidence that it is alive today".
  - L-1 (a) and L-2 (a) recommend "true" for nine and ten rows that hold no dated evidence at all.
  - L-2's rule marks an episode by its tradition, and the census routes IX.28's continuation into IX.18, which is marked true.
  - What actually sets IX.28 apart is a positive record of its dispersal: the wind-down c. 2013 [S], and release 19's "the conversation dissipated".
- *Fix:* in G-50 (a) and §2d L-3, replace the clause with: "(a) False: its own record shows it dispersing (Emergent Village wound down c. 2013 [S]; release 19: 'the conversation dissipated'), and the tradition it fed already has its own row, IX.18." Add one line: "This departs from L-2's tradition rule; (b) applies that rule instead." The recommendation stays Mark's to take.

**M-5. Two stale or missing references.**
- IX.3 "Wanted" (record line 342): "would lift the living-as-of-2010 call off [S]". This contradicts the revision log's "No line of the record … ties the living mark to 2010". *Fix:* "would show the fellowships still meeting after 2010, the evidence the living mark lacks (§2d L-2)."
- §2d, after the table: "`living.json` also gives the newest *verified* year and every item in full". `living.json` is a scratchpad file, not in the repo. *Fix:* "Each entry's `livingReason` in the proposed-edits JSON also gives the newest verified year and every item in full."

## COSMETIC

- **C-1.** Thirteen §2 "Register: N edits" counts trail the JSON by one or two, because the R2-S2 edits were added without updating them. Record → JSON: IX.5 11→12, IX.6 3→5, IX.8 7→9, IX.9 4→5, IX.10 10→12, IX.11 10→11, IX.14 10→11, IX.19 10→11, IX.22 7→9, IX.25 13→14, IX.28 14→16, IX.48 13→14, IX.49 13→14. The Summary total, 448, is correct.
- **C-2.** IX.49's `livingReason` lists "First Fruits of Zion statements … dated 2010-11" without [S]. The census story's verification reads "from reference summaries; primary text not yet read". Add "[S]". The grade, "none verified", already reflects this.
- **C-3.** §2d names the groups B/C1/C2/C3 in its table, and the JSON and G-5 name them L-1 to L-4. Show both in the table's header line once: "B = L-1, C1 = L-2, C2 = L-3, C3 = L-4".

---

## Verdict

**GATE-ELIGIBLE AFTER FIXES.**
- Round 2's two substantial findings and its minor and cosmetic findings are closed. The validator passes on the applied census under both G-8 options.
- No substantial finding. No fabrication: every evidence item checked is in the repo with its true status, and the grades follow R3.
- The five minor and three cosmetic fixes are all mechanical. Each is a stated replacement or a recount: no new research, no new source and no change to any recommendation Mark has not yet seen. They need no further review round. The reviser applies them, re-runs `apply3.py` and `scan3.py` with the widened word list, and the document goes to Mark's gate.
