Simulated review — informational only, not an Article 31 substitute.

# Doc_01 recheck: the last P1 fix (Round 15 N6) and the Doc_09 sermon-scope line

- **Document:** `Build/worlds/lpc/scripts/wb_lpc_s21.py` (world_core Caution 2), `wb_lpc_s25.py` (force 3B-2 body), the two records they write, and `Build/worlds/lpc/Doc_09_Story_Inventory.md` line 105. The fixes are uncommitted in the working tree on top of head `8090fa1a`.
- **Round:** 16
- **Reviewer:** Opus 5.5
- **Reviewer model:** Opus 5.5 (claude-opus-5-5) for the whole run; no fallback to another model occurred
- **Reviewer agent:** independent recheck subagent, fresh context (drafted none of the fixes)
- **Drafter:** the `lpc` build thread
- **Drafter model:** not stated in the working tree (uncommitted, no trailer)
- **Drafter agent:** the `lpc` build thread's fix pass for Round 15 N6
- **Date:** 2026-10-24
- **Scope:** targeted recheck of three sites only: (1) world_core Caution 2 in `wb_lpc_s21.py` and its record; (2) force 3B-2's body in `wb_lpc_s25.py` and its record; (3) Doc_09 line 105's sermon-scope sentence. Plus a sweep of lpc records, scripts and Docs for any other site saying the gap holds nothing dated or no dated rows. Doc_01 itself is not re-reviewed.
- **Ordered by:** the project lead's Cap ruling of 2026-10-24 (`Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`, "Cap ruling: lpc Doc_01, a recheck of the last P1 fix", the file's last entry)
- **Truncation check, method 1:** line and byte count with an end-of-file read. `wb_lpc_s21.py` 4,521 lines, 308,933 bytes, ends `sys.exit(main())`; `wb_lpc_s25.py` 1,700 lines, 109,788 bytes, ends `main()`; force record 75 lines, 4,794 bytes, ends "making a claim."; world core record 432 lines, 27,231 bytes, ends "these five are not."; Doc_09 175 lines, 37,848 bytes, ends "draws on the 411 *Gesta*." Both scripts compile.
- **Truncation check, method 2:** reverse patch to the committed blob. `git diff` applied in reverse to copies of the five working files gives files whose `sha256sum` equals `git show HEAD:<path>` for each (s21 `cb833eae155b…`, s25 `95703ae031e4…`, force `bc44af2587ee…`, world core `c61569b2a74f…`, Doc_09 `b09aedcb932d…`). So each working file is the committed file plus exactly the reviewed hunks, nothing lost.
- **Method limits:** no web search and no model call. The generators were not re-run. Instead the `CAUTIONS` constant was read from `wb_lpc_s21.py` with `ast` and compared with the record's parsed `cautions` field, and the 3B-2 body string was read from `wb_lpc_s25.py` and compared with the record body. Both are equal. Nothing edited except this file.

---

## Prior findings

| Finding | Status | Evidence |
|---|---|---|
| Round 15 N6 (P1), site 1: world_core Caution 2 says the collection "holds nothing dated" in 258 to 391 | Fixed | `wb_lpc_s21.py:4219` to `:4222` and the record `:270` to `:273` now read: "Never describe what happened in those years from this world's own collection. Its few texts from those years, such as Optatus's polemic, the council canons and imperial law, record events but are not this world's own pastoral voice, so far as assessed." The false clause is gone. The three named kinds are real rows of this world dated inside the gap: Optatus (`Source_Registry.md` rows 27, 64, 300, Native; c. 366 to 393), the councils of Carthage I and II (rows 235 and 228, Native; c. 345 to 348 and c. 387 to 390), and the *Codex Theodosianus* (rows 44 and 88, Native; for example XVI.2.4 of 321). Doc_02 §7 (`Doc_02_Source_Ecology.md:122`) names all three and says "none of them is that voice". The force description (`wb_lpc_s25.py:1631` to `:1633`) says the same. "So far as assessed" keeps the qualification. Script and record match (parsed `cautions` equals the `CAUTIONS` constant). |
| Round 15 N6 (P1), site 2: force 3B-2 body rests on "the absence of dated Registry rows" | Fixed | `wb_lpc_s25.py:1685` to `:1687` and the record `:75` now read: "this force's own evidentiary base is the absence, so far as assessed, of this world's own pastoral voice in an interval". This agrees with the record's own description and `divergence_note` (no ordinary-pastoral voice "that this build has assessed"; Contested; OG-54) and with Doc_02 §7. It adds no claim. Script string and record body are equal. |
| Doc_09 line 105, "All of Augustine's sermons are inside the world" (noted outside scope in Round 15) | Fixed | Now: "These sermons are inside the world, which includes every sermon of Augustine in a public-domain edition held in the Library (Doc_01 line 30)". That is Doc_01 line 30's first sentence word for word, and the scope ruling's own words (`lpc_Decision_Log.md`, 2026-10-23, "Sermon scope is every public-domain sermon held"). The cited sermons fall inside it. Sermons 280 to 282 are Maurist Classis III, inside 1 to 363 and outside the excluded *dubii* (364 to 396); they stand in the PL 38 file at lines 89935 (`SERMO CCLXXX`), 90170 (`CCLXXXI`) and 90241 (`CCLXXXII`). The Scillitan sermon is Morin 1917 no. XXX, "De natale sanctorum Scillitanorum" (line 8466), one of the 33 Augustine sermons of the Guelferbytanus. It sits before the appendix of Optatus, Quodvultdeus and others (line 10297), so it is not among the nine unassessed tractatus. Morin 1917 is named in Doc_01 line 30. |

