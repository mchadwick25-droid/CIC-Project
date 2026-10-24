Simulated review — informational only, not an Article 31 substitute.

# Doc_02 and Source Registry targeted recheck of the CO-LPC-1 revision pass

- **Document:** `Build/worlds/lpc/Doc_02_Source_Ecology.md` and `Build/worlds/lpc/Source_Registry.md` (branch `claude/lpc-augustine-sermons-2026-10-23`, head `cd31eb55`; diff checked: `git diff d6b449e6 cd31eb55`)
- **Round:** 37
- **Reviewer:** Opus 5.5
- **Reviewer model:** Opus 5.5
- **Reviewer agent:** independent targeted-recheck subagent, fresh context (drafted none of the fixes)
- **Drafter:** Sonnet 5.5 and Opus 5.5 (revision passes)
- **Drafter model:** Sonnet 5.5
- **Drafter agent:** the `lpc` build thread's revision-pass drafters
- **Date:** 2026-10-23
- **Scope:** targeted recheck. Only the Round 36 findings (`Build/worlds/lpc/Review-Artifacts/Doc_02_ChangeOrder_Review_Round36.md`: P1-1 to P1-5, P2-1 to P2-9) are checked, against the vendored files and the project lead's rulings of 2026-10-23 in `Build/worlds/lpc/lpc_Decision_Log.md` (D3 clarified; D4 clarified; public-domain sermon scope; the 133-year silence qualified), plus any new error the fixes introduced, plus whether Doc_01 and Doc_02 now state the sermon scope, the D3 sentence, the Dolbeau line and the absence-record rule identically. The rulings are applied as given, not re-argued.
- **Ordered by:** the project lead's Cap rulings of 2026-10-23 (`Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`, "Cap ruling: lpc CO-LPC-1 revision pass, one targeted recheck per document", line 6879; and line 6883)
- **Truncation check, method 1:** line and byte count with an end-of-file read. Doc_02: 160 lines, 98,129 bytes; the last line ends "...from reopening any of the three documents."; ten `## ` headings present. Registry: 413 lines, 464,333 bytes; 308 numbered table rows, the last one row 308; the last line ends "...the same disclosure the sibling Donatism build's own Registry makes for itself."
- **Truncation check, method 2:** hash comparison against the committed blob. `sha256sum` of each working file equals that of `git show HEAD:<path>`: Doc_02 `a921e295ea27f4fb4461f06c2e4a123bb1a19d904120811b6b6a9ec28c6af745`; Registry `c096aae2bd91ef1efdb43ba03c61a7720ec1b2a02ea12233ab5d0a3cf6839e6e`.
- **Method limits:** no web search and no model call. Nothing edited except this file.

---

## Source markers verified

- **PL 39 contents.** `cic/texts/augustine_sermones-341-396-et-appendix-lat_migne-pl39.txt` line 192 "Sermones dubii. 1639"; line 194 "Sermonum Fragmenta. 1719"; line 196 "Appendix. — Sermones supposititii."; line 198 "I. De Scripturis. 1735". Holds.
- **Row 265, Classis V.** `cic/texts/augustine_sermones-ad-populum-lat_migne-gaume1841-t5.txt` line 117124 "CLASSIS V.", line 117125 "SERXffONES DUBII.", line 117130 "SERMO CCCLXIV". Holds.
- **Row 265, Appendix.** First running head "APPENDIX." at line 124390, so "from about line 124389" holds.
- **NPNF place headings.** `cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml` line 15408 (Sermon XL, "Delivered at Carthage in the Restituta"), line 17969 (`vii.lxvi-p4`, "Delivered at the Table of St. Cyprian"), line 19865 (`vii.lxxxiii-p4`). Holds.
- **Census.** A YAML parse of every atlas file in `cic/corpus-map/` gives this world 215 / 168 / 166 and `the-society-of-jesus.yaml` 123 / 99 / 99, next on all three counts, as Doc_02 line 15 now says.

---

## Prior findings

