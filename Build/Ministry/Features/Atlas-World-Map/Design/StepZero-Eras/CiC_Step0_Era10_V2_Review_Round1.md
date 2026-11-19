# Review — Step 0 Era 10 V2.0 (re-run as history, 1906–2010)

Reviewer: independent Opus 5.5 review · 2026-11-08 · Round 1 (full)

**Object:** `CiC_Step0_Era10_V2_0.md` and `CiC_Step0_Era10_V2_0_Proposed_Edits.json` (410 register edits on 49 entries, 6 new-entry drafts).
**Rules:** the Atlas Decision-Log change order "Change order: era 10 becomes history, 1906–2010", including its later block "What follows 2010". The standard is the L3B Step 0 Movement-Scope Methodology V1.0. The census is release 19.
**Method:** I applied every edit in order to a copy of the census (`apply_edits.py`). I scanned era 10's participant-facing fields after the edits (`scan.py`, `touched.py`). I diffed new tokens against the entry and the V1.0 research files (`newtokens.py`) and scored readability (`readab.py`). All scripts and outputs are in this directory. I read every one of the 365 edits other than the status-sentence removals, all six drafts, §0–§7 of the record, and the parts of the method that set the tiers.
**Known and excluded:** per the coordinator, G-6's mismatch with the "What follows 2010" ruling is already scheduled for the fix pass. It is not raised below.

---

## SUBSTANTIAL

**R1-S1. The story removals leave orphaned post-2010 content behind.**
- *Location:* JSON. IX.7 `documentedStories[1]`, IX.11 `[1]`, IX.16 `[0]` (`action: remove-story`). IX.28 `[1]`, IX.30 `[1]`, IX.32 `[1]` ("drop whole story"). IX.36 `[0]`.
- *Evidence:* `_meta.registerEditRule` says each edit is an exact substring replacement. Applied that way, the three "remove-story" edits blank only `title`. The three "drop whole story" edits blank only `text`. Everything else stays in the census. After applying:
  - IX.16[0] keeps `when: "2019–2022"`, a teaser saying the apostle "is arrested at Los Angeles airport in 2019", a caveat, and 2019/2022 sources.
  - IX.7[1] keeps `when: "22 February 2020 – 30 January 2023"` and the full text about Vanier's death in 2019.
  - IX.30[1] keeps the title "The Report the Board Published" and a teaser about the 2021 Zacharias report.
  - IX.28[1] keeps "Farewell, Rob Bell" (2011). IX.32[1] keeps the BibleProject story (2014–2019).
  - IX.36[0] ("The Year Mars Hill Came Apart", 2014) has no edit at all, though G-11(a) recommends removing it.
- *Fix:*
  - Encode each removal as one structural operation: `{"op":"remove-story","atlasId":…,"index":…}`, applied as deletion from the array.
  - State in `_meta` that structural operations run outside the substring rule, and in what order.
  - Add the missing IX.36[0] removal, conditional on G-11.

**R1-S2. The gate sees three story removals; the edits make seven.**
- *Location:* the Summary ("Three whole stories that fall after 2010 are proposed for removal (G-13), and one in IX.36 (G-11)"); G-13; §2b X6.
- *Evidence:* G-13 names only IX.7, IX.11 and IX.16. The IX.28, IX.30 and IX.32 story drops appear only in §2b's cross-cutting note X6, and no §6 question carries them. G-9 and G-10 decide IX.28 and IX.32 without mentioning that each loses a story.
- *Fix:* List all seven removals in G-13, or in a new question with options and a recommendation. Correct the Summary line to match.

**R1-S3. Post-2010 claims and present-tense lines remain in fields the edits touch.**
- *Location:* these fields after the edits are applied (each is a touched field). They break ruling 2, and "What follows 2010" rule 1 ("makes no claim about where it stands today").
  - IX.36 `documentedStories[1].caveat`: "Keller's last words are as reported publicly by his family. He is a public figure now dead". The edit deleted the 2023 death from the story text, but this caveat still asserts the death and cites words the story no longer contains.
  - IX.48 `legacy`: "Amy Slagle's fieldwork of 2011 remains the one dedicated scholarly study." This is a claim about today, in the present tense.
  - IX.40 `legacy`: "The English-language scholarship on the modern Georgian church remains thin". Same problem.
  - IX.28 `teaser`: "conference records now fragile with the platforms". IX.28 `voices[4]`: "now largely link-rotted and surviving through the Internet Archive". §2b X3 recommends keeping these, but no §6 question carries X3 (see R1-S7).
  - IX.25 `documentedStories[0].caveat` and IX.30 `documentedStories[0].caveat`: "He is a living person". This is a claim about today. The same line also sits, untouched, in IX.16[0], IX.25[1], IX.28[0], IX.32[1], IX.36[0] and IX.49[0]. IX.32[1] also says "No scholarly monograph yet treats this current".
  - IX.5 `legacy`: "A Pew study in 2011 put the number of Christians in China at around 67 million". This is allowed under G-4(a), but it is not labeled as later, and it does not say which year the count describes.
  - IX.43 `legacy`: "until now nothing carried it". This is map-voice, but "now" reads as today.
