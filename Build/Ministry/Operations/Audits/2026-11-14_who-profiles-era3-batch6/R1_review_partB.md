# R1 review, part B: John Moschus, Babai the Great, Severinus of Noricum (era 3 batch 6)

Reviewer: independent Opus, first sight of these drafts. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to (Style Guide 1.1 to 1.12); `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; the Who profile rulings in `Decision-Log.md`, 2026-11-12 to 2026-11-14. Babai the Great is major (cap 2:30, about 405 words, a cap and not a target). John Moschus is a recorder at standard length, and Severinus is standard: both 1 to 2 minutes, at most about 325 words at 162 wpm. Severinus's card tradition, "Early Benedictine / Italian Monasticism", is the coordinator's call (2026-11-14) and was checked only for being stated as the README says. I edited no profile file, made no paid or model-API calls and used no web.

Profiles: `john-moschus`, `babai-the-great`, `severinus-of-noricum`, with their cards, audio scripts and `records.json` entries, and the batch `README.md` sentences on them. Files are in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch6/`. Brief line numbers refer to the `.brief.txt` files, where each paragraph is one line and blank lines count (paragraphs sit on l.1, 3, 5, 7, 9, 11, 13). Card fields are named by key and list position. Other line numbers point to files under `cic/texts/`. An extra section checks the batch 5 `henana-of-adiabene` records correction made on this branch.

