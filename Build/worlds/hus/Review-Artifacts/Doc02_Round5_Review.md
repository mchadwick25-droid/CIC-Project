Simulated review — informational only, not an Article 31 substitute.

# Doc_01, Doc_02, Source Registry and gap ledger: second targeted recheck after the new sources (hus)

- **Reviewer model:** claude-opus-5-5
- **Drafter model:** Sonnet 5.5
- **Reviewer agent:** independent-review subagent, fresh context, launched from session_019FXuEebrCDmzYe987sNAxL (wrote none of the text under review)
- **Drafter agent:** hus build-thread drafting worker (revision commit 7ee370987; commit trailer reads "Claude Sonnet 5.5")
- **Round:** 5 (round 2 of the new-material cycle opened by the Library's acquisition of 2026-09-30; Round 1 is `Doc02_Round4_Review.md`)
- **Truncation check, method 1:** structural count. Doc_01: headings §1 to §10 present and in order, 219 lines, ends on the §10 disposition sentence and a newline. Doc_02: headings §1 to §11 present and in order, 224 lines, ends on the §11 disposition sentence and a newline. Registry: 79 numbered rows, every one with exactly 12 pipes, numbers exactly the set 1 to 79; Confidence letters A 33, B 18, C 18, D 1, "—" 9 (row 67 moved from B to A). Open_Gaps: 37 numbered entries, 1 to 37 with no gap; the diff of 7ee370987 deletes no line of the file, so entries 1 to 35 are unchanged; the file ends on a complete sentence and a newline.
- **Truncation check, method 2:** byte and hash comparison against the committed blob at HEAD 9c1b226b2 (no `hus` file changed after 7ee370987). For all four files `wc -c` equals `git cat-file -s` (Doc_01 54,509 bytes; Doc_02 53,956; Registry 88,817; Open_Gaps 38,032), and `git hash-object` equals `git rev-parse HEAD:<path>` (Doc_01 7732879681…, Doc_02 b2c59cc184…, Registry df0c35931e…, Open_Gaps 79b1758473…). None has uncommitted changes.
- **Date:** 2026-09-30
- **Documents:** `Build/worlds/hus/Doc_01_World_Identification_Boundaries_Orientation.md`, `Doc_02_Source_Ecology.md`, `Source_Registry.md`, `Open_Gaps_Tracking.md`, as committed at 7ee370987
- **Prior findings:** `Review-Artifacts/NewMaterial_Round1_Recheck.md` (Not clear, 0 P0, 1 P1, 7 P2). The drafter's account added to `Build/Ministry/Operations/Audits/hus_NewSources_2026-09-30.md` was treated as claims and checked at source.
- **Scope:** the diff of 7ee370987 against the Round 1 findings, plus anything the diff newly introduced. Low-to-medium effort.
- **Severity vocabulary:** P0 blocks, P1 must be fixed but is not disqualifying, P2 polish.

## Verdict

**Clear.** 0 P0, 0 P1, 3 P2.

The Round 1 P1 is fixed. Each live file now says what each chapter of Erben vol. 1 does, and the Article 4 result is stated at the right strength. All seven Round 1 P2s are fixed, and each fix was checked at source. Nothing new invents a source, a person or a detail, and no tag is set above its evidence.

The three new P2s are small precision points about the same three chapters. Two understate what the source shows and one gives a short line range. None changes a conclusion, a confidence tag or a boundary. On the bar of acceptable scholarly rigor, not perfection, Steps 1 and 2 of `hus` are clear on this cycle. A Round 3 is not needed. The P2s can be applied as wording fixes without a fresh review.

## Scope 1: the P1 on Hus's Czech creed

Checked line by line in `cic/texts/hus_sebrane-spisy-ceske-v01-ces_erben1865.txt`.

- **Chapter XXVII.** "Kapitola XXVII." is at 2248. The Nicene Creed runs from 2252 ("Věřím v jednoho boha otce všemohácieho, učinitele nebe") to "A mm." (Amen) at 2272, across a running head at 2268. "vtělil sé jest z ducha svatého, z Marie panny" is at 2258–2259, "a vstal z mrtvých třetí deá" at 2261 and "a opět přijde s oslavností" at 2262.
- **Chapter XXVIII.** The heading is misread at 2275. The incarnation is glossed at 2360–2362. Line 2362 names the crucifixion in garbled letters, and 2363 reads "a tak dále až do onoho slova: přijde s oslavností". The Spirit is glossed from 2369. So chapter XXVIII does not gloss the crucifixion, burial, rising, ascension or session. That is exactly what the drafter now says.
- **Chapter XXVI.** The heading is misread "Kapitola XX\1." at 2163. "Narodil sě z Marie panny" is at 2176, "Trpél pod I*ontským Pilátem" at 2179, "pohřeben byl" at 2185, "tíétí deň z mrtvých vstal" at 2190, "tělestně" at 2196, and the bodily return at 2201–2202. All as the drafter quotes them.

**Where the fix lands.** Registry row 60 (title, Licensed For and Verification Note), Doc_02 §8 (the row "Hus affirms the creed's substance"), Doc_01 §8 (the introduction, commitments 3 and 4, and the Result) and Open_Gaps entry 37 now give the three-chapter account. Entry 37 quotes the two sentences of entry 28 that it replaces, and both are verbatim in entry 28. Entry 28 itself is not edited, as the append-only rule requires.

**Strength of the conclusion.** Doc_01's Result now says that every clause is set out in the Nicene Creed (XXVII). It says the clauses from the crucifixion to the return are glossed on the Apostles' Creed (XXVI), not on the Nicene text. It concludes that the plain-sense test is met and the floor holds for Hus's own voice. That matches the source. The Confidence Map keeps "Documented" for "Hus affirms the creed's substance", which rests on the English works and on the creed set out and glossed in Czech. That tag is earned. The Czech-before-quotation caveat (page image) is kept everywhere. The optional Round 1 point was also taken: commitment 3 now cites "Narodil sě z Marie panny" (2176).

## Scope 2: the seven Round 1 P2s

| Round 1 finding | Now | Checked at source | Status |
|---|---|---|---|
| P2-1, stale gap statements | Entry 36 names each overtaken sentence: the Section B heading, R1, the Section E heading and lead paragraph, E1 and E2, entries 2 and 16, and entry 26's R2, R6 and R7 lines | Every quoted sentence is verbatim in Open_Gaps (lines 11, 33, 37, 63, 77, 79, 81, 82, 88, 91, 92). The replacements are true: rows 78 and 79 exist; the tract's title naming Hus is "in a later hand" (Thomson, lines 590–591); Březová and Brown are rows 68 and 70 | Fixed |
| P2-2, row 79 | The out-of-locus note is dropped; Licensed For is narrowed to the passages read; the Taborite confession is placed at 47613–47615 | "I have before me the confession of the Taborites, drawn up A. D. 1431, which in all respects agrees with our doctrine" at 47613–47615, inside the mapped locus 47370–47660 | Fixed |
| P2-3, row 67 | Letter A, licensed for the editor's statements only; Doc_01 §7 and Doc_02 §3 item 1 use Thomson's "a good deal" | "Thus we have no direct Ms. evidence for assigning the tract to Hus" at 591–592 (the sentence starts on 591; "later hand" at 590–591); "There is a good deal in this section taken from Wyclf's “De Potestate Pape"" at 741–742; "verbotenus e tractatu Wyclif De Potestate Pape (pp. 215—216) sumptum" at 11307 | Fixed |
| P2-4, line numbers | Row 55: 817, 820, 5439. Row 76: 21242, 21244, 21251–21252. Row 78: 34376 | "PARS PRIMA." 817; "EPISTOLAE M JOANNIS HUS," 820; "Amicis suis Constantiae." 5439; "964." 21242; "1436, Jul. 5 (Iglau)." 21244; "ipso die / post festum sancti Procopii" 21251–21252; "We, Nicholas, …" 34376 | Fixed |
| P2-5, Witness terms in rows 78–79 | Both open with a bold "Witness: first, for the legible English of a secondary compilation …; it is not an original-language witness" | Consistent with the header rule and with the rows' "S" role | Fixed |
| P2-6, row 58 and no. 95 | Row 58, Doc_02 §3 item 6 and the §8 row add that no manuscript survives and give Novotný's own reading | "Rukopis nezachován, zastupují ho Opera (Op)." 14654; "když Hus přijímání pod obojí byl již schválil" 14676; "datování před uvězněním pravděpodobnějším" 14682; "zdrželivě" 14683; "rozhodnějším" 14685. The rows report Novotný's view, and the Contested tag stands | Fixed |
| P2-7, change-relative wording | "now on the shelf", "no longer total", "now checkable", "newly vendored", "now vendored" and "now speaks" are gone | A search of Doc_01, Doc_02 and the Registry for "now", "no longer" and "newly" finds none of these phrases. The remaining "still" uses state present facts ("still refused" is a quotation; "still missing", "still wanted") | Fixed |

## Scope 3: what the diff newly introduced

- **Loci and quotations.** Every new line number and quoted string in the diff was matched in the vendored file, after whitespace normalisation only.
- **Tags.** No confidence tag changed except row 67's B to A. That A is limited to the editor's statements, which were read. It is not too strong.
- **Invention.** None. Novotný's reasoning is reported as his and the attribution of the tract stays the editor's argument.
- **Cross-world rows.** None added. Rows 78 and 79 remain the two corpus-map `context` assignments to this world.
- **Narration in live files.** None. The revision record went into the Audits file, not into the world files.
- **The "(Dated 2026-09-30.)" lead-ins** on five bullets of entry 36 and one of entry 37. `engine/m10/gaps.py` flags any line that cites "entry N" without a date on the same line, and these lead-ins satisfy it. Each bullet also names the superseded text by a verbatim quotation, which identifies it more precisely than a subject label. So the ledger's cross-reference rule is met in substance. The lead-ins read stiffly, and they are applied only where the tool needed them. This is acceptable in an append-only audit-trail file, and it is not a finding. A cleaner form in later entries is "entry 2 (the Taborite voice, 2026-09-30)", which carries subject and date together.

## Scope 4: tools

- `python -m engine.m10.cli gaps hus`: PASS.
- `python tools/check_live_commentary.py --surface worlds`, `hus` world files: Doc_01 and Doc_02 show one PROTECTED line each. Open_Gaps shows only PROTECTED lines (49). The Registry shows 54 REWRITE (iso-date) lines, 21 KEEP and 1 PROTECTED. The 54 are the Added and Discovery date cells that Framework V7.4 Step 2 requires, the same schema data cleared in the earlier rounds. No new REWRITE or ROUTE line appears.
- `--base origin/main --enforce`: exit 1 across the branch. Restricted to `Build/worlds/hus/`, the only REWRITE lines are those same 54 Registry schema cells. The new entries 36 and 37 classify as PROTECTED (entry-number, iso-date).

## Findings

**P2-1. Chapter XXVIII does gloss the return, and Doc_01 says it skips it.** Doc_01 §8, commitment 4, quotes "sedí na pravici otce, a opět přijde s oslavností" and then says "Chapter XXVIII skips these clauses". The Result says the clauses "from the crucifixion to the return" are glossed in XXVI "and chapter XXVIII passes over them". In fact XXVIII resumes at the return and glosses it. At 2363–2366 it says the faith says he will not come again to suffer, that he will judge the living and the dead and reign gloriously for ever, and that his kingdom will have no end. Registry row 60's "from the Holy Spirit onward" also omits this. Entry 37 is exact ("does not gloss the crucifixion, burial, rising, ascension or session"). The slip understates the evidence and changes no conclusion. Fix: say XXVIII passes over the crucifixion to the session and resumes with a gloss on the return (2363–2366).

**P2-2. Chapter XXVII's line range stops short.** Entry 37 gives chapter XXVII as lines 2248–2266. The creed continues across the running head at 2268 to "A mm." at 2272. The Spirit clauses are at 2263–2265 and 2270, and the Church, baptism and resurrection clauses are at 2270–2272. Fix: 2248–2272.

**P2-3. The rising on the third day is legible, and three places call it too garbled to quote.** Doc_01's Result, the Doc_02 §8 row and entry 37's last bullet say the rising "with the soul returned to the body" rests on a line too garbled to quote. Entry 37 and row 60 themselves quote "tíétí deň z mrtvých vstal" at 2190. Only the phrase that follows it, "duíii v t*lo navrátiv" (having returned the soul to the body), is garbled. Doc_01's commitment-4 bullet has it right ("garbled in the scan, and the sense is legible"). Fix: say the rising on the third day is legible at 2190, and only the words on the soul's return to the body are garbled. This is conservative as it stands, and no tag depends on it.

## Not re-verified

- Czech and Latin wording against page images. None was available, and every match here is to the OCR text.
- Registry rows and Doc_01 and Doc_02 text outside the lines changed by 7ee370987, including the other new rows cleared in Round 1.
- The Mehrning/Lydius attribution in row 79 beyond the quoted lines, and whether Mehrning's "confession of the Taborites" is a real Taborite document.
- Rights beyond the file headers.
- The audit file's account beyond the claims tied to the seven fixes and the P1.
- The Build State YAML.

## Disposition

Approved to proceed (Doc_02 and the Source Registry; not Frozen). Self-disposed by the Library thread after this recheck; the reviewer's verdict is above.
