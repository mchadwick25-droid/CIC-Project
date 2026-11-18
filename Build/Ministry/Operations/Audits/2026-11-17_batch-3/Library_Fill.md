# Library fill, batch 3 (2026-11-17): the Pachomius gaps and the Xi'an stele

Mark's ruling of 2026-11-17: "fill the Pachomius gaps, keep him in the batch". Five files vendored under
`cic/texts/INTAKE.md`, steps 1 to 9. The vendored files, their state and their shelves are also in
`Build/Ministry/Features/Source-Library/CFT-Wants.md` ("Batch 3 fill (2026-11-17)").

Rights rule for this batch: only a printed imprint of 1930 or earlier, read on the title page; no scan with a notice
against reproduction; no NC or ND licence; no lending-only item.

## Hosts

| host | state from this sandbox | used |
|---|---|---|
| archive.org (advancedsearch, metadata API, djvu.txt, PDF page images) | reachable | all five files |
| gallica, HathiTrust, books.google downloads, MDZ | not tried: archive.org held every target but one, and the one it lacks is not on those hosts either by the earlier logs | none |

No host was refused by the network proxy. TLS verification was not disabled.

## Holdings check, before any search

`ls cic/texts` for pachom, acta, migne, patrol, legge, nestor, amelin, ladeuze, jerome, regula. Held already and not
duplicated: `acta-sanctorum_maii-tomus-5-lat_palme1866.txt` and `acta-sanctorum_maii-tomus-6-lat_1739.txt`
(neither is the volume wanted, May III); `pachomius_rules-ethiopic_schodde1885.txt` (the Ethiopic Rule only).
No Patrologia Latina 23 file was held (PL 22 is not held either). No Amélineau, Legge or Ladeuze file was held.
`WORKS.yaml` has no entry for Pachomius, the Rule, or the Xi'an stele, so no WORKS expression was added.

## Targets

### 1. Amélineau, Histoire de saint Pakhôme (Annales du Musée Guimet 17, 1889): vendored

- Item `monumentspourser00amel` (Princeton Theological Seminary Library scan). One volume, cxii + 711 pages; it is
  not split in two.
- Imprint read on the title page image (PDF page 7): "Annales du Musée Guimet, tome dix-septième ... Paris, Ernest
  Leroux, éditeur ... 1889". The OCR prints "I 889". Rights: pd-us-by-date, no rights field on the record, no
  reproduction notice in the OCR or on the title page. The scan's own date and the catalogue date agree.
- Byte count of the download, 2,219,029, equals the host's listed size for the djvu.txt.
- OCR quality, said plainly: the French is good and can be quoted after a check against the scan. The Coptic is
  garbage (scrambled into Latin, Greek and accented glyphs; the first Bohairic lines at OCR line 4881 are an example).
  The Arabic is garbage too. Neither can be quoted or searched.
- Where things sit (OCR line; add 12 for file lines): introduction 77 to 4874; the Bohairic ("memphitic") Life of
  Pachomius with the French 4877 to 14793; the Life of Theodorus 14793 to 20359, with the Sahidic fragments from
  18509; the Arabic Life with French 20362 to about 38700.
- File: `amelineau_histoire-de-saint-pakhome-annales-guimet-17_leroux1889.txt`. Nothing stripped.

### 2. The Latin Life of Pachomius in the Acta Sanctorum, May III: vendored, with a correction to the brief

- Item `actasanctorum16unse` (Villanova scan). Title page read in the OCR: "Maii tomus tertius, quo dies XII, XIII,
  XIV, XV et XVI continentur ... Parisiis et Romae apud Victorem Palmé ... M. DCCC.LXVI." (OCR lines 202 to 238,
  with the year 1866 at 238). The record has no rights field. Byte count 6,689,780 equals the host's listed size.
- **The Latin printed there is not Dionysius Exiguus's version.** The Bollandists print "Acta auctore suppari monacho
  ex MSS. Graecis, interprete Daniele Cardono Soc. Jesu": Daniel Cardon's Latin of the Greek Life. A search of the
  volume for Dionysius or Exiguus finds no Pachomius text by him. This is the Greek Life in Latin, a witness to the
  same Life; it is not the Dionysian Latin Mark named.
- Where things sit (OCR line; add 12): commentary 78831; Prologue 80678; Life from Chapter I at 80922 to about
  88510; Paralipomena 88515 to about 94018; Appendix on Pachomius the Younger 94048 to about 95390.
