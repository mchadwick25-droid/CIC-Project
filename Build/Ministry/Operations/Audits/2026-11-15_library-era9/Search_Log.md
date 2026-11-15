# Library search log: era 9 (1815-1906), batch 1, the major figures (2026-11-15)

The search record for the Library thread's first fill of the era 9 wants: the 63 person rows marked major in
`Build/Ministry/Operations/Audits/2026-11-12_wanted-sources-combined/Wanted_Sources.md` (rows 163-225). The
vendored files, their state and their shelves are in `Build/Ministry/Features/Source-Library/CFT-Wants.md`
("Era 9, batch 1"). This file says where the batch searched, what it found, what it did not find, and what it
did not take. The rows not marked major (226-330), the era 9 outside witnesses, the era 9 council records and
the held eras 8-9 items are left for the next batches.

Rights rule for this batch (settled): only a printed imprint year of 1930 or earlier, read on the title page in
the OCR or on the scan's page image; a reprint counts by its own date; no NC or ND license, no permission
notice, no access-restricted item. During the batch Mark ruled on title pages that print no year (15 November:
"Copyright notice yes, preface with a check"): a copyright notice dated 1930 or earlier stands for the date,
and a dated preface stands for it where the library catalogue's date agrees. The wider rule of the same day
(American books of 1931 to 1963 that were never renewed; owner-stated free texts) was not used in this batch.

## Hosts

| host | state from this sandbox | used |
|---|---|---|
| archive.org (advancedsearch, metadata, djvu.txt, page images) | reachable | all 99 files |
| dbnl.org | reachable, by the eras 4-5 log | not tried in this batch (see Sadrach and de Cock below) |
| gallica, HathiTrust, books.google downloads, MDZ, documentacatholicaomnia | blocked or broken, by the era 5 log | not tried again |

No host was newly refused by the network proxy. archive.org has no full-text search from here, so every search
was by title, author and year.

## How the batch ran

Seven searchers ran in parallel (Sonnet), one per group: North American revival and restoration; new American
movements; British Dissent and the Caribbean; the Church of England, the Salvation Army and Wales; Continental
Europe; the Eastern churches; Africa, Asia and Latin America. Each was held to one helper script for
archive.org and to `grep` and `sed` on the downloads, and each checked `cic/texts/REGISTRY.yaml` first. None
stalled. They handed back about 100 candidates.

The Library thread then checked every candidate: the byte count against the host's record again, the host's
rights fields, and the imprint year on the title page. Where the OCR did not show the year, the page image was
read. Eighteen imprints were read on page images in this way, and three more title pages were read and found to
print no year. Thirteen candidates were dropped at this check (listed below; six of them came back in after
the ruling on undated title pages), and one not picked by a searcher was added after its title page image was read (the
English Declarations and Letters of Dollinger, 1891).

## Held already

- Row 200, Joseph Audo: Badger, The Nestorians and their Rituals (1852), both volumes, as an English witness.

## Not found

- **Row 181, John Nelson Darby.** No scan of the Letters or the Collected Writings before 1931 under about
  fifteen queries; the only hits are reprints of 1964 and 1974. Four of his own smaller books are located and
  not yet taken: `cihm_07686` (Seven lectures on the second coming, 1863), `studiesonbookda00darbgoog` (1864),
  `dialoguesonessa00darbgoog` (1863), `ministryonepistl00darb` (1900).
- **Row 197, Ambrose of Optina.** No letters and no early Life, in Cyrillic or in transliteration, under about
  twelve queries.
- **Row 207, Kiai Sadrach.** Nothing on archive.org under Sadrach, Sadrak, Karangjasa, Bagelen, Poerworedjo
  and the Dutch mission words. dbnl.org was not searched.
- **Rows 212 and 213, Nehemiah Tile and Mangena Mokone.** Neither is named in the report of the South African
  Native Affairs Commission of 1903-05 (`southafricannati00sout`, its section on the Ethiopian movement) or in
  five 1896 numbers of the Voice of Missions that were read. Sundkler (1948) is out by date.
