# R1 review: era 3 batch 2, part A (Church Family Tree Who profiles)

Reviewer: independent, first sight of these drafts (branch `who-profiles-era3-batch2`). Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; Mark's length rulings as the batch 1 review applies them (majors capped at 2:30, about 405 words, a cap and not a target; non-majors 1 to 2 minutes, at most about 324 words). I hunted hardest for the recurring faults of earlier batches: witness swaps, a modern year told as an ancient writer's, a contested point or an identification told as settled, absence claims a held file contradicts, two people of one name merged, common names without a place, and AI tells. I did not edit the drafts. I made no paid or model-API calls and used no web. Readability and quote search ran on local scripts only.

Profiles: `joshua-the-stylite`, `john-rufus`, `zachariah-rhetor` and `severus-of-antioch` (major), with their cards, audio scripts and entries in `records.json`. Files are in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch2/`. Joshua and Zachariah are Whos as recorders. Brief line numbers refer to the `.brief.txt` files, where each paragraph is one line and blank lines count (paragraphs sit on l.1, 3, 5, 7, 9, 11, 13). Other line numbers point to files under `cic/texts/`.

Method. I searched every quotation in the four briefs and cards in the vendored file the card or records cite, with a script that collapses whitespace, normalises quote marks, folds accents and lets letters be split by OCR spacing. For the OCR files (Wright's Joshua, Nau's Plerophories, Kugener's Lives of Severus, Raabe's Peter the Iberian, Hamilton and Brooks's Zachariah, Brooks's Severus letters) I read each passage by line number. I read each hit in context to see who is speaking: the ancient author, a document he quotes, a later compiler, a translator's preface, a footnote, or a bracket the translator supplied. I checked every factual sentence of each brief against its passage and searched the Library before accepting each absence claim or each attribution a modern editor might since have revised. I compared each `records.json` entry with its brief and card. Readability came from `engine.m1.gates.grade_text`, run from the repo root. Length assumes 162 words a minute. Every suggested brief fix below was applied to a scratch copy and re-scored; the post-fix word count and scores are given with each profile.

## Applies to all four

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

## 1. Joshua the Stylite

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
- The copyist's note (l.5): "the priest Mar Yêshûa (Joshua) the stylite, from the convent of Züknin, who wrote this Chronicle of the evil times that are past" (l.388–391). Exact. The note follows "Pray for the wretched Elisha, from the convent of Züknin (near Amid), who wrote this leaf" (l.360–361); "(near Amid)" is Wright's bracket. Wright's footnote puts the leaf "in the handwriting of Elisha of Züknin" (l.370–371). "Of Joshua we know little more than what he has himself thought fit to tell us" (l.335–336). Faithful.
- Dates (l.7): ch. C, "On the 28th of the month of the latter Teshri (November A.D. 506)" (l.4361–4362); the year is Wright's bracket, and the brief says so. Wright's preface: "The last date which occurs in it is 28th November A.D. 506… I have thought myself justifed in assigning the composition of the work to that winter and the earlier part of the following year, which is also Noeldeke's opinion" (l.337–344). See M2.
- "I am a plain man in speech… testify to be true" (l.9): ch. IV, l.598–600, after "But"; exact. "these chastisements… sent upon us for our sins" (l.605–608). Faithful.
- "if I remain alive" (l.13): ch. CI, l.4405–4406; "offer up prayer constantly on behalf of me" (l.4401–4402). Exact.
- Card: "it is generally acknowledged to be one of the most valuable authorities for the period with which it deals" (l.166–168), the Assemani and Martin history (l.162–173), Martin's title "écrite vers l'an 515" (l.197–198), the single Vatican manuscript (l.292–300). Exact. "Josue Stylites" is Assemani's running head (`assemani_…tomus1…1719.txt` l.58666, 58999). Card `uncertain` 4: Wright's two notes say "perhaps Dionysius" (l.364–365) and "probably from the pen of Dionysius" (l.4423–4424); "probably" stands.

**Findings**
- **B1 BLOCKING (items 1, 7; a superseded attribution told as settled, which held files contradict).** Brief l.11: "It survived because a later historian, Dionysius of Tell-Mahre, copied it into his own larger work." Wright says so in 1882: "We owe the preservation… to the care of a later historian, Dionysius of Tell-Mahré… patriarch of the Jacobites (ob. … A.D. 845), who incorporated it with his own larger work… The solitary manuscript… is preserved in the Vatican Library" (l.292–297), cited as Vatican "no. CLXII" (l.305–306). Two held scholars name that same compiler otherwise. Nau, in the Didascalie of Jacob in the same PO 8 volume the batch cites for John Rufus, prints an extract from "Pseudo-Denys, Vatican, ms. syr. 162" and says "le Pseudo-Denys écrivait en l'année 1086 des Grecs (775 de notre ère)" (`po08_john-rufus-plerophories-and-others-fra_1912.txt` l.48221–48226; also "le pseudo-Denys… avant l'année 773, dans sa compilation", l.438–439). Brooks calls him "the so-called Dionysius" (`john-ephesus_lives-eastern-saints-po17_brooks1923.txt` l.714). Chabot, introducing Michael the Syrian, separates "la chronique authentique de Denys de Tell-Mahré", which "est perdu, à l'exception d'un seul chapitre" (`michael-the-syrian_chronique-tome1-livres-i-vii-fra_chabot1899.txt` l.63096–63099). A writer of 775 cannot be the patriarch who died in 845. The narrator tells Wright's attribution as fact. The card repeats it, attributed to Wright but with no word that it was given up: `legacy.traces` 1 ("Dionysius of Tell-Mahre, a later patriarch and historian, copied it") and `uncertain` 4 ("probably by Dionysius of Tell-Mahre"). The records claim "Preserved by Dionysius of Tell-Mahré" is tagged Widely Accepted.
  - Fix, brief l.11 (with M3): "Wright says it is generally counted among the most valuable sources for its time. It survived inside a later Syriac chronicle, whose compiler Wright took for the patriarch Dionysius of Tell-Mahre. François Nau, a later French scholar, calls him the Pseudo-Dionysius, writing in 775."
  - Card `legacy.traces` 1: "The Chronicle survives inside a later Syriac chronicle, held in a single Vatican manuscript. Wright took its compiler for the patriarch Dionysius of Tell-Mahre; François Nau calls him the Pseudo-Dionysius, writing in 775, and E. W. Brooks 'the so-called Dionysius'." Card `uncertain` 4: "…a later addition, probably by the compiler Wright took for Dionysius of Tell-Mahre." Add to `uncertain`: "Who copied the Chronicle: Wright names Dionysius of Tell-Mahre, who died in 845; Nau dates the compiler to 775 and calls him the Pseudo-Dionysius." Add Nau (po08, Didascalie of Jacob) and Brooks (PO 17) to `sources.about`.
  - Records: the claim becomes Wright's, tagged Contested, with a `contested_claim` ("Who compiled the chronicle that preserves Joshua": Wright l.292–297 against Nau po08 l.48221–48226, Brooks PO 17 l.714, Chabot l.63096–63099).
- **M1 MINOR (item 8).** Brief l.3, first mention: "He wrote it for Sergius, a priest and abbot". Sergius is a common name, and Wright gives the place: "Sergius, the abbot of a convent in the district of Edessa" (l.334–335). The card's first mention (`keyWorks` 1, "Sergius, priest and abbot") has the same gap. Fix, brief l.3: "He wrote it for Sergius, a priest and abbot near Edessa." Card: "written for Sergius, priest and abbot of a convent near Edessa, …".
- **M2 MINOR (item 1).** Brief l.7: "places the writing in that winter and the next spring." Card `dates`: "that winter and the next spring". Wright says "that winter and the earlier part of the following year" (l.341–342); "spring" narrows it. Fix, brief: "He and the German scholar Theodor Noeldeke place the writing in the months after." Card: "that winter and the early part of the next year".
- **M3 MINOR (item 1).** Brief l.11: "Wright counts the Chronicle among the most valuable sources for its time." Wright reports a general judgment: "it is generally acknowledged to be" (l.166–167). The card keeps his words. Fix: "Wright says it is generally counted among the most valuable sources for its time." (in the B1 fix).
- **M4 MINOR (items 1, 4).** Brief l.3: "the war between the Greeks and the Persians." "Greeks" is Wright's rendering; his note says the Syriac word is "literally, the Romans", used for the Byzantine Greeks (l.448–450). A listener hears Greece. Fix: "the war between the Romans and the Persians."
- **M5 MINOR (item 4).** Brief l.3: one narrator sentence of 32 words ("He wrote it for Sergius… and the Persians."). Fix (with M1, M4): "He wrote it for Sergius, a priest and abbot near Edessa. Sergius had asked him for a record of the locusts, the famine and plague, and the war between the Romans and the Persians."
- Length with B1 and M1 to M5: the fixes add words. Suggested cuts: delete l.5's opening "Wright says we know little more of Joshua than he chose to tell." (card `uncertain` 1 holds it), l.9's "Joshua says plainly why he wrote.", and "near Amid" after Zuknin in l.5 (the card's `place` keeps it). Scored: 323 words (2:00), FK 6.6, Flesch 74.9.

---

## 2. John Rufus

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
- The scene (l.1): ch. XVI, "Quand je demeurais à Jérusalem, je suivis un jour la route qui conduit de Siloe, par la vallée… l'un des notables de la ville… je vis au pied de la montagne… un grand monastère devenu vieux et tombant en ruines" (l.2068–2073); "avec un visage souriant… C'était le monastère de Juvénal… quand le concile de Chalcédoine eut lieu, (ce monastère)… devint désert" (l.2116–2123); "Juvénal a été le compagnon de Judas, comme l'a dit de lui le bienheureux Dioscore" (l.2126–2128). Faithful; the speaker is John in the first person.
- Nau's life (l.3, 5, 7): "Il se nommait Jean, était Arabe du Sud de la Palestine, sans doute d'Ascalon ; il a étudié le droit à Beyrouth… ordonné prêtre à Antioche (476 à 478) par le patriarche Pierre le Foulon dont il avait été syncelle. Il a quitté cette ville quand le patriarche Pierre en a été chassé… où il a connu… Pierre l'Ibère, évêque monophysite de Maiouma, près de Gaza" (l.359–368); "rédigés en grec peu après l'année 512" (l.435), "pendant que Sévère était patriarche d'Antioche (512-518)" (l.376–377); 89 chapters (l.305–306); "La plupart des histoires proviennent du cercle de Pierre l'Ibère" (l.385–386); "un recueil d'Apophthegmes d'un nouveau genre, qui a pour but, non d'édifier, mais de combattre le concile de Chalcédoine et ses défenseurs" (l.501–503). Faithful, and all given to Nau.
- The altar (l.5): Kugener, Life of Severus, "il parut juste de lui confier la direction du couvent avec le grand Jean, ainsi que de réserver l'autel à Jean, surnommé Rufus. Celui-ci avait étudié précédemment les lois à Beryte avec Théodore" (`zacharias-scholasticus_vie-de-severe-po2-syr-fra_kugener1903.txt` l.5552–5555). Faithful. The same Life goes on to say Peter of Antioch drew him into the clergy and ordained him priest (l.5597–5599), which supports l.3 from a second witness.
- The heading (l.5; card `remembered` 1): "rédigées par l'un des disciples de saint Pierre l'Ibère, nommé le prêtre Jean de Beit-Rufin, d'Antioche, évêque de Maiouma de Gaza" (l.616–618). Exact.
- Checked with eyewitnesses (l.7): ch. XXI, "j'ai contrôlé sa vérité l'ayant apprise en l'entendant raconter d'une façon certaine par ceux qui l'avaient vue" (l.2802–2804). Faithful.
- Raabe (l.9): title "Syrische Übersetzung einer um das Jahr 500 verfassten griechischen Biographie" (`life-of-peter-the-iberian_petrus-der-iberer-deu_raabe1895.txt` l.1); "dessen Name schon zu Euagrios' Zeit [536 — 593] nicht bekannt war" (l.667–668); "ob etwa ihr Verfasser mit unserm Biographen identisch ist" (l.614–615). Faithful. I searched the Library for any held scholar who gives the Life of Peter to John Rufus and found none, so the records' absence note stands.
- The close (l.11): "Notre père et évêque, le vénérable abba Pierre l'Ibère, nous racontait" (l.620). Faithful.

**Findings**
- **M6 MINOR (items 1, 7; an identification told without its owner).** Brief l.5: "In his Life of Severus, Zachariah of Mitylene says…". The card repeats it in `remembered` 2, `uncertain` 1 and 2, and the Kugener source's author; the records witness does too. That the author of the Life became bishop of Mitylene is E. W. Brooks's identification (`zachariah-rhetor_chronicle_hamiltonbrooks1899.txt` l.351–367). Kugener, the Life's editor, calls him "Zacharie le Scholastique" (l.76, 307) and nowhere bishop of Mitylene. The batch README keeps "Zachariah Rhetor" for this reason, and the Zachariah card puts Mitylene in `uncertain` 1 as "Brooks's identification". The John Rufus texts tell it plainly, and the Severus texts call the same man "Zachariah Rhetor". No held witness argues against Brooks, so this is minor, but the pattern asks a Dominant Modern Reconstruction to name its owner, and the batch should use one name. Fix: "Zachariah Rhetor" at each of these places in the John Rufus brief, card and records.
- **M7 MINOR (item 8).** Brief l.1: the first mention is "His companion smiled and said it had been Juvenal's." The place comes only on the second mention ("Juvenal of Jerusalem"), and a listener is never told who Juvenal was. Chapter XVI says he lived in the monastery "quand il arriva à l'épiscopat" (l.2117). Fix: "His companion smiled and said it had been the monastery of Juvenal, bishop of Jerusalem." Then: "John answered that Juvenal had been the companion of Judas…".
- **M8 MINOR (item 10).** The brief runs 333 words (2:03), past the non-major ceiling of about 324. Suggested cut, brief l.9: "Its German editor, Richard Raabe, asks whether the author of the Plerophories wrote it too, and leaves the question open." This replaces the last two sentences; card `uncertain` 3 already holds the Evagrius point.
- **M9 MINOR (records).** The records claim "He succeeded Peter the Iberian as bishop of Maiuma; he was in Jerusalem in 485" is tagged Widely Accepted. It rests on Nau alone ("Il semble dès lors… car il lui a succédé", l.375–376), and the card's `uncertain` 2 sets it against Zachariah's narrower line. Fix: tag it Dominant Modern Reconstruction, witness Nau, and keep the heading's "évêque de Maiouma" as the Documented claim it already is.
- With M6 to M8: 321 words (1:59), FK 8.2, Flesch 64.8.

---

## 3. Zachariah Rhetor

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
- The pamphlet (l.5): "J'examinais les livres des libraires établis dans le Portique royal… me donna le libelle… on bafoue un philosophe… il s'est distingué depuis dans l'épiscopat… J'entends parler de Sévère" (Kugener l.379–387). Faithful. "in Constantinople" rests on Brooks's l.349–350 and Kugener's gloss "ici (= à Constantinople)" (l.7060); acceptable.
- "a very lame one" (l.5): Brooks, Select Letters introduction, "it must be admitted that the answer is a very lame one" (`severus-of-antioch_select-letters-book6-part1_brooks1903.txt` l.89–93). Exact. This is Brooks in his second book, and the card's sources list it.
- The history (l.7): the compiler's appendix, "for the most part from the Chronicle of Zachariah, a rhetor, which he wrote in Greek to a man named Eupraxius, who lived at the Court" (l.300–304, quoting l.2040–2044); Brooks, "the work of Zachariah ended in 491… who followed him in bks. 3-6 only, and to whom the name of Zachariah was wrongly attached by later writers" (l.310–314). Faithful.
- Mitylene (l.9): "the author of the Dialogue… inscribed 'Zachariou Scholastikou… episkopou Mutilēnēs', who in his preface states that he had studied at Alexandria… Now Zachariah of Mitylene was present at the Synod of 536… conforming perhaps to the Chalcedonian faith, was made bishop of Mitylene" (l.353–366); note 4, "His name is not among the signatures to the decree of the Synod of 536, and he may possibly have been a nominee of Anthimus" (l.385–386). See M11.
- The close (l.11): the preface "tore into ten thousand rents the perfect Robe of Christ, woven from the top throughout" (l.2177–2178), within "the history of one Zachariah by name, who begins to write in Greek to Eupraxius as follows" (l.2163–2165). Exact; the compiler presents the preface as Zachariah's.
- The records' handling of Brooks's withdrawn Plerophories note (corrigenda, "p. 3, note 5. Omit the second sentence", l.190) is right.

**Findings**
- **M10 MINOR (item 7; disputes in place).** Brief l.7: "Brooks says the compiler followed Zachariah in books three to six only…". The records file this as a `contested_claim` with Land on the other side, and the card's `uncertain` 4 gives both. The brief gives one. Brooks: "In spite of these facts Land ascribes bk. 7 to Zachariah" (l.330). Kugener names Land as the 1870 editor of the Syriac (`zacharias-scholasticus_…kugener1903.txt` l.17148). Fix, after that sentence: "Land, the chronicle's first editor, gives him book seven as well."
- **M11 MINOR (item 1).** Brief l.9: "A bishop of that name was at a synod in 536, Brooks says, though his name is not among the signatures to its decree. Brooks suggests, with a "perhaps," that he had come over to Chalcedon's side by then." Brooks's "perhaps" goes with being made bishop ("at a later time, conforming perhaps to the Chalcedonian faith, was made bishop", l.364–366). The missing signature is Brooks's note, and there he reads it the other way: "he may possibly have been a nominee of Anthimus" (l.386), the bishop the synod condemned. Set side by side, the two sentences suggest a link Brooks does not make. Card `uncertain` 2 has the same gap. Fix, brief: "A bishop of that name was at a synod in 536, Brooks says. Brooks suggests, with a "perhaps," that he had come over to Chalcedon's side to become bishop." Card `uncertain` 2: "…and notes that his name is not among the signatures to its decree; he may possibly have been a nominee of Anthimus, Brooks says."
- **M12 MINOR (card; item 1).** Card `uncertain` 1: the identification "rests on the Greek heading of a dialogue…". Brooks also relies on Dionysius Bar Salibi's citation of "Zachariah the Rhetor and bishop of Melitene", which he reads as an error for Mitylene (l.260–263, 357–358). Fix: "It rests on the Greek heading of a dialogue by 'Zachariah Scholasticus', later bishop of Mitylene, whose preface says he studied at Alexandria, and on a citation by Dionysius Bar Salibi of 'Zachariah the Rhetor and bishop of Melitene', which Brooks takes for a slip for Mitylene."
- **M13 MINOR (card; an absence put too widely).** Card `dates`: "No source used here gives his birth or death." Brooks gives a bound: he "died or was deposed between 536 and 553" (l.366–367), and the records' absence note mentions it. Fix: "No source used here gives his birth. By Brooks's identification he died or lost his see between 536 and 553."
- With M10 and M11: 324 words (2:00), FK 7.8, Flesch 63.2.

---

## 4. Severus of Antioch (major)

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
- The arrest (l.1), Evagrius IV.4, tr. Walford: "Justin, in the first year of his reign, ordered him to be arrested, and to be punished, as some say, by having his tongue cut out… he flies from his see, in the month Gorpieus, which in the Latin language is called September, in the five hundred and sixty-seventh year of the Era of Antioch" (`evagrius-scholasticus_ecclesiastical-history_walford1846.txt` l.7868–7898). Faithful. Brooks: "on Sept. 29 fled from Antioch", and the note "Evagr. (iv. 3) seems to place his flight in 519… but the homilies… which are arranged chronologically, and end with Lent 518, are decisive for the earlier date" (`severus-of-antioch_select-letters-book6-part1_brooks1903.txt` l.200, 213–218). See M14.
- Birth and schooling (l.3), Kugener: "L'illustre Sévère est Pisidien d'origine, sa ville natale est Sozopolis" (l.533); "sa mère devenue veuve l'envoya avec ses deux frères, qui étaient plus âgés que lui, à Alexandrie, pour étudier la grammaire et la rhétorique" (l.588–590). Faithful. Brooks: "His enemies accused him of having in his youth followed heathen practices, and it was in order to refute this charge that Zacharias wrote his life… the answer is a very lame one" (l.89–93). Exact.
- Baptism and the monastery (l.5): Kugener, "baptisé dans la chapelle du divin et victorieux martyr Leontios" (l.5224–5226); Evagrius III.32–33, "having participated in holy baptism in the sacred precinct of the divine martyr Leontius, who is revered at Tripolis… a certain monastery situated between the city of Gaza and the town called Majumas; in which latter place Peter the Iberian… passed through the same discipline… expelled from his own monastery by Nephalius… obtains the notice of the emperor Anastasius, as is narrated by the author of the life of Severus" (l.6986–7014). Faithful; see M15.
- Bishop and letters (l.7): Brooks, "Severus was ordained his successor (Nov. 6, 512)" (l.172–173); Evagrius, "Severus, in issuing synodical letters, expressly anathematised the synod at Chalcedon"; the Alcison letters, "which included an anathema, both on the synod and all others who affirmed two natures or persons in the Lord" (l.7015–7037). Faithful.
- Exile and death (l.9): Brooks, "for the rest of his life lived for the most part in hiding in Egypt… wrote the controversial works against Julian the deposed bishop of Halicarnassus, who maintained the incorruptibility of Christ's body" (l.201–206); "in Mar. 536 Anthimus was deposed, and he and Severus expelled from the city, while at the synod held in May their final condemnation was decreed. On Feb. 8, 538 Severus died in Egypt" (l.237–241). Evagrius IV.10, "She also persuades Justinian to send for Severus" (l.8166–8169); IV.11, "a constitution was drawn up by Justinian in which he anathematised Severus, Anthimus, and others" (l.8212–8214). Faithful.
- Misael (l.11, 13), Select Letters I.17: "as to interest or the avaricious system of loans it was my desire not to know even the very name of them" (l.2773–2775); "a great load of debts and of interest was hanging over it… I forgot the spiritual laws" (l.2783–2786); "who Himself alone is able to heal our church that is groaning under many wounds, and to change need into abundance" (l.2826–2828). Exact.
- The letter count (l.13): "the total cannot have been less than 3759. Of these the version of Athanasius comprises 123 only" (l.253–256); "made in the year A.S. 980 (669)" (l.276–277). The year 669 is Brooks's conversion, and the sentence opens on "Brooks reckons". Faithful.
- Card: Brooks on the monastery of Theodore, "Called by the so-called Zacharias Rhetor (vii. 10) the monastery of Theodore" (l.140–141); the episcopate "little evidence beyond the assertions of his enemies produced at the synod of 536" (l.193–197); "probably under Theodora's influence" (l.231–232). Faithful. I found no birth year in Zachariah's Life, Evagrius or Brooks, so the card's absence stands.

**Findings**
- **M14 MINOR (item 7; disputes in place).** Brief l.1: "He fled his see in September. E. W. Brooks, the English translator of his letters, dates the flight to 518." The records hold the year as a `contested_claim`, and the card's `uncertain` 3 gives both sides; the brief gives Brooks's side only. Fix: "He fled, and E. W. Brooks, the English translator of his letters, dates the flight to 29 September 518. Evagrius's year seems to give 519, Brooks notes, but Severus's dated sermons decide it."
- **M15 MINOR (items 1, 6; one witness counted as two).** Brief l.5: "Zachariah and Evagrius agree he was baptized…" and "…where Peter the Iberian had lived, Evagrius says." Evagrius ends the whole passage, baptism to Anastasius, with "as is narrated by the author of the life of Severus" (l.7013–7014), and Brooks notes that Zachariah's Life was "Used by Evagrius (iii. 33)" (l.97). Zachariah's Life tells the same events itself: Nephalius (Kugener l.6524, 6649–6660) and the plea to the emperor (l.6773–6782). The brief counts a source and its copyist as two agreeing witnesses. Fix: "Zachariah says he was baptized at the shrine of the martyr Leontius at Tripolis. He became a monk between Gaza and Majuma, where Peter the Iberian had lived. … Severus pleaded their cause at Constantinople before the emperor Anastasius. Evagrius tells this from a Life of Severus, which Brooks takes for Zachariah's."
- **M16 MINOR (item 4).** Brief l.3: a 29-word narrator sentence ("His fellow student Zachariah Rhetor wrote a Life of him, which says…"). Fix: "His fellow student Zachariah Rhetor wrote a Life of him. It says his widowed mother sent him and his two older brothers to Alexandria to study grammar and rhetoric."
- Length with M14 to M16: the brief is at the cap already. Suggested cuts: drop l.13's "Brooks reckons his letters once numbered at least 3,759; a Syriac version made in 669 keeps 123." (card `keyWorks` 1 holds it), so the close reads "In the same letter, Severus says God alone is…", with `[warmly]` still before it. Shorten l.3's Brooks sentence to "Brooks says Zachariah wrote to answer a charge of pagan rites in Severus's youth, and judges that "the answer is a very lame one."" Scored: 401 words (2:29), FK 7.9, Flesch 61.9.

---

## Totals

Part A: 1 blocking, 16 minor.

| Profile | Blocking | Minor |
|---|---|---|
| Joshua the Stylite | 1 (B1) | 5 (M1 to M5) |
| John Rufus | 0 | 4 (M6 to M9) |
| Zachariah Rhetor | 0 | 4 (M10 to M13) |
| Severus of Antioch | 0 | 3 (M14 to M16) |

Blocking: **B1**, Joshua the Stylite. Brief l.11, card `legacy.traces` 1 and `uncertain` 4, and the records tell Wright's 1882 attribution of the preserving chronicle to Dionysius of Tell-Mahre (d. 845) as fact. Held files by Nau (po08 l.48221–48226: the same Vatican ms. syr. 162, by a "Pseudo-Denys" writing in 775), Brooks (PO 17 l.714, "the so-called Dionysius") and Chabot (Michael the Syrian t.1 l.63096–63099) say the compiler was someone else.

Cross-profile note: the same man is "Zachariah of Mitylene" in the John Rufus texts and "Zachariah Rhetor" in the Zachariah and Severus texts (M6). One name across the batch, the README's, closes it.