- *Fix:*
  - IX.36 caveat: delete "Keller's last words … family." and "now dead"; read "He was a public figure, and the page does not assess his theology."
  - IX.48: "The one dedicated scholarly study, Amy Slagle's fieldwork, was published later, in 2011."
  - IX.40: "English-language scholarship on the modern Georgian church was thin, and this map names that thinness rather than papering over it."
  - IX.28: "conference records kept on fragile platforms" and "the movement's real archive from 2002, kept on platforms that later decayed".
  - Caveats: "the page describes only his dated public acts."
  - IX.5: "A Pew study published in 2011 estimated about 67 million Christians in China in 2010."
  - IX.43: "and no entry carried it before this one."

**R1-S4. The IX.20 relationsSummary edit uses the banked text the record itself rejects.**
- *Location:* JSON IX.20 `relationsSummary` edit (marked "CONDITIONAL on IX.20 Q1"); §1E D-P7; G-21; §2b IX.20 Q1.
- *Evidence:*
  - §1E says the V1.0 banked text "is itself unusable" because it narrates process. D-P7 proposes "Continues the Ethiopian church of Tewodros and Menelik. The tree has no entry for Ethiopian Christianity between 1650 and 1855."
  - G-21(a) recommends "apply the new replacement drafted here".
  - The JSON instead sets: "continuation of VIII.49's re-founded empire church; the lane's true disclosed silence is 1650–1855". That is the banked text minus its parenthesis. It still puts an atlasId and internal jargon ("true disclosed silence") into a participant field.
  - IX.20 Q1 in §2b recommends applying "the banked text". The record recommends two different texts.
- *Fix:* Set the JSON `new` to D-P7's text. Re-word IX.20 Q1 to name D-P7's text, so §1E, §2b, G-21 and the JSON agree.

**R1-S5. G-4's description of option (a) does not match what the edits do.**
- *Location:* G-4; JSON IX.30 `documentedStories[0].caveat`; IX.29, IX.30 and IX.19 `legacy`.
- *Evidence:*
  - G-4(a) says it "keeps … the 2018 reports in IX.30's story caveat". The IX.30 caveat edit ("remove the 2018–2019 events (after the era)") deletes them, as IX.30 Q1(a) recommends.
  - G-4(a) says "later outside scholarship … may stay". The edits still strip later scholarship from three rows: Hummel's 2023 study (IX.29 legacy), Bowler's *Blessed* (2013) (IX.30 legacy) and *Let Them Not Return* (2017) (IX.19 legacy).
  - Meanwhile Pew 2011 (IX.5), Slagle 2011 (IX.48) and the 2020/2023 L'Arche reports (IX.7, five fields) stay.
  - Mark answering G-4(a) would be approving something the edits do not do.
- *Fix:* Make G-4's text state the rule the edits actually follow, then make the edits consistent with it. Either restore the later scholarship labeled as later, or say plainly that later works stay in `sources[]` only and keep none in prose. Correct the IX.30 parenthetical either way.

**R1-S6. Two new entries are recommended for entry on a base the method does not allow.**
- *Location:* D-E2 (independent mission movement) and D-E3 (student and campus movements); G-31; G-32; the Summary ("3 ready for the gate").
- *Evidence:*
  - Method §B step 3: "Sourcing and Ecology are near-threshold checks … recording citation-grounded reasoning for each score." Tier 1 needs Sourcing and Ecology cleared "comfortably"; Tier 2 needs them cleared.
  - D-E2 grades B1 "Moderate to 1974 in-repo; Thin after" and B2 "Rich as judgment", with no citation. Yet its tier is "Tier 1 or 2 signal".
  - D-E3 grades B1 "Thin-to-moderate" and B2 "Moderate-to-rich as judgment". Its participant-facing `why` ends "Their story still needs its own sources before it can be told here", which is a placeholder in a row proposed for entry. Its statusDescription says "the entry waits on a source base".
  - The record's own D-Q1 holds the Anglican skeleton back because "a row with no base would be the first in the census drafted on Thin". D-E3 is thinner than that skeleton, and D-E2 is thin for its last 36 years.
- *Fix:*
  - Re-grade B2 on both drafts as not yet assessable, since no source is cited.
  - Drop D-E2's Tier 1 signal.
  - Recast G-31 and G-32 so the recommended option is "name as gaps and draft once a base is staged", consistent with G-16.
  - Treat D-E2 and D-E3 as skeletons, and remove D-E3's placeholder `why` from any text proposed for the census.
  - Correct the Summary to "1 ready for the gate (Iglesia ni Cristo)".

