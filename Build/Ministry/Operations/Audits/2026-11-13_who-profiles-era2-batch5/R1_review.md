# R1 review: ten Who profiles, era 2 batch 5

Two independent Opus reviewers, each at first sight of its drafts, reviewed the batch in two parts: part A (Socrates of Constantinople, Mesrop Mashtots, Cyril of Alexandria, Sozomen, Theodoret of Cyrrhus) and part B (Leo of Rome, Koriun, Alexander of Alexandria, Eusebius of Nicomedia, Ossius of Cordoba, and the README). Totals: 1 blocking, 22 minor. Each part follows as written.

## R1 review: era 2 batch 5, part A (Church Family Tree Who profiles)

Reviewer: independent, first sight of these drafts. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; and the failure types of the era 2 batch 1 to batch 4 R1 reviews, above all the witness swap. I did not edit the drafts. I made no paid or model-API calls and used no web. Readability and quote search ran on local scripts only.

Profiles: `socrates-of-constantinople`, `mesrop-mashtots` (MAJOR), `cyril-of-alexandria` (MAJOR), `sozomen`, `theodoret-of-cyrrhus` (MAJOR). Files are in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch5/`. Brief line numbers refer to the `.brief.txt` files, where each paragraph is one line and blank lines count. Other line numbers point to files under `cic/texts/` unless marked. The batch README is outside part A and was not reviewed.

Method. I searched every quotation in the five briefs and cards in the vendored file the card names. The match stripped XML tags, collapsed whitespace and normalised quote marks; for the Langlois OCR and Perry's Syriac acts I also used a letters-only match. I read each hit in context to see who is speaking: the ancient author, a document he quotes, the translator's introduction, a footnote, or a bracket the translator supplied. I checked every factual sentence of each brief against its passage, reading Emine's French of Koriun, Moses of Khoren III.67 and Lazar of Pharp in full where Mesrop's brief and card use them. I compared each `records.json` entry with its brief and card. Readability came from `engine.m1.gates.grade_text`, run from the repo root. Length assumes 162 words a minute.

## Applies to all five

- **Audio = brief.** Each audio script matches its brief exactly once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, placed before the final sentence. No tag appears in any brief or card.
- **Readability.** All five pass (FK at most 10, Flesch at least 60). Theodoret sits nearest the floor (Flesch 61.8). Four sentences run past 25 words, and in each the excess is quoted source (Socrates l.11, Sozomen l.13, Theodoret l.7 and l.9), so none is a finding.
- **Card order.** All five follow Mark's order. Missing fields are left out: Mesrop has no keyWorks and no "Their own words", since no writing of his is held. keyWorks never goes past three. Each `uncertain` list opens with the brief's own caveat or its main witness limit. The `"date": null` in source entries is the schema the earlier batches used.
- **Length.** Mesrop (406 words, 2:30), Cyril (405, 2:30) and Theodoret (406, 2:30) are at the major cap; one word over "about 405" is within "about", as batch 4 ruled. Socrates is 326 words (2:01) and Sozomen 321 (1:59). Every `briefLength` matches.
- **Who test (item 14).** Socrates and Sozomen are recorder Whos, as the README says. Mesrop is a founder known through a disciple's record (Koriun), and his brief marks the Life as a disciple honouring a saint. Cyril and Theodoret each have a body of work and a following. The drafts carry no list lines; those belong to the map build and were not checked here.

| Profile | Words | Est. length @162 | FK | Flesch |
|---|---|---|---|---|
| Socrates of Constantinople | 326 | 2:01 | 6.9 | 66.8 |
| Mesrop Mashtots (MAJOR) | 406 | 2:30 | 7.0 | 69.6 |
| Cyril of Alexandria (MAJOR) | 405 | 2:30 | 6.9 | 65.4 |
| Sozomen | 321 | 1:59 | 7.3 | 64.4 |
| Theodoret of Cyrrhus (MAJOR) | 406 | 2:30 | 8.0 | 61.8 |

---

## 1. Socrates of Constantinople

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Zenos, Valesius, Baronius, Harnack, Hartranft named) |
| 6 | Partisan witness named and marked | PASS (no partisan witness carries a claim) |
| 7 | Contested both sides | PASS (Novatian: Baronius v. Valesius; lawyer: Zenos and Valesius v. Harnack, Hartranft) |
| 8 | Common names placed | PASS |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:01) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder Who) |

**Quotes** (all exact, speaker confirmed; `npnf202_socrates-sozomen-ecclesiastical-histories.xml`)
- "in my youth at Constantinople" (l.1): Socrates V.16 (l.15686). Helladius's boast of "nine men" and Ammonius's complaint that the statue was kept "in order to render that religion ridiculous" are in the same chapter (l.15700–15712). Theophilus's own stated reason is different ("Lest… the heathens should deny…"), and the brief rightly gives the "ridiculous" reading to Ammonius.
- "where I was born and educated" (l.3): V.24 (l.16777).
- "O holy man of God, Theodore" (l.3, card): VI, Introduction (l.16923) and VII.48 (l.21609). II.1 has "O sacred man of God, Theodore", which the brief does not quote.
- "that more credit was due to him who had suffered" (l.5): II.1 (l.5660). The rewriting and the added letters of the emperors and decisions of the bishops follow at l.5662–5683.
- "Most holy" (l.5) and the card's "The zealots of our churches will condemn us for not calling the bishops 'Most dear to God,' 'Most holy,' and such like.": VI, Introduction (l.16955–16956).
- "a mere youth" (l.7): I.13 (l.3859). Auxanon, "a very aged presbyter of the Novatian church", went to Nicaea "when quite a youth" (l.3855–3858).
- "may live in peace; for as long as peace continues, those who desire to write histories will find no materials for their purpose" (l.11): VII.48 (l.21607).
- Card: "is a matter of difficult critical investigation" (Zenos, l.691); "according to the best authorities" (Zenos, l.1672); "Socrates was the finer mind, that he had larger sympathies" and "with a sharper and brighter criticism" (Hartranft, l.24637–24639); "simply an uncertified tradition" (Hartranft, l.22057). All Zenos's or Hartranft's own words, and the card names them so.

**Narrative checks**
- Plain style for "the masses and illiterate men, who are intent merely on knowing the facts": VI, Introduction (l.16926–16950). Faithful.
- Seven books from Constantine's proclamation to Theodosius's seventeenth consulship, VII.48 (l.21613–21622); 439 is the note there and Zenos's introduction (l.890–892). The continuation of Eusebius is I.1 (l.1855–1870).
- Zenos on the Novatians: Baronius, Labbe and others "after Nicephorus Callisti" held he was one (l.941–946), and the passages are listed as their arguments (l.946–1016); Valesius "followed by most of the more recent writers" puts it down to impartiality (l.1019–1035), and Socrates "mentions the Novatians as distinct from the Catholic Church" (l.1043–1046). The brief's and card's telling is faithful.
- Scholasticus: from "student" to "any one who had passed through study to the professions, of which the advocate's was one" (Zenos's note, l.869–877); Zenos "According to the preponderance of evidence" (l.866); Valesius "a layman and a lawyer" and Harnack's denial (l.883–886). Faithful.
- Card dates: Valesius's 379, "the only certainty… that he was born nor earlier than 379" (Zenos, l.725–733, the source's own misprint "nor"); "He must have lived… until some time after that date, as he speaks of a revision of the first two books" (l.900–901). Theodore "rightly… inferred" to be a presbyter, and not Theodore of Mopsuestia, d. 429 (l.1250–1257). Liberatus "the Carthaginian deacon" and Theodorus Lector (l.1677–1679); the Tripartite History (l.1689–1694). All faithful.
- records.json matches the brief and card. Both disputes have `contested_claim` records.

**Findings**
- None.

---

## 2. Mesrop Mashtots (MAJOR)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, minor (M2) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Koriun, Langlois, Moses of Khoren, Lazar of Pharp, Saint-Martin, Indjidji, Emin named; "a note in Langlois's edition" is used only where the note has no signed author) |
| 6 | Partisan witness named and marked | PASS (Koriun placed as a disciple honouring a saint, early, at l.3) |
| 7 | Contested both sides | FAIL, minor (M1); PASS on the death day and Samos/Samosata (card) |
| 8 | Common names placed | PASS in the brief; card minor (M3) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:30) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (founder through a disciple's record) |

**Quotes and close tellings** (`langlois_collection-historiens-armenie-tome2-fra_1869.txt`; Emine's French of Koriun, l.3420–4400)
- Koghten, the remnants of pagan ways, and the difficulty of preaching without Armenian letters; his prayer for them (l.1): Koriun, l.3496–3505, 3518–3525. Faithful.
- "men he saw with his own eyes" (l.3): "des hommes que nous avons nous-même vus de nos yeux" (l.4339–4340), with "Nous fûmes les témoins attentifs… et les serviteurs de ces saints docteurs" (l.4342–4344). The demons fleeing toward Media (l.3507–3512) back "with demons put to flight". "His pupil": Koriun's "serviteurs" and Lazar of Pharp's "Gorioun, disciple du bienheureux Maschthotz" (l.36209–36210).
- Son of Vartan, from Daron (OCR "Baron"), Greek literature as a child, the royal archives, then the monk's life (l.3): Koriun, l.3428–3450. The note giving 361, 441 and "à l'âge de quatre-vingts ans" is at l.3474–3477; it is unsigned, and the brief correctly says "A note in Langlois's edition".
- Sahak, Vramshapuh, Syrian Mesopotamia, Daniel's promise and the failure (l.5): l.3555–3585. "comme si [c'eût été] les Tables divines" (l.7, "tablets from God"): l.3646–3647. The right hand writing on stone, "dans son cœur" (l.5): l.3586–3593, 3621–3625.
- "un solitaire de Samos… Rufin… disciple d'Épiphane, qui donna aux caractères les formes voulues… d'après le mode parfait de l'alphabet des Hellènes" (l.5): l.3626–3633. The brief's "whom the text calls a man of Samos" is exact.
- Proverbs first (l.3634–3636); Theodosius the Younger on the throne (l.3643); children "ayant la voix douce", schools in every province (l.3651–3656); the Georgians and the Aghouank (l.3657–3664). Faithful.
- Persian governors allowing only Syriac (l.9): l.3697–3702; Atticus "conféra à Mesrob [le titre de] prédicateur" (l.3725–3727). The brief folds in the move to Roman Armenia and Vartan's company; nothing told is wrong.
- Borborides: "la prison, les chaînes… on les brûlait, on les enfermait et on les chassait du pays" (l.11): l.3779–3787. Kept as Koriun's.
- Theodore, "exclu du concile d'Éphèse… Théodore [de Mopsueste]", books after "Paul de Samosate et de Nestorius", the council's letters, the expulsion (l.11): l.4098–4110. The brief drops the bracket and Paul of Samosata; both choices are sound.
- Death "la même année, le dixième mois après la mort… de Sahag, le dix-huitième jour de méhégan… dans la Ville-Nouvelle", after "quelques jours de maladie"; he "se mit sur son séant… bénit la très-sainte Trinité et confia ses disciples à la grâce de Dieu" (l.13): l.4213–4240. "blessed God" for "the Holy Trinity" is a fair plain telling.
- "caractères mesrobiens… la seule appellation que l'on a coutume de donner à l'alphabet national arménien" (l.15, card): Langlois, l.3044–3050.
- Card: Moses of Khoren's "qui surpassait en vertu ses contemporains les plus vertueux" (l.25335–25338, Moses III.67, thirteenth of méhégan, six months, Vagharschabad); Lazar's "Vagharschabad, nommée également nouvelle ville", 13 méhégan, six months (l.37874–37878); Lazar's pointer to Koriun's Life "à quelle époque, en quel endroit et par le moyen de qui les lettres furent retrouvées" (l.36209–36212); "ne fit que reprendre un travail" (Langlois after Indjidji, l.3053–3058); the copyists' "Samos" (Langlois, l.3406–3407) and Saint-Martin's Samosata (note, l.3671–3674); the Mamikonian supposition by Emin (note, l.3477–3479); "quelques auteurs le prétendent… ce qui est le plus vraisemblable" on the army and the archives (Langlois, l.2810–2814); Moses as Mesrop's nephew (Langlois's introduction to Moses, "Son oncle Mesrob prit soin de son éducation"). All exact, speakers correct.

**Narrative checks**
- The card's treatment of "[de Mopsueste]" as the bracket's, not Koriun's, is right, and the record does the same.
- Langlois says that "Gorioun et Moïse de Khorène font observer qu'il existait… un ancien alphabet national" (l.3059–3062), citing the Armenian edition. The held French of Koriun has no such line (searched l.3420–4400). The card's "Koriun says the Syrian bishop Daniel's help came to nothing" is true of the held text; this is noted for the reviser and is not a finding.
- records.json matches the brief and card, and carries three `contested_claim` records (death, first letters, Rufinus's town).

**Findings**
- **M1 MINOR (item 7; disputes in place).** `records.json` carries "Whether Mesrop was the first to make Armenian letters" as a `contested_claim`, with Langlois (after Luc Indjidji) and the later writers he quotes on the other side. The card's `uncertain` item 4 gives that side. The brief does not. It tells Daniel's failure and the revelation, and closes on "the Mesropian letters", so a listener hears only Koriun's side of the founding claim the profile rests on. This is the pattern of batch 4 Pelagius M1. Lazar of Pharp, a held fifth-century witness, also says Daniel already held Armenian letters that proved "insuffisantes" (l.36299–36316). Fix: in l.5, after "…but they could not find signs for the sounds of Armenian.", add "Lazar of Pharp, a later Armenian historian, says Daniel already held old Armenian letters, too few for the language. Langlois, after Luc Indjidji, holds that Mesrop took up work begun long before." To stay within about 405 words, drop l.7's "Koriun adds that he gave the Georgians letters and renewed those of a people called the Aghouank." The card states it twice (`legacy.traces` 2, `uncertain` 7).
- **M2 MINOR (items 1, 5; a bracket given to the author).** Card `legacy.traces` item 1 says "Sahak corrected the first hasty translations against them" as Koriun's. In the French the subject is the translator's bracket: "Ensuite, [Sahag] reprit en sous-œuvre les livres qui avaient été traduits d'abord à la hâte" (l.3870–3872). The sentence before has "les bienheureux saints Sahag et Mesrob" as subject. The card treats the "[de Mopsueste]" bracket carefully and should treat this one the same way. Fix: "…They brought back sound copies of the Scriptures, and the first hasty translations were corrected against them; the French supplies Sahak's name in brackets."
- **M3 MINOR (item 8, card).** Card `knownFor` says "made the Armenian letters with a hermit named Rufinus". Rufinus is a common name, and Rufinus of Aquileia is a batch 4 Who; the place first appears only in `uncertain` item 5. Card `legacy.traces` item 1 has "Joseph" with no identifier, while the note the card relies on names him "Joseph de Baghin" (l.3639–3640, note 4 at l.3679–3680; Koriun's Edessa passage points back to it at l.3836). Fix: `knownFor` "…with a hermit named Rufinus, whom Koriun's text calls a man of Samos, …"; `legacy.traces` 1 "Eznik of Goghp and Joseph of Baghin among them".

---

## 3. Cyril of Alexandria (MAJOR)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, minor (M1, M3) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL, minor (M2) |
| 5 | No role for a witness | PASS (Socrates, Zenos, Nestorius, Percival, Jackson, Venables, Bright, Driver and Hodgson named) |
| 6 | Partisan witness named and marked | PASS (Socrates's Novatian leaning placed by Zenos at the Hypatia verdict; Nestorius "Cyril's enemy") |
| 7 | Contested both sides | PASS in the brief (Hypatia; the two depositions; bribery); card minor (M3) |
| 8 | Common names placed | PASS in the brief; card minor (M4) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:30) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes** (all exact, speaker confirmed)
- "rightly and blamelessly" (l.1): Cyril at Ephesus, Session I (`npnf214_seven-ecumenical-councils.xml` l.15820). The individual votes are Percival's bracketed summary (l.15822–15828), and the record says so.
- "we all anathematize Nestorius as a heretic" (l.1): the bishops' cry (l.15845).
- "with greater power than Theophilus had ever exercised" (l.3): Socrates VII.7 (`npnf202…` l.19112). The bracket "[Yet the partisans of Cyril triumphed.]" is "not found in the Greek" (note, l.19105–19108); the brief does not use it, and the record says so. Good.
- "Let no one call Mary Theotocos" (l.7): Anastasius's sermon in Socrates VII.32 (l.20705). Nestorius "delivered several public discourses… and totally rejected the epithet Theotocos" (l.20733–20736) backs "Nestorius backed him".
- "ventured to call the holy Virgin, the Mother of God" (l.7): Cyril's Second Letter to Nestorius (npnf214 l.15795), with the following clause told faithfully.
- "the gold of iniquity" (l.9, card): Nestorius, Bazaar (`nestorius_bazaar-of-heracleides_driver-hodgson1925.txt` l.15817).
- "Let the heavens rejoice, and let the earth be glad" (l.9): Cyril to John (npnf214 l.19428), where Cyril quotes the Psalm in his own opening.
- "Everlasting be the memory of Cyril. Leo and Cyril taught the same thing." (l.11, card): the bishops at Chalcedon after the Tome (npnf214 l.20002).
- Card: "flesh animated by a rational soul" (l.15737); "the Holy Virgin is the Mother of God" (Anathematism I, l.16300); "confirmed by the subscription of all" (Aëtius, l.19394); "because he wrote against these very Anathemas" (Percival, l.15881); "the Acts do not recite…" (Percival, l.15897); "himself had drawn up at Ephesus two years before" (Jackson, `npnf203…` l.4413); "severe censure" (Zenos, npnf202 l.1075); "not the least opprobrium, not only upon Cyril" and "but also upon the whole Alexandrian church" (Socrates VII.15, l.19572–19589, split by the note, quoted as two pieces); Bright's "Cyril was no party…" (the note, l.19583–19585); "June 9, or 27, 444", "A painful suspicion of their genuineness, however, still lingers", "ascribed to Theodoret" (Venables, quoted by Jackson, npnf203 l.38192–38204); "At last and with difficulty the villain has gone." (Letter 180, l.38224). All exact, speakers correct.

**Narrative checks**
- Theophilus's death 15 October and the consuls, Timothy, Abundantius "the commander of the troops in Egypt", the third day, the Novatian churches (VII.7, l.19087–19122). The night attack, the synagogues, the expulsion (VII.13, l.19428–19448). Nitria, Ammonius's stone, death under torture, "enrolled among the martyrs" (VII.14, l.19484–19512). Hypatia, frequent interviews with Orestes, the crowd led by the reader Peter, March, the year 415 in the note (VII.15, l.19545–19592). All faithful. "Socrates does not say Cyril ordered it" is true of VII.15.
- "June 431": Percival's introduction gives the session "on June 22" (npnf214 l.17808). Ephesus in Socrates VII.34: Cyril's party did not wait for John; Nestorius's party deposed Cyril and Memnon; John "pronounced unqualified censure on Cyril as the author of all this confusion" (l.20895–20912). Nestorius's own account has the council that came with John depose "Cyril and Memnon" (Bazaar l.15199–15209, and the Easterns' report at l.15298–15318). The card's `uncertain` item 4 is right.
- Driver and Hodgson's note on "the letters of Acacius of Beroea and Epiphanius the Archdeacon and Syncellus of Cyril" (Bazaar l.15954–15956). Faithful.
- Jackson gives 444 himself (npnf203 l.4197, l.17793 "from 412 to 444"), so "died in 444, by Blomfield Jackson" stands. Jackson's note on Letter 180: Baronius contested it, Garnerius thought the bitterness no argument against it (l.38160–38170). Faithful.
- records.json matches, with four `contested_claim` records.

**Findings**
- **M1 MINOR (item 1).** Brief l.1: "One by one they said he had. Then, the acts record, they cried out together, 'we all anathematize Nestorius as a heretic.'" In the acts the cry does not follow the vote on Cyril's letter. Nestorius's own letter was read next, and the bishops gave their opinions on it one by one; the cry came after that (npnf214 l.15829–15845). As written, the cry seems to answer Cyril's letter. Fix: "One by one they said he had. Then Nestorius's reply was read and judged, and the acts record that they cried out together, 'we all anathematize Nestorius as a heretic.'"
- **M2 MINOR (item 4; a paragraph that opens on a thesis).** Brief l.5 opens "Socrates tells of hard years." It carries no fact, and the paragraph's own events give it its weight. Fix: delete it and begin "Socrates says that after Jews killed Christians in a night attack, Cyril led a crowd to the synagogues and drove the Jews from the city."
- **M3 MINOR (items 1, 7, card).** Card `uncertain` item 5 says the reception of the Twelve Anathematisms at Ephesus is disputed. It then names only Percival, through his "the Acts do not recite that this letter of Cyril's was read…". That makes Percival the doubter. In fact he goes on: "I would suggest, however, that for those who defend John of Antioch… it is the height of inconsistency to deny that the Council adopted the Anathemas" (npnf214 l.15897–15904). The acts extract he prints also has the bracket "[The letter was read which begins thus:] … Cum Salvator noster" (l.15858–15864), the opening of the letter with the anathemas. The record's `contested_claim` has the bracket; the card does not. Fix: "Whether Ephesus received the Twelve Anathematisms is disputed. Henry Percival says 'the Acts do not recite that this letter of Cyril's was read, nor do they state that the Anathemas were received', though the extract he prints has a bracket saying the letter was read. He thinks the council most likely adopted them, and adds that no one disputes that Chalcedon received them twenty years later."
- **M4 MINOR (item 8, card).** Card `legacy.traces` item 1 says "the archdeacon Aëtius said". Aëtius is a common name, and Aetius of Antioch is an era 2 batch 1 Who. The acts give the place: "Aëtius, the Archdeacon of the imperial city" and "Aëtius the Archdeacon of Constantinople" (npnf214 l.19401, 20019). Fix: "Aëtius, archdeacon of Constantinople, said…".

---

## 4. Sozomen

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, minor (M1) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Hartranft, Zenos named) |
| 6 | Partisan witness named and marked | PASS (no partisan witness carries a claim; the Hilarion story kept as "It is said") |
| 7 | Contested both sides | PASS (use of Socrates: three views, Hartranft's own named) |
| 8 | Common names placed | PASS (Hilarion of Gaza, Socrates of Constantinople, Theodoret of Cyrrhus at first mention) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (1:59) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder Who) |

**Quotes** (all exact, speaker confirmed; `npnf202_socrates-sozomen-ecclesiastical-histories.xml`)
- "My grandfather and many of my ancestors were compelled to flee in this manner" (l.1): Sozomen V.15 (l.36359). Pagan parentage, Alaphion, Bethelia "a populous town near Gaza" (l.36360–36363); "It is said that the above-mentioned families were converted through the instrumentality of the monk Hilarion" (l.36372–36378). The hedge is kept.
- "the other family" (l.3): V.15 (l.36386–36388). Hartranft's note "He probably means that of Alaphion" falls between "other" and "family"; the base text reads "the other family". "but they were then very aged" (l.36395).
- "an advocate in the same court of justice as that to which we belong" (l.5): II.3 (l.28468). "I myself received the greatest benefits" (l.28462) backs "the shrine helped him too".
- "purify it by thy labors" (l.7): Dedication (l.26184). "stretches to thy seventeenth consulship" (l.26189), and Hartranft's note "a.d. 323 to a.d. 439, but he did not carry the narrative further than a.d. 425" (l.26190–26192). The brief gives the years to Hartranft. Good.
- "such epistles as favored their own heresy" (l.9): I.1 (l.26409).
- "such a record of their manner of life that others, led by their example, might attain to a blessed and happy end" (l.13): I.1 (l.26444), Sozomen's own words. Hartranft repeats the line in his introduction (l.23248), but the brief gives it to Sozomen, which is right.
- Card: "wholly unfair and unwarranted by the general usage of his day" and "a feeble reviser of Socrates" (Hartranft, l.24633); "has taken his stuff from Sozomen, and says nothing about the original" (l.24631); "was the finer mind" (l.24637); "from the ascension of Christ to the deposition of Licinius" (Sozomen, quoted by Hartranft, l.22332); "cannot yet be accurately determined" (l.21680); "We can only guess" (l.21784). All exact.

**Narrative checks**
- The grandfather's gift for Scripture, Ascalon and Gaza (l.36380–36386). The first churches and monasteries founded by "this family" (l.36388–36390). Hartranft finds the use of Socrates "sure", from the Novatian material "reproduced by Sozomen as Socrates gives them" (l.24598–24608), and gives the three views (l.24617–24624). "Socrates preceded Sozomen by a few years" (l.24595). Born "somewhere between 370 and 380", reckoned back from Hilarion, the grandfather and the exile (l.21784–21793). Writing "not very soon after June 443" (l.22394–22401). All faithful.
- records.json matches the brief and card. The Hilarion story is tagged Inferential-Thin, which suits Sozomen's "It is said".

**Findings**
- **M1 MINOR (item 1; a hedge dropped).** Brief l.3 says "Chester Hartranft… takes this to mean Alaphion's". Card `uncertain` item 2 says "Hartranft's note takes it to be Alaphion's", and the records claim says "the family is Alaphion's by Hartranft's note". The note reads "He probably means that of Alaphion" (l.36388). This is the batch 3 dropped-hedge pattern. Fix: brief "Chester Hartranft, who revised the English translation, thinks it probably means Alaphion's."; card "Hartranft's note says he 'probably means that of Alaphion.'"; records "probably Alaphion's, by Hartranft's note".

---

## 5. Theodoret of Cyrrhus (MAJOR)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS in the brief; records minor (M2) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Jackson, Bertram, Möller, Dioscorus, Leo, Gennadius, Richardson named; "Bertram, a modern scholar" names the witness first) |
| 6 | Partisan witness named and marked | PASS (his own letters "to answer his accusers"; the 449 acts as his opponents', on the card) |
| 7 | Contested both sides | PASS (views at Chalcedon: Bertram v. Möller; Jackson's "substantially at one" against the sentences of 449 and 553) |
| 8 | Common names placed | FAIL, minor (M1) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:30) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes** (all exact, speaker confirmed; `npnf203_theodoret-jerome-gennadius-rufinus.xml` unless marked)
- "Theodoret must now anathematize Nestorius", "Unless I set forth at length my faith I cannot speak", "Anathema to Nestorius" (l.1): the Chalcedon acts as Jackson quotes them from Labbe (l.3307–3337). The brief says "The council's acts record the scene, and Blomfield Jackson, his translator, quotes them", which places the speaker right. "Anathema to Nestorius" is the start of Theodoret's longer sentence (l.3335), not a cry of the bishops (who shout the same words at l.3319).
- "unwillingly consecrated", the parents' promise "Even before my conception" (l.3): Letter 81, to the consul Nomus (l.31440, 31496–31499).
- "From the revenues of my see I erected public porticoes; I built two large bridges" (l.5): Letter 81 (l.31507). The eight villages of Marcionists and "many a time was I stoned" follow (l.31510–31515).
- "I have done pastoral duty in eight hundred churches" (l.5): Letter 113, to Leo (l.33165).
- "was not made flesh by mutation, but took flesh" and "not because she gave birth in natural manner to God, but to man united to the God that had fashioned Him" (l.7): Theodoret's Counter-statement against Anathema I (l.4704–4733). I checked the heading at l.4698–4703: the words are Theodoret's, not Cyril's anathema above them and not Jackson's. Correct speaker.
- "were substantially at one" (l.7): Jackson's own judgment (l.2756), and the brief gives it to Jackson.
- "with a pen", "I was five and thirty days' march away", "I await the sentence of your apostolic see" (l.9): Letter 113 (l.33141–33174).
- "the victory you and we together had won" (l.11, card): Leo, Letter 120 (`npnf212_leo-great-gregory-great.xml` l.10295).
- "Theodoret impiously wrote" (l.11, card): sentence of the council of 553 (npnf214 l.23657).
- "Historians substitute books for panels, bright description for pigments" (l.13): Church History I, Prologue (l.5205).
- Card: "because the holy Archbishop Leo had restored the bishopric to him" (the acts as Jackson quotes them, l.3234); "who has brought trouble on all the Churches of the East" (Dioscorus, `council-of-ephesus-449_second-synod-of-ephesus-syriac-acts_perry1881.txt` l.15595, found by letters-only match across OCR breaks); "Against Eutyches the presbyter and Dioscorus bishop of Alexandria" (Gennadius 89, l.43766); "has been generally attributed to Theodoret" (Jackson, l.2729); "some probability that Theodoret survived till 458; none that he lived longer." (Jackson, l.3411); "Cyrrhaus" (Richardson's note, l.43760). All exact.

**Narrative checks**
- Dioscorus's sentence: "has ventured to hold tenets and write in opposition to those Positions… laid down by our very Blessed Father and Bishop Cyril", deposed and excommunicated, and the request that the emperors commit "these Treatises of the impious Theodoret… to the burning of the fire" (Perry l.15581–15633). Faithful.
- Jackson: "Nestorius, patriarch of Constantinople, was bound by ties of close friendship both to Theodoret and to John"; Rome's condemnation "In August, 430"; "asked Theodoret to refute Cyril" (l.2711–2736). Consecration "a.d. 423" at about thirty (l.2606) after Tillemont's 393 (l.2399–2403); Garnier's 386 and Möller's 390 (l.2395–2408). Bertram (1883) and Möller (l.3339–3342). Gennadius's "ten books… until the accession of the elder Leo in whose reign he died" (l.43772–43776). Jackson's "reinstated at Chalcedon in spite of what he had written, and what he had written was anathematized at Constantinople in spite of his reinstatement" (l.3511–3513). Five books and "105 years… ending with the death of… Theodorus and Theodotus" (l.18272–18274). Jackson on the name Eranistes, "a picker up of various scraps of heresy" (note, l.18522–18524). All faithful.
- The card and records are frank that the birth at Antioch rests on Jackson's retelling of the Religious History, which the Library does not hold. The Chalcedon session is held only as Jackson quotes it. Both are correct.

**Findings**
- **M1 MINOR (item 8; and "no statements that have no context").** Brief l.1 opens on the shout "Theodoret must now anathematize Nestorius" and "They wanted him to curse Nestorius by name". The listener is not told who Nestorius is until l.7, "Nestorius, bishop of Constantinople". The card never gives his see: his first mention is in `uncertain` item 1 ("his friendship with Nestorius"), after Leo's quoted "blasphemy of Nestorius" in `legacy.remembered` 1. The Cyril profile in this batch places him at first mention in both texts. Fix: brief l.1 "They wanted him to curse Nestorius, the deposed bishop of Constantinople, by name." and l.7 "Nestorius was his close friend, Jackson says."; card `uncertain` item 1 "…for his friendship with Nestorius of Constantinople…".
- **M2 MINOR (item 1, records; a phrase given to the wrong witness).** The `contested_claim` "Whether Theodoret and Cyril really differed" gives "were substantially at one" to "Blomfield Jackson, and William Bright as Jackson quotes him". The phrase is Jackson's alone (l.2756). Bright, in the quotation Jackson gives, says they "were essentially nearer to each other in belief than at the time they would have admitted" (l.2766–2771). Fix: "Blomfield Jackson: the two 'were substantially at one'. William Bright, as Jackson quotes him: Theodoret 'uses a good deal of language which is prima facie Nestorian', but he and Cyril 'were essentially nearer to each other in belief than at the time they would have admitted' (npnf203 l.2756, 2766–2771)."

---

## Totals (part A)

| Profile | Blocking | Minor |
|---|---|---|
| Socrates of Constantinople | 0 | 0 |
| Mesrop Mashtots (MAJOR) | 0 | 3 (M1–M3) |
| Cyril of Alexandria (MAJOR) | 0 | 4 (M1–M4) |
| Sozomen | 0 | 1 (M1) |
| Theodoret of Cyrrhus (MAJOR) | 0 | 2 (M1–M2) |
| **Part A** | **0** | **10** |

I found no witness swap of the batch 1 kind in part A. Every quotation was confirmed at its place in the vendored file, with its speaker checked. The checks covered Socrates against Zenos's notes and the bracket "not found in the Greek", Sozomen against Hartranft's notes and introduction, Koriun against Langlois's notes and the "[de Mopsueste]" bracket, the council's acts against Jackson's and Percival's framing, Theodoret's Counter-statements against Cyril's anathemas, and Venables against Jackson.

Patterns across part A:
1. **Translator's brackets and witness alignment.** Mesrop M2 gives a bracketed subject to Koriun. Cyril M3 makes Percival the doubter when he leans the other way. Theodoret M2 gives Jackson's phrase to Bright.
2. **A contested founding claim left to the card** while `records.json` carries it (Mesrop M1).
3. **First mentions.** Common names or unexplained names lack a place on the card (Mesrop M3, Cyril M4) or in the opening scene (Theodoret M1).
4. **Small fidelity points.** A dropped "probably" (Sozomen M1), a compressed sequence in the acts (Cyril M1) and a thesis-opening sentence (Cyril M2).


---

## R1 review: era 2 batch 5, part B (Church Family Tree Who profiles)

Reviewer: independent, first sight of these drafts. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; and the failure types of the era 2 batch 1 to batch 4 R1 reviews, above all the witness swap, a modern dating told as resting on an ancient text, and an absence claim the held files contradict. I did not edit the drafts. I made no paid or model-API calls and used no web. Readability and quote search ran on local scripts only.

Profiles: `leo-of-rome` (MAJOR), `koriun` (recorder), `alexander-of-alexandria`, `eusebius-of-nicomedia` (MAJOR), `ossius-of-cordoba`, and the batch `README.md`. The last three come from the supplement scan (`Build/Ministry/Operations/Audits/2026-11-12_who-scan-supplement/`, rows 105, 108 and 104, and `Opus_Check_Notes.md`). Files are in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch5/`. Brief paragraph numbers ("para 3") count the blank-line-separated paragraphs of each `.brief.txt`. Other line numbers point to files under `cic/texts/` unless marked.

