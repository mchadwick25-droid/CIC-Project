Simulated review — informational only, not an Article 31 substitute.

# Step 0 — Movement-Scope Confirmation (lpc): full review after change order CO-LPC-1

**Document:** `Build/worlds/lpc/Step0_Movement_Scope_Confirmation.md` (branch `claude/lpc-augustine-sermons-2026-10-23`, head `a0209b8d`; last edited by CO-LPC-1 in `eb717583`)
**Round:** 6
**Reviewer:** Opus 5.5
**Reviewer model:** claude-opus-5-5
**Reviewer agent:** independent Opus 5.5 review subagent (workflow-spawned, full review, high effort)
**Drafter:** Sonnet 5.5 drafters for CO-LPC-1, checked by the `lpc` build thread; the original 2026-09-01 text and its Round 1 to 5 revisions were drafted by the `lpc` build thread (no model named in the Decision Log)
**Drafter model:** Sonnet 5.5
**Drafter agent:** CO-LPC-1 Sonnet 5.5 drafter (Step 0, Doc_01, Doc_02, Source Registry file set)
**Date:** 2026-10-23
**Scope:** full review of the document in its current state: factual and quotation accuracy, consistency with the `lpc` Decision Log rulings of 2026-10-23 (D1 to D5, CO-LPC-1) and earlier, consistency with Doc_01 and with neighbouring worlds' files, source attribution, stage job, and whether CO-LPC-1's edits are correct and introduced no new error. Forces Framework integration does not apply to Step 0.
**Ordered by:** the project lead's Cap ruling of 2026-10-23 (System Hub Decision Log, "Cap ruling: lpc change order CO-LPC-1", which names this file)
**Truncation check, method 1:** line and byte count with end-of-file read: `wc -l -c` gives 181 lines, 63,448 bytes; the file ends with a newline after line 181 ("**Pending:** nothing procedurally. Phase A continues to Doc_01."); headings §0 to §6 are all present in order (lines 8, 18, 26, 78, 132, 145, 153).
**Truncation check, method 2:** content hash against the committed blob: `sha256sum` of the working file and of `git show HEAD:Build/worlds/lpc/Step0_Movement_Scope_Confirmation.md` are identical (`d4268247…8a088371`), and `git status` shows the file unmodified, so the text read is the whole committed text.

## Method

Read in full: the document; CLAUDE.md; `Build/reference/method/skills/cic-build-cycle/SKILL.md`; the `lpc_Decision_Log.md` entries of 2026-10-23 (D1 to D5, Doc_02 §7, Doc_05 crosswalk, lexicon method, liturgical candidates, Article 20, CO-LPC-1, review route) and the Article 3 ruling of 2026-09-16; Open_Gaps OG-28 to OG-51; Step0 Round 1 to 5 reviews (Round 5 in full); the CO-LPC-1 diff of this file (`git show eb717583`).

Every quotation of 20 or more characters was extracted by script and searched in the named source, then each lead was confirmed by reading the passage: the Step 0 Conclusion v2, the Step 0 Methodology V1.0 and CF V7.4 DRAFT (text extracted from the `.docx`); Constitution V2.2 in `Build/reference/L1-Foundation/`; the `lpc`, `ijc` and `hal` corpus-map files; `hal` Doc_01 §8.1 (line 172); `cic/texts/README.md`; `ijc` Step 0, Doc_01, Doc_02 and Open_Gaps item 16; `records/ijc/source/ijc.source.augustine-confessions.md`; the Donatism Step 0 now in the tree (`Build/worlds/don/`) and the superseded draft at commit `4f420cbb`; `cic-website/data/world-census.json`. All quotations of the Constitution, Methodology, Step 0 Conclusion, corpus maps, `hal` Doc_01, `ijc` files and the texts README were confirmed word for word, allowing for marked ellipses and brackets. The CO-LPC-1 edits that hold up: the census sentence (line 16) matches the census entry exactly (status, atlas I.8, dates, region); the `ijc` paraphrase (line 177) matches `ijc` Open_Gaps item 16 ("authorized directly by Mark once the original build thread was confirmed retired"); the Donatism-draft paraphrases (lines 70, 72) match the draft at `4f420cbb` (its line 55 and its B3 line 94), and the claim about the current Donatism text matches `Build/worlds/don/Step0_Movement_Scope_Confirmation.md:116`.

## Findings

### P1-1. §4 item 2(e) still states, in the present tense, a reading Donatism's Step 0 no longer holds, and contradicts the CO-LPC-1 edit two sections above it

