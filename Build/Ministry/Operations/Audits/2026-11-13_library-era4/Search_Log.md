# Library search log: era 4 (622-1054), 2026-11-13

The search record for the Library thread's era 4 batch. The wants are the era 4 rows of
`2026-11-12_wanted-sources-combined/Wanted_Sources.md` (person rows 14-54, council rows 9-15). The
vendored files, their state and their shelves are recorded in
`Build/Ministry/Features/Source-Library/CFT-Wants.md` (era 4 section). This file says where the batch
searched, in which languages, and what it found, did not find, or could not reach.

## Hosts

| host | state from this sandbox | used |
|---|---|---|
| archive.org (advancedsearch, metadata, djvu.txt, page images) | reachable | every file came from here |
| dmgh.de (MGH) | reachable | not needed: the MGH texts wanted were found on archive.org |
| gallica.bnf.fr | blocked by the site's browser check (HTTP 403) | no |
| HathiTrust (catalog and babel) | blocked by the site's browser check (HTTP 403) | no |
| books.google.com | page reachable, downloads refused from this host (batch 4) | no |
| documentacatholicaomnia.eu | TLS certificate chain fails against the sandbox's CA bundle | no |
| e-rara.ch | reachable | not searched |

## Holdings check, before any search

A whitespace-tolerant grep of all 1,649 files in `cic/texts/` for 36 title and name patterns (Vita
Anskarii, Historia abbatum, Íslendingabók, Memoriale sanctorum, Muqtabis, Asoghik, Ishoyahb,
Khandzta, Iviron and the rest), and of file names. No want was held. The hits were mentions or
namesakes: Mouravieff's retelling of the Caves founders and of Boris and Gleb; the Cluny Recueil
(held) cites Berno's testament by incipit only; Sathas III is held, IV is not; Nikephoros Kallistos
(PG 147) is a namesake trap for Patriarch Nikephoros I.

## Searches, by want

Four searchers ran in parallel (Sonnet), one per language group; each pick was then re-read by
the Library thread (record, title page, byte count). Languages searched are given per group.

**Greek and Byzantine (Greek, Latin, German, Russian).**
- John of Damascus, Life by John of Jerusalem: PG 94 found.
- Theodore the Studite (Life by Michael the Monk, Letters, Antirrhetici): PG 99 found.
- Stephen the Younger; Nikephoros I: PG 100 found. De Boor's Nicephori opuscula (1880) found in two
  scans; both garble the Greek, so PG 100 was taken.
- Theophanes: PG 108 taken. De Boor's Teubner edition (1883-85) and the Bonn edition (1839-41) also
  found, not vendored.
- Nicholas I Mystikos: PG 111 and de Boor's Vita Euthymii (1888) found.
- Michael Keroularios: Will, Acta et scripta (1861) and Sathas IV (1874) found.
- Paulicians: Gieseler's Peter of Sicily (1846) taken. PG 104 also has it. Theophanes Continuatus:
  PG 109 taken; Bekker's Bonn edition (1838) also found. Peter the Higumen as a separate text: not
  found.
- Clement of Ohrid: PG 126 found. Not found: Miklosich, Vita S. Clementis (1847); Tunitskii (1918);
  Snegarov.
- Stephen Mansur: Acta Sanctorum, March III (1865) found. Not found: Papadopoulos-Kerameus,
  Pravoslavnyi Palestinskii Sbornik 57 (1907).
- Theodore Abu Qurrah: PG 97 and Graf (1910) found. Not found: Bacha (1904). Not taken: an upload
  that may be Graf, with a CC BY 3.0 licence on its record (`Abu-qurrahGermanTranslation`).
- Councils: Mansi XII-XVII (Welter facsimile, 1901-02) all found. XIV-XVII taken for the councils of
  852-880. Hefele's English (Clark) stops at 787. Hefele-Leclercq III and IV (1909-11) found, not
  vendored.

**Slavic (Church Slavonic, Russian, Ukrainian, Czech, German, Latin).**
- Cyril and Methodius: Ginzel (1861) taken, for the Latin Life of Methodius and John VIII's letters.
  Bodianskii's Slavonic collection (1862) found, but its OCR is garbled. Goetz (1897) is a study.
  Not found: Pastrnek (1902), Lavrov (1930), Miklosich's Vita S. Methodii (1870), MGH Epistolae VII.
  Not taken: Kantor (1983), which is in copyright. No Slavonic Life of Constantine with usable OCR
  was found.
- Kievan Caves Paterik: Abramovich (1911) taken. Abramovich's Kyiv edition carries both 1930 and
  1931 on its title pages, so its public-domain status is doubtful, and it was not taken. Viktorova
  (1870) has garbled OCR. Heppell (1989) is in copyright.