- OCR quality: Latin fair, the two columns run together in places; Greek poor.
- File: `acta-sanctorum_maii-tomus-3-lat-grc_palme1866.txt`.

### 2b. Dionysius Exiguus's Latin Life: located, not taken

- Rosweyde's Vitae Patrum, item `VitaePatrumRosweyde1628` (Antwerp, Plantin, 1628; Public Domain Mark on the record;
  also `VitaePatrumRosweyde1615`) prints "Vita Sancti Pachomii ... interprete Dionysio Exiguo abbate Romano" at OCR
  line 19999 of its 5,980,788-byte djvu.txt, with Dionysius's prologue after it.
- Not taken because the OCR reads the long s as f throughout ("Pachomij", "ftcutioGrucoreperta"), so it would be a
  second witness only, and I did not read its title page image for the imprint. Migne PL 73 (the other printing of
  it) was not found on archive.org by the identifiers tried (patrologiae_cursus_completus_lat_vol_073 does not exist).
  This is for Mark to rule: take Rosweyde 1628 as it stands, or look further for PL 73.

### 3. Jerome's Latin of the Rule of Pachomius, PL 23: vendored, part I only

- Item `sanctieusebiihie02jero` (University of Toronto scan of Garnier's Migne-successors printing). The Elenchus
  names "Tomi XXIII" parte I and parte II; the item binds both.
- Title page of tomus secundus (OCR line 414, read): "Parisiis, apud Garnier fratres, editores et J.-P. Migne
  successores ... 1883". The title leaf of tomus tertius (part II), read on the page image (PDF page 409), prints no
  year. Part II is therefore not taken: the file is cut at host OCR line 68272, the end of part I. The original
  download was 157,071 lines and 5,090,586 bytes, equal to the host's listed size, so the whole can be fetched again.
  The Pachomian material is all in part I.
- Where things sit (OCR line; add 12): Vallarsi's admonition on the Rule 4223; Jerome's preface to the translation
  about 4300; the Rule ("Regula patris nostri Pachomii hominis Dei") 4506; Praecepta et instituta 5655; Praecepta
  atque judicia 5915; Monita 6198; the letters of Pachomius and Theodorus and the Easter letter to the monasteries
  (7200) to 7243. The Didymus translation follows at 7243.
- OCR quality: Latin fair, columns run together in places, Greek in the notes garbled.
- File: `jerome_opera-pl23-part1-with-regula-pachomii-lat_migne1883.txt`.

### 4. Legge, The Nestorian Monument of Hsî-an Fû (1888): vendored

- Item `nestorianmonumen00legg` (Princeton Theological Seminary Library scan). The other result for the title,
  `cu31924023155785`, is catalogued 1966 (a reprint) and was not taken.
- Imprint read in the OCR (OCR lines 31 and 110): "London, Trübner & Co., 57 and 59 Ludgate Hill ... 1888 ... Oxford,
  Horace Hart, printer to the University". Rights: pd-us-by-date, no rights field. Byte count 141,936 equals the
  host's size.
- OCR quality: the English is good. **The Chinese text of the inscription is not in the OCR** (a few lines of
  scattered glyph fragments at OCR lines 246 to 340); it cannot be read or quoted from this file. The English is usable.
- Where things sit (OCR line; add 11): preface 118; the translation with Legge's notes 342 to about 3550 (Alopen is
  "Olopun", with Legge's note on the name at about 1025); the lecture and the sketch of later missions from 3556.
- File: `legge_nestorian-monument-of-hsi-an-fu_trubner1888.txt`.

### 5 (optional). Ladeuze, Étude sur le cénobitisme pakhomien (1898): vendored

- Item `tudesurlecnobit00ladegoog`, a Google Books scan of an NYPL copy; the record gives possible-copyright-status
  NOT_IN_COPYRIGHT. The OCR of the title page is garbled, so the title page was read on the page image (PDF page 9):
  "Louvain, typ. J. Van Linthout; Paris, A. Fontemoing, éditeur ... 1898". The preface is dated "Louvain, 8 mai 1898".
  Byte count 1,032,992 equals the host's size.
- Google's preamble and usage notice (a request for non-commercial use and for keeping the watermark) were removed at
  intake as a host addition, on the coordinator's ruling of 2026-11-17 after Decision-Log.md (era 9 batch 2b, and its
  later batch): host lines 1-111, 7,617 bytes, from the Google Book Search mark to the line ending
  "...à l'adresse http://books.google.com". The header's Provenance note gives the text, the line count, the host URL
  and the original size (1,032,992 bytes). Nothing of the printed work was changed. An earlier version of this file
  kept the notice; it was replaced.
