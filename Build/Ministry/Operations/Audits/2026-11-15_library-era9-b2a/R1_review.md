# R1 review: Library batch, era 9 (1815-1906), batch 2a

**Verdict: clears with fixes.** No rights failure and no wrong role were found. Four headers state a fact the file does not bear out (B1-B4). All four are corrections to wording or line numbers; none changes whether a file may be held.

## Blocking findings

In B1-B3 the Publication Date line names a line that is not the imprint. The imprint year does stand on the title page, at a different line. The same wrong line is carried into the shelf row's `date.source` and `edition_date.source`.

**B1. `assam-mission_papers-and-discussions-of-the-jubilee-conference-1886_1887.txt`, header line 4** (and its staging row, lines 17 and 21).
- The header says "1887 (line 27 of this file, on the title page)".
- Line 27 reads `A8  A53  1887`. It is the second line of a library call-number slip (line 25: `BV  3280  .`), not the title page.
- The title page runs from line 150 to line 176, and the imprint `1887.` is at line 176, under "CALCUTTA : PRINTED BY J. W. THOMAS, BAPTIST MISSION PRESS" (lines 173-175).

**B2. `darby_seven-lectures-on-the-second-coming-of-the-lord_toronto1863.txt`, header line 4** (and staging lines 15 and 19).
- The header says "1863 (line 31 of this file, on the title page)".
- Line 31 reads `DELIVERED IN TORONTO, IN 1863,`. That is the year the lectures were given.
- The imprint `1863.` is at line 44, under "TORONTO : GOSPEL TRACT DEPOSITORY" (lines 39-41).

