# Library search log: era 8 (1650-1815), batch 2, 2026-11-15

The record for the second era 8 batch: the British Isles and the Methodists, North America, Catholic Europe and
the Jesuits, and the volumes batch 1 found and left. No new search was run. The candidates are the two unspent
tables of the era 8 handover (`../2026-11-15_library-era8/Handover.md`) and its list "Found by batch 1 and not
vendored". Thirty-seven files were vendored. Their states and shelves are in
`Build/Ministry/Features/Source-Library/CFT-Wants.md` ("Era 8 (1650-1815), batch 2").

## Scope

The coordinator set the scope on 15 November. The era 8 rows of the "Texts to fetch, by era" card list were not
taken: that list came from the legend check and was dropped for every era. Mark's direction of 2026-11-15, as
the coordinator passed it on: "we dont need to build out more legends we need to make sure the who and counsils
are drawing from their own sources not sources writen 1000 years later". No quote, story or lexicon entry was
rendered.

## The check before the fetch

Run on 15 November for all 41 candidates, against `cic/texts/REGISTRY.yaml`,
`Build/worlds/_cross-world/download-queue-seed.yaml`, `Build/worlds/_cross-world/WANTS-REGISTER.md` and
`Build/worlds/_cross-world/CORPUS-USE.md`, by archive.org identifier and by author and title in `cic/texts/`.

- Held already, dropped: Richardson, Memoirs of Alexander Campbell, vol. 1 (`memoirsalexande00unkngoog`; held as
  `richardson_memoirs-of-alexander-campbell-v1_1868.txt`).
- A later printing of a held text, left out by the coordinator's instruction: Gobat's Journal, New York 1850
  (`journalthreeyea01bairgoog`; the London print of 1834 is held).
- Held in another volume, so the candidate is a new volume: Davies's Sermons (vol. 3 of another edition held;
  vol. 1 taken); Launay (tomes 1 and 2 held; tome 3 taken); Pascoe (vol. 1 held; vol. 2 taken); the Historia
  cultus Sinensium (the main volume held; the Continuatio taken); Valentijn (deel 3 held; deel 2, see below);
  the Code noir (the collection of 1767 held; the collection of 1743, see below).
- No other candidate's identifier, author or title was in the four files.

The check was run again against `origin/main` just before intake, after main was merged into the branch: no
pick's identifier was in main's registry or seed file, and no pick's author and title was in `cic/texts/`.

## Rights rule used

A printed imprint of 1930 or earlier, read on the title page in the OCR or on the scan's page image; a reprint
counts by its own date. No file carries a permission notice or a non-commercial license other than Google's
standard sheet. Nothing was taken under the rule for American books of 1931-1963.

One file rests on ruling R12 (a title page with no year): **Love, Samson Occom and the Christian Indians of New
England.** The title page (page image, leaf n8) prints "Boston, The Pilgrim Press, Chicago" and no year. Its
verso (leaf n9; host lines 70-71) prints "Copyright, 1899, by W. DeLoss Love". The preface is dated October
1899 and the archive.org record's date is c1899. The header's rights line says so.

Taft's two volumes are a reader's upload of 2025 with no library catalog record. The scan photographs a bound
old copy with a Thursfield Smith Collection plate; vol. I's title page prints 1825 (page image, leaf n6) and
vol. II's prints 1828 (host line 19114). The printed years are the basis.

## How each file was checked

The 39 candidates that stayed in after the check were fetched again by identifier on 15 November
(`fetch.py`; the list is `candidate_ids.txt` less the two dropped). Every download's byte count equals the size
archive.org lists for the djvu.txt, and equals the count in `fetch_manifest.json` from the first fetch.

Five Sonnet mappers had mapped the contents under the era 8 `MAPPER_BRIEF.md` (`mapper-reports/`). The Library
thread then read the title pages. Where the OCR garbles the year or the volume, it read the page image:

