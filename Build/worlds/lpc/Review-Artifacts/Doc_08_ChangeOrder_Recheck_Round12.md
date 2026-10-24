Simulated review — informational only, not an Article 31 substitute.

# Doc_08 targeted recheck of the CO-LPC-1 revision pass

- **Document:** `Build/worlds/lpc/Doc_08_Forces_Document.md`, with `Build/worlds/lpc/lpc_Force_Index.md`, `Build/worlds/lpc/scripts/gen_force_index.py` and `records/lpc/force/*` (branch `claude/lpc-augustine-sermons-2026-10-23`, head `9a6d4d27`; diff checked: `git diff d6b449e6 9a6d4d27`)
- **Round:** 12
- **Reviewer:** Opus 5.5
- **Reviewer model:** Opus 5.5
- **Reviewer agent:** independent targeted-recheck subagent, fresh context (drafted none of the fixes)
- **Drafter:** Sonnet 5.5 (revision pass) and Opus 5.5 (renderings pass)
- **Drafter model:** Sonnet 5.5
- **Drafter agent:** the `lpc` build thread's revision-pass drafters
- **Date:** 2026-10-23
- **Scope:** targeted recheck of the revision pass. Only the Round 11 findings (`Review-Artifacts/Doc_08_ChangeOrder_Review_Round11.md`: P1-1, P2-1 to P2-6) are checked, each against the vendored source or upstream document where factual, plus any new error the fixes introduced, plus the Force Index regeneration. The rest of Doc_08 is not re-reviewed.
- **Ordered by:** the project lead's Cap ruling of 2026-10-23 ("Cap ruling: lpc CO-LPC-1 revision pass", `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`)
- **Truncation check, method 1:** line and byte count with an end-of-file read. `wc` gives 476 lines and 73,502 bytes. The last line ends "This document has now been through **eight** review rounds.", all 12 `## ` headings are present, and there are 17 `#### Force` headings.
- **Truncation check, method 2:** hash comparison against the committed blob. `git hash-object` of the working file and `git rev-parse 9a6d4d27:<path>` both give `c6ea54ad397e1b22e93319dfe6876843accc265f`. `git status` showed no change to tracked files before this file was written.
- **Method limits:** no web search and no model call. Nothing edited except this file. Generators run only on scratch copies under the session scratchpad. Readability scored with `engine/m7/turn_readability.score_turn`.

---

## Force Index regeneration

Doc_08, `gen_force_index.py` and the `Doc08_*` review files were copied to a scratch folder and the generator run as `gen_force_index.py <scratch>`. It exited 0 ("17 forces, 15 connections, 8 gravities"). `diff` against the committed `lpc_Force_Index.md` is empty, and both files hash to sha256 `9245dfe48ebf6444d2bda903ae04da595401187a3cace72a0598c35b433ba4c2`. The committed file was not touched.

---

## Prior findings

| Finding | Status | Evidence |
|---|---|---|
| P1-1 gap claim ruled false, attributed to Doc_02 §7 | **Fixed** | Doc_08:23 and :264 now state Doc_01's test as `Doc_02_Source_Ecology.md:122` words it ("no surviving voice continuous with Cyprian's ordinary-pastoral mode, from within this world's boundary"), name the gap-dated rows (Optatus rows 27, 64, 300; council canons; *Codex Theodosianus* rows 44, 88) and keep "Documented, on that narrower test". Rows 27, 44, 64, 88 and 300 exist as described (`Source_Registry.md`). Propagated: `records/lpc/force/lpc.force.transmission-asymmetric-span-133-year-silence.md:16` and the description; claims register now carries `12cba1a0`, `0f20f386` and `4e601197` with the new wording and `25da1952` is gone (`lpc_Claims_Register.md:101-102`); `Doc_05_Ecological_Reconstruction.md:27` (§0.3) carries the same test. |
| P2-1 review record stale and narrower than stated | **Not fixed** | Doc_08:14, :432, :470, :472 and :476 still say "eight" rounds and "the Round 8 fix pass… unreviewed"; Doc_08 does not record the CO-LPC-1 amendment. `gen_force_index.py:196` still globs only `Doc08_Round*_Review.md`. |
| P2-2 "six hits at two entries" not re-run | **Partly fixed** | Doc_08:399 drops the figure and says the hits sit inside the Reported-Experience Status paragraphs at 3B-1 and 3B-2. Those paragraphs (:252, :270) each carry "Forces Framework §3", so the location claim holds. The scan itself is still not re-run or counted. |
| P2-3 process narration | **Fixed** | :177 ("an independent review found…") removed; :403 restated without "named here for whoever next relies on this notice"; :405 "richer than the stubs they replaced" removed; the old :407 paragraph removed, and its Latin-only *Retractationes* disclosure survives at :256; :432 no longer narrates "five rounds and five fix passes". |
| P2-4 run-on sentence | **Fixed** | :474 "…create no `.xlsx` workbooks. Markdown is the required form…". |
| P2-5 2B-5 record overstates the translation gap | **Fixed** | `records/lpc/force/lpc.force.transmission-institutionally-dominant-side.md:81-82` "holds no complete English translation of it, and none of this passage". |
| P2-6 Layer 2 quotation count | **Fixed** | :209 and :428 "four quotations from Cyprian and one from the *Retractationes*". |

**The P1-2 propagation from the Doc_07 review, checked here because it edits Doc_08 and three force records.** Doc_08:53 now reads "made common… The pattern was not new. Tertullian, *On Modesty* XXII… 'seek peace at the hands of' imprisoned martyrs" (verbatim at `anf04_tertullian4-minucius-felix-commodian-origen1-2.xml:9565`). Connections 1A-1→2B-1 and 1A-1→2B-2 and the G2/G8 lines say "makes… a mass category" and "at scale"; the Index carries the same wording. The three edited force records (`decian-persecution-libelli-system`, `confessors-claim-to-grant-peace`, `recurring-contest-failed-member`) agree with Doc_08. No new factual error.

---

## New findings

**P2-A. Doc_08:264 says the *Codex Theodosianus* rows "date from the gap".** The Codex was compiled after the gap and *contains* laws from it. Doc_02 §7 and Doc_08:23 both say "date from it or record its events", which is accurate. Fix: use the same wording at :264.

**P2-B. Two edited force descriptions fell below the grade-8 floor.** `score_turn` on the `description` field: `decian-persecution-libelli-system` FK 7.7 / FRE 62.2, `recurring-contest-failed-member` FK 7.9 / FRE 62.0, both `below_floor=True`, no hard failures. CLAUDE.md treats grade 8 as a floor worth staying above. Nothing is wrong in substance; the plain-language edits ("give up", "get", "alone") shortened words past the floor. Fix at the next pass on these records, not by a separate round.

**Observation, not counted.** `scripts/wb_lpc_s25.py`, run on a scratch copy with its repository root redirected, regenerates all 17 force records differently from the committed records, including records this pass did not touch (for example `lpc.force.plague-of-cyprian.md`: different `canon_cells` and a pre-plain-language description). The drift predates this pass, so the script is not the live source of these records. Whether it should be retired or brought back in step is for the build thread.

## Summary

The one P1 is fixed at every site Round 11 named, in Doc_08, the 3B-2 record, the claims register and Doc_05 §0.3, and the restated wording matches Doc_02 §7 and the Registry. The Force Index regenerates byte-identically. Four of six P2s are fixed; the review-count record (P2-1) is not, and the hit scan (P2-2) is only partly. No P0 or P1 remains.

VERDICT: Approved to proceed
