Simulated review — informational only, not an Article 31 substitute.

# Doc_04 Gravity Discovery (lpc): second targeted recheck of the Round 15 open findings

- **Document:** `Build/worlds/lpc/Doc_04_Gravity_Discovery.md`, with `records/lpc/gravity/lpc.gravity.confessor-authority-vs-episcopal-peace.md` and `records/lpc/gravity/lpc.gravity.penitential-discipline.md` (branch `claude/lpc-augustine-sermons-2026-10-23`, head `cd31eb55`; fixes read as `git diff 9a6d4d27 cd31eb55`)
- **Round:** 16
- **Reviewer:** Opus 5.5
- **Reviewer model:** claude-opus-5-5
- **Model note:** the harness reports that this run switched to Opus 5 (1M context) because Opus 5.5 could not be used. When the switch happened is not recorded, so some or all of this review may be Opus 5.
- **Reviewer agent:** independent second-recheck subagent, fresh context; drafted none of the fixes or renderings
- **Drafter:** Sonnet 5.5 and Opus 5.5 (revision passes)
- **Drafter model:** Sonnet 5.5
- **Drafter agent:** the `lpc` build thread's revision-pass drafters, after `Doc_04_ChangeOrder_Recheck_Round15.md`
- **Date:** 2026-10-23
- **Scope:** second targeted recheck. Only the findings Round 15 left open are checked — N1 (the "texts tested here" limit in the two gravity records), N2 (Doc_04 line ~150, the Decian sentence against Tertullian, *On Modesty* XXII) and N3/P2 ("in every congregation") — together with any new error these fixes introduced. Nothing else in Doc_04 is re-reviewed.
- **Ordered by:** the project lead's Cap ruling of 2026-10-23, "Cap ruling: lpc, a second targeted recheck for Doc_04, Doc_05 and Doc_09" (`Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`)
- **Truncation check, method 1:** line and byte count with an end-of-file read. `wc -l -c` gives Doc_04 273 lines / 77,996 bytes, the confessor-authority record 86 lines / 4,616 bytes, the penitential-discipline record 114 lines / 6,210 bytes. Doc_04 ends on the Disposition's closing sentence ("§7 Open Items 6 and 8 are closed."); each record ends on its provenance paragraph. Doc_04's headings §1 to §8 and the Disposition are present in order.
- **Truncation check, method 2:** hash comparison against the committed blobs. `sha256sum` of each working file equals `git show cd31eb55:<path> | sha256sum` (Doc_04 `d400afe58aab…`, confessor record `2e99cf7769ac…`, penitential record `9a4fa21ccb06…`). `git status --short` reports no modification under `records/lpc`, so the text read is the committed text.
- **Method limits:** no web search, no model call. Nothing edited but this file. Latin and English checked by direct read of the vendored files.

---

## Prior findings

| Finding | Status | Evidence |
|---|---|---|
| N1 (P1). The sermon-scope bound was not carried into the two gravity records | **Fixed** | Confessor-authority record lines 77 to 79 now read "A search of the texts tested here found no confessor-authority material from Augustine's phase. The sermons now in scope have not been searched for it. On the texts tested, the tension belongs to the first phase alone." "Anywhere in this world's sources" is gone. Penitential-discipline record lines 81 to 82 now read "No text we tested from Augustine's phase is built around a crisis like that of the lapsed, at the same acute, empire-wide scale. We have not tested the sermons now in scope." Both now match Doc_04 lines 150, 175, 182 and 190 and the retest carried at §7 item 9 (line 217). Both records are `register: etic`, so the build-voice "we tested" is in register, not a world-voice slip. The rest of the penitential-discipline rewrite changes wording only: readmission to "take that person back", "a laxer rival route" to "an easier rival road", with no fact dropped or added. |
| N2 (P1). Doc_04 still stated that the Decian persecution created the confessors' claim | **Fixed** | Doc_04 line 150 now reads "the Decian persecution made confessors a large class and made their claim acute, but it did not create the claim: Tertullian, *On Modesty* XXII (Registry row 29, a Named Comparandum and not this world's record), already describes offenders who 'seek peace at the hands of' imprisoned martyrs." Verified at source: the quoted words stand verbatim at `cic/texts/anf04_tertullian4-minucius-felix-commodian-origen1-2.xml:9565`, inside *Of Martyrs, and Their Intercession on Behalf of Scandalous Offenders* (div3 `iii.viii.xxii`, line 9550), where the suppliants are adulterers and fornicators besetting a prisoner in bonds, so "offenders" is a fair gloss. Registry row 29 is Tertullian, Excluded as a Named Comparandum (`Build/worlds/lpc/Doc_02_Source_Ecology.md:29`), so the citation carries its own boundary caveat, as the same correction does at Doc_05:86, Doc_07:192 and Doc_08:53. Doc_04 now agrees with the corrected records. |
| N3 (P2). "In every congregation" in the confessor-authority record is unsupported | **Partly** | The universal claim is gone: line 73 now reads "The Decian persecution put confessors in one congregation on a mass scale." But the replacement is taken from Doc_08:53, whose sentence is "It put the *lapsed* and the *confessors* in one congregation on a mass scale inside one year" — and dropping "the lapsed and" leaves a sentence that reads as if the confessors appeared in a single congregation. See N1 below. The identical "every congregation" wording also survives at `Build/worlds/lpc/Representative/lpc_Rep_Phase2_Formation_Calibration.md:49`; see N2 below. |

