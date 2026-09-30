Simulated review — informational only, not an Article 31 substitute.

# Doc_02 and Source Registry: targeted recheck of the directed corrections of 2026-09-29 (lpc)

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent-review subagent, fresh context, launched from session_019FXuEebrCDmzYe987sNAxL (wrote none of the text under review)
- **Drafter agent:** Library-thread drafting worker (commits 34e2128ac, b29cf8989 and cb2840bd7; commit trailers read "Claude Sonnet 5.5")
- **Round:** 32 (a targeted recheck of the directed corrections of 2026-09-29; not a new revision cycle)
- **Truncation check, method 1:** structural count. Registry: 244 table lines, every one with exactly 12 pipes; 242 numbered rows forming exactly the set 1 to 242, no gap and no duplicate; the file ends on a complete sentence and a newline. Doc_02: headings §1 to §10 all present, in order; §10 ends on a complete sentence and a newline.
- **Truncation check, method 2:** byte and hash comparison against the committed blob at HEAD cb2840bd7. `wc -c` equals `git cat-file -s` (Registry 310,331 bytes; Doc_02 85,767 bytes), and `git hash-object` equals `git rev-parse HEAD:<path>` for both files (Registry 8b608f0f…, Doc_02 d4cc4df4…).
- **Date:** 2026-09-29
- **Documents:** `Build/worlds/lpc/Doc_02_Source_Ecology.md`, `Build/worlds/lpc/Source_Registry.md`, as committed at HEAD cb2840bd7
- **Severity vocabulary:** P0 blocks, P1 must be fixed but is not disqualifying, P2 polish (P0/P1/P2 correspond to HIGH/MEDIUM/LOW in Rounds 1 to 30).

## Verdict

**Not clear.** 0 P0, 2 P1, 9 P2.

Every finding of the 2026-09-29 independent check (P1-1 to P1-6, P2-A to P2-F) is fixed, and each fix is true at the vendored source. The verifier's five late fixes hold, with one residue at row 214. The CSEL 58 reversion is complete and consistent. The corpus figures are right by two methods.

The two P1 findings are both in material the later commit added. The sweep paragraph says the `csel-dev` repository holds no Cyprian or Optatus. It holds both. And Doc_02 §3 still counts five vendored secondary works, where there are now fifteen.

Nothing found misstates the historical world or invents a source.

## Scope 1: the findings of the 2026-09-29 check

| Finding | Status | Checked at source |
|---|---|---|
| P1-1 Doc_02 CIL VIII and *Codex Theodosianus* wording | Fixed | Doc_02 §5 now names both files as held. CIL file header "Numidiae Latinarum Supplementum", title page `BEROLINI APVD GEORGIVM REIMERVM` / `MDCCCXCIV` (lines 115–116). No "not currently vendored" or "own branch" phrase is left in either file. |
| P1-2 Row 44 narrowing | Fixed; letter escalated | `XVI, 5, 21 (392 lun. 15).` heading at line 86853; operative clause 86855–86857 with `viritim` on 86856; `denis libris auri proposita condemnatione multentur` at 86863. The cell now says what was read and not read, and leaves the letter undecided. |
| P1-3 Row 65, act 158 | Fixed | Fourteen line-initial `N. Augustinus` lines, reproduced by grep; act 158 at 121764 stops at `episcop`, and 121768 reads `mendalum ·usccpi fll nibacripsj`. Thirteen speeches, a floor. Roster `ACTORES VII.` at 113068, `Augustinus Uipporegiensis.` at 113076. Doc_04 reliance is stated. |
| P1-4 Rows 14 and 213 | Fixed; split letter escalated | Row 213 now states the cluster sits only in `donatism.yaml`, discloses the row 43 overlap, and names Letter LIII as joint (`vii.1.LIII`). Row 14's Latin markers are real: `CONTRA LITTERAS PETILIANI` 24752, `LIBER SECUNDUS` 25771, `LIBER TERTIUS` 33390. Doc_02 §1 now says row 14 grounds one claim. |
| P1-5 Corpus count | Fixed | See Scope 5. |
| P1-6 Possidius | Fixed | `CHAPTER VIII` at 2075, heading 2076–2077, `Megalius, Bishop of Calama` 2131–2132; `CHAPTER XXXI` at 4916 (English) and 5960. Doc_02 §2 and §4 now say the whole *Vita* was read, by the drafting thread. |
| P2-A Row 65 branch wording | Fixed | Now "Not currently vendored (Lancel's edition)." |
| P2-B Line numbers rows 44 and 65 | Fixed | All on the current base. |
| P2-C Rows 29 and 204 | Fixed | Both cite `latin-apologists`; `tertullian-s-voice` appears once, as the name of the merged entry. |
| P2-D Row 189 path | Fixed | Full path; the file exists. |
| P2-E Row 14 locus, row 213 joint letter | Fixed | "chapter 51 (section 118)"; LIII called a joint letter. |
| P2-F Doc_02 Status | Fixed | Now discloses edits after disposition and names the check they answer. |

