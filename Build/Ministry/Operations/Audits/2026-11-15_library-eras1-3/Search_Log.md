# Library search log: eras 1-3 (70-622), 2026-11-15

The search record for the Library thread's eras 1-3 batch. The wants are the eras 1-3 rows of
`2026-11-12_wanted-sources-combined/Wanted_Sources.md`: person rows 1-13, council rows 1-8, and Library-label
correction 19 (the missing page of the held Lactantius). The vendored files, their state and their shelves are
recorded in `Build/Ministry/Features/Source-Library/CFT-Wants.md` (eras 1-3 section). This file says where the
batch searched, in which languages, and what it found, did not find, or did not take.

Rights rule for this batch: only a printed imprint of 1930 or earlier, read on the title page; a reprint counts
by its own date; no NC or ND licence, no permission notice, no access-restricted item.

## Hosts

| host | state from this sandbox | used |
|---|---|---|
| archive.org (advancedsearch, metadata, djvu.txt, page images) | reachable | every file came from here |
| gallica, HathiTrust, books.google downloads, MDZ, documentacatholicaomnia | blocked or broken, by the era 5 log | not tried again |

No host was newly refused by the network proxy.

## Holdings check, before any search

A whitespace-tolerant grep of the full text of all files in `cic/texts/` for each want (Letter to Flora,
Malchion and the Samosata fragments, Peri Pascha, Agathangelos, Kephalaia, Shabuhragan, Fihrist, Shushanik in
six spellings, Kalankatuatsi and Aghuen, Vita Sabae, Simocatta, Malalas, Ezana, Maron, Historia religiosa,
Tyconius, Apollinaris and the Roman synod, Dvin, Menas and Anthimus), and a read of `REGISTRY.yaml`.

Held already:
- **John Malalas (row 12).** The whole Chronographia is in the held PG 97 file, from about OCR line 6696 to book
  XVIII at about 62320. The Latin is readable; the Greek OCR is poor. It had no shelf row; it has one now.