- **Row 178, John Thomas:** Eureka, and any Life of him. **Row 180, Noyes:** Bible Communism and a volume of
  the community's paper (only single weekly numbers are scanned). **Row 191:** Catherine Booth's Female
  Ministry of 1859 (only a reprint of 1975). **Row 214:** War on the Saints before 1931 (reprints of 1964 to
  1994 only), and anything in Evan Roberts's own words. **Row 222:** Bourne's History of the Primitive
  Methodists (1823). **Row 224:** the Act of Secession of 1834 and a Life of de Cock. **Row 196:** the Missouri
  Synod's constitution of 1847 as a separate print. **Row 218:** Lipscomb's census letters of 1906 (Religious
  Bodies 1906, vol. 2, was read and does not name him). **Row 185:** Hamberg's Visions of Hung-Siu-tshuen
  (1854) under its own title. **Row 198:** a diary or Life of Nikolai of Japan. **Row 199:** any account of
  Khrimian in English before 1931. **Row 201:** an Arabic Coptic history in a printing before 1931. **Row
  202:** Barsukov's Life of 1883 and the Works of 1886-88. **Row 194:** the Gereformeerde Dogmatiek (the only
  item has no text on the host). **Row 193:** a Life of Kuyper before 1931. **Row 223:** Fliedner's own
  account of Kaiserswerth in German. **Row 173:** Spiritual Gifts in a printing before 1931. **Row 186:**
  Conselheiro's own sermon notebooks.

## Seen and not taken