- **Where:** `Build/worlds/lpc/Step0_Movement_Scope_Confirmation.md:137`, item (e).
- **Evidence:** line 137 reads "Donatism's own Step 0 confirmation reads the portfolio entry's 'not the schism-crisis angle' parenthetical as qualifying both Cyprian and Augustine together … Doc_01 must resolve this reading divergence explicitly." The current Donatism Step 0 attaches the parenthetical to Cyprian alone (`Build/worlds/don/Step0_Movement_Scope_Confirmation.md:116`: "is the source's own parenthetical attached specifically to that clause"). CO-LPC-1 rewrote §2 A5 to say the draft held that reading only "at that stage", that the draft is "since superseded", and that the divergence was "retired in Doc_01 §5" (line 72; Doc_01 line 116: "which retires the divergence Step 0 §4 item 2(e) flagged"). Item (e) was not touched, so the binding list now orders Doc_01 to resolve something the same document calls retired, and misstates another world's file. Doc_01 §8 item 11(a) (`Doc_01_World_Identification_Boundaries_Orientation.md:183`) named §4 item 2(e) as one of the three sites needing this exact correction. CO-LPC-1 fixed sites (b) and (c) but not (a). This is the stranded-neighbour pattern §6 line 171 already names, for the sixth time.
- **Fix:** restate item (e) in the past tense and in line with §2 A5. For example: the two same-day drafts read the parenthetical differently; Donatism's Step 0 now reads it as qualifying Cyprian alone; Doc_01 §5 adopted the Cyprian-scoped reading and retired the divergence. Then sweep the same claim at line 169 ("Donatism's own draft attaches the parenthetical to both anchor figures together and binds that world-level reading"), which should also be in the past tense, and line 110 ("a divergence for Doc_01 to resolve"). Update Doc_01 §8 item 11 once all three are fixed (OG-50 already flags it as partly stale).

### P1-2. The body still calls the IJC boundary breach live and unresolved, while §6 says it is fixed and verified

- **Where:** lines 108, 114, 130.
- **Evidence:** line 108: "Escalated at §6, not resolved here — it is outside this thread's write scope … and outside what Doc_01/Doc_02 of *this* world can fix." Line 114: "World #4 (the Optatus placement, and the reading divergence with Donatism's own draft) and the World #6 boundary breach are both live, currently-unresolved items requiring action before Doc_01/Doc_02 close." Line 130 counts "World #6's Confessions overlap" as one of "two live, specifically-named boundary items." Against this, §6 (line 177) says the project lead authorised this thread to make the fix, and that it "is complete and independently verified." Line 179 says "the escalation actually resolved". `ijc` Open_Gaps item 16 confirms the fix. Line 108 is also wrong on write scope, since the fix was in fact made by this thread on the project lead's authority. Line 114 is also stale on the Donatism divergence (see P1-1). OG-43 (check 11) assigned line 108 to this change order as a narration site to clear. The CO-LPC-1 diff does not touch line 108.
- **Fix:** keep the finding in B3 (the breach was real and this check found it). Change the status words to match §6: it was escalated, the project lead authorised the fix, and it is fixed (`ijc` Open_Gaps item 16). At line 114, the live items should be only the Optatus placement and the Antiochene contrast. At line 130, drop the Confessions overlap as a live item, or mark it resolved. Remove the write-scope reasoning at line 108.

### P2-1. The Article 3 question is still described as standing, with no pointer to the 2026-09-16 ruling

- **Where:** lines 44, 52, 136, 161.
- **Evidence:** line 52: "the standing Article 3 ambiguity … is carried forward, explicitly, as binding on Doc_01". Line 161 says the document "explicitly declines to resolve the Article 3 century-gap ambiguity". The project lead's ruling of 2026-09-16 (`lpc_Decision_Log.md:1861`) closed the constitutional question: Article 3 permits gapped formation-types under a four-part test. The same entry (line 1885) directs that "Documents that carried the question as open now point at this entry rather than restating its status." What Step 0 says about its own act stays true (Step 0 neither created nor closed the question). But a reader is not told that the question has since been ruled on.
- **Fix:** add one pointer sentence at §2 "Resolution for this world" and at §4 item 1. It should say the question was ruled on 2026-09-16 (Decision Log entry) and that Doc_01 §5 discharged item 1 under that ruling. Do not restate the ruling.

### P2-2. Stale state lines in the header and the tail

- **Where:** line 181 ("Pending: nothing procedurally. Phase A continues to Doc_01."); line 3 (status as of Round 5 only).
- **Evidence:** Docs 01 to 09 are built and Approved to proceed (Decision Log, 2026-10-23 CO-LPC-1 entry). The document now carries unreviewed change-order edits under this Round 6 review.
- **Fix:** replace line 181 with a current, non-narrative state line, or remove it. Leave the history to the Decision Log, as CO-LPC-1 did for the other narration.

