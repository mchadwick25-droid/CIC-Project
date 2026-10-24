Simulated review — informational only, not an Article 31 substitute.

# Doc_04 Gravity Discovery (lpc): targeted recheck of the revision pass

**Document:** `Build/worlds/lpc/Doc_04_Gravity_Discovery.md`, with `records/lpc/gravity/*`, `records/lpc/honest_limit/lpc.limit.411-gesta-unread.md` and `records/lpc/world_core/*` (branch `claude/lpc-augustine-sermons-2026-10-23`, head `9a6d4d27`; fixes read as `git diff d6b449e6 9a6d4d27`)
**Round:** 15
**Reviewer:** Opus 5.5
**Reviewer model:** claude-opus-5-5
**Reviewer agent:** independent Opus 5.5 recheck subagent (drafted none of the fixes)
**Drafter:** Sonnet 5.5 (revision pass) and Opus 5.5 (renderings pass)
**Drafter model:** Sonnet 5.5
**Drafter agent:** the `lpc` build thread's revision-pass drafters, after `Doc_04_ChangeOrder_Review_Round14.md`
**Date:** 2026-10-23
**Scope:** targeted recheck of the revision pass. Only the findings of `Doc_04_ChangeOrder_Review_Round14.md` (P1-1 to P1-4, P2-1 to P2-7) are checked, with any new error the fixes introduced. Also checked, as ordered: that the rewritten description of `records/lpc/gravity/lpc.gravity.confessor-authority-vs-episcopal-peace.md` keeps every fact of its previous version, and that its Tertullian claim is true. The rest of the document is not re-reviewed.
**Ordered by:** the project lead's Cap ruling of 2026-10-23 (System Hub Decision Log, "Cap ruling: lpc CO-LPC-1 revision pass, one targeted recheck per document", `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md:6879`)
**Truncation check, method 1:** line and byte count with an end-of-file read: `wc -l -c` gives 273 lines, 77,917 bytes. The file ends on the Disposition's closing sentence ("§7 Open Items 6 and 8 are closed."). Headings §1 to §8 and Disposition are present in order (lines 12, 16, 22, 154, 167, 192, 207, 220, 260).
**Truncation check, method 2:** hash comparison: `sha256sum` of the working file and of `git show 9a6d4d27:<path>` are identical (`d0314cb9…6c76a980`). `git status --short` shows Doc_04 and every file under `records/lpc` unmodified against the head, so the text read is the committed text.

## Method

Read Round 14 in full and the word diffs of Doc_04 and of the six records the pass changed. Each fix was checked at its site. Factual fixes were checked against the vendored files at their structural markers:

- Sermo 352: heading "SERMO CCCLll" (OCR of CCCLII) at `cic/texts/augustine_sermones-341-396-et-appendix-lat_migne-pl39.txt:4166`, §9 at line 4796, quotation at lines 4799 to 4802. The tome's index puts the *Sermones dubii* at column 1639 (line 192), after Sermo 362 (columns 1617 to 1629, lines 8877 and 9686).
- Letter LIV §1: `npnf101_augustine-confessions-letters.xml`, div3 `vii.1.LIV` (line 29860), paragraph "1." at line 29873, quotation at lines 29895 to 29896; Latin `augustine_epistulae-1-123-lat_goldbacher-csel34.txt:15466-15467`, under the address to Januarius at line 15401.
- Letter XLIII §19: div3 `vii.1.XLIII` (line 27539), paragraph "19." at line 28103, quotation at line 28126; Latin lines 12350 to 12351.
- Tertullian, *On Modesty* XXII: `anf04_tertullian4-minucius-felix-commodian-origen1-2.xml`, div3 `iii.viii.xxii`, "Of Martyrs, and Their Intercession on Behalf of Scandalous Offenders" (line 9550).

Doc_01 and Doc_02 quotations were checked against `Doc_01_World_Identification_Boundaries_Orientation.md:95, 102, 106, 110` and `Doc_02_Source_Ecology.md:40`. The OG-36 note-free counts were checked in `Open_Gaps_Tracking.md` OG-36. `records/lpc` was searched for "reachable", "untapped" and for unbounded Augustine-phase absence claims.

## Prior findings