- OCR quality: French good.
- Where things sit (this file's own lines, since the preamble is removed): preface 254; Part I, the sources, 316; the
  koinonia under Pachomius 9163; under Shenoute 11635.
- File: `ladeuze_etude-sur-le-cenobitisme-pakhomien-fra_1898.txt`.

## Registry and shelves

All five entries are in `cic/texts/REGISTRY.yaml`: supplied_by the batch-3 Library fill, date_added 2026-11-17.

Staging files (`cic/corpus-map/_staging/`), assigned non-exclusively. The census holds no separate Pachomian entry:
`pachomius` is a person told within `desert-monasticism` (I.3), and no other census movement mentions Pachomius or a
koinonia, so the four Pachomian files go to `desert-monasticism` only. `alopen` is told within
`the-church-of-the-east-on-the-silk-road` (III.1), so Legge goes there only.

| file | atlas entry | rows |
|---|---|---|
| Amélineau | desert-monasticism | Bohairic Life with French, Life of Theodorus, Arabic Life with French (tradition, assigned: second witnesses in French, since the Coptic and Arabic OCR cannot be read); the introduction (context, provisional) |
| Acta Sanctorum May III | desert-monasticism | Cardon's Latin Life (tradition, assigned); the Paralipomena (tradition, provisional); the Bollandist commentary and Appendix (context, provisional) |
| Jerome PL 23 part I | desert-monasticism | the Latin Rule (tradition, assigned); Jerome's preface (context, provisional) |
| Legge | the-church-of-the-east-on-the-silk-road | the stele in Legge's English (tradition, assigned); the lecture (context, provisional) |
| Ladeuze | desert-monasticism | the study (context, provisional) |

No row is marked `needs-ruling`. The Jerome Rule row says the Latin is Jerome's of about 404 from the Greek, and the
Amélineau rows say the French is Amélineau's. The Latin and French files are second witnesses to the Coptic and Greek
Pachomian texts; none is Pachomius's own Coptic. The Legge stele row records that the Chinese is not in the OCR and
that the project's own rendering from the Chinese is a separate step.

## Commands

- `python cic/engine/texts_registry.py`: OK, every vendored file has a header-verified rights line, an ENTRIES row, and
  no ENTRIES row points at a missing file.
- `python cic/engine/texts_registry.py --write-readme`: wrote `cic/texts/README.md`.
- `python cic/engine/corpus_map_merge.py --check`: passed (rc 0), no finding from the five new files. The first
  attempt failed on a YAML quoting error in my own staging notes (an apostrophe in a single-quoted note); I rewrote
  those notes as block scalars before the check passed.
- `python cic/engine/corpus_map_merge.py`: merged (rc 0), 5122 work assignments across 304 entries. It reports one
  finding that is not from this fill: `fixture-synthetic.yaml` is hand-written and nothing in staging produces it.
  Left alone.
- `python cic/engine/corpus_index.py --build`: passed (rc 0), about 5 minutes for the whole corpus.

## Not found, not taken

- Dionysius Exiguus's Latin Life of Pachomius: not in the Acta Sanctorum; located in Rosweyde 1628, not taken (see 2b).
- Migne PL 73: not found under the identifiers tried.
- Part II of the Jerome volume: not taken (no year on its title page).
- The Chinese text of the Xi'an inscription: not in the OCR of any file taken; Legge's English is.
- The Coptic and Arabic texts in Amélineau: on the page but not in the OCR.
- Gallica, HathiTrust, Google Books downloads and MDZ: not tried.

## Calls for the writers

- Quote Amélineau only from the French, after a check against the scan, and as his translation.
- The Acta Sanctorum Life is Cardon's Latin of the Greek, not Dionysius's.
- The Jerome Rule is the Latin of a Greek version; it is Pachomian legislation, not Pachomius's own words.
- A quotation from Legge's English (1888) also gets the project's modern English with the second rendering, per INTAKE.md.
