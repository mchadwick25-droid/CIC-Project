# R1 review: ten Who profiles, era 3 batch 2

Three independent Opus reviewers, each at first sight of its drafts, reviewed the batch in three parts: part A (Joshua the Stylite, John Rufus, Zachariah Rhetor, Severus of Antioch), part B (Brigid of Kildare, Caesaria of Arles the Elder, Caesarius of Arles) and part C (Julian, missionary to the Nobadae, Ferrandus of Carthage, Benedict of Nursia, and the README). Totals: 5 blocking and 36 minor (part A 1 and 16, part B 2 and 11, part C 2 and 9).

## Part A

Reviewer: independent, first sight of these drafts (branch `who-profiles-era3-batch2`). Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; Mark's length rulings as the batch 1 review applies them (majors capped at 2:30, about 405 words, a cap and not a target; non-majors 1 to 2 minutes, at most about 324 words). I hunted hardest for the recurring faults of earlier batches: witness swaps, a modern year told as an ancient writer's, a contested point or an identification told as settled, absence claims a held file contradicts, two people of one name merged, common names without a place, and AI tells. I did not edit the drafts. I made no paid or model-API calls and used no web. Readability and quote search ran on local scripts only.

Profiles: `joshua-the-stylite`, `john-rufus`, `zachariah-rhetor` and `severus-of-antioch` (major), with their cards, audio scripts and entries in `records.json`. Files are in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch2/`. Joshua and Zachariah are Whos as recorders. Brief line numbers refer to the `.brief.txt` files, where each paragraph is one line and blank lines count (paragraphs sit on l.1, 3, 5, 7, 9, 11, 13). Other line numbers point to files under `cic/texts/`.

Method. I searched every quotation in the four briefs and cards in the vendored file the card or records cite, with a script that collapses whitespace, normalises quote marks, folds accents and lets letters be split by OCR spacing. For the OCR files (Wright's Joshua, Nau's Plerophories, Kugener's Lives of Severus, Raabe's Peter the Iberian, Hamilton and Brooks's Zachariah, Brooks's Severus letters) I read each passage by line number. I read each hit in context to see who is speaking: the ancient author, a document he quotes, a later compiler, a translator's preface, a footnote, or a bracket the translator supplied. I checked every factual sentence of each brief against its passage and searched the Library before accepting each absence claim or each attribution a modern editor might since have revised. I compared each `records.json` entry with its brief and card. Readability came from `engine.m1.gates.grade_text`, run from the repo root. Length assumes 162 words a minute. Every suggested brief fix below was applied to a scratch copy and re-scored; the post-fix word count and scores are given with each profile.

### Applies to all four

- **Audio = brief.** Each audio script matches its brief exactly once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, before the closing paragraph (Joshua, John Rufus, Zachariah) or the closing sentence (Severus). No tag appears in any brief or card. When a brief fix below changes the closing line, the audio script follows it.
- **Readability.** All four pass (FK at most 10, Flesch at least 60). Severus sits nearest the floor (Flesch 62.1). Narrator sentences past 25 words: Joshua l.3 (32 words; M5) and Severus l.3 (29; M16). The other long ones are mostly quotation.
- **Length.** Severus runs 404 words (2:30), at the cap. Zachariah runs 323 (2:00). Joshua (329, 2:02) and John Rufus (333, 2:03) run a little past the non-major ceiling (M8 for John Rufus; the Joshua fixes bring it back). Every `briefLength` matches.
- **Card order.** All four follow Mark's order. Missing fields are left out. keyWorks never goes past three. Each `uncertain` list opens with the brief's main caveat. The `"date": null` in source entries is the schema the earlier batches used.
- **Who test (item 14).** Joshua and Zachariah are recorders whose works are main sources for their years (Wright; Brooks, "Our knowledge of the early life of Severus is mainly drawn from the biography"). John Rufus has the Plerophories in his own words. Severus has his letters and a following. The drafts carry no list lines; those belong to the map build and were not checked here.

| Profile | Words | Est. length @162 | FK | Flesch |
|---|---|---|---|---|
| Joshua the Stylite | 329 | 2:02 | 6.4 | 77.0 |
| John Rufus | 333 | 2:03 | 8.1 | 65.4 |
| Zachariah Rhetor | 323 | 2:00 | 7.9 | 63.5 |
| Severus of Antioch (major) | 404 | 2:30 | 7.9 | 62.1 |

---

### 1. Joshua the Stylite

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, blocking (B1); minor (M2, M3, M4) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (M5) |
| 5 | No role for a witness | PASS (Wright, Noeldeke, Elisha, Sergius named) |
| 6 | Partisan witness named and marked | PASS (no partisan witness used) |
| 7 | Contested both sides | FAIL, blocking (B1) |
| 8 | Common names placed | FAIL, minor (M1) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:02; the fixes bring it to 2:00) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes and close tellings** (`joshua-the-stylite_chronicle_wright1882.txt`)
- The famine (l.1): ch. XLI, "The year 812 (A. D. 500—1)… They were sleeping in the porticoes and streets, and wailing by night and day from the pangs of hunger; and their bodies wasted away… and they began to die in the porticoes and in the streets" (l.2013–2027). The year 812 is Joshua's; "A. D. 500—1" is Wright's bracket, and the brief gives it to Wright. Faithful. "The poor" is the brief's word for "those who were in the city"; the passage is about the starving, so it holds.
- Sergius (l.3): ch. I, "Sergius, priest and abbot, in which thou hast bidden me write for thee, by way of record… when the locusts came… earthquake and famine and pestilence, and (about) the war between the Greeks and the Persians" (l.424–430). Faithful, but see M4 on "Greeks".
- The copyist's note (l.5): "the priest Mar Yêshûa (Joshua) the stylite, from the convent of Züknin, who wrote this Chronicle of the evil times that are past" (l.388–391). Exact. The note follows "Pray for the wretched Elisha, from the convent of Züknin (near Amid), who wrote this leaf" (l.357–358); "(near Amid)" is Wright's bracket. Wright's footnote puts the leaf "in the handwriting of Elisha of Züknin" (l.370–371). "Of Joshua we know little more than what he has himself thought fit to tell us" (l.335–336). Faithful.
- Dates (l.7): ch. C, "On the 28th of the month of the latter Teshri (November A.D. 506)" (l.4361–4362); the year is Wright's bracket, and the brief says so. Wright's preface: "The last date which occurs in it is 28th November A.D. 506… I have thought myself justifed in assigning the composition of the work to that winter and the earlier part of the following year, which is also Noeldeke's opinion" (l.337–344). See M2.
- "I am a plain man in speech… testify to be true" (l.9): ch. IV, l.596–598, after "But"; exact. "these chastisements… sent upon us for our sins" (l.605–608). Faithful.
- "if I remain alive" (l.13): ch. CI, l.4405–4406; "offer up prayer constantly on behalf of me" (l.4401–4402). Exact.
- Card: "it is generally acknowledged to be one of the most valuable authorities for the period with which it deals" (l.172–173), the Assemani and Martin history (l.170–177), Martin's title "écrite vers l'an 515" (l.197–198), the single Vatican manuscript (l.292–300). Exact. "Josue Stylites" is Assemani's running head (`assemani_…tomus1…1719.txt` l.58666, 58999). Card `uncertain` 4: Wright's two notes say "perhaps Dionysius" (l.364–365) and "probably from the pen of Dionysius" (l.4423–4424); "probably" stands.

**Findings**
- **B1 BLOCKING (items 1, 7; a superseded attribution told as settled, which held files contradict).** Brief l.11: "It survived because a later historian, Dionysius of Tell-Mahre, copied it into his own larger work." Wright says so in 1882: "We owe the preservation… to the care of a later historian, Dionysius of Tell-Mahré… patriarch of the Jacobites (ob. … A.D. 845), who incorporated it with his own larger work… The solitary manuscript… is preserved in the Vatican Library" (l.292–297), cited as Vatican "no. CLXII" (l.305–306). Two held scholars name that same compiler otherwise. Nau, in the Didascalie of Jacob in the same PO 8 volume the batch cites for John Rufus, prints an extract from "Pseudo-Denys, Vatican, ms. syr. 162" and says "le Pseudo-Denys écrivait en l'année 1086 des Grecs (775 de notre ère)" (`po08_john-rufus-plerophories-and-others-fra_1912.txt` l.48221–48226; also "le pseudo-Denys… avant l'année 773, dans sa compilation", l.438–439). Brooks calls him "the so-called Dionysius" (`john-ephesus_lives-eastern-saints-po17_brooks1923.txt` l.714). Chabot, introducing Michael the Syrian, separates "la chronique authentique de Denys de Tell-Mahré", which "est perdu, à l'exception d'un seul chapitre" (`michael-the-syrian_chronique-tome1-livres-i-vii-fra_chabot1899.txt` l.63096–63099). A writer of 775 cannot be the patriarch who died in 845. The narrator tells Wright's attribution as fact. The card repeats it, attributed to Wright but with no word that it was given up: `legacy.traces` 1 ("Dionysius of Tell-Mahre, a later patriarch and historian, copied it") and `uncertain` 4 ("probably by Dionysius of Tell-Mahre"). The records claim "Preserved by Dionysius of Tell-Mahré" is tagged Widely Accepted.
  - Fix, brief l.11 (with M3): "Wright says it is generally counted among the most valuable sources for its time. It survived inside a later Syriac chronicle, whose compiler Wright took for the patriarch Dionysius of Tell-Mahre. François Nau, a later French scholar, calls him the Pseudo-Dionysius, writing in 775."
  - Card `legacy.traces` 1: "The Chronicle survives inside a later Syriac chronicle, held in a single Vatican manuscript. Wright took its compiler for the patriarch Dionysius of Tell-Mahre; François Nau calls him the Pseudo-Dionysius, writing in 775, and E. W. Brooks 'the so-called Dionysius'." Card `uncertain` 4: "…a later addition, probably by the compiler Wright took for Dionysius of Tell-Mahre." Add to `uncertain`: "Who copied the Chronicle: Wright names Dionysius of Tell-Mahre, who died in 845; Nau dates the compiler to 775 and calls him the Pseudo-Dionysius." Add Nau (po08, Didascalie of Jacob) and Brooks (PO 17) to `sources.about`.
  - Records: the claim becomes Wright's, tagged Contested, with a `contested_claim` ("Who compiled the chronicle that preserves Joshua": Wright l.292–297 against Nau po08 l.48221–48226, Brooks PO 17 l.714, Chabot l.63096–63099).
- **M1 MINOR (item 8).** Brief l.3, first mention: "He wrote it for Sergius, a priest and abbot". Sergius is a common name, and Wright gives the place: "Sergius, the abbot of a convent in the district of Edessa" (l.337–338). The card's first mention (`keyWorks` 1, "Sergius, priest and abbot") has the same gap. Fix, brief l.3: "He wrote it for Sergius, a priest and abbot near Edessa." Card: "written for Sergius, priest and abbot of a convent near Edessa, …".
- **M2 MINOR (item 1).** Brief l.7: "places the writing in that winter and the next spring." Card `dates`: "that winter and the next spring". Wright says "that winter and the earlier part of the following year" (l.342); "spring" narrows it. Fix, brief: "He and the German scholar Theodor Noeldeke place the writing in the months after." Card: "that winter and the early part of the next year".
- **M3 MINOR (item 1).** Brief l.11: "Wright counts the Chronicle among the most valuable sources for its time." Wright reports a general judgment: "it is generally acknowledged to be" (l.172). The card keeps his words. Fix: "Wright says it is generally counted among the most valuable sources for its time." (in the B1 fix).
- **M4 MINOR (items 1, 4).** Brief l.3: "the war between the Greeks and the Persians." "Greeks" is Wright's rendering; his note says the Syriac word is "literally, the Romans", used for the Byzantine Greeks (l.448–450). A listener hears Greece. Fix: "the war between the Romans and the Persians."
- **M5 MINOR (item 4).** Brief l.3: one narrator sentence of 32 words ("He wrote it for Sergius… and the Persians."). Fix (with M1, M4): "He wrote it for Sergius, a priest and abbot near Edessa. Sergius had asked him for a record of the locusts, the famine and plague, and the war between the Romans and the Persians."
- Length with B1 and M1 to M5: the fixes add words. Suggested cuts: delete l.5's opening "Wright says we know little more of Joshua than he chose to tell." (card `uncertain` 1 holds it), l.9's "Joshua says plainly why he wrote.", and "near Amid" after Zuknin in l.5 (the card's `place` keeps it). Scored: 323 words (2:00), FK 6.6, Flesch 74.9.

---

### 2. John Rufus

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | minor (M6); records minor (M9) |
| 2 | Quotes verbatim | PASS (the card's French quotations, checked) |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Nau, Raabe, Zachariah named) |
| 6 | Partisan witness named and marked | PASS ("a book of testimonies against Chalcedon"; card `uncertain` 4) |
| 7 | Contested both sides | minor (M6) |
| 8 | Common names placed | FAIL, minor (M7) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | FAIL, minor (M8) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes and close tellings** (`po08_john-rufus-plerophories-and-others-fra_1912.txt` unless noted)
- The scene (l.1): ch. XVI, "Quand je demeurais à Jérusalem, je suivis un jour la route qui conduit de Siloe, par la vallée… l'un des notables de la ville… je vis au pied de la montagne… un grand monastère devenu vieux et tombant en ruines" (l.2068–2073); "avec un visage souriant… C'était le monastère de Juvénal… quand le concile de Chalcédoine eut lieu, (ce monastère)… devint désert" (l.2124–2139); "Juvénal a été le compagnon de Judas, comme l'a dit de lui le bienheureux Dioscore" (l.2142–2143). Faithful; the speaker is John in the first person.
- Nau's life (l.3, 5, 7): "Il se nommait Jean, était Arabe du Sud de la Palestine, sans doute d'Ascalon ; il a étudié le droit à Beyrouth… ordonné prêtre à Antioche (476 à 478) par le patriarche Pierre le Foulon dont il avait été syncelle. Il a quitté cette ville quand le patriarche Pierre en a été chassé… où il a connu… Pierre l'Ibère, évêque monophysite de Maiouma, près de Gaza" (l.361–368); "rédigés en grec peu après l'année 512" (l.435), "pendant que Sévère était patriarche d'Antioche (512-518)" (l.394–395); 89 chapters (l.305–306); "La plupart des histoires proviennent du cercle de Pierre l'Ibère" (l.403–404); "un recueil d'Apophthegmes d'un nouveau genre, qui a pour but, non d'édifier, mais de combattre le concile de Chalcédoine et ses défenseurs" (l.501–503). Faithful, and all given to Nau.
- The altar (l.5): Kugener, Life of Severus, "il parut juste de lui confier la direction du couvent avec le grand Jean, ainsi que de réserver l'autel à Jean, surnommé Rufus. Celui-ci avait étudié précédemment les lois à Beryte avec Théodore" (`zacharias-scholasticus_vie-de-severe-po2-syr-fra_kugener1903.txt` l.5552–5555). Faithful. The same Life goes on to say Peter of Antioch drew him into the clergy and ordained him priest (l.5596–5599), which supports l.3 from a second witness.
- The heading (l.5; card `remembered` 1): "rédigées par l'un des disciples de saint Pierre l'Ibère, nommé le prêtre Jean de Beit-Rufin, d'Antioche, évêque de Maiouma de Gaza" (l.616–618). Exact.
- Checked with eyewitnesses (l.7): ch. XXI, "j'ai contrôlé sa vérité l'ayant apprise en l'entendant raconter d'une façon certaine par ceux qui l'avaient vue" (l.2802–2804). Faithful.
- Raabe (l.9): title "Syrische Übersetzung einer um das Jahr 500 verfassten griechischen Biographie" (`life-of-peter-the-iberian_petrus-der-iberer-deu_raabe1895.txt` l.1); "dessen Name schon zu Euagrios' Zeit [536 — 593] nicht bekannt war" (l.667–668); "ob etwa ihr Verfasser mit unserm Biographen identisch ist" (l.609–610). Faithful. I searched the Library for any held scholar who gives the Life of Peter to John Rufus and found none, so the records' absence note stands.
- The close (l.11): "Notre père et évêque, le vénérable abba Pierre l'Ibère, nous racontait" (l.620). Faithful.

**Findings**
- **M6 MINOR (items 1, 7; an identification told without its owner).** Brief l.5: "In his Life of Severus, Zachariah of Mitylene says…". The card repeats it in `remembered` 2, `uncertain` 1 and 2, and the Kugener source's author; the records witness does too. That the author of the Life became bishop of Mitylene is E. W. Brooks's identification (`zachariah-rhetor_chronicle_hamiltonbrooks1899.txt` l.351–367). Kugener, the Life's editor, calls him "Zacharie le Scholastique" (l.76, 307) and nowhere bishop of Mitylene. The batch README keeps "Zachariah Rhetor" for this reason, and the Zachariah card puts Mitylene in `uncertain` 1 as "Brooks's identification". The John Rufus texts tell it plainly, and the Severus texts call the same man "Zachariah Rhetor". No held witness argues against Brooks, so this is minor, but the pattern asks a Dominant Modern Reconstruction to name its owner, and the batch should use one name. Fix: "Zachariah Rhetor" at each of these places in the John Rufus brief, card and records.
- **M7 MINOR (item 8).** Brief l.1: the first mention is "His companion smiled and said it had been Juvenal's." The place comes only on the second mention ("Juvenal of Jerusalem"), and a listener is never told who Juvenal was. Chapter XVI says he lived in the monastery "quand il arriva à l'épiscopat" (l.2136). Fix: "His companion smiled and said it had been the monastery of Juvenal, bishop of Jerusalem." Then: "John answered that Juvenal had been the companion of Judas…".
- **M8 MINOR (item 10).** The brief runs 333 words (2:03), past the non-major ceiling of about 324. Suggested cut, brief l.9: "Its German editor, Richard Raabe, asks whether the author of the Plerophories wrote it too, and leaves the question open." This replaces the last two sentences; card `uncertain` 3 already holds the Evagrius point.
- **M9 MINOR (records).** The records claim "He succeeded Peter the Iberian as bishop of Maiuma; he was in Jerusalem in 485" is tagged Widely Accepted. It rests on Nau alone ("Il semble dès lors… car il lui a succédé", l.373–374), and the card's `uncertain` 2 sets it against Zachariah's narrower line. Fix: tag it Dominant Modern Reconstruction, witness Nau, and keep the heading's "évêque de Maiouma" as the Documented claim it already is.
- With M6 to M8: 321 words (1:59), FK 8.2, Flesch 64.8.

---

### 3. Zachariah Rhetor

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | minor (M11); card minor (M12, M13) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Brooks, Land named) |
| 6 | Partisan witness named and marked | PASS (l.5, "to defend his friend"; the preface's attack on Chalcedon told as his) |
| 7 | Contested both sides | FAIL in the brief, minor (M10); card PASS |
| 8 | Common names placed | PASS (Severus of Antioch; Zachariah by the record's epithet) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:00) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes and close tellings**
- The first day at Berytus (l.1), Kugener: "je me rendis à mon tour à Beryte pour étudier le jus civile. Je m'attendais à devoir souffrir de la part des étudiants… Je m'attendais surtout à avoir à souffrir de la part de Sévère… J'entrai le premier jour dans l'école de Léontios… Il me salua en effet le premier, en souriant" (l.2902–2915). Faithful.
- Gaza and Alexandria (l.3): "Il était comme moi originaire du port de Gaza" (l.3535, said of Zenodore); "avec lequel j'ai été, dès sa première jeunesse, à Alexandrie et en Phénicie, entendant les mêmes maîtres que lui" (l.526–528). Faithful.
- Brooks's dating (l.3): "a native of Gaza… studied law in company with Severus at Alexandria and Berytus in the reign of Zeno… practised as an advocate at Constantinople, where he was living at the time of writing the Life" (`zachariah-rhetor_chronicle_hamiltonbrooks1899.txt` l.346–350). Exact, given to Brooks.
- The pamphlet (l.5): "J'examinais les livres des libraires établis dans le Portique royal… me donna le libelle… on bafoue un philosophe… il s'est distingué depuis dans l'épiscopat… J'entends parler de Sévère" (Kugener l.384–391). Faithful. "in Constantinople" rests on Brooks's l.349–350 and Kugener's gloss "ici (= à Constantinople)" (l.7060); acceptable.
- "a very lame one" (l.5): Brooks, Select Letters introduction, "it must be admitted that the answer is a very lame one" (`severus-of-antioch_select-letters-book6-part1_brooks1903.txt` l.89–93). Exact. This is Brooks in his second book, and the card's sources list it.
- The history (l.7): the compiler's appendix, "for the most part from the Chronicle of Zachariah, a rhetor, which he wrote in Greek to a man named Eupraxius, who lived at the Court" (l.300–304, quoting l.2040–2044); Brooks, "the work of Zachariah ended in 491… who followed him in bks. 3-6 only, and to whom the name of Zachariah was wrongly attached by later writers" (l.310–314). Faithful.
- Mitylene (l.9): "the author of the Dialogue… inscribed 'Zachariou Scholastikou… episkopou Mutilēnēs', who in his preface states that he had studied at Alexandria… Now Zachariah of Mitylene was present at the Synod of 536… conforming perhaps to the Chalcedonian faith, was made bishop of Mitylene" (l.353–366); note 4, "His name is not among the signatures to the decree of the Synod of 536, and he may possibly have been a nominee of Anthimus" (l.385–386). See M11.
- The close (l.11): the preface "tore into ten thousand rents the perfect Robe of Christ, woven from the top throughout" (l.2182–2183), within "the history of one Zachariah by name, who begins to write in Greek to Eupraxius as follows" (l.2163–2165). Exact; the compiler presents the preface as Zachariah's.
- The records' handling of Brooks's withdrawn Plerophories note (corrigenda, "p. 3, note 5. Omit the second sentence", l.193) is right.

**Findings**
- **M10 MINOR (item 7; disputes in place).** Brief l.7: "Brooks says the compiler followed Zachariah in books three to six only…". The records file this as a `contested_claim` with Land on the other side, and the card's `uncertain` 4 gives both. The brief gives one. Brooks: "In spite of these facts Land ascribes bk. 7 to Zachariah" (l.330). Kugener names Land as the 1870 editor of the Syriac (`zacharias-scholasticus_…kugener1903.txt` l.17148). Fix, after that sentence: "Land, the chronicle's first editor, gives him book seven as well."
- **M11 MINOR (item 1).** Brief l.9: "A bishop of that name was at a synod in 536, Brooks says, though his name is not among the signatures to its decree. Brooks suggests, with a "perhaps," that he had come over to Chalcedon's side by then." Brooks's "perhaps" goes with being made bishop ("at a later time, conforming perhaps to the Chalcedonian faith, was made bishop", l.364–366). The missing signature is Brooks's note, and there he reads it the other way: "he may possibly have been a nominee of Anthimus" (l.386), the bishop the synod condemned. Set side by side, the two sentences suggest a link Brooks does not make. Card `uncertain` 2 has the same gap. Fix, brief: "A bishop of that name was at a synod in 536, Brooks says. Brooks suggests, with a "perhaps," that he had come over to Chalcedon's side to become bishop." Card `uncertain` 2: "…and notes that his name is not among the signatures to its decree; he may possibly have been a nominee of Anthimus, Brooks says."
- **M12 MINOR (card; item 1).** Card `uncertain` 1: the identification "rests on the Greek heading of a dialogue…". Brooks also relies on Dionysius Bar Salibi's citation of "Zachariah the Rhetor and bishop of Melitene", which he reads as an error for Mitylene (l.260–263, 357–358). Fix: "It rests on the Greek heading of a dialogue by 'Zachariah Scholasticus', later bishop of Mitylene, whose preface says he studied at Alexandria, and on a citation by Dionysius Bar Salibi of 'Zachariah the Rhetor and bishop of Melitene', which Brooks takes for a slip for Mitylene."
- **M13 MINOR (card; an absence put too widely).** Card `dates`: "No source used here gives his birth or death." Brooks gives a bound: he "died or was deposed between 536 and 553" (l.366–367), and the records' absence note mentions it. Fix: "No source used here gives his birth. By Brooks's identification he died or lost his see between 536 and 553."
- With M10 and M11: 324 words (2:00), FK 7.8, Flesch 63.2.

---

### 4. Severus of Antioch (major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | minor (M15) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (M16) |
| 5 | No role for a witness | PASS (Evagrius, Brooks, Zachariah named) |
| 6 | Partisan witness named and marked | PASS (Evagrius at l.1, "on the side of the Council of Chalcedon"; the Alcison letter "from Chalcedon's side"); minor (M15) on independence |
| 7 | Contested both sides | FAIL in the brief, minor (M14); card and records PASS |
| 8 | Common names placed | PASS (Flavian as bishop of Antioch, Anthimus of Constantinople, Julian of Halicarnassus, the emperor Justin with the year) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:30, at the cap) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes and close tellings**
- The arrest (l.1), Evagrius IV.4, tr. Walford: "Justin, in the first year of his reign, ordered him to be arrested, and to be punished, as some say, by having his tongue cut out… he flies from his see, in the month Gorpieus, which in the Latin language is called September, in the five hundred and sixty-seventh year of the Era of Antioch" (`evagrius-scholasticus_ecclesiastical-history_walford1846.txt` l.7872–7898). Faithful. Brooks: "on Sept. 29 fled from Antioch", and the note "Evagr. (iv. 3) seems to place his flight in 519… but the homilies… which are arranged chronologically, and end with Lent 518, are decisive for the earlier date" (`severus-of-antioch_select-letters-book6-part1_brooks1903.txt` l.200, 213–218). See M14.
- Birth and schooling (l.3), Kugener: "L'illustre Sévère est Pisidien d'origine, sa ville natale est Sozopolis" (l.533); "sa mère devenue veuve l'envoya avec ses deux frères, qui étaient plus âgés que lui, à Alexandrie, pour étudier la grammaire et la rhétorique" (l.591–593). Faithful. Brooks: "His enemies accused him of having in his youth followed heathen practices, and it was in order to refute this charge that Zacharias wrote his life… the answer is a very lame one" (l.89–93). Exact.
- Baptism and the monastery (l.5): Kugener, "baptisé dans la chapelle du divin et victorieux martyr Leontios" (l.5224–5226); Evagrius III.32–33, "having participated in holy baptism in the sacred precinct of the divine martyr Leontius, who is revered at Tripolis… a certain monastery situated between the city of Gaza and the town called Majumas; in which latter place Peter the Iberian… passed through the same discipline… expelled from his own monastery by Nephalius… obtains the notice of the emperor Anastasius, as is narrated by the author of the life of Severus" (l.6986–7014). Faithful; see M15.
- Bishop and letters (l.7): Brooks, "Severus was ordained his successor (Nov. 6, 512)" (l.174–175); Evagrius, "Severus, in issuing synodical letters, expressly anathematised the synod at Chalcedon"; the Alcison letters, "which included an anathema, both on the synod and all others who affirmed two natures or persons in the Lord" (l.7015–7037). Faithful.
- Exile and death (l.9): Brooks, "for the rest of his life lived for the most part in hiding in Egypt… wrote the controversial works against Julian the deposed bishop of Halicarnassus, who maintained the incorruptibility of Christ's body" (l.201–206); "in Mar. 536 Anthimus was deposed, and he and Severus expelled from the city, while at the synod held in May their final condemnation was decreed. On Feb. 8, 538 Severus died in Egypt" (l.237–241). Evagrius IV.10, "She also persuades Justinian to send for Severus" (l.8166–8169); IV.11, "a constitution was drawn up by Justinian in which he anathematised Severus, Anthimus, and others" (l.8212–8214). Faithful.
- Misael (l.11, 13), Select Letters I.17: "as to interest or the avaricious system of loans it was my desire not to know even the very name of them" (l.2773–2775); "a great load of debts and of interest was hanging over it… I forgot the spiritual laws" (l.2783–2786); "who Himself alone is able to heal our church that is groaning under many wounds, and to change need into abundance" (l.2826–2828). Exact.
- The letter count (l.13): "the total cannot have been less than 3759. Of these the version of Athanasius comprises 123 only" (l.253–256); "made in the year A.S. 980 (669)" (l.279). The year 669 is Brooks's conversion, and the sentence opens on "Brooks reckons". Faithful.
- Card: Brooks on the monastery of Theodore, "Called by the so-called Zacharias Rhetor (vii. 10) the monastery of Theodore" (l.140–141); the episcopate "little evidence beyond the assertions of his enemies produced at the synod of 536" (l.195–197); "probably under Theodora's influence" (l.233). Faithful. I found no birth year in Zachariah's Life, Evagrius or Brooks, so the card's absence stands.

**Findings**
- **M14 MINOR (item 7; disputes in place).** Brief l.1: "He fled his see in September. E. W. Brooks, the English translator of his letters, dates the flight to 518." The records hold the year as a `contested_claim`, and the card's `uncertain` 3 gives both sides; the brief gives Brooks's side only. Fix: "He fled, and E. W. Brooks, the English translator of his letters, dates the flight to 29 September 518. Evagrius's year seems to give 519, Brooks notes, but Severus's dated sermons decide it."
- **M15 MINOR (items 1, 6; one witness counted as two).** Brief l.5: "Zachariah and Evagrius agree he was baptized…" and "…where Peter the Iberian had lived, Evagrius says." Evagrius ends the whole passage, baptism to Anastasius, with "as is narrated by the author of the life of Severus" (l.7013–7014), and Brooks notes that Zachariah's Life was "Used by Evagrius (iii. 33)" (l.97). Zachariah's Life tells the same events itself: Nephalius (Kugener l.6524, 6649–6660) and the plea to the emperor (l.6776–6782). The brief counts a source and its copyist as two agreeing witnesses. Fix: "Zachariah says he was baptized at the shrine of the martyr Leontius at Tripolis. He became a monk between Gaza and Majuma, where Peter the Iberian had lived. … Severus pleaded their cause at Constantinople before the emperor Anastasius. Evagrius tells this from a Life of Severus, which Brooks takes for Zachariah's."
- **M16 MINOR (item 4).** Brief l.3: a 29-word narrator sentence ("His fellow student Zachariah Rhetor wrote a Life of him, which says…"). Fix: "His fellow student Zachariah Rhetor wrote a Life of him. It says his widowed mother sent him and his two older brothers to Alexandria to study grammar and rhetoric."
- Length with M14 to M16: the brief is at the cap already. Suggested cuts: drop l.13's "Brooks reckons his letters once numbered at least 3,759; a Syriac version made in 669 keeps 123." (card `keyWorks` 1 holds it), so the close reads "In the same letter, Severus says God alone is…", with `[warmly]` still before it. Shorten l.3's Brooks sentence to "Brooks says Zachariah wrote to answer a charge of pagan rites in Severus's youth, and judges that "the answer is a very lame one."" Scored: 401 words (2:29), FK 7.9, Flesch 61.9.

---

### Totals

Part A: 1 blocking, 16 minor.

| Profile | Blocking | Minor |
|---|---|---|
| Joshua the Stylite | 1 (B1) | 5 (M1 to M5) |
| John Rufus | 0 | 4 (M6 to M9) |
| Zachariah Rhetor | 0 | 4 (M10 to M13) |
| Severus of Antioch | 0 | 3 (M14 to M16) |

Blocking: **B1**, Joshua the Stylite. Brief l.11, card `legacy.traces` 1 and `uncertain` 4, and the records tell Wright's 1882 attribution of the preserving chronicle to Dionysius of Tell-Mahre (d. 845) as fact. Held files by Nau (po08 l.48221–48226: the same Vatican ms. syr. 162, by a "Pseudo-Denys" writing in 775), Brooks (PO 17 l.714, "the so-called Dionysius") and Chabot (Michael the Syrian t.1 l.63096–63099) say the compiler was someone else.

Cross-profile note: the same man is "Zachariah of Mitylene" in the John Rufus texts and "Zachariah Rhetor" in the Zachariah and Severus texts (M6). One name across the batch, the README's, closes it.

## Part B

Reviewer: independent, first sight of these drafts. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; Mark's rulings in the Decision-Log (2026-11-12: majors capped at 2:30, about 405 words, a cap and not a target; non-majors 1 to 2 minutes, at most about 324 words). The coordinator also asked that Brigid's brief say plainly that Cogitosus's Life was written long after her and is a miracle Life, tagged at the right confidence. I hunted hardest for the recurring faults: witness swaps (an editor's summary or note given to the ancient Life, or one witness's fact given to another), a modern year told as an ancient writer's, a contested event told as settled, absence claims a held file contradicts, and namesakes merged (the two abbesses Caesaria; Brigid and Birgitta). I did not edit the drafts. I made no paid or model-API calls and used no web. Readability and quote search ran on local scripts only.

Profiles: `brigid-of-kildare`, `caesaria-of-arles-the-elder` and `caesarius-of-arles` (major), with their entries in `records.json`. Files are in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch2/`. Brief line numbers refer to the `.brief.txt` files, where each paragraph is one line and blank lines count (paragraphs sit on l.1, 3, 5, 7, 9, 11, 13). Other line numbers point to files under `cic/texts/`.

