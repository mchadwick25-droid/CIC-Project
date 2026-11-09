# Era 10, IX.50 the Christian Right: adversarial review, Round 2

Reviewer: independent Opus 5.5 review · 2026-11-09 · Round 2 (targeted recheck)

**Object.** `Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Era10_IX50_Proposed.json`, `CiC_Step0_Era10_IX50_Trace.md` (with its "Revision log (after Round 1)"), the applied row `the-christian-right` in `cic-website/data/world-census.json` (release 23), and the IX.33 and IX.24 edits. Branch `claude/era10-p2e10c`, pulled; head `980cf992e`.
**Against.** `CiC_Step0_Era10_IX50_Review_Round1.md`.
**Method.** Targeted recheck only: what changed (word diff `fb68bae6f..6eec2f318` on the proposal; `6eec2f318..980cf992e` on the census), against the Round 1 findings. E2, E3 and E11 were fetched directly with `curl` and their text searched for each quoted string; E11 was also corroborated with WebSearch. Readability re-scored with `engine/m7/readability.py` `measure`. No model was used to read pages. No repo file was edited. No metered model call was made.

## Verdict

**GATE-ELIGIBLE.** Every Round 1 finding is closed. No SUBSTANTIAL or MINOR finding is new. There is one COSMETIC finding, in the trace only (a broken table in §6); it can be fixed mechanically at any time and does not hold the gate.

Carry-forward, not a finding: the trace says Mark should be told in one line that the id follows naming sub-option n1, which he has not ruled on separately (S1). That line still has to reach him before release 23 is promoted to `live`.

## 1. Round 1 findings

| Finding | Status | Check |
|---|---|---|
| S1 id | **Closed** | Row `id` is `the-christian-right`. `_meta.id` uses the Round 1 wording. Trace §5 is updated. The string `christian-nationalism` does not occur anywhere in the release 23 census or in the new tree page. |
| M1 floorNote | **Closed** | Text is the Round 1 wording exactly. The absence claim now follows the evidence and is framed as "On his account". |
| M2 verified list | **Closed** | E2 and E3 move to "Verified in this run", with the clip range and the exact strings. Wanted item 3 is lifted. Item 2 is narrowed to the full record beyond the clip. The §4 "cannot read" bullet now rests on the founders' circle and cites Falwell's "great differences" sentence. |
| M3 Dallas framing | **Closed (changed source accepted)** | See §2 below. `why` and `longDescription` now name the Religious Roundtable as the organizer, and Reagan speaks to "the crowd". Splitting each long sentence in two keeps the meaning of the Round 1 wording, and the "you" can no longer be read as the Moral Majority. |
| M4 principles | **Closed** | "It named four principles of its own: 'pro-life, pro-family, pro-morals, and pro-American'." This is E1 verbatim, marked as the movement's own words. |
| M5 sourcing | **Closed** | Round 1 wording exactly. |
| M6 relationsSummary | **Closed** | Round 1 wording exactly. "Its founders were ministers" (E1). |
| M7 IX.24 | **Closed** | `new` is the Round 1 wording exactly. The `ruling` and trace §2 say the line comes from option (ii) and is a cross-reference, not a lineage. |
| M8 livingEvidence | **Closed** | Lewis is marked "a study of its present-day advocacy and opinion". The *Examiner* is dated 26 June 2025, with the conference on 26–28 June. The E10 source note matches. CD / L-3 stand. |
| M9 Reagan as a voice | **Closed** | `voices` now has four entries. Reagan's entry is gone. |
| C1, C2 | **Closed** | "moderate to rich"; "carried by organizations". |
| C3 | **Closed** | Encyclopedia.com added, with the "first executive director" note. The Wilcox note records the 2010/2011 cataloging and the co-author's two surnames. "members" is used. |
| C4 | **Left, as allowed** | Both IX.33 pointers stand. |

## 2. Re-verification of the changed and newly verified sources