**R1-S7. §6 leaves out six local questions plus X3, so stale copy survives the gate.**
- *Location:* §6, against §2 "Open questions".
- *Evidence:* These local questions have no G-number and no answer route:
  - IX.4 Q1 (the Kimbanguist 2021 WCC exclusion)
  - IX.18 Q1 (keep, fold into IX.35, or drop)
  - IX.19 Q1 ("living Syriac communities read as erasure")
  - IX.33 Q1 (stale statusDescription)
  - IX.38 Q1 (the grade of the scale claim)
  - IX.48 Q1 (the name)
  - §2b X3 (notes on the archive's own condition)

  After the edits, IX.33, a Tier 1 row, still shows the statusDescription "Proposed for a future survey; not yet reviewed."
- *Fix:* Add these as G-39 onward, each with options and a recommendation, or fold each into a named G-question. Update the "38" in the Summary and in §6.

---

## MINOR

**R1-M1. Present tense and edit history in the new drafts.**
- D-E1 `why`: "Pasugo has set out its teaching since February 1939" and "By its own counts it is the largest church". Fix: "Pasugo carried its teaching from February 1939"; "By its own counts it was the largest church founded in the Philippines in 2010".
- D-E1 `statusDescription`: "Split out of the earlier four-body entry". D-E1 `relationsSummary`: "carried on the register with three other bodies until it was given an entry of its own". Both narrate the census's own editing in a live field, which CLAUDE.md forbids. Fix: delete both clauses.
- D-E6 `_draft.proposal` still says "revised as history to 2000". Fix: "2010".

**R1-M2. Commentary from the retired addendum stays in touched statusDescriptions.**
- *Location:*
  - IX.18: "now or ever"; "it now has the history it lacked".
  - IX.23: "not a present-day description of a feeling".
  - IX.29: "not an undated present-tense claim".
  - IX.32 statusDescription and floorNote: "now rests on … not an undated present-tense claim"; "rather than on a present-tense characterization".
  - IX.26: "named only minimally for now".
- *Evidence:* CLAUDE.md says any edit to a live file also removes the commentary already in it. This text describes the retired addendum's process.
- *Fix:* Cut each clause after the dated-text statement. For example, IX.32 becomes "Its note on the doctrinal floor rests on its dated carrier texts."

**R1-M3. Broken cross-references and file names.**
- The movements section is §4, but the record cites it as §5 in D-P5, 1F D-Q6(a), the last row of 1G, §3 ("§5, D-Q8"), and §7's 4A and W23.
- §4's subsections are labeled 5A–5C. §7's subsections are labeled 4A–4C.
- The record cites `proposed_entries.json` six times and `entries.json` once. Neither file exists; the drafts are in `CiC_Step0_Era10_V2_0_Proposed_Edits.json` under `newEntries`.
- Fix: renumber the labels and correct the file names.

**R1-M4. IX.50: "no default" alongside a recommendation, plus naming drift.**
- §6 says IX.50 "carries no default". §3 then gives "My recommendation depends on the outcome of D-Q8", and G-15 repeats the lean. A conditional recommendation is acceptable, but the two statements contradict each other.
- §3 offers the names "The New Christian Right" or "The Christian Right, 1979–2010". D-E6 and G-15 use "The Christian Right".
- D-E6's `id` still reads `christian-right-and-christian-nationalism`.
- G-15(i) bundles dropping the "Christian Nationalism" name into adopting the row. The name should be Mark's separate choice.
- §3 B1 says "Six dated anchors, five of them verified", but §3 lists eight (seven verified).
- *Fix:*
  - Replace "carries no default" with "is Mark's direct ruling; the conditional lean below is advisory".
  - Settle one candidate name and offer the naming as a sub-option.
  - Note the id for a decision before first publication.
  - Recount the anchors.

**R1-M5. G-5's header does not fit two of its rows.** It says "rows whose own window closed before 2010", but IX.18 and IX.32 now end in 2010. Their open question is whether a label, or a current with no body, can be "living". Fix: "Fifteen rows whose 'living' flag turns on P2-V", with a note on the two rows.

**R1-M6. [S] status blurred on IX.32.**
- §2b says "Wright's NTPG and Surprised by Hope verified". V1.0's Sources_E verifies NTPG's title and publisher only; its year (1992) is [S].
- G-10 and the livingReason rest IX.32's Tier 2 and living flag on "Wright's popular books of 2006 and 2008". *Simply Christian* (2006) is [S] in V1.0, and the record does not say so.
- Fix: "NTPG (title and publisher verified, year [S]); Surprised by Hope 2008 verified; Simply Christian 2006 [S]". Carry the [S] into G-10.

**R1-M7. Edits that add a claim of their own.**
- IX.37 `documentedStories[0].text`: "Neither book ended the argument" replaces "Both books are still read". It is a new claim with no source. Fix: "The church they describe went on."
- IX.10 `longDescription`: "published steadily for four decades" (from 1971) reaches past 2010. Fix: "published steadily through the rest of the century and after".

**R1-M8. Readability of the new text.**
- Of 487 sentences in new strings, 45 run past 25 words. Aggregate Flesch Reading Ease is about 58, below the target of 60. Flesch-Kincaid grade is 8.7, which is within range.
- Worst cases, by word count: D-E6 `sourcing` (45), IX.27 `legacy` (44), IX.14 `legacy` (40), IX.8 `legacy` (40), IX.32 `legacy` (37), IX.24 `legacy` (35), IX.25 `legacy` (34). The full list is in `read_out.txt`.
- Fix: split each of these at its colon or semicolon.
- American spelling is clean: no British forms found. No assistant-voice tells found.

**R1-M9. A confidence grade used for a verification question.** The IX.10 confidence note reads "1918 Sunday School Committee: Contested at the verification level". `Contested` grades a disputed claim, not a split between research runs. Fix: "[S], since the two runs diverge; the church's traditional date".

## COSMETIC

- **R1-C1.** Drafter voice and assembly residue in the record: "I counted", "This is not my slice", "Flag outside my slice, for the IX.14 drafter", "Its drafter owns the detail". The 1G IX.14 flag and the 1A IX.22 flag are now handled in §6 and can go.
- **R1-C2.** G-8 says "Every anchor is dated 2015 or later". The Summary says IX.31's "story begins at the 2010 boundary". Use one phrasing.
- **R1-C3.** D-E6 `_draft` and §3 give the Dallas briefing as 21 August 1980, carried verified from V1.0. Reagan's address is usually dated 22 August (the briefing ran 21–22 August). The participant text says only "August 1980", so nothing displays wrong. Re-check before any finer date is published.

---

## Clean checks (verified sound)

- **The edits apply cleanly.** All 410 register edits apply as exact, unique substrings, in order, with no conflict across 49 entries and 13 field types.
- **No fabrication found.**
  - 96 edits add tokens not found elsewhere in their entry. Every token traces to the V1.0 research files, except stylistic words ("Official", "Afterward", "Suspicion").
  - The longer substitutions trace to sources: the IX.48 Alexy I voice (from its own story and sources), IX.36's TGC 2007 Confessional Statement (V1.0 verified), IX.39's 1995 Supreme Court ruling, IX.16's 1982 Moon conviction (IX.16's story), and IX.40's recognitions of 1943 and 1990.
