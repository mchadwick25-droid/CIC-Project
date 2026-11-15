# Library search log: era 9 (1815-1906), batch 2a (2026-11-15)

The search record for the second fill of the era 9 wants. It covers the person rows for Africa, Asia, Oceania,
Latin America, the Caribbean and the Eastern churches in
`Build/Ministry/Operations/Audits/2026-11-12_wanted-sources-combined/Wanted_Sources.md` (rows 226, 246-248,
263-266, 279-322 and 324-326), batch 1's not-found rows by new routes (Darby, Ambrose of Optina, Sadrach, Tile,
Mokone, Hamberg, Os Sertoes) and the date checks batch 1 left owing (Kuyper's Stone Lectures, A Retrospect,
Walsh, Aggressive Christianity). The vendored files, their state and their shelves are in
`Build/Ministry/Features/Source-Library/CFT-Wants.md` ("Era 9, batch 2a"). Left for batch 2b: rows 227-245,
249-262, 267-278, 323 and 327-330, and the date check on the Kaiserswerth account "by a lady".

Rights rule for this batch: Mark's rulings R1 to R12 as recorded in `cic/texts/INTAKE.md`, section 2, and in the
Library's Decision-Log. Every file here rests on a printed year of 1930 or earlier. Where the title page prints
no year, the header names the copyright notice, or the dated preface together with the library catalogue
record that agrees with it. The rule for American books of 1931 to 1963 was not used. Nothing was taken from
the Dictionary of African Christian Biography.

## Hosts

| host | state from this sandbox | used |
|---|---|---|
| archive.org (advancedsearch, metadata, MARC record, djvu.txt, page images) | reachable | all 74 files |
| dbnl.org | its robots file disallows every automated client except two named search engines, and a search request was answered 429 | not used; see the hand-fetch list |
| HathiTrust, Papers Past, prlib.ru | refuse automated clients | not tried; see the hand-fetch list |
| gallica, books.google downloads, MDZ, documentacatholicaomnia | blocked or broken, by the earlier logs | not tried again |

No host was newly refused by the network proxy. archive.org has no full-text search from here, so every search
was by title, author and year, in the original script and in transliteration.

## How the batch ran

Six searchers ran in parallel (Sonnet), one per group: the Russian church and Alaska; the Eastern churches of
the Near East, the Balkans and Galicia; Africa; Asia; Oceania, Latin America, the Caribbean and the
Philippines; Darby and the owed date checks. A seventh went back for nine gaps. Each was held to one helper
script for archive.org and to `grep` and `sed` on the downloads. None stalled on a permission prompt; four
could not write their `report.md` (a tool rule refused the file) and gave the report in their final message.

The Library thread then checked every candidate: the byte count against the host's record, the host's rights
fields, the lending collections, and the imprint year on the title page. Ten imprints were read on page
images (listed below). One pick was dropped as a lending-library scan and replaced, one as held already, and
one host file was cut because its second half is a volume printed in 1932.

Five fresh checkers (Fable) then read every vendored file and wrote its title-page facts, content note and
locus from the text. The searchers' notes were used only as pointers.

## Imprints read on page images

Pharmakidis (leaf n7, 1849); Lindley, vol. 2 (n6, 1866); Reyes, La sensacional memoria (n8, 1899); Codigo de la
Reforma (n4, 1861); Darby, Studies on the Book of Daniel (n5, 1864); Darby, Dialogues on the Essays and Reviews
(n5, MDCCCLXIII); Davis, Sketch of Neesima (n8, 1890; the OCR reads 1800); Evans, Biographical Dictionary (n9,
1907); Dom Vital, O Bispo de Olinda (n8, 1873); Macedo Soares, A Guerra de Canudos (n6, 1902; the
OCR of the same title page misreads the year as 1903). Four more leaves were opened to find these and were blank or
were not title pages.

## Title pages that print no year

Taken on a copyright notice of 1930 or earlier: Hardy, Life and Letters of Neesima (1891); Uchimura, The Diary
of a Japanese Convert (1895); Jessup, Fifty-three Years in Syria, vols. 1 and 2 (1910); Catherine Booth,
Aggressive Christianity (Boston; "Entered ... in the year 1883") and Godliness (1883).

Taken on a dated preface that the catalogue record agrees with: Stern, The Captive Missionary (preface of 26
October 1868; MARC "[1868]"); Documentos interesantes de la Iglesia Filipina Independiente (January 1906; MARC
1906); Aglipay's Catequesis (prologue of 25 May 1912; MARC 1912); Macedo Costa, A Questao Religiosa (prefixed
letters of December 1886; MARC 1886; two prefixed letters are dated January 1887).

Not taken, because neither test is met:

- **Kuyper, Calvinism: the Stone Lectures (row 193).** `calvinismsixstonny00kuyp`, `calvinismsixston00kuyp`,
  `calvinismsixlect00kuypuoft`: no copyright notice and no dated preface; the only date is that of the lecture.
  The catalogue records read "[1899]", "[etc. etc., 1899]" and "[1899?]". The Dutch scans
  `hetcalvinismezes00kuyp` ("[1898?]") and `hetcalvinismez00kuyp` (second printing, "[19--]") are undated too.
