# Library search log: era 9 (1815-1906), batch 2b (2026-11-15)

The search record for the Library thread's fill of 49 person rows of
`Build/Ministry/Operations/Audits/2026-11-12_wanted-sources-combined/Wanted_Sources.md`: rows 227-245, 249-262,
267-278, 323 and 327-330, with the date check batch 1 left on the Kaiserswerth account "by a lady" (row 223). A
sibling thread, batch 2a, took the other rows of 226-330 and batch 1's other retries. The vendored files, their
state and their shelves are in `Build/Ministry/Features/Source-Library/CFT-Wants.md` ("Era 9, batch 2b").

Rights rule (as recorded on main, 15 November): the imprint year on the title page, 1930 or earlier; a reprint
by its own date; where the title page prints no year, a copyright notice of 1930 or earlier, or a dated preface
the library catalogue's date agrees with; a year printed in the title on the title page where the catalogue
agrees. The wider rule for American books of 1931 to 1963 was not used: no such book was found for these rows.
No owner-declared free text was taken.

## Hosts

| host | state from this sandbox | used |
|---|---|---|
| archive.org (advancedsearch, metadata, djvu.txt, page images) | reachable | all 61 files |
| dbnl.org | reachable, by the earlier logs | not needed: Groen van Prinsterer was found on archive.org |
| HathiTrust, Papers Past, prlib.ru | refuse automated clients | not tried |
| gallica, books.google downloads, MDZ, documentacatholicaomnia | blocked or broken, by the earlier logs | not tried |

No host was newly refused by the network proxy. archive.org has no full-text search from here, so every search
was by title, author, subject and year.

## How the batch ran

Five searchers (Sonnet), by group: the American revival and holiness rows; the Black church, Baptist, Quaker and
Unitarian rows; the new American movements, the Catholic Apostolic Church and the Brethren; the British rows;
the Continental rows and the Kaiserswerth date check. A sixth searcher retried seven rows the first pass left
empty, with new queries. Each was held to `tools/ia.py`, `grep` and `sed`, and checked
`cic/texts/REGISTRY.yaml` first. None stalled on a permission prompt. Each reported that its write of a
`report.md` file was refused, so the reports came back as messages and the picks as `picks.json`.

The Library thread then checked every pick: the byte count against the host's record, the host's rights fields,
and the date on the title page. Seven dates were read on the scan's page image by the Library thread itself (Elaw, Taylor, Emma
Smith's hymnbook, Monod in French, Lasserre in French, the Kaiserswerth account, Roberts's preface). Fresh checkers (Fable) then wrote every content note and locus from the staged
text; searchers' notes were not used.

## Changed at the Library thread's check

- **Row 228, Williams, Life of Elder John Smith.** The searcher's pick (`lifeofelderjohns00will`) carries the
  imprint "Christian Board of Publication, St. Louis" with no year, and the host dates it 1870 from the preface:
  a later, undated reprint. Replaced by `lifeofelderjohns00williala`, whose title page prints "Cincinnati: R. W.
  Carroll & Co., 1870".
- **Row 251, Emma Smith's hymnbook.** `collectionofsacr00smit` carries an Intellectual Reserve copyright line
  and was not taken. The microfilm copy `per_utah-and-the-mormons_a-collection-of-sacred-h_emma-smith_1835`
  carries no modern notice; its title page image prints 1835. Taken.
- **Row 276, Lohe in German.** `etwasausdergesc00lhgoog` (Etwas aus der Geschichte des Diaconissenhauses
  Neuendettelsau, third edition, Gutersloh 1907; the year read on the page image) was dropped after the
  checker's read: the black-letter OCR cannot be read, title page included. Listed below as located.
- **Row 239, Taylor's Story of My Life.** The title page prints 1895; the text prints a document and an entry
  of June 1896. The header says so.

## Stripped at intake

Google's own preamble was removed from the twelve files that come from Google scans, and nothing else: the
notice that begins "This is a digital copy of a book" through the web-address line that closes "About Google
Book Search". Each header's Provenance note gives the line and byte
count removed. No archive.org notice and no OCR debris was removed. In these headers, line numbers are the
vendored file's own lines.

## Not found

- **Row 230, Daniel Coker.** No original printing of the Dialogue (1810) or the Journal (1820) under about
  twenty queries. `msam.-282-11` and `msam.-282-12` are typescripts of 1900 by G. W. Forbes (a sketch of Coker
  and a transcript of his journal): not a printing, so cite only. Payne's History of the African Methodist
  Episcopal Church (1891), which tells of Coker, was taken in their place.
- **Row 249, Hiram Edson.** His account of the morning after 22 October 1844 was not found in any printing
  before 1931. His discourse of 1849 was taken. `graduatetheologi00hira` (an Advent Review bundle of 1850) is
  located.
- **Row 253, Emmeline B. Wells.** No bound volume of the Woman's Exponent; the host holds partial sets of
  issues only (`exponent1882`, `1883`, `1886`, `1890`, `1891`, `1893`), not taken. No Life found.
- **Row 258, Tirzah Miller.** Nothing before the edition of 2000.
- **Row 327, "Awstin" and the Western Mail.** The Religious Revival in Wales pamphlets (Cardiff, 1904-05) were
  not found under nineteen queries (title, publisher, creator, the Welsh title, the year window).
