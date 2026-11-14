# R1 review, part C: Constantius of Lyon, Faustus of Riez, Gennadius of Marseilles, Ruricius of Limoges (era 3 Who batch 6)

Reviewer: independent Opus, first sight of these drafts, full effort. Profiles: `constantius-of-lyon` (recorder), `faustus-of-riez`, `gennadius-of-marseilles` (recorder) and `ruricius-of-limoges`, all non-major, at most about 325 words. For each I read the brief, card, audio script and `records.json` entry, and the batch `README.md` sentences on these ids. Files are in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch6/`. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; the era 3 Who scan entry and the Who profile entries of 2026-11-12 to 2026-11-14 in `Decision-Log.md`. Brief line numbers refer to the `.brief.txt` files, where each paragraph is one line and blank lines count (paragraphs sit on l.1, 3, 5, 7, 9). Card line numbers refer to the `.card.json` files. Other line numbers point to files under `cic/texts/`.

Method. I re-checked every quotation and close telling in the four briefs, cards and records against the vendored file and lines cited, collapsing whitespace and reading the OCR by line (Engelbrecht's CSEL 21, Levison's MGH SRM 7 extract, Richardson's and Jackson's NPNF 2.3, Barralis 1613, Peiper's Avitus, Migne's PL 42, 65, 67, 83 and 100-101, Leo and Krusch's MGH AA 4, Arndt and Krusch's MGH SRM 1, Maassen's MGH Concilia 1, Bruns's Canones II, Wasserschleben's Regino, Warfield's NPNF 1.5, Mommsen's Chronica minora 1). I read each hit in context to see who speaks: the ancient author, a document he quotes, an editor's prolegomena, a note, an apparatus, an index or a corrigenda page. I checked every factual sentence of each brief against its passage. Before accepting any absence or "only" I searched the whole Library under OCR variants with whitespace-tolerant patterns: Riochatus (`[a-z]iochat|r.ochat|riocat`), Sidonius's letters (`Sidonius\s+(domino|Constantio|Ruricio|Fausto|Patienti)`, the opening of I.1, the Patiens verses of II.10), `Ruric|Roric|Kuric|Huric`, Agde (`Agath`), Gennadius with Massil- and Scholari-, and Constantius with Germanus. That search found three held lines the drafts do not use and that change what they say: Krusch's own reversal in the addenda of MGH SRM 1 (C-B1), Leo's index naming the grandson as the later council signer (R-M5), and the acts of Agde with their own year (R-M1). Truncation of the Levison file was checked by two independent methods (below). Readability came from `engine.m1.gates.grade_text`, run from the repo root, and every suggested brief fix was applied to a scratch copy in the session scratchpad and re-scored. I did not edit any profile file, made no paid or model-API calls and used no web.

### Applies to all four

- **Audio = brief.** Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). Each opens with `[calmly]` and has one `[warmly]`, at the start of the closing paragraph. No tag appears in a brief or card. When a fix below changes a brief, the audio script follows it.
- **Readability.** All four pass now and after the fixes. Narrator sentences over 25 words are only the lead-ins to quotations and modern renderings, noted where the rendering itself runs long (C-M1).
- **Length.** The drafts run 324 to 331 words. Three are over the ~325 ceiling (Constantius 327, Faustus 331, Ruricius 328). The fixes below bring all four to 323 to 325; each re-scored figure is in the table.
- **Card order.** All four follow Mark's order; missing fields are absent; keyWorks never pass three; each `uncertain` list opens with the brief's own caveat.
- **Who test (item 14).** Constantius and Gennadius are recorders, per the README and the Palladius ruling. Faustus has his works held and a following (Ruricius, Sidonius's praise, the feast at Riez). Ruricius has two books of letters held. List lines belong to the map build and were not checked.
- **README.** Its sentences on these ids (order by best held date, Ruricius in Benjamin's place, Constantius and Gennadius as recorders at standard length, card traditions as the scan's placings) match the drafts and the supplement scan.

| Profile | Words | Est. @162 | FK | Flesch | After fixes |
|---|---|---|---|---|---|
| Constantius of Lyon | 327 | 2:01 | 8.2 | 65.4 | 323 words, 2:00, FK 8.0, Flesch 66.1 |
| Faustus of Riez | 331 | 2:03 | 8.5 | 62.4 | 324 words, 2:00, FK 8.1, Flesch 63.1 |
| Gennadius of Marseilles | 324 | 2:00 | 8.0 | 65.0 | 325 words, 2:00, FK 8.2, Flesch 64.0 |
| Ruricius of Limoges | 328 | 2:01 | 7.3 | 66.6 | 324 words, 2:00, FK 7.2, Flesch 67.3 |

---

### 1. Constantius of Lyon (recorder)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, blocking (C-B1, card); minor (C-M4, C-M5, C-M6) |
| 2 | Quotes verbatim | PASS (no verbatim quote; the close is a modern rendering, see C-M1) |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (C-M1 rendering length; C-M2 anachronism) |
| 5 | No role for a witness | PASS (Levison, Sidonius, Isidore, Krusch, Prosper named) |
| 6 | Partisan witness named and marked | PASS (none in play; Levison's judgment of the Life is his) |
| 7 | Contested both sides | FAIL, blocking (C-B1: Krusch's side is his superseded view) |
| 8 | Common names placed | PASS (Patiens of Lyon, Germanus bishop of Auxerre, Martin of Tours, Ennodius of Pavia, Adomnán of Iona) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | minor (327 words; fixed by C-M1 and C-M2) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS ("His own life is thin" opens `uncertain`) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder) |

**Quotes and close tellings** (`constantius-lyon_vita-germani_levison1920.txt` unless named)
- The verses (l.1): Levison l.371-373, "cum Patiens episcopus Lugduni ecclesiam aedificasset, versus hexametros composuit una cum carmine Secundini parietibus basilicae altari vicinis inscribendos", from Sidonius ep. II.10 (note 16, l.389). Faithful.
- Life (l.3): l.364-370, "virum Lugdunensem sive clericum sive absque ordinibus sacris vitae religiosae deditum amicum Sidonii, qui ei et singulas epistulas inscripsit et octo libros earum collectos dedicavit, quas ut ederet Constantius ei suaserat"; "c. a. 473 Arvernis in 'civica simultate' concordiae restituendae operam dedisset"; "persona aetate gravis … religione venerabilis"; l.391 "De ordinibus eius ecclesiasticis non constat". Faithful.
- The writing of the Life (l.5): letter to Patiens, l.1789-1791, "imperasti saepissime, ut vitam sancti Germani episcopi obumbratam silentio … traderem"; preface l.1965-1966, "tanta enim iam temporum fluxere curricula, ut obscurata per silentium vix colligatur agnitio"; letter to Censurius l.1880-1885, "ut pagina, quae adhuc intra secreti vicinia tenebatur, longius me auctore procederet essemque ipse reatus mei quodammodo et accusator et proditor"; Levison l.432, "Vitam c. 480. aut paulo post compositam". Faithful.
- Judgment (l.7): l.455-458 ("non tam biographi quam hagiographi munere fungens … miracula exigui momenti magnam partem operis efficiant aeque atque in Vita Martini a Sulpicio Severo composita, quam Constantio notam fuisse … demonstrant"); l.529-531 ("in tanta penuria testium minime omnino spernendum est; sed quamvis caute adhibendae sint"); l.587-589 (Bede, HE I.17-21, "magna ex parte ad verbum fere … descripsit"). Faithful.
- Close (l.9): l.4574-4579, "Ego duplicem veniam a te, lector, exposco, primum quod soloecismis et abiectione verborum aures tuas vulnero, deinde quod prolixior pagina videtur parare fastidium … Et tamen Deum testor conscium secretorum, me plura de domni mei Germani factis agnita et probata tacuisse". See C-M1.
- Card: Isidore, De vir. ill. 17, "Siquidem et Constantius episcopus Germani vitam contexuit" (`isidore-seville_…pl83…` l.121539-121540); Levison on Isidore's error and the Spanish codex (l.391-402, 583-584); Ennodius, Fortunatus, Adomnán (l.536-538, 585-587); Patiens 449 to before 494 (l.375-376, 1768-1770); Prosper and the synod (l.471-476, 505); the Alleluia victory (l.466-468); fifteen years packed (l.521). All faithful except uncertain 6 (C-B1).

**Truncation of `constantius-lyon_vita-germani_levison1920.txt`.** Confirmed by two independent methods. (1) Text end: the file's last bytes are "Et ideo in scribendo succinctum^" followed by a newline (l.4579-4580, checked with `od`); the sentence and the epilogue stop mid-clause, and p.283 carries no apparatus block, while every other page does (compare p.282, l.4513-4553). (2) Stated boundary: the header says the extract runs "through 'EXPLICIT VITA SANCTI GERMANI EPISCOPI' (p. 283)" (l.9); no such body line exists after the p.283 running head (l.4571), and the only "Explicit vita sancti Germani" in the file is a variant reading inside p.282's apparatus (l.4550). So the rest of the epilogue and its apparatus are missing. No claim leans on the missing text: the brief's close, the card and every records claim cite lines up to l.4579, and the rendered clause ("Deum testor … tacuisse") is complete in the file. The records already note the gap (`absent_details`, "The end of the Life"). See C-M7 for logging it.

**Tradition placing ("British and Welsh Christianity").** Checked, not raised as a finding. It is the supplement scan's placing (`Who_Scan_Supplement.md` l.150, "British and Welsh Christianity (Germanus's missions)") and matches Germanus of Auxerre's card (`era2/batch6/germanus-of-auxerre.card.json`). It is defensible for a recorder whose one work is the main source for the British missions and for Bede's account. A listener will see a man of Lyon placed in a British tradition; the card's `place` ("Lyon, in Gaul") and `knownFor` make the reason clear. If the coordinator wants him on the Gallic side too, Faustus's card shows the two-placing form ("Gallic Monastic-Ascetic Christianity; British and Welsh Christianity"). That is a coordinator's call, not a fault.

**Findings**

- **C-B1 BLOCKING (card `uncertain` 6, l.31; records `contested_claims` 1; items 1, 5, 7; a witness's superseded view told as his view).** The card says: "Bruno Krusch says Gregory copied a whole chapter of his Miracles of Julian word for word from it without naming it. Levison holds that Gregory did not know it." Krusch said that in his introduction (`gregory-tours_opera-mgh-srm-1-lat_arndt-krusch1885.txt` l.35826-35829), but in the Addenda et emendanda of the same volume, p.883, he reverses it: "De Vita S. Germani Autisiodorensis, quae Constantio vulgo attribuitur, vide quae p. 772 n. 6 scripsi. Iam nullus dubito, quin Vitae scriptor e Gregorio ipso hauserit" (l.66231, 66256-66257): I now have no doubt that the Life's writer drew on Gregory himself. The text Krusch compared was Duru's edition (his notes cite it by book, "lib. I, c. 7, Duru", l.44305-44306), which he calls "Pseudo-Constantius" (l.60038) and the Life "quae Constantio tribuitur" (l.58580-58581); Levison says the genuine text had been printed only by Mombritius, that the vulgate is a much-interpolated second Life, and that Krusch himself said so at that same p.883 ("Textum vulgatum interpolationibus refertum esse, monuerunt etiam B. Krusch, SS. R. Merov. I, 883", Levison l.659-660, 703-704). So the card sets up a dispute between Krusch and Levison that Krusch's own final word, in a held volume, does not support.
  Fix, card `uncertain` 6: "Whether Gregory of Tours knew the Life. In his introduction to Gregory's Miracles, Bruno Krusch says Gregory copied a whole chapter of his Miracles of Julian almost word for word from a Life of Germanus, which he cites in Duru's edition. In the additions at the end of the same volume he holds the reverse: the writer of that Life, which he calls the Life commonly given to Constantius, drew on Gregory. Wilhelm Levison holds that Gregory did not know Constantius's Life, since Gregory has Germanus die at Rome, where the Life has Ravenna, and he says the text then in print was a much-interpolated second Life." Records: side 1 of "Whether Gregory of Tours knew the Life of Germanus" becomes "Bruno Krusch, first: Gregory copied Virt. Iul. 29 almost word for word from the Life (gregory-tours arndt-krusch1885 l.35826-35829; note l.44305-44306, citing Duru's text); Krusch, later in the same volume: 'Iam nullus dubito, quin Vitae scriptor e Gregorio ipso hauserit', of the Life 'quae Constantio vulgo attribuitur' (l.66256-66257, p.883)"; and add to side 2 Levison l.659-660 and 703-704 on the interpolated vulgate text and Krusch's note at p.883.

- **C-M1 MINOR (brief l.9; items 2, 4; the rendering bar in `CLAUDE.md`).** "I call God, who knows all secrets, to witness that I have kept silent about many deeds of my lord Germanus that I knew and had proved." Three points. "All" is added: the Latin is "conscium secretorum", who knows secrets. "That I knew and had proved" makes Constantius the knower and prover, where "agnita et probata" is passive, deeds known and proved. And the rendering runs 27 words, past the ~25-word bar for a modern rendering. Fix: "Then he writes, in modern words, "I call God, who knows what is hidden, to witness that I have left out many deeds of my lord Germanus that were known and proved."" (rendering 25 words; Opus-authored per `CLAUDE.md`). Records: the epilogue claim notes the new rendering.

- **C-M2 MINOR (brief l.7; item 4, Style Guide 1.7 anachronism).** "Bede, in England, copied large parts of it". There was no England in Bede's day; his title names a people, the English. Fix: "Bede copied large parts of it almost word for word into his History of the English." (also holds the length).

- **C-M3 MINOR (item 10; length).** 327 words, over the ~325 ceiling. C-M1 and C-M2 bring it to 323. No other cut needed.

- **C-M4 MINOR (brief l.1; item 1).** "Sidonius Apollinaris, later bishop of Clermont." "Later" asserts that he became bishop after the church and verses, which no held line dates (Levison gives the letters "paulo post a. 470", l.1768-1769, about when Sidonius became bishop). Fix: "Sidonius Apollinaris, bishop of Clermont." Witness for the see: Gregory of Tours, HF II.23, tr. Dalton (`gregory-tours_history-of-the-franks-v2_dalton1927.txt` l.2963-2967), already in the records.

- **C-M5 MINOR (card `uncertain` 1, l.26, and 2, l.27; item 1).** Item 1 says "No source used here gives his family, his birth, his death or his orders", but item 2 then gives sources that do name his orders (manuscript headings, priest; Isidore, bishop), and the records' own search found two more that call him a priest: Rees, "Constantius, a priest of Lyons" (`rees_lives-of-the-cambro-british-saints-lat-eng_1853.txt` l.17717-17718), and an unsigned note in Migne's Marius Mercator, "Constantius presbyter" (`marius-mercator_opera-omnia-lat_migne-pl48.txt` l.20173). Fix, item 1: "No source used here gives his family, his birth or his death, and the sources disagree on his orders." Item 2, add after the manuscript headings: "W. J. Rees and an unsigned note in Migne's Marius Mercator also call him a priest."

- **C-M6 MINOR (card `knownFor`, l.3; item 1).** "the account of Germanus's life and journeys to Britain that Bede later copied". Bede copied chapters 12-16 and 25-27 (Levison l.587-589), not the account. Fix: "…the account of Germanus's life and journeys to Britain, parts of which Bede later copied."

- **C-M7 MINOR (records and tracking; `CLAUDE.md`, "Track gaps").** The truncation of the Levison file is recorded only in this profile's `absent_details` ("For the lead"). It is a Library defect that every future user of the file inherits. Fix: log it in Open-Gaps under this batch's entry ("Era 3 Who batch 6"), naming the file, the two checks above, the missing end of the epilogue and its apparatus on p.283, and the lead to re-extract p.283 from archive.org item `passionesvitaequesanctorum5`.

After the fixes: 323 words, 2:00, FK 8.0, Flesch 66.1.

---

### 2. Faustus of Riez

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, blocking (F-B1); minor (F-M4) |
| 2 | Quotes verbatim | PASS (Gennadius's English exact; Latin renderings marked "in modern words") |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (F-M2, F-M3, F-M6) |
| 5 | No role for a witness | PASS (Engelbrecht, Avitus, Gennadius, Warfield, Sidonius named) |
| 6 | Partisan witness named and marked | PASS ("A Life of Fulgentius of Ruspe, hostile to Faustus") |
| 7 | Contested both sides | PASS (see below) |
| 8 | Common names placed | PASS (Faustus of Riez, Avitus of Vienne, Gennadius of Marseilles, Fulgentius of Ruspe, Caesarius of Arles, Ruricius of Limoges) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | FAIL, minor (331 words; F-M1) |
| 11 | grade_text | PASS (Flesch 62.4, close to the floor; 63.1 after fixes) |
| 12 | Card order, caveat repeated | PASS ("The judgment on his teaching" opens `uncertain`) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**The grace dispute.** Told in place with both sides named, and no label told as settled. The brief gives the hostile Life of Fulgentius (marked hostile; `fulgentius-ruspe_opera-contra-arianos-pl65-lat_migne1847.txt` l.9687-9693, "favens occulte Pelagianis, sed catholicus tamen volens videri"); Warfield's "chief champion" with the label as his ("what he names semi-Pelagianism"; `npnf105_augustine-anti-pelagian-writings.xml` l.954-956) and Orange 529 as his ("he says"; l.956-957, "so far as a formal condemnation could reach, semi-Pelagianism was suppressed"); Engelbrecht's denial (`faustus-riez_de-gratia-and-collected-works_engelbrecht1891.txt` l.652-667, "Faustum neque Semipelagianum fuisse neque a Caesario … habitum esse … hominis bona fide errantis verba"); the 534 treatise with its attribution to Caesarius as Engelbrecht's (l.659-662; fragment l.13805-13821); and Gennadius's praise. The card adds Isidore (`isidore-seville_…pl83…` l.122089-122092, "Pelagianae pravitati consentienti"), the Scythian monks and Hormisdas (l.590-606), Fulgentius's lost seven books (l.622-628), Ado on Avitus and Engelbrecht's answer (l.630-647). Orange 529 is not named in the brief as Caesarius's condemnation of Faustus, which the canons do not do (records `absent_details`, checked). Engelbrecht also reports Krusch's argument that Caesarius wrote nothing against Faustus (l.648-652); the brief does not need it.

**The Riochatus opening and Barralis.** The letter is Sidonius IX.9, held only in Barralis's 1613 print, but held twice there: once whole (`barralis_chronologia-sanctorum-insulae-lerinensis-lat_1613.txt` l.4712-4800) and once again with Barralis's hostile gloss (l.5510-5545). The two OCR passes of the same pages agree on every word the brief uses, and Engelbrecht's summary (l.566-572) and Hugh Williams's note in the Gildas volume ("Faustus sent two of his writings to Britain by the hands of a fellow-countryman, Riocatus … antistes ac monachus (Mon. Hist. Germ., viii, 157)", `gildas_de-excidio-britanniae-lorica-penitential-lat-eng_williams1899.txt` l.9659-9663) are two further witnesses. The opening can rest on it, told in modern words as the drafter does, once F-B1 is fixed. Barralis's gloss (Faustus hid the books from a bad conscience) is his, and is rightly not used.

**Is any Sidonius text truly not held?** No Sidonius edition is held, and no letter to Faustus other than IX.9 (Barralis). Some Sidonius letters are held in other books, none touching these four people: to Domnulus, Agroecius, Perpetuus and Euphronius in Mansi 7 (`mansi_sacrorum-conciliorum-collectio-tomus-7-451-492-lat_welter-facsimile1901.txt` l.99896-100197) and to Euphronius in the Acta Sanctorum (`acta-sanctorum_augusti-tomus-1-lat_1750.txt` l.40220). The records' "No Sidonius edition is held" stands. The card and records never claim more.

**Quotes and close tellings** (Engelbrecht unless named)
- Birth (l.3): Avitus, "ortu Britannum habitaculo Regiensem" (`avitus-vienne_opera-mgh-aa-6-2-lat_peiper1883.txt` l.7378-7379, OCR "Britauuum"). Lérins and 433: l.159, 229-240 ("itaque a. 433 Faustum abbatem Lerinensem factum esse constat"). Riez: Gennadius ch. LXXXVI (`npnf203…` l.43684-43686).
- Lucidus (l.5): retraction l.11205-11206, "qui dicit alios deputatos ad mortem, alios ad vitam praedestinatos"; Faustus l.11046-11048, "nos ergo per medium Christo duce gradientes post gratiam, sine qua nihil sumus, laborem officiosae servitutis adserimus" (rendered faithfully, marked "in modern words"); prologue l.3550-3567 (Leontius's council and mandate); l.3602-3604, "humanam … infirmitatem sine gratia sibi posse sufficere stulte credidit"; 474, l.555-562; Gennadius l.43693-43697, "that the grace of God always invites, precedes and helps our will" (exact).
- Close (l.9): exile l.322-350 ("neque improbabilis est coniectura virorum doctorum ab Eurico"); ep. 9 l.13401-13404, "sine sede propria possessores, sine possessione divites sumus" (faithful).
- Card: Regino/Gelasian list l.29717-29718 and Wasserschleben's note l.29638-29639 (exact); Engelbrecht on the interpolation l.582-589; De spiritu sancto l.427-434; Barralis's feast l.4535-4536; Maassen's Faustus of 549 (records). All faithful except `place` (F-M4).

**Findings**

- **F-B1 BLOCKING (brief l.1; records claim 1; item 1; the scene misreported).** "Unrest among the peoples kept him at Clermont, and there its bishop, Sidonius Apollinaris, read the books." The letter says the reverse of "there". While Riochatus stayed in the town he showed Sidonius Faustus's other gifts but hid the books: "sic reliqua dona vestra detexit, ut perurbane quae praestantiora portabat operuerit" (Barralis l.5539-5540, second print; first print l.4759-4760). Only after two months or more, when he had left, did Sidonius ride after him, catch him and read them: "post duos aut his amplius menses … pernicibus equis insecutus abeuntem … sarcinas solvo, quaesitum volumen invenio, produco, lectito, excerpo" (l.5540-5548; l.4762-4772). That pursuit is the scene of the letter, and the complaint that the books "brushed past his walls without a greeting" (l.4731-4732) is about the books being kept from him.
  Fix, brief l.1 (scored with F-M1 to F-M3 and F-M6): "Riochatus, a bishop and monk, was carrying books by Faustus of Riez to the Britons. Unrest among the peoples held him at Clermont, where he kept the books hidden. When he left, the bishop there, Sidonius Apollinaris, rode after him and read them. August Engelbrecht, who edited Faustus, takes them to be his work On Grace." Records claim 1: add "he hid the books during his stay ('quae praestantiora portabat operuerit'); after 'duos aut his amplius menses' Sidonius rode after him 'pernicibus equis', found the book and read it ('quaesitum volumen invenio, produco, lectito, excerpo')", with witness Barralis l.4759-4772 and l.5539-5548, and add Williams, Gildas volume, l.9659-9663, as a further witness to Riochatus and the books.

- **F-M1 MINOR (item 10; length).** 331 words, over the ~325 ceiling, and F-B1 adds words. Cuts, all scored: drop the "brushed past his walls" sentence (the pursuit carries the scene); l.3 "and then its abbot, from 433 by Engelbrecht's reckoning" becomes "and its abbot from 433, by Engelbrecht's reckoning", and "At last he became bishop of Riez in Gaul" becomes "Then he became bishop of Riez" (the card keeps "in Gaul"); l.5 "Lucidus's later retraction condemns the view" becomes "Lucidus later retracted the view"; "praised the books for teaching" becomes "praised them for teaching"; l.9 "he wrote to his friend Ruricius" becomes "he wrote to Ruricius".

- **F-M2 MINOR (brief l.7; items 4, 8; context).** "Benjamin Warfield calls Faustus…". Engelbrecht is introduced and Warfield is not, so a listener does not know who he is (Mark: "no statements that have no context"; the batch 5 C-M2 ruling on Dalton). The sentence also runs 23 words with a nested "which, he says". Fix: "The Princeton scholar Benjamin Warfield calls Faustus the chief champion of what he names semi-Pelagianism. He says the Council of Orange put it down in 529." Witness for Princeton: `npnf105…` l.516-519, "BENJAMIN B. WARFIELD, D.D., PROFESSOR IN THE THEOLOGICAL SEMINARY AT PRINCETON, N.J."

- **F-M3 MINOR (brief l.3; item 4, unearned word).** "At last he became bishop of Riez" carries a sense of long waiting that no source gives. Fixed in F-M1 ("Then").

- **F-M4 MINOR (card `place`, l.9; items 1, 7).** "Britain, where Avitus of Vienne says he was born" settles a point the card itself lists as uncertain (item 4) and the records as contested: Avitus says "a Briton by birth"; that this means the island is Engelbrecht's reading ("pro certo habemus", l.152-154), against others who place him in Brittany (l.146-150). Fix: "Britain, by August Engelbrecht's reading of Avitus of Vienne, who calls him a Briton by birth; the island monastery of Lérins; Riez, in Gaul, as its bishop".

- **F-M5 MINOR (records).** Claim 1 cites only Barralis's first print and Engelbrecht. Add the second print (l.5528-5548) and Williams (l.9659-9663), as in F-B1; this matters because the Barralis header asks for a second check before quoting.

- **F-M6 MINOR (brief l.9; item 4, doubled hedge).** "probably by the Gothic king Euric, Engelbrecht thinks". Fix: "by the Gothic king Euric, Engelbrecht thinks." Engelbrecht calls the guess "neque improbabilis" (l.324-325), and "thinks" carries that.

After the fixes: 324 words, 2:00, FK 8.1, Flesch 63.1.

---

### 3. Gennadius of Marseilles (recorder)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS; card minor (G-M3) |
| 2 | Quotes verbatim | PASS (all Richardson's English, exact) |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (G-M1, G-M2) |
| 5 | No role for a witness | PASS (Richardson, Jackson, Mommsen, Walafrid, Alcuin named) |
| 6 | Partisan witness named and marked | PASS (the Louvain theologians are given as an unsigned note's report, placing him in a party) |
| 7 | Contested both sides | PASS (the Augustine line, the "I Gennadius" notice, the Book of Church Dogmas, priest or bishop) |
| 8 | Common names placed | PASS (Proterius as bishop of Alexandria, Timothy Aelurus, Prosper of Aquitaine, John Cassian, Augustine of Hippo, Macarius the Egyptian, Gelasius bishop of Rome, Faustus of Riez) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (324 words) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS ("His own life is thin" opens `uncertain`) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder) |

**Quotes and close tellings** (`npnf203_theodoret-jerome-gennadius-rufinus.xml`)
- Timothy (l.1): ch. LXXIII, l.43441-43458, "when Proterius had been put to death by the Alexandrians, in response to popular clamour, willingly or unwillingly allowed himself to be made bishop by a single bishop … wrote a very persuasive book to the Emperor Leo … that Leo of Rome, pontiff of the city, and the synod of Chalcedon, and all the Western bishops were fundamentally Nestorians … This book of his for learning’s sake, I translated by request of the brethren into Latin and prefixed a caveat." Both quoted phrases exact. Richardson's apparatus (l.43458-43459) says Migne and Herding omit the sentence; the manuscripts he collated carry it, so telling it as Gennadius's is sound, and the card notes the omission.
- Life and dating (l.3): Richardson's introduction l.38471-38487 ("The bulk of the work at least was composed about 480"); the title page l.688 (Richardson translated Jerome and Gennadius); Evagrius ch. XI l.42324-42343 ("the intimate disciple of the above mentioned Macarius … This work I have, under instructions, translated into Latin"). Faithful.
- Semi-Pelagian view (l.5): l.38488-38491, "glimpses of his own—the semi-Pelagian—point of view"; Prosper ch. LXXXV l.43661-43669 (exact); the Augustine line and Richardson's note l.42851-42865, "This expression in the editions has been the ground of much comment on Gennadius’ Semi-pelagian bias, but it almost certainly does not represent the original form of the text" (faithful).
- The notice and 496 (l.7): ch. XCIX l.43968-43975 (exact; Richardson's endnote "Died 496."); Richardson's rejection of the notice "as by a later hand" l.38477-38479; Jackson's prolegomena l.3611-3612, "Gennadius, presbyter of Marseilles, who died in 496". Neither gives a reason for 496 in the held lines, and Gelasius's own note reads "Bishop 492, died 496" (l.43862); the brief and card rightly give the year as theirs and draw no inference from it.
- Close (l.9): ch. LXXXVI l.43711-43712 (exact).
- Card: PL 42 admonition l.97003-97058 (Walafrid, Ratramnus, the Padolirone codex, Platina, the Louvain censure); Alcuin l.5646-5650; Mommsen l.42784-42785; the Acta Sanctorum l.180635-180636. The Book of Church Dogmas is under "Their own words" as "ascribed to Gennadius", with the attribution dispute in keyWorks and `uncertain` 6; that labels it honestly.

**Findings**

- **G-M1 MINOR (brief l.5; item 4, clarity).** "Gennadius credits Prosper of Aquitaine with an unsigned book against works of John Cassian, "which the church of God finds salutary, but which he brands as injurious"." Heard aloud, "he" can be taken for Gennadius, and what "which" refers to is unclear, so the point (Gennadius sides with Cassian's works against Prosper) is lost. Fix, same word count, verbatim fragments: "Gennadius thinks Prosper of Aquitaine wrote an unsigned book against works of John Cassian. He says Prosper "brands as injurious" works "which the church of God finds salutary"." ("I regard as his also", l.43666, is "thinks … wrote".)

- **G-M2 MINOR (brief l.7; item 4, context).** "He and Blomfield Jackson, in the same volume, give 496 for his death." Jackson is not introduced, and "in the same volume" means nothing to a listener. Fix: "He and Blomfield Jackson, Theodoret's translator in the same volume, give 496 for his death." Witness: title page l.682-684. To hold length, l.5's last two sentences merge: "The line drew much comment on his bias, Richardson says, though it almost certainly does not go back to Gennadius."; and l.3 "Little more is known of his own life" becomes "Little more is known of his life".

- **G-M3 MINOR (card `uncertain` 2, l.35; item 1, witness form).** "The year 496 for his death is given in notes by Richardson and by Blomfield Jackson". Richardson's is an endnote; Jackson's is a sentence of his prolegomena to Theodoret (l.3611-3612), not a note. Fix: "The year 496 for his death is given in a note by Richardson and in Blomfield Jackson's prolegomena to Theodoret, in the same English volume, with no reason given in the lines used here."

- **G-M4 MINOR (card `sources`; item 12).** `uncertain` 2 cites the Acta Sanctorum, but no Acta Sanctorum entry is in `sources.about`. Add: `{"title": "Acta Sanctorum, March, volume 3", "author": "Bollandists", "date": "1865", "language": "Latin", "file": "cic/texts/acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt"}`.

- **G-M5 MINOR (records).** Card `uncertain` 8 names "the much later Gennadios Scholarios", but the records' namesake claim covers only the patriarch of ch. XC. Scholarios is held: add a namesake claim citing `gennadius-scholarius_opera-omnia-pg160-grc-lat_migne1866.txt` (its header and title), Documented.

After the fixes: 325 words, 2:00, FK 8.2, Flesch 64.0.

---

### 4. Ruricius of Limoges

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, blocking (R-B1); minor (R-M1, R-M6) |
| 2 | Quotes verbatim | PASS (all modern renderings, marked "in modern words", faithful) |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (R-M3, R-M4) |
| 5 | No role for a witness | PASS (Engelbrecht, Caesarius, Fortunatus, Sidonius, Faustus named) |
| 6 | Partisan witness named and marked | PASS (none in play) |
| 7 | Contested both sides | minor (R-M2, one side of Caesarius's letter) |
| 8 | Common names placed | PASS (Caesarius of Arles, Verus bishop of Tours, Faustus of Riez, Venantius Fortunatus, Sidonius Apollinaris) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | minor (328 words; R-M4) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS ("His life comes almost wholly from his letters" opens `uncertain`) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes and close tellings** (Engelbrecht unless named)
- Agde (l.1): Caesarius to Ruricius l.24680-24694, "Dum nimium tribularetur animus meus, quare ad synodum vestram praesentiam non meruimus obtinere, sanctus et domnus meus Verus episcopus mihi dignatus est dicere, quod per suum diaconum mihi Agate vestras litteras destinasset, quas ego nescio quo casu aut qua neglegentia me non retineo suscepisse … dignissimum fuerat, ut personam dirigeretis, quae ad vicem vestram subscriberet"; Verus of Tours, l.2959-2960. Ruricius, ep. II.33, l.23184-23188, "fecit hoc infirmitas, non voluntas. ipsi etenim recolere potestis, quam fessum me Burdigala videritis et hoc hieme, quando esse soleo fortior solito". Faithful. A second witness ties II.33 to Agde: the Maurist prolegomenon in PL 67 (`facundus-ferrandus-caesarius-dionysius-pl67-lat_migne1865.txt` l.96512-96546).
- 485, the epitaph, the wedding (l.3): l.2901-2903 and 953-958; Fortunatus carm. IV.5 (`venantius-fortunatus_opera-mgh-aa-4-lat_leo-krusch1881.txt` l.8290-8311, "Ruricii gemini flores, quibus Aniciorum iuncta parentali culmine Roma fuit … hinc avus, inde nepos"); l.2850-2851, "Ruricio et Iberiae epithalamium confecit Sidonius". Faithful, but see R-M6.
- Faustus (l.5): l.2890-2893, "Fausto imprimis auctore"; ep. I.1 l.20027-20044, "Olim te … fama celeberrima praedicante cognovi … adhaesit, doctor eximie, anima mea post te" (Ps. 62:9, l.20046); l.20070-20074 (see R-B1); Faustus ep. 9 l.13409-13412, "hanc primam munificentiam domino largiente percepi, quod piissimus meus Ruricius post vitae huius iactationes ad portum religionis proram salutis … convertit". Faithful.
- Death and churches (l.7): l.2926-2974 ("non multo post eum diem supremum obiisse veri simile esse cum Kruschio statuimus"); Fortunatus l.8302-8303, "tempore quisque suo fundans pia templa patroni iste Augustini, condidit ille Petri". Faithful.
- Close (l.9): ep. II.33 l.23197-23200, "si aliis nomen urbium praestat auctoritas, nobis auctoritatem demere non debet urbis humilitas, siquidem multo melius multoque eminentius est civitatem de sacerdote, quam sacerdotem de civitate notescere"; Engelbrecht l.2904-2906, "civitas … exigua atque infirma". Faithful.
- The councils of 535 and 541: Maassen l.6019, 6050, 8139 ("Ruricius Deo propitio Lemouice civitatis episcopus"), 9442 (549, through the archdeacon Bantardus). See R-M5.

**Findings**

- **R-B1 BLOCKING (brief l.5; item 1; a metaphor told as fact).** "He asks Faustus to send him harsher food, fit for his sickness, in place of the sweet dishes sent so far." In the letter the food is Faustus's words. Ruricius asks that whenever Faustus waters "the dryness of my earth with the rain of your eloquence", he send "non … delicatos et dulces cibos, sed austeriores et aegritudini meae congruos" (l.20070-20074); the sickness is the wounds of his sins, which he wants cut, not soothed: "ne vulneribus meis gratior sit foventis dextera quam secantis" (l.20078-20079), with "peccatorum meorum vincula" and "spinas criminum" just before (l.20034, 20043). As drafted, a listener hears that a sick man asked for real food. Fix: "He asks that Faustus's letters be harsher food, fit for a sinner's sickness, in place of the sweet dishes sent so far." Records claim on ep. I.1: add "quoties dignati fueritis ariditatem terrae meae eloquentiae vestrae imbre perfundere" and "ne vulneribus meis gratior sit foventis dextera quam secantis" (l.20070-20072, 20078-20079).

- **R-M1 MINOR (brief l.1; card `uncertain` 2, l.31; records claim 3; items 1, 5; a documented date told as an editor's).** "in 506 by August Engelbrecht's date" and "the year 506 is Engelbrecht's". The year is in the council's own acts, which are held: Bruns gives the heading "habitum era 644 … Anno vicesimo secundo Alarici regis sub die tertio Idus Septembris", with "Messala v. c. consule" in other codices (`bruns_canones-apostolorum-et-conciliorum-pars-altera-lat_1839.txt` l.10481-10501), and Engelbrecht cites the same dating (l.2933-2934). Fix, brief: "Bishops of Gaul met at Agde under Caesarius of Arles, in 506, and Ruricius of Limoges did not come." (Engelbrecht's first name moves to l.3: "August Engelbrecht, who edited his letters…".) Card `uncertain` 2: "The council he missed. Caesarius's letter names Agde, whose acts date it to 506. August Engelbrecht and an unsigned prolegomenon in Migne's Caesarius tie Ruricius's answer, that infirmity kept him away, to that council; Jacques Basnage, as that prolegomenon reports, held that he stayed away on purpose, which it calls invented. Ruricius also missed the council of Toulouse planned for the next year, as Sedatus of Nîmes's letter shows." (PL 67 l.96546-96553, "Hinc commentita sunt, quae de causa huius absentiae scripsit Iacobus Basnage … ac si venire noluisset Ruricius, quia primatum … usurpabat Caesarius".) Records: retag the 506 claim Documented, with Bruns as witness; add the PL 67 claim and the Basnage side as a contested claim.

- **R-M2 MINOR (brief l.1; item 7; one side of a letter).** The brief tells Caesarius's reproach and not his pardon, so Ruricius's answer reads as a defence against blame Caesarius in fact withdrew: "Sed quia novi, quam sancto et frequenti ac pio desiderio interesse volueritis, omnibus fratribus vestris votum vestrum et sanctam voluntatem exposui, pro qua re nihil pietati vestrae vel potuimus vel debuimus inputare" (l.24713-24716). The PL 67 prolegomenon reads the letter the same way: "partim obiurgat, partim excusat Ruricium" (l.96517-96518). Fix: after "Ruricius should, he wrote, have sent someone to sign in his place." add "Yet he held nothing against him." and start a new paragraph at "Ruricius answered" (which also brings l.1 back to one idea per paragraph).

- **R-M3 MINOR (brief l.7; items 4, 5).** "Engelbrecht, with Bruno Krusch, thinks he died…". Krusch is not introduced anywhere in the brief. The judgment is stated by Engelbrecht ("cum Kruschio statuimus"), and the card keeps Krusch. Fix: "Engelbrecht thinks he died not long after 507, when he was too frail to reach a council at Toulouse."

- **R-M4 MINOR (brief l.1 and l.7; items 4, 10).** Length 328, over the ~325 ceiling; and l.1 ends on a choppy pair, "Ruricius reminded Caesarius that he had seen him worn out at Bordeaux. That was in winter, when Ruricius was usually stronger." Fixes: "Caesarius himself, he wrote, had seen him worn out at Bordeaux, and in winter, when he was usually stronger." ("ipsi etenim recolere potestis", l.23186-23187); l.7 "Fortunatus says each of the two Ruricii founded" becomes "Fortunatus says each Ruricius founded". With R-B1, R-M1, R-M2 and R-M3 the brief is 324 words.

- **R-M5 MINOR (card `uncertain` 5, l.34; records `absent_details` 1; a held identification missed).** "A Ruricius signs at councils of 535 and 541 in Friedrich Maassen's edition; he cannot be this man if Engelbrecht's reckoning of his death is right." This leaves an open puzzle that a held line settles: Leo's index to Fortunatus names the signer as the grandson, "alter nepos illius interfuit concilio Arverno I. a. 535, Aurelianensi IV. a. 541, V. a. 549 per Bantaredum archidiaconum subscripsit" (`venantius-fortunatus_opera-mgh-aa-4-lat_leo-krusch1881.txt` l.53125-53130, "alter nepos" at l.53128), and gives the elder's death as "c. a. 507" (l.53126, OCR "51)7"). The records' search for "Huric-" missed this index line. Fix: "Which Ruricius. His grandson, also named Ruricius, was later bishop of Limoges too, by Venantius Fortunatus's epitaph. The index to Fortunatus's works in the Monumenta edition names the grandson as the Ruricius who signs at the councils of Clermont in 535 and Orléans in 541, and through his archdeacon at Orléans in 549, which Friedrich Maassen's edition prints." Records: add the claim with witness Leo l.53125-53130 and Maassen l.6019, 8139, 9442, and correct `absent_details` 1.

- **R-M6 MINOR (card `dates`, l.8, and `uncertain` 1, l.30; item 1).** The 485 rests on more than "a letter Faustus wrote soon after returning from exile". That letter shows only that Ruricius was newly bishop when Faustus had newly come home (l.957-959). The year is Engelbrecht's year for Faustus's return, which is itself conditional: "Quodsi Euricus in causa fuit, ut Faustus a. 477 in exsilium pelleretur, illo demum mortuo i. e. anno 485 in patriam hunc rediisse veri simile est" (l.348-350). Fix, `uncertain` 1: "…The year 485 for his election rests on Engelbrecht's reading of a letter Faustus wrote soon after returning from exile, to Ruricius newly made bishop, and on his guess that Faustus came home in 485, when King Euric died, if Euric had exiled him." The brief's "dates his election to 485 from one of Faustus's letters" may stand, since it gives the year as Engelbrecht's.

- **R-M7 MINOR (card `otherNames`, l.5; Naming rule).** "Ruricius the elder" is not a form any vendored source spells; the sources say "avus" (Fortunatus), "Ruricius noster" against "Ruricio iuniori" (Engelbrecht l.2975) and "alterum" (Leo). Fix: drop it, or replace it with a spelled form, "Ruricius Lemovicensis episcopus" being already covered by the first entry.

After the fixes: 324 words, 2:00, FK 7.2, Flesch 67.3.

---

### Verdicts

- Constantius of Lyon: NOT CLEAR (1 blocking, 7 minor).
- Faustus of Riez: NOT CLEAR (1 blocking, 6 minor).
- Gennadius of Marseilles: CLEAR on blocking points, with 5 minor findings to apply (NOT CLEAR until they are applied and rechecked).
- Ruricius of Limoges: NOT CLEAR (1 blocking, 7 minor).
