# Source Readiness Dossier — The Scandinavian Reformation Kingdoms

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** VI.27
**Corpus-map slug:** `scandinavian-reformation-kingdoms`
**Time window:** 1520s-1650 (census start 1527, end 1650)
**Region(s):** Denmark-Norway (including Iceland), Sweden-Finland
**Dossier author / date:** library/source-research thread, Era VII session, world VI.27 agent, October 2026
**Corpus-map / `cic/texts/` state as of:** October 2026, branch `library/era-vii-2026-10`. No
`cic/corpus-map/scandinavian-reformation-kingdoms.yaml` existed before this pass and the corpus held no
Scandinavian Reformation text. The five staging files below are written and pass
`corpus_map_merge.py --check` (15 assignments across 2 Atlas entries), not yet merged.

**Second pass, October 2026.** Two more files vendored with two staging files: Anjou's
History of the Reformation in Sweden in Mason's English (1859), and Bishop Glostrup's
visitations of Oslo and Hamar, 1617 to 1637 (Danish, 1895), the Norwegian church's own
record, extracted from a scan that binds a second book after it. The Danish side was searched
again: Palladius's Visitatsbog (1872) and the Danish Ordinantz of 1539 were found but their
Fraktur OCR is unreadable; Palladius's Latin catechism exposition for the Norwegian parish
priests (1552) is readable and is a new lead whose scan carries a ProQuest banner for the lead
to rule on; Tausen's scans were re-sampled and are still unusable. Google Books could not be
used this session (zero API quota, a 429 on the web search after one query). The vendored
leads moved from section 3 into section 1; section 6 revised.

## 1. Already assigned