| Finding | Status | Evidence |
|---|---|---|
| P1-1 D3 rule differs between Doc_01 and Doc_02 | Fixed (now ruled) | `Doc_02_Source_Ecology.md:13` carries the ruled sentence word for word as `Doc_01_World_Identification_Boundaries_Orientation.md:30`: "On questions about Augustine, the Representative, Datus, answers from Augustine's own words and from the witnesses of his own time ... He does not answer from later readings of Augustine." |
| P1-2 Sermones 364 to 396 both in and out; Appendix mislocated | Fixed | `:13` "the Maurist *Sermones* 1 to 363, Classes I to IV"; both blocks excluded by name; `:49` gives each its own marker (PL 39 col. 1639 and row 265 line 117124 for the *dubii*; PL 39 col. 1735 and row 265 from about line 124389 for the Appendix), all verified above. Faithful to "D4 clarified". |
| P1-3 Latin sermon files called "the quote base" | Fixed | "quote base" no longer appears. `:49` "The Latin sermon files are second witnesses under `cic/texts/INTAKE.md`"; per row: 265 locating only, 268 finding aid only, 216, 217, 219 and 267 (33 sermons only) second witnesses until verified against the page image; "A sermon quote record can be made only from a passage that clears that rule." `:31` lists them as second witnesses, consistent. |
| P1-4 "preached to his own congregations at Hippo and Carthage" widened; circular licence | Fixed | `:19` "the NPNF headings place three of them at Carthage or at the Table of St. Cyprian" with the three loci, verified above. `Source_Registry.md:32` (row 19) Licensed For now says the same and no longer cites Doc_02 back. |
| P1-5 "against his own wishes" quoted as Augustine's | Fixed | `:19` now reads "presbyter in 391, against his own wishes, by congregational seizure", without quotation marks. |
| P2-1 Psalm exposition cited to the Latin row | Fixed | `:19` "(20 and 21; row 201 is Migne's Latin of the Psalm exposition)". |
| P2-2 all secondary files called Confidence C | Fixed | `:75` "Confidence B or C, per row". |
| P2-3 wrong next-largest census file | Fixed | `:15`, verified by YAML parse above. |
| P2-4 "Gaume 1841 printing" | Fixed | `:13`, `:31`, `:49` "Migne's 1841 printing" of Tomus V, row 265. |
| P2-5 §7 says the gap is attested only through Donatism's sources | Fixed | `:122` "mostly through sources that are Donatism's territory", "the list is not exhaustive", with row 11's letters from 386 as the example; the silence is qualified and Contested here and at `:128`. |
| P2-6 status lines name no current review | Fixed | `Doc_02_Source_Ecology.md:3` and `Source_Registry.md:3` name Round 36 as latest and the two checks before it. |
| P2-7 three Registry P2s from Round 34 | Partly fixed | Row 265 now points to rows 189, 171, 219, 267 and 268, and gives `CLASSIS V` at line 117124 and `SERMONES DUBII` at 117125 (`Source_Registry.md:330`). Rows 303 to 308 are still Confidence A with no Confidence sentence, and no Open_Gaps entry tracks it (see N2). |
| P2-8 process narration in the canonical file | Not fixed | `:133` ("for the first time"), `:138` (Round 14 to 18 history), `:160` ("for the first time since Round 14", the Round 30 account) are unchanged. Round 36 made this wait on the project lead's word on PROTECTED lines; carried, not escalated here. |
| P2-9 Morin 1917 counted without excluding the nine tractatus | Fixed | `:13` "Morin 1917, the 33 sermons only, row 267"; `:49` the same. |

---

## Doc_01 and Doc_02 side by side

| Item | Doc_01 (`:30`) | Doc_02 (`:13`) | Same? |
|---|---|---|---|
| D3 sentence | "On questions about Augustine, the Representative, Datus, answers from Augustine's own words and from the witnesses of his own time, such as Possidius, the councils and the letters written to and about him. He does not answer from later readings of Augustine." | identical | Yes |
| Dolbeau line | "Dolbeau's 26 sermons (1996, Registry row 50) are Augustine's but in copyright, so they are not used." | "Dolbeau's 26 sermons (1996, row 50) are Augustine's but in copyright, so they are not used" | Yes |
| Absence-record rule | "Where the sermons we hold do not speak to a question, an absence record says so, and it speaks only for those sermons." | identical | Yes |
| Excluded blocks | *Sermones dubii* (Classis V, 364 to 396) and the Appendix of *supposititii* | identical | Yes |
| Scope statement | "The world includes every sermon of Augustine in a public-domain edition held in the Library." | Opens "As Doc_01 §2 states, this world includes all of Augustine's sermons", and only later says "the scope is every sermon of Augustine in a public-domain edition held in the Library"; `:7` says "all of Augustine's sermons except the two blocks" | No (N1) |

---

## New findings

### N1 (P1). Doc_02 still says the world includes "all of Augustine's sermons", and attributes that to Doc_01

- **Where:** `Doc_02_Source_Ecology.md:13` ("As Doc_01 §2 states, this world includes all of Augustine's sermons:") and `:7` ("sermon scope (all of Augustine's sermons except the two blocks the Maurists judged doubtful)").
- **Evidence:** the ruling "Sermon scope is every public-domain sermon held" (Decision Log line 2551) sets the scope as "every sermon of Augustine in a public-domain edition held in the Library, less the two doubtful blocks". Doc_01 `:30` says exactly that. Doc_02 `:13` says the opposite first, then the same paragraph says Dolbeau's 26, which "are Augustine's", are not used. Line 7, the governing summary, carries only the wrong form.
- **Why it matters:** this is the defect the Dolbeau ruling was made to remove: a scope stated as all of Augustine's sermons lets an absence record claim more than the sermons held. Doc_02 also misquotes Doc_01 on it, and the brief requires the two to state the scope identically.
- **Fix:** at `:13`, "As Doc_01 §2 states, this world includes every sermon of Augustine in a public-domain edition held in the Library:", and drop the later restatement after the Dolbeau sentence; at `:7`, "(every sermon of Augustine in a public-domain edition held in the Library, except the two blocks the Maurists judged doubtful)".

### N2 (P2). Rows 303 to 308 still carry Confidence A with no Confidence sentence, untracked

- **Where:** `Source_Registry.md`, rows 303 to 308.
- **Evidence:** each row's Confidence column reads A and no row says why. Row 303 says its authorship "rests on the editor's judgment ... the Maurists doubted it", which sits oddly with A. No Open_Gaps entry names rows 303 to 308; OG-39 tracks only the Round 34 P1s.
- **Fix:** add a Confidence sentence to each row (or lower it), or log the item under OG-39.

---

## Summary

All five Round 36 P1s are fixed and verified at source, and eight of the nine P2s are fixed or partly fixed. Doc_02 carries the D3 sentence, the D4 exclusions, the Dolbeau line and the absence-record rule exactly as Doc_01 does. One substantial defect remains: Doc_02's scope sentence at lines 7 and 13 still says "all of Augustine's sermons", against the public-domain scope ruling and against Doc_01, which it claims to quote (N1).

Counts: 0 P0, 1 P1 (N1), 2 P2 open (N2, which carries the remainder of P2-7; and P2-8, carried).

VERDICT: Substantial revision required
