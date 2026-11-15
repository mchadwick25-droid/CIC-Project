# Library search log: era 6 (1300-1517), 2026-11-15

The search record for the Library thread's fill of the era 6 wants: the era 6 rows of `CFT-Wants.md` (Wanted
Sources person rows 99-112 and outside-witness rows 5-9) and the Library wants of Open-Gaps 264, 267 and 271. The
vendored files, their state and their shelves are in `Build/Ministry/Features/Source-Library/CFT-Wants.md` (the
"Era 6, filled" section). This file says where the batch searched, what it found, what it did not find, and what it
did not take.

Rights rule for this batch: only a printed imprint of 1930 or earlier, read on the title page or on the scan's page
image; a reprint counts by its own date; no NC or ND licence, no permission notice, no access-restricted item.

## Hosts

| host | state from this sandbox | used |
|---|---|---|
| archive.org (advancedsearch, metadata, djvu.txt, page images) | reachable | all 27 files |
| dbnl.org | reachable, by the eras 4-5 log | not needed |
| gallica, HathiTrust, books.google downloads, MDZ, documentacatholicaomnia | blocked or broken, by the era 5 log | not tried again |

No host was newly refused by the network proxy. archive.org has no full-text search from here, so every search was
by title, author and year.

## Holdings check, before any search

