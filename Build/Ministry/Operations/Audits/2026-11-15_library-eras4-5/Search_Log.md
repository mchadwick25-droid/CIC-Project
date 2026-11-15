# Library search log: eras 4-5 (622-1300), second fill, 2026-11-15

The search record for the Library thread's second pass over eras 4 and 5. The first pass is in
`2026-11-13_library-era4/Search_Log.md` and `2026-11-13_library-era5/Search_Log.md`. The wants this time are the
rows those passes left not found or held, and the Library wants the Who and council batches added since: Open-Gaps
263, 265, 266, 268 and 272, with one item from 267. The vendored files, their state and their shelves are recorded
in `Build/Ministry/Features/Source-Library/CFT-Wants.md` (the "Eras 4-5, second fill" section). This file says where
the batch searched, what it found, what it did not find, and what it did not take.

Rights rule for this batch: only a printed imprint of 1930 or earlier, read on the title page; a reprint counts by
its own date; no NC or ND licence, no permission notice, no access-restricted item.

## Hosts

| host | state from this sandbox | used |
|---|---|---|
| archive.org (advancedsearch, metadata, djvu.txt, page images) | reachable | 45 of the 46 files |
| dbnl.org | reachable | the 1875 Hadewijch |
| gallica, HathiTrust, books.google downloads, MDZ, documentacatholicaomnia | blocked or broken, by the era 5 log | not tried again |

No host was newly refused by the network proxy.

## Holdings check, before any search

A whitespace-tolerant grep of the full text of every file in `cic/texts/` for 44 title and name patterns (al-Muqtabis
and Ibn Hayyan, Berno's testament, the Lives of Constantine, the twenty martyrs of Mar Saba, Peter the Higumen,
Photius against the Manichaeans, Boris and Gleb, the Synodikon, Willibald, the Caroline Books, the Life of Tarasius,
the Mystagogia, Skylitzes, Attaleiates, Zonaras, Pachymeres, Akropolites, Walter Daniel, Hadewijch, Teodosije, De
miseria, the Life of Robert, Dominic's process, Humbert's Legenda, Valdes, Cosmas the Priest, Nerses of Lambron, the
Lyon sentence, Fulcher, the Gesta Francorum, Guibert, Wendover, Peter of Vaux-de-Cernay, Bekkos, Zelus fidei,
Cummian, the Annals of Ulster, the Anglo-Saxon Chronicle, Deusdedit).

Held already, and missed before:
- **Berno's testament (era 4 row 32).** The held PL 133 file prints it whole: "TESTAMENTUM DOMNI BERNONIS", at about
  file line 67228 of `odo-cluny_opera-with-john-of-salerno-vita-odonis-pl133-lat_migne1853.txt`. The first era 4 log
  said PL 133 does not print it; that was wrong.
- **The sentence of Lyon I against Frederick II (council row 19).** Matthew Paris copies the bull into his chronicle:
  "ad Apostolice dignitatis", at about file line 29303 of
  `matthew-paris_chronica-majora-v4-rolls-series-57-lat_luard1877.txt`.

Held and not enough: the Latin Passion of the twenty martyrs in the Acta Sanctorum, March III (no Greek); Döllinger
II, which names Valdes but does not print his profession; the Armenian Recueil I, which cites Nerses of Lambron's
synodal speech but prints only his letter to Leo II and extracts; the 1750 Acta Sanctorum for August I, whose OCR
could not be searched for Dominic's process.

## Searches, by group

Six searchers ran in parallel (Sonnet), one per group. Two stalled and were stopped; two more finished their work
from the files already fetched. Each pick was then checked by the Library thread: the title page, the byte count
against the host's live record, the wanted passage. Where the OCR could not give the imprint year, the Library
thread read it on the scan's page image (Mansi XII, Acta Sanctorum March II).

**Era 4, Latin West.**
- Willibald's Life of Boniface: Levison's Latin (1905) and Robinson's English (1916) taken. Two more scans of each
  not taken.
- The Caroline Books: Bastgen (MGH, 1924) taken. PL 98 not found. A modern CC0 upload not taken.
- Hadrian I's reply to Charlemagne: MGH Epistolae V (1899) taken; its record is mislabelled. The reply is also in
  Mansi XIII, taken for Nicaea II.
- The Anglo-Saxon Chronicle: Plummer I (1892) and Gomme's English (1909) taken. Plummer II (1899), Thorpe (1861),
  Giles and Earle (1889) found, not taken.
- The Annals of Ulster I (Hennessy 1887) taken; only its English can be read. Two more scans and Mac Carthy's
  volumes II-III found, not taken.
- Bede's chronicle: Mommsen (MGH Auctores antiquissimi XIII, 1898) taken. Giles and PL 90 not taken.
- Deusdedit: Wolf von Glanvell (1905) taken. The searcher could not place the abridged acts of 861; the Library
  thread found them at book IV, chapters 428-431. A second scan and Martinucci (1869) not taken.