Method. I searched every quotation and close telling in the three briefs and cards in the vendored file the card or records cite, stripping XML, collapsing whitespace and searching tolerantly in the OCR files (Migne PL 72 and PL 67, Krusch's MGH SRM 3, Maassen's MGH Concilia 1, Williams ab Ithel's Annales Cambriae, Stokes's Tripartite Life and Book of Lismore, White's Muirchu). I read each hit in context to see who is speaking: the ancient Life, an editor's introduction, apparatus or note (Krusch, Basnage, Migne's editors, the Bollandists, Maassen), or an index. I checked every factual sentence of each brief against its passage, searched before accepting each absence claim, and compared each `records.json` entry with its brief and card. Readability came from `engine.m1.gates.grade_text`, run from the repo root. Length assumes 162 words a minute. Every suggested brief fix below was applied to a scratch copy and re-scored; the post-fix word count and scores are given with each profile.

### Applies to all three

- **Audio = brief.** Each audio script matches its brief exactly once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, placed before the closing paragraph. No tag appears in any brief or card.
- **Readability.** All three pass (FK at most 10, Flesch at least 60). Narrator sentences past 25 words: Caesaria l.1 (26 words, "He had sent her there, his disciples write, so that she might learn what she would teach, and be a pupil before she was a teacher."), which carries the Life's own words "ut disceret quod doceret, et prius esset discipula quam magistra" and reads well aloud; noted, not a finding.
- **Length.** Caesarius runs 403 words (2:29), under the cap. Brigid runs 327 words (2:01), within "about 2:00". Caesaria runs 331 words (2:03), past the non-major mark (M8). Every `briefLength` reads "about 2 minutes" or "about 2 minutes 30 seconds" and matches.
- **Card order.** All three follow Mark's order. Missing fields are left out: Brigid and Caesaria have no keyWorks and no "Their own words". keyWorks never goes past three. Each `uncertain` list opens with the brief's main caveat (but see B1 and B2 on what that caveat says).
- **Namesakes.** Brigid is kept apart from Birgitta: neither the brief nor the card names Birgitta, and `otherNames` holds only "Brigida" and "Brigit", the held spellings (Cogitosus and the annals; Stokes's Lismore Life). The two abbesses Caesaria are kept apart in all three profiles: Caesaria's brief names "another Caesaria" as successor (l.7) and tells the confusion with its witness (l.9); Caesarius's brief has the Life written for "the abbess who then led the convent" (l.3), the second Caesaria, and never calls her his sister. Checked against the Life's prologue ("reverenda nobis virgo Caesaria", Krusch l.36188), I,58 ("succedente eidem quae nunc superest Caesaria matre", l.38054) and II,47 (l.39562–39563).
- **Who test (item 14).** Brigid founded and led Kildare and is known through a biographer's record, marked as hagiography (scan row l.92). Caesaria stands on the scan's woman rule, one WHO source and she led (scan row l.82), confirmed by the coordinator. Caesarius has his own Rules, letters, sermons and council signatures, and a following. The drafts carry no list lines; those belong to the map build and were not checked here.

| Profile | Words | Est. length @162 | FK | Flesch |
|---|---|---|---|---|
| Brigid of Kildare | 327 | 2:01 | 6.5 | 71.1 |
| Caesaria of Arles the Elder | 331 | 2:03 | 6.6 | 73.4 |
| Caesarius of Arles (major) | 403 | 2:29 | 6.6 | 74.1 |

---

### 1. Brigid of Kildare

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, blocking (B1); minor (M1, M2) |
| 2 | Quotes verbatim | PASS (card minor M5) |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Cogitosus, Basnage, Migne, Muirchu, Newport White, Whitley Stokes named; "his editor Newport White" is named) |
| 6 | Partisan witness named and marked | PASS (Cogitosus's Life marked as hagiography, l.3) |
| 7 | Contested both sides | PASS for her parents and her death year; the date of Cogitosus, see B1 and M4 |
| 8 | Common names placed | FAIL, minor (M3) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:01) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS in shape; caveat content, see B1; card minor (M6) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes and close tellings**
- The church scene (l.1), Cogitosus in PL 72 (`john-biclaro-leander-pl72-lat_migne1878.txt`): the bodies of "episcopi Conleath et hujus virginis sanctae Brigidae ... a dextris et a sinistris altaris ... monumentis posita ornatis, vario cultu auri et argenti et gemmarum, et pretiosi lapidis, atque coronis aureis et argenteis desuper pendentibus" (l.59384–59403, two-column OCR); the painted, linen-hung wall across the church (l.59410–59414); the bishop "cum sua regulari schola" by one door, the "abbatissa cum suis puellis et viduis fidelibus" by another (l.59420–59430). Faithful.
- "the head of almost all the Irish churches" (l.3): "caputpene omnium Hiberniensium Ecclesiarum" (l.58505). The brothers' request and the elders: "Cogisti me, fratres ... pauca de pluribus, a majoribus et peritissimis tradita" (l.58488–58496). Faithful.
- The parents (l.5): "a christianis nobilioribusque parentibus ... patre Dubtocho, et matre Brocca" (l.58535–58538). The hermit called "de eremo et de sua vita solitaria ... ut Ecclesiam in episcopali dignitate cum ea gubernaret" (l.58517–58518). The robes: "vestimenta transmarina et peregrina episcopi Conleath ... pauperibus largita est", and like garments "perlata in curru duarum ... rotarum" (l.59171–59205, column-interleaved OCR). Faithful.
- The feast (l.7, 13): "alii ob epularum abundantiam, alii languidi propter sanitates, alii ad spectaculum turbarum; alii cum magnis donis venientes ad solemnitatem nativitatis sanctae Brigidae, quae in die Kalendarum Februarii mensis dormiens" (l.59487–59493). Faithful. Cogitosus gives no year: searched the Life (l.58480–59515) for "anno" and numerals; none.
- The annals (l.7), `annales-cambriae-rolls-series-20-lat_williams-ab-ithel1860.txt`: "454. X. Annus. Brigida Sancta nascitur" (l.2352) and "521. Lxxvii. Sanctus Columcille nascitur. Quies Sanctae Brigidae" (l.2399–2400); the A.D. years are the editor's margin, as the card says. The Nennius extracts, Stokes (`stokes_tripartite-life-of-patrick-v2-...1887.txt`): "A natiuitate Columbae usque mortem sanctae Brigidae quatuor anni sunt" (l.13495–13496). Faithful.
- Basnage (l.9): "EODEM TEMPORE. COGITOSUS" under "ANNO DOMINI DXCI" (l.58417, 58430); "Cogitosum hic reponimus, aliorum vestigiis insistentes potius quam nostrae sententiae addicti. Quippe multo recentiorem credimus illum scriptorem" (l.58436–58446); the painted images "quae posteriora redolent saecula" (l.58476–58478). Faithful, except "at her tomb" (M2).
- Muirchu and White (l.9), `patrick_writings-and-life-with-muirchu-eng_white1920.txt`: "save only that of my father Cogitosus" (l.3805–3806); "Cogitosus is known as the author of a Life of St. Brigid of Kildare" and Graves's emendation "now generally accepted" (l.3741–3750); Muirchu at Birr "a.d. 695-697" (l.3768–3770). Faithful.
- The Lismore Life (l.11), `stokes_lives-of-saints-from-the-book-of-lismore-iri-eng_1890.txt`: "bought a bondmaid named Broicsech" (l.18019–18021); "the form of ordaining a Bishop was read out over Brigit" at her veiling by Bishop Mél (l.18282–18288); the Book compiled "in the latter half of the fifteenth century" (l.218–219). Faithful.
- Card `uncertain` 3, "nepote culpabili": Cogitosus's close, "Orate pro me Cogitoso nepote culpabili" (l.59502), and Basnage, "Qua ratione igitur se nepotem appellaverit, nobis aeque ac Canisio incertum" (l.58456–58460). Card `uncertain` 4, the Canisius note: "Marianus Scotus ait obiisse sub Justino Seniore imperatore anno 321 [OCR for 521], quem potius sequor cum Baronio ... quam Sigebertum. Can." (l.59368–59370). Card `uncertain` 6: "Haec enim legibus adversantur" (l.58468). All faithful.

**Findings**
- **B1 BLOCKING (items 1, 7, 12; the coordinator's requirement; a settled point framed as open).** The brief never says plainly that Cogitosus wrote long after Brigid. Its only signals are "from what he says elders had handed down" (l.3) and, inside a paragraph that opens "When Cogitosus wrote is also disputed" (l.9), Basnage's "much later" and an undated Muirchu. A listener hears the date of the Life as an open question. It is not open on that point. Every held witness puts the Life well after her death, and they differ only on how long: Cogitosus himself writes of her tomb and her feast and from what elders handed down (l.58494–58496, 59384–59403, 59487–59493); Migne's placing is 591 (l.58417, 58430); Basnage holds him "non coaevum, sed recentiorem", one who heard of her living virtues "a majoribus tantum" (l.58470–58472); White makes him the father of Muirchu, who signed at Birr in 695–697 (l.3741–3750, 3768–3770); and Stokes's index dates him "A.D. 800-835" (M4). The card repeats the gap: `uncertain` 1 says "hagiography and mostly miracles" and "from what elders had handed down", but not "long after". `records.json` has no claim that the Life was written long after her, so it carries no confidence for the point the coordinator asked to have tagged. The README says the brief marks the Life as "written long after her", which the brief does not yet do.
  Fix, brief l.3: "He wrote her Life in Latin long after her death, at the brothers' request, from what he says elders had handed down. It is hagiography, and mostly miracles." Brief l.9: "How long after her Cogitosus wrote is disputed. Migne prints the Life under the year 591, following others, as Basnage's note says. Basnage thought Cogitosus wrote much later, since he describes painted images and miracles in her church. Muirchu, in his Life of Patrick, names his father Cogitosus. Muirchu's editor Newport White takes the father for Brigid's biographer, and places Muirchu in the 690s." To hold the length, delete l.11's second sentence ("It says that when Bishop Mél gave her the veil, the form for making a bishop was read over her."); the card's `remembered` 2 keeps it. Card `uncertain` 1: "Her life rests on Cogitosus's Life, which is hagiography and mostly miracles, written long after her death. Cogitosus says he wrote from what elders had handed down. He gives no year for her birth or death." Records: add the claim "Cogitosus wrote long after her death, from what elders handed down", witness "Cogitosus, prologue (l.58494–58496), with Basnage (l.58470–58472), White (l.3741–3750, 3768–3770) and Stokes's index (l.21226)", `formation_confidence` Widely Accepted; the contested claim "When Cogitosus wrote" becomes "How long after her Cogitosus wrote", with the sides as they are plus Stokes (M4). Add "Basnage: the Life teems with miracles ('tota miraculis scatet', l.58446)" as a Documented claim, so the miracle-Life marking has its witness in the records.
- **M1 MINOR (item 1; a place name given to Cogitosus).** "In the great church at Kildare, Cogitosus writes" (l.1) and "On her feast, Cogitosus says, crowds came to Kildare" (l.13). Cogitosus never names Kildare in the held Life (searched l.58480–59515). He sets her monastery "in campestribus campi Liffei" (l.58512–58513). The name comes from White ("a Life of St. Brigid of Kildare", l.3748–3749) and the Lismore Life ("the place in which Kildare stands to-day", l.18604). The identification is not in doubt; only the attribution is wrong. Card `traces` 1 has the same ("the church of Kildare", as Cogitosus's). Fix: l.1 "In her great church on the plains of the Liffey, Cogitosus writes, ..."; l.13 "On her feast, Cogitosus says, crowds came to her church." l.3's narrator line "Brigid founded the monastery of Kildare in Ireland" stands. Card `traces` 1: "Cogitosus says her church was ruled together by a bishop and an abbess, ...".
- **M2 MINOR (item 1; Basnage's ground).** "since he describes painted images and miracles at her tomb" (l.9). Basnage says Cogitosus had seen wonders "in ejus templo operari solita", worked in her church (l.58466–58468), not at her tomb. Card `uncertain` 2 ("of miracles at her tomb") and the records claim ("he saw miracles at her tomb") repeat it. Fix: "miracles in her church", in all three.
- **M3 MINOR (item 8).** "the year Columba was born" (l.7). Several saints bear the name. The annals name him "Sanctus Columcille" (l.2399), and later "Columcille in Brittania exiit" (l.2417). Fix, brief l.7: "The Welsh annals put her death in the year Saint Columcille was born." Card `dates` and `uncertain` 4: "the year Columcille was born". (Card `dates` and `uncertain` 4 also name "Sigebert", a common name; Basnage and the Canisius note give him no place, so the name stays as the sources have it and the gap is logged.)
- **M4 MINOR (items 7, 12; records; a held side missing).** Stokes's index to the Tripartite Life, the file the card already cites, dates Cogitosus "A.D. 800-835" (l.21226), which sits against White's late-seventh-century identification. The scan row noted it (Who_Scan_Era3 l.92). Neither the card's `uncertain` 2 nor the records' contested claim "When Cogitosus wrote" gives it. Fix, card `uncertain` 2, add: "Whitley Stokes, in the index to his Tripartite Life, dates Cogitosus to between 800 and 835." Records: add the same as a side, witness "Stokes, index (l.21226)".
- **M5 MINOR (item 2; card).** Card `remembered` 1: "they had one heart and one mind". The Latin is "ut unum cor consiliumque haberent unum" (l.5921–5923), one heart and one counsel; "one mind" moves it toward Acts 4:32. Fix: "one heart and one counsel". The records claim already reads "one counsel".
- **M6 MINOR (card; a report told as a date).** Card `dates`: "Basnage's note in Migne gives her birth as 439". Basnage says "Nata dicitur Brigida anno 439" (l.58467–58468), is said to be born; `uncertain` 4 rightly calls it a report. Fix: "Basnage's note in Migne reports her birth as 439 and gives her death as 518, after Sigebert, or 521, after Martinus Polonus".
- Length with B1, M1 and M3, and the l.11 cut: 319 words (1:58), FK 6.9, Flesch 69.0. No sentence past 25 words.

---

### 2. Caesaria of Arles the Elder

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, blocking (B2); minor (M7) |
| 2 | Quotes verbatim | PASS (card minor M9) |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (M7) |
| 5 | No role for a witness | PASS (the Life's five authors, Krusch, Migne, the Bollandists named) |
| 6 | Partisan witness named and marked | PASS ("It is a saint's Life", l.3) |
| 7 | Contested both sides | PASS (which Caesaria the letters address, on the card; Krusch's 512 and Cassian identification marked as his, l.5) |
| 8 | Common names placed | PASS (Caesaria of Arles l.3; John Cassian; the second Caesaria kept apart) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | FAIL, minor (M8, 2:03) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS in shape; caveat content, see B2 |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (scan's woman rule) |

**Quotes and close tellings**
- The founding and the call (l.1), Life I,35, Krusch (`passiones-vitaeque-sanctorum-merovingici-mgh-srm-3-lat_krusch1896.txt`): "in latere ecclesiae monasterii fabricat archam. Evocat Massiliensi monasterio venerabilem germanam suam Caesariam, quam inibi ideo direxerat, ut disceret quod doceret et prius esset discipula quam magistra, et in praeparatis habitaculis cum duabus aut tribus interim sodalibus intromittit" (l.37205–37212). The same in Migne (`facundus-ferrandus-caesarius-dionysius-pl67-lat_migne1865.txt` l.84953–84960). Faithful.
- The crowds and the enclosure (l.5): "facultatibus quoque et parentibus renuntiantes ... ita retrusae, ut usque diem transitus earum nulli liceat foris ianuam egredi de monasterio" (l.37212–37218). Faithful in substance; see M7 on "she". The Rule addressed "Sanctis ... sororibus in monasterio quod ... condidimus" (pl67 l.85049–85051). Faithful.
- The burial (l.7): the triple basilica with stone sarcophagi for the virgins (Life I,57, l.37990–37995); "Non multum igitur post monasteriae [Migne: monasterii] matrem germanam suam Caesariam ... inter has quas praemiserat ... iuxta eam quam sibi paraverat condidit sepulturam, succedente eidem quae nunc superest Caesaria matre" (I,58, l.38050–38054); "ultra ducentarum puellarum venerabilem Caesariam matrem" at his last visit (II,47, l.39562–39563). Faithful.
- The confusion (l.9): the Bollandist commentary "(Ex Bolland.)" in PL 67: "adeoque illi dedicata non est haec Vita, ut per errorem scripserunt aliqui" (l.96138–96145), and Migne's note (a), "Haec Caesaria non est soror S. Caesarii, quae ante ipsum erat defuncta" (l.77109–77112). Faithful.
- Krusch's date and identification (l.5): "cum die 26. Augusti a. 512 monasterium dedicatum est" and "Massiliam in monasterium a Cassiano conditum" (l.34734–34737), with note 4 citing Gennadius c.62 (l.37259). The Life says only "Massiliensi monasterio". Faithful, and rightly marked as Krusch's.
- The close (l.13): "Caesarii patris, Caesariae matris expetunt gremium" (l.37214). Faithful.
- Card `uncertain` 3: the headings "EPISTOLA PRIMA S. CAESARII AD CAESARIAM ABBATISSAM" (pl67 l.86506–86507) and "Caesariae sanctae sorori abbatissae" (l.86729–86732); Migne's preface "missae feruntur ad Caesariam sororem suam" (l.76995–76997). Faithful.

**Findings**
- **B2 BLOCKING (items 1, 4; a false absence; recurring fault 4).** "All that is known of her comes from her brother's Life." (l.3). Card `uncertain` 1 opens the same way. A held file says otherwise, and the card itself cites it. Krusch reports that Venantius Fortunatus wrote of her, "neque vero Casaria ipsius artem effugit pia soror, quam non semel proposuit exemplum imitandum" (l.35667–35668), and his note on her name gives Fortunatus's poems and a manuscript of Gregory of Tours, "Ita a Fortunato appellatur (Carm. VIII, 3, 39; App. XIII, 3, 3. 13), quocum cod. B 1 Gregorii, H. Fr. IX, 42, convenit" (Krusch's note 8, l.34757–34758). The card's `remembered` 3 uses the Fortunatus report. The two letters headed to an abbess Caesaria, which Migne's editors say were sent to his sister (l.76995–76997), are a further possible witness. Fix, brief l.3: "Her story comes almost wholly from her brother's Life." Card `uncertain` 1: "Her story comes almost wholly from the Life of Caesarius of Arles, a saint's Life by his disciples: the bishops Cyprian of Toulon, Firminus and Viventius, the priest Messianus and the deacon Stephen. Bruno Krusch adds that Venantius Fortunatus held her up as an example. No words of her own survive." Records: the absent detail "Deeds of hers apart from her brother's" stands; add nothing that says the Life is the only witness.
- **M7 MINOR (items 1, 4; a pronoun that can mislead).** "They were enclosed for life, so that none might pass the convent door until the day she died." (l.5). The paragraph before is about Caesaria, so "she" can be heard as Caesaria. The Life says "usque diem transitus earum", until their own death (l.37217). Fix: "They were enclosed so that none might leave by the convent door until they died."
- **M8 MINOR (item 10; length).** 331 words (2:03), past the non-major mark of about 324 words. Fix, with B2 and M7: shorten l.5's "Caesarius wrote a Rule for them, addressed to the sisters in the convent he had founded." to "Caesarius wrote a Rule for them." The card's `traces` 2 keeps the address.
- **M9 MINOR (item 2; card; one witness's words heard as another's).** Card `remembered` 3: "Bruno Krusch says that Venantius Fortunatus ... more than once held up "Casaria ... pia soror" as an example to follow." The Latin in quotation marks is Krusch's own sentence (l.35667), not a line of Fortunatus, whose poems are not held. Set beside Fortunatus's name it reads as his phrase. Fix: "Bruno Krusch says that Venantius Fortunatus, the poet of Radegund's household, more than once held up Casaria, Caesarius's pious sister, as an example to follow."
- Length with B2, M7 and M8: 316 words (1:57), FK 6.5, Flesch 73.0.

---

### 3. Caesarius of Arles (major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS (the drafter's two flagged passages checked below); minor (M11) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | minor (M10) |
| 5 | No role for a witness | PASS (the Life's five authors, Krusch, Maassen named) |
| 6 | Partisan witness named and marked | PASS ("a saint's Life by men who called him father", l.3; the Life's polemic on Alaric on the card) |
| 7 | Contested both sides | PASS (Valence and Orange: Maassen "leaves open which council came first", l.9) |
| 8 | Common names placed | PASS (Cyprian of Toulon, Silvester of Chalon, Eonius of Arles, Alaric of the Visigoths, Theodoric at Ravenna, Boniface of Rome) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:29) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**The two passages the drafter flagged (the ransom and the silver dish).** Both rest on the Life, not on Krusch alone. Krusch's introduction does summarise them ("sacra ministeria vendens", l.34711; "ut argentei disci dono ab eo honoraretur. Quem cum vendidisset pretioque captivos plurimos liberasset", l.34755–34757), but the brief says nothing that only the summary carries.
- The ransom (l.1), Life I,32: through the garbled columns the Life reads "Fugatis denique obsidionibus et Arelatum Gothis cum captivorum inmensitate reversis, replentur baselicae" (l.37108–37109); it names the silver "quod venerabilis Eonius antecessor suus ecclesiae mensae reliquerat" and "argentea vase" (l.37119–37122); and the clean lines that follow have Caesarius say that priests and clergy "nolunt dare insensibile argentum aut aurum de donariis Christi pro mancipiis Christi" (l.37138–37141), which presumes he did. The brief's "gave the church's silver to buy them free" stays within that. The saying is clean: "Non credo contrarium esse Deo, de ministerio suo redemptionem dari, qui se ipsum pro hominis redemptione tradidit" (l.37143–37144), introduced by "hoc saepissime dicens" (l.37137). The brief gives it "in modern words" and does not quote it. Faithful (see M11 on "to clergy").
- The silver dish (l.7), Life I,37: the OCR is garbled, but the Life's own words survive in pieces: the king's gift with "trecentis" (solidi) and a request that "beatitudo vestra ... percipiat ... in memoria sui habeat"; then "per ministros suos adpretiatum discum facit publice venundari ... pretio coepit captivorum plurimos liberare", and the onlookers' "dominicum munus ... pretium Caesarius episcopus multitudines liberat captivorum" (l.37286–37300). The brief's "The king gave him a silver dish, and he sold it to free more captives" is the Life's.

**Other quotes and close tellings**
- The authors (l.3): the prologue to "reverenda nobis virgo Caesaria" (l.36188); "patris nostri" (I,14, l.36579); Cyprian "Thelonensis antistes" (I,60, l.38080); book one and book two as Krusch's incipit and explicit report them (l.36220–36221, 39664–39665). Faithful.
- His early life (l.5): "Cabillonensis territorii fertur indigena" (l.36259); "Cum ergo octavum decimum gereret aetatis annum, ignorante familia vel parentibus ... sancti Silvestri" (l.36274–36279); "Lirinense monasterium tiro sanctus expetiit" (l.36335); the abbot "cogit ... ad civitatem Arelatensem causa recuperandae salutis adduci" (l.36410–36413); Eonius's ordaining him deacon and priest and his choosing him (l.36500–36575, rough OCR); "inter quasdam sepulturas latibulum requisivit" (l.36580–36581). Faithful.
- Alaric and the exile (l.7): "Alaricum Wisigothorum regem, ad quem tunc Arelatensis civitas pertinebat ... cum esset Arriana barbarus perversitate subversus" (l.36758–36761); the notary Licinianus's charge "civitatem Arelatensem Burgundionum ditionibus subiugare", and "in Burdigalensem civitatem est quasi in exilio religatus" (l.36809–36824). The passing to the Ostrogoths (I,34, l.37198–37199) and "sub custodia Ravennam usque perduci ... regem quoque Theudericum" (I,36, l.37219–37223). Faithful.
- Grace (l.9): "multi quidem aemuli surrexerunt, qui eius resisterent doctrinae de gratia" (l.38073–38074); Valence and Cyprian (l.38077–38081); "nihil per se in divinis profectibus quenquam arripere posse, nisi fuerit primitus, Dei gratia praeveniente, vocatus" (l.38141–38142); "Bonifacius Romanae ecclesiae papa ... prosecutionem sancti Caesarii apostolica auctoritate firmavit" (l.38150–38152). Orange, Maassen (`concilia-aevi-merovingici-mgh-concilia-1-lat_maassen1893.txt`): "pauca capitula ab apostolica nobis sede transmissa" on "gratia et libero arbitrio" (l.4232–4240); Caesarius heads the subscriptions (l.4799–4800); the heading "CONCILIUM ARAUSICANUM A. 529" (l.4142); "Ambiguum igitur relinquitur, utrum concilio Arausicano a. 529 ... Valentinum prius an posterius habitum sit" (l.5240–5242). Faithful; the year is told as Maassen's.
- Rules, sermons, forty years (l.11): "in Francia, in Gallias atque in Italia, in Hispania ... transmisit per sacerdotes, quid in ecclesiis suis praedicare facerent" (l.37972–37974); "per istos quadraginta annos, quibus administravit" (l.39316–39317). Faithful.
- The close (l.13), Rule for Nuns, prologue: "ut cum in regno cum sanctis ac sapientibus virginibus feliciter introibitis, me cum stultis non remanere foris vestro suffragio obtineatis" (pl67 l.85049–85058, two-column OCR). Faithful. The request sits in the prologue's first paragraph, after the greeting and one sentence, so "opens with a request" holds.
- Card: `dates` from Krusch, "a. 542, die ante depositionem S. Augustini, i. e. 27. Augusti" (l.35237–35239), and 469/70 and 501–503 (l.36313, 35270); `remembered` 1 "semper in oculis omnium novus apparebat" (l.39318–39319); `remembered` 2 "qui concilio Arausicano praesedit" (Maassen l.4152–4153); `remembered` 3 Fortunatus as Krusch quotes him, "Et mansit monachus pontificale decus" (l.35663–35666); `traces` 3 Radegund's Poitiers, "quae hanc S. Caesarii Regulam in parthenon suum Pictaviense introduxit" (pl67 l.85035–85037); `uncertain` 7 the Testament "a clerico ecclesiae maioris ... fictum", for "tributorum immunitatem" (l.35677–35686). All faithful.

**Findings**
- **M10 MINOR (item 4; a pronoun that can mislead).** "Boniface, bishop of Rome, upheld Caesarius. He signed first at a council in Orange, whose chapters on grace and free will came from Rome." (l.9). The nearest "he" is Boniface, so a listener can hear the bishop of Rome signing at Orange. Fix: "Caesarius signed first at a council in Orange, ..." (word count unchanged).
- **M11 MINOR (item 1; close telling).** "His disciples report what he often said to clergy who would not do the same." (l.1). Caesarius speaks of those clergy in the third person, wishing they would explain themselves: "Velim tamen dicerent darentque mihi rationem aliqui mei domini sacerdotes sive reliquus clerus, qui ... nolunt dare" (l.37137–37140). Fix: "what he often said of clergy who would not do the same."
- Length with M10 and M11: 403 words (2:29), FK 6.7, Flesch 73.7.

---

### Totals

2 blocking (B1 `brigid-of-kildare`; B2 `caesaria-of-arles-the-elder`) and 11 minor (M1–M6 `brigid-of-kildare`; M7–M9 `caesaria-of-arles-the-elder`; M10–M11 `caesarius-of-arles`). The drafter's concern about the Caesarius opening and the silver dish is cleared: the Life carries both, and nothing in the brief rests on Krusch's summary alone. The two Caesarias are not merged anywhere, and Brigid is not confused with Birgitta. Every fix above was checked against the line it cites, and every brief fix was scored on a scratch copy: Caesarius stays under the 2:30 cap (403 words), and Brigid (319) and Caesaria (316) at or under about 324 words, with FK at most 10 and Flesch at least 60.

## Part C
### R1 review: era 3 batch 2, part C (Church Family Tree Who profiles)

Reviewer: independent, first sight of these drafts (branch `who-profiles-era3-batch2`, commit c99df43f). Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; Mark's rulings in the Decision-Log (majors capped at 2:30, about 405 words, a cap and not a target; non-majors 1 to 2 minutes, at most about 324 words; 162 words a minute). For Julian the coordinator's instruction was that length follows John of Ephesus, with no stretching. I hunted hardest for the recurring faults of earlier batches: witness swaps (an editor's note given to the ancient writer, or one witness's fact given to another, here Facundus against the anonymous book on church writers against Victor of Tunnuna), a modern year told as an ancient writer's, a contested point told as settled, absence claims a held file contradicts, namesakes merged (Julian against Julian of Halicarnassus, who sits on the same page of Michael the Syrian; Benedict against the other Benedicts), and pronouns that blur Julian and John of Ephesus. I did not edit the drafts. I made no paid or model-API calls and used no web. Readability and quote search ran on local scripts only.

Profiles: `julian-missionary-to-the-nobadae` (major), `ferrandus-of-carthage` (not major), `benedict-of-nursia` (major), their entries in `records.json`, and the batch `README.md`. Files are in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch2/`. Brief line numbers refer to the `.brief.txt` files, where each paragraph is one line and blank lines count (paragraphs sit on l.1, 3, 5, 7, 9, 11, 13). Other line numbers point to files under `cic/texts/`.

Method. I searched every quotation in the three briefs and cards in the vendored file the card or records cite, with tags stripped, whitespace collapsed and quote marks normalised; for the OCR files (Payne Smith's John of Ephesus, Chabot's Michael the Syrian, Migne PL 65, 67 and 83, Mommsen's Chronica minora, Gardner's Gregory, Gasquet's Rule) I read each passage by line number and searched tolerantly. I read each hit in context to see who is speaking: the ancient author, a document he quotes, a translator's preface or footnote, a Migne note, or an editor's notitia. I checked every factual sentence of each brief against its passage and compared each `records.json` entry with its brief and card. Before accepting any absence or closed-list claim I searched `cic/texts/` for other held files on the person. This found Bar Hebraeus's Chronicon ecclesiasticum (Abbeloos and Lamy, vol. 1) retelling Julian's mission, and Faustino Arevalo's Isidore (PL 83), which prints the "anonymous" notice of Ferrandus as a chapter of Isidore's own book. Readability came from `engine.m1.gates.grade_text`, run from the repo root. Every suggested brief fix below was applied to a scratch copy and re-scored.

### Applies to all three

- **Audio = brief.** Each audio script matches its brief exactly once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, before the closing line. No tag appears in any brief or card.
- **Readability.** All three pass (FK at most 10, Flesch at least 60). Ferrandus sits nearest the floor (Flesch 61.7). Narrator sentences past 25 words: Julian l.3 (28 words, see M1) and Ferrandus l.3 (27 words, see M6). Julian l.1 (28) is mostly the quoted threat.
- **Length.** Julian is at the cap (402 words, 2:29) and Benedict on it (405, 2:30). Ferrandus is at the non-major ceiling (325, 2:00). Every `briefLength` matches.
- **Card order.** All three follow Mark's order. Missing fields are left out (Julian has no keyWorks and no "Their own words", which is right: no word of his is held beyond what John reports). keyWorks never goes past three. Each `uncertain` list opens with the brief's main caveat.
- **Tradition names.** "Nubian Christianity", "Latin African Christianity under Byzantium" and "Early Benedictine / Italian Monasticism" are the census names in `cic-website/data/world-census.json`.
- **Who test (item 14).** Julian is the founding teacher of the Nobadae's church in John's account ("their teacher"); the scan marks STORY as a fair alternative, and the coordinator holds him WHO. Ferrandus has his letters and the Breviatio canonum. Benedict has his Rule. The drafts carry no list lines; those belong to the map build and were not checked here.

| Profile | Words | Est. length @162 | FK | Flesch |
|---|---|---|---|---|
| Julian, missionary to the Nobadae (major) | 402 | 2:29 | 7.1 | 70.0 |
| Ferrandus of Carthage | 325 | 2:00 | 8.3 | 61.7 |
| Benedict of Nursia (major) | 405 | 2:30 | 7.0 | 71.5 |

---

### 1. Julian, missionary to the Nobadae

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS, apart from B1 |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL, minor (M1 pronouns and a 28-word sentence; M2 a repeated close) |
| 5 | No role for a witness | PASS (John, Payne Smith, Michael the Syrian named) |
| 6 | Partisan witness named and marked | FAIL, blocking (B1) |
| 7 | Contested both sides | PASS (nothing contested is told) |
| 8 | Common names placed | PASS (Theodosius of Alexandria; Theodore, an old bishop from the Thebais; the card's name gives his role, which keeps him apart from Julian of Halicarnassus) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS on scene and story; length see M2 |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS on order and caveat; card minor (M3) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (judgment call, as the scan says) |

**Quotes and close tellings** (`john-of-ephesus_ecclesiastical-history-part3_paynesmith1860.txt`, John speaking unless said)
- Theodora's letter (l.1): "your life shall answer for it; for I will immediately send and take off your head" (l.12821-12823; the OCR closes the quote with "?"). "both his majesty and myself have purposed to send an embassy to the people of the Nobadæ, and I am now despatching a blessed man named Julian; and further my will is, that my ambassador should arrive ... before his majesty's" (l.12811-12816). The duke: "You must wait a little, while we look out and procure beasts of burden, and men who know the deserts" (l.12825-12827). Faithful.
- Julian and Justinian (l.3): "a presbyter named Julianus, an old man of great worth, who conceived an earnest spiritual desire to christianize the wandering people who dwell on the eastern borders of the Thebais beyond Egypt" (l.12755-12759); "when the king heard that the person she intended to send was opposed to the council of Chalcedon, he was not pleased, and determined to write to the bishops of his own side in the Thebais, with orders for them to proceed thither and instruct them" (l.12776-12779, 12798). Faithful.
- Payne Smith (l.5): "he was a Monophysite: and though his party ... yet they refused to receive the council of Chalcedon" (translator's preface, l.286-290). "he" there is John. Michael the Syrian: "Le récit est abrégé de Jean d'Asie ou d'Éphèse, H. E., IIIe part., iv, 6" (Chabot's note 3, `michael-the-syrian_chronique-tome2-livres-viii-xi-fra_chabot1901.txt` l.20293). The brief's "shortens" is Chabot's finding, told plainly; the card names Chabot. Acceptable.
- The Nobadae (l.7): "received them with pleasure" (l.12866-12867); "utterly abjured the error of their forefathers" (l.12881-12882); Theodosius "being required to receive the council, and having refused, was ejected by the king from his throne" (l.12890-12892); "we shall walk after the example of pope Theodosius" (l.12922-12923). Faithful. John also says Julian's party "instructed them how they should receive them, and what answer they should give" before the emperor's envoy came (l.12900-12901). The brief leaves this out. It is not a finding, since nothing told is wrong, but it is the one place where John shows his own side's hand.
- The caves (l.9): "he used to say that from nine o'clock until four in the afternoon he was obliged to take refuge in caverns, full of water, where he sat undressed and girt with a linen garment, such as the people of the country wear" (l.12934-12938). Theodore: "a bishop from the Thebais, an old man, named Theodore" (l.12943-12944); "a certain Theodore, a very old man, and bishop of the city called Philæ" (iv.49, l.15453-15454). Faithful. The "bishop Theodore of Phyle" of footnote e (footnote e, l.12948) is Payne Smith's; the brief rightly rests "bishop of Philae" on John's iv.49.
- Return, death and Longinus (l.11, 13): "arrived in safety at Constantinople, where he was most honourably received by the queen" (l.12965-12967); "the blessed Julian their teacher had died but a very short time before, and also because her late majesty, the queen Theodora, had given orders that the excellent Longinus should be made bishop there" (l.12977-12982); Longinus "a priest" (l.12742). "taught both the king and his princes, and most of the tribes in his dominions, for a period of two years" (iv.49, l.15450-15452). Exact.
- "John gives no year for any of it." Checked: the years in the file near these chapters are Payne Smith's (footnotes, preface) or belong to later chapters (iv.11-12, A.D. 575 onward). John gives only relative time ("eighteen years, more or less", l.15477). True.
- "All that is known of Julian comes from John." Michael the Syrian (above) and Bar Hebraeus (`barhebraeus_chronicon-ecclesiasticum-vol1-lat_abbeloos-lamy1872.txt` l.14057-14188, "presbyter quidam orthodoxus, nomine Julianus, Constantinopoli ministerio addictus papae Theodosii Alexandrini") retell the same story centuries later. Neither is an independent early witness, so the brief's sentence stands; the card and records should still name Bar Hebraeus (M3).
- Card: "the blessed Julian their teacher" (l.12978) exact. Michael says "retourna à la ville impériale. Il y mourut." (Chabot l.20410-20411), as the card says. Michael's dating to the twelfth century is the file header's (l.1-2, 1126-1199).
- The pronoun hunt. Every "he" in the brief was read against the nearest names. The faults are B1 (l.5) and M1 (two in l.3). The rest are clear: l.9 "He used to say" and l.11 "He died" follow "Julian" as subject; l.13 "He says that Julian taught" names Julian.

**Length (the coordinator's question).** John's account is four chapters (iv.6-8 and 49) and is rich: the letter, the duke's trick, the conversion, the refusal, the caves, the return, Longinus. The brief carries all of it without invention, and most of its 402 words are John's. The one stretch is the close (M2), which repeats l.9. With M1 and M2 applied the brief runs 378 words (2:20), which is the length John's material gives.

**Findings**
- **B1 BLOCKING (items 6, 4; the partisan witness's marking can be heard as the translator's).** Brief l.5: "John's English translator, Payne Smith, notes that he belonged to the party that refused Chalcedon, and John tells the story from Julian's side." The subject of the clause is Payne Smith, so "he" is first heard as Payne Smith, which is wrong (an Anglican translator, not a Monophysite). It can also be heard as Julian, who did oppose Chalcedon (l.12776-12777), which loses the point of the sentence. This is the brief's one placing of its partisan witness, and as written a listener cannot tell whom it marks. Payne Smith's line is about John (l.286-290). Fix: "John's English translator, Payne Smith, notes that John belonged to the party that refused Chalcedon, and John tells the story from Julian's side." Scored: 402 words, FK 7.1, Flesch 70.0.
- **M1 MINOR (item 4; pronouns between Julian, John and Justinian, and a long sentence).** Brief l.3: "He longed to make Christians of this people, John says. He took the plan to Theodora." The second "He" comes straight after "John says". And: "Justinian disliked it, John writes, because Julian opposed the Council of Chalcedon, and he told bishops of his own side in the Thebais to go and teach them." (28 words) Here "he" sits after "Julian" and can be heard as Julian sending bishops of his own side. Fix: "John says Julian longed to make Christians of this people and took the plan to Theodora. Justinian disliked it, John writes, because Julian opposed the Council of Chalcedon. So the emperor told bishops of his own side in the Thebais to go and teach them."
- **M2 MINOR (items 4, 10; a close that repeats, the one stretch).** Brief l.13: "He says that Julian taught 'both the king and his princes, and most of the tribes in his dominions, for a period of two years.'" l.9 has already told the two years and the baptism of "the king, his nobles and many people"; the close adds only "most of the tribes". It reads as a beat line. Fix: end on the line before it, and move `[warmly]` there in the audio: "Afterwards a priest named Longinus was made bishop for the Nobadae, as Theodora had ordered. [warmly] John calls Julian "their teacher."" (In the brief, without the tag.)
- **M3 MINOR (card `uncertain` 3; records).** "The race between the empress's envoy and the emperor's is told only by John". Michael the Syrian tells it (Chabot l.20280-20354), and so does Bar Hebraeus (l.14150-14172), both after John. The card's item 1 already says Michael's is shortened from John's, so the sense is right but the words are not. Fix: "The race between the empress's envoy and the emperor's is John's story, told as an episode of the empress's craft; Michael the Syrian and Bar Hebraeus retell it after him. No held source tells it from the emperor's side." Records `absent_details` "A second, independent witness": add "Bar Hebraeus's Chronicon ecclesiasticum retells the mission (barhebraeus vol1 l.14057-14188); it is later and adds that Julian served Theodosius at Constantinople." Card `sources.about` may add the Bar Hebraeus file if the card names him.

With B1, M1 and M2 applied (scratch copy): 378 words (2:20), FK 7.2, Flesch 68.6, no narrator sentence past 25 words.

---

### 2. Ferrandus of Carthage

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS, apart from B2 |
| 2 | Quotes verbatim | PASS (no quotation in the brief; card Latin checked) |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL, minor (M5 pronoun; M6 a 27-word sentence) |
| 5 | No role for a witness | FAIL, minor (M4 "its editor") |
| 6 | Partisan witness named and marked | PASS (l.3: Facundus "writes as a partisan") |
| 7 | Contested both sides | FAIL, blocking (B2); the Life of Fulgentius PASS |
| 8 | Common names placed | PASS (Pelagius and Anatolius as deacons of Rome; Facundus of Hermiane; Theodore of Mopsuestia; Theodoret of Cyrrhus; Ibas of Edessa; Fulgentius of Ruspe; Victor of Tunnuna; Isidore of Seville) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:00) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS on order and caveat; sources part of B2 |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Witness by witness** (`facundus-ferrandus-caesarius-dionysius-pl67-lat_migne1865.txt` unless said)
- Facundus (l.1, 13): "venerabiles Pelagius et Anatolius, Romani diaconi ... laudabilis in Christo memori[ae] Ferrando Carthaginiensi diacono scripserunt, ut habito de hac causa diligenti tractatu, cum reverendissimo ejusdem Ecclesiae Carthaginiensis episcopo ... consulentibus respondere" (l.49119-49126). The book "ad Justinianum imperatorem" (l.41866), its preface naming the letter of Ibas "quam ... memorata synodus catholicam judicavit", Theodore of Mopsuestia "ejusque doctrina", and "quaedam Theodoreti Cyrri episcopi scripta" (l.41872-41880). Facundus is given only what Facundus says. Hermiane "in Africae provincia Byzacena" is a Migne note (l.41891); the brief's "an African bishop" is an identifier and adds no claim.
- The question about the dead (l.5): "Ferrandus, inquit, ad Pelagium et Anatolium Romanos diaconos consulentes eum, utrum liceat quemquam damnare post mortem, edidit rescriptum" (the note on Facundus, l.49143-49147; Gallandi l.68268-68273). Rightly given to the book on church writers, not to Facundus. On whether that book is anonymous, see B2.
- Ferrandus (l.5): "Quae autem finiuntur judicantibus episcopis sanctis ... sequenda sunt, amplectenda sunt: in retractatione ... teneri non debent" (Letter VI, l.71428-71433); "Quid prodest cum dormientibus habere certamen" (l.71436-71437); "cui si Deus indulgentiam dedit, nihil nocet nostra severitas; si supplicium praeparavit, nihil prodest nostra benignitas" (l.71449-71451). Faithful paraphrase. (In the letter the last two clauses are said of a man who died before his case was tried, inside the Church; the brief's "a man" is a fair shortening.) The heading "Pro epistola Ibae episcopi Edesseni, adeoque pro tribus capitulis" (l.71089-71090). That the letter survives: Gallandi says Chifflet published it from two manuscripts, after Baronius had thought it lost (l.68297-68303).
- Fulgentius (l.7): "absentem magistrum frequentibus epistolis compellare" (Letter II, l.68761); Epistola XI heading "de salute Aethiopis catechumeni, baptizati cum jam vi morbi esset mentis impos, ac non percepta eucharistia mortui" (`fulgentius-ruspe_opera-contra-arianos-pl65-lat_migne1847.txt` l.24760-24763). Faithful.
- The Life (l.9): the author "ad suscipiendam professionem monachorum conversus, in illo parvissimo monasterio quod sibi apud Sardiniam pro Christi nomine relegatus effecerat" (pl65 l.7991-7994). The Migne note: "P. Chiffletio aliisque videtur quod a Ferrando ... in praefatione ad opera Fulgentii Ferrandi Divione edita anno 1649. Alios tamen haec non convincunt, cum Vitae auctor videatur a latere Fulgentii non discessisse" (pl65 l.7961-7966). Gallandi on Noris: "At haec accepisse haud potuit V. C. nisi ab auctore Vitae sancti Fulgentii; ea enim nuspiam alibi legas" (l.68658-68659, running across the column). Both sides named; told in place. PASS.
- Victor and the year (l.13): "546 POST CONSVLATVM BASILI V. C. ANNO VI. 1. Ferrandus Carthaginis ecclesiae diaconus clarus habetur" (`chronica-minora-2_...mommsen1894.txt` l.18987-18989; OCR "ccclesiae", "habctur"). The 546 is Mommsen's margin, and the brief says it is the editor's. Gallandi: "id unum compertum habemus, eum jam diem obiisse anno 547, quo Facundus ... scripsit ... Ferrandum 'laudabilis in Christo memoriae' virum appellat" (l.67899-67905). Faithful; no modern year is given to Victor.
- Card: Pagi and Natalis Alexander "absque testibus" (l.67894-67895); Chifflet's "aut exsul ... aut intra domesticos parietes moerore confectus occubuerit" (l.68323-68325); the kinsman guess "aut affinem fuisse aut consanguineum ... pene persuadet" (l.67841-67848); Pithou, Miraeus, Christianus Lupus and Natalis Alexander for, Noris, Pagi, Mangeant and Fontanini against, Gallandi's reading that Noris changed his mind, and the Life printed after "indubiis Ferrandi epistolis" (l.68589-68681); Breviatio "quo anno ... plane incompertum habemus" (l.68565-68566); Letter VII "Qualis esse debeat dux religiosus in actibus militaribus, seu de septem regulis innocentiae" (l.71562-71563); Letters IV, V and the second Letter II to Eugippius, Severus "scholasticum Constantinopolitanum" and Anatolius "De duabus in Christo naturis" (l.70149-70150, 70283, 68767-68771). All faithful.

**Findings**
- **B2 BLOCKING (items 1, 7; a disputed attribution told as settled, with a held file on the other side).** Brief l.5: "A short anonymous book on church writers, printed with Isidore of Seville's, says the Romans asked whether a man may be condemned after his death." Card `legacy.traces` 1 says the same ("a short anonymous book on church writers printed with Isidore of Seville's"), and the records witness reads "The anonymous book on twelve church writers usually attached to Isidore". That the book is anonymous is Gallandi's view ("incertus auctor libelli de xii Scriptoribus ecclesiasticis, qui Isidoro Hispalensi et Ildefonso Toletano subjici solet", l.68268-68270) and Miraeus's. Two held lines give it to Isidore. Gallandi himself reports that Baronius "Isidoro Hispalensi ascribit" (l.68296-68297). And Faustino Arevalo's edition of Isidore (`isidore-seville_sententiae-eccl-officiis-historia-gothorum-pl83-lat_migne1860.txt`, title page l.399) prints the Ferrandus notice as chapter 11 of Isidore's own De viris illustribus (l.121206-121208, with the quotation at l.121279-121290), puts "Hactenus Isidorus" only after chapter 46 (l.120536), and answers Miraeus's doubt about the first twelve chapters (l.120512-120523). Fixes:
  - Brief l.5: "A short book on church writers, printed with Isidore of Seville's works, says the Romans asked whether a man may be condemned after death." Scored with this fix alone: 324 words (2:00), FK 8.2, Flesch 62.4.
  - Card `legacy.traces` 1: "His letter to Pelagius and Anatolius was quoted in a short book on church writers printed with Isidore of Seville's works. Gallandi calls its author unknown; Baronius, as Gallandi reports, and Faustino Arevalo, Isidore's editor, give it to Isidore. Gallandi says the quotation there is cut and corrupt, and gives it from the letter."
  - Card `sources.about`: add "De viris illustribus, chapter 11 (ed. Faustino Arevalo)", author Isidore of Seville, or an unknown author, Latin, `cic/texts/isidore-seville_sententiae-eccl-officiis-historia-gothorum-pl83-lat_migne1860.txt`.
  - Records: the claim's witness becomes "The book on church writers printed with Isidore of Seville (PL 83 l.121206-121290, as chapter 11 of Isidore's De viris illustribus in Arevalo's edition), quoted in a Migne note (pl67 l.49143-49150) and by Gallandi (l.68268-68291)"; add a `contested_claim`: "The book's author" — For anonymous: Gallandi (l.68268-68270, 68287), Miraeus as Arevalo reports him (pl83 l.120512-120514). For Isidore: Baronius as Gallandi reports him (l.68296-68297); Arevalo's edition (pl83 l.120512-120536, 121206).
- **M4 MINOR (item 5; a role for a named witness).** Brief l.13: "in the year its editor gives as 546". The card names him (Theodor Mommsen). Fix: "in the year Theodor Mommsen, its editor, gives as 546".
- **M5 MINOR (items 4, 7; a pronoun that leans toward settling the Life's authorship).** Brief l.9: "Whether he wrote the Life of Fulgentius is disputed. Its author says he became a monk in the small monastery Fulgentius built in exile in Sardinia." Coming after "Whether he wrote", the second "he" is first heard as Ferrandus, which would tell as fact that Ferrandus became a monk there. That rests only on the Life, if it is his (records tag it Inferential-Thin, and Gallandi says the author speaks only of himself, "de Ferrando nihil, omnia vero ista de se ipso prolocutum", l.68667-68668). Fix: "Its author says that he himself became a monk in the small monastery Fulgentius built in exile in Sardinia."
- **M6 MINOR (item 4; length).** Brief l.3: "These were Theodore of Mopsuestia and his teaching, some writings of Theodoret of Cyrrhus, and a letter of Ibas of Edessa that the council had judged sound." (27 words.) Fix: "These were Theodore of Mopsuestia and his teaching, and some writings of Theodoret of Cyrrhus. The third was a letter of Ibas of Edessa that the council had judged sound."

With B2, M4, M5 and M6 applied, the brief runs 331 words. To hold about 2:00, delete l.7's "He made a short digest of church laws as well." (the card's `keyWorks` holds the Breviatio, and the pattern does not repeat card facts as a list). Scored on a scratch copy: 321 words (1:59), FK 8.3, Flesch 61.5, no narrator sentence past 25 words.

---

### 3. Benedict of Nursia

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, minor (M7) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Gregory, Edmund Gardner, Francis Gasquet named) |
| 6 | Partisan witness named and marked | PASS (l.3: "a book of miracles, written to honour a saint"; card `uncertain` 1) |
| 7 | Contested both sides | PASS (the date he left Rome is on the card as Gardner's "disputed") |
| 8 | Common names placed | FAIL, minor (M8 "Saint John"); Benedict himself PASS ("Benedict of Nursia" at first mention in brief and card) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:30) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS; card part of M7 |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes and close tellings** (`gregory-great_dialogues_gardner1911.txt`, Gregory in the 1608 English, unless said)
- Subiaco (l.1): "a desert place called Sublacum, distant almost forty miles from Rome" (l.3489-3490); "lived there in a strait cave, where he continued three years unknown to all men, except to Romanus ... from the top thereof, upon a long rope, did let down the loaf, upon which also with a band he tied a little bell, that by the ringing thereof the man of God might know when he came with his bread" (l.3500-3512). "The devout and religious youth Bennet" (l.3455-3456). Faithful.
- The witness (l.3): "All the notable things and acts of his life I could not learn; but those few ... I had by the relation of four of his disciples" (l.3427-3430), naming Constantinus, Valentinianus, Simplicius and Honoratus (l.3436-3441). "were written in 593" is Gardner's introduction (l.1022-1025), and the brief gives it to Gardner. Honoratus "saith not that he received it from his own mouth, but that he had it of other monks" (l.4505-4507), as card `uncertain` 1 says.
- Birth and Rome (l.5): "born in the province of Nursia, of honourable parentage, and brought up at Rome in the study of humanity. But for as much as he saw many by reason of such learning to fall to dissolute and lewd life ... giving over his book, and forsaking his father's house" (l.3413-3422). Faithful. Gardner: "born at Nursia about 480. The date of his leaving Rome is disputed; it was probably a few years before 500" (l.12628-12630). Gasquet: "born at Nursia, a city of Umbria, in the year 480" (`benedict_rule-of-saint-benedict_gasquet1925.txt` l.172-173). See M7.
- The poisoned wine (l.7): "they agreed to poison his wine ... he, putting forth his hand, made the sign of the cross, and straightway the glass ... brake in pieces" and "Go your ways, and seek ye out some other father suitable to your own conditions" (l.3681-3697). Exact. "he returned back to the wilderness which so much he loved" (l.3699-3706); "he built there twelve Abbeys ... and in each of them placed twelve monks" (l.3847-3849). Faithful.
- Cassino (l.9): "Cassino, standeth upon the side of an high mountain ... the foolish and simple country people ... worshipped the god Apollo ... beat in pieces the idol ... built the oratory of St. Martin, and where the altar of the same Apollo was, he made an oratory of St. John" (l.4167-4182). Gardner: "founded the great Abbey of Monte Cassino in 528 or 529" (l.12691-12692). Faithful.
- The Rule (l.11): Gregory, "he wrote a rule for his monks, both excellent for discretion and also eloquent for the style" (l.5566-5567); Gasquet's Rule, "Listen, my son, and turn the ear of thine heart to the precepts of thy Master" (l.626-627), "a school for the service of God, in which we hope nothing harsh nor burdensome will be ordained" (l.768-770), "at specified times in manual labour, and at other fixed hours in holy reading" (ch. 48, l.3113-3115), "Let all guests who come be received as Christ would be" (ch. 53, l.3309), "this little Rule written for beginners" (ch. 73, l.4299). All exact.
- Death (l.13): "having his weak body holden up betwixt the hands of his disciples, he stood with his own lifted up to heaven, and as he was in that manner praying, he gave up the ghost" (l.5588-5591); he "told the day of his holy death to his monks" (l.5578-5579); "the holy man could not otherwise teach, than himself lived" (l.5571). Gardner: "According to the tradition ... St. Benedict a month later, March 21, 543" (l.12777-12779); Gasquet, "according to the tradition of the Benedictine Order, on March 21, 543" (l.202-203). Exact; no year is given to Gregory.
- Namesakes: nothing from Benedict of Aniane, Benedict Biscop or Pope Benedict I is in the profile. The records' note that "no held editor gives 547" was checked: Gardner, Gasquet and Hunter Blair give 543 or no death year; 547 is only in the Library's file headers. True. (Hunter Blair's preface dates the Rule "About 535 a.d.", `benedict_rule-of-st-benedict-lat-eng_hunter-blair1907.txt` l.150. The profile does not date the Rule, so this is not a finding; it may go on the card beside Gasquet's "probably" if wanted.)

**Findings**
- **M7 MINOR (item 1; a date given more loosely than one witness gives it).** Brief l.5: "Gardner and the editor Francis Gasquet give his birth as about 480." Card `dates`: "Born about 480 ... as Edmund Gardner and Francis Gasquet give it." Gardner says "about 480" (l.12628); Gasquet says "in the year 480" (l.172-173). The records claim quotes Gasquet correctly. Fix, brief: "Gardner gives his birth as about 480, and the editor Francis Gasquet as 480." Card `dates`: "Born, by Edmund Gardner, about 480, and by Francis Gasquet in 480; died, by the tradition of his order, in 543, as both give it."
- **M8 MINOR (item 8; a common name).** Brief l.9: "built chapels to Saint Martin and Saint John." Gregory identifies the second when he tells the burial: "Buried he was in the oratory of St. John Baptist which himself built, when he overthrew the altar of Apollo" (l.5612-5613). Fix: "built chapels to Saint Martin and Saint John the Baptist." To hold the cap with M7, cut l.9's "on a high mountain," (Gregory's detail; the brief does not need it).

With M7 and M8 applied and that cut (scratch copy): 405 words (2:30), FK 7.0, Flesch 71.2.

---

### README

Compared with `era3/batch1/README.md` and checked against `Who_Scan_Era3.md` and `2026-11-12_who-scan-dedupe/Removed_Rows.md`. The shape matches batch 1 (ids, the order and its source, rescored rows, the major marks with who confirmed them, names, card traditions, the file table). The years given for each person match the scan's rows (Joshua fl. c.507, John Rufus fl. to c.515, Brigid 518 or 521, Zachariah after 536, Severus 538, Caesaria before 542, Caesarius 542, Julian fl. c.543-c.545, Ferrandus d. c.546, Benedict c.547; Vahan c.505 and Kaleb to c.540). `records.json` has all ten keys. "'Nobadia' is in no held file" is true (searched `cic/texts/`). "Julian has no place in any held source" is true of a place-name for him; Bar Hebraeus says only that he served Theodosius at Constantinople (l.14057-14059), which is not an epithet.

- **M9 MINOR (the order; a skipped row not named).** Batch 1's README names the live person entries it skipped ("Patrick and Peter the Iberian fall in the same years and are skipped as live person entries"). Batch 2's says "None is a live person entry" but does not say one was skipped. Simeon of Beth Arsham, "fl. c.510-c.530", is a WHO row marked "person entry (live)" (`Who_Scan_Era3.md` row 41) and falls by that order between Brigid of Kildare (518 or 521) and Zachariah Rhetor (after 536). He is not in `Removed_Rows.md`. Fix, after "None is a live person entry or was written before.": "Simeon of Beth Arsham (about 530) falls in the same years and is skipped as a live person entry."

---

Totals, part C: 2 blocking (B1 `julian-missionary-to-the-nobadae`; B2 `ferrandus-of-carthage`) and 9 minor (M1-M3 `julian-missionary-to-the-nobadae`; M4-M6 `ferrandus-of-carthage`; M7-M8 `benedict-of-nursia`; M9 README). Every fix above was checked against the line it cites, and every brief fix was scored on a scratch copy: Julian 378 words (2:20), Ferrandus 321 (1:59), Benedict 405 (2:30), each with FK at most 10 and Flesch at least 60.
