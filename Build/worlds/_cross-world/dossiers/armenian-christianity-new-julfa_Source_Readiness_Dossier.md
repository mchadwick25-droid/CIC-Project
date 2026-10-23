# Source Readiness Dossier — Armenian Christianity: Etchmiadzin and New Julfa

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** VI.28
**Corpus-map slug:** `armenian-christianity-new-julfa`
**Time window:** 1517-1650
**Region(s):** Armenia (Etchmiadzin, Erivan, old Julfa on the Araxes) and Isfahan (New Julfa)
**Dossier author / date:** library/source-research thread, Era VII session, world VI.28 agent, 2026-10-23
**Corpus-map / `cic/texts/` state as of:** 2026-10-23, branch `library/era-vii-2026-10`.
No `cic/corpus-map/armenian-christianity-new-julfa.yaml` existed before this
pass. The five staging files below are written and pass
`corpus_map_merge.py --check` (not yet merged). The census sourcing line
reads "Moderate: colophons, the New Julfa church-building record,
merchant-network documents, Arakel of Tabriz (Davrizhetsi)'s history from the
1660s, and material on Etchmiadzin under Safavid rule."

## 1. Already assigned

Nothing was assigned to this world before this pass. A grep of every
`Title:` and `Creator:` header line in `cic/texts/` for Armenian, Julfa,
Etchmiadzin, Arakel, Zakaria, Moses Khoren, Agathangelos and Eznik found one
Armenian author file, `moses-khoren_history-of-armenians-ita_mechitaristi1850.txt`
(fifth century, assigned to `armenian-christianity-conversion-era`), and no
Agathangelos or Eznik file. A grep of the bodies for Julfa, Etchmiadzin and
Isfahan found only the outside witnesses listed in section 2. The five files
below were vendored this pass and staged.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Mémoires historiques sur les Sofis (Brosset's French, 1876), seventeenth-century Etchmiadzin, Erivan, Julfa and the shahs | zakaria | tradition | assigned | ~0.5M of ~1.9M chars, French | `zakaria_memoires-historiques-sur-les-sofis-fra_brosset1876.txt` |
| Cartulaire de Iohannou-Vank (same volume) | zakaria | tradition | provisional | part of the above | same file |
| History of Armenia, vol. II (Chamich; Avdall's English, 1827): the Persian conquest, the expatriation, New Julpha, the catholicoi | chamich | context | assigned | ~0.78M chars, English | `chamich_history-of-armenia-v2_avdall1827.txt` |
| History of the Armenians in India (Seth, 1897): the Julfa deportation tradition and the merchant diaspora | seth | context | assigned | ~0.45M chars, English | `seth_history-of-the-armenians-in-india_1897.txt` |
| The Church of Armenia (Ormanian; Gregory 1912), chapters XV-XVI | ormanian | context | assigned | ~0.57M chars, English | `ormanian_church-of-armenia_gregory1912.txt` |
| The Six Voyages of Tavernier (1678): Julfa, New Julfa, the Armenian religion | tavernier | context | assigned | ~2.4M chars, English | `tavernier_six-voyages-through-turky-into-persia-and-the-east-indies_phillips1678.txt` |

The same files carry further rows for sibling entries. `armenian-christianity-era-8`
(VII.24): Zakaria's 1690s as `antecedent`, Abraham of Crete's History of
Nadir Shah as `tradition`, Chamich's eighteenth-century catholicoi, Seth,
Ormanian. `armenian-cilicia` (IV.20), `armenian-cilicia-after-the-kingdom`
(V.21) and `bagratid-armenian-christianity` (III.16): Samuel of Ani's year
tables, Chamich Parts V-VII, Ormanian. `armenian-christianity-conversion-era`
(I.10), `armenian-christianity-after-avarayr` (II.4), `paulicians` (III.12):
Ormanian's chapters. `church-of-caucasian-albania` (II.14): Hasan
Dchalaliants's History of Aghovanie. `armenian-christianity-zartonk` (VIII.32):
Seth, Ormanian, Avdall's continuation. `orthodoxy-under-the-ottomans-parish-millet-and-n`
(VI.17) and `church-of-the-east-schism-of-1552` (VI.30): Tavernier's passing
notices. All are `context` or `antecedent` and `provisional`, placed on dates
and chapter lists, not read, except where the staging note names a read passage.

**Witness quality, stated plainly.** Ormanian has clean OCR and is ready to
quote once each quote is checked against the page image. Zakaria (Brosset)
and Chamich (Avdall) read well with errors in proper names, and the Brosset
file opens with pages of image noise; treat both as second witnesses for
exact wording until a page image is checked. Seth is readable with scattered
garbled words. Tavernier's OCR renders the long s as the letter f throughout
and breaks many words; it is a second witness. Nothing here is a source
written inside 1517-1650 by an Armenian in the original language. Zakaria is
the nearest: he was born about 1626 (Brosset's preface) and writes mostly of
1640-1699, with Shah Abbas's reign reported from informants.

**Scale.** About 6.1 million characters in five files: ~1.9M French, ~4.2M
English. Only about a quarter of Zakaria's volume (the Mémoires and the
Cartulaire) is this world's voice; the rest of that volume (Nadir Shah,
Samuel of Ani, Davith-Beg, the Aghovanie history, a nineteenth-century
Russian officer's memoir) serves other entries. Most of Tavernier is India.

## 2. Cross-link opportunities

- **Olearius, Voyages and Travels of the Ambassadors** (`olearius_voyages-and-travels-of-the-ambassadors_davies1662.txt`,
  assigned to the Russian entries). The Holstein embassy to Persia (1633-39)
  buried two of its men in the Armenian churchyard at Julfa (line 23659),
  was received at the Armenian church in the Julfa suburb by the patriarch of
  the place (line 24095), and describes Julfa as an Armenian suburb with twelve
  churches and over three thousand houses (line 26003). Tier: same
  time-place. Row proposed in `crosslink_fragment.yaml`.
- **Rycaut, Present State of the Greek and Armenian Churches** (`rycaut_present-state-greek-armenian-churches_1679.txt`,
  assigned to the Ottoman Orthodox entries). The Armenian chapters run from
  line 16692 and name Etchmiadzin at about line 17730. A consul's view of 1678,
  a generation after the window. Tier: same place, after the window. Row
  proposed.
- **Harasiewicz, Annales Ecclesiae Ruthenae** (`harasiewicz_annales-ecclesiae-ruthenae-lat_1862.txt`,
  assigned to the Brest entry). The editor's note (lines 4802-4806) records
  that the Armenian bishop of Lviv, Nicolaus Torosowicz, accepted union with
  Rome in 1634 and took the archbishop's title. The Armenian church in Poland
  is a branch of this world's diaspora. Tier: same time, different region.
  Row proposed.
- **Patrologia Orientalis tome 16** (`patrologia-orientalis-tomus16_synaxaire-arabe-jacobite-barmahat-bachons-synaxaire-armenien-tre-fra_graffin-nau1922.txt`,
  assigned to Armenian Cilicia). The Armenian Synaxarion of Ter Israel
  (French only; the Armenian column is not recovered) is the church's own
  calendar of saints. Tier: out-of-window, same tradition. Row proposed.
- **Moses Khoren, History of the Armenians** (Italian, `moses-khoren_history-of-armenians-ita_mechitaristi1850.txt`,
  assigned to the conversion-era entry). Fifth century; Chamich and Zakaria
  both cite it as the founding national history (Zakaria's first chapter names
  Agathangelos and Moses). No row proposed. Tier: out-of-window.
- **Hough, History of Christianity in India vol. II** (`hough_history-of-christianity-in-india-v2_1839.txt`,
  lines 4923-4925 on the Armenians who never submitted to Rome, citing Galanus
  and Asseman). A Protestant historian's passing note; no row proposed. Tier:
  out-of-window.
- **Purchas, Hakluytus Posthumus vol. XII** (`purchas_hakluytus-posthumus-pilgrimes-v12_1906.txt`,
  line 2895 and following). The Armenian village on the coast near the Jenkinson
  voyage; a passing mention in a Muscovy volume. No row proposed.
- The existing Armenian entries (conversion era, after Avarayr, Cilicia) hold
  no text from this window.

## 3. Verified acquisition leads

Each row below was checked against its actual host page (archive.org metadata
fetched, title page and text read in the OCR) on 2026-10-23. Rows for each
are in `seed_fragment.yaml`.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Collection d'historiens arméniens, tome II (Zakaria, Mémoires historiques sur les Sofis; Cartulaire; Aghovanie; Davith-Beg; Abraham of Crete; Samuel of Ani; Russian officer's memoir) | Zakaria of Kanaker and others | M.-F. Brosset (French) | 1876 (title page; catalogued 1886) | `archive.org/details/collection-d-historiens-armeniens-1886-2-717` | pd-us-by-date; individual upload, no rights field, no access restriction | metadata fetched; title page ("1876", Indiana University Libraries stamp) and five OCR samples read; compared with the Google scan; VENDORED |
| History of Armenia, vol. II, with Avdall's continuation | Michael Chamich | Johannes Avdall | 1827 | `archive.org/details/india.history.resource.35267` | pd-us-by-date; Public.Resource.Org India History collection, no rights field | metadata and title page read; VENDORED |
| History of the Armenians in India from the Earliest Times to the Present Day | Mesrovb J. Seth | none (English) | 1897 (Luzac, London) | `archive.org/details/historyarmenian00sethgoog` | pd-us-by-date; host NOT_IN_COPYRIGHT; Harvard copy | metadata and title page read; VENDORED |
| The Six Voyages of John Baptista Tavernier | J.-B. Tavernier | John Phillips (host catalogue; not printed in the OCR) | 1678 | `archive.org/details/sixvoyagesofjohn00tave` | pd-us-by-date; host "Not in copyright" (BHL); Smithsonian Libraries copy | metadata and title page read; VENDORED |
| The Church of Armenia | Malachia Ormanian | G. Marcar Gregory | 1912 | `archive.org/details/thechurchofarmen00ormauoft` | pd-us-by-date; host NOT_IN_COPYRIGHT; Toronto copy | metadata, title page and the dated introduction read; VENDORED |
| Collection d'historiens arméniens, tome II (Google scan, Oxford copy) | as above | Brosset | 1876 (catalogued 1874) | `archive.org/details/collectiondhist00arhagoog` | pd-us-by-date; NOT_IN_COPYRIGHT | fetched and compared; OCR reads worse; not vendored. A fallback for a doubtful reading. |
| Sir John Chardin's Travels in Persia, vols. 1 and 2 | John Chardin | Edmund Lloyd (OCR title page) | 1720 | `archive.org/details/bim_eighteenth-century_sir-john-chardins-trave_chardin-john-sir_1720_1` and `..._1720_2` | pd-us-by-date; no rights field | metadata fetched; four Julfa passages in vol. 1 read (events of 1670-73). Not vendored: after the window, and Tavernier and Olearius cover Julfa. |
| The Travels of Sig. Pietro della Valle | Pietro della Valle | not named by the host | 1665 | `archive.org/details/bim_early-english-books-1641-1700_the-travels-of-sig-piet_della-valle-pietro_1665` | pd-us-by-date; no rights field | metadata only; a search of the OCR for Julfa spellings found none, so relevance to this world is unconfirmed. |
| History of the Armenians in India, other scans | Seth | none | 1897 / 1895 | `historyarmenian01sethgoog` (Michigan copy, 1897); `india.history.resource.106107` (Calcutta printing catalogued 1895) | pd-us-by-date; no rights field on the Calcutta item | metadata and size compared; not vendored (same book) |

**English beside the French.** No public-domain English translation of
Zakaria or of the rest of Brosset's volume exists in the library or on the
reachable hosts. Chamich in Avdall's English is a different, later work on
the same events. Recorded as a gap, not a failure to search.

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Arakel of Tabriz (Davrizhetsi), Book of History, the Armenian text (item `india.history.resource.117162`, host title "Girk' Patmut'eants'", catalogued Oscan Yerevants, Amsterdam, 1669, language arm) | The census's named main source; the host calls it the 1669 printing | The OCR is Tesseract run in Armenian over what is mostly unreadable text (the 155,000 tokens are dominated by single letters and noise). The OCR has no title page, so the edition is not identified by the file (it could be the 1669 print or a later reprint) and the 1669 date rests on the catalogue alone. Unusable as a quotable text and the date cannot be confirmed. A clean re-scan or a transcription is needed. |
| Arakel de Tauriz, Livre d'histoires, in Brosset's French (Collection d'historiens arméniens, tome I, 1874) | Brosset translated Arakel in volume I; his footnotes in volume II cite Arakel by chapter | Volume I was not found on archive.org. The Google item `collectiondhist00arhagoog` has a volume-I description but holds volume II (title page "1876"). Title and creator searches (Arakel, Arhakel, Davrizhetsi, Ardzrouni, "historiens arméniens", Brosset) and guessed Google identifiers returned nothing else. HathiTrust and Gallica are blocked. Volume I would be public domain by date (1874). |
| Arakel of Tabriz, Book of History, trans. Bournoutian (Costa Mesa, 2010) (`arakel-of-tabriz-2010-bournoutian`) | The only English; the census cites it | In copyright (2010). The item sits in a patron-library collection with no rights field. Not vendored. |
| Zakaria of Kanaker, Chronicle, trans. Bournoutian (2004-07) | English for Zakaria | In copyright; not on the host. The vendored Brosset French covers the same author. |
| Simeon of Poland (Simeon Lehatsi), Travel Accounts, trans. Bournoutian (2007) (`bournoutian-2007-simeon-of-poland`) | A travelling Armenian priest of the early 1600s | In copyright (2007). The Armenian original or Brosset's translation was not found by transliteration or Armenian-script searches. |
| Abraham of Crete, Chronicle, trans. Bournoutian (1999) | The Etchmiadzin catholicos | In copyright. Brosset's French of his History of Nadir Shah is vendored inside the Zakaria volume (outside the window). |
| Colophons of Armenian manuscripts (Sargisean; Hakobyan 1951-55; the Kesaratsi Psalter colophon of 1638) | The census names colophons as the world's best voice; the first documented story rests on Kesaratsi's colophon | Searches by author, title and Armenian script on archive.org found no colophon collection or Julfa imprint scan. Hakobyan 1951-55 is in copyright. Kévorkian's catalogue of incunabula (1986) is in copyright. Zakaria's chapter XXXVII (file line 5658) names the Julfa press and Khatchatour Késaratsi, which is the nearest vendored text. |
| Matthew of Tsaretsi; Hovhannes Julayetsi; Khachatur Kesaratsi's own writings | Named in the brief as possible voices | No archive.org item found by title or creator search; nothing in copyright-clear form. Khachikyan's English of the merchant Hovhannes Joughayetsi's ledger (1966, `khachikian-1966-ledger-jughayetsi-english`) is in copyright. |
| Carmelite Chronicle of Persia (1939) | Latin missionaries at Isfahan | In copyright (1939, foreign publication); title search on archive.org found nothing. |
| Galanus, Conciliatio ecclesiae armenae cum romana (Rome, 1658) (`pts_conciliationisecclesiae_1608_1`, `_1609_2`) | A Catholic missionary's long account of the Armenian church, published at the window's end | Both volumes are public domain by date (host NOT_IN_COPYRIGHT) but the OCR is Tesseract in Armenian over Latin text and reads as noise (sampled at the opening). The two files are 2.1M and 4.6M chars. Unusable until re-OCR'd; not vendored. |
| Herbert, Some Yeares Travels (1638) (`bub_gb_hNn7DbdAKVAC`) | An English traveller at Isfahan in 1627-29 | Full text fetched; a search for Julfa spellings found no hit. |
| Tavernier, second scan `sixvoyagesofjohn00tave_0` (Getty) | A second copy of the same translation | Fetched and compared; the same long-s-as-f OCR and 16% larger; the Smithsonian scan was vendored. |
| Chamich, vol. I (`historyofarmenia0002unse`) and the DLI second scan of vol. II | The earlier volume and a second scan | Vol. I stops before the window (Parts I-IV); the second scan of vol. II reads slightly worse. Neither vendored. |
| Urbatagirk (Venice, 1512) and the Amsterdam Bible of 1666 | Named in the brief as printing records | Searches by title found no archive.org item. Ormanian (line 4098 of the vendored file) records the 1512 and 1666 imprints; record only, nothing to vendor. |
| Seth's "History of the Armenians in India", 1895 Calcutta printing (`india.history.resource.106107`) | The brief names 1895 | The Luzac 1897 scan was vendored because its title page and rights field are readable; the Calcutta item has no rights field. |
| Chardin and Tavernier in French (`voyagesduchevali*`, `lessixvoyages*`) | The original French of both outside witnesses | Many scans on archive.org; the English translations carry the same Julfa passages. Not opened. |

## 5. Open cross-world questions

- **Armenian entries and the "richer window later".** The census status for
  this entry is "Researched — deferred, richer window later", and it
  continues as `armenian-christianity-era-8` (VII.24, c. 1700-1815,
  Constantinople, Venice, Mount Lebanon). Zakaria's chronicle runs to 1699 and
  Chamich's Parts VI-VII to 1780, so the same texts serve both. Whoever builds
  either should settle, once, which entry reads Zakaria and Chamich as voice
  and which as context.
- **Zakaria's date.** About three-fifths of the Mémoires (Shah Abbas II, 1642-66,
  and after) fall after 1650. The census window ends in 1650. The `assigned`
  row on this entry rests on the Julfa press chapter, the life of the
  catholicos Mosès and the Abbas-era reports. A reader may rule that the
  window is too early for the main voice.
- **Samuel of Ani and Chamich Parts V-VI** are mapped as `context` to the
  Bagratid and Cilician entries on dates and contents pages only. Those
  entries' own dossiers should confirm.
- **Persian-side and Latin-missionary context.** The Carmelite and Capuchin
  missions at Isfahan (Tavernier lines 7635, 13456, 13478) bear on Latin-rite
  work in Persia; no census world covers them. Named, not decided.
- **Armenians in Poland (Lviv).** One row for the 1634 union is proposed; the
  Armenian diaspora church in Poland may deserve its own mapping if the
  Ruthenian entries (VI.20) are built.
- **The Church of the East.** Tavernier's passing notices of Nestorians
  and Jacobites at Basra and elsewhere are staged to the 1552 schism entry
  (VI.30) as `context`, `provisional`; that entry's dossier should confirm.

## 6. Step 0 scope notes and recommendation

**Floor (A1).** The census floorNote reads "No question — this is one of the
ancient Oriental Orthodox churches, whose difference from the Chalcedonian
churches is about how Christ's divinity and humanity are described, not about
whether he is God." Nothing in the texts read this pass raises a creedal
question. Ormanian's chapters on dogma (XX-XXV) are available if a Doc_01
wants the church's own statement.

**Uniqueness against sibling worlds (B3).** No sibling covers Etchmiadzin
under Safavid rule, the 1604-05 deportation, New Julfa or the Julfa press.
VII.24 continues the story from 1700. V.21 ends with the see's return to
Etchmiadzin in 1441. The Ottoman Orthodox entries (VI.17, VII.18) cover the
Greek millet, not the Armenian church. The overlap with VII.24 is in the
sources, not the window.

**Sourcing (B1, B2).** The census says "Moderate". The library now holds
one real contemporary voice (Zakaria, in Brosset's French, mostly after 1650),
four secondary English texts, and four outside witnesses (Tavernier, Olearius,
Rycaut, Harasiewicz's note). The census's own named sources are not in usable
public-domain form: Arakel of Tabriz is only in copyright English or an Armenian
scan that cannot be read, and Brosset's volume I was not found; the colophons
and the merchant documents are not on the reachable hosts. The two
documented stories in the census rest on Arakel and on Kesaratsi's colophon;
only the press story has any vendored text (Zakaria, chapter XXXVII).

**Scale (B5).** About 6.1 million characters in five files, of which roughly
0.5M is this world's own voice. That is smaller on voice than a typical
finished world.

**Recommendation: open question.** The world is real, distinct from its
siblings and floor-clear. What is missing is the voice the census itself
names: Arakel's history and the colophons. Zakaria alone, in a French
rendering with OCR errors and mostly after 1650, may or may not be enough for a
build. Mark's ruling is needed on whether to build on Zakaria with the English
secondaries, or to hold the build until a readable Arakel (a clean Armenian
re-scan, or Brosset's volume I) is found. This is a recommendation for Mark,
not a decision.
