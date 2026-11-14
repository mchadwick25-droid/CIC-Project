# R2 changes: era 3 batch 6, part B

What was done for each R2 finding, and where. I opened every cited line in its vendored file before making the change. No brief changed, so the audio scripts stand as they were. `records.json` was re-loaded just before each write, and only the `babai-the-great` entry was changed. In `era3/batch5/records.json`, only the words "held whole" in the `henana-of-adiabene` note "A second witness to Babai's doctrinal charges" changed. The diff is one line, with indent=1, ensure_ascii=False and no trailing newline kept. No `date` key was added or removed.

Files are under `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/`. Line numbers point to files under `cic/texts/`.

| Finding | Done |
|---|---|
| R2-B-B1 (Braun's Life of George called "whole") | Braun's own notes confirmed: "Von der sehr langen Einteilung gebe ich nur die wichtigsten Gedanken" (braun1915 l.12442-12443), "Das folgende, sachlich belanglose Enkomion auf die Heilige übergehe ich" (l.13161-13162), "Ein langes Enlromion ... übergehe ich" (l.13319-13322) and "Die folgenden, sachlich inhaltslosen Ausführungen übergehe ich" (l.13806-13807). All four fixes applied as worded: the Babai card's `keyWorks` 2 `about`, the records claim opening, the records `absent_details` "A Syriac or English text of his own books", and the batch 5 Henana note. |
| R2-B-M1 (Guidi: quarrel between the two men; line ranges) | Confirmed: "excitavit inter duas illas firmissimas religionis turres, duo Babhay, nec conquievit ... usque ad finem agonis" (guidi1903 l.2050-2052), "cognominaverunt" (l.2064), "Scripsit autem ... libros multos" (l.2069-2070), and Mari's quotation ending on l.13520. Card `uncertain` 1 applied as worded. In the records, the Satan clause was added to the Guidi claim, and the witness now reads l.2032-2037, 2050-2064, 2069-2070. The contested claim and the Book III absent detail now cite l.2036-2064. The Mari witness now cites l.13517-13520. |
| R2-B-M2 (long card sentences; "which" after Khosrau) | Applied as worded to `uncertain` 5, `uncertain` 6 and `legacy.traces` 4. Seert l.29556-29558 and Scher's note l.29565 confirmed. |
| R2-B-M3 (Labourt's word "lost in the scan") | Applied as worded: "a word before the dates cannot be read in the Library's text of his page." The OCR word "phone" stands at labourt1904 l.17771. |

### Length and readability

No brief changed. The figures from R1 stand:

| Profile | Words | Time @162 | FK | Flesch |
|---|---|---|---|---|
| John Moschus (recorder) | 325 | 2:00 | 7.1 | 68.0 |
| Babai the Great (major) | 404 | 2:30 | 6.8 | 73.0 |
| Severinus of Noricum | 324 | 2:00 | 7.0 | 69.0 |