## Scope 2: the verifier's five late fixes

1. **Row 44, gold and silver.** Holds. `XVI, 5, 52 (412 lan. 30>.` at 87872; every rank from `inl^ustres` (87878) to `plebei` is `auri pondo`; only `circumcelliones argenti pondo decem` (87882) is silver. The row now says exactly this.
2. **Row 214, letter B.** Holds under the rule. The Licensed-For is cross-checking NPNF, done at one opening only (Book I §1, line 8510, against `npnf104` div4 `v.iv.iii.i`).
3. **Rows 215–217, grep facts.** Hold. Case-insensitive, over `.txt` and `.xml` files only: `Parmenian` 26 files, `Cresconi` 34, `unico baptismo` 5. The three rows use the same convention.
4. **Row 217, the address.** The wording is now right: Augustine addresses the reply to Constantine. The marker is not (P2-1).
5. **Rows 214 and 216, present truth.** Row 216 holds: `Pars II (CSEL 52)`, title page 24189–24213, `PRAEFATIO.` 24247. Row 214 keeps one stale sentence (P2-2).

## Scope 3: new rows reopened (twelve of 25, plus 214–217)

Calibration rule, as the Registry states it: "Confidence **A** is used only where a row's Licensed-For content was itself directly read and verified against the vendored text … **B** is used where a specific work or locus is named accurately but was not independently re-checked against the vendored text. **C** is tied to a real author/work with no specific locus pinpointed. **D** is genre/tradition-level attribution with no specific text or author named."

| Row | File, header, rights | Markers | Letter under the rule |
|---|---|---|---|
| 218 TEI *De fide et operibus* | Exists; CC BY-SA licence element line 49; csel-dev path `stoa041` matches | 107, 110, `<pb n="97"/>` 2829, `Explicit liber beati` 2860: all real | B consistent |
| 222 TEI *De mendacio* | Exists; header "machine-corrected transcription" is in the header (line 8); path `stoa050` | 107, 110, `cotidianis actibus` 111, 2432, 2437: real | B consistent |
| 225 CSEL 41 scan | Exists; `MDCCCC` 143, 176; host date 1866 recorded; Harvard copy | 234, 2307, 6833–6834, 26505, 32564: real; 14 corpus entries, one `provisional` | B consistent; stale header remark (P2-2) |
| 226 Krueger *De catechizandis* | Exists; 1893 at 55; `augustindecatech00augu` | 475 real; title page marker imprecise (P2-3) | B consistent |
| 227 Migne sermons t. V | Exists; header names Migne, Petit-Montrouge, 1841 preface | 699, 106615, 117124 real | C rests on OCR quality, not on the rule's text (decision 6) |
| 229 Morin 1917 | Exists; `MN41725ucmf_2` | `MCMXVH` 100, imprimatur 118, 1775, 10303 real | B consistent |
| 230 Caillau 1842 | Exists; `bub_gb_smqVbL56i0oC` | 40, 3105, 3798 real | C on OCR and ascription (decision 6) |
| 231 Knopf-Krueger 1929 | Exists; 1929 at 53; `Alle Rechte vorbehalten` recorded | 4820, 4823, 2438 real; Perpetua marker wrong (P2-4) | B consistent |
| 232 Gebhardt 1902 | Exists; `actamartyrumsele0000gebh` | 6474–6475, 6481–6482, 1560, 6920, 7492 real; OCR remark wrong (P2-5) | B consistent |
| 233 Koch 1926 | Exists; `Copyright 1926` at 109, recorded | 80, 326, 362 real | C matches rows 205–212 |
| 238 Benson 1897 | Exists; Macmillan | 77, 92, 455 real | C matches precedent |
| 242 von Soden 1909 | Exists; slice of `quellenundforsch12deutuoft` pp. 1–42; host date 1898 recorded | heading 12–16 real; footnote cross-reference is in the header | C matches precedent; row 211 left stale (P2-6) |