Method. Every quotation in the five briefs and cards was searched in its vendored file with a match that strips XML tags and ignores whitespace and quote style (with a letters-only fallback for OCR). Each hit was read in context to see who is speaking: the ancient author, a document or speaker he quotes, an epitomator (Photius), the translator's or editor's introduction, or an endnote. Every factual sentence of each brief and each card item was checked against the passage it rests on. I read the Latin of Prosper (Mommsen) and the French of Langlois's volume (Koriun, Lazar of Pharp, Moses of Khoren, Langlois's introduction and notes) and compared the narrator's telling with them. I compared each `records.json` entry with its brief and card. Readability came from `engine.m1.gates.grade_text`, run from the repo root. Length assumes 162 words a minute.

## Applies to all five

- **Audio = brief.** Each audio script matches its brief exactly once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, placed before the final sentence. No other tag appears, and no tag is in any brief or card (the README only describes them).
- **Readability.** All five pass (FK at most 10, Flesch at least 60). Eusebius (60.0) and Alexander (60.4) sit at the Flesch floor. No narrator sentence runs past 25 words. Leo para 3, "As Leo quotes him, Eutyches had said, …", is 27 words, but most of them are Eutyches's words as Leo quotes them, so this is not a finding (the batch 4 Pelagius ruling).
- **Card order.** All five follow Mark's order. Missing fields are left out (Alexander and Eusebius have no otherNames). keyWorks never goes past three. The `"date": null` in source entries is the schema the earlier batches used, so it is not a finding.
- **Length.** Leo 403 words (2:29) and Eusebius 404 (2:30) are at the major cap. Koriun 328 (2:01), Alexander 321 (1:59) and Ossius 322 (1:59) are within "about 2 minutes". Every `briefLength` matches.
- **Who test (item 14).** Leo and Eusebius each have a body of work and a following. Koriun is a recorder Who, as the README says. Alexander and Ossius have their own letters (and, for Ossius, the Sardican proposals) and a following. The drafts carry no list lines; those belong to the map build and were not checked here.