Nothing was assigned to this world before this pass. A grep of every `Title:`
and `Creator:` header in `cic/texts/` for Sweden, Swedish, Danish, Denmark, Norway, Iceland,
Petri, Tausen, Bugenhagen, Gustav, Agricola, Finland, Scandinavia and Nordic found no
Scandinavian file. A grep of the bodies for Olaus or Olavus Petri, Bugenhagen, Hans Tausen,
Gustavus Vasa, Gudbrand, Jon Arason, Laurentius Petri, Uppsala Synod and Christian III
found only passing mentions (see section 2). Five files were vendored this pass and staged.

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Ordinatio ecclesiastica Regnorum Daniae et Norvegiae (Church Ordinance of 1537), Latin | danske-folkekirke | tradition | assigned | ~172K chars, Latin | `danske-folkekirke_ordinatio-ecclesiastica-lat_vinitor1537.txt` |
| Olavus Petri, Samlade skrifter vol. 1: the reform writings of 1526-1528 | olavus-petri | tradition | assigned | ~1.18M chars, Swedish | `olavus-petri_samlade-skrifter-v1-swe_hesselman1914.txt` |
| Olavus Petri, Samlade skrifter vol. 2: the Manual of 1529, the Swedish Mass, the hymns of 1536, the postil | olavus-petri | tradition | assigned (3 rows) | ~1.14M chars, Swedish | `olavus-petri_samlade-skrifter-v2-swe_hesselman1915.txt` |
| The Mass in Sweden (Yelverton, 1920): the masses of Olavus and Laurentius Petri, John III's Red Book, Charles IX's communion office, with English beside the Swedish | yelverton | tradition (2 rows); antecedent for the medieval Latin mass | assigned; antecedent provisional | ~458K chars, Latin, Swedish, English | `yelverton_mass-in-sweden-lat-swe-eng_yelverton1920.txt` |
| Upsala mötes beslut, 20 March 1593 (Företal and the articles) | bensow | tradition | assigned | ~265 lines of a 1.75M-char volume, Swedish | `bensow_svenska-kyrkans-bekannelseskrifter-swe_bensow1912.txt` |
| Konkordieboken in Swedish (the rest of the Bensow volume) | bensow | context here (Sweden adopted it only in 1663 and 1686) | provisional | ~1.5M chars, Swedish | same file |
| The History of the Reformation in Sweden (Anjou, 1850; Mason's English, 1859) | anjou | context (secondary narrative quoting the reformers and the diet acts in English) | assigned | ~1.57M chars, English | `anjou_history-of-the-reformation-in-sweden_mason1859.txt` (second pass) |
| Bishop Nils Glostrup's visitations of the dioceses of Oslo and Hamar, 1617 to 1637 (Daae and Huitfeldt-Kaas, 1895) | glostrup | tradition | assigned | ~0.28M chars, Danish; the Glostrup book only, extracted from a scan that binds a second book after it | `glostrup_visitatser-i-oslo-og-hamar-stifter-1617-1637-dan_daae-huitfeldt-kaas1895.txt` (second pass) |

The same files carry rows for the Wittenberg entry (`lutheran-wittenberg-and-its-congregations`,
VI.1): `tradition`, `needs-ruling` for the Ordinatio, Olavus Petri's volumes and the Petri masses
(see section 5), and `tradition`, `provisional` for the Swedish Book of Concord.

**Witness quality, stated plainly.** Olavus Petri vols. 1 and 2 (clean Swedish OCR, sampled at
four points), the Mass in Sweden (readable, sampled at four points) and Bensow (Projekt
Runeberg's proofread text) are ready to quote once each quote is checked against the page image.
The Ordinatio of 1537 is a Gothic-type scan with readable Latin but 4,791 long-s glyphs, 959
r-rotunda glyphs (a barred r after p, c and h) and scattered noise, sampled at five points; it is a
second witness for exact wording until a quote is checked against the page image, and the quote
gate has no mapping for the r-rotunda glyph (a ruling for the lead; the registry `apparatus`
mechanism is the likely home). The year of vol. 2 (1915) is the host date only; the OCR title page
prints no year. Bensow's square-bracket glosses in the 1593 text are the editor's, not the synod's.

The two second-pass files: Anjou reads clean (about 0.93) and is quotable once checked, but it
is a nineteenth-century narrative, placed as context, and its value is the English it gives for
the Swedish documents vendored in the original. Glostrup is the Norwegian church's own voice,
a bishop's parish visitations under the Ordinance a century after the Reformation, readable
seventeenth-century Danish (read by eye; the project has no Danish baseline) with the editors'
notes clean; primary in the original, quotable and renderable once checked against the page
image. The host scan binds a second Kildeskriftfond book (Storm's Historisk-topografiske
Skrifter, 1895) after the Glostrup book; the vendored file holds scan lines 1 to 9473, the
Glostrup book entire, and nothing of the second.

**Scale.** About 4.7 million characters in five files: 4.1M Swedish, 0.17M Latin, 0.46M mixed
Latin, Swedish and English. The Swedish side is deep; the Danish-Norwegian side is one Latin
ordinance; Iceland and Finland have no vendored text.

## 2. Cross-link opportunities

Every vendored file whose body mentions the figures above was listed and the hits read.

- **The Augsburg Confession** in `melanchthon_augsburg-confession_anon-pg275.txt` and in
  `book-of-concord_symbolical-books-evangelical-lutheran-church_jacobs1911.txt` (Part II from
  line 1374, the Apology from 3270). The Uppsala Synod of 1593 committed Sweden to the three
  ecumenical creeds and the unaltered Augsburg Confession (Bensow's note, line 31696 of the
  Bensow file), and the Ordinance of 1537 presupposes it. Tier: same time-place for what the
  Swedes adopted; the text itself is the authority this world argued from. Rows proposed in
  `crosslink_fragment.yaml` (`antecedent`, `provisional`). The rest of the Jacobs volume, the
  Formula of Concord (1577), was adopted in Sweden only in 1663 and 1686 (Bensow), after the window.
- **Calvin's Letters, vol. IV** (`calvin_letters-vol4_bonnet1858.txt`): DXXVI to Martin Micronius
  (line 1305, "Progress of the Reformation in Sweden") and DXXVII to the Prince Royal of Sweden
  (line 1424, Geneva, 26 February 1559), with Bonnet's note on Gustavus Wasa and Eric XIV
  (line 1438) and the dedication of the Commentary on Hosea to Gustavus Wasa. Tier: same
  time-place (an outside Reformed witness to the Swedish court). Row proposed (`context`,
  `assigned`). Vol. I carries a one-line footnote on Christian III (line 5752, "who introduced
  the Reformation into his States"); no row.
- **Knox, Works vol. II** (`knox_works-v2_laing1895.txt`, line 13666): a footnote on Eric XIV of
  Sweden as a suitor of the Scottish queen, with his accession on Gustavus Vasa's death in 1560.
  Tier: same time, different region. A passing reference; no row.
- **Council of Trent, Canons and Decrees (Waterworth)** (line 2907) names Bugenhagen as Luther's
  associate at Wittenberg in a note; no link to this world. Tier: out-of-window of the
  Scandinavian material. No row.
- **Schwenckfeld, Corpus Schwenckfeldianorum vol. 1** (lines 5284, 20724, 27328): Bugenhagen as a
  Wittenberg figure in the Silesian story, and a Pomeranian princess; not Scandinavian. No row.
- **Luther's Works, selected (Jacobs-Spaeth), vol. 1** has one hit for Denmark or Sweden; not
  opened beyond the hit. The Wittenberg bucket already holds the Luther texts; a build that
  wants Luther's own exchange with the Danish court (the ordinance preface says the draft went
  to him) should search them.
- **The Jesuit Latin volumes** (Lainez, Nadal, Polanco, Borgia) were not searched for the Swedish
  mission of the 1570s-80s under John III (the Red Book is in the Yelverton file, whose text
  discusses whether a Jesuit wrote it, at about line 4558). A build wanting the Catholic side of the Red
  Book dispute should look there. Tier: same time-place, not opened.

## 3. Verified acquisition leads

Public-domain editions found on the Internet Archive, each checked on October 2026 by reading the
host metadata and the title page or imprint in the fetched OCR (method per row). Rows for each
are in `seed_fragment.yaml`. The first five were vendored.

| title | author | translator | year | url | rights basis | verified by (method + date) |
|---|---|---|---|---|---|---|
| Ordinatio ecclesiastica Regnorum Daniae et Norvegiae et Ducatuum Sleswicensis Holtsatiae etcet. | Danske folkekirke (in the name of Christian III); printer Johannes Vinitor | none (Latin) | 1537 | `archive.org/details/ordinatioecclesi00dans` | pd-us-by-date; no rights field, no access restriction; Boston Public Library | metadata, full text, title page and colophon read, five-point sample, October 2026. VENDORED. |
| Samlade skrifter af Olavus Petri, vols. 1 and 2 | Olavus Petri; ed. Bengt Hesselman | none (Swedish) | 1914, 1915 | `olavuspetri0001unse`, `olavuspetri0002unse` | pd-us-by-date; no rights field; Internet Archive | metadata, full text, contents read, four-point sample, October 2026. VENDORED. Vol. 2's year is the host date only. |
| The Mass in Sweden, its development from the Latin rite from 1531 to 1917 | E. E. Yelverton | Yelverton | 1920 | `massinswedenitsd00petr` | pd-us-by-date; no rights field; PIMS, University of Toronto | metadata, title page "1920" read, contents read, four-point sample, October 2026. VENDORED. |
| Svenska kyrkans bekännelseskrifter (with Upsala mötes beslut 1593) | Oscar Bensow (ed.) | none (Swedish) | 1912 | `arkivkopia.se-runeberg-bekann12` | pd-us-by-date; no rights field; Arkivkopia copy of Projekt Runeberg | metadata, text, title page "1912" read, the 1593 text read, October 2026. VENDORED. |
| Svenska kyrkoreformationens historia (the Swedish original of Anjou, 1850) | L. A. Anjou | none (Swedish) | 1850 | `svenskakyrkoref01anjogoog`, `svenskakyrkoref00anjogoog` | pd-us-by-date; NOT_IN_COPYRIGHT | Google scans, not opened beyond the OCR header, October 2026. The English (1859) was vendored in the second pass (section 1). |
| The National Church of Sweden (Hale Lectures, 1910) | John Wordsworth, Bishop of Salisbury | none | 1911 | `archive.org/details/nationalchurchof00wordrich` | pd-us-by-date; NOT_IN_COPYRIGHT; University of California | metadata, title page read, text fetched (1.13M chars), October 2026. Not vendored. An Anglican outside witness. |
| Diplomatarium Islandicum (Íslenzkt fornbréfasafn), vol. 11, A.D. 1310-1544 | Hið íslenzka bókmentafélag | none (Icelandic) | 1915 (Reykjavik) | `archive.org/details/diplomatariumisl11kaup` (vol. 10: `diplomatariumisl10kaupuoft`) | pd-us-by-date; no rights field; Robarts, University of Toronto | metadata, title page read, text fetched (1.96M chars), "ORDINANZIA 1542" heading at line 6346, October 2026. Not vendored. The body runs on to 1549. The Jon Arason letters were not isolated: the OCR spells his name in several forms. |
| Samlade skrifter af Olavus Petri, vols. 3 and 4 | Olavus Petri | none (Swedish) | 1916, 1917 (host dates) | `olavuspetri0003unse`, `bwb_T3-BUN-536` | pd-us-by-date; no rights field | metadata and contents pages, October 2026. Not vendored. Vol. 4 holds the Chronicle, Sielenes tröst and Tobie comedia. |
| Inbjudningsskrifter ... trehundraårsminnet af Upsala möte (essay on the Swedish church reformation and the Uppsala meeting 1593) | S. E. Henschen, A. N. Sundberg and others | none (Swedish) | 1893 | `archive.org/details/inbjudningsskri00univgoog` | pd-us-by-date; NOT_IN_COPYRIGHT; Harvard (Google scan) | metadata, text fetched (758K chars), essay heading at line 358, October 2026. Secondary. Not vendored. |
| Käsikiria castesta ia muista christikunnan menoista (Agricola's Finnish Manual) | Mikael Agricola | none (Finnish) | 1549 | `archive.org/details/kasikiria-1549` | Public Domain Mark 1.0 on the item; also pd by date | metadata, text fetched (138K chars), three-point sample (readable, long-s), October 2026. Not vendored. Other Agricola items on the host: `rucouskiria-1544`, `p107-06_messu`, `P2106SeWsiTestamentti`, `psalteri` (not opened). |
| Brevis expositio catechismi pro parochis Norvegianis, per Petrum Palladium, cum praefatione Philippi Melanchthonis | Peder Palladius | none (Latin) | 1552 (Veit Kreutzer, per the host) | `archive.org/details/den-kbd-pil-130018161541-001` | pd-us-by-date for the 1552 print; the item carries no rights field and every page of the OCR carries the banner "Early European Books, Copyright 2009 ProQuest LLC. Images reproduced by courtesy of the Royal Library, Copenhagen", so the scan's status is for the lead to rule (INTAKE section 2) | Second pass, October 2026: metadata read; text fetched (136 KB) and sampled at five points, readable Latin with long s as f (about 0.50 against the project's Latin baseline), ninety-eight banner lines. The Danish-Norwegian church's own voice beyond the Ordinance, for Norway's parish priests, with Melanchthon's preface. Not vendored on the rights question. |
| Olavus Petri, the Church Reformer of Sweden | Nils Forsander | none | 1918 | `archive.org/details/olavuspetrichur00forsgoog` | pd-us-by-date; "COPYRIGHT, 1918" read; NOT_IN_COPYRIGHT | metadata, OCR, October 2026. Secondary English biography. Not vendored. |

**Public-domain English beside the non-English texts.** Found for the Swedish Mass (Yelverton, 1920,
vendored). Not found for the Ordinance of 1537, the Uppsala decisions of 1593, the Manual of 1529
or Olavus Petri's tracts. These gaps are recorded in section 4.

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Kirkeordinansen 1537/39, the Danish draft and the Danish ordinance of 1539 (`kirkeordinansen10000unse`, Akademisk Forlag, 1989) | The Danish text of the 1539 ordinance | 1989 edition, access-restricted (lending), in copyright. No 19th-century printing of the 1539 Danish text was found. |
| Royal Library Copenhagen scan of the Ordinatio (`den-kbd-pil-130018152623-001`) | A second witness for the 1537 Latin | Fetched: the Fraktur is read as other letters ("TftDinaao", "£ccleftafttea"), and every page carries a ProQuest banner. The Boston scan was vendored. |
| English translation of the 1537 ordinance | The brief asks for English beside every non-English text | Title searches on "church ordinance" with Denmark or Danish, "Kirkeordinans" and "Ordinatio" returned only the two Latin scans and the 1989 Danish volume. E. H. Dunkley, The Reformation in Denmark (SPCK 1948; `reformationinden0000ehdu` and several more scans) is a 1948 history in copyright. No public-domain English found. |
| Danske Kirkelove (Rørdam, 1883-89) | The census lists Danish church law; the brief names it | archive.org title searches "kirkelove", "Danske Kirkelove", the creator "Rørdam, Holger Frederik" (the University history, Monumenta historiae danicae, Lamentatio ecclesiae and others; nothing titled Kirkelove) and a free-text search returned nothing. The Google Books API returned a quota error, so that host was not searched. Not found. |
| Hans Thomissøn, Den danske Psalmebog (1569) and a modern edition | The census names hymnals; the brief names it | The only Thomissøn items found are five Royal Library prints of sermons and consolation tracts of 1570-73 (`den-kbd-pil-130018166489-001` to `-005`), not opened. No hymnal and no modern edition of 1569 was found. Open as a lead for another host. |
| Hans Tausen, Smaaskrifter (Rørdam 1870) | Tausen's own pamphlets, public domain by date | Both scans (`smaaskrifterafha00taus`, `smaaskrifter00tausgoog`) read the Fraktur as Latin letters ("tøom", "tlje", "Ijanb"); the 16th-century Danish is unusable as text. Kept in section 3's seed as a lead for a clean transcription. Also seen, not opened: Tausen's translation of Menius, Oeconomia Christiana (1538, `den-kbd-pil-130017586409-001`, Royal Library). Second pass, October 2026: `smaaskrifterafha00taus` re-fetched and sampled at five points, still unreadable at every point; a creator search for Tausen and Tavsen on archive.org found no other scan; Google Books could not be searched. Still a lead for a clean transcription. |
| Peder Palladius, En Visitatz Bog (ed. Svend Grundtvig, Samfundet til den danske literaturs fremme, 1872; `envisitatzbogin00fremgoog`, NOT_IN_COPYRIGHT) | The bishop of Zealand's visitation book of the 1540s, the classic Danish source for the ordinary parish | Second pass, October 2026: metadata read, text fetched (550 KB) and sampled at five points. The 1872 edition prints the old text in Fraktur, which the OCR reads as Latin letters ("bem aff jtælenc c førbe bem"); only the editor's notes in roman type read. Unusable as text; a lead for a clean transcription, like Tausen. |
| En Ordinantz hvorledis Kirketjenesten skal holdes udi Danmarks og Norges Riger (the Danish Ordinance of 1539, Royal Library `den-kbd-pil-130017049802-001`, printer Hans Barth; the host attributes the translation to Palladius with a query) | The Danish text of the 1539 ordinance, which the first pass found only in the 1989 edition | Second pass, October 2026: metadata read (no rights field, early-european-books collection), text fetched (162 KB) and sampled: Fraktur read as noise at every point (about 0.35 of tokens match any Dutch word, by letter chance). Also seen in the same search: "Den rette Ordinants" printings of 1553, 1562 and 1574 (`den-kbd-pil-130018150655-001` and siblings), not opened. Closed as a text; the Latin Ordinatio of 1537 stays the vendored witness. |
| Palladius, Formula visitationis provincialis seu praepositorum (1555, `den-kbd-pil-130018161576-001`) | The superintendent's own Latin visitation formula | Second pass, October 2026: text fetched (71 KB) and sampled: garbled at every point (about 0.35), unlike the 1552 catechism exposition (section 3). Closed as a text. |
| Merle d'Aubigné, History of the Reformation in Europe in the Time of Calvin, vol. VII: Geneva, Denmark, Sweden, Norway (1876; `india.history.resource.86661`) | The only English narrative of the Danish Reformation the title search found | Secondary and not opened; a nineteenth-century Genevan historian, not a Scandinavian source. Noted so the next search does not repeat it. |
| Schaff, Creeds of Christendom vol. 3 (`bibliothecasymbo03scha`) | The brief names it for the Swedish confessions | Full text fetched (2.5M chars): no hit for Sweden, Swedish, Denmark, Danish or Upsala. It has no Scandinavian confession. (Its Augsburg Confession is already in the corpus in other renderings.) |
| Kurtzer Bericht von dem Concilio in Upsal, Anno 1593 (Greifswald, 1693; `MN40301ucmf_14`) | A German account of the synod printed a century later | Microfilm of 22K characters of Fraktur read as Latin letters; garbled. Not usable. |
| Uppsala 1593 as a separate acta printing | The census says the acta are "verified" | Title searches "Upsala möte", "Uppsala möte 1593" found only Henschen's 1893 invitations (section 3). The decisions were found inside the Bensow volume and vendored. |
| Laurentius Petri's Church Order of 1571 as its own text | The brief names it | Creator and title searches returned nothing. Yelverton prints its mass (book pp. 49-64) with English. The Swedish ordinance text itself is not vendored. |
| English of Olavus Petri's Manual of 1529: O. V. Anderson, The Church Manual of Olavus Petri (Rock Island, Augustana Book Concern; `churchmanualofol00petr`) | The only English translation of the Manual; the host dates it 1930 | The OCR title page prints no year, and the translator's bibliography cites works of 1933, 1935 and 1936 (lines 2859, 2877, 2885). It cannot be 1930, and no earlier date is shown. Not shown to be public domain; not vendored. |
| Yelverton, The Manual of Olavus Petri 1529 (SPCK, 1953; `bwb_C0-AVR-752`, `manualofolavuspe0000eric`) | Another English of the Manual | 1953, in copyright; the first is access-restricted. |
| Conrad Bergendoff, Olavus Petri and the Ecclesiastical Transformation in Sweden (Macmillan 1928; `olavuspetrieccle0000berg` and variants) | The standard study in English | Scholarship, not a source; the scans are lending-library items (the 0000 identifier family) and the 1965 reprints are in copyright. Never vendored. |
| Gudbrand's Bible (1584) and the preface | The census/brief name it | Archive.org holds only modern retypings (`nyja-testamentid-gudbrandsbiblia`, `gudbrandsbiblia-2026`, `gudbrandsbiblia-2026-numerud-og-vidbaett`, Kristnar Bækur) whose licence and edition are unclear. No 1584 facsimile found. Not vendored. |
| The Danish Bible of 1550 (`1550-king-christian-iii-bible`, Christian Pedersen) | The Danish vernacular Bible under Christian III | A user upload of a 2.1 GB scan with 4.8M characters of OCR; out of scale for the corpus. Not opened. |
| Oddur Gottskálksson's Icelandic Bugenhagen translations: Historia Pinunnar (1558, `den-kbd-pil-130018148235-001`, Royal Library) and Gudspjöll og Pistlar (`GudspillogPistla000816902v0HelgReyk`, National and University Library of Iceland) | Icelandic liturgical books of the Danish ordinance | Metadata only; not opened, rights of the Icelandic item not stated on its page. Open as leads. |
| Jon Arason's letters and Skalholt, 1550 | The census cites the Skalholt story | No separate edition found. The letters are inside the Diplomatarium Islandicum (section 3). Gunnar Gunnarsson's Jon Arason (host date 1930, Danish, `bwb_KU-153-868`) is a twentieth-century book, not a source, and was not opened. |
| Butler, The Reformation in Sweden (1883; `reformationinsw00butl` and variants) | Another English narrative | Seen in the search list (NOT_IN_COPYRIGHT); not opened. Anjou (section 3) is the narrative lead. |
| Cornelius, Svenska kyrkans historia efter reformationen (1886; `svenskakyrkansh00corngoog`) | Swedish church history after the Reformation | Seen only; secondary; not opened. |
| Project Runeberg's Samlade skrifter of Olavus Petri (`arkivkopia.se-runeberg-opetri`, 128K chars) | A cleaner Runeberg text of Olavus Petri | Fetched header only: 128K characters against 1.2M per volume of the Hesselman edition; it is a partial extract. The full volumes were vendored. |

## 5. Open cross-world questions

- **Lutheran Wittenberg (VI.1) and this world.** The census windows overlap (VI.1: 1517-1580,
  "Saxony, then N. Europe"; VI.27: 1520s-1650). The Ordinance of 1537 was drafted with Bugenhagen
  and approved at Wittenberg; Olavus Petri studied there and built the Swedish church on its models;
  the Uppsala Synod adopted the Augsburg Confession. Whether these texts are Wittenberg's voice
  or only this world's is the mapping decision. The staging rows for VI.1 are `needs-ruling` and
  `tradition`; the Swedish Concordia is `provisional`. Whoever builds either entry should settle,
  once, which world reads them as voice and which as context. This is also the census's own "part of
  another world" question for VI.27 (section 6).
- **The Tridentine Church (VI.22) and the Red Book of John III.** The Red Book of 1576 was a
  liturgy that moved toward Catholic usage under a king with Jesuit contacts; Yelverton prints it
  and says the Uppsala meeting of 1593 forbade its further use (line 4679). The Jesuit Latin volumes in the corpus may hold the
  Catholic side. No row proposed.
- **Finland.** The census names Agricola. No Agricola text is vendored; the Manual of 1549 is
  a verified lead (section 3). Whether Sweden-Finland is one world or the Finnish church a separate
  voice is for the build.
- **Iceland and Norway.** Both are in the window by the census. Iceland has only the
  Diplomatarium lead; Norway has the Ordinance (shared with Denmark) and the Glostrup visitations
  lead. Whether the world's sources can speak for them as well as for Denmark and Sweden is for
  Doc_01 to decide.
- **The Anabaptists (VI.3) and Schwenckfelders (VI.15).** The Formula of Concord (Jacobs) condemns
  both; the Swedish Concordia in the Bensow file repeats that, but Sweden adopted it only after the
  window. No row proposed here.

## 6. Step 0 scope notes and recommendation

**Floor (A1).** The census floorNote reads "No question". The Uppsala decision commits the Swedish
church to the three ecumenical creeds and the unaltered Augsburg Confession, and the Ordinance of
1537 was sent to Luther for approval; nothing seen this pass raises a creedal question. A Doc_01
should disclose a historical point, not a doctrinal one: in both kingdoms the reformation came from
the crown and the diet, not from below.

**Sourcing (B1) and ecology (B2).** The census calls this "rich institutionally". The test supports
that for Sweden and only in part for the rest. Sweden has a deep, clean, primary run in its own
language: the Reformation's leading writer in four volumes (two vendored), the first vernacular
Manual, Mass and hymns, the Petri masses with English, and the Uppsala acta of 1593. Denmark-Norway
has the founding ordinance, but only as a Latin scan with systematic glyph noise. The Danish
voice beyond the ordinance (Tausen, Thomissøn's hymnal, the Kirkelove) was found only as garbled
scans or not found, and every Danish and Norwegian vernacular text is a lead or a gap. Iceland and
Finland are leads. The ordinary voice the census promises (hymnal tradition and visitation records)
is in hand for Sweden (the hymns of 1536 in vol. 2) and, after the second pass, for Norway
(Glostrup's visitations of 1617 to 1637, the bishop's own Danish). There is no
public-domain English for the Ordinance, the Uppsala decisions, the Manual or the tracts, so a
build would work from the Swedish and Latin originals, which the intake rules allow as primary;
Anjou's narrative (1859) now gives an English cross-check for the Swedish side. The Danish
vernacular voice is still missing: Tausen, Palladius's Visitatsbog and the Danish Ordinantz all
exist on the host only as unreadable Fraktur OCR, and the one readable Danish-side voice found,
Palladius's Latin for the Norwegian priests, waits on a rights ruling.

**Uniqueness (B3).** The sibling most like it is the Lutheran Wittenberg entry (VI.1), which shares the
confession and the Wittenberg models. This world differs in its mechanism (the crown and the diet
imposing and then teaching a church, with a state church that lasted) and in its language, and
nothing in VI.1's sources is Scandinavian. Overlap is in the confession, not in the sources. The
Scandinavian Conversion entry (III.14) ends in 1104, and the Haugean and Laestadian entries start
after 1796.

**Audiences (B4).** The Church of Sweden, the Church of Denmark, the Church of Norway, the Church
of Iceland and the Evangelical Lutheran Church of Finland are living bodies whose national memory
is built on this period; Lutheran emigrant churches in North America (the Augustana Synod that
published two of the English books found here) keep it too. A real audience exists.

**Scale (B5).** About 6.6 million characters in seven vendored files after the second pass (4.7M
in the first five), plus verified leads of about 5 million characters (Wordsworth, Diplomatarium
vol. 11, Agricola, Olavus Petri vols. 3 and 4, Palladius's Latin). Mid-size by the library's
scale, Swedish-heavy.

**Recommendation: build.** Unchanged by the second pass. The Swedish half of the world's own voice
is vendored, clean and primary, the floor is clear, and the window and mechanism are distinct
from Wittenberg's. The second pass added Norway's own voice (Glostrup) and an English narrative
for Sweden (Anjou), and confirmed that the Danish vernacular is not reachable as text on the
hosts this sandbox can use. The census's "institutionally rich" holds for Sweden, for the
Ordinance and now for Norway's visitations, not for the Danish vernacular, Iceland or Finland,
so the world should be scoped to Sweden and Denmark-Norway at Doc_01 and treat the thin edges as
honest limits. What is still worth doing before Doc_02 is a rights ruling on the Royal Library
scans (Palladius 1552) and a clean transcription of Tausen or the Visitatsbog from a host this
sandbox cannot reach. This is a recommendation for Mark, not a decision.