- Cummian's Easter letter: Ussher's Sylloge (1632) found in two scans; the OCR of both is too poor to read the
  letter. Not taken. PL 87 not tried.
- The Bibliotheca Cluniacensis (1614 and the 1915 reprint): not found again. Berno's testament is held (above).

**Era 4, Byzantine and Greek.**
- Photius: PG 102 (1860) taken, for the books against the Manichaeans, the Mystagogia and the letters. PG 103 and
  104 found, not taken; PG 104 has Peter of Sicily (held) and no Peter the Higumen.
- Peter the Higumen: Gieseler's Appendix (1849) not found, under several spellings and by full text.
- Nicaea II: Mansi XII (Welter 1901) and XIII (Welter 1902) taken. A Google scan of 1767 not checked.
- The Greek Passion of the Mar Saba martyrs: Papadopoulos-Kerameus (1907) not found. archive.org holds the
  Palestinskii sbornik only from 1954.
- Theodore the Studite's other letters: Mai and Cozza, Nova Patrum Bibliotheca VIII (1871) taken, in Latin only.
  Tomus IX not found.
- The Life of Tarasius: PG 98 (1860) taken, in Hervet's Latin. Heikel (1891) not found.
- The Life of Euthymius in readable Greek: two more scans of de Boor (1888) read; both garble the Greek. Not taken.
  A 1970 printing is out by date.
- Kedrenos with Skylitzes II (Bonn 1839), Attaleiates (Bonn 1853), Zonaras III (Bonn 1897) taken. Kedrenos I, PG
  121-122, Pinder's Zonaras I-II, Dindorf's Zonaras and three poorer Attaleiates scans not taken.
- Psellos's accusation of Keroularios: Bréhier in the Revue des études grecques XVI (1903) and XVII (1904), both
  taken. A second scan of XVII not taken.
- The synod of 843: Uspenskii (1893) not found. Montfaucon's Bibliotheca Coisliniana (1715) only lists the
  Synodikon in manuscript entries. Regel and PG 120, named in the leads, were not searched.

**Slavic, Arabic, Armenian.**
- The Life of Constantine: Dümmler and Miklosich (Vienna Denkschriften XIX, 1870) taken; the Latin translation is
  clean, the Slavonic cannot be read. The Italian Legend: Acta Sanctorum, March II (Palmé 1865) taken. Not taken:
  Teodorov-Balan I (1920; the Slavonic is garbled) and II (1934, out by date); Bilbasov (1868; garbled); Leger
  (1868; a study). Not found: a Life of Methodius beyond the held Ginzel, Pastrnek, Lavrov, Fontes rerum
  Bohemicarum I.
- Boris and Gleb: the Uspenskii sbornik in the Chteniia for 1899 found, its Slavonic OCR poor. Not taken.
  Abramovich (1916), Sreznevskii (1860) and Bodianskii (1859) not found.
- Teodosije's Life of Sava: not found. A 2016 translation is in copyright. Chodzko (1858) is Domentijan, held.
  Bašić (1924), named in the leads, was not searched.
- Cosmas the Priest: Kukuljević's Arkiv IV found; the Cyrillic cannot be read and the year is not on the OCR title
  page. Not taken. Popruzhenko not found.
- The Kyiv archive volume (Arkhiv Iugo-Zapadnoi Rossii I.7, 1887): found in two scans. Page 384, the Polish passage
  on Ilarion, is read as Cyrillic look-alike letters and cannot be quoted. Not taken.
- Ibn Hayyan: no edition before 1937. Taken as a later witness: Gayangos's al-Maqqari, volumes I (1840) and II
  (1843), which name Ibn Hayyan on about 140 lines. Dozy's Analectes and Recherches not found; his Histoire des
  Musulmans d'Espagne (1861) found, not read.
- Nerses of Lambron's synodal speech: Aucher (1812) and Neumann (1834) not found.

**Era 5, Byzantine and the councils.**
- Mansi XXII (Lateran IV) and XXIV (Lyon II), both Welter 1903, taken.
- Mansi XX (Clermont): one scan. Its OCR and its page images (leaves n2 to n8, viewed by the Library thread) have
  the half-title and the Venice licence of 1767 but no imprint leaf, so the year of the printing cannot be read.
  The host says 1902. Not taken; for Mark.
- Mansi XXIII (Lyon I): not found again. Taken instead: MGH Constitutiones II (Weiland 1896), with the bull of
  deposition and a report of the council. Huillard-Bréholles VI.1 (1860) found, not taken.
- Pachymeres I (Bonn 1835) and Gregoras I (Bonn 1829) taken. Pachymeres II found, not taken.
- Akropolites: Heisenberg (Teubner) and the Bonn edition (1836) found; the OCR of both is unusable. Not taken.
- Bekkos: PG 141 (the 1882 printing) taken.
- Hefele in English, volumes 4 (1895) and 5 (1896), taken. Hefele-Leclercq V.1 (1912), V.2 (1913) and VI.1 (1914)
  found with readable title pages; not taken, as in the first era 5 pass (a modern historian in three more volumes).