| file | leaf | what the page image prints | what the OCR reads |
|---|---|---|---|
| Davies, Sermons, vol. I | n6 | "M.DCC.XCIV." | "M.DCC.xeiv-" |
| Marsollier, tome 1 | n6 | "M. DCC. LVIII" | "M. Dec LVIIL" |
| Marsollier, tome 2 | n6 | "M. DCC. LVIII" | "M, Dec. LVIIL" |
| Du Fossé | n6 | "A Utrecht ... M DCC XXXIX" | "M Dec XXXIX" |
| Fontaine, tome 2 | n10 | "A Cologne ... MDCC XXXVIII" | "MDCG XXXVUl." |
| A Relation of the Missions of Paraguay | n0 | "London: Printed for J. Marmaduke in Long-Acre. M.DCC.LIX." | "M. Dec. LIX." |
| Soli Muratori, Vita | n4 | the full title, "In Napoli MDCCLVIII, presso Giuseppe Ponzelli" | the first title lines are missing |
| Continuatio Historiae cultus Sinensium | n4 | "Coloniae, M. DCC." | "M. D C C." |
| Quesnel, tome 1 | n4 | "A Paris, chez André Pralard ... M. DC. XCIII." | "M. D C. X C 1 1 1." |
| Wilberforce, vol. I | n11 | "Vol. I." and "MDCCCXXXVIII" | "VOL. L" |
| Vieira, Parte duodécima | n8 | "Anno de 1699" | "i6$9-" |
| Dobrizhoffer, Historia, pars I | n6 | "Viennae ... Anno 1784." | "ANNO i784^" |
| Love, Samson Occom | n8, n9 | no year on the title page; "Copyright, 1899" on its verso | the same |
| Taft, vol. I | n6 | "1825." | the same |
| Parry | n9 | "1895." | "1896." |
| Campbell, Declaration and Address | n2, n3 | no year on the title page; "1908" with the printer's name on the next leaf | "1906" |
| Code noir (not taken) | n4 | "A Paris, chez les Libraires associez. M. DCC. XLIII." | "M. DGC. XL III." |

The spec that wrote the headers (`mkspec2.py`) checks about 140 line anchors against the host text before it writes
anything: each cited title-page year, heading and wanted passage must stand at the cited line. Six anchors
first failed on OCR garbles of the right word and were confirmed by reading the lines.

## Corrections to the earlier notes

- **Parry is 1895, not 1896.** The mapper and the batch handover took the OCR's "1896." for the title page. The
  page image prints 1895, which is also the host's date. The file is named for 1895 and its header says what
  the OCR reads.
- **Campbell's Declaration and Address is 1908, not 1906.** The title page (leaf n2) prints no year. The leaf
  after it (n3) prints "1908, Record Publishing Company, Coraopolis Pa."; the OCR misreads the year as "1906",
  and the mapper, the batch handover and this thread's first header all followed the OCR. The round 1 review
  caught it on the page image. The host's date of 1908 was right. The reprinted title page of 1809 is garbled
  in the OCR ("I8OQ.").
- Wilberforce: the title page prints "Vol. I."; the identifier's "04" is not the volume.
- Hannah More, vol. I: third edition, MDCCCXXXV, not the host's 1834.
- Raikes: the matter at host lines 2273-2374 is newspaper extracts of 1784, not a letter. His letters are to
  Colonel Townley (25 November 1783) and to the Arminian Magazine (5 June 1785).
- Fontaine: Cologne, 1738, on both title pages; the host says Utrecht, 1739.
- A "Digitized by" line that a one-space search misses stands in Orton, Cooley and the Campbell reprint; each
  header names it. Every file was searched again with any run of spaces between the words.

## The review