- **Hudson Taylor, A Retrospect (row 204).** `retrospect0000tayl` (catalogue: 2nd ed., London, Morgan & Scott,
  1894) has no dated preface and no copyright notice; `retrospect00tayl_0` has no title page in the OCR;
  `cihm_88818` is catalogued "[1900?]".
- **Walsh on the Uganda martyrs (row 210).** `blnegromartyrsof00wals`: no year, no notice, no dated preface;
  the catalogue says "[between 1920 and 1929?]".
- **Catherine Booth, Aggressive Christianity, the London sermon (row 191).** `aggressivechris00boot` is a
  single sermon of 16 pages with only the day it was given. The Boston printing of the whole book was taken.
- `optinapustyn51` and its duplicate `1926_20251015` (row 197): preface dated 1926, no catalogue record.
- Makary Glukharev, Mysli o sposobakh (row 296), `mysliosposobahkuspeshnejshemurasprostran72`: a censor's leaf
  dated 30 July 1894, which would count like a dated preface, but the item has no catalogue record to agree.
- Mondon-Vidailhet's translation of the chronicle of Theodore, vol. 2 (`chroniquedetho02wald`): the catalogue
  says only "Pref. 1904". Stock's Story of Uganda in the scan `storyofugandavic00stoc`; the Toronto scan, whose
  title page prints 1892, was taken.
