# R2 recheck: Library era 8 batch 1 (31 files), 2026-11-15

**Verdict: CLEARED.** Both blocking findings and every should-fix finding are resolved in the records as they stand. One note-grade finding (18) is only partly fixed: a sentence round 1 found wrong still stands in a live header and in the registry. It is a one-line mechanical fix and does not need another round.

Line numbers are file lines unless marked OCR. Page images and the atlas entries' window years could not be checked (the corpus-map files do not carry them).

## Round-1 findings

1. **RESOLVED.** Vansleb Histoire header line 9 and REGISTRY 24346 now read "drawn, its heading says, from Arabic authors (the first name is garbled there; 'Abulbaracat' is named often elsewhere in the book)". The heading at 14116-14119 reads "tiré de l'e^-hMaracat & de plusieurs autres Autheurs Arabes". "Abulbaracat" and near spellings stand on about fourteen body lines (1290, 3735, 12931, 12961, 15365, 15843 and others). "Macrizi" only at 14903 and 14915. Al-Maqrizi is not named in the header, registry, seed or staging note.
2. **RESOLVED.** Divers voyages header line 2 credits the archive.org record, says the title page names no author, and cites "Pere Alexandre" at OCR 6289; file 6301 reads "Pere Alexandre! ne craignez rien". Staging has `authors_ruled: rhodes` (file lines 44-70, 6301), and the merged copy agrees (UNATTRIBUTED.yaml 3166-3171).
3. **RESOLVED.** Al-Jabarti header lines 1-2, REGISTRY 24358 and seed 27107 read "Abdulaziz Kahil Bey" and "Gabriel Nicolas Kahil Bey". File 58 reads "ABDULAZIZ KAHIL BEY - GABRIEL NICOLAS KAIIIL BEï". No "Khalil" is left in the registry, seed or corpus-map.
4. **RESOLVED.** Pallu header line 3: "(title page, read on the page image, leaf n2; the OCR drops these lines)".
5. **RESOLVED**, all four points.
   - Date: header line 4 cites both title pages, the second at OCR 15962 and 15971. File 15974 reads "O O L O N I M" and file 15983 reads "M. D C C."
   - Label: header line 9 and REGISTRY 24426 now call the first piece Charmot's notes, with title, preface and five sections.
   - Staging row 2: `author: charmot`, locus "the Notae at OCR 126-7940; the Notationes at 8194-13133". The brief of Innocent XII (file 7943 on) and the Jesuit pieces are outside it. File 13146 opens the next piece ("Dispunctio"), so 13133 is the right end.
   - Evidence and date source: Charmot's evidence cites 138-169 and 158; file 158 reads "NICOLAO CHARMOT" and 169 "Oblata die 29. mensis Iulii 1698". The Mandate's year now rests on "decima Novembris 16931" (file 18829), not on Launay. Maigrot's evidence lines 15645-15657 and 15932 hold.