- **The Roman synod against Apollinaris (council 1).** Mansi III, held, prints the notice of the synod ("Concilium
  Romanum III, in quo Apollinaristarum haeresis damnata") at about file line 47669. No acts survive; Damasus's
  letters are in Theodoret (NPNF 2.3, held).
- **The Donatist council against Tyconius (council 2).** No acts survive. The one witness is Augustine, Contra
  epistolam Parmeniani I.1, in the held PL 43 file from about file line 1340.
- **The Maronite tradition's own account (row 5).** Duwayhi's history is held twice in Arabic (Shartuni's edition),
  both poor scans.
- Held and not enough: Otto's and Routh's fragments of Melito (not the homily); Holl's second Epiphanius volume
  (haer. 34-64, so not Panarion 33); Langlois tome 2 (Agathangelos is in tome 1); Cotelier tomus II (the Life of
  Euthymius, not Sabas); Brosset's Georgian history, which only mentions Shushanik in passing.

## Searches, by want

Three searchers ran in parallel (Sonnet), one per group. Each pick was then downloaded again by the Library
thread and checked: host record, title page, byte count, the wanted passage, the volume's end.

**Era 1 (German, French, English, Latin, Greek).**
- Mani (row 1): the editions the audit named (the Cologne Codex 1988, the Kephalaia 1940, the Psalm-Book 1938) are
  in copyright. Taken: Flügel 1862 (the Fihrist on Mani, Arabic and German); Sachau's al-Biruni 1879 (quotes the
  Shabuhragan); Le Coq, Türkische Manichaica I, in the Prussian Academy's Abhandlungen for 1911; Chavannes and
  Pelliot, Un traité manichéen retrouvé en Chine, in the Journal asiatique for 1911 and 1913; Le Coq's English
  Khuastuanift in the Journal of the Royal Asiatic Society for 1911. Not found: F. W. K. Müller,
  Handschriften-Reste II (1904); the Abhandlungen volume for 1904 lists it but does not print it. Found, not
  taken: Alfaric, Les écritures manichéennes (1918, a study); Le Coq's Chotscho (plates only).
- Melito (row 2): no edition of the Peri Pascha before 1931 exists; the homily was first printed by Bonner in 1940.
  archive.org has Bonner 1940 and Perler 1966, both after the date rule. Not taken.
- Ptolemy (row 3): Holl's Epiphanius I (GCS 25, 1915) taken. Harnack's Brief an die Flora (1904) found, not taken:
  its title-page OCR is unreadable and Holl prints the same letter.
- Paul of Samosata (row 4): Loofs 1924 and Bardy 1923 (first edition) taken. Routh III and Lawlor's article not
  searched further once both were found.
- Lactantius, correction 19: a second scan of CSEL 19 (item corpusscriptorum0019vari) has page 411 and was taken.
  A third scan (operaomnia01lact) also has it, with double-spaced OCR; not taken.

**Armenia, Georgia, Albania, Aksum, the Maronites (French, German, Russian, Latin, Italian, Armenian, Georgian,
Arabic, English).**
- Gregory the Illuminator (row 6): Langlois, Collection, tome I (1867) taken, in a scan that binds tomes I and II;
  Lagarde's Greek Agathangelos (1887) taken. The Italian Storia di Agatangelo (Venice 1843) found, not taken.
  Thomson 1976 is in copyright.
- Ezana (row 7): Littmann, Deutsche Aksum-Expedition IV (1913) and Budge, History of Ethiopia I (1928) taken.
  A second Budge scan carries "dc.rights: not available" and was not used; a 1966 reprint is out by date. Müller
  1894 and Bent 1893 found, not taken. A second Littmann scan reads "for use in library only" (a shelf note).
- Shushanik (row 8): not found in a usable text. Lang 1956 is in copyright and Peeters's Latin is 1935. The
  Armenian version (Sopʻerkʻ haykakankʻ 9, Venice 1853) is on archive.org, but its OCR is unreadable and it is a
  different recension from Iakob's Georgian; not taken. Sabinin 1882, Gorgadze 1917 and Malan 1866 were searched in
  Latin, Cyrillic and Georgian script and not found.
- Vachagan and Movses Daskhurantsi (rows 9, 10; council 4): Manandian's Beiträge zur albanischen Geschichte (1897)
  taken; it translates the canons of Aghuen (I.26) and other chapters into German. The whole History was not found
  before 1931: Patkanov's Russian (1861), Emin's and Shahnazarian's Armenian (1860) are not on archive.org. Dowsett
  1961 and the later editions are in copyright.
- The councils of Dvin (councils 5, 7, 8): Ter-Minassiantz (Texte und Untersuchungen 26.4, 1904), which translates
  letters from the Book of Letters, and Brosset's Deux historiens arméniens (1870), which has Ukhtanes on the
  break with the Georgians, taken. The Book of Letters itself (Girkʻ Tʻghtʻotsʻ, Tiflis 1901) is on archive.org,
  dated from the page image, but its Armenian OCR has no usable lines; not taken. Ter-Mikelian 1892 found, not taken.
- Maron (row 5): Migne PG 82 (Theodoret, with the Historia religiosa; 1864) taken. The Maronites' own account:
  Nau's Opuscules maronites, both parts (1899, 1900), and Naironus's Dissertatio (Rome 1679) taken. A second Nau
  scan is flagged for lending only and was not used. Dib 1930 not found (only a 1962 English version). Gutberlet's
  German Theodoret (1926) was searched by title and not found.

**Byzantine and the councils (Latin, Greek, German, French, Russian, English).**
- Sabas (row 11): no readable Greek Life was found. The one scan of Cotelier's tomus III is the unusable one;
  Pomialovskii 1890 is not on archive.org; Schwartz 1939 is out by date. Taken: the Latin Life in Surius's December
  volume (Turin 1880), whose own heading says it may be Metaphrastes's paraphrase of Cyril.
- Malalas (row 12): held (above). Dindorf's Bonn edition (1831) taken as well, for its better Greek. Three other
  Dindorf scans had poorer Greek.
- Theophylact Simocatta (row 13): Bekker's Bonn edition (1834, Greek and Latin) taken. De Boor 1887 found in two
  scans, not taken: the OCR turns the Latin title page into Greek letters, so the year could not be read from the
  text. Two more Bekker scans and one garbled scan not taken.
- Constantinople 536 (council 6): Mansi VIII in the Welter facsimile (1901) taken; the acts run from about OCR
  line 90500 to about 116790.
- Beth Lapat 484 (council 3): nothing beyond the held Chabot and Braun. The acts were annulled and are lost. The
  Chronicle of Seert (Patrologia Orientalis 7) summarises a letter of Barsauma; grepped only, not taken.

## Not found or not filled, by want

- Melito, Peri Pascha (row 2): no public-domain edition can exist before 1940.
- Iakob Tsurtaveli, Martyrdom of Shushanik (row 8).
- Movses Daskhurantsi's whole History (row 10): only Manandian's chapters.
- Cyril of Scythopolis, Vita Sabae in Greek (row 11): a Latin Life only, possibly the paraphrase.
- F. W. K. Müller's Turfan fragments (row 1); the Armenian Book of Letters in a readable scan (councils 5, 7, 8).
- The synod of Beth Lapat (council 3): none survives.