| # | Result | How checked |
|---|---|---|
| **E11** Reagan Library, Morton Blackwell Files, "Roundtable (2 of 2)", Box 40 | **Confirmed. Adequate on its merits.** The PDF returned 200 (40 pp., 3.2 MB). Its cover sheet reads "Collection: Blackwell, Morton: Files Folder Title: Roundtable (2 of 2) Box: 40". The schedule proposal is dated 12 March 1982 and comes from Elizabeth H. Dole, with Morton C. Blackwell as project officer. Found verbatim: "Address the Memphis National Affairs Briefing of the Religious Roundtable"; "The Roundtable is headed by Ed McAteer who organized major rallies across the country for the President in 1980"; under PREVIOUS PARTICIPATION, "President Reagan addressed a major, highly successful religious/political briefing in August 1980 in Dallas". The OCR text splits two words ("suc cessful", "Da llas"); the trace's quotation is the true reading. The *Crisis to Crisis with Barbara Jordan* press release in the same folder reads verbatim: "McAteer sponsored a gathering in Dallas, Texas, called 'The National Affairs Briefing,' where 10,000 ministers came to hear then-candidate Ronald Reagan and several evangelists speak." Taken together, a White House planning document and a contemporary press account place the Dallas briefing with the Roundtable and its head. That supports "a briefing run by another group, the Religious Roundtable". It is a stronger, more primary source than the Miller Center essay Round 1 named. WebSearch corroborates it independently: Miller Center, "Building a Movement Party", and Baptist News Global say Robison and McAteer's Religious Roundtable organized the August 1980 program. The row does not claim the Roundtable was the only organizer, so Robison's part does not make it wrong. The row uses no attendance figure, so the sources' differing counts (10,000 ministers; 15,000–17,000 attendees) do not touch it. Typing the folder as "primary" is right. | curl + pdftotext, string search; WebSearch |
| **E2** AAPB, MacNeil/Lehrer, 22 Aug 1980 | **Confirmed.** Each string occurs once in the page text: "not a religious organization. It is totally political"; "72,000 pastors, Roman Catholic priests, Jewish rabbis, Mormon elders, fundamentalist, you name it"; "there is a coalition in this country of moralists. They're not all evangelical by any means; moralists who share similar moral values"; "though we theologically have great differences, we we very much share those premises and are willing to fight together"; "August 22, 1980"; "06:22 - 10:45". | curl, string search |
| **E3** American Rhetoric, Reagan, 22 Aug 1980 | **Confirmed.** "delivered 22 August 1980, Dallas Reunion Arena, Dallas, Texas" and "AUTHENTICITY CERTIFIED: Text version below transcribed directly from audio" both occur once; the page is marked abridged. The full sentence matches word for word. The only difference is the page's curly apostrophe in "can't". | curl, string search |

## 3. Applied census row against the proposal

- `the-christian-right` occurs once in release 23. It is deep-equal to `newRows[0]`: every field, and the same key order. It sits between IX.49 and IX.51.
- Each `registerEdits` old string occurs once in its field in release 22. Applying old to new reproduces the release 23 text exactly for IX.33 `legacy`, IX.33 `relationsSummary` and IX.24 `relationsSummary`. No other field of any existing row changed.
- Meta: `totalEntries` 307 to 308; `statusCounts['Pre-Survey Candidate']` 225 to 226; `release` {22, 2026-11-08} to {23, 2026-11-09}. Nothing else in meta changed.

## 4. Fabrication, tone, window, readability

- **Fabrication.** None. Every new or changed sentence traces to a verified item (trace §3, re-checked against E1–E5 and E11). The teaser ("five ministers ... drew support from several faiths") rests on E1 and E2.
- **Tone.** Even. The changes take out the one implied link Round 1 found (M3), mark the self-labels as the movement's own (M4), and narrow three claims. Nothing in the row speaks of motives.
- **Window.** The history ends with the 2009 founding of the Faith and Freedom Coalition and Williams (2010). Items after 2010 (Lewis 2017, the *Examiner* 2025, the undated FFC page) are used only for the living mark or the 2009 date, and are labelled so.
- **Readability** (initials joined, as in the trace). Fields: statusDescription 55.3 / 8.3; sourcing 48.8 / 8.8; floorNote 70.1 / 6.4; relationsSummary 61.1 / 7.5; why 54.1 / 9.2; longDescription 59.4 / 8.4; legacy 73.9 / 5.6. These match trace §6 within rounding. Overall Reading Ease is about 59.6 by the trace's measure, and 57.4 if the `voices` entries are counted too. FK grade is 8.0–8.6. That is 0.4–2.6 below the 60 target. The cause is the proper names the M3/M4 fixes require (Religious Roundtable, Christian Coalition, Faith and Freedom Coalition). Sentences average about 11–13 words. No real sentence runs past 25 words: the one 25-word "sentence" the splitter reports in `why` is a quotation ending in `.'` joined to the next sentence. The writing standard treats the target as something to write toward, not a hard script, and the shortfall comes only from names. It is not a finding.

## 5. Findings

### X1 — COSMETIC. Trace §6 carries an orphaned, empty table header

- **Location.** `CiC_Step0_Era10_IX50_Trace.md` §6, the two lines right after the scoring note: "| field | words | Reading Ease | FK grade |" and "|---|---|---|---|". They come before "After Round 1:" and have no rows.
- **Fix.** Delete those two lines. This is mechanical, in a Ministry file, and does not touch the census.

## 6. Validator

`node tools/validate-census.mjs cic-website/data/world-census.json --atlas cft-website/index.html --tree cft-website/tree` exits 0: "308 movements, 579 edges, 10 eras — 0 errors, 2 warnings". The two warnings are the old shortName length warnings (`anatolian-church-third-century`, `palestinian-ascetic-monasticism-early`), which were also present in release 22. The tree page `cft-website/tree/the-christian-right.html` exists and is in `sitemap.xml`.

Sources (WebSearch): [Reagan Library, Blackwell Files, Roundtable (2 of 2)](https://www.reaganlibrary.gov/public/digitallibrary/smof/publicliaison/blackwell/box-040/40_047_7007844_040_015_2017.pdf); [Miller Center, "Building a Movement Party"](https://millercenter.org/node/48826); [Baptist News Global, McAteer obituary](https://baptistnews.com/article/religious-right-pioneer-ed-mcateer-dead-at-78/); [American Rhetoric, Reagan 22 Aug 1980](https://americanrhetoric.com/speeches/ronaldreaganreligiousliberty.htm).
