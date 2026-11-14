# Library search log: era 5 (1054-1300), 2026-11-13

The search record for the Library thread's era 5 batch. The wants are the era 5 rows of
`2026-11-12_wanted-sources-combined/Wanted_Sources.md`: person rows 55-98, outside-witness rows 1-4, council
rows 16-19. The vendored files, their state and their shelves are recorded in
`Build/Ministry/Features/Source-Library/CFT-Wants.md` (era 5 section). This file says where the batch searched,
in which languages, and what it found, did not find, or could not reach.

## Hosts

| host | state from this sandbox | used |
|---|---|---|
| archive.org (advancedsearch, metadata, djvu.txt, page images, full-text search) | reachable | every file came from here |
| dmgh.de (MGH) | reachable, but a page-image viewer only; no text or PDF endpoint | no |
| dbnl.org | reachable | Hadewijch's Dutch editions found; not vendored (rights, see below) |
| gallica.bnf.fr | blocked by the site's browser check (HTTP 403) | no |
| HathiTrust (catalog and babel) | blocked by the site's browser check (HTTP 403) | no |
| books.google.com | downloads refused from this host (batch 4) | no |
| documentacatholicaomnia.eu | pointer only; its certificate chain also fails against the sandbox's CA bundle | no |
| digitale-sammlungen.de (MDZ) | API refused (HTTP 403); the search page is a script shell with no hits | no |

## Holdings check, before any search

A whitespace-tolerant grep of the first lines of all 1,700 files in `cic/texts/` and of the full text for 45
title and name patterns (Gesta Innocentii, Exordium Parvum, Vita Norberti, Libellus de principiis, Magna Vita,
Alexiad, Panoplia dogmatica, Benjamin of Tudela, Ibn Jubayr, Sacconi, Salimbene, Domentijan, Typikon and the
rest), and a read of `cic/texts/REGISTRY.yaml`. Almost no want was held. Held and relevant: the Primary
Chronicle (Cross 1930, PSRL I) and Abramovich's Paterik, which prints Nestor's Life of Theodosius; Peeters in
Analecta Bollandiana 36-37, which prints the Life of George the Hagiorite; Evans 1899 (the Mirror of Perfection);
Yule-Cordier's Cathay and the Way Thither; Mansi XIV-XVIII.

## Searches, by want

Five searchers ran in parallel (Sonnet), one per language and topic group; each pick was then re-downloaded
and re-read by the Library thread (record, title page, byte count). Languages searched are given per group.

**Latin church and councils (Latin, Old French, French, German, English, Armenian).**
- Innocent III: Migne PL 214-217 found; PL 214 taken (the Gesta and the Registers, book I). Baluze (1682),
  Hurter (Fraktur) also found, not taken. Powell 2004 is in copyright.
- Anselm and Eadmer: PL 158 and 159 taken. Schmitt and Southern are in copyright.
- Becket: PL 190 taken (the Lives and the letters). The Rolls Series 67 (seven volumes) found, not taken
  (title pages unchecked). Duggan and Staunton are in copyright.
- Abelard: PL 178 taken. Bellows's English (Gutenberg 14268) has no printed year. Cousin 1849 also found.
- Adam of Bremen: Schmeidler 1917 and Steinberg 1926 (German) taken. Waitz 1876 found. Laurent 1893 is
  garbled Fraktur. Tschan 1959 is in copyright.
- William of Tyre: RHC Occidentaux I, both parts, taken. PL 201 also found. Paulin Paris's French (1879-80)
  found, not taken. Babcock and Krey 1943 is in copyright.
- Jacques de Vitry: the Douai Historia (1597) and Röhricht's edition of the letters (1894) taken. Bongars
  (1611) and the Sermones found, not taken. Huygens and Donnadieu are in copyright.
- Councils: Mansi XXI taken (Troyes). The Council of Jerusalem has no acts; William of Tyre is its witness.
  Mansi XXIII (Lyon I) is not on archive.org; Matthew Paris IV (Rolls 57) taken for the narrative. Hefele-
  Leclercq V.2 (1913) found, not taken (a modern historian). Nerses of Lambron's speech (Hromkla) not found.

**Cistercians, Carthusians, canons, Templars (Latin, French, German, English).**
- Bernard and William of St Thierry: PL 182, 183 and 185 taken, with Eales's English in four volumes (Mabillon's
  text). PL 180 and 184 found, not taken. Matarasso 1993 is in copyright.