A whitespace-tolerant grep of the full text of every file in `cic/texts/` for 41 name and title patterns (Joseph of
Volotsk, the Prosvetitel, Savva Chernyi, Euthymius of Tarnovo, Tsamblak, Hilarion of Moglena, Theodosius of Tarnovo,
Stephen of Perm, Epiphanius the Wise, Kirill of Beloozero, Pachomius, Solovki, Teodosije, Zara Yaqob, the Mashafa
Berhan, Perruchon, Ewostatewos, Estifanos, Jakoubek, Margery Kempe, Pomerius, Capistrano, the Vita Gerardi, Rolle's
Psalter, Vetter's Tauler, Gregory of Sinai, Bridget's Life and later books, Ockham, Palamas, Vegio, Petit's
Synodikon, Basel, Rashid al-Din, Ibn Battuta, Ibn Khaldun, Abu'l-Fida, al-Qalqashandi).

Held already, and missed before:
- **Zara Yaqob's chronicle in a usable translation (row 101).** The held Perruchon volume
  (`zara-yaqob_chroniques-zara-yaeqob-baeda-maryam-gez-fra_perruchon1893.txt`) prints a running French translation
  of both chronicles beneath the Ge'ez: Zar'a Ya'eqob from about file line 2922 ("Au nom de la Trinité ...
  j'entreprends de raconter et de décrire toutes les institutions de notre roi"), Ba'eda Maryam from about 8540. Its
  header, registry note and shelf note said no full French translation was in the volume. That was wrong and is
  corrected in this batch. The revolt of the "enfants d'Estifa" (the Stephanites) is told at about file line 6720.
- **Margery Kempe's short treatise (row 103).** Held in
  `cell-of-self-knowledge_seven-early-english-mystical-treatises_gardner1910.txt`, the only part of her Book in
  print by 1930.
- **Abu'l-Fida (outside-witness row 8).** The held `rhc-historiens-orientaux_t1-fra_academie1872.txt` prints a
  "Résumé de l'histoire des croisades tiré des Annales d'Abou'l-Fedâ" in French, from about file line 6059 to about
  23098, and his autobiography from about 23101 to about 24592. The header of that file names only Ibn
  al-Athir.

Held and not enough: Mouravieff for the Russian founders (a later retelling); the Latin Revelations of Bridget, which
end at Book V ("Explicit Quintus Liber", file line 108685); the Philokalia, which holds Gregory of Sinai's works and
no Life; Horstman's Rolle, which cites the Psalter and does not print it.

## Searches, by group

Four searchers ran in parallel (Sonnet), one per group, each held to one helper script for archive.org and to
`rg` and `sed` on the downloads. None stalled. Each pick was then checked by the Library thread: the title page or
its page image, the byte count against the host's record, the wanted passage. Three corrections came out of that
check: the Gibb scan is a 1992 reprint, the journal volume with Ockham's letter is a Johnson reprint, and the
Acta Sanctorum for October X is the Brussels printing of 1861, not the Paris reprint the host names.

**Russian.**
- Joseph of Volotsk: the Great Menaion Reader for 1-13 September (St Petersburg 1868) taken, for the Life under 9
  September and his Dukhovnaia gramota. The OCR does not name Savva Chernyi as the Life's author. The Prosvetitel
  was not found under eight title and author queries, old and new spelling. Nevostruev's Life (1865) not found.
  Seen, not taken: Khrushchov's study of Joseph's writings (1868; a study); "O eresi zhidovstvuiushchikh" (1902;
  new documents on the heresy, not Joseph's text; not read through); the Poslaniia of 1959 (out by date).
- Stephen of Perm: the Life by Epiphanius not found (Druzhinin 1897, Kushelev-Bezborodko 1862). Seen, not taken:
  Krasov's monograph (1896) and the Perm clergy's memorial book (1896), both retellings.
- Kirill of Beloozero: Akty istoricheskie I (1841) taken, for his three letters and his testament. A second scan of
  the same volume not taken. The Life by Pachomius not found (Yablonskii 1908; Nikolskii). Three monastery
  histories (1896, 1897, 1900) were seen and not read.
- Zosima and Savvatii: no printing of the Lives found. Seen, not taken: Sergievskii's retelling (Moscow 1897), which
  says it follows the Menaion text; Dosifei's description of the monastery (the host says 1834; the OCR year is
  unclear) and its third part of documents (1836); Meletii (1881, not read). The April volume of the Great Menaion
  is not on archive.org.
- The rejection of Florence: the Akty volume holds the letter of Vasilii II to the patriarch and Metropolitan
  Jonah's letters naming Isidore. Popov (1875) and Pavlov (1878), with Simeon of Suzdal's account, not found.
  Pierling (1912), a study, not taken.

**South Slavic and Greek East.**
- Euthymius of Tarnovo: Kałużniacki's Werke (Vienna 1901) taken. The OCR was run with a Cyrillic model: the
  Slavonic can be followed, the German cannot be read, so the title page was read on the image. No second scan.
- Tsamblak's Praise of Euthymius: the only scan of Kałużniacki's "Aus der panegyrischen Litteratur der Südslaven"
  is the Variorum reprint of 1971. Not taken.
- Theodosius of Tarnovo (Kallistos's Life): not found. The Sbornik za narodni umotvoreniia is on archive.org for
  1901 only; the Chteniia for 1860 is not there.
- Teodosije's Life of Sava: not found again (fourteen queries; Daničić 1860, Bašić 1924).
- Kallistos's Life of Gregory of Sinai (Pomialovskii 1894): not found.
- Palamas's letter from captivity: Neos Hellenomnemon and the Deltion are not on archive.org under any spelling
  tried. The full Triads were first printed in 1959.
- Petit's article on the Synodikon of Thessalonica: Échos d'Orient volume 18 is not on archive.org (volumes 6, 10,
  12, 14-17 and 19 are).
- Basel: Mansi 29 and 30 (Welter 1904) taken. The year of tome 29 was read on the page image.

**Latin West.**
- Jakoubek of Stříbro: von der Hardt, tomus III (1698), taken; it prints his Demonstratio of 1415 inside Mauritius
  of Prague's reply. A second scan of the same tome and seven scans of other tomes not taken.
- Pomerius: Analecta Bollandiana 4 (1885) taken. A second scan with poorer OCR not taken.
- John of Capistrano: Acta Sanctorum, October X (Brussels 1861), taken, with Nicholas of Fara's Life and two more.
- Kempis's Life of Gerard Groote in Latin: Pohl's volume 7 (1922) is not on archive.org. Two older printings of the
  Opera omnia (1615; Amort 1728) hold the Life, but their OCR at that place is too poor to check a name. Not taken.
- Rolle's English Psalter: Bramley (Oxford 1884) taken. Two more scans of it not taken.
- Tauler: Vetter (1910) is not on archive.org. Naumann's selection after Vetter (Bonn 1914) taken. Corin's French
  (1924) and Naumann's 1933 volume not taken.
- Maffeo Vegio's Life of Bernardino: Acta Sanctorum, May V (Palmé 1866), taken.
- Bridget: the second volume of the held edition (Rome 1628), with Books VI-VIII, taken; the Life by her two
  confessors in Scriptores rerum Suecicarum III (Uppsala 1871-76) taken. The Acta Sanctorum for October IV (Palmé
  1866) was read and not taken: it prints Birger's and Berthold's Lives, not the confessors'.
- Ockham: Birch's De sacramento altaris (1930) taken. His letter to the chapter at Assisi (Müller, Zeitschrift für
  Kirchengeschichte 6, 1884, pages 108-112) is on archive.org only in a Johnson Reprint, so it was not taken; the
  letter was read there at about OCR lines 6112-6358. Brampton's edition (1929) was seen and not checked.
- A witness to the burning of Wyclif's bones: not found. The Fasciculi zizaniorum (1858) has no such passage.

**Ethiopian, Arabic and Persian.**
- Zara Yaqob's own books: Dillmann (1884) not found. The only Mashafa Berhan on archive.org is the edition of 1964.
- Ewostatewos: Turaev (1905, 1906) not found. A Latin edition of 1955 is out by date.
- Estifanos: nothing printed by 1930 was found. The king's chronicle, held, tells the revolt from the court's side.
- Rashid al-Din: Quatremère (1836) not found; Blochet (1911) and the undated Persian scans cannot be read.
- Ibn Battuta: Defrémery and Sanguinetti, volumes 1-4 (1853-58), taken. Gibb's English: the scan with a 1929 title
  is the Asian Educational Services reprint of 1992; another is a 1939 impression; a third carries a CC BY-NC-ND
  licence. None taken. Lee's English (1829) found, not read.
- Ibn Khaldun: de Slane's Prolégomènes, parts 1-3 (1863-68), and his Histoire des Berbères, volumes 1-4 (1852-56),
  taken. Other scans of both not taken.
- Abu'l-Fida: held (above). Reiske's Annales Muslemici, five volumes (1789-94), found, not read and not taken.
- al-Qalqashandi: Wüstenfeld (1879) and Gaudefroy-Demombynes (1923) taken.

## Imprints read on the page image

Where the OCR title page gave no year, the Library thread viewed the leaf: Euthymius (leaf n7), Mansi 29 (n7),
Ibn Battuta 1 (n6) and 4 (n2), Histoire des Berbères 1 (n6), Gaudefroy-Demombynes (n8), von der Hardt III (n2),
Acta Sanctorum October X (n10), Bridget volume II (n4), Scriptores rerum Suecicarum III (n6).

## Not found or not filled, by want

- Rows 99-112: the Prosvetitel; the Lives of Stephen of Perm, Kirill of Beloozero, and Zosima and Savvatii;
  Tsamblak's Praise of Euthymius; the Life of Theodosius of Tarnovo; Zara Yaqob's own books; the Gadla
  Ewostatewos; the Acts of Estifanos; the full Book of Margery Kempe (first printed 1936 and 1940).
- Outside witnesses: Rashid al-Din.
- Open-Gaps 264 and 267: Kempis's Latin Life of Gerard in a readable print; Vetter's full Tauler; Kallistos's Life
  of Gregory of Sinai; Ockham's letter in a printing of its own date; Palamas's letter from captivity and the
  full Triads; Petit's article. Colledge and McGinn is in copyright and was not searched.
- Open-Gaps 271: a roll of Basel's members, a signed list for Haec sancta, a witness to the burning of Wyclif's
  bones, Luther at Leipzig, and the Coptic, Ethiopian and Armenian texts were not searched in this batch.