- **The drafts trace to the record.**
  - D-E1 comes entirely from IX.16's own copy.
  - D-E2's two-currents framing comes from VIII.25's legacy.
  - D-E3's SVM lines come from VIII.25. Its Campus Crusade line comes from IX.48's story.
  - D-E6: every anchor appears in V1.0 with its mark unchanged (Moral Majority 1979 kept [S]; the Faith and Freedom Coalition's 2009 founding was verified in V1.0). The Reagan quote matches V1.0 word for word.
- **No [S] item from V1.0 is treated as verified,** apart from the softer case in R1-M6.
- **The counts reconcile.**
  - Tiers: 11 / 29 / 3 / 4 register / 1 label / 1 dropped = 49, matching the JSON.
  - Living: 45 yes / 3 no / 1 n/a.
  - Date changes: 32 moved from "present" to 2010, plus IX.28.
  - P2-V flags: 15. IX.34's "does not turn on P2-V" is correctly excluded.
  - Gate questions: G-1 to G-38 number 38.
- **§1A matches the census.** 37 living era-9 rows end at 1906, and 20 have no edge or continuesAs into era 10. The listed IDs match exactly.
- **The fact fixes are correct.** IX.14's Taizé correction ("two years later", 1940 after 1938) is right. IX.20's "still unresolved in 2010" follows correctly from the 2018 reconciliation.
- **Gate-question form.** Every G-question gives real options and a recommendation, except the IX.50 wording in R1-M4. None decides something that is Mark's. IX.50, the frozen-row touches, the INC numbering and the change order on Bible translation are all left to him.
- **Grade vocabulary.** The formation_confidence grades in the JSON confidence notes use the five-level vocabulary, apart from R1-M9. "Not Attested" is not used as a sixth grade.

## Verdict

**GATE-ELIGIBLE AFTER FIXES.** I found no fabrication. The seven substantial findings are defects in encoding, consistency and standard. The edits as written would leave post-2010 story content in the census (S1, S3). The gate would see a different set of removals and rules than the edits carry out (S2, S5, S7). One edit contradicts the record's own text (S4). Two drafts are recommended for entry on a base the method does not support (S6). Each fix is stated above. A Round 2 targeted recheck of S1–S7 should suffice.