No printed year on the title page, and the check the ruling asks for still owed (a copyright notice of 1930 or
earlier, or a dated preface that the library catalogue's date agrees with):

- `calvinismsixstonny00kuyp`, `calvinismsixston00kuyp`, `calvinismsixlect00kuypuoft`: Kuyper, Calvinism, the
  Stone Lectures for 1898-1899 (row 193). Three scans; none prints a year.
- `aggressivechris00boot`: Catherine Booth, Aggressive Christianity (row 191). Only the day the sermon was given.
- `retrospect0000tayl` and five other scans of Hudson Taylor's A Retrospect (row 204).
- `blnegromartyrsof00wals`: Walsh, on the Uganda martyrs, with a chapter on Charles Lwanga (row 210).
- `inspiration00hodg`, the separate printing of Hodge and Warfield (row 217); `kaiserswerthdea00deacgoog` (row
  223); `optinapustyn51` (row 197).

Taken after the ruling, each with the date and its place named in the rights line: Offord's Jerry McAuley
(copyright 1885), McAuley's Transformed (copyright 1876), Booth-Tucker's Life of Catherine Booth, vol. 1
(copyright 1893), The Story of the Welsh Revival (copyright 1905), Ellis's History of Madagascar, vols. 1 and 2
(preface of 10 October 1838; the Wellcome Library's catalogue date is 1838; vol. 2 prints no date of its own).
Wayland's Life of Trust was first set aside as undated; its title page image prints 1868 under a library
stamp, and it was taken. The full Life of Pastor Hsi (row 205) turned out to be bound in the scan of One of
China's Scholars.

OCR that cannot be read:

- `MN41583ucmf_3`: Wichern's Denkschrift, third edition, Hamburg 1889 (row 192; the imprint was read on the
  page image). `ignazvondlling01frie`: Friedrich, Ignaz von Dollinger, vol. 1, 1899 (row 195).
  `bub_gb_fLdlAAAAMAAJ`: Dollinger, Briefe und Erklarungen, 1890 (row 195). All three are black letter.
- `1875WaldenstromPGudsLamBetraktelseOverJesaja53V.6`: Waldenstrom in Swedish, 1875 (row 225).
- The Armenian works of Khrimian (row 199): `amboghjakanerker00khri` (1929), `hrawirakerkrina00hayrgoog`
  (1892), `haygoyzhashkhar01hayrgoog` (1877), `sirakewsamulbar01hayrgoog` (1893). Two more were not sampled:
  `haygoyzhashkhar00hayrgoog` (1908), `sirakewsamulbar00hayrgoog` (1887).
- A Rhenish Mission item of 1928 on Nommensen (row 206).

Reprints, by their own date: the Metropolitan Tabernacle Pulpit reprint of 1974; the Darby reprints; Spiritual
Gifts (1945 facsimile); the Christian Baptist, vol. 1 (1955); Science and Health "1875" (a modern reprint);
Rufayla's Coptic history (the 2000 reprint of the 1898 edition); War on the Saints.

Typed transcriptions with no title page to check: Spiritual Gifts, vols. 1 and 2; Phillips, Evan Roberts, the
Great Welsh Revivalist (the 1923 English edition), which also asks for private use only.

## Held for Mark

- `004518-completo`: Os Sertoes, third edition, Laemmert, Rio de Janeiro, 1905 (rows 186 and 187). The only
  printing before 1931 on the host, with clean OCR. The host record carries the Public Domain Mark, but the
  Brasiliana USP notice at the end of the file asks for non-commercial use and no republication without leave.
- `bookofdoctrineco01unse`: Doctrine and Covenants, Liverpool 1852 (row 174), which carries an Intellectual
  Reserve copyright line. The Kirtland printing of 1835 was taken in its place.
- `brukspatronadamsson1863waldenstrom` (CC BY-NC-ND 4.0) and `brukspatronadamsson01waldenstrom` (CC BY-NC-SA
  2.5): Waldenstrom in Swedish (row 225).

## Located, not yet taken

Further volumes of works taken in part: Spurgeon's Autobiography, vols. 2-4 (`spurgeonsautobio02spuruoft`,
`03`, `04`); Irving's Collected Writings, vols. 1-4 (`collectedwriting01irvi` to `04irvi`); Liddon's Life of
Pusey, vols. 2-4 (`lifeofedwardbouv02lidd_1`, `03lidd_0`, `04lidd`); Coleridge's Memoir of Keble, vol. 2
(`memoirofrevjohnk02cole`); the Journal of Discourses, vol. 2 (`gtu_32400003383829`); the Christian Baptist for
1826 and 1829; year volumes of the Millennial Harbinger; Zion's Watch Tower for 1879-1881; Veniaminov's Notes,
part 3 (`zapiskiobostrovahunalashkinskogootdelas87`), his letters (1898) and Z. Barsukova's Life (1901);
Friedrich's Dollinger, vols. 2-3; Der Lutheraner, the fourth year, which prints the 1847 constitution
(`DerLutheraner04`); Walther's Kirche und Amt (1875); Wichern's Gesammelte Schriften (1901); Lindley, vol. 2;
Hudson Taylor, vol. 2 (`hudsontaylorchin00tayl`); the Tracts for the Times, vols. 3 and 4.

Other witnesses: Cannon's Life of Joseph Smith (1888); Gates's Life of Brigham Young (1930); Frothingham and
Chadwick on Parker; Petty's History of the Primitive Methodists (1860); Morgan (1909) and Lewis (1906) on the
Welsh revival; Hadley, Down in Water Street (1902); Rullmann on the Secession (1930); Lewis's Review (1829)
and Waln (1826) on the Hicksite separation; Crowther's Gospel on the Banks of the Niger; a French book on the
Uganda martyrs, not checked (`les-martyrs-negres-de-l-ouganda-000001174`).

## The ruling on undated title pages

The batch first left out thirteen wanted texts whose title pages print no year. The point was put to the
coordinator, and Mark ruled on 15 November: "Copyright notice yes, preface with a check". Six files came in
under it (above). The rule is in `cic/texts/INTAKE.md`, section 2, and the ruling is quoted in the Library's
Decision-Log.