| Profile | Words | Est. length @162 | FK | Flesch |
|---|---|---|---|---|
| Leo of Rome (MAJOR) | 403 | 2:29 | 6.5 | 72.3 |
| Koriun | 328 | 2:01 | 6.2 | 74.8 |
| Alexander of Alexandria | 321 | 1:59 | 7.7 | 60.4 |
| Eusebius of Nicomedia (MAJOR) | 404 | 2:30 | 7.6 | 60.0 |
| Ossius of Cordoba | 322 | 1:59 | 7.8 | 61.1 |

---

## 1. Leo of Rome (MAJOR)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, minor (M1) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Prosper, Feltoe, Gore, Mommsen named) |
| 6 | Partisan witness named and marked | PASS (Prosper "writes of Leo with reverence"; Leo's "robbers" given as his, and the card says he was not there) |
| 7 | Contested both sides | PASS (Attila: Prosper against Feltoe's rumours; birthplace; 43rd or 47th) |
| 8 | Common names placed | PASS |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:29) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes** (all exact, speaker confirmed)
- "has not abandoned the helm of the Church": Leo, Sermon III.3, "On His Birthday, III: Delivered on the Anniversary of his Elevation" (`npnf212_leo-great-gregory-great.xml` l.13337, 13432).
- "I confess that our Lord was of two natures before the union, but after the union I confess one nature": the Tome, ch. 6, in Bright's English in the acts of Chalcedon (`npnf214_seven-ecumenical-councils.xml` l.19938–19941). Leo is quoting Eutyches, as the brief says. Feltoe's English of the same line reads differently ("had two natures … I confess but one", npnf212 l.5597), so the brief rightly follows the npnf214 text the card lists.
- "whole in what was his, whole in what was ours": the Tome (npnf214 l.19750). "Each nature … keeps what is its own" is a fair telling of "each of the natures retains its proper character" (l.19763).
- "a Latin bishop, ignorant of Greek, defining the faith for Greek-speaking bishops": Gore, quoted by Feltoe (npnf212 l.615–622). "Charles Gore's Life of Leo the Great" is in Feltoe's bibliography (l.1200).
- "not of judges but of robbers": Leo, Letter XCV, "To Pulcheria Augusta" (npnf212 l.8587, 8640).
- "Peter has spoken thus through Leo": acts of Chalcedon, Session II, after the reading of the Tome (npnf214 l.19995–20000). Feltoe's own telling, "Peter has spoken by Leo" (npnf212 l.754), is not used.
- "Christian, acknowledge thy dignity": Sermon XXI, "On the Feast of the Nativity, I" (npnf212 l.14492, 14608).
- Card: "none but the slightest indirect allusion", "no reason, however, to doubt the substantial truth", "aided, it is thought, by rumours of threatened invasion at home" (l.851–861); "can claim the honour with certainty" (note 1, l.408–409); "it is thought" for the acolyte (l.436); "extended over the whole of Christendom as the successor of S. Peter" (l.486); "on which Leo's chief claim to our thanks and praise rests" and "the final and complete definition of the cardinal doctrine of the Incarnation" (l.546–548); "the first great Latin-speaking pope and bishop of Rome" (l.418–419). Prosper's "beatissimus papa Leo" (`prosper_chronica-minora-1-lat_mommsen1892.txt` l.54955) and "per sanctum papam Leonem praedicabatur" (l.54990, the close of entry 1369 on Chalcedon). All exact.

**Narrative checks**
- Attila (Prosper 1367, l.54942–54957): the senate and people chose to seek peace by envoys; Leo "suscepit hoc negotium" with Avienus and Trygetius, "auxilio dei fretus"; "ita summi sacerdotis praesentia rex gavisus est, ut et bello abstinere praeciperet et ultra Danuvium promissa pace discederet". The brief's telling is faithful, and Lake Benacus is rightly kept as Feltoe's (l.859).
- 440 (Prosper 1341, l.54627–54635): "XL amplius diebus Romana ecclesia sine antistite fuit … praesentiam diaconi Leonis expectans, quem tunc inter Aetium et Albinum amicitias redintegrantem Galliae detinebant … XLIII Romanae ecclesiae episcopus ordinatur". Faithful. Feltoe's "Sept. 29" and "47th bishop" (l.476–477) match the card.
- 455 (l.55120–55129): "occurrente sibi extra portas sancto Leone episcopo, cuius supplicatio ita eum deo agente lenivit … ab igni tamen et caede atque suppliciis abstineretur. per quattuordecim igitur dies … omnibus opibus suis Roma vacuata est". Faithful.
- Feltoe on 448 (archimandrite, Flavian, l.555–587), Ephesus 449 (the Tome "was not read at all", Eutyches restored, Flavian deposed, l.636–660), the fourth session adopting the Tome (l.776–777), canon 28 (l.787–811), and death "Late in the year 461 … after a rule of twenty-one years" (l.903–904). Youth: "Of his youth we know nothing" (l.410–411). Faithful.
- records.json matches, with the Attila and birthplace `contested_claim`s in place.

**Findings**
- **M1 MINOR (item 1; a modern dating told as resting on an ancient text).** Brief para 2: "Prosper says that in 440, when Xystus, bishop of Rome, died, …". Prosper gives no year number. His entry stands under the consuls "Valentiniano Aug. V et Anatolio" (l.54624), and "a. 440" is Mommsen's margin. The card says exactly this: "Prosper dates his entries by the consuls of each year. The years 440, 452 and 455 are given by Theodor Mommsen's edition and by Feltoe." The brief contradicts its own card. Fix: "In 440, by Feltoe's date, Xystus, bishop of Rome, died. Prosper says Rome's church waited more than forty days for its deacon Leo." (Feltoe: "Next year (440) … In his absence Sixtus died", npnf212 l.460–473.)

---

## 2. Koriun (recorder)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, minor (M1) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Langlois, Lazar of Pharp, Moses of Khoren, Emine named; the authorship note is given as "a note in … Langlois's edition", not to a person) |
| 6 | Partisan witness named and marked | PASS (the Life marked as "the work of a disciple honouring a saint", with its wonders named) |
| 7 | Contested both sides | PASS (patron: Lazar against Langlois; authorship rests on the note and Lazar) |
| 8 | Common names placed | PASS in the brief; card minor (M2) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:01) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder Who) |

