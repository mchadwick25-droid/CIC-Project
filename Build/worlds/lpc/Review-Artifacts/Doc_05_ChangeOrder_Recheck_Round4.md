Simulated review — informational only, not an Article 31 substitute.

# Doc_05 targeted recheck of the CO-LPC-1 revision pass

- **Document:** `Build/worlds/lpc/Doc_05_Ecological_Reconstruction.md` (branch `claude/lpc-augustine-sermons-2026-10-23`, head `9a6d4d27`; diff checked: `git diff d6b449e6 9a6d4d27`)
- **Round:** 4
- **Reviewer:** Opus 5.5
- **Reviewer model:** Opus 5.5
- **Reviewer agent:** independent targeted-recheck subagent, fresh context (drafted none of the fixes)
- **Drafter:** Sonnet 5.5 (revision pass) and Opus 5.5 (renderings pass)
- **Drafter model:** Sonnet 5.5
- **Drafter agent:** the `lpc` build thread's revision-pass drafters
- **Date:** 2026-10-23
- **Scope:** targeted recheck of the revision pass. Only the Round 3 findings (`Review-Artifacts/Doc_05_ChangeOrder_Review_Round3.md`: P0-1, P1-1, P1-2, P2-1 to P2-7) are checked, each against the vendored source where factual, plus any new error the fixes introduced. The P0 sweep covers all of `Build/worlds/lpc` (Doc_03, `Lexicon-Chunks/`, `Lexicon_Deployment_Index.md`, `Representative/`, `scripts/`) and `records/lpc`. §1.4 rests on the project lead's Article 20 ruling; only the corrected Pinianus wording is checked against Letter CXXVI.
- **Ordered by:** the project lead's Cap ruling of 2026-10-23 ("Cap ruling: lpc CO-LPC-1 revision pass", `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`)
- **Truncation check, method 1:** line and byte count with an end-of-file read. `wc` gives 427 lines and 103,803 bytes. The last line ends on the Disposition's closing sentence ("Doc_04 §7 item 6 is closed, and nothing here relies on it."), and all fifteen `## ` headings are present.
- **Truncation check, method 2:** hash comparison against the committed blob. `git hash-object` of the working file and `git rev-parse 9a6d4d27:<path>` both give `472724090bc7099e1aff934303c741a3cd73be80`.
- **Method limits:** no web search and no model call. Nothing edited except this file. Counts re-run with Python over the vendored XML, tags stripped and `<note>` elements removed.

---

## Prior findings

| Finding | Status | Evidence |
|---|---|---|
| P0-1 Epistle II sentence given to Cyprian | **Partly fixed.** Doc_05 and every prose carrier are fixed; one generator script still carries it (new P1-A) | Doc_05:177, :179, :269, :350, :360 now rest on Epistle LIV §14. The English is verbatim at `anf05_hippolytus-cyprian-caius-novatian.xml:35009-35011` ("a portion of the flock has been assigned to each individual pastor, which he is to rule and govern, having to give account of his doing to the Lord"), inside `div3 n="LIV"` (line 34434) and its §14 (line 34975). The Latin is verbatim at `cyprian_epistulae-lat_hartel1871-csel3-tei.txt:10115-10117`, letter `n="59"` (line 9345), section `n="14"` (line 10097). The endnote "[Note this decree, 'by all of us,' and what follows.]" sits earlier in the sentence (anf05:35005-35006), as the note says. The §10 note now cites row 1. Sweep: `lpclex001_the-flock.md:33, :57, :61`, `lpc_Rep_Phase3_Voice_Construction.md:19` and `records/lpc/term/lpc.term.the-flock.md:51-52, :95-96` are corrected. Doc_03, `Lexicon_Deployment_Index.md`, the other `Representative/` files and `records/lpc` have no remaining site. `scripts/wb_lpc_s22.py:430-432` does (P1-A). The defect is logged at `Open_Gaps_Tracking.md:1746`. |
| P1-1 §0.3 and §7 gap claim | Fixed | Doc_05:27 now states Doc_01's narrower test and names the gap-dated rows (Optatus, canons, imperial law, Augustine before 391). Doc_05:301 reads "No ordinary-pastoral voice (Doc_02 §7)". The §7 prose (line 307) now reads "a genuine silence of any ordinary-pastoral voice". |
| P1-2 §1.4 Pinianus wording | Fixed | Doc_05:104: "We wanted him as our presbyter… We thought the word might yet be broken, or that another bishop might ordain him." This matches Letter CXXVI §1 (`npnf101_augustine-confessions-letters.xml:44488-44496`: "if they obtained him as their presbyter"; "a violation of my promise might be extorted from me, or that… he might be ordained by another bishop"). The "ours by living among us", "a church does not get many such" and "rich man's family" lines are gone. Doc_05:106 now says the letter does not put Pinianus's residence before the disturbance; §3 (44557), §12 (44822) and §13 (44845) carry the promise. Doc_05:191 now says the crowd did not get the ordination and won a sworn promise of residence; §3-§4 (44544-44578) show the oath demanded and given. |
| P2-1 §0.8 Ethical/Legal row | Fixed | Doc_05:68 "§6.8 (coercion only)". |
| P2-2 CF V7.4 / V1.4 §F divergence not carried | Fixed | Doc_05:405 (§11 item 16) and the Disposition's portfolio clause (line 427). |
| P2-3 count and rule | Fixed | Doc_05:175 states the ruled rule and gives 102 (flock 53, shepherd 36, pastor 13). I re-ran it on the Cyprian `div1` (anf05 lines 27373-59723), `<note>` removed, whole words with plurals, case-insensitive: 53/36/13 = 102. Doc_05:387 (§11 item 14) cites the ruling and OG-36. |
| P2-4 Doc_03 misquoted | Fixed | Doc_05:181 now quotes only "through different figures and different words", which Doc_03 contains. |
| P2-5 Doc_04 record-state statements | Fixed | Doc_05:370 and the Disposition say "two items". Doc_05:342 says "Doc_04's carried findings are closed". "Open Item" now survives only in the §11 heading. |
| P2-6 Document Log, duplicate, narration | Partly fixed | The duplicated Round 1 sentence is gone, and the narration at former lines 139 and 371 is reduced (Doc_05:139, :371). The Document Log (lines 413-417, three dated rows) still has no Round 2, Round 2 fix pass, CO-LPC-1 or Round 3 row. Doc_05:340 still narrates the sweep error ("nothing in the document could have caught it"). This is P2 and not blocking. |
| P2-7 sermon-volume figures | Fixed | Doc_05:201, :239 and :313 qualify ~308,000 words as the vendored NPNF English body, row 19. |