### P2-3. Two file paths no longer resolve

- **Where:** line 6 cites `Build/Ministry/Technology/CiC_Record_Native_World_Build_Process_V1_2.md`. No such file exists: the process document is at `Build/reference/method/CiC_Record_Native_World_Build_Process_V2.0.md`, and V1.9 is in `Archive/Superseded-Method/`. Line 12 cites `World-Builds/Imperial-Juridical-Christianity/Step0_Movement_Scope_Confirmation.md`, which is now `Build/worlds/ijc/Step0_Movement_Scope_Confirmation.md`. CO-LPC-1 updated the `ijc` Open_Gaps path at line 177 but not these two.
- **Fix:** point each one to the current path, or name the archived version actually used on 2026-09-01.

### P2-4. The skill and CO-022 quotations do not match the repository text (registered, still open)

- **Where:** line 163 (the three limbs of category 4) and line 165 ("Before disposing of any document, check it against these four categories …").
- **Evidence:** neither string is in `Build/reference/method/skills/cic-build-cycle/SKILL.md`. The closest repository wording is `Build/reference/Project-Reference/CiC_OneDocAtATime_Build_Protocol_2026-07-06.md:39` ("a contradiction discovered between two already-cleared master documents, or a finding that cuts against a decision made earlier in the build"). These quotations come from the installed skill as it stood on 2026-09-01. OG-50 already registers this as not done.
- **Fix:** as OG-50 says, either quote the repository copy exactly or paraphrase. Or name the source as the installed skill text of 2026-09-01.

### P2-5. B1's Augustine sermon line does not match D1 and D4

- **Where:** line 87, "~97 sermons preached to his own congregations at Hippo and Carthage".
- **Evidence:** D4 counts exactly 97 sermon divisions in `npnf106` from the vendored file. Carthage was not Augustine's own see. Under D1 and the CO-LPC-1 Doc_01 scope paragraph (`Doc_01…md:26`), the world's sermon base is now all of Augustine's sermons, including the vendored PL 38/39 and Gaume Latin texts, not only the NPNF selection. Step 0's eligibility verdict is unaffected, since B1 only gets stronger.
- **Fix:** "97 sermons in the NPNF selection, preached at Hippo, Carthage and elsewhere". Add one clause noting that the world's sermon scope was widened on 2026-10-23 (Decision Log D1, D4), with the Latin texts vendored.

### P2-6. The superseded Donatism draft is cited with no locator

- **Where:** lines 70, 72 ("in a draft since superseded"; "Donatism's own draft at that stage").
- **Evidence:** the draft exists only at commit `4f420cbb`. CO-LPC-1 moved that locator to the Decision Log, so a reader of Step 0 cannot check the paraphrase. A citation is not narration.
- **Fix:** add the commit and path (`4f420cbb`, `World-Builds/Donatism/Step0_Movement_Scope_Confirmation.md`), or cite the Decision Log's CO-LPC-1 entry, where they are kept.

## Not findings (checked and sound)

- **Article 4.** The five commitments (line 32) match Constitution V2.2 word for word. The claim at line 151 that `ijc` Step 0 §2 A1 still carries a four-item restatement is true (`Build/worlds/ijc/Step0_Movement_Scope_Confirmation.md:26`).
- **IJC cross-check.** Cyprian appears exactly once in `ijc` Doc_01 (line 98) and never in its Doc_02. The `ijc` source record's `work:` field and its BOUNDARY sentence are quoted exactly.
- **Cyprian.** The corpus-map facts hold: the four pseudo-Cyprianic treatises, the two given to Novatian, and the sententiae of 87 bishops, September 256.
- **Augustine.** The corpus-map figures hold: ~695,000 words, 168 letters, 17 letters at ~52,892 words.
- **Step 0 status of other worlds.** Neither `hal` nor `desert` has a Step 0 confirmation file (line 89).
- **Process narration.** The disposition block (lines 155 to 179) is reported by `tools/check_live_commentary.py` as PROTECTED, the tail-section convention the checker applies fleet-wide. It is therefore not raised as a finding here.

## Summary

CO-LPC-1's own edits to Step 0 are accurate at the sentences they changed: the census, the `ijc` paraphrase, and the Donatism paraphrases. But the change order left two neighbouring status claims false. §4 item 2(e) still states a Donatism reading that no longer exists, and still orders Doc_01 to resolve a divergence the document now calls retired. The body still calls the IJC breach live and unresolved, while §6 records it fixed. Both change what the document claims, so both are substantial under the build-cycle skill. Per the Cap ruling, they go to the project lead and no further review file follows without a new ruling.

## VERDICT: Substantial revision required

VERDICT: Substantial revision required
