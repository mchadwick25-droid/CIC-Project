# R1 changes: Library era 8 batch 1, 2026-11-15

What the Library thread did with each finding of `R1_review.md`. The fixes were made in the spec (`mkspec1.py`)
and the whole intake was run again from it, so the headers, the registry, the seed and the staging rows all come
from the corrected text. No file's body was touched: each is still the host's djvu.txt, byte for byte, after a
12-line header. The batch is now 31 files.

| finding | grade | what was done |
|---|---|---|
| 1. Vansleb, Histoire: the catalog's source named as al-Maqrizi | blocking | Fixed. The header now says the catalog is drawn, by its heading, from Arabic authors, that the first name is garbled there, and that "Abulbaracat" is named often elsewhere in the book. Al-Maqrizi is no longer named. |
| 2. Rhodes, Divers voyages: the author credited to the title page | blocking | Fixed. The Library thread read the title page on the page image (leaf n6): it names no author. The Creator line now says the attribution is the archive.org record's, that the title page says only "le retour de l'Autheur", and that the narrator is addressed as "Pere Alexandre" at host line 6289. The staging file carries an author ruling with that evidence, and the row's note says the title page names no author. The row was already needs-ruling. |
| 3. Al-Jabarti: translators' names | should fix | Fixed from the page image (leaf n8): "Abdulaziz Kahil Bey" and "Gabriel Nicolas Kahil Bey". |
| 4. Pallu: publisher line not in the OCR | should fix | Fixed. The header says the publisher's lines were read on the page image, leaf n2. |
| 5. Historia cultus Sinensium, four points | should fix | Fixed. The date line cites both title pages (the second at host lines 15962 and 15971). The long first piece is now described as Charmot's notes, with its title, preface and five sections. The second staging row covers only Charmot's Notae and Notationes and no longer the Jesuit pieces or the Jesuit shelf. The Charmot evidence cites file lines 138-169, his name at 158. The Mandate's year no longer rests on Launay. |
| 6. Rhodes: "before the window" | should fix | Fixed. The window opens in 1650. The notes and the caution now say that the missions described come before it and that the prints are of 1651, 1652 and 1682. |
| 7. McCarter: the preface answers what "was not read" | should fix | Fixed. The note quotes the preface ("several years' pastoral labour among the South African Dutch colonists", host lines 75-77). The row is tradition, provisional: the book of 1869 falls inside the entry's window of 1652-1906. |
| 8. Roles of the Ceylon Sketch and McCarter | should fix | The Sketch (1848) is now context, needs-ruling: it was written after the entry's window closed in 1806, as Launay and Pascoe were after theirs. McCarter stays tradition, for the reason in row 7. |
| 9. Parry: a permission line on the microfilm target | should fix | The reviewer is right: host lines 16-18 read "Reproductions may not be made without permission from Columbia University Library". The rule for this work is that a scan with a permission notice is not taken. Parry was taken out of the batch (file, staging row, registry and seed entries). A Google scan of the same edition is left for the next batch. Logged in the Search_Log and CFT-Wants. |
| 10. Divers voyages header: a tracking reference | should fix | Fixed. The sentence is gone. |
| 11. "licence" | should fix | Not changed. The Library writes "licence" for the noun (`cic/texts/INTAKE.md`, the registry's own `open-licence` term), and `tools/check_spelling.py --enforce` passes on this branch. |
| 12. Vansleb, Histoire: "the OCR does not give the numeral" | note | Fixed in the header and the Search_Log: the OCR reads "M. pC. LXXVII." |
| 13. Proyart: the approbation of 1770 | note | The header now says "the OCR reads 26 May 1770", and the row's date rests on the title page alone. The page image was not checked. |
| 14. Launay: the synod's year in the first copy | note | Fixed: the header says the first copy's OCR reads 1679. |
| 15. Rhodes, Tunchinensis: "privilege" | note | Fixed: "the Society's permission to print (Avignon, 1 May 1651)". |
| 16. Cathechismus: title-page lines | note | Fixed: host lines 5-28, the Vietnamese title at 20-21. |
| 17. Pascoe: "secretary" | note | Fixed: "assistant secretary" in the note and the caution. |
| 18. Al-Jabarti caution | note | Fixed: "other men and a book title". |
| 19. Vansleb, Nouvelle relation: "journal of 1672-1673" | note | The note now says the journal opens in May 1671. The header title keeps "en 1672 et 1673": the Library thread saw those words on the page image of the title page (leaf n6), and the mapper read them in the OCR. |
| 20. Lee row: the year's source | note | Fixed: "read on the page image, leaf n9". |
| 21. Antonil: the licences' lines | note | Fixed: host lines 351-410. |

Also changed, not from a finding: the CFT-Wants table marks Proyart's first part as needs-ruling; a row and a log
entry record the second look at Bacha's Abu Qurrah (an era 4 item), whose rights now clear and whose one scan is
cropped.

After round 2 and the merge of main: Butcher's vol. 2 was dropped from this batch, because the era 9 Library batch had vendored the same scan under the same filename and it reached main first. The batch is 30 files; the era 8 shelf row for Butcher was added to the staging file already on main.