| Finding | Status | Evidence |
|---|---|---|
| P1-1. Sermon scope (D1) changes the evidence under the negative Persistence findings | Partly | Doc_04 is fixed. Each of the four named sites now bounds its claim to "the texts tested here": Candidate 2 Persistence at line 47, Candidate 8 at line 150, the §5 closure at line 175 ("closed on the texts tested here: it did not persist ... the sermons now in scope have not been tested against it") and the §5 bullet at line 182. A sermon-scope statement (line 190) quotes Sermo 352 §9 correctly and glosses it accurately. §7 item 9 (line 217) carries the retest, and OG-52 (`Open_Gaps_Tracking.md:1749`) logs it. No §4 classification moves. **Not swept to the records built from those findings:** see N1. |
| P1-2. Candidate 5's search bound omits Letters XLIII and LIV; G5 states an unbounded absence | Fixed | Doc_04 line 90 now records both letters as restatements found and not weighed. The English and Latin quotations match the vendored files at the markers listed under Method. Line 94 applies the same bound to Persistence, and lines 162 and 169 read "each among the texts weighed". G5 (`lpc.gravity.conciliar-authority-theory.md:61-64`) now names both letters and bounds the claim to "the texts weighed". The Formation-test note for the project lead is at line 90, and the omission is logged at OG-52 (`Open_Gaps_Tracking.md:1749`). Minor: the Latin of Letter LIV runs onto line 15467 ("saluberrima auctoritas"), not line 15466 alone. |
| P1-3. World core presents closed Open Items 6 and 8 as live | Fixed | Caution 6 drops "A firm answer looks reachable" (`lpc.core.latin-pastoral-congregational-christianity.md:308`). The keyword note now reads "Doc_04 classifies it Supporting on the project lead's ruling" (line 422). The *Gesta* paragraph now reads "kept for narrow, checkable facts. They are not asked to settle what councils can decide" (line 257). `grep -rni "reachable\|untapped" records/lpc` returns nothing. |
| P1-4. §7 Open Item 6 mixes superseded and current text | Fixed | The "original item read" passage, with its order to commission a read, is deleted. Item 6 (line 214) now holds the precedent §4a closure, the act-158 finding with its line-by-line grounds, and the row 65 concordance. |
| P2-1. Doc_02 quotation left uncorrected | Fixed | Line 56: "Augustine argues *with* Cyprian, disputing his ruling while claiming his communion", which matches `Doc_02_Source_Ecology.md:40` and Doc_01 lines 102 and 106. |
| P2-2. Two Doc_01 quotations carry an inserted "own" | Fixed | Line 65: "Tested against this document's hardest instance" (Doc_01:110). Line 175: "is Doc_04's to confirm" (Doc_01:95). |
| P2-3. Doc_03 counts restated without the matching rule | Fixed | §7 item 10 (line 218) gives the apparatus-included figures and the note-free 106, 139 and 91. These match OG-36. |
| P2-4. Record sentences say more about the *Gesta* than is known | Fixed | G5 line 85: "We do not ask the 411 Gesta ... to settle it. They have not been read in full." Limit record line 27: "So we cannot tell you how our own bishops ... argued authority"; "yet" is gone. |
| P2-5. Status, Disposition and §8 out of date; narration survives | Partly | Line 3 is now a true status line. §8 adds the 2026-09-29 check, the L0 check, CO-LPC-1, Round 14 and the revision pass (lines 252 to 256). The narration at old lines 207 ("own restored"), 213 (the Round 2 assessment), 214 ("a sixth attempt ... nine rounds") and 259 to 261 (Round 11 quotations, "twelfth round") is removed. The Disposition was not reduced to the disposition and the open escalation. It still carries the "stated plainly because the gap is unusually wide" and "recorded so no later document mistakes it" framing (lines 264 and 271). The §8 row for the revision pass (line 256) has "—" in its file and outcome cells. |
| P2-6. G1 claims sermon collections for both bishops | Fixed | `lpc.gravity.pastoral-office-flock-keeping.md:62-63`: "It appears in Cyprian's letters and treatises. It appears in Augustine's sermons." |
| P2-7. Residual narration and stale facts in the records | Fixed | World core caution 11 is rewritten without "has not yet returned" (line 338). The registry sentence now names `records/worlds/lpc.yaml` (line 425), which exists. G5's `divergence_note` drops "the sharpest such divergence" and "Doc_01's nine rounds" (line 15). "It should be said plainly" and "stated plainly rather than padded" are gone (G5 lines 61, 89). The G1 and G5 provenance lines both read "Taken from" (G1:101, G5:105). |

## Confessor-authority record (G8): rewritten description against its previous version

The previous description was compared paragraph by paragraph with the current one (`lpc.gravity.confessor-authority-vs-episcopal-peace.md:40-78`). The following are kept: the tension is unresolved; the evidence rests mainly on Cyprian's letters, read through one lexicon term; the confessors survived questioning under persecution and wrote requests naming lapsed people; Cyprian's bishop-controlled penance was built to answer that claim; Letters XX and XXI show the confessors in their own voice; De Lapsis and the letters on penance show his answer; penance has its shape because the rival claim existed; Cyprian keeps restating the bishop's control; the tension is bounded to Cyprian's crisis years and does not organize the world; it competes with penitential discipline and supports the pastoral office; the A and B citation grades; the Valerianic persecution ended the phase; the confessors' claim is itself a force; all three forces belong to the first phase.