One independent review by Opus (`R1_review.md`): 25 findings in 20 files, one blocking (Campbell's year), seven
substantial, seventeen minor, none on rights. All 25 were corrected in the spec and the 37 files were vendored
again from it (`R1_changes.md`). A targeted recheck followed (`R2_recheck.md`).

## Three judgement calls

1. **Valentijn, Oud en Nieuw Oost-Indiën, deel 2 (`oudennieuwoostin02vale`): not taken.** The volume is the
   description of Amboina and the "Ambonsche Zaken", about 600,000 words of Dutch. The mapper found no section
   headed for church affairs, only scattered mentions and lists of ministers. Deel 3, which is held, has the
   book on Amboina's church. The rights are clear (Dordrecht and Amsterdam, MDCCXXIV; byte count equal), so it
   can be taken later if a writer needs the civil history.
2. **Code noir, the collection of 1743 (`codenoirourecuei00fran`): not taken.** Its table of contents was read
   against the held collection of 1767. The acts that touch the church are in the held file: the edict of March
   1685, the edict of March 1724 for Louisiana, the ordinance of 15 June 1736 on manumission and baptism, and
   the declaration of 15 December 1738. What the 1743 collection adds is customs and trade acts of 1716 to 1742
   and an "acte de notoriété" of 1705 on slaves as movable goods. Rights clear; byte count equal.
3. **Taft, Holy Women: taken.** See "Rights rule used" above.

## Hosts

| host | state from this sandbox | used |
|---|---|---|
| archive.org (metadata, djvu.txt, page images) | reachable | all 37 files |

No other host was tried, and none was refused by the network proxy.

## Not taken, with the reason

| item | identifier | reason |
|---|---|---|
| Richardson, Memoirs of Alexander Campbell, vol. 1 | `memoirsalexande00unkngoog` | held already |
| Gobat, Journal, New York 1850 | `journalthreeyea01bairgoog` | a later printing of a held text |
| Valentijn, deel 2 | `oudennieuwoostin02vale` | call 1 above |
| Code noir, 1743 | `codenoirourecuei00fran` | call 2 above |

Located by the first era 8 session and still not taken, because the wanted row was met by one volume: Roberts's
Hannah More, vol. 2 (`memoirsoflifecor02robe`, Harper, 1834); the Wilberforce Life, later volumes
(`lifewilliamwilb02wilbgoog`, `lifewilliamwilb12wilbgoog`, `lifeofwilliamwil04wilbuoft`; vol. 5 only as a
lending copy); Bouquet's edition of du Fossé (1876-79); Gonod's Lettres de Rancé (`lettresrecueill00rancgoog`,
year garbled in the OCR, page image not read); Vieira's other Sermoens volumes; Dobrizhoffer's Latin, parts 2
and 3 (not located); Quesnel's later tomes (not located).

Not found by the first era 8 session, and not searched again here: Hindmarsh, Rise and Progress (1861); Ann
Griffiths in Welsh; Kirk's Biographies (1909); Davenport's Confession and Retractions; Herman of Alaska; the
whole of Occom's narrative of 1768 and of Nathan Cole's "Spiritual Travels" in a print of 1930 or earlier; the
Methodist gaps (Wesley's Letters, his Sermons after vol. 1, Charles Wesley's Journal vol. 2, Whitefield's later
Journals, Fletcher's Checks, the Arminian Magazine).

## Cautions for profile writers

- **Extracts, not wholes.** Occom's narrative of 1768 is held only in the short opening Love prints (about twelve printed lines). Nathan
  Cole is held only in the extract Walker prints. Raikes's letters are held only as Gregory prints them.
- **Lives with letters inside.** Roberts on Hannah More, the Wilberforce sons, Taft, Cooley on Haynes, Orton on
  Doddridge and Gibbons on Watts all quote their subject's letters and journals inside a later writer's frame.
  Name the letter-writer when quoting, and say whose book prints it.
- **Translations of translations.** The English Relation of the Missions of Paraguay (1759) follows a French
  version whose translator says he cut and reordered Muratori. The English Dobrizhoffer (1822) leaves passages
  out, by its own preface. Quote from the Italian and the Latin.
- **Attributions that are not on the title page.** Dutton ("By A. D."), Judith Sargent Murray ("By Constantia"),
  Quesnel (no name), the Life of Bray (unsigned; Todd reports it as Samuel Smith's), the Continuatio (no name;
  the pieces are headed as Charmot's). Each header says where the name comes from.
- **Reprints.** Campbell's Declaration and Address is read in the reprint of 1908, which claims to follow the
  1809 print letter for letter; the claim was not tested. Orton is read in the Edinburgh reprint of 1825.
  Marsollier is the "nouvelle édition" of 1758.
- **Poor OCR.** The Gleaner, vol. 2; Vieira's three volumes (two columns run together); the title pages and
  headings of the two eighteenth-century London prints (Dutton; the Relation). Check any quotation on the page
  image.
- **A scan that stops short.** The Wilberforce Life, vol. I, ends inside its appendix; the scan has no end page.
- **A shelf outside its window.** Parry sits on `the-sayfo-and-the-syriac-diaspora`, the nearest entry; the
  census has no entry for the Syriac Orthodox between 1650 and 1906. Haynes sits on the New England awakening
  entry because the census names him there, though his ministry is later.