---

## New findings

### P1-A. The P0 misattribution survives in the term generator, which disagrees with the corrected record

- **Where:** `Build/worlds/lpc/scripts/wb_lpc_s22.py:430-432`, the `src(1, …)` locus for `lpc.term.the-flock`: "the watch-keeping passage on a shepherd's charge to keep watch over the flock, and the relief provision…".
- **Evidence:** this is the Epistle II sentence (anf05:28783, `div3 n="II"`, Roman clergy to the Carthaginian clergy), cited under Registry row 1 for a term whose `evidential` field says "Cyprian's own words carry this image". The same script's `evidential` text was updated at lines 480-487 to Epistle LIV 14, but this source locus was not. The committed record now reads "Epistle LIV 14 -- a portion of the flock assigned to each pastor… and Epistle V, the relief provision…" (`records/lpc/term/lpc.term.the-flock.md:51-52`). No script produces that text (`grep "Epistle LIV 14"` finds only line 484, the evidential field). So the record was edited by hand away from its generator, and re-running `wb_lpc_s22.py` would put the misattribution back into `records/lpc`.
- **Why P1:** this is the P0's own defect, inside the sweep scope the Cap ruling named, in the file that produces a canonical record. Fixing the record by hand while the generator keeps the error is a fix on a fix.
- **Fix:** change the `src(1, …)` locus at lines 430-432 to the record's wording (Epistle LIV 14, and Epistle V for the relief provision), and confirm that a dry regeneration gives a byte-identical `lpc.term.the-flock.md`.

### P2-A. The §4 inhabited line adds "with it"

Doc_05:177: "each of us must give account to the Lord for what he does with it." The source says "having to give account of his doing to the Lord" (*rationem sui actus*), that is, of his own conduct in general. "With it" ties the account to the flock alone. It is a small narrowing in a line marked **Documented**. *Fix:* "…must give account to the Lord for what he has done."

### P2-B. §6.7 pattern 4 sets the new evidence against "jurisdiction" without qualifying it

Doc_05:269: "authority described as the care of an assigned portion of the flock… rather than as jurisdiction (§4, Epistle LIV §14)". The sentence in Epistle LIV §14 is itself a jurisdictional decree, that "the case of every one should be heard there where the crime has been committed" (anf05:35007-35009). It argues for each bishop's territorial jurisdiction and against appeal to Rome. G1's own wording, "not as jurisdiction over other sees" (Doc_05:175), is accurate. *Fix:* "rather than as jurisdiction over other sees."

---

## Summary

All of the Round 3 P1s are fixed, and the Epistle LIV §14 replacement is verbatim in both anf05 and Hartel. The Pinianus correction now stays within Letter CXXVI §1 and §3. The P0 is fixed in every prose and record site but remains in the generator script for `lpc.term.the-flock` (P1-A). That is one targeted edit and a regeneration check. Under the Cap ruling, this finding goes to the project lead.

VERDICT: Substantial revision required