**One fact was deliberately replaced.** "The Decian persecution created confessors as a class with any claim to authority at all" became "put confessors in every congregation on a mass scale. Their claim was not new". That is a correction, and the correction is right.

**The Tertullian claim is true.** *On Modesty* XXII (`anf04`, div3 `iii.viii.xxii`, line 9550) describes sinners who crowd round a Christian newly in bonds, "and they seek peace at the hands of those who are risking their own". Tertullian calls these prisoners "martyrs"; they are living, imprisoned confessors, so "sinners who ask confessors for peace" is a fair rendering. The treatise is Tertullian's, well before 250.

**Small shifts in strength:** "instead of settling it once" became "He cannot settle it once" (line 59). "Does not fully explain that insistence" became "does not explain how hard they press" (line 60), which drops "fully". Neither changes the finding, and neither is raised. The new sentence "in every congregation" is raised at N3.

## New findings

### N1 (P1). The sermon-scope bound was not carried into the gravity records built from the findings it bounds

- **Where:** `records/lpc/gravity/lpc.gravity.confessor-authority-vs-episcopal-peace.md:77-78`: "A search found no confessor-authority material from Augustine's phase anywhere in this world's sources. So the tension belongs to the first phase alone." `records/lpc/gravity/lpc.gravity.penitential-discipline.md:79-82`: "Whether it continues into Augustine's phase was checked directly ... No text from Augustine's phase is organized around a crisis like that of the lapsed".
- **Evidence:** Doc_04 now says the opposite about the scope of these same findings. Line 150: "no Augustine-phase confessor-authority material is identified in the texts tested here ... The sermons now in scope were not searched for it." Line 190: these are findings "on the texts tested here. It is not a finding about the sermons now in scope." The G8 sentence was rewritten in this very pass and still says "anywhere in this world's sources". The G2 record was not touched. This is the same defect Round 14 rated P1 in the G5 record (P1-2): a record states an unbounded absence that its own source document bounds. These records are what the Representative draws on. The build-cycle rule on corrections requires a sweep "through every copy of the claim, and not only the named sites" (`SKILL.md`, Naming and term propagation).
- **Fix:** bound both sentences to the texts tested, and say the in-scope sermons have not been searched (Doc_04 §7 item 9). For G2, the Sermo 352 passage need not be named, but "No text from Augustine's phase" must become a claim about the texts tested.

### N2 (P1). Doc_04 still states the confessor fact that this pass corrected in the G8 record and its force record

- **Where:** Doc_04 line 150 (Candidate 8, forces-connection notation): "the Decian persecution is what creates confessors as a category with any claim to authority at all, since a confessor's own standing rests entirely on having survived interrogation under that specific persecution."
- **Evidence:** *On Modesty* XXII (`anf04`, div3 `iii.viii.xxii`, line 9550) shows sinners seeking peace from imprisoned confessors decades before Decius. OG-52 (`Open_Gaps_Tracking.md:1749`) logs this as an older error ("confessors granting peace before 250 (Tertullian, *On Modesty* XXII)"). The pass corrected it in the G8 record ("Their claim was not new") and in `records/lpc/force/lpc.force.confessors-claim-to-grant-peace.md` (old: "existed as a class with a claim only because the Decian edict created them"; new: "The Decian edict made confessors a large class with a claim"). It did not correct Doc_04, which is the source those records are "taken from". So the gravity spine now contradicts its own record, and it is false against a vendored primary source. Candidate 8's Tensional classification does not depend on the sentence.
- **Fix:** restate line 150 to match the corrected record. The Decian persecution made confessors many and made their claim acute. It did not create the claim, which Tertullian already attests. Then search Docs 05 to 09 for the same sentence.

### N3 (P2). "In every congregation" in the G8 record is not supported

- **Where:** `lpc.gravity.confessor-authority-vs-episcopal-peace.md:73-74`: "The Decian persecution put confessors in every congregation on a mass scale."
- **Evidence:** Doc_04 makes no such claim, and no source cited in the record gives confessors for every congregation. "Many confessors" is attested by Cyprian's letters; "every congregation" is a universal claim with nothing behind it.
- **Fix:** "The Decian persecution made confessors many" or similar, at the scope the sources show.

## Summary

All four Round 14 P1 findings are fixed in Doc_04 and at the record sites Round 14 named. P1-1's bound was not carried into the G2 and G8 gravity records (N1). The Tertullian correction made to the G8 record is true and keeps every other fact of the earlier version. But Doc_04 line 150 still states the corrected claim (N2). Of the P2 findings, six are fixed and P2-5 is partly fixed. Two P1 findings remain open, so per the Cap ruling they go to the project lead.

VERDICT: Substantial revision required