Each Licensed-For is confined to what was checked, or it says outright that a passage must be checked first. Rows 231 and 232 license only the three Cyprianic acts. Row 229 declines to license the nine tractatus.

## Scope 4: the CSEL 58 reversion

Complete. Neither document says CSEL 58 is vendored. Rows 61, 193, 195 and 196 and Doc_02 §1 and §9 all say it is not vendored, and all give the Johnson facsimile reason. The retired file and its staging file are renames into `Archive/Retired-Library-Texts/`, whose README states the ground. The retired file itself prints `Reprinted with the permission of the original publishers` (53), `JOHNSON REPRINT CORPORATION` (55) and `First reprinting, 1961, Johnson Reprint Corporation` (98). `cic/texts/` and `cic/corpus-map/` hold no `csel58` file or entry. `REGISTRY.yaml` mentions CSEL 58 only in notes on the CSEL 34 and 44 rows ("remains open"), not as an entry. `python3 cic/engine/texts_registry.py` exits 0 and prints OK. One overstatement remains (P2-7).

## Scope 5: corpus figures, recounted two ways

- **Method A, YAML parse** of each atlas file's `works:` list (excluding `AUTHOR-IDS`, `PAIRS`, `UNATTRIBUTED`). Results: lpc 151 raw, 131 `tradition`, 129 distinct `tradition` titles, 20 `context`. `latin-apologists` 98/96/44. `alexandria-catechetical` 69/61/61. `post-apostolic-house-church` 95/84/58 is third on raw, so the "next-largest" statements hold.
- **Method B, line grep** of `^- work:`, `^  role: tradition` and `^  role: context` in the three files. Results: lpc 151/131/20, apologists 98/96/0, alexandria 69/61/8. These agree with Method A.
- **Exact-title duplicates:** 2, the *Enchiridion* and the *Scillitan Martyrs*.
- **Context entries:** 20. There are 17 modern works dated 1894 to 1930, plus Prosper, the Latin Library *Codex*, and the *Gesta*.
- **Second-witness entries:** 39. That is 12 earlier ones plus 27 from the sweep. The 27 were rebuilt from each entry's note:
  - CSEL 41 plus TEI: 21 entries, of which 4 are counted once (*De adulterinis*, *De divinatione*, TEI *De agone*, TEI *De fide et operibus*). That leaves 17.
  - Krueger: 1.
  - Migne: 3 (*Sermones dubii* is counted once).
  - Gebhardt and Knopf: 6 (one *Marianus* and one *Montanus* are counted once).
- **Counted once:** 131 − 2 − 39 = 90. All true.

## Scope 6: the sweep paragraph

- **The bibliographies were opened.** `download-queue-seed.yaml` has 42 new rows: 25 vendored, 5 verified but held, 12 reference-tier. That matches the paragraph. On archive.org, `geschichtederalt0003otto` (Bardenhewer 3, 1912), `bub_gb_J1sKAQAAMAAJ` (Bardenhewer 2, 1914), `dictionaryofchri0001will` (Smith and Wace vol. 1, 1877) and `geschichtederrm01krgoog` (Schanz, 1896) resolve to the works named.
- **The sandbox list** is consistent with what I saw. `ccel.org` and `thelatinlibrary.com` do not connect. `gallica`, `babel.hathitrust.org` and `github.com` return 403. The `api.github.com` contents call returns 403. `raw.githubusercontent.com` answers.
- **The `csel-dev` claim is false (P1-A).**