**Quotes** (all exact; `langlois_collection-historiens-armenie-tome2-fra_1869.txt`)
- Card: "Cette histoire a été écrite véridiquement par le célèbre Gorioun": Lazar of Pharp (l.36218–36220), who adds "qui en avait été chargé sur les instantes prières du roi d'Arménie Vramschapouh". "fort élevé": Langlois's introduction (l.2819–2820). Exact.

**Narrative checks**
- The opening scene follows the Life (l.3848–3864): "quelques-[uns de leurs] compagnons, appelés, l'un Léon, l'autre Gorioun, vinrent … dans la ville de Constantinople. Ils se joignirent à Eznig, comme à un frère de la même famille, avec qui ils avaient été élevés … s'occupèrent d'achever leurs travaux spirituels … copies authentiques des Saintes-Écritures, des écrits … des pères de l'Église, et des canons des saints conciles de Nicée et d'Éphèse". "Eznik of Goghp" is note 3 (l.3822). The note "(2) L'auteur de la Biographie de Mesrob" (l.3896) is the note the brief names. Faithful.
- The self-description (l.4336–4378): "des hommes que nous avons nous-même vus de nos yeux … Nous fûmes les témoins attentifs de leurs prédications … et les serviteurs de ces saints docteurs … en laissant de côté beaucoup d'actes de leur vertu … en ne racontant que les choses principales, dignes d'être connues". The close (l.4392–4398): "servir de modèle d'exhortation à leurs enfants spirituels, et à ceux qui veulent enseigner la vérité à leur nation". The demons put to flight (l.3507–3511) and the luminous cross over the house (l.4252–4256). All faithful.
- Langlois (l.2741–2768): sent to Byzantium with Ghévont, then Jerusalem, made "évêque des Géorgiens" by Sahag, "Il mourut, à ce que l'on croit, en Géorgie; mais on ne saurait dire rien de positif à cet égard, car ses contemporains ne donnent aucun détail"; the Life written "à la prière du patriarche Joseph", the "source principale" for Armenian literary history "depuis la fin du quatrième siècle jusque dans le courant du cinquième". The copyists' cuts (l.2822–2832), Agathangelos "loin d'être tranchée" (l.2843–2851), and the Mekhitarist edition of 1854 behind Emine's French (l.2860–2863). Faithful.
- Lazar sends readers to the Life to learn "à quelle époque, en quel endroit et par le moyen de qui les lettres furent retrouvées" (l.36214–36217). Faithful.

