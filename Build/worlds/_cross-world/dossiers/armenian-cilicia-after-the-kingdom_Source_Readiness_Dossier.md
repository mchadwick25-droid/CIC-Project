# Source Readiness Dossier — Armenian Christianity after the Kingdom (Sis to Etchmiadzin)

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** V.21
**Corpus-map slug:** `armenian-cilicia-after-the-kingdom`
**Time window:** 1300–1441
**Region(s):** Cilicia (Sis), then Etchmiadzin; Cyprus and the Latin courts as the outside record
**Dossier author / date:** Library thread, Era VI session (east batch), October 2026
**Corpus-map / `cic/texts/` state as of:** October 2026, branch `library/era-vi-2026-10`. The bucket `cic/corpus-map/armenian-cilicia-after-the-kingdom.yaml` held three works, all provisional, staged by the Era VII session while it worked on the New Julfa world (VI.28). Eight files were vendored this pass, each with a staging file that passes `corpus_map_merge.py --check`. Their registry entries, seed rows, the WORKS entry and the cross-link rows sit in the lead's fragment files until merged.

Census inputs (checked October 2026 in `world-census.json`): status Pre-Survey Candidate, floor note "No question — the ancient miaphysite confession, unchanged." Sourcing line: "Thin after Shnorhali's generation, but colophons are rich: the era's Armenian voice survives mostly in scribes' margins." The census names four voices: Levon V, Grigor Tatevatsi, Kirakos of Virap and the scribes of the colophons. The census has no `sources` list for this world.

## 1. Already assigned