- Darby: `ministryonepistl00darb` (a later publisher's printing, no year) and `synopsisofbookso05darb`
  ("[18--]"). Kireevsky, vol. 2 (`polnoesobraniesochinenijivkireevskogo25`): no year in the OCR, no catalogue
  record. Oikonomos, Peri ton O' hermeneuton, vol. 1 (`peritnoermeneutn01oiko`): the title-page year cannot be
  read in the OCR or on the image. `respostadobispo00nacigoog` (Brazil).

## Dropped at the Library thread's check

- The archive.org item that holds Sheptytsky's book for the Ruthenians of Canada is named
  `herbarzpolskipow01niesuoft_202605`, an identifier that belongs to another book. The file's title page and
  colophon are Sheptytsky's (Zhovkva, 1911), and it was taken.

- `fiftythreeyearsi0000jess` (Jessup, vol. 1): a lending-library scan. Replaced by `fiftythreeyears00unkngoog`.
- `thechurchofarmen00ormauoft` (Ormanian, The Church of Armenia, 1912): held already.
- `brazilianmystic00cunn` (Cunninghame Graham): held already, from batch 1.
- The Chronicle of Menelik II: the host file holds tome I (Paris 1930) and tome II (Paris 1932). Only tome I
  was taken; the file is cut before tome II's title page, and its header says so.

## Not found

- **Row 212, Nehemiah Tile.** Not named in Whiteside's History of the Wesleyan Methodist Church of South Africa
  (two scans), Brownlee's Reminiscences, five volumes of Theal, Wells's Stewart of Lovedale, Du Plessis (1911),
  Molema (1920) or the Native Affairs Commission report of 1903-05. Du Plessis has one sentence on an
  ex-Wesleyan "Nehemiah" in Tembuland and the "Church of the Tembus" (`historyofchristi00dupl`, OCR line
  25540), without his surname. No Cape Blue-book and no volume of the Christian Express is on the host.
- **Row 305, Iakov Netsvetov.** Nothing before 1931 under about ten queries; his journals are in modern
  editions only.
- **Row 197, Ambrose of Optina:** his letters and Agapit's Life (about twenty more queries). **Row 293,
  Macarius of Optina:** his collected letters and the Life of 1861. The Optina history of 1902 tells of both.
- **Row 295, Theophan the Recluse:** his letters, Put' ko spaseniiu, Chto est' dukhovnaia zhizn' and the Russian
  Dobrotolyubie. **Row 296:** Makary Glukharev's letters.
- **Rows 291 and 292:** the acts of the Maronite synod of 1818, and anything by or on Elias Hoyek. **Row 290:**
  Massaad's own letters; Churchill (1862) does not name him.
- **Row 298, Nerses Varzhapetian.** **Row 301, Konstantinos Oikonomos:** his defence of the Patriarchate.
  **Row 302:** the acts of the council of 1872; von Mach's English book on the Exarchate; Gedeon's documents.
- **Row 288, Philiphe Binh.** His own book is in a modern printing only, and Louvet, Launay and Shortland do
  not tell of him.
- **Row 311, Liang Fa:** his tract. **Row 312, Ta'unga:** his own narrative; Gill (1855) quotes short reports.
- **Row 280:** the Doctrina y Reglas Constitucionales (1904), the Oficio Divino (1906), La religion del
  Katipunan (1900) and the church's periodical of 1903-04. **Row 281:** a second account of Apolinario de la
  Cruz that can be read (see Mas, below).
- **Row 285:** the Ley Juarez of 1855 (the Codigo de la Reforma begins with 1856). **Row 286:** the text of
  the consecration decree was not found by search in the two volumes of Garcia Moreno's writings.
- **Row 287:** Macedo Costa, Direito contra o direito; a printed Carta pastoral of Dom Vital.
- **Row 321:** Bokwe's Ntsikana. **Row 185:** Hamberg's Visions of Hung-Siu-tshuen under any spelling.
- **Row 181, Darby:** the Letters, the Collected Writings and a Life before 1931 (reprints of 1964 and 1974
  only). **Row 191:** Female Ministry (a reprint of 1975 only).
- **Rows 186 and 187:** no printing of Os Sertoes of 1902 to 1911 other than `004518-completo`; the other three
  items on the host are modern editions or the same Brasiliana file. Nothing in Conselheiro's own words.

## Seen and not taken

- `informesobreele00masgoog`: Sinibaldo de Mas, Informe (1843), which tells of Apolinario de la Cruz (OCR lines
  11425-11660). The catalogue says the title page is wanting and supplied in manuscript, the page images are
  blank or unreadable, and the OCR is badly garbled. `informe-sobre-...-vol-1` is CC BY-NC-ND.
- `les-martyrs-negres-de-l-ouganda-000001174`: a digital retyping marked "(c) Bibliotheque Saint Libere 2014".
- `aleut_matthew`: a retypesetting of 2006 with its own copyright line.
- `AAlexandrina-118680`: al-Dibs's Arabic history of the Maronites (1905); the OCR cannot be read.
- `shinkonikkitsuke0000uchi`: Uchimura in Japanese (1919); the OCR cannot be read.
- C. S. Smith's History of the African Methodist Episcopal Church (1922): reprint copies only.
- `mylifeinbasutola00casa`: a reprint of 1971. `hopesofchurchofg0000unse`: a modern lending scan.
- `conventionesdere0000vari` and Janvier's Constitutions d'Haiti (a reprint of 1977).

## Located, not yet taken

Ethiopia: Rassam, vol. 2 (`narrativeofbriti02rass`, 1869 on leaf n8); Waldmeier's Autobiography
(`autobiographyoft00wald`); Gobat's Journal (`journalthreeyea01gobagoog`), which does not tell of Salama III.
Uganda: Ashe, Two Kings of Uganda (`twokingsofuganda00ashe`), with a chapter on the murder of Balikudembe;
Baunard's Lavigerie, vol. 2 (`lecardinallavige02baunuoft`). Maronites: Churchill, Mount Lebanon, three volumes
(`mountlebanonate01churgoog`); al-Dibs (`unset0000unse_p3l6`, `unset0000unse_b7e8`). Greece: Oikonomos, vols.
2-4. Russia: John of Kronstadt's collected works, vol. 4 (1892), and extracts from his diary (1893). Japan:
`howibecamechrist00uchi` (1922). Pacific: Murray, Missions in Western Polynesia (`missionsinwester00murruoft`);
Gill, Life in the Southern Isles; the 1887 printing of Joel Bulu. Philippines: `ads8004.0001.001.umich.edu`.
Haiti: St. John, Hayti or the Black Republic (1884); Leger in French. Mexico: three more scans of the Codigo
de la Reforma. Ecuador: Berthe in French (4th ed., 1888). Brazil: `amaonariaeosjes00olivgoog` (1875).
Demerara: `reportproceedin01socigoog`, `casejohnsmithon00socigoog`, `missionarysmith00commgoog`. Brethren:
`lecturesonsecond0000jnda_p7b1` (1909). Catherine Booth: `papersonpractica00boot` (1891),
`popularchristian00boot_3` (1904). Northeast India: `aonagaprimer00clariala` (1891). Sadrach: none further.

## Hand-fetch list for Mark

Hosts that refuse automated clients, so nothing was fetched from them. Each needs a browser.

| want | where | edition |
|---|---|---|
| Row 207, Kiai Sadrach | dbnl.org, full-text search for "Sadrach" and "Karangjoso" | Dutch mission periodicals and reports before 1931 (Heyting's report; Lion Cachet, Een jaar op reis in dienst der zending, 1896) |
| Row 224, Hendrik de Cock | dbnl.org | the Acte van Afscheiding of 1834; a Life before 1931 |
| Row 204, A Retrospect | HathiTrust catalogue, "A retrospect" by J. Hudson Taylor | any printing whose title page prints a year (the first is London, Morgan & Scott, 1894 by the catalogue) |
| Row 193, Kuyper's Stone Lectures | HathiTrust | a printing with a dated title page or copyright notice (Revell, New York; Hoveker & Wormser, Amsterdam) |
| Row 212, Nehemiah Tile | HathiTrust | Cape of Good Hope, Blue-book on Native Affairs, 1884 and 1885 |
| Row 197, Ambrose of Optina | prlib.ru | Sobranie pisem optinskogo startsa ieroskhimonakha Amvrosiia (1906-08); Agapit's Zhizneopisanie (1900) |
| Row 293, Macarius of Optina | prlib.ru | Sobranie pisem ... Makariia (1862-63) |
| Row 312, Ta'unga | Papers Past | Rarotongan mission papers that print his letters |