**Findings**
- **M1 MINOR (item 1; a source made to say less than it does).** Card `uncertain` item 4: "Moses of Khoren also names Leon and Koriun among the pupils who went to Byzantium, and says they went of their own accord." The records claim "Went to Byzantium with Leon of his own accord" says the same. Moses gives a motive the card drops, and it is the one unfavourable judgment on Koriun in the held sources: "Mais, poussés par l'envie, leurs compagnons et leurs condisciples, appelés Léon et Gorioun, se rendirent spontanément à Byzance" (l.24626–24661, across the page break). Fix (card and records): "Moses of Khoren also names Leon and Koriun among the pupils who went to Byzantium. He says they went of their own accord, 'poussés par l'envie', moved by envy of those already there."
- **M2 MINOR (item 8 and "no statements with no context", card).** Several card first mentions carry no identifier or context. In `knownFor`, "Sahak" is bare; Sahak is a common Armenian name, and the brief rightly has "Sahak, patriarch of the Armenians". In `place` and `legacy`, "Langlois" has no first name or role. In `uncertain` item 3, "Ghevont" means nothing to a listener, though the edition's own note says he is the Leon of the Life: "Léon ou Ghévont, prêtre de Yanant" (l.3887, as the OCR reads). In `legacy.traces` item 3, "the work of Agathangelos" has no context. Fixes: `knownFor` "…pupil of Mesrop Mashtots and of Sahak, patriarch of the Armenians, whose…"; `place` "Georgia, by Victor Langlois's account"; `uncertain` item 3 "sent to Byzantium with Ghevont, the Leon of the Life by a note in the edition, …"; `legacy.traces` item 3 "…may have put Agathangelos's History of Tiridates into Armenian" (Langlois: "l'Histoire du secrétaire de Tiridate" and "l'ouvrage d'Agathange", l.2835–2846).