The first three rows were in the bucket before this pass. The last eight are the files vendored this pass. Scale is characters in the vendored file, counted; where a row covers part of a file the passage is named.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| History of Armenia (Chamich; Avdall's English, 1827), vol. 2, Part VII, chapters I–V: Tamerlane to the return of the see to Etchmiadzin | chamich | context | provisional | part of 777,135 characters (printed pages 311–340) | `chamich_history-of-armenia-v2_avdall1827.txt` |
| The Church of Armenia (Ormanian; Gregory's English, 1912), chapters XIII–XV: attempts at union and the return to Etchmiadzin | ormanian | context | provisional | part of 568,309 characters (file lines 3339–4122) | `ormanian_church-of-armenia_gregory1912.txt` |
| Tables chronologiques de Samouel d'Ani, with the continuation to 1348 (Brosset's French, 1876) | samuel-of-ani | context | provisional | part of 1,919,717 characters (file lines 18531–28860) | `zakaria_memoires-historiques-sur-les-sofis-fra_brosset1876.txt` |
| Recueil des historiens des croisades, Documents arméniens II: Hayton, Pseudo-Brocard, Daniel de Thaurizio, Jean Dardel's Chronique d'Arménie (to 1384) | rhc-armeniens | context | assigned | 4,807,849 characters | `rhc-armeniens_documents-armeniens-t2-latins-et-francais-fra_academie1906.txt` |
| Recueil des historiens des croisades, Documents arméniens I: Armenian chroniclers in French; in the window, Hethum II's poem, Sempad's continuator to about 1335 and the closing appendix | rhc-armeniens | tradition | provisional | 3,557,312 characters in the file; the window parts are a small share of it | `rhc-armeniens_documents-armeniens-t1-fra_academie1869.txt` |
| Mansi, tomus 25 (1300–1344): the acts of the Councils of Sis (1307) and Adana (1316) | mansi | tradition | assigned | 3,623,256 characters in the file; the Sis acts are about 23,000 | `mansi_sacrorum-conciliorum-collectio-tomus-25-1300-1344-lat_welter-facsimile1903.txt` |
| Documents pour servir à l'histoire des Lusignans de la Petite Arménie, 1342–1394 (Langlois 1859), with a colophon of 1393–94 | langlois | context | assigned | 131,794 characters | `langlois_documents-lusignans-petite-armenie-1342-1394-fra_langlois1859.txt` |
| Étude sur Thomas de Medzoph (Nève, Journal asiatique 1855) | neve | context | provisional | 104,005 characters | `neve_etude-sur-thomas-de-medzoph-fra_journal-asiatique1855.txt` |
| Het'um the Historian's History of the Tartars (Bedrosian's English, 2004) | hetum | context | assigned | 192,556 characters | `hetum_history-of-the-tartars-flower-of-histories-of-the-east_bedrosian2004.txt` |
| Haithoni Armeni historia orientalis (Latin of Nicolas Falcon, ed. Müller 1671) | hetum | context | assigned | 218,509 characters | `hetum_historia-orientalis-de-tartaris-lat_muller1671.txt` |
| Léon le Magnifique and the Table chronologique de l'histoire de Sissouan (Alishan, Venice 1888) | alishan | context | assigned | 794,441 characters in the file; the year-by-year table is about 51,000 (file lines 16139–17870) | `alishan_leon-le-magnifique-et-table-chronologique-de-sissouan-fra_alishan1888.txt` |

The same pass staged secondary placements. RHC II is on the earlier Cilician world (IV.20) and the Church of the East under the Mongols (context, provisional). RHC I and Alishan are on IV.20 (tradition and context, provisional). Het'um in English is on IV.20 and the Mongols world (context, provisional); the Latin text is on this world only. Mansi tomus 25 is on the Latin papal church from Avignon to Lateran V (tradition, provisional).

What kind of witness each is:

- **The church's own acts.** Mansi 25 prints the acts of the Armenian council of Sis, headed "jussu Gregorii patriarchae et Leonis Armeniae regis ... anno Domini MCCCVII", and of Adana in 1316. They are the Armenian church's council record in Latin, in the form Rome kept it. Long s is read as f, so they are second witness.
- **The court and its confessor.** Het'um's History of the Tartars (1307) is the voice of the Cilician court speaking to Pope Clement V. It is in clean modern English by a translator who declares it public domain, with the Latin and the French in the library beside it. Dardel's chronicle is a French Franciscan's account of Levon V's last years. Neither speaks for the church on doctrine.
- **One colophon.** Langlois prints, as his last item, a French rendering of an Armenian manuscript note of 1393–94. It is the only colophon the library holds in a form that can be read.
- **The later histories.** Chamich, Ormanian and Alishan are late Armenian histories from native sources. Alishan's year-by-year table is the best single list of the window.
- **Not here.** Grigor Tatevatsi, Kirakos of Virap and the scribes have no text of their own in the library. Levon V appears in Dardel and Langlois.

## 2. Cross-link opportunities

Checked by searching the headers and bodies of every `cic/texts/*.txt` for Armenia, Armenian, Sis, Cilicia, Levon, Leo V, Hayton, Hetoum, Tatev, Etchmiadzin and Tamerlane, then opening the hits. Proposed rows are in the lead's `crosslinks.yaml`.

- **Chamich, History of Armenia vol. 2, `chamich_history-of-armenia-v2_avdall1827.txt`** (bucket: this world, provisional). Tier: same time-place. Read at the cited lines, it fits, and I propose raising the row to assigned. The council of Sis of 1342 (Armenian era 791), called to answer a book of 117 "heresies" sent from Avignon, is at line 14107; the fall of Sis at 14504; Gregory of Tatev at 15103; the choice of Kirakus of Khor Virap at Etchmiadzin at 15369–15503.
- **Ormanian, The Church of Armenia, `ormanian_church-of-armenia_gregory1912.txt`** (bucket: this world, provisional). Tier: same time-place. Lines 3860–3880 say the king called a synod at Sis in 1307, that the catholicos died before it met, and that the desire for union grew from then until the see moved in 1441. Proposed: raise the row to assigned. Note that this differs from the heading of the Mansi acts (see §5).
- **Mansi, tomus 26, `mansi_sacrorum-conciliorum-collectio-tomus-26-1344-1409-lat_welter-facsimile1901.txt`** (bucket: the Latin papal church). Tier: same time-place. The Nicosia attendance list (about line 35519) names an Armenian bishop, Gregory, among the bishops. Proposed row: context / provisional.
- **Mansi, tomus 31, the Council of Florence, `mansi_sacrorum-conciliorum-collectio-tomus-31-concilium-florentinum-lat_welter-facsimile1906.txt`.** Tier: same time, different region. The heading "De Armeniis" is at line 98033 and runs to about line 99150. Whether the Armenian delegation of 1439 came from Sis is not checked. Proposed row: context / provisional.
- **Seth, History of the Armenians in India (1897), `seth_history-of-the-armenians-in-india_1897.txt`** (bucket: New Julfa and later worlds). Tier: out-of-window secondary. Lines 1380–1396 mention the last king's travels in Europe and his death at Paris, and the Mamluk conquest. Noted, no row proposed.
- **Rycaut, Present State of the Greek and Armenian Churches (1679), `rycaut_present-state-greek-armenian-churches_1679.txt`.** Tier: out-of-window. The Armenian church of the seventeenth century under Ottoman and Persian rule. Noted, no row: after the window.
- **Moses Khoren, History of the Armenians (Italian, 1850), `moses-khoren_history-of-armenians-ita_mechitaristi1850.txt`.** Tier: out-of-window (the fifth-century Armenian history). Noted, no row.
- **Barhebraeus, Chronicon ecclesiasticum vol. 3, `barhebraeus_chronicon-ecclesiasticum-vol3-lat_abbeloos-lamy1877.txt`.** Sixty hits for the Armenians, including Lamy's additions; the thirteenth-century chronicle and the editor's notes. Noted, no row: not opened for Cilicia.

## 3. Verified acquisition leads

Each lead was checked on its host. Item records were read for date, `possible-copyright-status`, licence and the text file. Texts fetched were sampled at opening, middle and end. All are public domain by date unless a row says otherwise.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Het'um the Historian's History of the Tartars [Flower of Histories of the East] | Het'um the Armenian | Robert Bedrosian | 2004 | archive.org `HetumTheHistoriansFlowerOfHistoriesOfTheEast` | the translator's own declaration in the text: "This translation is in the public domain. It may be copied and distributed freely." | metadata and text read; 0.19 MB fetched; clean English; October 2026. **Vendored.** The translation includes bracketed passages from Burger's 1988 edition of Pynson's c. 1520 English; the lead may want to confirm the declaration covers them. |
| Haithoni Armeni historia orientalis (Latin of Falcon) | Hayton; Nicolas Falcon; ed. Andreas Müller | none (Latin) | 1671 | archive.org `bub_gb_1VwdIBtEDCYC` | pd-us-by-date; Public Domain Mark 1.0 | metadata and title page read; 0.22 MB fetched; readable Latin, long s read as f; October 2026. **Vendored.** |
| Recueil des historiens des croisades, Documents arméniens II | Académie des inscriptions et belles-lettres | none (Latin and French) | 1906 | archive.org `recueildeshistoriensdescroarme2` | pd-us-by-date | metadata and title page read; 4.9 MB fetched; readable; October 2026. **Vendored.** |
| Recueil des historiens des croisades, Documents arméniens I | Académie des inscriptions et belles-lettres | none (French) | 1869 | archive.org `recueildeshistoriensdescroarme1` | pd-us-by-date; Public Domain Mark 1.0 | metadata and title page read; 3.7 MB fetched; clean; October 2026. **Vendored.** |
| Sacrorum conciliorum collectio, tomus 25 | G. D. Mansi (ed.) | none (Latin) | 1782 (Welter facsimile 1903) | archive.org `sacrorumconcilio0025joan` | pd-us-by-date | metadata and title page read; 3.6 MB fetched; Latin, long s read as f, about 0.47 matched against a clean Latin list (the Mansi 6 file already vendored reads about 0.35); October 2026. **Vendored.** |
| Documents pour servir à l'histoire des Lusignans de la Petite Arménie | Victor Langlois | none (French) | 1859 | archive.org `DocumentsPourServirALhistoireDesLusignansDeLaPetiteArmenie` | pd-us-by-date on the OCR title-page year | title page read; 0.13 MB fetched; clean; October 2026. **Vendored.** |
| Étude sur Thomas de Medzoph (Journal asiatique 1855) | Félix Nève | none (French) | 1855 | archive.org `EtudeSurThomasDeMedzophEtSurSonHistoireDeLarmenieAuXveSiecle` | pd-us-by-date on the journal title page | title page read; 0.10 MB fetched; readable; October 2026. **Vendored.** |
| Léon le Magnifique, with the Table chronologique de l'histoire de Sissouan | Ghewond M. Alishan | none (French) | 1888 | archive.org `lonlemagnifique00alisgoog` | pd-us-by-date; NOT_IN_COPYRIGHT | metadata and title page read; 0.82 MB fetched; clean; October 2026. **Vendored.** The census-list form "Alishan, Sissouan (1899)" was not found under that title. |
| Exposé des guerres de Tamerlan et de Schah-Rokh ... d'après la chronique arménienne de Thomas de Medzoph | Félix Nève | none (French) | Brussels, memoir presented 1858 | archive.org `NeveExposeDesGuerresDeTamerlan` | not established: the OCR reads the title-page year as "MDCCCM" | metadata read; 0.38 MB fetched at the front; October 2026. Not vendored; a longer French treatment of the same chronicle. |
| Histoire politique et religieuse de l'Arménie, tome I (to the death of the last king, 1393) | François Tournebize | none (French) | no year on the scan | archive.org `TournebizeHistoirePolitique` | not established: the scan's title page shows only the Firmin-Didot imprint and the item has no metadata | metadata read; 2.6 MB fetched; clean, with 177 hits for Cyprus, 1307, 1316 and the council of Sis; October 2026. Not vendored until the year is confirmed. |
| Conciliationis Ecclesiae Armenae cum Romana (two scans) | Clemens Galanus | none (Latin and Armenian) | 1650–1661 | archive.org `pts_conciliationisecclesiae_1608_1` and `bub_gb_NCRzlUvh2mkC` | pd-us-by-date; NOT_IN_COPYRIGHT and Public Domain Mark 1.0 | metadata read; 2.1 MB fetched; Armenian columns are noise; October 2026. A seventeenth-century Roman case, after the window; not vendored. |
| Smbat Sparapet's Chronicle | Smbat Sparapet | Robert Bedrosian | 2005 | archive.org `SmbatSparapetsChronicle` | the translator's declaration: "This work is in the public domain. It may be copied and distributed freely." | metadata and text read; 0.39 MB fetched; clean; October 2026. Ends in 1272, before the window; for the earlier Cilician world. Not vendored. |
| L'extrême Orient au moyen-âge | Louis de Baecker | none (French) | 1877 | archive.org `lextrmeorientau00baecgoog` | pd-us-by-date; NOT_IN_COPYRIGHT | metadata read; 0.96 MB fetched; clean; October 2026. Hayton's French among other travellers' texts; not vendored. |
| Les Mongols d'après les historiens arméniens | Édouard Dulaurier | none (French) | 1858–1860 | archive.org `LesMongolsDapresLesHistoriensArmeniensFragmentsTraduitsSurLesTextes` | not established: no title page in the offprint and no host metadata | 0.33 MB fetched; clean; October 2026. Mostly thirteenth-century; not vendored. |
| Hayapatum: Patmut'iwn Hayots' | Ghewond M. Alishan | none (Armenian) | 1901 | archive.org `hayapatumpatmut00alisgoog` | pd-us-by-date; NOT_IN_COPYRIGHT | metadata read; 2.3 MB fetched; the OCR reads as Armenian script; October 2026. Scholarship in Armenian; not vendored. |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Pynson's English of Hetoum (1520) | Named in the task as the English | Searched archive.org for Hayton, Haython, Haiton, Hetoum, "Lytell Cronycle", "Flower of the histories of the East" and Pynson. No EEBO item found. The modern edition (Burger 1988) is in copyright. The Bedrosian translation (vendored) is the English leg. |
| Thomas of Medzoph, Patmut'iwn Lank-T'amuray (Armenian, `PatmutiwnLank-tamurayEwYajordatsIwrotsArarealTovmaVardapeti`) | The Armenian chronicle of Tamerlane and the church's losses | Fetched (210 KB) and sampled. The Armenian comes out as Latin-letter noise. The item has no date or rights field. Unusable. |
| Colophons of Armenian manuscripts (Khachikyan, 14th and 15th centuries, `Khachikyan1401`, `Khachikyan1402`, `Khachikyan15A01`, `Khachikyan15B01`; Matevosyan, 13th century) | The census names the colophons as the era's voice | Soviet Armenian publications of the 1950s to 1980s in Armenian; in copyright as foreign works of 1931 or later. The hosts carry no dates. Not downloaded. Sanjian's English *Colophons* (1969) is in copyright and was not searched on the host. |
| Rüdt-Collenberg, *The Rupenides, Hethumides and Lusignans* (1963, `rudt-collenberg-1963-rupenides-hethumides-lusignans`) and *Les Bullae et Litterae adressées par les papes d'Avignon à l'Arménie cilicienne, 1305–1375* (1986, `Collenberg1986BullaeEtLitterae`) | The papal letters to Cilicia | In copyright. |
| Alishan, *Sissouan ou l'Arméno-Cilicie* (1899) | Named in the task | Not found by title or creator. The 1888 book by the same author (vendored) covers the ground. |
| Brosset, Collection d'historiens arméniens, tome II (`collection-d-historiens-armeniens-1886-2-717`) | Brosset's French of Armenian chroniclers | A duplicate: the same volume is on the shelf as `zakaria_memoires-historiques-sur-les-sofis-fra_brosset1876.txt`. |
| Kirakos Gandzakets'i and Vardan (Bedrosian, `KirakosGanjaketsisHistoryOfTheArmenians`) | Armenian chroniclers in English | Thirteenth century, before the window. |
| Tatevatsi, Book of Questions; any text of Grigor Tatevatsi or Kirakos of Virap | The census names them as voices | Searched archive.org for "Grigor Tatevatsi", "Tatev monastery", "Kirakos Virapetsi". One 2016 art-history paper on two Bibles turned up and is not on point. No text found. |
| Ormanian, Azgapatum (National History, Armenian, `OrmanianAzgapatum1`) | A fuller Armenian form of Ormanian's history | A 5.9 MB upload with no date or rights field. The English summary (vendored) is on the shelf. |
| Mas Latrie, Histoire de l'île de Chypre sous les Lusignan (`mas-latrie-histoire-de-lile-de-chypre-sous-le-regne-des-princes-de-la-maison-de-lusignan-v-1-1861`) | Cyprus and Cilician Armenia in the fourteenth century | Volume 1 is listed; not opened. Scholarship with documents. |
| *Hetum*, the 2014 upload `hetum` (RecCrosArm2, 5.1 MB) | Another file of Hayton's French | A copy of the same RHC volume already vendored. |

## 5. Open cross-world questions

- **The break at 1300.** The earlier Cilician world (IV.20) ends in 1300 and this one starts there. The sources straddle the break: Hetum II's poem and Hayton's Flor (1307) look back to the thirteenth century, and the Alishan table starts in 1219. The Step 0 for both worlds should say where the line falls.
- **The 1307 council.** The Latin acts in Mansi 25 name Catholicos Gregory and King Levon as convening the council of Sis. Ormanian says the catholicos died before the synod met and that Constantine III was then put in his place. Chamich puts a Sis council in 1342 answering Avignon's book of 117 "heresies". The Responsio ad errores impositos Hermenis in the RHC volume looks like the Latin side of that affair; this was not checked. Doc_02 should treat these as contested and tag them.
- **The Latin papal church.** The Sis and Adana acts are also in the Latin papal church's volume (V.14), and the Avignon letters to Cilicia are in a book in copyright. How the two worlds divide the union story is open.
- **The Church of the East under the Mongols.** Hayton's Book III is a Mongol history. The proposed rows put Het'um on that world as context. Whether it belongs there is for that world's builder.
- **Two catholicosates.** The census says Sis kept its own succession after 1441. Where that line is told afterwards is a later world's business, and nothing in this window's sources follows it.
- **Cyprus.** The Lusignan court and the Nicosia council are shared with the Maronite world (V.22). The Mansi 26 file and the Dardel chronicle sit between the two.
- **Hetum's rights.** The Bedrosian translation includes passages from Burger's 1988 edition. The lead may want to confirm the translator's declaration covers them before any quote is published.
- **The Armenian originals.** Under the September 2026 rule a clean original can be primary. No Armenian original in the library is clean. Say this plainly in Doc_02.

## 6. Step 0 scope notes and recommendation

**Floor (A1).** The census says the miaphysite confession is unchanged. Nothing found disturbs that. The Sis acts put the pressure toward Rome's feasts and rites ("in festis celebrandis, aliisque constitutionibus, et traditionibus suscipiendis"), not a change of creed, and the Avignon charges of 117 errors were answered. I read the acts' opening only.

**Sourcing (B1).** The census says "thin, but colophons are rich". The library can show the thinness and not the richness. The only colophon in a readable form is Langlois's last item. The rest of the colophon record is in Armenian in books still in copyright. What the library does hold is institutional: council acts, a court's history, a confessor's chronicle, a year-by-year table and late histories.

**Ecology (B2).** Two insiders (the court through Het'um; the church through the council acts) and one outside observer (Dardel). The resisting clergy of the census, who stiffened against union, appear in the acts and in Dardel only as the people the union failed to move. Grigor Tatevatsi has no text.

**Uniqueness (B3).** Against the earlier Cilician world the line is the year 1300. Against New Julfa (VI.28) it is the see at Etchmiadzin, which both worlds touch. Against the Latin papal church it is the union story. Each is a boundary to state.

**Audiences (B4).** Etchmiadzin and the Catholicosate of Cilicia are living seats. The Armenian diaspora is a large and reachable audience.

**Scale (B5).** About 13.7 MB vendored in eight files, of which the two RHC volumes are 8.6 MB and Mansi 25 is 3.6 MB. Eight placements in this world's staged rows plus seven on neighbouring worlds. Four cross-link rows touch this world. The best new item is Bedrosian's Het'um: clean public-domain English.

**Recommendation: open question.** The movement's own voice in the window is a council record in Latin, a court's history in clean English, and one colophon in French. The voices the census names (Tatevatsi, Kirakos, the scribes) have no usable text. A Representative would speak from the court and the council, which is a skewed picture of a church whose clergy resisted union. The choice to put to the lead is whether to fold this window into the earlier Cilician world, so that one world carries the Armenian line from 1080 to 1441 on the same sources, or to build it alone and say the colophons are missing. The sources support the first better than the second. This is a recommendation for Mark to weigh, not a decision.