- Boris and Gleb: the Primary Chronicle s.a. 6523, in Cross (1930) and PSRL I (1926). Not found:
  Abramovich (1916), Sreznevskii (1860). The Jagiellonian manuscript scan (CC0) has garbled OCR.
  Kantor and Hollingsworth are in copyright.
- Ilarion: the Moscow 1844 printing taken. Franklin (1991) is in copyright.
- Primary Chronicle: Cross (1930) and PSRL I (1926) taken. Also found: the 1846 PSRL (fair OCR) and
  Miklosich (1860, garbled). Not taken, in copyright: Cross and Sherbowitz-Wetzor (1953) and the
  1973 printing. Also not taken: a 2026 synthetic narration upload.

**Latin West (Latin, Old English, Old Norse, English, German).**
- Anskar and Rimbert: Robinson (1921) and Waitz (1884) taken.
- Alfred: Sweet's Pastoral Care (1871) taken; a second scan of part I was not taken.
- Asser: Stevenson (1904) and Cook (1906) taken. Jane (1908) and Giles (1848) also found.
- Dunstan: Stubbs (1874) taken.
- Æthelwold:
  - Ælfric's Life, in the Abingdon Chronicle II (1858): taken.
  - The Life in PL 137: taken.
  - The Regularis Concordia: Logeman, Anglia 13 (1891), taken. Reyner (1626) found, but its OCR is
    poor. Symons (1953) and Lapidge-Winterbottom (1991) are in copyright.
- Oswald: Raine, Historians of York I (1879) taken.
- Biscop and Ceolfrid: Plummer (1896) and Wilcock (1910) taken. Not taken: King's Loeb Bede (1930),
  whose record reads "Permission Granted to Digitize". Its rights field does not settle its status.
- Þorgeir and the Althing: Origines Islandicae I (1905) taken. Also found: Golther (1892), Finnur
  Jónsson (1930), the Reykjavík 1909 printing, and Kahle's Kristni saga (1905). Not found:
  Hermannsson's Book of the Icelanders (1930). Grønlie (2006) is in copyright.
- Benedict of Aniane: PL 103 taken.
- Eulogius, Alvarus, Flora and Maria: PL 115 and PL 121 taken. Not searched: Flórez, España
  Sagrada. Gil (1973) and Wolf (2019) are in copyright.
- Berno: the Bibliotheca Cluniacensis (1614) was not found. PL 133 does not print the testament.
  The held Cluny Recueil gives only its incipit.
- Odo and Gerald: PL 133 and Swoboda's Occupatio (1900) taken.
- Odilo: PL 142 taken. His All Souls decree is inside Jotsald's Life. No separate Statutum was
  found.

**Arabic, Armenian, Syriac, Georgian (and Latin, French, German, Russian versions).**
- al-Tabari: de Goeje, prima series IV and V, taken. Also found: prima III, VI, the Introductio and
  Indices, and Zotenberg's French of Bal'ami (1867-74). Zotenberg is a Persian adaptation, not al-Tabari's text.
  Nöldeke (1879) was found. The SUNY translation is in copyright.
- Ibn Ishaq: Weil (1864, German) and Wüstenfeld's Arabic, part 1 (1858), taken. Guillaume (1955)
  is in copyright.
- Ibn Hayyan, al-Muqtabis: not found. Antuña's edition (1937) is too late. Dozy cites it only by
  manuscript folio.
- Stepanos of Taron: Gelzer and Burckhardt (1907) and Macler (1917) taken. Not found: Dulaurier
  (1883), Malkhasean (1885). The 1854 Armenian scan has garbled OCR; the 2010 Antelias edition is in
  copyright. Greenwood (2017) is in copyright.
- Ishoyahb III: Duval's Latin version (CSCO, 1905) taken. Not taken: the Syriac volume, whose OCR is
  garbled. The 1955 Louvain item is restricted and in copyright.
- Grigol of Khandzta, and John and Euthymius: Peeters, Analecta Bollandiana 36-37 (1917-19), taken.
  Not found: Marr (1911).
- Council of Dvin (719): Aucher's John of Odzun (1834) taken. Hefele-Leclercq III has no Dvin 719.

## Not found, by want

- Ibn Hayyan (row 36).
- Berno's testament in full (row 32).
- A Slavonic Life of Constantine and Life of Methodius with usable OCR (row 17). The Latin Life of
  Methodius is held.
- The Greek Life of Clement in a pre-1931 edition other than Migne (row 39). PG 126 is held.
- Mansur's Greek Passion (row 51). The Latin Acts in the Acta Sanctorum are held.
- Peter the Higumen (rows 42-43).
- Councils: the synod of 843 was not confirmed in Mansi XIV. The Althing (council row 15) has only
  Ari's account, written after the event. That account is held.