**P1-A. Registry, Saturation statement, "Field-bibliography sweep", Method: "It holds no Cyprian, Optatus or Tyconius textgroup."** The repository holds Cyprian and Optatus under suffixed textgroup ids. The probe covered bare ids only.

- `data/stoa0104a/__cts__.xml` names "Cyprian Saint, Bishop of Carthage". Works `stoa001` to `stoa015` exist, from *Ad Donatum* to *De Dominica Oratione*, with *Epistulae* at `stoa012`. `stoa0104a.stoa007.opp-lat1.xml` (*De Lapsis*, 108,519 bytes) describes itself as Hartel, CSEL 3.1, Vienna 1868.
- `data/stoa0215a/__cts__.xml` names "Optatus, Saint, Bishop of Mileve". `stoa001` is *S. Optati Milevitani libri VII* (the text file is 664,596 bytes) and `stoa002` is the *Appendix Decem Monumentorum Veterum*, both from Ziwsa's CSEL 26.
- No Tyconius textgroup turned up under any `stoa0001`–`stoa0420` id with or without an `a`/`b` suffix. That part of the claim stands as far as I checked.

This matters beyond wording. Row 191 (Hartel CSEL 3) sits at C on OCR grounds, and a machine-corrected TEI of the same edition exists. The Optatus appendix is the Donatist documentary dossier. The sentence must be corrected. The "did not reach" paragraph should also say that suffixed textgroup ids were not probed.

## Scope 7: the narration removal

I checked twenty cuts against HEAD: A5 to A25 of `Build/Ministry/Operations/Audits/lpc_Doc02_Registry_Narration_Moved_2026-09-29.md`, covering rows 1, 6, 28, 37, 39 (three cuts), 40, 41, 45, 56, 61 (two cuts), 64, 67, 78 (two cuts), 88, 89, 90 and 99. In every case the fact survives in the row, and only a date or a Decision-Log pointer moved. The audit file carries the moved text verbatim. No fact was lost.

One residue: row 78's "had not been located despite repeated searches across two rounds prior to — closed as stated above — disclosed" was broken before the cut and is still broken (folded into P2-9).

## Scope 8: truncation

Both methods are in the header. Both files are complete.

## Scope 9: decisions for the project lead

The escalations are unchanged and correctly stated as open:

- Row 44 is B, and the row says "which letter the calibration rule assigns on that reading is undecided".
- Row 33 is C and points to OG-20. The only change in the diff is "an open question — see" to "undecided (OG-20)".
- Row 11 (A, "not decided") and row 14 (A, "A for that one locus and B for the rest") are untouched.

Recommendations:

1. **Row 44: A.** The Licensed-For content (the statute behind §25's fine) has been read at XVI.5.21 and mapped clause by clause, which meets the rule's bar for A. The one inference, that §25's "Theodosius" is the author of the constitution, is stated in the row.
2. **Row 33: B.** This matches rows 30–32, which are WebSearch-verified and unread.
3. **Split letters (rows 11 and 14): one letter per row.** Narrow each Licensed-For to what was verified, so the row earns A. Move the unverified body-level claim to a separate B row or to the Comparandum Note. This keeps the verified locus usable without a two-letter cell.
4. **Petschenig rows 215–217 at A: keep.** Their Licensed-For is the work's identity, its voice and the absence of any English rendering. All three are verified at heading, opening, close and by grep.
5. **TEI and machine-corrected rows 218–224, and rows 225, 226, 229, 231 and 232 at B: keep.** The rule applies as written.
6. **Rows at C on OCR grounds (227, 228, 230; precedent 191, 193): a methodology call.** The rule's text ties C to the absence of a pinpointed locus, not to OCR quality, and these rows do pinpoint loci. Recommend amending the rule text to state the OCR ground, since two approved rows already rely on it. The alternative is re-lettering them B.
7. **Scholarship rows 233–242 at C: keep.** This matches rows 205–212.
8. **Compound Boundary Status on rows 231 and 232 (and row 229 in effect): decide with item 3.** "Native" for the Marianus, Montanus and Cyprian acts is right on date and place (Cyprianic-period Africa, 258–259). But a cell that holds several statuses has the same shape as a split letter.
9. **Row 225 (the CSEL 41 volume as a second witness) at B: keep.**
10. **Vendoring the `csel-dev` Cyprian and Optatus TEI** is an acquisition question for the source-research thread, not an escalation. It is noted here only because P1-A hides it.

## Scope 10: new errors

**P1-B. Doc_02 §3, line 73: "Five older, public-domain secondary works are now vendored in full".** Rows 233–242 add ten more: Koch ×3, Poschmann, d'Alès, Benson, Mesnage, Toulotte, Audollent and von Soden 1909. §3 names none of them. Doc_02 §1 sends the reader to "§3 below" for "seventeen of those twenty modern, 1894–1930" context entries, but §3 lists seven files (five works), dated 1901 to 1921. This is the same kind of error as the 2026-09-29 check's P1-5: a present count made false by later vendoring.

- **P2-1. Row 217 Licensed-For:** `Constantine frater` is cited at line 60981. It is on line 60982, and 60981 carries `Respondere diuersa sentientibus et a regula ueritatis`.
- **P2-2. Stale header remarks.** Row 214 still reads "File header: … CSEL LI (Pars I, 1908) and LIII (Pars III, 1910)" and says the header records the G5 request. That describes the header b29cf8989 replaced. The current header names LI, LII and LIII, and the G5 note is in `REGISTRY.yaml`, not the header. Row 225 says "the file header's content note says thirteen". cb2840bd7 changed it to "fourteen".
- **P2-3. Row 226:** the title page "naming Wolfhard and Krueger (line 46)" is imprecise. Line 46 carries only Wolfhard; `Gr. Kruger.` is on line 52.
- **P2-4. Row 231:** the marker `Passio Perpetuae` (line 3538) is a bibliography entry (d'Alès, *Revue d'histoire ecclésiastique* 1907), not the act. The act runs under `8. Martyrium der Perpetua und Felicitas.` (running head at 2909).
- **P2-5. Row 232:** "The header does not assess the OCR" is wrong. The header's Language line says the Latin is "readable text with occasional C/O letter misreads".
- **P2-6. Row 211** still says the von Soden *Ketzertaufstreit* article is "Not yet vendored". Row 242 vendors it and only notes the discrepancy.
- **P2-7.** Doc_02 §1 and §9, and rows 61, 193, 195 and 196, say "the only public scan of CSEL 58 is" the Johnson facsimile. The Archive README supports only "no other public scan … on the Internet Archive". Scope the claim to what was searched.
- **P2-8. Saturation, Method:** "The others were opened and their title pages read" does not hold for Schanz 1896. Its queue row says "the title page was not confirmed".
- **P2-9. Registry Status line** still says the 2026-09-13 return "has not yet returned". Doc_02's Status names the 2026-09-29 check the corrections answer. Also row 78's broken clause (Scope 7).

## Not verified

- Tyconius was checked only across unsuffixed and `a`/`b`-suffixed `stoa` ids.
- The Bardenhewer name counts, and the content of the reference works beyond their archive.org metadata, were not checked.
- The "41 files" count for Augustine in `csel-dev` was not checked.
- The OCR line counts in rows 218–242 were not recomputed. The verifier reproduced those for rows 214–217.
- The Possidius read's word count was not checked.
- I did not re-read the Doc_02 sections the corrections did not touch.

## Outside this scope, noted only

- `Doc_04_Gravity_Discovery.md` line 7 still quotes row 65 as "not yet drawn on by it".
- The records and scripts the verifier listed (Lancel `license: public-domain`, "fourteen acts", "silver-fine schedule", `tertullian-s-voice`) are unchanged.
- OG-20's heading ("has never run the V7.4 field-bibliography sweep") is now out of date. The file is append-only, so this needs a new entry rather than an edit.