- **Row 268, Priscilla Lydia Sellon.** Nothing of her own (the Reply to Spurrell, A Few Words) and no Life
  before 1931. Two pamphlets of 1852 by others were taken. `reportofinquiryi00chur` (the Exeter inquiry of
  1849) is located.
- **Row 260, J. G. Bellett.** Neither the Recollections by his daughter (1895) nor the Interesting
  Reminiscences. One of his own books was taken.
- **Row 255.** Norton's Memoirs of James and George Macdonald (1840) and his Restoration of Apostles and
  Prophets (1861); vol. 2 of the Morning Watch (1830). **Row 254:** the Christadelphian magazine, Roberts's
  autobiography, his Life of Dr. Thomas, and any Life of him. **Row 241:** the Proceedings of the Southern
  Baptist Convention of 1845 (the host's items so dated are volumes of 1916 to 1925). **Row 242:** the Baptist
  Union's record of 1887-88. **Row 240:** Hailey's Life of Graves (1929). **Row 236:** Wilder's own history of
  the movement (1935). **Row 237:** vol. 2 of the Life of Bunting (1887). **Row 276:** Drei Bucher von der
  Kirche in German, and Deinzer's Life. **Row 277:** Estrade's Apparitions de Lourdes, and Bernadette's own
  depositions. **Row 278:** the Pastoral "out of the Flaminian Gate" as a separate print. **Row 270:** no
  English print of Ongeloof en Revolutie before 1931. **Row 330:** the census names a modern encyclopedia
  article, which is not a text to hold; Sarah Clarke's own account of 1914 was taken.

## Seen and not taken

- `collectionofsacr00smit` (row 251): an Intellectual Reserve copyright line. Held for Mark with batch 1's
  Doctrine and Covenants of 1852.
- `lifeofelderjohns00will` (row 228): an undated later reprint (above).
- `etwasausdergesc00lhgoog` (row 276): OCR that cannot be read (above).
- `OngeloofEnRevolutieG.GroenVanPrinsterer1847` (row 270): the host dates it 1847; its title page reads "Derde
  uitgaaf, 1903". The second edition of 1868 was taken.
- `pacificgardenmis0000carl_r4e1` (row 330): 1942, and no renewal search was run because Sarah Clarke's own
  account of 1914 fills the want.
- `christendomastra0000robe` (1927) and `patriarchsbeingm0000jgbe` (1909): lending copies.

## Two picks on a lending-style identifier

`threebooksconcer0000wilh` (Lohe, Three Books concerning the Church, 1908) and `lettertomisssell0000phil` (the
Bishop of Exeter's Letter to Miss Sellon, 1852) are in the host's own-scans collection. Neither record carries
the access-restricted flag, and each full text downloaded whole from the public address with the listed byte
count. They were taken on their title-page years.

## Located, not yet taken

Further volumes: Hodder's Shaftesbury, vols. 2-3 (`lifeworkofsevent02hodduoft`, `india.history.resource.86561`);
Ashwell and Wilberforce, vols. 2-3 (`a614417002ashwuoft`, `lifeoftherightre03ashwuoft`); the Life of Maurice,
vol. 2 (`lifeoffrederickd02maur`); Ward's Wiseman, vol. 2 (`lifeandtimescar03wardgoog`); Froude's Remains, part
1, vol. 2 (`remainsoflaterev12frouuoft`); Cabot's Emerson, vol. 2 (`memoirofralphwal02caboiala`); Drummond's
Speeches, vol. 2 (`speechesinparlia02drumuoft`); Dialogues on Prophecy, vols. 2-3 (in the same item, and
`10410364bsb`); the Morning Watch for 1830 and 1831 (`morningwatchorq02hendgoog`, `morningwatchorq01hendgoog`).

Other witnesses: Cox's Life of Colenso, vol. 1 (`lifeofjohnwillia01coxg`); Colenso's Pentateuch, part 2
(`pentateuchandbo01colegoog`); Mott's history of the Student Volunteer Movement (1892, no printed year,
`historyofstudent00mott`) and Wilder's pledge pamphlet (1890, `pledgeofstudentv00wild`); Hamilton's history of
1895 (`ahistoryunitasf00hamigoog`); the Sisk translation of Lasserre (1872, `ourladylourdest00monzgoog`);
Roberts's The Trial (1908, `thetrialofthemos00robeuoft`) and his debate with Bradlaugh (1876,
`isbibledivineas00robegoog`); Bellett's Minor Prophets (1870) and Evangelists (1886); Newton's Thoughts on the
Apocalypse in the printing of 1904; the Pacific Garden Mission's annual reports of 1895, 1907 and 1915; the
Life of Lorenzo Snow by Eliza R. Snow (1884); In His Steps in printings of 1899.

## For Mark to fetch by hand

Nothing was verified on HathiTrust, Papers Past or prlib.ru, since they refuse automated clients, so no URL
is listed. The texts most worth a hand search there, each with the edition wanted: Coker's Journal (Baltimore,
1820) and Dialogue (Baltimore, 1810); the Western Mail's The Religious Revival in Wales (Cardiff, 1904-05, six
numbers); Bellett's Recollections (1895); Norton's Memoirs of James and George Macdonald (1840); Sellon's Reply
to a Tract by the Rev. J. Spurrell (1852); the Proceedings of the Southern Baptist Convention (Richmond, 1845);
a bound year of the Woman's Exponent.