Method. I opened every quoted passage at its cited line in the vendored file. For each one I read the context to see who is speaking: the ancient author, a document he copies, a translator's or editor's note, or a running head. That meant the PG 87.3 Moschus volume, where Papebroch's Life of Sophronius quotes the old notice, Fabricius's notice as Harles printed it ("HAL." marks, "Hactenus Fabricius" at l.24445), and Lipomanus's letter. For Babai it meant Scher's Chronicle of Seert, Budge's Thomas of Marga, Labourt, Chabot's and Braun's Synodicon, Duval's Ishoyahb, Badger's Abdisho and Wigram. For Severinus it meant Robinson's Eugippius, Foulke's Paul the Deacon and Mansi 10. I checked each factual sentence of each brief against its passage. Before accepting any "not held", "only" or "none" claim, I searched all of `cic/texts/` with whitespace-tolerant patterns under every spelling and OCR form I could find. For Moschus: Moschus, Moschi, Moscho, Eucrat-, Evirat-, Limonar-, Leimon, "Spiritual Meadow", "Pratum spirituale", "Pré spirituel". For Babai: Babai, Babaï, Bäbai, Babhai, Bàbhay, Babaeus, Babaeo, Babaoo, "Mar iJabae". For Henana: Hnana, Henana, Hannänä, Hananus, Rannana. For Severinus: Severin- beside Noric-, Eugipp-, Favian-, Lucull- and Odoac-. That search found held files the drafts do not use. Mari's and 'Amr's histories name Babai the Great (Gismondi's Latin; the records say they do not). Oskar Braun's 1915 German gives Babai's whole Life of George, and Georg Hoffmann's 1880 German gives extracts. The anonymous Syriac chronicle Guidi edited (Chronica minora) has a notice of Babai and his quarrel with "Babai the Little". Cotelier's Monumenta II and John of Damascus in PG 94 hold Meadow chapters and the Damascene's citations. The Anonymus Valesianus in Mommsen's Chronica minora quotes the Life of Severinus. Readability is `engine.m1.gates.grade_text`, run from the repo root. Every brief fix below was applied together to a scratch copy (`/tmp/claude-0/-home-user-CIC-Project/5632ba95-e0b1-504b-a130-94b73aea15af/scratchpad/partB/`) and re-scored.

### Applies to all three

- **Audio = brief.** Each audio script matches its brief exactly once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, at the start of the closing paragraph. No tag appears in any brief or card. When a brief fix below changes a line, the audio script follows it.
- **Readability.** All three pass before and after the fixes. No narrator sentence runs past 25 words. Babai l.13 has 30, but 24 of them are Thomas's quoted words.
- **Card order.** All three follow Mark's order. Missing fields are left out: Severinus has no `keyWorks` or `ownWords`. Each `uncertain` list opens with the brief's caveat.
- **Who test (item 14).** Moschus is a recorder. Babai heads a following and a body of 84 works. Severinus is a founder known through his disciple's record, which the brief marks as a saint's Life. The drafts carry no list lines; those belong to the map build and were not checked here.
- **Modern renderings in quotation marks.** Moschus l.1 and l.11 put English renderings of the Latin column in quotation marks. Babai l.9 renders Labourt's French. The records mark each one as a rendering. I checked each against its Latin or French and found them faithful (Moschus l.10086-10095, 3784-3786; Labourt l.15845-15866). The pattern allows an Opus-authored rendering presented as the quote, and the card's `uncertain` (Moschus) and `ownWords` (Babai) say which language stands behind them. So I raise no finding.

| Profile | Words | Est. length @162 | FK | Flesch | After fixes: words, FK, Flesch |
|---|---|---|---|---|---|
| John Moschus (recorder) | 327 | 2:01 | 6.7 | 70.0 | 324, 7.0, 68.4 |
| Babai the Great (major) | 403 | 2:29 | 6.8 | 73.0 | 404, 6.8, 73.0 |
| Severinus of Noricum | 322 | 1:59 | 6.9 | 69.4 | 324, 7.0, 69.0 |

Totals for part B: 6 blocking (B-B1 to B-B5, B-H1) and 14 minor (B-M1 to B-M14).

---

### 1. John Moschus (recorder)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | minor (B-M1) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (B-M3) |
| 5 | No role for a named witness | PASS |
| 6 | Partisan witness marked | PASS (n/a) |
| 7 | Contested claims show both sides | minor (B-M4) |
| 8 | Common names have place | minor (B-M2) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | minor (B-M3, 327 words) |
| 11 | Readability | PASS (6.7 / 70.0) |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who test | PASS (recorder) |

Checked and sound: the chapter 77 scene (l.9983-10095: noon, Stephen asleep, the Tetrapylon, the three blind men, the corpse that sat up, Sophronius's nod and words); the old notice as Papebroch prints it. That covers Saint Theodosius, the Jordan desert, the New Laura, Antioch, Alexandria, Rome, the wish for burial on Sinai and the Agarene raids (l.24917-24965, 25365-25398, 25455-25462). It also covers Papebroch's 620 from the eighth indiction (l.25403-25405) and Fabricius's first paragraph, before any "HAL." mark (l.3368-3400: "Passim invehitur in heresin Severi Acephali", "fabulosis non destitutum narrationibus", 620 from Bolland). I also checked Lipomanus on John of Damascus and Nicaea II (l.3664-3672), chapter 45 (l.7564-7590) and the dedication (l.3756, 3781-3786). The points the coordinator asked about hold. Photius's notice (Bibliotheca cod. 199) is not held: Freese's volume 1 is the only Photius, and searches for Moschus, Eucrat-, Leimon and 199 find nothing. No English Meadow is held. The brief keeps who is speaking straight, giving the notice its own voice ("the notice says") and Papebroch and Fabricius theirs.

**B-M1 MINOR (item 1). "Monks he met" overstates the Meadow's reach.** Brief l.3, "his book of stories about monks he met"; card `knownFor`, "the sayings and deeds of the monks they met". The dedication speaks of holy men "qui temporibus nostris claruere" (l.3776-3777). The notice says he wrote down what he "audisset vel vidisset" (l.24973), and Papebroch says the same: "ex omnibus quae viderat, audierat" (l.25364-25365). Many chapters are stories told to him about others ("Enarravit nobis abbas Joannes Persa", l.3662). Fix, brief l.3 (merged with B-M3): "Moschus, a monk of Palestine, tells this in the Spiritual Meadow, his book of stories about monks of his time, written for Sophronius." Fix, `knownFor`: "Monk of Palestine who travelled with his disciple Sophronius, later patriarch of Jerusalem, and gathered the sayings and deeds of monks of his time, seen on their travels or told to them, into the Spiritual Meadow, which he dedicated to him."

**B-M2 MINOR (item 8). Three names without their identifier at first mention.**
- Brief l.1, "his friend Sophronius". The identifier "later patriarch of Jerusalem" comes only in l.3. Fix: "One noon in Alexandria, John Moschus and his friend Sophronius, later patriarch of Jerusalem, went to study with the philosopher Stephen." (l.3 loses the phrase, see B-M1.)
- Brief l.5, "says Photius copied much of it". This is a bare name a general listener cannot place. Lipomanus gives "Photius patriarcha Constantinopolitanus" (l.3630). Fix: "says Photius of Constantinople copied much of it." On the card, `keyWorks` 1 `about` becomes "Photius of Constantinople, as Papebroch quotes him, found up to 342 in some copies".
- Card `dates`, "the reigns of the emperors Tiberius and Maurice". A listener will think of Tiberius Caesar. The notes to the same volume write "temporibus Tiberii II imp." (l.24460). Fix: "the reigns of the emperors Tiberius II and Maurice".

**B-M3 MINOR (items 4, 10). Length and two loose phrasings.** The brief runs 327 words, past the non-major ceiling of about 325. In l.5, "He lived long in the desert by the Jordan and at the New Laura" spreads "long" to the New Laura. The notice gives "non exiguo tempore" only for the Jordan desert (l.24938-24939). Fixes, applied with B-M1 and B-M2 to reach 324 words (FK 7.0, Flesch 68.4):
- l.1: "where three blind men were telling how each had lost his sight" becomes "where three blind men told how each had lost his sight".
- l.5: "He lived long in the desert by the Jordan, then at the New Laura of Saint Sabas."
- l.5: "When he heard the holy places had been taken," becomes "Hearing that the holy places had been taken,".
- l.7: "Raiders had closed the road to Sinai, so Sophronius buried him there."

**B-M4 MINOR (item 7). The notice's last words, which Papebroch has to explain away, are not on the card.** The brief tells the burial by Sophronius on the notice's word (l.7). The notice ends by saying the disciple who buried him "reliquumque vitae suae tempus in eodem coenobio transegit" (l.25464-25465). Papebroch says that unless Moschus's companion was someone other than Sophronius of Jerusalem, against "totius pene Graecae antiquitatis consensum", the words must be read loosely, as "de longe maxima vitae reliquae parte" (l.25465-25473). The brief may stand. The card should carry the point. Add to `uncertain`, after "His years": "The disciple. The notice says the disciple who buried him spent the rest of his life at Saint Theodosius. Daniel Papebroch, who holds with almost all Greek tradition that the disciple was Sophronius, later patriarch of Jerusalem, reads that as most of the rest of his life."

**B-M5 MINOR (records). The "English translation" note misdescribes what the search finds.** `absent_details` "An English translation of the Meadow" says the whole-Library search "finds only citations". It also finds two held texts. Cotelier's Monumenta II holds Meadow chapters in Greek and Latin (`cyril-scythopolis_vita-euthymii-cotelier-monumenta-v2-grc-lat_1681.txt` l.46158-59653, "EX JOHANNIS MOSCHI" running heads). John of Damascus's own citations under Sophronius's name are held in PG 94 (`john-damascus_opera-omnia-t1-with-vita-pg94-grc-lat_migne1860.txt` l.91844, 94857, 96433). The absence itself stands. Fix the note: "None held. Whole-Library search for Moschus/Moschi/Moscho, Eucrat-, Evirat-, Limonar-, Leimon, 'Spiritual Meadow' and 'Pratum spirituale' finds no English. It finds Cotelier's Greek-Latin chapters (cotelier monumenta-v2 l.46158-59653), which duplicate part of PG 87.3, John of Damascus's citations in PG 94 (l.91844, 94857, 96433), and citations elsewhere (e.g. Wardrop's Life of Nino l.16933-17002, PO 8, PO 16, Acta Sanctorum March III). The file header says no public-domain English exists."

**Verdict: John Moschus CLEAR** (no blocking finding; B-M1 to B-M5 to apply).

---

### 2. Babai the Great (major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL (B-B1) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a named witness | FAIL (B-B2, Chabot for Mari and 'Amr) |
| 6 | Partisan witness marked | PASS (Braun on Babai; Thomas writing at Beth Abe) |
| 7 | Contested claims show both sides | FAIL (B-B1, B-B4, B-B5) |
| 8 | Common names have place | minor (B-M6); FAIL on namesakes (B-B4) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS (403 words, under the cap) |
| 11 | Readability | PASS (6.8 / 73.0) |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who test | PASS |

Checked and sound: the Seert scene (l.29640-29644) and Babai's career there (l.29652-29680). Thomas I.7 ("somewhat hasty of speech and harsh in command", l.2100-2107), I.12-14 (Jacob's expulsion and the fathers' rebuke, l.2681-2683, 2769-2770; the dispersion, l.2938-3022), I.27 (the three metropolitans, l.4085-4140) and I.35 (the refusal and the angel, l.5164-5188; the closing quotation is verbatim). Braun's "der leidenschaftliche Babai" (braun1900 l.13690-13696). Labourt's De Unione passage (l.15845-15866). Scher's reading of the death (l.29693-29695). On the Thomas of Marga lead, the card rightly cites Book I. Book III, chapters I to III, is Rabban Babai of Gebilta under Selibha-zekha (l.12861-12895), a different man. The brief tells the Seert-against-Thomas dispute over his end in place, naming Scher as the reader. But see B-B4 on the namesakes, and B-B1 and B-B5 on dates.

**B-B1 BLOCKING (items 1, 7). Brief l.3 makes him abbot in the late 500s.** "Babai was an abbot of the Church of the East, in the Persian empire, in the late 500s and early 600s." No source has him abbot before the 600s. Scher reckons his succession to Dadisho "en 603/4" (seert l.29695). Labourt puts Dadisho's death "entre 615 et 620" (labourt1904 l.17771-17772). The card's own `uncertain` 4 carries that dispute. In the 580s and 590s he was a monk under Abraham and Dadisho (seert l.29644-29653; Thomas l.2104-2107). Fix: "Babai was a monk of the Church of the East, in the Persian empire, in the late 500s and early 600s."

**B-B2 BLOCKING (false absence, witness swap: records `absent_details` 3; card `uncertain` 5).** The records say Mari and 'Amr "name other Babais ... but no line naming Babai the Great was found". Both name him, in OCR the search missed. Mari: "Proprio itaque patriarcha ecclesia caruit ad annos decem et septem, eius interea gubernationem gerentibus Mar Aba archidiacono atque Mar Babaoo Magno e coenobio Mar Abraham" (`mari-ibn-sulayman_...gismondi1899.txt` l.13514-13517; "Babaoo" = Babaeo). 'Amr: "Sedem itaque administravit [citra ordinationem ut vicarius] Mar A!ia archidiaconus una cum Mar iJabae-) ^lngno" (`amr-ibn-matta_...gismondi1896-1897.txt` l.13424-13426; = Mar Aba ... Mar Babaeo Magno). The card's `uncertain` 5 gives the point to "J.-B. Chabot says the archdeacon Mar Aba and Babai directed the church". That passage names its sources: "Comp. 'Amr et Mâri dans la Vie du patriarche Grégoire" (chabot1902 l.37359-37361). So the card credits the modern editor with what the held medieval histories say.
- Fix, card `uncertain` 5: "His part in the vacancy. Thomas says three metropolitans asked him to visit the monasteries; the angel in Thomas's story calls him the vicar of the catholicos. The Arabic histories of Mari and 'Amr, in Enrico Gismondi's Latin, say the archdeacon Mar Aba and Mar Babai the Great governed the church while it had no head, and Mari counts seventeen years. J.-B. Chabot follows them."
- Fix, records: replace `absent_details` "Mari and Amr on Babai the Great" with a claim. Claim: "Mari: 'eius interea gubernationem gerentibus Mar Aba archidiacono atque Mar Babaoo Magno e coenobio Mar Abraham' for 'annos decem et septem' (OCR 'Babaoo' = Babaeo); 'Amr: 'Sedem itaque administravit [citra ordinationem ut vicarius] Mar A!ia archidiaconus una cum Mar iJabae-) ^lngno' (OCR for Mar Aba ... Mar Babaeo Magno; the bracket is Gismondi's)". Witness: "Mari, tr. Gismondi (mari gismondi1899 l.13514-13517); 'Amr, tr. Gismondi (amr gismondi1896-1897 l.13424-13426); Chabot cites both (chabot1902 l.37359-37361)". `formation_confidence`: Documented.

**B-B3 BLOCKING (false absence: records `absent_details` 1; card `keyWorks` 2 and `sources.ownWords`).** The records say "the Life of George only as two passages in Chabot's French ... Searched all of cic/texts for Babai/Babaï/Babhai/Babaeus". The whole Life is held in German, under the spelling "Bäbai". Oskar Braun's translation runs from "Geschichte unseres herrlichen und allheiligen Vaters Mär Giwargis ... verfaßt vom heiligen Rabban Mär Bäbai, dem Abte auf dem Berge Izalä" (`persian-martyr-acts_ausgewahlte-akten-persischer-martyrer-bkv22-deu_braun1915.txt` l.12419-12423). It runs to the end of the volume's acts, and Braun abridges only the long introduction (l.12442-12443). Braun's own heading dates George's death to 14 January 615 and calls Babai "Klostervisitator" during the vacancy "608—628" (l.852-858). The Henana charges are at l.13355-13400. Georg Hoffmann's German extracts of the same Life are also held (`persian-martyr-acts_auszuge-aus-syrischen-akten-persischer-martyrer-deu_hoffmann1880.txt` l.5596-5612). The held Life also carries Babai's own first-person preface, listing his earlier Lives of Abraham of Kashkar, written "vor ungefähr dreiunddreißig Jahren", and of Dadisho of Beth Daraye (braun1915 l.12435-12446).
- Fix, records `absent_details` 1: "The Book of the Union is held only as passages quoted in Labourt's French (l.15845-16120). The Life of George is held whole in Oskar Braun's German (braun1915 l.12419 ff., the introduction abridged, l.12442-12443), in Georg Hoffmann's German extracts (hoffmann1880 l.5596-5612) and as two passages in Chabot's French (chabot1902 l.42080-42240). No Syriac or English text of his books is held. Searched all of cic/texts for Babai/Babaï/Bäbai/Babhai/Bàbhay/Babaeus/Babaeo."
- Fix, card `keyWorks` 2 `about`: "a monk of Izla, once a Magian named Mihramgushnasp, put to death under Khosrau. Oskar Braun translates the whole Life into German, and J.-B. Chabot gives two passages in French, among them the charges against Henana of Adiabene; Scher says Paul Bedjan published the Syriac".
- Fix, card `sources.ownWords`: add `{"title": "Life of the martyr George (Mar Giwargis), in Ausgewählte Akten persischer Märtyrer (German tr. Oskar Braun)", "language": "German translation", "file": "cic/texts/persian-martyr-acts_ausgewahlte-akten-persischer-martyrer-bkv22-deu_braun1915.txt"}`.

**B-B4 BLOCKING (items 7, 8; namesakes kept apart wrongly; a held near-contemporary source unused: card `uncertain` 6 and 1; records).** Card `uncertain` 6 lists "Rabban Babai of Gebilta, the singer ... nor Babai bar Nisibnaye, Babai of Nisibis or Babai the Scribe" as separate men. The held East Syrian chronicle that Guidi edited (`chronica-minora-pars-prior-versio-lat_guidi1903.txt`) treats bar Nisibnaye and "Babai of Nisibis" as one man, and as Babai the Great's own contemporary. It names "Màr Babhay filius Nisibenorum" among the monks who came out of the Izla monastery (l.2032-2037). It says Satan stirred quarrels between "duo Babhay", and that "Asseclae, monachi, Mar Babhay magni (maioris) nemini permittebant ut in suum monasterium intraret, quin anathema diceret in eximium Mar Babhay nisibenum quem Babhay parvum (minorem) cognominaverunt" (l.2051-2058). It also says "Scripsit autem Mar Babhay magnus (maior) libros multos, disputationes atque interpretationes" (l.2069-2070). Labourt, a source the card already uses, reports the same quarrel from "l'anonyme de Guidi" (labourt1904 l.13093-13096). Budge instead places "Babhai bar-Nesibhnaye" under the catholicos Selibha-zekha (713-729), "famous for his beautiful voice" (budge1893 l.2071-2073). That is the time and the gift Thomas gives Rabban Babai of Gebilta (l.12863-12895). So the card splits what may be one man into two, and leaves out a dated quarrel between the two Babais that a near-contemporary chronicle records.
- Fix, card `uncertain` 6: "Namesakes. He is not Babai the catholicos of 497 to 502 in J.-B. Chabot's dates, nor Babai the Scribe, whom Abdisho of Nisibis lists. Nor is he his contemporary Babai of Nisibis, also called bar Nisibnaye, a monk who came out of Izla. An anonymous Syriac chronicle that Ignazio Guidi edited calls that monk Babai the Little, and says Babai the Great's followers let no one into their monastery who would not anathematize him. E. A. Wallis Budge instead puts a Babai bar Nesibhnaye, famous for his voice, under the catholicos Selibha-zekha, the time Thomas gives for Rabban Babai of Gebilta, the singer and founder of schools."
- Fix, card `uncertain` 1, add after its first sentence: "An anonymous Syriac chronicle that Ignazio Guidi edited also praises him and tells of his followers' quarrel with Babai the Little."
- Fix, records: add a claim. Claim: the three Guidi quotations above. Witness: "Anonymous East Syrian chronicle, tr. Guidi (chronica-minora guidi1903 l.2032-2037, 2051-2058, 2069-2070); Labourt (labourt1904 l.13093-13096)". `formation_confidence`: Documented. Add a `contested_claim`: "Who Babai bar Nisibnaye was". Sides: "Guidi's chronicle: Babai of Nisibis, son of the Nisibenes, a monk from Izla and Babai the Great's rival, called Babai the Little (l.2036-2058). Budge: Babhai bar-Nesibhnaye flourished under Selibha-zekha, 713-729 (budge1893 l.2071-2073)." Replace `absent_details` 4's companion note as needed so it names the chronicle.

**B-B5 BLOCKING (an editor's year told as the source's: card `legacy.traces` 4).** "In 612, the Chronicle of Seert says, he was too weak and old to join the bishops' debate before Khosrau, but helped them with his pen." The chronicle gives no year. "En 612" is Scher's footnote (seert l.29565), as the records' own witness line says ("612 is Scher's note"). Fix: "The Chronicle of Seert says he was too weak and old to join the bishops' debate before Khosrau, which Addai Scher dates to 612, but helped them with his pen."

**B-M6 MINOR (item 8). Brief l.7, "His Life of the martyr George".** George is a common name. Fix: "His Life of the Izla martyr George charges Henana with teaching fate and denying the resurrection of the body." (Post-fix with B-B1: 404 words, FK 6.8, Flesch 73.0.)

**B-M7 MINOR (item 1). Card `keyWorks` 1, "an unpublished copy that J.-B. Chabot lent him".** Labourt says only "Grâce à l'obligeance de M. Chabot, nous sommes en mesure d'adjoindre à ces textes un traité inédit de Babaï" (labourt1904 l.15764-15766). "Lent" adds a detail. Fix: "from an unpublished copy that J.-B. Chabot made available to him".

**B-M8 MINOR (item 7). Card `uncertain` 4, "J. Labourt puts Dadisho's death between 615 and 620".** The OCR line reads "Il mourut âgé de soixante-quinze ans, phone / 'entre 615 et 620" (labourt1904 l.17771-17772). A garbled word stands before "entre" and may be a hedge such as "probablement". Check the page image. If it is a hedge, write "J. Labourt puts Dadisho's death probably between 615 and 620", and adjust the records claim and contested side to match.

**Verdict: Babai the Great NOT CLEAR** (B-B1 to B-B5).

---

### 3. Severinus of Noricum

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a named witness | PASS ("his translator George W. Robinson" names him) |
| 6 | Partisan witness marked | PASS (n/a; hagiography marked) |
| 7 | Contested claims show both sides | minor (B-M11) |
| 8 | Common names have place | minor (B-M9) |
| 9 | One term for one thing | minor (B-M10) |
| 10 | Story, scene, disputes in place, length | PASS (322 words) |
| 11 | Readability | PASS (6.9 / 69.4) |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | List line, Who test | PASS |

Checked and sound. The death scene and both quotations are verbatim (robinson1914 l.3709-3712, 3828-3837). The memoir from "the daily narrations of the elder brethren" is at l.294-296, and Primenius and "purest Latin stock" at l.395-452. The rest checked at: the coming after Attila's death (l.788-793); fasting, prayer and alms (l.864-865); the refused bishopric (l.1689-1691); Odoacer and "Go forth to Italy!" (l.1489-1523); Giso, the rebaptism and Feva's reverence (l.1531-1538); Joseph's bones (l.3583-3585); Onoulfus's order (l.3927-3928); Gelasius, Victor, Barbaria and the Lucullan castle (l.4037-4049); Paschasius's reply (l.4253-4260); Gregory's letter to Anthemius (mansi-10 l.23210-23229); Foulke's note after Waitz (l.2672-2677). On the dates the coordinator asked about, the brief and card are right. The year is Robinson's ("c. 482", table l.4863) and Waitz's, through Foulke ("He died A.D. 482", foulke1907 l.2674). Eugippius gives only the day. No held line gives Mommsen's own year for the death. Mommsen's held Chronica minora dates only the Life, "editam a. 511" (chronica-minora-liber-genealogus l.33502). The card tradition reads as the README says. The README's reason holds: Eugippius has him "in the confession of the Catholic faith" (l.796), and the Rugian rulers' Arianism is Robinson's conclusion (l.1305-1308). The placing in Early Benedictine / Italian Monasticism rests on his community's move to the Lucullan castle, which Gregory's letter attests. It is a census placing and makes no claim on the card.

**B-M9 MINOR (item 8). Brief l.1, "Severinus felt a pain in his side".** The subject's own common name has no place at first mention, and "Riverside Noricum" first comes in l.5. Pope Severinus and Severinus Boethius share the name. Fix: "On the fifth of January, Severinus of Noricum felt a pain in his side." (Post-fix: 324 words, FK 7.0, Flesch 69.0.)

**B-M10 MINOR (item 9). The card names the Rugian queen two ways.** `legacy.traces` 3 has "King Feletheus and Queen Gisa" (Paul's spellings, foulke1907 l.2656-2657). `uncertain` 4 has "Queen Giso" (Eugippius's, robinson1914 l.1532), and the brief says "King Feva". Fix, `legacy.traces` 3: "Paul the Deacon, writing the History of the Langobards, names his monastery in Noricum and his warnings to the Rugian king Feletheus and his wife, whom Paul calls Gisa, and says Naples keeps his remains."

**B-M11 MINOR (items 1, 7). Card `uncertain` 3 loosens Eugippius's clue and pins it to the wrong year.** It says "more than five years had passed when the grave was opened, after Odoacer's war on the Rugians, which Robinson dates to 487". Eugippius says "the sixth year of his burial had already passed" (l.3965-3966). The opening came when Onoulfus ordered the Romans out, after Fredericus's return, which Robinson dates "488 ?" (table l.4869-4876). The war of 487 came before that. Fix: "The year of his death. Eugippius gives the day only. The year 482 is Robinson's and Waitz's. Eugippius's own clue is relative. He says the sixth year since the burial had passed when the grave was opened, as the Romans left for Italy after Odoacer's war on the Rugians. Robinson dates the war to 487 and the removal, with a query, to 488."

**B-M12 MINOR (records). A held early reader of the Life is left out of the "second witness" note.** `absent_details` "A second independent witness" lists what the search finds. It leaves out the Anonymus Valesianus in Mommsen's Chronica minora, which quotes the Life on Odoacer's visit: "de quo ita invenitur in libris vitae beati Severini monachi intra Pannoniam" (`chronica-minora-liber-genealogus_mommsen1892.txt` l.40428-40445; also `prosper_chronica-minora-1-lat_mommsen1892.txt` l.40340-40357). It is not independent, and Mommsen says it cites the Life (l.33502). The absence stands. Fix: add to the note, "and the Anonymus Valesianus, which quotes the Life on Odoacer (chronica-minora mommsen1892 l.40428-40445)".

**B-M13 MINOR (README l.9). "The correction is logged in Open-Gaps."** `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` has no entry on Severinus's placing, and this branch does not touch the file (`git log origin/main..HEAD -- .../Open-Gaps.md` is empty). Fix: append the numbered Open-Gaps entry the README promises (the batch 6 entry, with the scan correction "Severinus of Noricum: Early Benedictine / Italian Monasticism only; the Homoian placing came from the Rugians he lived among"), or until then reword to "The correction is to be logged in Open-Gaps with the batch 6 entry."

**Verdict: Severinus of Noricum CLEAR** (no blocking finding; B-M9 to B-M13 to apply).

---

### 4. Batch 5 records correction: `henana-of-adiabene`, "A second witness to Babai's doctrinal charges"

The corrected note in `era3/batch5/records.json` reads in part: "Both held texts that state the charges are Babai's own: his De Unione, held in part as J. Labourt quotes it in French from an unpublished copy Chabot lent him (labourt1904 l.15763-15866; on Henana and the resurrection body, l.15816-15818), and his Life of George of Izla, held as the two passages Chabot gives in French (synodicon-orientale chabot1902 l.42081-42240)."

Cited lines:
- labourt1904 l.15763-15866. The De Unione introduction is at l.15764-15768 ("Grâce à l'obligeance de M. Chabot ... un traité inédit de Babaï sur l'Incarnation (De unione)"). l.15763 is the end of the preceding sentence, on the Passion of George and the 612 exposition. The first quoted passage ends at l.15866 ("en sorte qu'il n'y a pas deux Fils ou deux Fils du Très-Haut"). The range is right to within one line.
- labourt1904 l.15816-15818. Labourt's footnote: "D'après le traité De Unione, Henana admettait que le corps du Christ ressuscité et ceux des fidèles ... étaient [sphériques] (ms., p. 126)". The sentence runs on to l.15820 ("comme on le voit d'après l'anathème qui conclut le ch. xix"). It is a report by Labourt of De Unione, not a quotation. The note's "as J. Labourt quotes it" covers the passages; for this point "reports" is the exact word.
- chabot1902 l.42081-42240. Chabot's two passages, from "composée par saint Rabban Mar Babai" (l.42080-42081) through the monk's list of charges (l.42093-42104) and "Le sort et la fatalité sont cause de tout" (l.42113-42118), to the anathema on "Henana le chaldéen et l'hérétique" (l.42242). Right.

Is the note now true? The core claim holds. Every held text that states the fate and resurrection charges is Babai's own. I found no other held author who states them: Seert's "doctrines hérétiques" names none, and Timothy I, through Assemani, condemns Henana's exegesis, not these doctrines (assemani 3.1 l.14926-14935). But one clause is false.

**B-H1 BLOCKING (false absence, batch 5 records).** "His Life of George of Izla, held as the two passages Chabot gives in French". The Life is held whole in Oskar Braun's German (braun1915 l.12419 ff.). The charges stand there: "Er leugnet die Auferstehung der Leiber und (lehrt), daß es eine Erlösung nur für die Seelen gebe" (l.13355-13400). Georg Hoffmann's German extracts hold the same passage: "der dort sehr verbreiteten Haerese des Hannänä Hdhaijabhäja, welcher das Schicksal lehrt ... leugnet die Auferstehung der Leiber" (hoffmann1880 l.5596-5612). The batch 5 R1 review already named the Hoffmann extracts as "a second translation of Babai, not a second witness" (R1_review.md l.183). Exact replacement note: "None held. Both held texts that state the charges are Babai's own: his De Unione, held in part as J. Labourt quotes and reports it in French from an unpublished copy Chabot made available to him (labourt1904 l.15764-15866; on Henana and the resurrection body, l.15816-15820), and his Life of George of Izla, held whole in Oskar Braun's German (persian-martyr-acts bkv22 braun1915 l.12419 ff.; the charges at l.13355-13400), in Georg Hoffmann's German extracts (persian-martyr-acts hoffmann1880 l.5596-5612) and as the two passages Chabot gives in French (synodicon-orientale chabot1902 l.42080-42240). Babai's Evagrius commentary is cited by Braun and Labourt but not held; the Chronicle of Seert speaks of 'doctrines heretiques' without naming them."

**B-M14 MINOR (same note).** The same false "lent him" as B-M7 ("an unpublished copy Chabot lent him"). The replacement above already uses "made available to him".

---

## Verdicts

- John Moschus: **CLEAR** (0 blocking, 5 minor).
- Babai the Great: **NOT CLEAR** (5 blocking: B-B1 to B-B5; 3 minor).
- Severinus of Noricum: **CLEAR** (0 blocking, 5 minor).
- Batch 5 Henana records correction: **NOT YET TRUE** in one clause (B-H1 blocking, B-M14 minor).
