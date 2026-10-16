# Source Readiness Dossier — Recusant English Catholicism

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is.

**Atlas ID:** VI.7
**Corpus-map slug:** `recusant-english-catholicism`
**Time window:** 1559–1650
**Region(s):** England (census region tag: North Europe)
**Dossier author / date:** library/source-research thread (Era VII session), 2026-10-16
**Corpus-map / `cic/texts/` state as of:** 2026-10-16, branch `library/era-vii-2026-10`. Ten files vendored this pass with staging files written; the registry, seed and cross-link rows are in the session fragments awaiting the lead's merge. No `cic/corpus-map/recusant-english-catholicism.yaml` bucket existed before this pass.

## 1. Already assigned

Nothing was assigned before this pass. The ten files below are vendored, headered and staged (`cic/corpus-map/_staging/`), validated with `corpus_map_merge.py --check`.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| A Narrative of the Gunpowder Plot (Gerard's own English, c. 1606), with Morris's Life of Gerard translating his Latin Autobiography at length | gerard-john; morris-john (the Life) | tradition | assigned | 1.3 MB; Life c. 9,000 lines, Narrative c. 9,000 lines | `gerard-john_condition-of-catholics-under-james-i_morris1871.txt` |
| The Troubles of Our Catholic Forefathers, First Series (nine household and convent narratives) | morris-john (compiler; inner writers named in the note) | tradition | assigned | 1.0 MB | `morris-john_troubles-of-our-catholic-forefathers-ser1_1872.txt` |
| The Troubles, Second Series: Life of Father William Weston (his autobiography in Morris's English); The Fall of Anthony Tyrrell (his own confession) | weston-william; tyrrell-anthony | tradition | assigned | 1.2 MB | `morris-john_troubles-of-our-catholic-forefathers-ser2_1875.txt` |
| The Troubles, Third Series: Ancient Editor's Note Book; Yorkshire Recusant's Relation; Holtby on persecution in the North; Ousebridge Kidcote prisoner's notes; Mush's Life of Margaret Clitherow | ancient-editor-note-book; yorkshire-recusant; holtby-richard; ousebridge-kidcote-prisoner; mush-john | tradition | assigned | 1.1 MB; the Clitherow life c. 5,000 lines | `morris-john_troubles-of-our-catholic-forefathers-ser3_1877.txt` |
| Memoirs of Missionary Priests 1577–1684 (Challoner, 1741; Pollen's 1924 revision) | challoner | tradition | assigned | 2.0 MB; entries to 1646 inside the window | `challoner_memoirs-of-missionary-priests_pollen1924.txt` |
| A Briefe Historie of the Glorious Martyrdom of Twelve Reverend Priests (1582; Pollen's partial reprint) | allen-william | tradition | assigned | 0.3 MB | `allen-william_briefe-historie-of-twelve-reverend-priests_pollen1908.txt` |
| An Epistle of Comfort; Mary Magdalen's Funeral Tears; The Triumphs over Death (Walter's 1822 reprint) | southwell | tradition | assigned | 0.3 MB | `southwell_funeral-tears-triumphs-epistle-of-comfort_walter1822.txt` |
| Rationes Decem (Latin, 1581) with Rickaby's English and Campion's English Challenge (the Brag) in Pollen's introduction | campion | tradition | assigned | 0.26 MB; Latin and English in one file | `campion_rationes-decem-ten-reasons-lat-eng_rickaby1914.txt` |
| Unpublished Documents relating to the English Martyrs, Vol. I, 1584–1603 (CRS vol. V): Catholic-written documents (tradition) and the state's documents (context) | catholic-record-society | tradition / context | assigned | 1.6 MB; 105 documents | `catholic-record-society_unpublished-documents-english-martyrs-v1_pollen1908.txt` |
| The Life of Lady Magdalen Viscountess Montague (Smith, 1609; C. F.'s English, 1627) | smith-richard | tradition | assigned (second witness) | 0.1 MB | `smith-richard_life-of-lady-magdalen-montague_cf1627.txt` |

All ten are also mapped where they serve a sibling world: Gerard, Weston, Holtby, Tesimond and Blount, Campion, Southwell and the Jesuit letters in CRS V to the Society of Jesus (VI.11, tradition); Allen's Briefe Historie and Challoner to VI.11 as context; Gerard's Narrative, the Ancient Editor's Note Book, Allen, Campion, Challoner and the CRS state documents to the English Reformation and Elizabethan Settlement (VI.4, context, provisional).

Witness quality, stated plainly. Nine files are clean OCR or a clean transcription and are primary voice, ready to quote once each quote is verified against the file. Three caveats hold inside them: Gerard's and Weston's autobiographies survive here only as Morris's 1871 and 1875 English of their Latin, inside Morris's own narrative, so their words are quotable only where Morris marks them; Allen's Briefe Historie is a partial reprint by the editor's own statement; Challoner's framing voice is 1741, with the contemporary relations embedded. The tenth file, Smith's Life of Lady Montague, is a garbled microfilm OCR and is a SECOND WITNESS only, vendored because the census names it and no other public-domain witness exists.

## 2. Cross-link opportunities

Checked by header search (`Title:`/`Creator:` lines of every `cic/texts/*.txt`) for this world's figures, places and controversies, then by opening the plausible hits.

- `barlow_brutum-fulmen_1681.txt` (bucket: the-tridentine-church). Prints Pius V's bull Regnans in Excelsis (1570) in English and Latin parallel columns. The bull is the act the recusants lived under and the "bloody questions" were about. Tier: named-never-opened for this world; same time-place. Proposed row (context, assigned) is in `crosslink_fragment.yaml` for the lead to add to the Barlow staging file.
- `polanco_chronicon-v6-lat_1898.txt` (the-society-of-jesus). Latin; 40 hits for Angli/Anglia/England, but the Chronicon ends in 1556, before this world's window. Tier: same time-different-region, not opened. No row proposed.
- `nadal_epistolae-v2-lat_1899.txt` (the-society-of-jesus). Six hits for England, 1562–1565. Tier: same time-different-region, not opened. No row proposed.
- `jesuit-constitutions_constitutiones-societatis-iesu-lat_1606.txt`. The rule the English Jesuits lived under; no English matter. Out of scope for a row.
- `foxe_acts-and-monuments-v3_cattley-townsend1837.txt` (lollardy; hussite). Volume III is Lollard-era; nothing Elizabethan. Out-of-window.
- The Bellarmine English devotional translations (1688, 1703, 1722, 1925) and `roman-missal_england1843.txt`. Out-of-window.
- `sarpi_history-of-the-council-of-trent_brent1676.txt`. Out of this world's subject; no row.

## 3. Verified acquisition leads

Public-domain editions verified on the host and not yet vendored. Each row is also in `seed_fragment.yaml` as `not-yet-downloaded`.

| title | author | translator/ed. | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| A True, Sincere and Modest Defence of English Catholics (1584), 2 vols. | William Allen | Catholic Library reprint (Manresa Press / Herder) | 1914 | archive.org `truesinceremodes01alleuoft`, `truesinceremodes02alleuoft` | pd-us-by-date; NOT_IN_COPYRIGHT | metadata + OCR sampled at five points (clean), 2026-10-16. First in line for the next intake. |
| The Letters and Memorials of William, Cardinal Allen | William Allen | T. F. Knox | 1882 | archive.org `lettersmemorials00alle` | pd-us-by-date | metadata only (Princeton Theological Seminary; D. Nutt, London), 2026-10-16; OCR not sampled |
| The Complete Poems of Robert Southwell | Robert Southwell | A. B. Grosart | 1872 | archive.org `completepoems00grosgoog` (Google scan, NOT_IN_COPYRIGHT); also `completepoemsofr00sout_0` (Boston Public Library scan, not sampled) | pd-us-by-date | metadata + OCR sampled (readable, scan noise), 2026-10-16 |
| The Poetical Works of the Rev. Robert Southwell | Robert Southwell | W. B. Turnbull | 1856 | archive.org `poeticalworksre00soutgoog` | pd-us-by-date; NOT_IN_COPYRIGHT | metadata only, 2026-10-16 |
| Ten Reasons (English only, clean transcription) | Edmund Campion | Joseph Rickaby | 1914 text | gutenberg.org/ebooks/13133 | pd-us-by-date; Gutenberg PD line | fetched and header read, 2026-10-16; not needed because the bilingual 1914 scan is vendored |
| A Christian Directory | Robert Persons | 1739 edition | 1739 | archive.org `christiandirecto00pars` | pd-us-by-date; NOT_IN_COPYRIGHT | metadata + OCR sampled, 2026-10-16: long s rendered as f throughout, so second-witness quality only; the 1851 edition `christiandirecto0000revr` has no status field and its access was not confirmed |
| The New Testament ... in the English College of Rhemes (1582) | Gregory Martin (tr.); Allen, Bristow (eds.) | none | 1582 | archive.org `nevvtestamentofi00mart` (BPL, complete); `thenewtestamento00rhei` (Princeton, NOT_IN_COPYRIGHT, catalogued "Defective") | pd-us-by-date | metadata for both; OCR of the Princeton scan sampled (long s as f), 2026-10-16 |
| The Holie Bible ... (Douai Old Testament) | Gregory Martin (tr.) | none | 1609 | archive.org `holiebiblefaithf00mart_0` | pd-us-by-date | metadata only, 2026-10-16 |
| A Manual of Prayers, newly gathered out of many authors | anonymous | none | 1583 | archive.org `bim_early-english-books-1475-1640_a-manual-of-prayers-new_manual_1583` | pd-us-by-date | metadata + OCR sampled, 2026-10-16: garbled at every point; lead only |
| Catholic Record Society Miscellanea I, II, III | various | Pollen, Gillow and others | 1905–06 | archive.org `publicationscat45britgoog` (vol. 1), `publicationscat31britgoog` (vol. 2: Persons' memoirs, first part; Welsh Marches recusants), `publicationscat46britgoog` (vol. 3: Tower Bills 1575–89; life of Thomas Maxfield; Sir Robert Crosse's Catholic wife, 1607) | pd-us-by-date; NOT_IN_COPYRIGHT | opening pages read for volume and contents, 2026-10-16 |
| The Douay College Diaries, Third to Fifth, 1598–1654, with the Rheims Report | English College, Douai | Burton and Williams | 1911 | archive.org `douaycollegediar10engl`, `douaycollegediar11engl` | pd-us-by-date | metadata only, 2026-10-16 |
| Recusant Roll No. I, 1592–3 (CRS 18) | Exchequer | editor not read | 1916 | archive.org `recusantrollnoi100grea` | pd-us-by-date | metadata only, 2026-10-16 |
| The Ven. Philip Howard, Earl of Arundel (CRS 21) | Pollen and MacMahon (eds.) | none | 1919 | archive.org `publications21cathuoft` | pd-us-by-date; NOT_IN_COPYRIGHT | opening page read, 2026-10-16; a documentary life of a lay martyr |
| CRS Miscellanea VI: Bedingfeld Papers (incl. Sir Henry Bedingfeld's Meditations on the Passion, 1646) | Pollen (ed.) | none | 1909 | archive.org `publicationsofca06cath` | pd-us-by-date | contents read, 2026-10-16; mostly post-1650 |
| Edmund Campion: A Biography (secondary) | Richard Simpson | none | 1896 | archive.org `edmundcampion00simpuoft` and others | pd-us-by-date; NOT_IN_COPYRIGHT | search result only; secondary, not primary voice |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Gerard, The Autobiography of a Hunted Priest (Caraman, 1951) | The census names it | In copyright; not on any reachable host as a free item. Superseded by Morris 1871 (vendored), which translates the autobiography at length inside the Life. |
| Weston, Autobiography of an Elizabethan (Caraman, 1955) | The census names Weston's autobiography | In copyright (archive.org `williamwestonaut0000phil`, `williamwestonaut0000unse` are restricted 1955 items). Superseded by Morris 1875 (vendored). |
| Mush, True Report of Margaret Clitherow, standalone | The census names it | Every standalone item on archive.org is 1947 or later (Monro 1947, Claridge 1966, Mary Joanna 1971, Rayne-Davis 2002), all in copyright. The text is in Morris, Third Series (vendored). |
| Smith, An Elizabethan Recusant House (Southern, 1954) | Clean modern edition of the Montague life | In copyright (`elizabethanrecus0000smit`, 1954). Only the 1627 microfilm is public domain; vendored as second witness. |
| CRS "Miscellanea IV" (1907), Google scan `miscellanea30unkngoog` | Catalogued as carrying Persons' memoirs (concluded) and Catholic chaplaincies and families in the North | The OCR of the item is an Italian book (text about Tasso's letters), not the CRS volume; the catalogue record does not match the scan. Closed as a mis-scanned item; no other scan of Misc. IV found. |
| CRS vol. 12 (`catholicrecord12unknuoft`) and vol. 8 (`publicationsofca08cath`) | Series volumes in window | Vol. 12's opening pages returned no readable title; vol. 8 is the Diary of the Blue Nuns of Paris (1658 onward), outside the window. Not vendored. |
| Southwell, An Epistle of Comfort, 1605 and 1616 EEBO microfilms | The original edition | Microfilm OCR; the 1822 Walter reprint (vendored) is the readable public-domain text. |
| Persons, Christian Directory 1739 | Named in the task | OCR renders long s as f throughout; a quote could not be verified against it. Kept as a lead for a second witness only (§3). |
| Rheims New Testament 1582 and Douai OT 1609 | Named by the census | Public domain and reachable, but 3 MB each and long-s-as-f OCR; not vendored this pass to keep the intake at ten files. Leads in §3 with both scans identified. |
| Manual of Prayers 1583 | Named by the census | Only an EEBO microfilm scan, garbled at every sample point. Lead in §3. |
| Project Gutenberg catalogue dates for Gerard (1840–1912) | Suggests a different author | A catalogue error: the 1871 title page and Morris's Life identify the author as John Gerard, 1564–1637. The text is the right book; the header says so. |
| Campion, Rationes Decem 1584 Latin (`bub_gb_mV8wDDQd4YgC`) and German 1589 (`bub_gb_rN47AAAAcAAJ`) | Early editions | Google Books scans of continental printings; the 1914 Manresa reprint vendored carries the Latin cleanly. Not checked further. |
| Allen, Defence of Sir William Stanley's surrender of Deventer (Chetham Society, 1851) | Allen's voice | Political pamphlet on the Netherlands war; outside this world's subject. Not vendored. |

## 5. Open cross-world questions

- **VI.7 vs. the Society of Jesus (VI.11).** Gerard, Weston, Campion, Southwell, Holtby, Tesimond and Blount are Jesuits and their narratives are the recusant world's richest inside voice. Both worlds have a native claim; the staging maps each text to both. Which world holds the Representative's voice for the English mission (the household church seen from the priest's hole, or the Society's own mission story) is for Doc_02 and Doc_04 of whichever world builds first. Not decided here.
- **VI.7 vs. the English Reformation and Elizabethan Settlement (VI.4).** The state's documents in CRS V, Gerard's catalogue of the penal laws, Allen's answer to Burghley and Campion's Challenge are placed in VI.4 as provisional context. VI.4's own dossier should decide whether it wants a hostile Catholic witness, and whether the Settlement's own voice (Burghley's Execution of Justice, 1583, not yet searched) should be vendored to stand opposite Allen.
- **Seculars vs. Jesuits inside the world.** The Wisbech stirs and the Archpriest controversy (1595–1602) split the community; Weston's Life (Second Series, chapter XVI) gives the Jesuit side. No public-domain Appellant text was searched this pass. A build will need one for balance; flagged, not decided.
- **The Tridentine Church (VI.22).** Barlow's Brutum Fulmen is proposed as a cross-link row from that world's staging file; the lead adds it.

## 6. Step 0 scope notes and recommendation

**Floor (A1).** The census floorNote says "No question". Nothing found this pass changes that: this is the Roman Catholic Church in England under penal law.

**Sourcing (B1).** Strong, and in the community's own voice. The inside narratives (Gerard, Weston, Mush, Holtby, the Yorkshire papers, the household papers of the First Series), the martyrologies (Allen 1582, Challoner), the apologetic and devotional equipment (Campion, Southwell) and the state's record (CRS V) are all now vendored in public-domain English, with Campion's Latin original beside its translation. The gaps are the devotional books themselves (Rheims NT, Manual, Persons' Directory: all public domain, all reachable, all long-s OCR) and the Appellant side.

**Ecology (B2).** The source base is unusually balanced for a persecuted community: first-person narrative, hagiography, martyrology, polemic and the persecutors' own paperwork. The hagiographic bias of Mush and Allen is declared in the texts themselves and should be handled with the five-level confidence vocabulary, not smoothed over. Women are present by name and in their own recorded words (Clitherow's answers at arraignment, Lady Babthorpe's Recollections, the Montague life), which is what the census promised.

**Uniqueness (B3).** Real overlap with VI.11 (the Jesuit narrators) and VI.4 (the same events from the other side), but the household church is a distinct subject neither sibling has: a church run from private houses by laywomen and hidden priests. The overlap is in authors, not in the world's shape.

**Audiences (B4).** The census's own case (a household-based church under persecution, echoing the earliest house churches) holds in the sources: Gerard's and Weston's accounts are built around households.

**Scale (B5).** About 9.3 MB vendored, roughly a million and a half words, comparable to a mid-size built world; eight distinct named inside voices plus anonymous household and prison writers.

**Recommendation: build.** The world clears the floor without question, its own voice is vendored in depth and in English, its women are documented in their own words, and its distinctive shape (the household as church) is not covered by any sibling. The open items (Appellant voice, the devotional books, the Jesuit-overlap ruling with VI.11) are Doc_02 work, not blockers. This is a recommendation for Mark, not a decision.
