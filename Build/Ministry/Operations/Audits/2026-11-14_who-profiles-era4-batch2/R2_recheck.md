# R2 recheck: era 4 batch 2

Round 2 ran in two parts, each a targeted recheck by a fresh Opus agent that had not seen the drafting or round 1, at full effort. The parts follow, unchanged.

## R2 recheck, part 1: Dionysius of Tel Mahre, Jacob of Edessa, Benjamin I of Alexandria, Gregory of Narek

Reviewer: independent Opus, first sight of these files. I edited no profile, records or notes file. I made no git, web, paid or model calls, and used local scripts only. Inputs: R1_partB.md, R1_changes_partB.md, R1_partD.md, R1_changes_partD.md, the current batch 2 briefs, cards and audio, and the scratchpad records and notes. I found the changed text by diffing each brief against the R1 scored copies in `review/fixB/` and `review/fixD/` and by comparing the cards and records with the wording R1 quotes. I opened every cited line again in its vendored file and read it in context, folding OCR noise, long s, double spaces and hyphen breaks.

Short names as in R1: BH1, MICHAEL1, MICHAEL2, ASSEMANI1, ELIAS, PO16, CHRONMIN, MAI10, RENAUDOT, PG111, WRIGHT, FOTHERINGHAM (part B); HIST, NIKIU, BASSET, BUDGE, ABUSALIH, CHAMICH, ISSAV, ISSRIT, GELZER, MACLER, PARISOT, NURIKHAN (part D). ASSEMANI in part D is the same file as ASSEMANI1.

**Mechanical checks (all four).** `engine.m1.gates.grade_text` was run from the repo root on each current brief. A script confirmed that each audio file equals its brief once `[calmly] ` (at the start) and `[warmly] ` (at the start of the last paragraph) are removed, that each holds those two tags only, and that no tag is in a brief or card. Each card parses as JSON, is in batch 1's order (Benjamin has no `otherNames`, as R1 noted), has no empty or null field, and has at most three keyWorks. Every `sources` file exists. No card sentence outside `sources` runs past 25 words.

| Profile | Words | Time @162 | FK | Flesch | Longest brief sentence | Audio = brief |
|---|---|---|---|---|---|---|
| dionysius-of-tel-mahre | 404 | 2:30 | 7.65 | 66.96 | 22 (P1) | yes |
| jacob-of-edessa | 404 | 2:30 | 7.11 | 68.81 | 21 (P1) | yes |
| benjamin-i-of-alexandria | 404 | 2:30 | 8.21 | 60.19 | 24 (P7) | yes |
| gregory-of-narek | 405 | 2:30 | 8.03 | 61.53 | 25 (P6, unchanged) | yes |

The three brief fixes below change no word count. With them applied (scratch copies in `/tmp/claude-0/-home-user-CIC-Project/46148d77-0e3f-56b5-a386-901106a72590/scratchpad/review/fixR2p1/`): Dionysius 404 words, FK 7.68, Flesch 66.76; Benjamin 404, FK 8.18, Flesch 60.40; Gregory 405, FK 8.03, Flesch 61.53.

---

### Dionysius of Tel Mahre