- Petit's Typikon of Pakourianos (1904): not found.

**Era 5, Latin chroniclers and the councils.**
- Clermont: Recueil des historiens des croisades, Historiens occidentaux III (1866: Fulcher, Robert the Monk,
  Raymond, the Gesta Francorum) and IV (1879: Guibert, Baldric, Albert), taken. Krey's English (1921) taken. PL
  151 (1853: Urban II) taken.
- Bernold of Constance: PL 148 has his chronicle, with 1095 at about OCR line 110562, but no year can be read on
  its OCR title page. Not taken.
- Lateran IV: Roger of Wendover, Hewlett II (1887), and Richard of San Germano (Pertz 1864) taken. Coxe's Wendover
  IV (1842) starts at 1216; not taken. Gaudenzi's edition of Richard's first chronicle (1888) found, not taken.
- Peter of Vaux-de-Cernay: Guébin and Lyon I (1926) found; it stops at 1212, before the council. Not taken. Volume
  II (1930) is not on archive.org. The Recueil des historiens des Gaules XIX was seen, not read.
- Lyon II: Friedberg's Corpus iuris canonici II (1881) taken, for the constitutions in the Liber Sextus. "Zelus
  fidei" is not in it. Part I (Gratian, 1879) and Cocquelines's Bullarium III not taken.

**Era 5, monastic, mendicant, beguine.**
- Hadewijch: the 1875 edition taken from dbnl.org (below).
- Walter Daniel: Powicke's offprint of 1922 taken, for the Letter to Maurice and the extracts from the Life. A
  second scan not taken.
- Innocent III: PL 216 (1891 printing) and PL 217 (1890) taken. PL 215 not taken.
- Robert of Molesme: PL 157 (1899 printing) and the Acta Sanctorum, April III (Palmé 1866), taken. The second
  also holds Raymond of Capua's Life of Catherine of Siena, an era 6 want.
- Clare: the Acta Sanctorum, March I, in Palmé's reprint (1865), taken for the four letters to Agnes; Lazzeri's
  edition of the Process (Archivum Franciscanum Historicum XIII, 1920) taken. Not taken: Robinson's article in
  volume III (1910; a study). Not found: Seraphicae legislationis textus originales (1897). Balfour and Fiege, named
  in the leads, were not searched.
- Dominic's process and Humbert's Legenda: Quétif and Échard I (1719) found; it describes the two inquiries and
  does not print them here, and its OCR runs the columns together. Not taken. Palmé's August I was not found among
  the scans fetched.
- Salimbene in Latin: not found. The Italian version (1882) and the German (1914) found, not taken; the 1942 and
  1966 editions are out by date.
- The Metrical Life of Hugh: not searched.

## Hadewijch on dbnl.org

Mark's ruling allows Hadewijch only in the 1875 edition. dbnl's page for that title (text id `hade002werk01_01`)
carries the mark "Auteursrechtvrij", and the notice it links reads: "Het auteursrecht op dit werk is verlopen. Dat
betekent dat het behoort tot het publieke domein. Iedereen mag het vrij hergebruiken voor ieder doel." It asks,
as custom, that the source be named with "geraadpleegd via DBNL (KB, nationale bibliotheek)". So this edition has
its own public-domain statement on the host, which the first era 5 pass did not record. The site's general terms
page was not read. The file is dbnl's keyed text of 2009, 233,630 bytes, equal to the Content-Length dbnl sent. It
holds the poems only.

## Not found or not filled, by want

- Era 4: Ibn Hayyan's own book (a later witness is held); the Greek Passion of the Mar Saba martyrs; Peter the
  Higumen; the Tale of Boris and Gleb; a Slavonic Life of Methodius and any readable Slavonic of either Life; the
  synod of 843; a readable Greek Life of Euthymius; Cummian's letter in a readable scan; Ilarion's consecration in
  the Kyiv archive volume; Mansi XX; Heikel's Greek Life of Tarasius.
- Era 5: Teodosije's Life of Sava; Cosmas the Priest; Nerses of Lambron's speech; Mansi XXIII and the other Lyon I
  constitutions; "Zelus fidei"; Akropolites; Dominic's process and Humbert's Legenda; Clare's Testament and her
  letters in her own Latin; Salimbene's Latin; Peter of Vaux-de-Cernay for 1215; Bernold; Petit's Pakourianos;
  Valdes's profession and the French or Latin Mirror of Simple Souls (not searched again: none was printed before
  1931); Cyril III's own record (not searched again).
- No English before 1931 was looked for where none exists: Theophanes, the Life of Stephen the Younger, Nikephoros,
  Nicholas Mystikos, Peter of Sicily, Ilarion, the trial of Maximus.