- Citeaux founders: PL 166 taken (Charta, Usus, Exordium, Harding's Bible letter). The French "Le petit et le
  grand exorde" (1884) found, not taken. Guignard, Nomasticon (1892) and Janauschek not found; Waddell 1999 is
  in copyright. A Life of Robert of Molesme was not found.
- Bruno: Le Couteulx's Annals I (1887) and PL 152 taken; PL 153 (Guigo) not taken. Lettres des premiers
  Chartreux is in copyright.
- Aelred: PL 195 taken. Walter Daniel's Life: not found (see below).
- Hugh of Lincoln and Adam of Eynsham: the Magna Vita (Rolls 37, Dimock 1864) taken. Giraldus's Life of Hugh
  (Rolls 7) found, not taken. The Metrical Life not found. Douie and Farmer is in copyright.
- Norbert: PL 170 taken. MGH SS 12 is on dmgh.de as page images only. Acta Sanctorum June I found, not taken.
  Le Paige not found. Antry and Neel 2007 is in copyright.
- Templars: Curzon 1886 and the Latin Rule edition of 1903 taken. Upton-Ward and Barber and Bate are in copyright.

**Mendicants, heresy, beguines (Latin, Italian, French, German, Dutch, Middle English, English).**
- Celano: d'Alençon 1906 (Latin, all three works) and Howell 1908 taken. Analecta Franciscana X is in copyright.
- Clare: Robinson 1910 taken. Not found: the Letters to Agnes, the Testament, the Process.
- Leo: Lemmens 1901 and Sabatier 1898 (Latin Speculum) taken. Salter's Three Companions found, not taken.
- Agnes of Prague: Seton 1915 taken.
- Dominicans: Gerard de Frachet (Reichert 1896; Conway 1924), Altaner 1925, Humbert (Berthier 1888-89), Jordan's
  Libellus in the Acta Sanctorum (August I) taken. MOPH acta capitulorum and Quétif-Échard found, not taken.
  Not found: Dominic's Process, Humbert's Legenda. MOPH XV-XVI and Scheeben are in copyright.
- Aquinas: the Leonine Summa tomi 4-12 and Tocco in the Acta Sanctorum (March I) taken. The English Dominican
  Province volumes were found; only one title page was verified, so none was taken.
- Joachim: Buonaiuti 1930 and the Acta Sanctorum (May VI) taken. The Venice 1519 and 1527 scans are garbled and
  carry publisher notices. Psalterium decem chordarum not found.
- Valdes: Stephen of Bourbon (Lecoy de la Marche 1877) and Döllinger II (1890) taken. Walter Map (Wright 1850,
  James 1914, James's English 1923) found, not taken. The Profession of 1180 not found separately.
- Rainerius: Martène-Durand V taken. Moneta (Ricchini 1743) found, not taken. Dondaine 1946 is in copyright.
- Salimbene: Coulton 1907 taken. The Latin (MGH SS 32) is on dmgh.de as page images only. A German translation
  (Doren 1914) has garbled OCR. An Italian version of 1882 was found, its translator not verified. The Bernini
  Cronica (Bari 1942) carries a Public Domain Mark on its record but a 1942 imprint, and was not taken.
- Hadewijch: the Dutch editions (1875, 1895, 1924-25) are on dbnl.org, not archive.org. dbnl gives no per-item
  licence and warns that books under 140 years old may be protected. Not taken; held for Mark.
- Marie d'Oignies: Acta Sanctorum June V taken. Mulder-Bakker 2006 is in copyright.
- Porete: Kirchberger 1927 (Middle English Mirror) and Langlois 1894 (Revue historique 54) taken. Lea II found,
  not taken (a history). No Old French or Latin Mirror in public-domain print. Guarnieri 1965 and Babinsky 1993
  are in copyright.

**Byzantine, Slavic, Georgian (Greek, Church Slavonic, Serbian, Czech, Georgian, Russian, French, Latin).**
- Domentijan: Daničić 1865 taken. Safarik (garbled), Chodzko's French (1858, from an abridged edition) found,
  not taken. Teodosije (Daničić 1860), the Typika and Ćorović 1928 not found.
- Anna Komnene: Reifferscheid 1884 taken. Dawes 1928 found as a transcription on archive.org with a
  non-commercial-use notice; not taken, held for Mark. Schopen's Bonn volume (Latin, garbled Greek) and PG 131
  found, not taken. Sewter, Leib 1937 are in copyright or post-1930.
- Zigabenos: Gieseler 1842 taken. PG 130 found, not taken. Cosmas the Priest: no public-domain Slavonic edition
  found; Popruzhenko 1907 is not on archive.org.
- Pakourianos: Mousaios 1890 (in Commentationes philologae Ienenses IV) taken. Petit 1904 not found.
- Nestor and George the Hagiorite: already held (see CFT-Wants).

**Arabic, Hebrew, Coptic, travellers (Arabic, Hebrew, Latin, French, German, Italian, English).**
- Marco Polo: Yule-Cordier 1903, both volumes, taken. Moule and Pelliot is in copyright. Pauthier, Marsden,
  Neumann found, not taken.
- Cyril III ibn Laqlaq: his own continuation is only in Atiya et al. (in copyright). Renaudot 1713 taken as a later
  Latin witness. Riedel 1900 (his canons, listed not printed) and Vansleb 1677 found, not taken.
- Ibn al-Athir: RHC Historiens orientaux I and II.1 (French) taken. Tornberg's Arabic found; vol. 10
  downloaded, OCR fair to garbled, not taken. Richards 2006 is in copyright.
- Usama: Hitti 1929 taken. Schumann 1905 (German) found, not taken. Derenbourg not found. Later translations are in
  copyright.
- Ibn Jubayr: Wright's Arabic text (1852) taken. De Goeje's 1907 revision survives as a 1949 facsimile reprint
  (rights unclear) and was not taken. Amari 1880 (Sicily only) found, not taken. Broadhurst 1952 is in copyright.
- Benjamin of Tudela: Adler 1907 taken. Asher 1840, Grünhut-Adler and Wright 1848 found, not taken.

## Not found, by want

- Teodosije's Life of Sava (row 92); Cosmas the Priest's Sermon (row 89, context).
- Walter Daniel's Life of Ailred (row 70); a Life of Robert of Molesme (row 58); the Metrical Life of Hugh.
- Clare's Letters, Testament and Process (row 61); Dominic's Process (row 62); Humbert's Legenda (row 97).
- Waldo's Profession of 1180 as a separate public-domain text (row 65); the Old French and Latin Mirror (row 75).
- Hadewijch (row 73) and Anna Komnene's English (row 88): found but held for rights.
- Cyril III ibn Laqlaq's own text (row 93).
- Councils: Lyon I decree text (Mansi XXIII); Hromkla's acts and Nerses of Lambron's speech.