6. **RESOLVED.** CFT-Wants 733-734: "The missions all three describe come before the entry's window, which opens in 1650; the prints are of 1651, 1652 and 1682." The three staging notes agree (Divers voyages line 13, Tunchinensis line 13, Cathechismus line 13: "Printed in 1651, as this entry's window opens"). See new note C.
7. **RESOLVED.** McCarter staging line 13 quotes "several years' pastoral labour among the South African Dutch colonists" (OCR 75-77); file 87-89 reads exactly that. The row is `tradition`, `provisional`. CFT-Wants 700-701 carries the same quotation.
8. **RESOLVED.** Ceylon Sketch staging lines 9-10: `context`, `needs-ruling`. The merged row (catholics-of-dutch-ceylon.yaml 42) and CFT-Wants 683 agree. McCarter stays `tradition` with a stated reason.
9. **RESOLVED.** No `parry*` file in `cic/texts/` or `_staging/`. Grep "parry" finds nothing in REGISTRY.yaml or anywhere under `cic/corpus-map/`. The only seed hit is Henry Parry Liddon (27939), which is unrelated. CFT-Wants 663 and Search_Log 84-90 say the scan was not taken and quote the Columbia permission line as the reason.
10. **RESOLVED.** Divers voyages header line 9 has no tracking sentence. Grep for "first printing of 1653" finds nothing in the registry or seed.
11. **NOT CHANGED; the reason given is half right.** `cic/texts/INTAKE.md` writes "licence" throughout (lines 75, 82, 91) and uses `open-licence` as a registry term (lines 76, 133), so the Library's own usage supports keeping it. CLAUDE.md does not support it: its one use is "license" (line 86). Acceptable to leave; see new note B.
12. **RESOLVED.** Vansleb Histoire header line 4 and Search_Log 54 both give "the OCR reads 'M. pC. LXXVII.'"; file 63 reads that.
13. **RESOLVED.** Proyart header line 9: "approbation (the OCR reads 26 May 1770)". Both staging rows date from the title page alone. The page image is still unchecked, as R1_changes says.
14. **RESOLVED.** Launay t1 header line 9: "the first copy's OCR reads the year as 1679". CFT-Wants 723 agrees.
15. **RESOLVED.** Tunchinensis header line 9 and staging line 12: "the Society's permission to print (Avignon, 1 May 1651)".
16. **RESOLVED.** Cathechismus header line 9: title page at OCR 5-28, Vietnamese title at 20-21. The title page stands at file 17-40 and the Vietnamese at 32-33.
17. **RESOLVED.** Pascoe staging line 24 and CFT-Wants 697: "assistant secretary".
18. **PARTLY.** CFT-Wants 707-708 now reads "other men and a book title". The al-Jabarti header (line 9, last sentence) and REGISTRY 24358 still read "Other 'El Djohari' passages concern a Muslim sheikh". The file has at least two men (1139 "Mohammed ibn El Djohari", 6716 "Ahmed el Djohari") and a book title (4157 "Sohah el Djohari").
19. **RESOLVED.** Nouvelle relation staging line 13: "which opens in May 1671". The header title keeps "en 1672 et 1673" on the page image's authority, which I could not check.
20. **RESOLVED.** Gobat staging line 23: "title page: 1834, read on the page image, leaf n9".
21. **RESOLVED.** Antonil staging line 12: "OCR lines 351-410".

## Agreement checks

- REGISTRY (24346, 24358, 24414, 24426) and the seed (27086, 27107-27116, 27256, 27277-27286) repeat the corrected headers word for word for the Vansleb Histoire, the Divers voyages, al-Jabarti and the Historia. That includes the leftover al-Jabarti sentence.
- The merged corpus-map rows carry the corrected staging text (chinese-catholicism-1650-1906.yaml 6-23 and 92-104; vietnamese-catholicism-to-1815.yaml 85 and 102; the-dutch-reformed-church-at-the-cape.yaml 20; catholics-of-dutch-ceylon.yaml 42).
- CFT-Wants 637 says "Thirty-one files"; the table lists thirty-one. Its shelves agree with staging on the changed rows: McCarter tradition (651), Historia with Charmot needs-ruling (675), Ceylon context needs-ruling (683), Proyart part 1 needs-ruling (648). Search_Log 44 says "all 31 files".

## New problems from the fixes

- **A. SHOULD FIX.** The leftover of finding 18: the al-Jabarti header line 9 and REGISTRY 24358 now contradict the batch's own corrected caution. Correct the sentence in the spec ("concern other men and a book title") and regenerate.
- **B. NOTE.** R1_changes row 11 cites CLAUDE.md for "licence". CLAUDE.md has only "license" (line 86). Drop CLAUDE.md from that row; INTAKE.md and the `open-licence` term carry the reason on their own.
- **C. NOTE.** CFT-Wants 679 still shelves the Divers voyages as "needs-ruling: before the window" with no qualifier, beside a print year of 1682. The caution at 733-734 makes the meaning clear, but the table cell repeats the wording finding 6 objected to. "The missions come before the window" would match.
- **D. NOTE.** The Historia header line 4 says the second title page "gives 'COLONIAE'" at OCR 15962. The OCR there reads "O O L O N I M" (file 15974). That is the print's word, not the OCR's; the year at 15971 is exact.

Not checked: page images (leaves n2, n6, n8, n9), the window years 1650, 1652-1906 and 1806, and `tools/check_spelling.py`.