**B3. `valaam_ocherk-iz-istorii-amerikanskoi-pravoslavnoi-missii-rus_1894.txt`, header line 4** (and the staging row's two source lines).
- The header says "1894 (line 19 of this file, on the title page)".
- Line 19 reads `(1794—1894)`, the centenary span in the heading.
- The imprint `1894.` is at line 58, under the St. Petersburg printer's line.
- The Content note gives the title page as lines 14-56; it runs to line 58.

**B4. `macedo-soares_a-guerra-de-canudos-por_1902.txt`, header lines 4 and 9** (and staging lines 15 and 20).
- Line 4 says leaf n6 prints "1a edicao" and "Rio, Typ. Altina, 1902", and that "an earlier leaf, the cover, reads 1903 in the OCR".
- Line 9 says the "title page" is at lines 24-46.
- The OCR holds one imprint leaf only, at lines 24-46. It carries the author, the edition statement (`K DIÇÃO`), `RIO`, `Typ. Altiiia, Assenibléa 96` and `1903` at line 46.
- So the leaf the Content note calls the title page is the leaf the Publication Date line calls the cover, and it carries the words line 4 assigns to the 1902 leaf. No second imprint is in the OCR; the next leaf has only `MACEDO SOARES`.
- One of the two header statements is wrong. Either year passes the rights rule. The filename, the wants row, the caution at CFT-Wants line 1007 and Search_Log lines 51-52 all follow the header.
- Fix: look at the page images again, state which leaf is which, and make lines 4 and 9 agree.

## Non-blocking findings

**N1. CFT-Wants.md line 978 says Klein "does not name Joseph Mukasa". The file names him.**
- `klein_le-cardinal-lavigerie-et-ses-oeuvres-d-afrique-fra_1897.txt` prints "Joseph Mkasa" at lines 6973-6974, 6986 and 7022.
- It tells of his pleading for Hannington, his sentence, his beheading and his last words to Mouanga at lines 7022-7045.
- The shelf locus (7154-7220) and the Content note cover only Charles Louanga. The passage serves row 318 as well as row 210.

**N2. Scanner page marks remain where the batch says they were removed.** CFT-Wants line 854 says "Google's preamble and the scanner's page marks were removed, and each header says what was removed."
- `jessup_fifty-three-years-in-syria-v1_1910.txt`: the Provenance note says 8 page-mark lines were removed. 476 lines beginning `Digitized by` remain, each followed by `Googk`. In the first 150 lines they are at 13, 56, 64, 72, 90, 99 and 137.
- `ioann-kronshtadtskii_my-life-in-christ_goulaeff1897.txt`: the note says 434 page-mark lines were removed. 138 `Digitized by` lines remain, for example lines 26 and 29 (`Google`), 188 and 568-571.
- `reyes_la-sensacional-memoria-spa_1899.txt`: the note names only the preamble. 238 lines still carry the mark, for example `,Google` at lines 24, 28, 32, 36 and 40 and `Hoaedb,GoOgle` at line 81.
- The removal seems to have caught only marks that sit whole on one line. Either remove the two-line form as well, or make the three Provenance notes and line 854 say what is left.
- The other nine Google scans are clean. Line numbers in these three headers will move if lines are removed.

**N3. `iglesia-filipina-independiente_documentos-interesantes-spa_1906.txt`.**
- Line 213, the date of the compiler's own address, reads `Manila, I F., 1 ro de Enero de 1936.` It is plainly a misreading of 1906: every document in the file is dated 1902-1905, and the index at lines 1865-1888 ends at 30 October 1905. The header should name it, since it is a date after 1930 in the front matter.
- Header line 4 says "the title page prints no year". The OCR holds no title page at all (lines 13-48 are noise), and CFT-Wants line 990 says the title page cannot be read. The same wording stands in `aglipay_catequesis-de-la-iglesia-filipina-independiente-spa_1912.txt` line 4, where the title leaf (lines 13-37) is garbled and shows no imprint. Both should say "cannot be read in the OCR", as the Macedo Costa header does.
- In both files the Title and Publisher come from the catalogue, and the header does not say so. In the Documentos file the Creator comes from the signature at lines 210-211, which the OCR reads `Alejandro Bemollino`.

**N4. `macedo-costa_a-questao-religiosa-do-brazil-perante-a-santa-se-por_1886.txt`, header lines 4-5.**
- "One prefixed letter is dated January 1887": there are two, at lines 410 and 612.
- The note at line 114 says the letters arrived after the reprint was finished. So the front matter was printed in 1887, against the catalogue's 1886; the preface-and-catalogue test is met only loosely. Rights are not affected. CFT-Wants line 1006 and Search_Log line 64 repeat "one".
- Line 12619 reads "1 de Julho de 1899" for a letter of Leo XIII. This is very likely a misreading (the prefatory letters of 1886-87 address the author as living), but the header could say so.

**N5. `darby_dialogues-on-the-essays-and-reviews_2nd-ed1863.txt`.**
- The bound-with tract "Dr. Colenso and the Pentateuch" has its own title page at lines 21190-21206 (London, W. H. Broom). It shows no year in the OCR.
- The header's 1863 rests on the first work alone and does not say this.
- The shelf row maps "the whole volume" under author darby, though the file names no author for either work.

**N6. `guebre-sellassie_chronique-du-regne-de-menelik-ii-t1-fra_coppet1930.txt`.**
- The title page prints 1930 at lines 113 and 193, so the rule is met at its last eligible year.
- The volume's own genealogical table (lines 62308-62316) speaks of the coronation "en novembre de la même année" in the past tense.
- The printer's line at 62977 carries no date. Nothing in the file prints 1931 or later, and the cut before tome II is clean.

**N7. `adriaanse_sadrachs-kring-nld_1899.txt`.**
- Line 51 (`DONNER. - 1899.`) is a fragment of a split leaf. The whole title page is at lines 65-80, with the imprint at line 80.
- The Content note's ranges (68-76 and 86-99) leave the imprint line out.

**N8. `sheptytsky_kanadiiskym-rusynam-ukr_1911.txt`, header line 7.**
- The source item is `herbarzpolskipow01niesuoft_202605`, an identifier that names a different book.
- The file's own title page (lines 13-24) and colophon (lines 3863-3864) are Sheptytsky's. The Search Log does not mention the mismatch; one sentence there would save the next reader a check.

## What was checked

**Part A, all 74 files.**
- Header lines 1-5 were read for every file, and the title-page region or the cited line was read in the OCR for every file.
- Of the 54 title-page line cites, 51 show the imprint at the line named; three do not (B1-B3).
- All six copyright-notice cites are right: Hardy 69, Uchimura 117, Jessup v1 146 and v2 71, Aggressive Christianity 51, Godliness 103.
- The dated-preface cites are right: Stern 464, Documentos 183, Aglipay 1342, Macedo Costa 171.
- For the ten years read on page images, nothing in the OCR contradicts the year except Macedo Soares (B4). The files are Pharmakidis, Lindley, Davis, Evans, Reyes, Codigo, Vital, Macedo Soares and the two Darby books.
- Every file was searched whole for years from 1931 on. All hits are library or treatment stamps, host scan notices, numbers, or OCR misreadings of nineteenth-century dates (for example Optina lines 5680-10320, and Jessup v2 line 46, a stamp of 1951). The one worth naming is in N3.
- No reprint notice, later copyright, non-commercial notice or permission notice was found in any file.
- No duplicate of a held work was found in REGISTRY.yaml.

**Part B, 41 files in depth** (header, Content note, shelf row, and the lines they cite).
- All 28 files not in English.
- The seven English files with no title-page year: Hardy, Uchimura, Jessup v1 and v2, both Catherine Booth books, Stern. For Hardy, Uchimura and the two Booth books the title page, the notice and the header were checked, not the body cites.
- Six more English files: Bleby, the Demerara court-martial report, Milne, Joel Bulu, Mackay, Wylie.
- Every body line cite opened was right, apart from the findings above.

**Part C.**
- The batch 2a section of CFT-Wants.md (lines 845-1012) and Search_Log.md were read whole.
- Language counts, edition statements, name spellings and the "does not name" claims were checked by search. The claims for Churchill, Lynch, Pharmakidis, the African Methodist Episcopal encyclopaedia, Louvet, Launay, Shortland and Garcia Moreno hold.
- Contradicted: line 978 (N1), line 854 (N2), line 1006 (N4) and line 1007 (B4).

**Part D.**
- Sixteen staging rows of the earlier batch were opened: Finney, Briggs's Defence, Briggs-trial parts 1 and 3, the Presbyterian Review, Noyes, McAuley, Offord, Disselhoff, Phillips, both Bavinck files, both Taylor-Howard files and Page.
- They were judged against the census windows in ATLAS-TARGETS.md. Each role fits rule 4.

**Rule 4 for this batch.** The roles of all 74 rows were read against what each file is. None was found wrong.

**Commands.** None was refused. Beyond the forms named in the brief, `grep` was used with `-c`, `-m`, `-i` and `-E`, and `sed -n` with several ranges and `=` to print line numbers; all were read-only. One long search for rights notices ran past the time limit and finished in the background with no matches.
