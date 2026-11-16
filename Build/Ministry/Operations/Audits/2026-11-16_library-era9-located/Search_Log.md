# Library search log: era 9 (1815-1906), the located volumes, 2026-11-16

The record for the follow-on to era 9 batch 2b: the volumes that batch listed as "Located, not yet taken"
(`../2026-11-15_library-era9-b2b/Search_Log.md`). Twenty-eight files were vendored (4,093,682 words). Their
states and shelves are in `Build/Ministry/Features/Source-Library/CFT-Wants.md` ("Era 9 (1815-1906), the located
volumes"). The 134 card rows of that batch's `Texts_To_Fetch_Era9.md` were not taken: the list came from the
legend check and was dropped by the coordinator, passing on Mark's direction of 2026-11-15. No quote, story or
lexicon entry was rendered.

## The check before the fetch and the search

Run on 15 November against `cic/texts/REGISTRY.yaml`, `Build/worlds/_cross-world/download-queue-seed.yaml`,
`Build/worlds/_cross-world/WANTS-REGISTER.md` and `Build/worlds/_cross-world/CORPUS-USE.md`, by archive.org
identifier for the twenty listed scans, and by author and title in `cic/texts/` for all of them and for the six
listed items that had no identifier (Bellett's two books, the Life of Lorenzo Snow, the Pacific Garden Mission's
reports, the later volumes of the Dialogues, Froude's other volumes). Run again against `origin/main` just
before intake.

- No listed scan's identifier was held. The item `dialogues-on-prophecy` is in the registry for vol. I; vol. II
  is another file of the same upload.
- Later printings of a held text, not taken: Sheldon's In His Steps in printings of 1899 (the print of 1897 is
  held); Newton's Thoughts on the Apocalypse in the printing of 1904 (the second edition of 1853 is held).
- A second English version of a held work, taken: Lasserre's Our Lady of Lourdes in Sisk's translation of 1872
  (the held English of 1870 names no translator).
- Neither register names any of these works.

## Searches

Six short searches of archive.org's catalog (title and creator fields) for the items without an identifier,
and one for Froude's volumes. Found: Bellett's Minor Prophets (`minorprophets00bell`) and Evangelists
(`11604936bsb`); the Life of Lorenzo Snow (`biographyfamilyr00snow`); two Pacific Garden Mission reports
(`annualreportpaci1907paci`, `annualreportpaci1915paci`); Dialogues on Prophecy, vol. II, as a file of the
upload `dialogues-on-prophecy`; Froude's part 1, vol. II (`remainsoflaterev21frou`) and part 2, vol. II
(`a5826854rs02frouuoft`). Not found: the mission's report of 1895.

## Rights rule used

A printed imprint of 1930 or earlier, read on the title page in the OCR or on the scan's page image. No file
carries a permission notice or a non-commercial license other than Google's standard sheet. "All rights
reserved" on six title pages of 1881 to 1897 does not block them (R12's companion ruling). Nothing was taken
under the rule for American books of 1931-1963.

Calls made here, which the coordinator or Mark may overrule:

1. **The Pacific Garden Mission's fortieth annual statement: taken, dated 1916 by its own text.** The cover and
   the title leaf print no year (page images, leaves n0 and n2). The statement opens "The close of our fiscal
   year ending Sept. 15th, 1916" (host lines 43-44), the auditor's letter is dated 17 November 1916 (line 430),
   and the library's shelf mark on the cover reads 1915/16. The archive.org record has no date field. R12
   speaks of a copyright notice or a dated preface with the catalog agreeing; this is a dated report whose
   every internal date is 1915 or 1916, and the header's rights line says what the date rests on.
2. **Dialogues on Prophecy, vol. II: taken on its printed year.** The only scan is a reader's upload of a Google
   reproduction, with no library catalog record. The title page prints MDCCC XXVIII and James Nisbet, the same
   publisher as vols. I and III. The page image could not be read, since the upload holds three books in one
   item; the year is the OCR's.
3. **Cabot's Emerson, vol. II, is the eighth edition of 1895**, while the held vol. I is the printing of 1887.
   The two volumes are from different printings of the same work; the header says so.
4. **The American Church History volume is taken whole** (three histories), with a shelf row only for
   Hamilton's Moravian history, the wanted text. The two Reformed histories have no census entry of their own
   among the shelves and get no row.

## How each file was checked

Twenty-eight scans were fetched on 15 November (`fetch.py`); each byte count equals the size archive.org lists
(`fetch_manifest.json`). Four Sonnet mappers mapped the contents under the era 8 `MAPPER_BRIEF.md`
(`mapper-reports/`). The Library thread read every title page in the OCR, and read the page image wherever the
OCR year was garbled or missing, or differed from the host's date:

| file | leaf | what the page image prints | what the OCR reads |
|---|---|---|---|
| Cox, Life of Colenso, vol. I | n6 | "London: W. Ridgway. 1888." | the place and year are missing |
| Lasserre, tr. Sisk | n7 | "Thomas Richardson and Son ... MDCCCLXXII." | "UDOCOLZZU." |
| Roberts, The Trial | n6 | "Birmingham: C. C. Walker ... 1908." | "1008." |
| Hodder, vol. II | n10 | "1887." | "1387." |
| The Morning Watch, vol. III | n8 | "1831." | "18SL" |
| The Morning Watch, vol. I | n8 | "Vol. I.-1829." and, under the publisher, "1830." | the same |
| Roberts and Bradlaugh | n6 | "1876." | garbled |
| Mott, History | n2 | "1892" under the author's name | the year is missing |
| R. G. Wilberforce, vol. II | n10 | "1881" | the same |
| R. G. Wilberforce, vol. III | n10 | "1882" | the same (a library slip's "1880" stands above it) |
| Froude, part 1, vol. II | n6 | "1838." | the same |
| Froude, part 2, vol. I | n8 | "1839." | the same |
| Froude, part 2, vol. II | n6 | "1839." | the same |
| Pacific Garden Mission, 31st report | n2 | "September 15, 1908" | the same |
| Pacific Garden Mission, 40th statement | n0, n2 | no year | the same |

The other thirteen years are the OCR's and agree with the host's date: Dialogues vol. III (1829), Hodder vol.
III (1886), Maurice (1884), Ward (1897), Cabot (1895), Drummond (1860), Colenso (1863), Wilder (June 1890), the
American Church History volume (1895), Bellett (1870; 1886), Snow (1884), and Dialogues vol. II (see call 2).

The spec that wrote the headers (`mkspec299.py`) checks about 110 line anchors against the host text before it
writes anything. Two first failed on OCR garbles of the right word.

## Corrections to the list

- The scan listed as Colenso's Pentateuch, part 2 (`pentateuchandbo01colegoog`), is **part III** (1863,
  Deuteronomy). Part II was not found.
- The scan listed as Froude's Remains, part 1, vol. 2 (`remainsoflaterev12frouuoft`), is **part 2, vol. I**
  (1839). Part 1, vol. II, and part 2, vol. II, were found as well, so the Remains are now held whole.
- `10410364bsb` holds vol. III of the Dialogues only.
- `india.history.resource.86561` is Hodder's vol. III, in the printing of 1886; vol. II is of 1887.
- `morningwatchorq02hendgoog` is vol. I (1829) and `morningwatchorq01hendgoog` is vol. III (1831). Vol. II
  (1830) and the later volumes were not looked for.
- The Pacific Garden Mission scans report the years ended September 1908 and September 1916, whatever the
  identifiers say.
- Bellett's Evangelists scan holds the part on John only, though its contents list four Gospels.

## Hosts

| host | state from this sandbox | used |
|---|---|---|
| archive.org (catalog search, metadata, djvu.txt, page images) | reachable | all 28 files |

No other host was tried, and none was refused by the network proxy.

## Still not held

The Pacific Garden Mission's report of 1895; Colenso's part II; the Morning Watch, vol. II and vols. IV-VII;
Bellett's Evangelists on Luke, Matthew and Mark; Cox's Colenso, vol. 2; the hand-fetch items of batch 2b's
search log.

## Cautions for profile writers

- **Lives with letters and diaries inside** (R. G. Wilberforce, Hodder, Maurice, Ward, Cabot, Cox, Eliza Snow):
  name the diarist or letter-writer when quoting, and say whose book prints it.
- **The Bradlaugh debate** is a shorthand report printed by Roberts; he says Bradlaugh did not revise it.
- **Froude's Becket** has passages in large type and bracketed notes that the editors say are not his.
- **No author on the title page:** the Dialogues, the Morning Watch, The Trial. Drummond's part in the
  Dialogues is not stated in the volumes.
- **Two "Thirteenth" conversations:** vol. II of the Dialogues ends with a Conversation the Thirteenth and vol.
  III opens with another so headed. Cite by volume and line.
- **Lasserre in Sisk's English** is a translation; Bernadette's words come through two hands.