---

## 3. Alexander of Alexandria

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, minor (M2) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Sozomen, Hartranft, Robertson, Newman, Theodoret, Jackson, Zenos named) |
| 6 | Partisan witness named and marked | FAIL, minor (M1) |
| 7 | Contested both sides | PASS (three accounts of the start; authorship of the circular letter; year of death) |
| 8 | Common names placed | PASS in the brief; card minor (M3) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (1:59) |
| 11 | grade_text | PASS (Flesch 60.4, at the floor) |
| 12 | Card order, caveat repeated | FAIL, minor (M1: the card's first caveat is not in the brief) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes** (all exact, speaker confirmed)
- "O Athanasius, thou thinkest to escape, but thou wilt not escape": Sozomen II.17 (`npnf202_socrates-sozomen-ecclesiastical-histories.xml` l.29352–29354). It sits inside Sozomen's quotation of "Apolinarius, the Syrian" (l.29335), which runs from "In all these matters" to "called to the conflict", followed by "Such is the account given by Apolinarius". So the brief is right: Sozomen tells it, from that writer. "This quotation is first made by Soz., and is found nowhere else" is Hartranft's endnote (l.29336), correctly given to him on the card. The chapter's note "About five months after the council of Nicæa, according to a statement of Athan." (l.29326) is also Hartranft's and is not used.
- "with perhaps too philosophical minuteness": Socrates I.5 (l.2073). Socrates's own words.
- "A doubtful and unsupported assertion": Hartranft's endnote to Sozomen I.15 (l.27588). Correctly his.
- "as one of the retinue of Alexander" and "that admirable bishop, who had successfully withstood the blasphemies of Arius": Theodoret I.25 (`npnf203_theodoret-jerome-gennadius-rufinus.xml` l.7997–8005). Theodoret's own narrative.
- Card: "one of the earliest documents of the Arian controversy": Robertson's introduction to the Encyclical (`npnf204_athanasius-select-works-letters.xml` l.18940–18942). "because he afterwards returned to the Homoousian faith": Photius, Epitome II.7 (`philostorgius_ecclesiastical-history_walford1855.txt` l.124). Note 26, "Valesius observes that the falsehood of this statement…" (l.568). Exact.

**Narrative checks**
- Theodoret I.1 (npnf203 l.5279–5289): Arius "fell a prey to the assaults of jealousy, when he saw that the helm of the high priesthood was committed to Alexander". Jackson's note "Patriarch, a.d. 312–326" (l.5280). Faithful.
- Sozomen I.15 (npnf202 l.27580–27590): Alexander "sat down as a judge … and led both sides into a discussion … seemed to incline first to one party and then to the other". Faithful.
- Circular letter, Socrates I.6 (l.2155–2212): "pay no attention to anything that Eusebius should write"; "with the bishops of Egypt and Libya, being assembled together to the number of nearly a hundred, have anathematized Arius". Robertson on Newman's case, "of great weight", Kölling's counter-arguments "trivial" (npnf204 l.18916–18935). Faithful.
- Letter to Alexander of Constantinople, Theodoret I.3: "the Son of God was not created out of the non-existent" and "the Father and the Son are inseparable" (npnf203 l.5506–5513). Faithful.
- Death: Theodoret "five months after the council of Nicæa" (l.7998). Zenos: Socrates and Sozomen "are both mistaken in putting the death of Alexander … after the return of Eusebius and Theognis"; Theodoret's "a few months after", "hence in 325" (npnf202 l.3994–3999). The Festal Index "departed this life on xxii Pharmuthi", with Robertson's note "April 17" (npnf204 l.64077–64079), and his reading of Athanasius's "five months" (l.24797–24804). Faithful.

**Findings**
- **M1 MINOR (items 6 and 12).** The brief never says that its witnesses are Alexander's own side. Theodoret's charge that Arius acted from jealousy (para 3) is a pro-Nicene historian's reading of an opponent's motive, and it is told beside the other two with no mark. The card's first `uncertain` item does carry the caveat: "Most of his story comes through his own side: his letters and the church historians who held to Nicaea." The pattern asks that item to repeat the brief's own caveat, and here the brief has none. This is the batch 2 Tyconius pattern, applied to a witness partisan for the subject. Fix, brief para 3, first sentence: "The historians, who all held to Nicaea, tell three stories of how the two fell out." That adds four words. Trim elsewhere to keep about 2:00, for example "who revised Sozomen's English" (the card carries it).
- **M2 MINOR (item 1; a loose quantifier the files contradict).** Card `uncertain` item 1: "The one account from Arius's side, Philostorgius, survives only in a hostile summary by Photius." A held account from Arius's side is Arius's own letter to Eusebius of Nicomedia, in Theodoret I.4, which opens "Arius, unjustly persecuted by Alexander the Pope" and says "We are persecuted, because we say that the Son has a beginning…" (npnf203 l.6002–6064). The Eusebius card cites that same chapter. Fix: "Most of his story comes through his own side: his letters and the church historians who held to Nicaea. From Arius's side, the held sources are Arius's own letter to Eusebius of Nicomedia, kept by Theodoret, and Philostorgius, who survives only in a hostile summary by Photius."
- **M3 MINOR (item 8 and "no statements with no context", card).** Card `uncertain` item 3: "He names Kölling as arguing against it." Kölling has no first name or context. Robertson's bibliography gives him as the author of a "Geschichte der Arianischen Häresie (1st vol., 1874, 2nd, 1883)" (npnf204 l.1352–1354). Fix: "He names Kölling, author of a German history of the Arian heresy, as arguing against it."

---

## 4. Eusebius of Nicomedia (MAJOR)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Philostorgius, Photius, Socrates, Sozomen, Duchesne, Jackson, Zenos, Walford, Robertson named) |
| 6 | Partisan witness named and marked | PASS (Philostorgius "on Eusebius's side" through "a hostile summary by Photius"; "Most other accounts come from men who fought him", para 2) |
| 7 | Contested both sides | PASS (signing at Nicaea; reason for exile; Ulfila's consecrator; the baptism) |
| 8 | Common names placed | FAIL, minor (M1 brief context; M2 card) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:30) |
| 11 | grade_text | PASS (Flesch 60.0, at the floor) |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes** (all exact, speaker confirmed)
- "You subscribed, Eusebius, in order to escape being sent into banishment": Photius, Epitome I.10, reporting Philostorgius's Secundus (Walford l.108). "within three months after the conclusion of the synod" is the same paragraph. The brief has said the book lives only in Photius's summary.
- "my fellow-Lucianist": Arius's letter, Theodoret I.4 (npnf203 l.6064). Jackson's note "Lucianus the priest of Antioch" supplies "of Antioch".
- "pay no attention to anything that Eusebius should write to you": Alexander's circular letter, Socrates I.6 (npnf202 l.2167–2168).
- "There is, indeed, nothing which is of His substance": Eusebius's letter to Paulinus, Theodoret I.5 (npnf203 l.6192). "was not made out of His substance" (l.6159–6160) backs the paraphrase, and the request to write "to my lord Alexander … bringing him over" (l.6201–6203) backs "win Alexander over".
- "the co-operator in the cruelty of the tyrants": Constantine to the Nicomedians, Theodoret I.19 (l.7501). The seizure of men from Alexandria and the banishment with Theognis are the same letter (l.7546–7556).
- "we subscribed the declaration of faith; we did not subscribe the anathematizing": the plea, Socrates I.14 (npnf202 l.3956).
- "by Eusebius and the other prelates": Photius, Epitome II.5 (Walford l.120). Card adds "that were with him", also exact.
- "Eusebius and his fellows have always been the supporters and associates of the impious heresy": Athanasius, Encyclical Letter (npnf204 l.21126, 21242).
- Card: "does not give the correct reason" is Zenos's note (npnf202 l.3934). "had formerly co-operated with Eusebius" is Socrates II.12 (l.6180). "At the hand of Eusebius of Nicomedia" is Jackson's endnote 443 (npnf203 l.8288–8289), as the scan's Opus check found, and the brief and card both give it to Jackson. "personal entourage, of one man, a master of intrigue" is Robertson (npnf204 l.4128). Exact.

**Narrative checks**
- Socrates I.8: "Five only would not receive it … Eusebius bishop of Nicomedia…" and the edict that exiled them (npnf202 l.2950–2966). Walford's note 14 holds Socrates mistaken (Walford l.546). Sozomen I.15: "a man of considerable learning and held in high repute at the palace" (npnf202 l.27625–27626). Socrates II.7: Constantius "ejects Paul … and sending for Eusebius of Nicomedia, invests him" (l.5879). Socrates II.8: the synod of Antioch "in the consulate of Marcellus and Probinus … the fifth year after the death of Constantine", Zenos "341 a.d." (l.5933–5934). Zenos's "328 a.d." for the recall (l.3934). Duchesne: "Eusèbe de Nicomédie le vit … le consacra évêque pour sa nation" (`duchesne_histoire-ancienne-de-leglise-tome2-fra_3e-ed1907.txt` l.20994–20995). Photius II.14, the disciples of Lucian (Walford l.138); II.16, the will (l.142); note 31, "This would seem to be a mistake … Theodoret … falls into the same error" (l.578). All faithful.
- records.json matches. Both `contested_claim`s are in place, and Constantine's letter and Athanasius are tagged hostile.

**Findings**
- **M1 MINOR (item 8 and "no statements with no context").** Brief para 3: "Sozomen says he was learned and stood high at the palace." This is Sozomen's only mention in the brief, with no context, while Philostorgius, Duchesne and Jackson each get one. The Alexander brief in this batch has the form: "Sozomen, a church historian of the next century". Fix: "Sozomen, a church historian of the next century, says he was learned and stood high at the palace."
- **M2 MINOR (item 8, card).** Card first mentions without the place the pattern asks for. In `dates`, "Zenos's note to Socrates" and "by Socrates" are the card's first two mentions of Socrates, a common name and the pattern's own example. In `keyWorks`, "kept by Theodoret" is the card's first Theodoret. In `uncertain` item 4, "after deposing Paul" names a common name bare. Fixes: `dates` "…by A. C. Zenos's note to Socrates of Constantinople…"; `keyWorks` item 1 "…kept by Theodoret of Cyrrhus"; `uncertain` item 4 "…after deposing Paul, bishop of Constantinople" (Socrates II.7, npnf202 l.5879).

---

## 5. Ossius of Cordoba

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL (B1; M2) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL, minor (M3) |
| 5 | No role for a witness | PASS (Athanasius, Socrates, Theodoret, Sozomen, Percival named; the presidency note given as "a note in Robertson's edition") |
| 6 | Partisan witness named and marked | PASS (Athanasius: "his account takes a side", para 2) |
| 7 | Contested both sides | FAIL, minor (M1 hedge dropped; M2 one side's beating given only to the other); PASS on the presidency at Nicaea |
| 8 | Common names placed | PASS |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (1:59) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | FAIL (B1: the card's absence claim) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes** (all exact, speaker confirmed)
- "I was a Confessor at the first, when a persecution arose in the time of your grandfather Maximian", "remember that you are a mortal man", "Intrude not yourself into Ecclesiastical matters": Ossius's letter, History of the Arians 44 (npnf204 l.39254–39306). The letter warns Constantius against "Ursacius, Valens and their fellows" (l.39258–39259), which backs "the bishops his letter had warned against".
- "more than sixty years": Athanasius, History of the Arians 42 (l.39203). "now a hundred years old", "detained him a whole year in Sirmium", "broken by suffering … to hold communion with Valens, Ursacius … though he would not subscribe against Athanasius", and "he bore witness to the force which had been used towards him, and anathematized the Arian heresy": History of the Arians 45 (l.39388–39410).
- "in which he did not take the lead": Defence of his Flight 5 (l.36606). The bracket after it is the editor's.
- "greatly loved this man": Socrates I.7 (npnf202 l.2461). "most highly distinguished" and "the first place": Theodoret, in this edition II.12 (npnf203 l.9650–9651), in his own narrative.
- Card: "the Abraham-like old man, Hosius, truly so called" (npnf204 l.39356); "although the lists are bad witnesses" (Robertson, l.2159); "Hosius, the confessor" and "the friend of Paulinus and Eustathius" (Sozomen III.11, npnf202 l.31476–31478); "Bishop Hosius said" (Canons of Sardica, npnf214 l.30600 and after). Exact.

**Narrative checks**
- Canon I of Sardica: "Hosius, bishop of the city of Corduba, said: … Let no bishop be allowed to remove from a small city to a different one" (npnf214 l.30585–30590). Percival: "it is possible that … Hosius of Cordova may have done so … yet there is no evidence that anything of the kind ever took place" (l.790–793). The Latin lists open with "Osius episcopus ciuitatis Cordubensis" (`patrum-nicaenorum-nomina_subscription-lists-lat_gelzer-hilgenfeld-cuntz1898.txt` l.4792–4793, 4820). The note "Hosius presided at Nicæa" (npnf204 l.20432). Socrates II.31: "stripes and tortures were inflicted on the old man. Wherefore he was constrained by force to … subscribe" (npnf202 l.8202–8213). Zenos on the three councils of Sirmium (l.7900–7905). Faithful.
- Robertson's notes place the lapse in 357 (npnf204 l.36364–36365, and the bracket "357 a.d." at l.36615). Faithful.

**Findings**
- **B1 BLOCKING (items 1 and 12; an absence claim the held files contradict).** Card `dates` ends "no source used here gives his death". Card `uncertain` item 4 says "No other source used here tells his death". The records `absent_details` says "Birth, family, death year and place: No source used here gives them". Henry Percival's volume, which the card lists under "Their own words" for the Canons of Sardica, reports three views on when he died. In the introduction to the Synod of Gangra: "Hefele denies this and says: 'At the time of the Synod of Gangra Hosius was without doubt dead.' But such has not been the opinion of the learned, and Cave is of opinion that Hosius's episcopate covered seventy years ending with 361, and (resting on the same opinion) Pagi thinks Hosius may have attended the Synod in 358 on his way back to Spain" (npnf214 l.8435–8448). This is the batch 2 Ulfila and Cyril pattern, where a card said no held source gave what a held file does give. Fix, card `dates`: "…which Archibald Robertson's notes to Athanasius place in 357. No ancient source used here gives the year of his death. Henry Percival reports Cave's view that his episcopate ended in 361, and Hefele's that he was dead before the Synod of Gangra." Card `uncertain` item 4: "Athanasius says that before his death he condemned the Arian heresy and named the force used on him. No other ancient source used here tells his death. Percival reports that Hefele thought him dead before the Synod of Gangra, while Cave ends his episcopate in 361 and Pagi thinks he may have been at Gangra in 358." In records.json, change the absent detail to "Birth, family, and an ancient witness to his death" and add a `contested_claim`, "When he died", with those three sides from npnf214 l.8435–8448.
- **M1 MINOR (items 1 and 7; a hedge dropped).** Card `uncertain` item 3: "Socrates and Sozomen say he was beaten until he signed a creed there." Sozomen hedges: "being extremely old, he sunk, as it is reported, beneath the blows that were inflicted on him, and yielded his consent and signature" (npnf202 l.32899–32901). He repeats the hedge in IV.12, "consented, though by compulsion, at Sirmium, as it is reported" (l.33395–33405). The records claim keeps "'as it is reported'", but the card drops it. Fix: "Socrates says he was beaten until he signed a creed there; Sozomen says so too, 'as it is reported'."
- **M2 MINOR (items 1 and 7; one side's evidence given only to the other).** Card `uncertain` item 3 opens "His lapse is told two ways" and gives the beating to Socrates and Sozomen. The brief has the same split: Athanasius's year at Sirmium against "In Socrates's telling, he was beaten and tortured". But Athanasius, in the Defence of his Flight 5, which the card lists, also tells of blows: "if afterwards, upon the repeated stripes above measure that were inflicted upon him, and the conspiracies that were formed against his kinsfolk, he yielded to them for a time" (npnf204 l.36613–36616). The two accounts differ on what he yielded, not on whether he was beaten. Fix for the card: "His lapse is told two ways. Athanasius, in the History of the Arians, says that after a year's confinement at Sirmium he shared communion with Valens and Ursacius but would not sign against Athanasius. In his Defence of his Flight he speaks of 'repeated stripes above measure', after which 'he yielded to them for a time'. Socrates says he was beaten until he signed a creed there; Sozomen says so too, 'as it is reported'. A. C. Zenos notes…". The brief may stand as it is, since each sentence is true of its witness. If a brief change is wanted, para 5 could read "Athanasius says Constantius held him for a whole year at Sirmium, and elsewhere speaks of repeated blows."
- **M3 MINOR (item 4, "no statements with no context"; item 8).** Brief para 4: "At Sardica, Theodoret says, he held 'the first place.'" The brief never says Sardica was a council, so its "canons" in the next sentence come with no context. The same paragraph's "Sozomen says" is his only mention, with no context. Fix: "At the council of Sardica, about 343 by Percival's date, Theodoret says he held 'the first place.'" (npnf214 l.930, "Sardica (343 circa)"). And: "The eastern bishops met apart and deposed him, says Sozomen, a church historian of the next century." Trim elsewhere to keep about 2:00, for example "who edited the council records" can go to the card.

---

## 6. Batch README.md

- **README-M1 MINOR.** The README gives Ossius as "last attested about 357, by Athanasius's account of his exile at 'a hundred years old'". Athanasius gives no year. The 357 is from Robertson's notes (npnf204 l.36364–36365, 36615), as the card says. Also, the "hundred years old" passage is not an exile: Athanasius says Constantius, "instead of banishing him, detained him a whole year in Sirmium" (l.39390–39391). The README is internal, but it is where a later reviewer looks first, and it repeats the batch 4 README fault of a modern year given to the wrong witness. Fix: "Ossius of Cordoba (last attested about 357, by Archibald Robertson's notes to Athanasius's account of his detention at Sirmium at 'a hundred years old')".
- The rest of the README is correct for part B. It names the ids, gives the major marks as confirmed (Leo and Eusebius major, Alexander, Ossius and Koriun not), names Koriun as a recorder Who in the Auxentius and Palladius form, and gives the card and records schema, which matches the five cards. Alexander's "326, an editor's note" matches Jackson's note, and Eusebius's "about 341, a note in Zenos's edition of Socrates" matches l.5933.

---

## Totals, part B

| Profile | Blocking | Minor |
|---|---|---|
| Leo of Rome | 0 | 1 (M1) |
| Koriun | 0 | 2 (M1–M2) |
| Alexander of Alexandria | 0 | 3 (M1–M3) |
| Eusebius of Nicomedia | 0 | 2 (M1–M2) |
| Ossius of Cordoba | 1 (B1) | 3 (M1–M3) |
| Batch README.md | 0 | 1 (README-M1) |
| **Part B** | **1** | **12** |

No witness swap of the batch 1 kind was found in part B. Every quotation was confirmed at its place in the vendored file, with its speaker: Eutyches as Leo quotes him in Bright's Tome against Feltoe's differing English; Apolinarius inside Sozomen against Hartranft's notes; Photius's epitome against Philostorgius; Jackson's endnote against Theodoret's text on the baptism; Ossius's letter against Athanasius's narrative; and the Langlois notes against Koriun's Life. Patterns across part B:
1. **An absence claim contradicted by a held file** (Ossius B1). Percival's volume, already cited on the card, reports Hefele, Cave and Pagi on his death.
2. **A modern year given to an ancient witness** (Leo M1, where the brief contradicts its own card; README-M1).
3. **A source made to say less than it does**: Moses's "envy" (Koriun M1), Sozomen's "as it is reported" (Ossius M1), Athanasius's own "stripes" (Ossius M2), and Arius's own letter overlooked (Alexander M2).
4. **First mentions without a place or context**, mostly on cards (Koriun M2, Alexander M3, Eusebius M1–M2, Ossius M3).