| R1 finding | Verdict | Evidence |
|---|---|---|
| B-B1 (the editors put on the wrong side) | RESOLVED | BH1 l.22351-22366 reads "idque de prolixiori ejusdem Chronico intelligendum; nam Chronicon brevius ... non Joanni Darensi, sed Georgio Amidae chorepiscopo ... Ita Assemanus". The records now put Assemani, the editors, Wright and Chabot's 1895 edition on side 1. Side 2 is Chabot's "Pseudo-Denys" (MICHAEL1 l.13650, 59560; MICHAEL2 l.36430) and Fotheringham's "olim per errorem Dionysio Telmaharensi tributa" (FOTHERINGHAM l.190-191). Chabot's 1895 "Quatrième partie de la Chronique de Denys de Tell-Mahré" is at MICHAEL1 l.62784-62786. Card `uncertain` 3 is faithful line by line. Its Wright sentence is unclear (R2-B-M2). |
| B-M1 (P1: the decree, the lawgiver, "a sinner") | RESOLVED | The decree is at BH1 l.21384-21389 ("decem viri cujuscumque religionis"). Lazarus's "nobis edictum datum est" is at l.21500-21505 and the deposed bishop of Baghdad at l.21393-21395. The answer ending "una porro ex legibus nostris est principatus noster ecclesiasticus" is at l.21509-21518, and "deponatis peccatorem non prohibemus" at l.21700-21706. |
| B-M2 (P4: emir, rebuke, outcome, reason) | RESOLVED | BH1 l.21042-21053 gives the year, "Emirus Abdallah ... descendisset in Aegyptum" and Mohammed's destruction. "Abdallah, Tahiri filium" is at l.20841. The storm and Tanis are at l.21059-21066. "reprehendit eum ... de navigatione ... quum posses per epistolam significare", the letter "ne laederet ... neve ecclesias impeteret" and the graded tax are at l.21162-21181. |
| B-M3 (P6: the preface's frame) | RESOLVED, with one word to fix (R2-B-M1). DECLINED-ACCEPTABLE for "anyone of his church" | The protest "tu n'as pas considéré la vieillesse ... des stations et des prostrations à la porte des princes avec le mépris" is at MICHAEL2 l.27490-27508. Keeping "Dionysius's church" after "He says Theophilus ..." is a fair call against a wrong antecedent. |
| Word budget (P3, P5 trims) | RESOLVED | The ordinations on Friday, Saturday and Sunday are at BH1 l.20612-20620. "Apschinus ... pacem noluit, sed villas eorum ... comburens, plurimos quidem interfecit, reliquos vero vinctos navibus ... misit" is at l.21812-21819. |
| B-M4 (`uncertain` 4: the year) | RESOLVED | "Anno autem Graecorum 1136 (Chr. 823), quum Emirus Abdallah descendisset in Aegyptum", BH1 l.21042-21044. "Eodem anno" for the second journey is at l.21798. |
| B-M5 (`uncertain` 2: whose chronicle) | RESOLVED | MICHAEL2 l.27771-27773. |
| B-M6 (Eutychius, Makrizi, Renaudot) | RESOLVED | Eutychius: the Bimaidae "vectigal & tributum pendere noluerunt" and al-Mu'tasim sent, in Renaudot's quotation at RENAUDOT l.17714-17726 and in PG111 l.87139-87158. Makrizi: "eodem sedem Alexandrinam occupante ... anno Hegirae 216 Afschinum adversus eos copias duxisse", l.17703-17710. Neither names Dionysius. The first voyage is at l.17620-17623 ("Dionysius ... advenit, & dies multos apud illum ... transegit"). The drafter's "says Dionysius was there" is better than R1's wording, since Makrizi does refer to the Alexandrian patriarch. "totidem verbis" and Le Quien's "Baammyritanos" are at BH1 l.21826-21833. |
| B-M7 (records: where Tel Mahre was) | NOT RESOLVED | Charon is added (CHARON l.33957), but the absence still stands, and another held file gives the place. See R2-B-B1. |
| Note (the Nomocanon rule) | Taken, faithful | "Et in sponsione coronarum etiam sponsor frater est sponsi, et paranympha soror est sponsae ... uti definiunt Dionysius patriarcha Telmaharensis, et religiosus Iacobus Edessae", MAI10 l.45740-45750. Mai names the Nomocanon as Bar Hebraeus's at l.838-844 and l.38227-38232. |

#### New findings

- **R2-B-B1 BLOCKING (records `absent_details` 1, "the place Tel Mahre"; a false absence).** The detail still lists the place as absent, and the note says "no held line ties it to Dionysius's name". W. Wright's introduction to Joshua the Stylite puts a footnote on "Dionysius of Tell-Mahré*" (WRIGHT l.294). The note reads "... in Arabic تل ماکري, a small town on the river Balikh, between ar-Rakkah and Hisn Maslamah, according to Yáküt in the Mujam al-Buldan" (l.314-316; the OCR garbles its opening words). R1 missed this too.
  - Fix, records: the detail becomes "His birth year and family". Add to the note: "Where Tel Mahre was: W. Wright, citing Yaqut's Mu'jam al-Buldan, makes it 'a small town on the river Balikh, between ar-Rakkah and Hisn Maslamah' (WRIGHT l.294, 314-316). No held source says Dionysius was born there." Keep the Charon sentence, and change its tail to "no held line ties that see to Dionysius". Add a Documented claim with the same quotation.
  - Optional, card `place`, as a new last sentence (19 words): "Tel Mahre, W. Wright notes from the geographer Yaqut, was a small town on the river Balikh."

- **R2-B-M1 MINOR (brief P6, l.11; and audio; item 1; a word stronger than the source).** "There Dionysius protests that John ignored his old age". The French is "tu n'as pas considéré la vieillesse" (MICHAEL2 l.27490-27491), you did not take it into account. "Ignored" adds deliberate disregard, the fault the drafter found in R1's "forgot". Fix: "There Dionysius protests that John overlooked his old age and the contempt of waiting at princes' doors." The word count does not change.

- **R2-B-M2 MINOR (card `uncertain` 3, sentence 3; items 1 and 4; the Wright sentence can be misread).** "W. Wright, in his edition of Joshua the Stylite, calls the Vatican chronicle Dionysius's own larger work." The card has not said that the Vatican chronicle is the one Assemani found at Scete. Coming right after "a shorter chronicle", "larger work" reads as the longer chronicle that runs to 844, which is not Wright's point. Wright means the work that took in Joshua's short chronicle: "We owe the preservation of the short Chronicle of Joshua the Stylite to ... Dionysius of Tell-Mahré ... who incorporated it with his own larger work" (WRIGHT l.292-296). He ties it to Assemani's pages on it (l.300-308, 318, "Bibl. Orient., t. ii, p. 98 sqq., and pp. 341-8"). Fix (15 and 13 words): "W. Wright, in his edition of Joshua the Stylite, also gives this chronicle to Dionysius. He says Dionysius took Joshua's short chronicle into his own larger work."

**Verdict, Dionysius of Tel Mahre: NOT CLEAR. 1 blocking (R2-B-B1, records), 2 minor (R2-B-M1 in the brief and audio).**

---

### Jacob of Edessa

| R1 finding | Verdict | Evidence |
|---|---|---|
| B-B2 (the Chronicle marked wanted) | RESOLVED | CHRONMIN l.14453-14480: "CHRONICON IACOBI EDESSENI. INTERPRETATUS EST E.-W. BROOKS"; "Codice Musaei Britannici Add. 14,685"; "Auctor Iacobus Philoponus ... quem cum Iacobo Edesseno eundem fuisse ... satis liquet"; "Fragmenta non ultra annum 942 Sel. — 631 p. Chr."; "ipse Michael notat ... suspicatur"; "anno 1003 Sel. — 692 ... adfirmat Elias Nisibenus; quod si verum est, anni 18 continuatori". The `keyWorks` 1 sentences and the `uncertain` 2 sentences match. The source entry is added. Notes l.32 withdraw the Wanted entry. The older Wanted line at l.25 stays as an append-only log. |
| B-B3 (canons marked not held) | RESOLVED, with an incomplete heading list (R2-B-M4) | MAI10 l.38646-38650: "Iacobi Edessae. Xatam, quae superest ex oblatione, idest farinam, sine reprehensione sacerdotibus sociis suis vendere possunt sacerdotes". The card trace is faithful, and it is right to give no count. |
| B-M8 (P1: placed out of time) | RESOLVED | "il renonça à la charge pastorale ... Avant de partir, il discuta avec le patriarche et les évêques au sujet de l'observation des canons ... le fit brûler devant la porte du monastère du patriarche", MICHAEL2 l.36393-36398. |
| B-M9 (P3: no time) | RESOLVED | PO16 l.45708-45712 ("en l'an 700/1"); BH1 l.17519-17522; ASSEMANI1 l.97591-97596. |
| B-M10 (P4: the tracts) | RESOLVED | "un contre les pasteurs de l'Église; l'autre contre ceux qui transgressent la loi et les canons ecclésiastiques", MICHAEL2 l.36399-36401. |
| B-M11 (P7: the books) | RESOLVED | "fit charger ses livres et les expédia devant lui ... il termina sa vie dans ce couvent (de Tell 'Ada)", MICHAEL2 l.36419-36421. "Les bienheureux (moines) du couvent de Tell 'Ada ... s'empressèrent de faire reprendre ses livres avant qu'ils ne passassent l'Euphrate", l.36747-36753. "Its monks" is right. |
| Word budget (P2 to P8 trims) | RESOLVED | Each trimmed sentence keeps its witness. The year tables stay in `keyWorks` 1 (MICHAEL2 l.40776-40778). |
| B-M12 ("Edgar") | RESOLVED | "mon élève, M. Edg. Triffaux", PO16 l.44598-44599. Brief, `keyWorks` 3 and both source lines read as R1 asked. |
| B-M13 (an unnamed passage as a witness) | RESOLVED, with one form to fix (R2-B-M3) | The «...» passage "pendant douze ans il expliqua les Écritures d'après le texte grec", with Kenneshre, is at PO16 l.45728-45736, and its note "KUGENER et CUMONT, Recherches sur le Manichéisme, p. 88" at l.45768. The records tag is now Dominant Modern Reconstruction. |
| B-M14 (`dates`: Chabot's 692) | RESOLVED | Brooks: "1003 Sel. — 692 p. Chr." (CHRONMIN l.14477-14478). Chabot: "la Chronique a dû être écrite en 692, sous le premier règne de Justinien II ... et sous celui de 'Abd el-Mélik" (MICHAEL1 l.56636-56638). |
| B-M15 (`uncertain` 1: Elias's year) | RESOLVED | "Annus 89 iniit feria 5a die 1° kanun i anni 1019 Graecorum ... Iulianus patriarcha Iacobitarum mortuus est et Iacobus Edessenus", ELIAS l.6495-6503. The split into two sentences keeps Elias as the subject of the second. |
| Note (Malech on dots) | DECLINED-ACCEPTABLE | It is a late secondary report, and `uncertain` 6 is true as it stands. |

#### New findings

- **R2-B-M3 MINOR (card `uncertain` 5; records claims and `contested_claims` on the teaching years; item 4; a form an English reader misreads).** "M.-A. Kugener and Fr. Cumont". In English "Fr." reads as "Father", and this batch uses it that way ("Fr. Issaverdentz", NURIKHAN l.17931). Kugener and Triffaux print the name both ways: "F. CUMONT" (PO16 l.45722) and "Fr. Cumont" (l.44831). Fix, in the card and in both records items: "M.-A. Kugener and F. Cumont".

- **R2-B-M4 MINOR (records claim on the Nomocanon, `absent_details` 2; notes "After R1"; item 1; a heading list with gaps, and one reply of Jacob's left out).** The records give 23 heading lines as the headings for Jacob's canons. Five more headings, in OCR forms the search missed, read "lacobi Edessae" (MAI10 l.38776, 44049), "Tacobi Edessae" (l.39681, 40490) and "Iacobi Edcisae" (l.43917). The Nomocanon also reports one of Jacob's replies to John the Stylite: "Iohannes Stylita interrogans religiosissimum Jacobum Edessae, responsum accepit: dixit ... haud ex necessitate fit hoc ieiunium" (l.41398-41402). So "his letters ... not held as texts" needs the same narrowing that the canons got. The two bare "Iacobi." headings (l.38949, 39540) could be Jacob of Sarug and should not be added.
  - Fix, records claim: add l.38776, 39681, 40490, 43917 and 44049 to the heading list, and add a claim quoting l.41398-41402.
  - Fix, `absent_details` 2: "His letters are not held as texts. The Nomocanon reports one reply of his to John the Stylite, on the apostles' fast (MAI10 l.41398-41402). The Responses to Addai are not held." Mirror this in the notes.
  - No card change: the trace gives no count, which stays right.

**Verdict, Jacob of Edessa: CLEAR on the brief and audio. NOT CLEAR on card and records: 0 blocking, 2 minor (R2-B-M3 on the card, R2-B-M4 in the records).**

---

### Benjamin I of Alexandria

| R1 finding | Verdict | Evidence |
|---|---|---|
| D-B1 (a false absence of a writing) | RESOLVED as an absence. The fix brought in a new error (R2-D-B1) | The homily is listed at ASSEMANI l.124088-124089, "Benjamini Patriarche Alexandrini Homilia de Nuptiis Canz Galilez". The date that R1, the records, the notes and the card give it belongs to the codex before it. |
| D-M1 ("many" for "most") | RESOLVED | "he drew to himself most of the people whom Heraclius ... had led astray", HIST l.44830-44833. |
| D-M2 ("these anathemas" with no context) | RESOLVED | HIST l.47893-47910: III "shall be anathema", IV and V "let him be anathema", VI "shall cast him out", VII "be degraded". The quotation is verbatim at l.48051-48052. |
| D-M3 ("Romans"; four short sentences; length) | RESOLVED. The tense of the reworded Renaudot sentence needs a fix (R2-D-M1) | "a fugitive from the Romans", HIST l.44467. Barshut, the "very rich" parents and Theonas are at l.42836-42847. Charles: "John of Nikiu was probably born about the time of the Mohammedan invasion of Egypt. He was the Coptic bishop of Nikiu", NIKIU l.178-179 (R1 cited l.175-176; the lines are 178-179). The drafter's reordering keeps Charles as the subject, which is right. |
| D-M4 (Mennas built up; forward reference) | RESOLVED | HIST l.43572-43582 and l.43750-43753 ("Say that the council of Chalcedon is good ... But Mennas would not do so"). The old `uncertain` 8 is gone. |
| D-M5 (`knownFor` told as settled) | RESOLVED | The safe-conduct is now the History's. |
| D-M6 (Basset's 630-648) | RESOLVED | "(630-648)" stands in parentheses after "le trente-huitième de la liste" at BASSET l.40726-40727. "Il demeura patriarche pendant trente-neuf ans" is at l.40597, and "mourut après avoir exercé le patriarcat pendant trente-neuf ans" at l.40875-40876. |
| D-M7 (a role for the Abu Salih editor) | PARTLY | The role is gone, but naming Evetts as the note's author rests on an inference the preface does not support (R2-D-M3). The note is at ABUSALIH l.9662-9665, continued unsigned at l.9700-9702, and "622 to 660 ?" is at l.11741. |
| D-M8 (Abulbircat, Elmacinus) | RESOLVED | "Canon Chronologicus Abulbircat ... mors ejus incideret in an. J. C. 648, toto decennio citius quam Elmacinus, & alii", RENAUDOT l.11590-11595. "Georgius filius Hamd, vulgo Elmacinus dictus, historiam contexuerat a creatione mundi", l.441-442. |
| Note (Ludolf) | Taken, faithful | Records only. |

#### New findings

- **R2-D-B1 BLOCKING (card `keyWorks` 2 and the Assemani `sources.about` title; records claim and `absent_details` 1; notes l.29; a manuscript date and a catalogue misread).** The homily is said to be in "a manuscript of 1065", in "the catalogue of the Syriac manuscripts". Both are wrong.
  - In this list Assemani gives each codex its number, then its contents, then its size and any date. Codex XIV ends "In fol. membr. 120. script. anno Martyrum 655. (Christi 939.)", and XV follows (ASSEMANI l.124041-124055). The line "In fol. membr. 313. script. anno Martyrum 781. (Christi 1065.)" (l.124081-124084) closes codex XV, which runs from Ignatius's martyrdom to Gregory Nazianzen's homily. Benjamin's homily opens codex XVI (l.124085-124089). Codex XVI ends "In fol. membr. 139." with no date (l.124101), and XVII follows (l.124104). So the homily's manuscript is undated in the catalogue.
  - The list is headed "CODICES COPTICI, Quos Auctor ex Oriente advexit" (l.123862-123865, repeated at l.123953-123954). It is the Coptic manuscripts Assemani brought back from the East, not the Syriac ones.
  - Fix, card `keyWorks` 2 `about` (16, 10 and 5 words): "known here only from Joseph Assemani's list of the Coptic manuscripts he brought from the East. It names the homily in an undated parchment volume. The text is not held".
  - Fix, card `sources.about`, the Assemani title: "Bibliotheca Orientalis Clementino-Vaticana, volume 1, index of manuscripts: the Coptic codices Assemani brought from the East".
  - Fix, records claim: "Assemani's list of the Coptic codices he brought from the East ('CODICES COPTICI, Quos Auctor ex Oriente advexit', l.123862-123865) gives, as codex XVI, 'Benjamini Patriarchae Alexandrini Homilia de Nuptiis Canae Galilaeae' (l.124085-124089; OCR 'Patriarche', 'Canz Galilez'). The codex is 'In fol. membr. 139.' with no date (l.124101). The date 1065 at l.124081-124084 closes codex XV." Make the same change in `absent_details` 1 and in notes l.29.

- **R2-D-M1 MINOR (brief P6, l.11; and audio; item 4; tense breaks between two sentences).** "Eusèbe Renaudot, who wrote a Latin history of these patriarchs in 1713, calls their line heretical. He called the account a fable of later Copts." Fix: "He calls the account a fable of later Copts." This matches "calls" in the sentence before. Renaudot: "a Coptitis recentioribus inventa esse non dubitamus ... in longa illa sub Agathonis nomine fabula" (RENAUDOT l.11542-11547). The word count does not change.

- **R2-D-M3 MINOR (card `legacy.traces` 3, sentence 2, and `uncertain` 5, sentence 3; records claim on the Abu Salih notes; item 1; an author assigned on a reading the preface does not give).** The records make every note without "(A. J. B.)" Evetts's and cite the preface. The preface says the opposite. Butler's "contributions to the work are by no means limited to the notes which bear his initials" (ABUSALIH l.133-134). That marks the initialled notes as Butler's, but it leaves the unsigned ones open. The note at l.9662-9665 and l.9700-9702 is unsigned. The fix names Evetts's edition, which is held (l.1, l.44), without claiming he wrote the note.
  - Fix, `traces` 3 sentence 2 (16 words): "A note in B. T. A. Evetts's 1895 English Abu Salih says those monasteries were restored in Benjamin's time."
  - Fix, `uncertain` 5 sentence 3 (16 words): "A note in B. T. A. Evetts's 1895 Abu Salih gives 622 to 660 with a question mark."
  - Fix, records: tag the authorship claim Inferential-Thin, with "Butler's notes are initialled; the preface says his help went beyond them, so an unsigned note is the edition's and not surely Evetts's" (l.129-134).

**Verdict, Benjamin I of Alexandria: NOT CLEAR. 1 blocking (R2-D-B1, card and records), 2 minor (R2-D-M1 in the brief and audio).**

---

### Gregory of Narek

| R1 finding | Verdict | Evidence |
|---|---|---|
| D-B2 (his held words in Parisot) | RESOLVED | PARISOT l.1662-1667: "primusque, ut videtur, e scriptoribus Armenis Gregorius Narekensis (qui circa annum 1003 obiit) episcopum Nisibenum scriptoribus inseruit ... Ipse, inquit, arianam haeresim gladio verbi destruxit et dissolvit". The note "Oratio panegyrica prima in sanctum Iacobum Nisibenum (Liber precum, Constantinopoli, 1726 ...)" is at l.1716-1718. The Song of Songs line, "Ea praecipue apud nos quae de lingua graeca vel syriaca interpretata fuerunt, obscure versa sunt in linguam armeniacam ... Venetiis, 1789", is at l.1881-1883. `keyWorks` 2, `traces` 5, the source entry and both `absent_details` are faithful. |
| D-M9 (the who-line late; "Mekhitarist" undefined) | RESOLVED | The who-line is now sentence 6. "the Mukhitharian society of Venice, of which Chamich was a member" is at CHAMICH l.23420-23421, and "Fr. Issaverdenz, Mechitarist of Venice" at NURIKHAN l.18205-18206. "Monks of an Armenian order" is carried by Ormanian's "a monastic establishment ... his congregation" on Mekhitar's San Lazaro (ORMANIAN l.4483-4504). "brought up from his infancy in the convent of Narek, and in process of time became its abbot" is at CHAMICH l.4813-4816. |
| D-M10 (the Stepanos sentence floats) | RESOLVED, with one phrase to fix (R2-D-M2) | "Diese alle ordneten ... an, dafs die auf das Bekenntnis von Chalkedon getauften noch ein zweites Mal getauft werden sollten", GELZER l.6506-6510, after "Und Anania, der grofse Philosoph, welcher auch Mönch zu Narek war", l.6482-6483. MACLER l.4313-4316 and l.4350-4353 agree. |
| D-M11 (`traces` 1) | RESOLVED | "In MS β the text after a break, intended to show that the rite proper is finished, continues", then discourse xii and discourse xli, "Sons of the living God" (Conybeare l.34470-34477, 34530-34531), after "THE HOUR OF REST". |
| D-M12 (`traces` 3) | RESOLVED | "is found at the end of that gospel, written separately", ISSRIT l.16079-16080. |
| D-M13 (`traces` 4) | RESOLVED | Vaspurakan made over to the emperor at CHAMICH l.5651-5652 and l.5673-5674. "about one-third of the inhabitants" and Sebastia, A. D. 1021, at l.5685-5692. The friars of Narek with Gregory's body and the new convent at l.5696-5700. |
| D-M14 ("Rshtunikh") | RESOLVED | "Narek in der Provinz Rstunikh", GELZER l.6327-6328. |
| D-M15 (a loose "only") | RESOLVED | "Ce passage fait penser à Grégoire de Narek" is a note, not a limit. |
| D-M16 (`uncertain` 8 had no point) | RESOLVED | I searched every file that names Gregory for "Lamentation", "élégie", "Klage" and "lamentazion", and none calls the book the Book of Lamentations. Boré speaks of "Ses élégies sacrées" (BORÉ l.2415-2416) and Chamich of "several elegies" (l.4889), neither as a title. |
| D-M17 (the setting given to both prayers) | RESOLVED | "Finally, at the foot of the altar, he says in a low voice, the following prayer" (ISSRIT l.843-844); "They then say this prayer on the same subject" (l.907). |
| D-M18 (Issaverdens a Mekhitarist) | RESOLVED | NURIKHAN l.17930-17931 and l.18205-18206. |
| Notes (harangues, Sergius, the Ritual footnote) | DECLINED-ACCEPTABLE | They are unused leads, and the brief is at the cap. |

#### New findings

- **R2-D-M2 MINOR (brief P4, l.7, and audio; records `absent_details` 2; item 1; a writing date stretched).** "Stepanos of Taron wrote Armenian history in the same century." The brief has just set Gregory in "tenth-century Armenia". Macler gives Stepanos's third book as running "de l'an 887 à l'an 1005" (MACLER l.441-442), so Stepanos wrote it after 1004. He lived in the tenth century and met these teachers in his youth ("Dans notre jeunesse, nous avons vu nous-même quelques-uns de ces [Pères]", l.4346-4347), but he did not write in it. The card's "Stepanos of Taron, of Gregory's own century" (`uncertain` 7) is right.
  - Fix, brief and audio: "Stepanos of Taron, of the same century, wrote Armenian history." The word count does not change.
  - Fix, records `absent_details` 2: "Stepanos of Taron, who knew some of these teachers in his youth and wrote soon after 1004, describes Narek ...".

**Verdict, Gregory of Narek: NOT CLEAR. 0 blocking, 1 minor (R2-D-M2, in the brief and audio).**

---

### Writing checks on the changed text and the whole briefs

I read all four briefs again in full for AI tells, "not X but Y", "X, not Y" and "X and never Y" contrasts, empty contrasts, tails, aphorisms, triads, undefined terms and sentences over about 25 words. None of these remains in the briefs beyond the fixes above. The three-day ordination (Dionysius P3) and the "burned their villages, killed many, and shipped the rest away" (P5) are Bar Hebraeus's own sequences, not rhetorical triads. "for coming instead of writing" (Dionysius P4) is the source's own contrast ("quid cogebat te ut venires ... quum posses per epistolam significare"). In card `uncertain` 3, "addressed to George ... not to John of Dara" is the editors' own "non Joanni Darensi, sed Georgio" (BH1 l.22361-22364). No changed sentence gives a count that was not fully made, and none tells an editor's view as settled.

### Counts

| Profile | Blocking | Minor | In the brief and audio |
|---|---|---|---|
| Dionysius of Tel Mahre | 1 (R2-B-B1, records) | 2 | R2-B-M1 |
| Jacob of Edessa | 0 | 2 | none |
| Benjamin I of Alexandria | 1 (R2-D-B1, card and records) | 2 | R2-D-M1 |
| Gregory of Narek | 0 | 1 | R2-D-M2 |


## R2 recheck, part 2: Maximus the Confessor, Martin I of Rome, Timothy I of Baghdad, Photius of Constantinople

Reviewer: independent Opus, first sight of these files. I edited no profile, records or notes file. I made no git, web, paid or model calls, and used local scripts only. Inputs: `review/R1_partA.md`, `R1_changes_partA.md`, `R1_partC.md` and `R1_changes_partC.md`; the current files in `Who-Profiles/era4/batch2/`; the scratchpad records and notes. I found the changed text by comparing the current briefs and cards with the wording R1 quotes. I opened each cited line again in its vendored file and read it in context, folding OCR noise, long s, double spaces and hyphen breaks. Short file names are R1's.

I scored every suggested brief fix on scratch copies in `/tmp/claude-0/-home-user-CIC-Project/46148d77-0e3f-56b5-a386-901106a72590/scratchpad/review/fixR2p2/`.

### Mechanical checks (all four)

A script confirmed that each audio file equals its brief plus `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph. Each has one tag of each kind, and no tag is in a brief or card. Each card parses as JSON. The cards are in batch 1's field order, with no empty or null field and at most three keyWorks. Photius has no `otherNames`, which is right, since the field is absent rather than empty. Every `sources` file exists.

| Profile | Words | Time @162 | FK | Flesch | Longest brief sentence |
|---|---|---|---|---|---|
| maximus-the-confessor (major) | 405 | 2:30 | 8.16 | 61.24 | 25 (P5, "One must speak…") |
| martin-i-of-rome (major) | 405 | 2:30 | 6.74 | 72.20 | 25 (P7, Bede) |
| timothy-i-of-baghdad (major) | 403 | 2:29 | 7.22 | 67.18 | 25 (P5, Thomas of Marga) |
| photius-of-constantinople (major) | 404 | 2:30 | 7.09 | 67.19 | 24 (P5, Symeon) |

No card sentence outside `sources` runs past 25 words. A script flagged Timothy `uncertain` 2 at 34, but that was two sentences of 17 words each, joined because the first ends inside a quotation mark.

After the fixes below, scored on the scratch copies: Maximus 405 words, 2:30, FK 8.16, Flesch 61.24, longest sentence 25. Martin 405, 2:30, FK 6.83, Flesch 71.57, longest 25. Timothy 405, 2:30, FK 7.27, Flesch 66.89, longest 25. Photius 404, 2:30, FK 7.11, Flesch 66.98, longest 24. Maximus stays above the 60 floor; its one brief fix changes word order only.

---

### Maximus the Confessor

| R1 finding | Verdict | Evidence |
|---|---|---|
| A-B1 (Macarius trace without the council's verdict) | RESOLVED | Card l.31. In NPNF l.25749 the council cries "To Macarius the heretic, anathema!", and l.25996-25997 reads "with the best of cause we anathematize and depose Macarius, who was bishop of Antioch". "Cursed Maximus and his disciples among the heretics" rests on "post hos omnes hereticos, eum qui nuper est exortus infaustum Maximum cum impiis ejus discipulis" (M11 l.74362-74367). The notes' difference 1 (l.28) and the records claim (l.134-135) carry both lines. |
| A-M1 (no identifier) | RESOLVED | Brief l.1, "the old monk Maximus the Confessor". The Greeks' "Theologus et confessor" is at PG90 l.275. |
| A-M2 (partisan witness unmarked) | RESOLVED | Brief l.3. The Relatio says "Respondit Dei servus" (PG90 l.6802). Duchesne's date stays attached: "comme il résulte des dates fournies par les interrogatoires de saint Maxime" (DUCH l.163416-163419). |
| A-M3 (Typos before the debate) | RESOLVED | Brief l.7. The debate is "a. 645" (PG90 l.280), and the Typos was issued "nuper, id est, per sextam indictionem" (l.7540-7541). The new sentence's stacked appositives are R2-A-M1. |
| A-M4 (no anchor; Ekthesis undefined) | RESOLVED | Brief l.9. Troilus and Sergius Eucrates question him "Eademque die ad vesperam" and ask "Non communicas throno Constantinopolitano?" (PG90 l.7497-7517), so "His questioners" has its anchor. "per ecthesim, quae in hac urbe Sergio auctore edita est" (l.7539-7540) supports "an earlier statement by the patriarch Sergius". The knock-on effect on card `uncertain` 9 is R2-A-M2. |
| A-M5 ("followers" for both) | RESOLVED | Brief l.15: "ejusque discipulum beatum Anastasium … alterum quoque beatum Anastasium" (PG90 l.11469-11474). Card l.40: Combefis, "non alter alterius discipulus … nunquam tamen ipse Maximus discipulum vocat" (l.16351-16362, under "FR. COMBEFISII NOTAE AD VITAM S. MAXIMI", l.15515). |
| A-M6 (prophecy in the narrator's voice) | RESOLVED | Brief l.17. The letter's writer names "dominum vero Anastasium abbatem, et me peccatorem" (PG90 l.11703-11704), so he is the other Anastasius, the envoy. The death is "tertio decimo die … Augusti … secundum divinum ejus vaticinium" (l.11748-11751). Declining the spoken year is right at the cap. |
| A-M7 ("them" with no referent) | RESOLVED | Brief l.13: "Suscipiant horum damnationem, quae Romae … synodice edita est" (PG90 l.9574-9576). |
| A-M8 (renderings in quotation marks) | RESOLVED | Card l.31 and l.47 have no marks. The only quotation left on the card is "Maximus monachus" (l.43), which is verbatim. |
| A-M9 (Fabricius and Migne with no context) | RESOLVED | Card l.8. "J. A. Fabricius" is held, for example in the Antiphonary of Bangor volume. Migne's running head reads "ANNUS 662" (PG90 l.140). |
| A-M10 (count overread) | RESOLVED | Card l.20: "pari quatuor Evangeliis numero, centenis comprehensum capitibus" (PG90 l.76078-76079). |
| A-M11 (process register) | RESOLVED | Card l.46. I also tested "No held source gives his birth year" across all of `cic/texts/`. The only hit is a Library file header ("c. 580-662", PG91 l.3), which is not a witness. The absence holds. |
| A-M12 (notes absence) | RESOLVED | Notes l.22 now gives NPNF l.18898 and l.40117. |

**Changed sentences, checked in full.** Brief l.1, 3, 5, 7, 9, 13, 15 and 17 and card l.8, 20, 31, 40, 46 and 47 each say what their lines say, with their witnesses attached. None gives a count it does not make, none tells an editor's view as settled, and none is a false absence. Dropping "to noble parents" (l.5) removes a claim and adds none.

**Writing, whole brief.** I found no AI tells, no "not X but Y" construction in the narrator's voice, no tails and no aphorisms. The close, "no teaching of his own, only the common teaching", tells Maximus's own "dogma proprium non habeo, sed commune" (PG90 l.7507-7508). It is in the source's own form and is attributed.

#### New findings

- **R2-A-M1 MINOR (brief l.7; item 4; a fix's sentence reads badly aloud).** "Later the emperor Constans, in an edict, the Typos, forbade talk of one will or two." Two appositives in a row split the subject from its verb. When the sentence is heard, "the Typos" can be mistaken for the subject. Fix, with the same 16 words, ending on the name the next paragraph picks up: "Later the emperor Constans forbade talk of one will or two in an edict, the Typos." Scored: 405 words, FK 8.16, Flesch 61.24.
- **R2-A-M2 MINOR (card `uncertain` 9, l.48; item 1; the card misdescribes the brief after A-M4).** "The brief names the last two." Since A-M4, the brief names the Typos but does not name the Ekthesis. It tells of it as "an earlier statement by the patriarch Sergius". Fix: "The brief tells of the last two."

**Verdict: NOT CLEAR.** All 13 R1 findings are resolved. There are 0 new blocking points and 2 minor ones.

---

### Martin I of Rome

| R1 finding | Verdict | Evidence |
|---|---|---|
| A-B2 (105 told as settled) | RESOLVED in the brief | Brief l.5 gives no count. The count is heard only inside Bede's quotation (l.13). The card's `keyWorks` 3 still tells the count in the narrator's voice (R2-A-M3). |
| A-M13 (Duchesne's year bare) | RESOLVED | Brief l.11. The prisoner arrives "septimo decimo die Septembrii" (M10 l.87655-87656), then serves "nonaginta tres dies" (l.87745) and "octoginta quinque dies post primas nonaginta tres" (l.88181-88182). His letter has him "navigantes sancta quinta feria cenae domini" (l.88441-88442). "The next spring" commits to no year and fits both Duchesne and the Breviary. |
| A-M14 (edition's year given to Bede) | RESOLVED | Brief l.13 runs 25 words. John is "abbat of the monastery of St. Martin, who came lately from Rome, by order of Pope Agatho"; he "brought with him the decision of the synod of the blessed Pope Martin and 105 bishops" and gave it to be transcribed in Benedict's monastery "at the mouth of the river Were" (GILES l.10355-10406). The quotation is verbatim. Card l.29: Heathfield, "the seventeenth of October, the eighth indiction", with Theodore "archbishop of the island of Britain, and of the city of Canterbury" presiding over "the other venerable bishops of the island of Britain"; the synod "held in the city of Rome, in the time oF the blessed Pope Martin … we receive" (l.10283-10336). Card l.30, "lately", matches l.10359. |
| A-M15 (his stand left to inference) | RESOLVED | Brief l.5, "for teaching one will", rests on Bede's "principally against those who taught but one will and operation in Christ" (GILES l.10403-10405). The joined sentence on l.7 rests on "Deinde directus est ab imperatore Theodorus exarchus, qui cognomento Calliopa dicitur" after Olympius's failure and death (M10 l.82111-82113, with Olympius at l.82119-82170). "his friend Theodore" fairly renders "sincera affectione dilecto fratri" (l.87160). The term "exarch" is R2-A-M4. |
| A-M16 (gloss on "illuc") | RESOLVED | Card l.16: "exceptis dumtaxat quibusdam illuc venientibus servis Dei causa eleemosynae, quibus & modicum quid praebuimus minime ad Saracenos transmissum" (M10 l.87253-87257). |
| A-M17 (the letter's addressees) | PARTLY | Card l.31. The addressees and the 125 bishops are now right (NPNF l.25508-25526), and so is Percival's summary (l.25595-25597). But "that council" has no antecedent on the card (R2-A-B1). |
| A-M18 (blinding: one witness) | RESOLVED | Card l.42. The Breviary's fifth lesson says the lictor "was struck with blindness" (BREV l.89131-89152). |
| A-M19 (Binius's 110) | RESOLVED | Card l.49. Binius reads "fynedo contum decem epifcoporum colletta" (M10 l.117106-117107), against Migne's "centum et quinquaginta episcoporum synodo" (THEO l.60748-60749). The records carry the third side with its OCR form (records l.145, 200). |

**Changed sentences, checked in full.** Brief l.3, 5, 7, 11 and 13, and card l.16, 29, 30, 31, 42 and 49. Apart from the findings below, each says what its lines say, with its witness attached.

**Writing, whole brief.** I found no AI tells, contrasts, tails or aphorisms. The close tells his letter, "Dominus enim prope est, & quid sollicitus sum?" (M10 l.88548-88555), and is attributed.

#### New findings

- **R2-A-B1 BLOCKING (card `legacy.traces` 3, l.31; items 1 and 4; a fix left a reference pointing to the wrong council).** The trace reads "for the legates they sent to that council". The Martin card never names the council of Constantinople of 680-681. The only councils before this trace are Heathfield (trace 1) and Martin's synod (trace 2). Read in order, "that council" points to one of them. Heathfield is the likelier reading, since trace 2 puts Agatho's envoy John there. Both readings are wrong: the letter was "an Instruction to the Legates Sent to Attend the Sixth Synod" (NPNF l.25508-25511), which met from 7 November 680 (l.24572). Fix: "Pope Agatho and a Roman synod of 125 bishops wrote to the emperors, for the legates they sent to the council of Constantinople in 680." (25 words.) The second sentence stands.
- **R2-A-M3 MINOR (card `keyWorks` 3, l.24; item 7; the count A-B2 took out of the brief is still told as settled on the card).** "the synod of 105 bishops that condemned…" tells the contested count in the narrator's voice. `uncertain` 9 gives the dispute, but this line does not point to it. Fix: "the synod that condemned Cyrus of Alexandria and Sergius, Pyrrhus and Paul of Constantinople. The Book of the Popes and Bede count 105 bishops. The Book of the Popes copies its account of the Typos from Martin's own speech there, Louis Duchesne says". The 105 is the Book of the Popes' "numero centum & quinque" (M10 l.82055) and Bede's (GILES l.10403).
- **R2-A-M4 MINOR (brief l.7 and card `uncertain` 6, l.46; item 4; an undefined term in a changed sentence).** "the exarch Olympius … a later exarch" gives a general listener a Byzantine title with no gloss. The Book of the Popes sends Olympius "ad regendam omnem Italiam" (M10 l.82126). After Olympius dies, "Deinde directus est … Theodorus exarchus" (l.82111-82113). Fix, brief, with the same 21 words: "After Olympius, governor of Italy, failed to seize him, the Book of the Popes says, his successor, Theodore Calliopas, took him." Scored: 405 words, FK 6.83, Flesch 71.57. Fix, card `uncertain` 6, first sentence: "Whether he backed Olympius, the emperor's governor in Italy, against the emperor." Card `uncertain` 7's "pope and exarch" can then stand.

**Verdict: NOT CLEAR.** Of the 8 R1 findings, 7 are resolved and 1 is partly resolved. There is 1 new blocking point (R2-A-B1) and 2 minor ones.

---

### Timothy I of Baghdad

| R1 finding | Verdict | Evidence |
|---|---|---|
| C-B1 (Elias given Seleucia) | RESOLVED | Card l.8 and l.52. Elias gives only "Institutus est Timotheus die dominica 7° iyyar anni 1091 Graecorum" (ELIAS l.3716-3717). Chabot has "intronisé à Séleucie, après huit mois de violentes contestations" (CHABOT l.40258-40259), BH has "deduxerunt Seleuciam" (l.9612), and Amr has "consecraverunt Modainae" (AMR l.13017). |
| C-B2 (Peter put in Timothy's time) | RESOLVED | Card l.29. Thomas's list is "the Bishops of whom the old man said that there should be two and forty" (TM l.20112-20113). Elijah appears in it as "Mar Eliya … elected Bishop of Mukan" (l.20157-20158), and Thomas writes "Mar Elijah, the men who were ordained by the pious Mar Timothy" (l.21004-21005). |
| C-B3 (Assemani's reading told as Amr's) | RESOLVED | Brief l.7 and card l.24 and l.49. Amr has "Saepe admodum eum accersebat Hadi chalipha ut cum eo colloqueretur de religione … [disceptaretque]" (AMR l.13027-13029), and Assemani has "Amrus … Hadium pro Mohdio legit" (ASSEMANI 3.1 l.29815-29816). "Argue" leans on Gismondi's bracketed "disceptaretque", which is acceptable. Card l.49's new wording is empty (R2-C-M3). |
| C-M1 (Amr bare) | RESOLVED | Brief l.1 and card l.9. |
| C-M2 ("three bishops") | RESOLVED | Brief l.5, "three persons" (TM l.21976-21977). |
| C-M3 ('Abdisho and Elias with no context) | RESOLVED | Brief l.7 and l.9. Mai heads him "Ebediesu Sobae, id est Nisibis, metropolitae" (MAI l.171). Bar Hebraeus in the same paragraph is still bare (R2-C-M4). |
| C-M4 (closing line; period) | RESOLVED | Brief l.11. The words "among the Indians, the Chinese, the Tibetans, the Turks" are verbatim (MINGANA l.1687-1688), and the source runs on with ", and in all the provinces". "Translates" is fair: Mingana read the Syriac "in an unpublished MS. of my own collection" (l.1702-1703) and gives it in English. |
| C-M5 ("Fertur" dropped) | PARTLY | Card l.30. The hedge is back in the first sentence, but the split cut it from the second (R2-C-M1). |
| C-M6 (no antecedent; "first") | RESOLVED | Card l.36-37. The boy "made his passage [thither by way of] this monastery" (TM l.17171) and hears "Forty and two years shalt thou stand at the head" (l.17212). The card also has "it was here pointed out to him" (l.21413-21414). |
| C-M7 ("Chabot follows him") | RESOLVED | Card l.46. Chabot's note gives "le vendredi 9 janvier 823" (CHABOT l.40361), and his index gives "9 janv. 825" (l.49679). |
| C-M8 (death-year witnesses) | RESOLVED | Card l.47 adds Mari. The records add Malech's "780-820" and Mingana's "779-823" (records l.166-167). |
| C-M9 (OCR flags, Timothy) | RESOLVED | A sample of the forms R1 named is now flagged in the records: "quadragesiraotertio", "Maraun", "dooueritque", "rcgni", "respoudc", "cliristianorum", "nutn- mis", "catbolicus", "Tmotheua" and "vestiraenta". "responde" is corrected. |

**Changed sentences, checked in full.** Brief l.1, 5, 7, 9 and 11, and card l.8, 9, 24, 29, 30, 36, 37, 46, 47, 49 and 52. Apart from the findings below, each says what its lines say, with its witness attached.

**Writing, whole brief.** I found no AI tells, contrasts, tails or aphorisms. The quotation that closes the brief is attributed, and its period sits outside the marks.

#### New findings

- **R2-C-M1 MINOR (card `legacy.traces` 2, l.30; items 1 and 7; the C-M5 split cut the hedge from a clause it governs).** Bar Hebraeus's whole report stands under "Fertur": "episcopos … alba gessisse vestimenta … carnem manducasse et duxisse uxores, et praeterea catholico Seleuciae non paruisse" (BH l.9750-9805). Mingana gives the same in English, "It is said that … were not under the jurisdiction of the Catholicos of Seleucia" (MINGANA l.1721-1725). The card's second sentence, "They had not obeyed the catholicos of Seleucia.", now reads as fact. Fix, second sentence: "It was also said that they had not obeyed the catholicos of Seleucia." (13 words.) The third sentence stands, since "Dicebant enim" is Bar Hebraeus's own statement.
- **R2-C-M2 MINOR (card `uncertain` 2, l.45; item 2, punctuation).** In `"truth acted with subtlety."` the period sits inside the marks, but the source runs on: "truth acted with subtlety and performed its work" (TM l.17293). Fix: `though "truth acted with subtlety".` The comma in `"by fraud,"` stands, because the heading has "BY FRAUD, * LIKE JACOB" (l.17242).
- **R2-C-M3 MINOR (card `uncertain` 6, l.49; item 4; a fix's sentence says nothing).** "Joseph Assemani reads Amr's report of al-Hadi's debates as naming al-Hadi instead." As worded, it says that a report about al-Hadi names al-Hadi, which tells the reader nothing. Assemani's point is that Amr puts Hadi where 'Abdisho has Mahdi: "Hadium pro Mohdio legit" (ASSEMANI 3.1 l.29815-29816). Fix: "Joseph Assemani takes Amr's report of debates with al-Hadi to be the same disputation, with al-Hadi in place of al-Mahdi." (20 words.)
- **R2-C-M4 MINOR (brief l.9; item 4; a name with no context, in the paragraph C-M3 fixed).** "Bar Hebraeus puts his death…" is the brief's only mention of him, and a general listener would not know him. The brief already glosses 'Abdisho and Elias on the same ground. His Chronicon Ecclesiasticum is held (BH, file title). Fix: "The historian Bar Hebraeus puts his death in the Arab year that began in June 819." Scored: 405 words, FK 7.27, Flesch 66.89.

**Verdict: NOT CLEAR.** Of the 12 R1 findings, 11 are resolved and 1 is partly resolved. There are 0 new blocking points and 4 minor ones.

---

### Photius of Constantinople

| R1 finding | Verdict | Evidence |
|---|---|---|
| C-B4 (false absence: 879 acts, Will) | RESOLVED | Card l.25 and l.43. The acts read "aut adjicere vel demere in tradito nobis a sancta & oecumenica Nicaeae primum magna synodo, anathema sit" (MANSI17 l.53399-53432). The note reads "postremas istas duas actiones, nempe quae sexta & septima appellantur, confictas esse ab ipsomet Photio" (l.52604-52606), and Will has "In ultimo consessu decretum est" (WILL l.3975-3979). The records carry the acts, the note and Will. A new defect in l.43 is R2-C-M6. |
| C-B5 (false absence: Will's 891) | RESOLVED | Card l.4 and l.47. Will says "ex dignitate expulsum in monasterium inclusit, ubi anno 891 decessit" (WILL l.3988-3989). Will names no monastery, so Symeon's Gordon stands on its own. The birth-year item is scoped to the card's sources. |
| C-M10 (Ignatius bare) | PARTLY | The identifier is added in brief l.5 and card l.31. But "his rival" still follows Nicetas, so Ignatius still reads as Nicetas's rival. R1 named this ambiguity, and the fix kept it (R2-C-M5). |
| C-M11 ("printed the letter") | RESOLVED | Brief l.7. |
| C-M12 (Nilus unmarked) | RESOLVED | Brief l.9 rests on the acts. Mansi heads Nilus "Ex Nilo Rhodi metropol. schismatico" (MANSI17 l.38859). |
| C-M13 (comma inside the quote) | RESOLVED | Brief l.13. The quotation is verbatim, and the source has "and record it ;" (FREESE l.1740-1741). |
| C-M14 (Symeon's cause told as fact) | RESOLVED | Brief l.9 and card l.41. Symeon: "latronem eum et parricidam ac divina indignum communione dicere ausus est. Qua ille re ira accensus Romam misit, tomoque impetrato … Photium sede ejicit" (PG109 l.63686-63690). LP2: "secundum Romanae aecclesiae constitutum, pervasorem Photium pepulit" (l.53411-53412), with "novus imperator Basilius" (l.53407) supporting "new". |
| C-M15 (Bury read as a view) | RESOLVED in substance | Card l.12 and l.45. Freese's note reads "To the caliph of Bagdad ; according to others, to Persia, or one of the Eastern emirs (Bury)" (FREESE l.1725-1726). Both lines put a period inside the marks of "to Assyria" (R2-C-M7). |
| C-M16 (held sides left out) | RESOLVED | (a) Card l.27: "et ab unionis sociis ad suas sententias tuendas in usum conversus est" (WILL l.3488-3489). (b) Card l.44: "Impudentissime autem Photius papam decepit de synodi decretis … palam anathemate Photium percussit, id quod a tribus sequentibus papis, Marino, Hadriano III., Stephano V. … repetitum est" (WILL l.3980-3987). (c) Card l.34: the spatharius's words are at LP2 l.53540-53545. The term "spatharius" is R2-C-M8. |
| C-M17 (OCR flags, Photius) | RESOLVED | "mySleria", "egct", "indignem", "institulorem", "MichaeUs" and "noclu" are each flagged in the records. |

**Changed sentences, checked in full.** Brief l.5, 7, 9 and 13, and card l.4, 12, 25, 27, 31, 34, 41, 43, 44, 45 and 47. Apart from the findings below, each says what its lines say, with its witness attached. Card l.25 tells the decree first and names its witnesses in the next sentence. The dispute over the sessions' authenticity is on the same card (l.42-43), so the line passes.

**Writing, whole brief.** I found no AI tells, contrasts, tails or aphorisms. "Yet he calls Photius the first scholar of his age" turns on a real fact: a hostile witness praises him.

#### New findings

- **R2-C-M5 MINOR (brief l.5 and card `uncertain` 2, l.39; item 4; the ambiguity C-M10 named is still there).** In "Nicetas the Paphlagonian, who wrote the Life of his rival, the patriarch Ignatius", "his" sits next to Nicetas and reads as Nicetas's. The same holds for "Nicetas the Paphlagonian wrote the Life of his rival Ignatius" on the card. Fix, brief, with the same 18 words: "Nicetas the Paphlagonian, who wrote the Life of Photius's rival, the patriarch Ignatius, was an enemy too." Scored: 404 words, FK 7.11, Flesch 66.98. Fix, card: "Nicetas the Paphlagonian wrote the Life of Photius's rival Ignatius."
- **R2-C-M6 MINOR (card `uncertain` 6, l.43; items 4 and 1; a reference with no antecedent, and a heading told ungrammatically).** In "says Photius made up those last two sessions himself", "those" refers to nothing. The item never says the decree stands in the sessions the note disputes, and so the note's point is lost. The note says Photius made up the sixth and seventh sessions and set in them "definitionem … nihil videlicet esse adjiciendum symbolo" (MANSI17 l.52604-52628). Also, "whom Mansi heads a schismatic" does not parse. Fix, third and fourth sentences: "An unsigned note printed with them says Photius made up the last two sessions himself, with their decree on the Creed. Nilus of Rhodes, whom Mansi's heading calls a schismatic, reports the same decree." (21 and 14 words.)
- **R2-C-M7 MINOR (card `keyWorks` 1, l.12, and `uncertain` 8, l.45; item 2, punctuation, in the strings C-M15 changed).** Both lines have `"to Assyria."`, but the source runs on: "ambassador to Assyria ^ had been confirmed" (FREESE l.1705-1706). Fix: `…as ambassador "to Assyria".` and `His embassy "to Assyria".`
- **R2-C-M8 MINOR (card `legacy.remembered` 4, l.34; item 4; an undefined term in the line C-M16c changed).** "Basil's spatharius" leaves a Byzantine rank unglossed. LP2 calls him both "Basilius legatus imperatoris" (l.53422) and "spatharius" (l.53542). Fix, first sentence: "In Hadrian II's Life, Basil's envoy, his sword-bearer, says the book falsely carried Basil's signature after Michael's." (17 words.) "Sword-bearer" matches the Martin card's rendering of the same office.

**Verdict: NOT CLEAR.** Of the 10 R1 findings, 9 are resolved and 1 is partly resolved. There are 0 new blocking points and 4 minor ones.

---

### Verdicts

- **Maximus the Confessor:** NOT CLEAR. All 13 R1 findings are resolved. There are 0 new blocking points and 2 minor ones (R2-A-M1 and R2-A-M2). The brief's Flesch is 61.24 before and after its fix.
- **Martin I of Rome:** NOT CLEAR. Of the 8 R1 findings, 7 are resolved and A-M17 is partly resolved. There is 1 new blocking point, R2-A-B1: "that council" in the Agatho trace points to Heathfield or Martin's synod. There are 2 minor ones (R2-A-M3 and R2-A-M4).
- **Timothy I of Baghdad:** NOT CLEAR. Of the 12 R1 findings, 11 are resolved and C-M5 is partly resolved. There are 0 new blocking points and 4 minor ones (R2-C-M1 to R2-C-M4).
- **Photius of Constantinople:** NOT CLEAR. Of the 10 R1 findings, 9 are resolved and C-M10 is partly resolved. There are 0 new blocking points and 4 minor ones (R2-C-M5 to R2-C-M8).

Four brief fixes carry into the audio: R2-A-M1, R2-A-M4, R2-C-M4 and R2-C-M5. Each was scored above, and each keeps the brief at 405 words or fewer, with FK at most 10 and Flesch at least 60.