---

## Sweep for other sites

Searched `records/lpc`, `Build/worlds/lpc/scripts` and the lpc Docs for "nothing dated", "no dated", "dated row", "dated Registry", "dated-row", "no row dates", "holds nothing", "nothing survives", "genuine silence" and like phrases. Review files, the Decision Log and `Open_Gaps_Tracking.md` hits are historical records of the defect and are not counted. One live site remains (N8). `wb_lpc_s24.py:138` ("nothing survives in their own words") is about Numeria and Candida, not the gap. Doc_01 line 112's "a genuine silence in the surviving record" sits inside the paragraph that tags the claim Contested and limits it to what was assessed; Round 15 passed it and it is not a finding.

---

## New findings

### N8 (P2). A script docstring still calls 3B-2's basis "the dated-row gap"

- **Where:** `Build/worlds/lpc/scripts/wb_lpc_s25.py:66` to `:68`: "3B-2 (Transmission, the 133-year silence) rest on a fact about this world's own Registry (... the dated-row gap at 3B-2)".
- **Evidence:** the Registry has dated rows inside the gap (rows 27, 64, 300, 228, 235, 44, 88; Doc_02 §7). The emitted body at `:1685` now says the basis is the absence, so far as assessed, of this world's pastoral voice. The docstring now disagrees with the line it describes. Round 15 saw it and did not count it.
- **Why P2:** it is not emitted into any record and does not reach the Representative. It is a false sentence in a canonical script, and the next editor reads it.
- **Fix:** replace "the dated-row gap at 3B-2" with "the absence, so far as assessed, of this world's own pastoral voice in the gap at 3B-2".

### N9 (P2). Caution 2's new sentence says "few" texts that "record events", which is looser than Doc_02 §7

- **Where:** `wb_lpc_s21.py:4220` to `:4222`; world core record `:271` to `:273`.
- **Evidence:** Doc_02 §7 says its list of gap rows "is not exhaustive". It also names Augustine's own writings from 386 to 391 (row 25, *Soliloquies*; row 22, *On the Morals*; row 11's letters from 386). Those date from the gap but do not "record events" in the way Optatus or the canons do. The sentence's examples are all true. Its general predicate fits only the examples. The sentence also runs 30 words and ends on the clipped "so far as assessed".
- **Why P2:** nothing in it is false of the named texts, and it keeps the qualified silence. It does not make the Representative claim the gap is empty. A plainer form would read better.
- **Fix (optional):** for example, "Some texts in it come from those years, such as Optatus's polemic, the council canons and imperial law. None that we have assessed is this world's own pastoral voice."

### N10 (P2). Caution 2's unchanged rule reaches 386 to 391, which this world's own record covers

- **Where:** the retained clause "Never describe what happened in those years from this world's own collection" (`wb_lpc_s21.py:4219` to `:4220`; record `:270` to `:271`). Not changed by this fix pass; Round 15's suggested wording kept it.
- **Evidence:** "those years" are 258 to 391. Augustine's conversion (386) and baptism (387) fall inside them. Doc_01 lists both as catalysts of this world, and Doc_02 §8 rates them Documented. The same world core cites the *Confessions* as "Augustine's own conversion narrative" (record `:37`). Read literally, the caution forbids that use.
- **Why P2, not P1:** the caution's frame ("Donatism's territory") limits the practical reading to the Donatist decades, and the text predates this fix and every recent round. It is outside this recheck's mandate, which is the last P1 fix. It is still a real ambiguity in text the Representative is governed by.
- **Fix:** bound the rule to what it means, for example "the years between Cyprian's death and Augustine's conversion", or add "Augustine's own life from 386 is this world's record and is not covered by this caution". Track it in `Open_Gaps_Tracking.md` if not fixed now.

---

## Carried, not rechecked

Round 15's P2s N2, N4 and N5 were outside this recheck and were not rechecked. N7 (byte-for-byte reproduction) still applies: the world core record's edited paragraph was hand-wrapped (record `:273` runs past the generator's line width), so a re-run would rewrap it. Content is equal, as checked above.

---

## Summary

Both N6 sites are fixed. Caution 2 no longer says the collection holds nothing dated in the gap. It names the real kinds of text from those years, says they are not this world's pastoral voice, and keeps the "so far as assessed" qualifier. The 3B-2 body now names the qualified absence of a pastoral voice, matching its own description, its Contested rating and Doc_02 §7. Every claim added is backed by Registry rows and Doc_02 §7. Script and record say the same thing at both sites. Doc_09 line 105 now matches Doc_01 line 30 and the public-domain scope ruling, and Sermons 280 to 282 and Morin 1917's Scillitan sermon fall inside that scope. The sweep found one leftover, in a script docstring that is not emitted (N8).

Counts: 0 P0, 0 P1, 3 new P2 (N8, N9, N10). Round 15's N6 and the Doc_09 line are fixed. N2, N4, N5 and N7 carried, not rechecked.

VERDICT: Approved to proceed
