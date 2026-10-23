# Source Readiness Dossier — The Kyiv-Mohyla Orthodox Revival

See `Build/worlds/_cross-world/SOURCE-READINESS.md` for what this is and
why it exists.

**Atlas ID:** VI.21
**Corpus-map slug:** `the-kyiv-mohyla-orthodox-revival`
**Time window:** 1615–1700
**Region(s):** Kyiv (North Europe region; lane 3, Greek East and Orthodoxy)
**Dossier author / date:** source-research thread, one-world agent, 2026-10-23 (the Era VII session began 2026-10-16; this agent's run was cut off by the usage limit and finished 2026-10-23)
**Corpus-map / `cic/texts/` state as of:** 2026-10-23. Three files are assigned to the bucket (§1). Five more are vendored and staged in `cic/corpus-map/_staging/`, pending the lead's merge.

Census block (VI.21): sourcing "Moderate-to-rich: academy records, catechisms, brotherhood statutes"; floor note "No question". The library check below finds the sourcing note more hopeful than the corpus. The Confession and a Kyiv polemic are in. The catechism of 1645, the Trebnyk of 1646 and the Mohyla Collegium's own statutes are not (§4).

## 1. Already assigned

**In `cic/corpus-map/the-kyiv-mohyla-orthodox-revival.yaml` (three files, merged):**

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| The Orthodox Confession (Confessio Orthodoxa), Greek with Latin | mogila | tradition | assigned | ~199,000 words in the whole volume, Greek about a third | `monumenta-fidei-ecclesiae-orientalis_confessions-grc-lat_kimmel1850.txt` |
| The Orthodox Confession, English version (Overbeck 1898, a lightly modernised 1762 English) | mogila | tradition | assigned | ~55,500 words | `mogila_orthodox-confession_overbeck1898.txt` |
| The Orthodox Confession, the untouched 1762 English with Nectarius's letter | mogila | tradition | assigned | one volume | `mogila_orthodox-confession_anon1762.txt` |

The 1762 file was vendored by the Orthodoxy under the Ottomans pass (VI.17) and already carries this world's row.

**Vendored this pass and staged (five files, pending merge):**

| work | author | role | confidence | approx. scale | source file |
|---|---|---|---|---|---|
| Golubev, *Kievskii mitropolit Petr Mogila i ego spodvizhniki*, vol. 1 (1883): narrative, and the documentary appendix "Materialy dlia istorii zapadno-russkoi tserkvi" from 1540 | golubev | context (narrative); tradition (appendix) | assigned (narrative); provisional (appendix) | ~290,000 words, Russian; documents in Ruthenian, Polish, Latin | `golubev_petr-mogila-i-ego-spodvizhniki-t1-rus_1883.txt` |
| Golubev, vol. 2 (1898): Mogila's rule 1633–1647, the polemics of his circle, the church governed; "Prilozheniia" of dated documents | golubev | context; tradition | assigned; provisional | ~336,000 words | `golubev_petr-mogila-i-ego-spodvizhniki-t2-rus_1898.txt` |
| *Russkaia istoricheskaia biblioteka* vol. 4, *Pamiatniki polemicheskoi literatury v Zapadnoi Rusi* (1878): Kopystenskii's *Palinodiia* (1621–1622), Krevza's *Oborona uni* (1617), the diary of Afanasii Filippovich (1646), the Kyiv council of 1640 as told by Sakovych, the epistles ascribed to the elder Artemii | kopystenskij, krevza, filippovich-afanasii, kyiv-council-1640-sakovych-account, artemii-starets | tradition, context | assigned or provisional by item | ~433,000 words | `russkaya-istoricheskaya-biblioteka_pamyatniki-polemicheskoi-literatury-zapadnoi-rusi-t4-rus_giltebrandt1878.txt` |
| Schaff, *Creeds of Christendom* vol. 2 (1878): Mogila's Confession Part I in Greek and Latin; Dositheus; Philaret's Longer Catechism in English | mogila, dositheus, philaret | tradition | assigned | ~213,000 words | `schaff_creeds-of-christendom-v2-greek-latin-creeds_1878.txt` |
| *Sinopsis* (the Kyiv Synopsis), St Petersburg printing, 1762 | kyiv-synopsis | tradition | assigned | ~40,000 words, Church Slavonic | `kyiv-synopsis_sinopsis-chu_1762.txt` |

What each file is, honestly:

- **The Confession** now has three witnesses to its wording (Kimmel, Schaff for Part I only, and the English of 1762 and 1898) and is the world's charter. Kimmel's Greek OCR is partial and Schaff's has the same kind of accent errors, so the Greek is a second witness until checked on page images. The Latin and the English are clean. Note that the same text is also the charter of VI.17 (Orthodoxy under the Ottomans); the weight each world gives it is for the builds to settle (§5).
- **Golubev** is a scholar's narrative with printed documents. The narrative is readable. The Latin and Polish documents and the Church Slavonic ones are garbled in the OCR. Both volumes are second witnesses. Golubev's own plan for a third volume (Mogila's schools and enlightenment work) is named in volume 2 and is not on the host.
- **The Archaeographic Commission volume** carries the only printed *Palinodiia* in the corpus and the Uniate text it answers. The Ruthenian and Slavonic read well. The Polish quotations are garbled. The Kyiv council of 1640 appears there only as Sakovych reported it. He had left the Orthodox, so that item is a hostile report, not the council's own record.
- **Schaff** is a compendium; only the Mogila, Dositheus and Philaret parts matter here. The English of Philaret's catechism is R. W. Blackmore's (1845), not Schaff's.
- **The Synopsis** is the Kyiv circle's own short history. This is the 1762 St Petersburg printing, not a Kyiv one. The attribution to Innokentii Gizel is the host's and the tradition's, not the title page's.

Scale: about 1.3 million words were vendored this pass, of which about 1.1 million are Russian, Ruthenian, Slavonic, Polish or Latin and nothing is in English except Schaff's compendium and the Confession already in hand. There is no public-domain English for any of the five (§4).

## 2. Cross-link opportunities

Checked 2026-10-23. Method: a case-insensitive search of every vendored `.txt` for Kyiv, Kieff, Kiew, Mogila, Mohyla and spelling variants; every file with more than a handful of hits was opened at the hit lines. Proposed rows are in the agent's `crosslink_fragment.yaml` for the lead to add to the existing staging files.

- **Robertson 1899, Acts and Decrees of the Synod of Jerusalem.** `dositheus_acts-and-decrees-synod-jerusalem_robertson1899.txt`. At about line 3911 "Peter Mogilas, humble Archbishop, Metropolitan of Kieff" signs the Constantinople synodal decree against Lucar's chapters for "all the Orthodox and Catholic Church of Christ that is in Little Russia"; the Kyivan bishops sign after him (3918–3930). Lives in the Ottoman Orthodoxy bucket. Tier: same time-different-region (Constantinople), same people. Role: context, assigned.
- **Guépin, *Un apôtre de l'union des Églises* (1897).** `guepin_apotre-de-l-union-des-eglises-fra_1897.txt`. Mohyla appears in 82 lines. Read at about lines 36724 and 37128–37150 (the 1627 Kyiv meeting of Smotrycki and Borecki, Mohyla as archimandrite of the Caves, the favourable words Guépin gives him). The index (lines 55832–56074) lists "Violences de Mohyla et des Cosaques contre les Uniates" and "Velléités de conversion de Pierre Mohyla". A Catholic biographer's hostile view. Lives in the Union of Brest bucket. Tier: same time-place. Role: context, provisional.
- **Pelesz, *Geschichte der Union*, vol. 2 (1880).** `pelesz_geschichte-der-union-bd2-deu_1880.txt`. 33 hits. At lines 14588–14712 Mohyla takes the see from Kopinskii (the file's account) and is called the "moralischen Mittelpunkt" of the Orthodox side's efforts. A Greek Catholic historian's view. Union of Brest bucket. Tier: same time-place. Role: context, provisional.
- **Harasiewicz, *Annales Ecclesiae Ruthenae* (1862).** `harasiewicz_annales-ecclesiae-ruthenae-lat_1862.txt`. Eight hits. One episode read at lines 16757–16780: Bishop Methodius Terlecki of Chelm refuses Mohyla's greeting. Union of Brest bucket. Tier: same time-place. Role: context, provisional; a pointer more than a source.
- **Lucaris, *Lettres anecdotes* (Amsterdam 1718).** `lucaris_lettres-anecdotes-fra_amsterdam1718.txt`. Lines 28872–28873 and 29099–29118 print Mogilas's signature and an editor's remarks on it. Ottoman Orthodoxy bucket. Tier: same time-different-region. Role: context, provisional (a partisan witness).
- **Brest agent's own proposal for the Commission volume.** The Union of Brest pass proposed three Brest rows for `russkaya-istoricheskaya-biblioteka_..._t4_...` from its header. This agent's staging file for that volume already carries Brest rows for Krevza, Filippovich and Kopystenskij, read from the text, so that proposal is covered. The Kyiv council row there is attributed to Sakovych's account, not to Vassian (the running heads read "po razskazu Sakovicha"; the Brest note read the contents list, whose narrator name the OCR garbles).
- **Checked and not linked:** `theiner_vetera-monumenta-poloniae-lithuaniae-v3-lat_1863.txt` (15 hits for "Mogila" in papal letters of the 1580s, which name an abbey, "Clarae Tumbae in Mogila", and a place dateline, not Mohyla); `smith-thomas_account-of-the-greek-church_1680.txt` (lines 12685–12745 on the Ruthenian churches and the Union of 1595, before the window; Brest thread's call); `avvakum_life-of-archpriest-avvakum_harrison-mirrlees1924.txt` ("poor little Russians" at line 742 is not about Kyiv scholars); `herberstein_notes-upon-russia-v1_major1851.txt` (Kyiv of the princes, 1500s); the Jesuit Institutum (Kiewicz is a surname).
- **Out of window, for completeness:** none needed.

## 3. Verified acquisition leads

All rows checked on archive.org by metadata fetch on 2026-10-23, and by opening the OCR where marked. "Vendored" rows are in `cic/texts/` (§1).

| title | author | translator/ed. | year | url | rights basis | verified by |
|---|---|---|---|---|---|---|
| Kievskii mitropolit Petr Mogila i ego spodvizhniki, vol. 1 | Stefan T. Golubev | none | 1883 (host) | archive.org `kievskijmitropolitpetrmogilaiegospodvizh97` | pd-us-by-date; no host rights field | metadata, five-point OCR sample. **Vendored.** |
| Kievskii mitropolit Petr Mogila i ego spodvizhniki, vol. 2 | Stefan T. Golubev | none | 1898 (host) | archive.org `kievskijmitropolitpetrmogilaiegospodvizh7` | pd-us-by-date; no host rights field | metadata, five-point OCR sample. **Vendored.** |
| Russkaia istoricheskaia biblioteka vol. 4 (Pamiatniki polemicheskoi literatury v Zapadnoi Rusi, book 1) | Archaeographic Commission | P. A. Giltebrandt | 1878 (title page read) | archive.org `russkajaistoricheskajabibliotekaizdavae2` (same volume as `pamyat1878`, not fetched) | pd-us-by-date | title page, contents, five-point sample. **Vendored.** |
| The Creeds of Christendom, vol. 2 | Philip Schaff | Schaff | 1878 (title page: Harper, entered 1877) | archive.org `creedsofchristen02scha` (NYPL copy) | pd-us-by-date; host NOT_IN_COPYRIGHT | title page, five-point sample. **Vendored.** |
| Sinopsis (Kyiv Synopsis), St Petersburg printing | anon. (host: Innokentii Gizel) | none | 1762 (host) | archive.org `sinopsisilikratkoeopisanieotrazlichnyhle85` | pd-us-by-date; no host rights field | title page in OCR, five-point sample. **Vendored.** |
| Razsuzhdenie o knige imenuemoi Pravoslavnoe ispovedanie very | Aleksei Bolkhovskii | none | 1804 (title page read) | archive.org `razsuzhdenieoknigeimenuemojpravoslavnoe63` | pd-us-by-date; no host rights field | title page read; about 12,000 words, five-point sample partly garbled. Not vendored: a discourse about the Confession, not the Confession. |
| Orthodoxos homologia (Greek, Latin and German), ed. C. G. Hofmann | Mogila, with Meletios Syrigos | Hofmann | 1751 | archive.org `orthodoxoshomol00syrigoog` | pd-us-by-date; host NOT_IN_COPYRIGHT | metadata and five-point sample: German Fraktur and Greek both garbled. Not vendored; Kimmel and Schaff hold the same text more cleanly. |
| Epanorthosis abo perspektiwa (Kraków) | Kasiian Sakovych | none | 1642 | archive.org `epanorthosisabo00sakogoog` | pd-us-by-date; host NOT_IN_COPYRIGHT | metadata and five-point sample: blackletter Polish garbled at all five points. Not vendored. The Uniate polemic that the Kyiv *Lithos* (1644) answers. |
| The Doctrine of the Russian Church (Philaret's catechisms), Blackmore's English | Russian Orthodox Church | R. W. Blackmore | 1845 | archive.org `doctrineofrussia00blac` | pd-us-by-date; host: "The Library of Congress is unaware of any copyright restrictions" | metadata only. Not vendored; Schaff already prints the same English. For the Russian Church entries. |
| Akty, otnosiashchiesia k istorii Iuzhnoi i Zapadnoi Rossii, vols. 1, 3 and 4 | Archaeographic Commission | none | 1863, 1861, 1863 | archive.org `auzr01`, `auzr03`, `auzr004` | pd-us-by-date; no host rights field | metadata and word counts only (contents not read). Vol. 1: 96 lines mention brotherhoods, year tokens mostly 1570–1592. Vol. 3: years 1645–1656. Vol. 4: 1657–1659. None looks like the 1615–1647 span. Not vendored; the series volumes for those years were not found. |

## 4. Checked and closed

| candidate | why it looked promising | why it's closed |
|---|---|---|
| Mohyla's Short Catechism of 1645 (Polish *Zbior krotkiey nauki*, Ruthenian *Katekhizis*) | Named in the brief as the world's catechism | archive.org searches 2026-10-23 on "Zbior krotkiey nauki", "Katechizm krótki", "Katechizis Mohyla", "Катихизис Могила" and "Mohyla" returned nothing that is this text. No public-domain printing found on the reachable hosts. |
| The Trebnyk of 1646 (Church Slavonic) | The service book that fixed priestly practice, in the census text | archive.org has `3-._20240402` ("Trebnik Petra Mogily", parts 2 and 3, a Z-Library upload with Russian titles; no date, no rights statement; OCR files of about 1.6 to 1.8 MB) and `Trebnik_20221222_222250_744815`. Not opened beyond metadata: no rights statement and the uploader's source is unknown, so not vendorable. A French study, `wenger-trebnik-moghila` (A. Wenger, 1957), is a foreign post-1930 publication, in copyright. Closed as a lead; a clean scan of the 1646 print would be the thing to find. |
| Malvy and Viller, *La confession orthodoxe de Pierre Moghila* (Orientalia Christiana vol. 10, 1927) | Critical Latin and Greek edition, public domain by date | archive.org searches on "Malvy", "Viller confession orthodoxe", "Moghila confession orthodoxe", "Pierre Moghila" and "Orientalia christiana" 2026-10-23 found only the later *Orientalia Christiana Periodica* and *Analecta* series, not volume 10 of the first series. Not found on a reachable host. A 1927 imprint would be public domain by date if a copy turns up. |
| Golubev vol. 3 | The text says Mogila's educational work was left for a third volume | Not on the host (no title with "Т. 3"). Closed. |
| Mohyla Collegium statutes and records | "academy records" in the census | No edition found. Golubev's appendices print some documents (provisional rows in §1); `kma2001` ("Kyiv-Mohyla Academy in names", Khyzhniak 2001, Ukrainian) and `kyiv-mohyla-academy` (Khyzhniak 1970) are in copyright. Closed. |
| Kopystenskii's *Palinodiia* as a separate Kyiv imprint | The census-named polemic | It was not printed in the 17th century (the editors' own preface: it lay unpublished for 255 years). The 1878 Commission volume is the first and only printed text; vendored (§1). |
| Schaff, *Creeds* vol. 2, later printings (`TheCreedsOfChristendomV2`, `creedsofchristen011887mbp`, `creedsofchristen027251mbp`, `in.ernet.dli.2015.90690`) | Same text, some with cleaner OCR | These carry copyright notices of 1905 and 1919 and appendices to 1928 (Pius XI, *Mortalium animos*). The host rights fields are empty or unreliable. The 1878 NYPL printing was used instead. Closed. |
| Blaeu's Amsterdam Greek edition of the Confession (1666, `ned-kbn-all-00001622-001`) | Contemporary Greek printing | The OCR is garbled Greek at all five points, and every page carries a ProQuest "Early European Books" copyright notice on the images. Not vendored. |
| *Liber Symbolicus Russorum* (German, 1727, `10627448bsb`) | A German version of the "Greater Catechism of the Russians" (the Confession) | Bavarian State Library item with no rights statement in the record; German Fraktur OCR; the Confession is already in hand three ways. Closed. |
| Halyatovsky (`halyatovsky1`, `halyatovsky2`), Radivilovsky (`sucho-id-20220324_20220324_2104`), Baranovych (`sucho-id-00000265-print-hist-kyiv-pl-1666`) | Kyiv-Mohyla alumni preachers, 1660s–1690s | These are scans of the old Cyrillic prints. The OCR for `halyatovsky2` is unreadable at all five points; the others are the same kind of scan (not sampled). Closed for OCR quality. Sumtsov's studies (`sumtsov24`, `sumtsov26`, 1884) are scholarship about them. A clean text would be a real gain for the late 17th century, which has almost no inside voice here. |
| Kyiv Synopsis, Kyiv printings (`1680g`, `5_20211201_20211201` of 1836) | The first printings | Not fetched; the 1762 St Petersburg printing is readable and vendored. The Kyiv printings remain available on the host. |
| Golubinsky, *Istoriia russkoi tserkvi*, and Makarii's history of the Russian church | General church histories, found by searching the host for them | Scholarship, not the world's voice. Golubinsky's volumes are on the host (for example `istorijarusskojtserkvit2periodvtoroj62`, 1900) and belong to the Russian Church thread. No Makarii volume for the window turned up. Closed here. |
| Arkhiv Iugo-Zapadnoi Rossii part 1 | The Commission's series for church and brotherhood documents | Item IDs of the form `arhivjugozapadnojrossiiizdavaemyjvreme*` were listed by the host search but their contents were not opened. `aruzr-1-2` is 18th-century (Znachko-Yavorsky, 1759–1771), out of window. Left open for a later pass. |
| Sevcenko, essay on the Kyiv revival | Named in the brief | In copyright (modern scholarship, per the brief). Not searched on the host. Closed as a lead only. |

## 5. Open cross-world questions

- **The Confession is shared with VI.17 (Orthodoxy under the Ottomans, 1453–1650) and VI.18.** It is the Ottoman world's charter against Lucaris and the Kyiv world's charter as its own metropolitan's book. All the Confession files already carry rows for both. Which world holds the "native" claim, and which holds the corroborating claim, is the two builds' call. This dossier does not decide it.
- **The Union of Brest (VI.20) owns the other side of the argument.** Krevza's *Oborona uni* and the Filippovich diary are in this world's file but are Brest rows too (§1). Potii, Smotrycki and the Lviv brotherhood stay with the Brest pass. Whether this world uses Krevza as an outside witness or leaves him to Brest is for Doc_02.
- **The Russian Church (VI.23, then Nikon to Holy Synod).** Two items reach Moscow. The epistles ascribed to Artemii are placed provisionally at VI.23 (the elder tried at the Stoglav council of 1551; the epistles were written in Lithuania). The Synopsis is placed provisionally at the Nikon-to-Synod entry because Russia reprinted it. Philaret's catechism (Schaff) is placed at the Synodal Century. Whether any of these should be context or not placed at all is for the Russian Church thread.
- **The Kyiv council of 1640 is only a hostile report.** The corpus has the council as Sakovych told it. The council's own acts, if they exist in print, were not found.
- **Authors.** `kopystenskij`, `krevza`, `filippovich-afanasii`, `artemii-starets`, `philaret` and the two body slugs `kyiv-council-1640-sakovych-account` and `kyiv-synopsis` are new. The first five and the Kyiv council slug carry `authors_ruled` blocks in the staging files (`metadata-omission`, `pseudonymous` or `anonymous`); `kyiv-synopsis` is the file-name prefix. `AUTHORS.md` entries, and agreeing the spelling of `krevza` and `filippovich-afanasii` with the Union of Brest pass (which used `filippovich`), are for the lead.
- **The earlier committed version of the Commission volume's staging file** had the Brest pass's `crosslink_fragment` text appended as a malformed list item. This agent regenerated the file without it; its Brest rows are the ones that matter.
- **Dates.** The Era VII brief gave 2026-10-16 for fetch dates. The files were fetched 2026-10-23 after the usage limit; headers say 2026-10-23.

## 6. Step 0 scope notes and recommendation

**Floor question (A1).** The census says "No question". Nothing read here contradicts that. The Confession is a Nicene, Chalcedonian Orthodox statement, approved by the Synod of Iasi and by the Eastern patriarchs. One thing is for Doc_02 to read, not for this dossier to claim: whether the Greek and Latin of the Confession in Kimmel and Schaff differ in places from the 1762 and 1898 English and from the later Jerusalem text. The three witnesses are all in hand, so the check can be done.

**Uniqueness and overlap with siblings (B3).** The overlap with VI.17 and VI.20 is in the sources (the Confession, the Union polemic), not in the formation story. This world is the one where an Orthodox church answers Rome and Reformation pressure by building a school, a press and a confession. VI.17 tells the same Confession from Constantinople under the Ottomans. VI.20 tells the union from the other side. No sibling holds the Kyiv school.

**Sourcing and ecology (B1, B2).** The world's own voice in the corpus is: one confession, in three witnesses; one long Kyiv polemic of the generation before Mohyla (the *Palinodiia*, 1621–1622); the Kyiv circle's short history (the Synopsis); and about 600,000 words of Golubev with printed documents that need page-image checking. What is missing: Mohyla's own catechism of 1645, his Trebnyk of 1646, the Collegium's statutes, and any late 17th century preacher in a clean scan. Almost nothing here is in English. Everything outside the Confession is in Russian, Ruthenian, Slavonic, Polish or Latin, with OCR that is garbled in the Latin, Polish and Slavonic documents. The inside voice is real but thin and mostly pre-Mohyla, or Mohyla's own single book. The hostile voice (Sakovych, Krevza, Guépin, Pelesz) is better covered than the friendly one.

**Audiences and scale (B4, B5).** Scale is adequate by words (about 1.3 million new, plus the Confession). Audience fit is strong: a church that answers pressure with education is a story many readers can enter. Scale in the voice of the revival itself is smaller than the word count suggests.

**Recommendation, for Mark to decide, not a decision: open question.** The floor and the uniqueness are clean, and a build could start on the Confession, the *Palinodiia*, the Synopsis and Golubev's documents. But the revival's own catechism, service book and school records are not in the corpus, and the Confession is already the Ottoman world's charter. Mark should rule whether a world may stand on one shared confession, one pre-Mohyla polemic and one history, with the catechism, the Trebnyk and the Collegium statutes recorded as honest absences (§4), or whether one more acquisition pass (a clean Trebnyk scan, Mohyla's catechism, the *Lithos*, a clean Halyatovsky or Radivilovsky) should come first. If he rules for the first, the call is **build**.