---

## New findings

### N1 (P2). The replacement for "in every congregation" no longer says what it means

- **Where:** `records/lpc/gravity/lpc.gravity.confessor-authority-vs-episcopal-peace.md:73`.
- **Evidence:** the source sentence is Doc_08's (`Build/worlds/lpc/Doc_08_Forces_Document.md:53`), and its point is that one edict put *both* the failed and the steadfast in the same congregation at once — the condition G2 and G8 answer. Shorn of "the lapsed and", "put confessors in one congregation on a mass scale" states a number ("mass scale") and a place ("one congregation") that pull against each other, and a reader cannot tell which is meant. Doc_04 line 150's own corrected wording ("made confessors a large class and made their claim acute") says the supportable thing plainly.
- **Why P2:** nothing false is now asserted, and the record's finding does not turn on the sentence; it is a clarity defect against the accessible-and-rigorous bar, in a record the Representative draws on.
- **Fix:** either Doc_04's own wording ("made confessors a large class and made their claim acute"), or Doc_08's full pairing.

### N2 (P2). The corrected claims were not swept into the Representative's Phase 2 calibration

- **Where:** `Build/worlds/lpc/Representative/lpc_Rep_Phase2_Formation_Calibration.md:49`, the G8 row: force "**1A-1** (puts confessors in every congregation on a mass scale)", and, later in the same cell, "**He does not carry this tension, or this claimed office, into his second-phase attestation**: no confessor-authority material exists there".
- **Evidence:** "in every congregation" is the exact phrase this pass removed from the gravity record, and `grep -rn "every congregation"` over `Build/worlds/lpc` and `records/lpc` finds it only here and in the tracking entry at `Build/worlds/lpc/Open_Gaps_Tracking.md:1757`. The flat "no confessor-authority material exists there" is the unbounded form of the claim Doc_04 lines 150 and 190 now bound, and the positive check the same cell relies on (`Build/worlds/lpc/Doc_05_Ecological_Reconstruction.md:128`) swept the eight NPNF English volumes `npnf101`–`npnf108`, which are not the Latin sermon editions now in scope. The build-cycle rule on corrections asks for a sweep through every copy of a corrected claim.
- **Why P2 and not P1:** the cell names the sweep's own scope two sentences earlier, the retest is already a registered open item (Doc_04 §7 item 9; `Build/worlds/lpc/Open_Gaps_Tracking.md` OG-52), and neither phrase reaches the compiled prompt — `grep` for "every congregation" over `packages/` returns nothing, and the permanent prompt carries no confessor-absence claim. If the project lead reads a Representative calibration document as load-bearing in the same way the gravity records are, this lifts to P1.
- **Fix:** carry Doc_04's corrected wording and its "texts tested here" bound into the G8 row, and log the sweep under OG-53.

### N3 (P2). Doc_04's superseded wording survives in the force-record generator

- **Where:** `Build/worlds/lpc/scripts/wb_lpc_s25.py:902-903` ("confessors as a category with any claim to authority at all … the Decian persecution, which is what creates confessors as a class") and line 1317 ("the same edict creates confessors as a class with a claim"), plus the unbounded "no Augustine-phase confessor-authority material is identified anywhere in this world's own corpus" at lines 904 to 907.
- **Evidence:** these are the sentences Round 15 found false against *On Modesty* XXII and unbounded against the sermon scope. The committed records now hold the corrected text, so the script and the records disagree, and a re-run would restore both defects into `records/lpc`.
- **Why P2:** the script is not the live source of the records as they now stand (the same divergence already exists for several other fields), so nothing in the canonical surface is presently wrong; the risk is a future regeneration.
- **Fix:** bring the generator into step with the corrected records, or retire it with a note, as the build thread decides for the sibling scripts named in `Doc_09_ChangeOrder_Recheck_Round10.md`.

---

## Summary

Both P1 findings Round 15 left open are fixed, and each is verified at the vendored source: the two gravity records now carry Doc_04's "texts tested here" bound, and Doc_04 line 150's Decian sentence is corrected and correctly cites Tertullian, *On Modesty* XXII, at `cic/texts/anf04_tertullian4-minucius-felix-commodian-origen1-2.xml:9565`. The P2 "in every congregation" is removed from the record, though its replacement now reads unclearly (N1) and the same phrase survives in the Representative's Phase 2 calibration (N2). No new P0 or P1 arises. The three new P2s should be logged under OG-53 and fixed in the next ordinary pass rather than by another review round.

VERDICT: Approved to proceed
