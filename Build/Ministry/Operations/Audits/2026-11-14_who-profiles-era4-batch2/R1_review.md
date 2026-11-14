# R1 review: era 4 batch 2

Round 1 ran in four parts, each by a fresh Opus agent that had not seen the drafting. The parts follow, unchanged.

## R1 review, part A: Maximus the Confessor, Martin I of Rome (era 4 Who batch 2)

Reviewer: independent Opus, first sight of these drafts. I edited no profile, records or notes file. I made no git, web, paid or model calls, and used local scripts only.

### Method

Bar: `Who_Profile_Pattern.md` checklist 1 to 14; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; the Decision-Log entries for era 3 batches 6 to 8 and era 4 batch 1 with their cap rulings; the era 4 scan's rulings block; part A of the era 4 batch 1 R1 review for format. For each id I read the `.brief.txt`, `.card.json`, `audio/<id>.audio.txt`, the scratch records and the drafter's notes. I opened every cited line in its vendored file and read it in context, folding OCR noise, long s, double spaces and hyphen breaks.

Files: PG 90 (`maximus-confessor_relatio-motionis-disputatio-bizyae-grc-lat_migne-pg90.txt`, "PG90"), PG 91 (`maximus-confessor_disputatio-cum-pyrrho-pg91-grc-lat_migne1860.txt`, "PG91"), Theophanes PG 108 ("THEO"), Mansi 10 ("M10"), Mansi 11 ("M11"), NPNF 2.14 (`npnf214_seven-ecumenical-councils.xml`, "NPNF"), Duchesne LP 1 ("DUCH"), Foulke's Paul the Deacon ("FOULKE"), Giles/Jane Bede ("GILES"), Plummer's Bede v1 ("PLUMMER"), the Bute Breviary ("BREV") and the England Missal.

Both men's own words are held only in Latin, so both briefs tell them in modern words without quotation marks. I checked each telling against the Latin in context (see "Sentences checked"). Neither brief presents a modern telling as a quotation. The one quotation in either brief (Bede, in the Martin brief) is verbatim English. The Maximus card puts two Latin renderings in quotation marks (A-M8).

Absence searches across `cic/texts/`: "Maximus (the) Confessor" in every file (16 hits; only Latin, Greek, German and passing English mentions, no English of his works or trials); "Leo Allatius" and "J. A. Fabricius" (both held); a birth year in PG 90 and PG 91; an author line for the Relatio motionis (none, though Combefis's notes discuss the Anastasii at PG90 l.16290-16390); Maximus in the Constantinople III acts in M11 (only Macarius's professions, l.35300-35322 and 74360-74367; l.53042 and 101709 are editors' notes); Maximus and Martin in NPNF; the deposition of Macarius in NPNF; Bede's date for Heathfield in GILES and PLUMMER; "typum exponere" in M10 (Martin's speech is held in the Lateran acts, l.89931-89940, as well as copied into the Book of the Popes, l.81990); the blinding of Olympius's sword-bearer outside the Book of the Popes; the synod's count in every held witness.

Readability comes from `engine.m1.gates.grade_text`, run from the repo root. I applied every suggested brief fix to scratch copies and scored them again: `/tmp/claude-0/-home-user-CIC-Project/46148d77-0e3f-56b5-a386-901106a72590/scratchpad/review/fixA/maximus-the-confessor.fixed.txt` and `/tmp/claude-0/-home-user-CIC-Project/46148d77-0e3f-56b5-a386-901106a72590/scratchpad/review/fixA/martin-i-of-rome.fixed.txt` (replacement lists `max.json` and `mar.json` in the same folder).

**Applies to both.** I checked by script that each audio file equals its brief once `[calmly] ` (at the start) and `[warmly] ` (at the start of the last paragraph) are taken out. No tag appears in a brief or card. Every brief fix below has to be carried into the audio. Both cards follow batch 1's field order (`name` through `sources`, `legacy.traces` then `remembered`, `sources.ownWords` then `about`), have no null or empty fields, and every `sources` file exists and holds the named work. Both card traditions are census movement names whose dates fit: The Byzantine Imperial Church (Heraclian & Iconoclast Eras), 622-843, names both men; Latin African Christianity under Byzantium, 533-c. 698, names Maximus. The drafts carry no list lines, so the list-line half of item 14 was not checked.

**The 680-681 council.** NPNF holds Percival's English. The council met from 7 November 680 to 16 September 681 (NPNF l.24572-24575). Its definition declares "two natural wills and two natural operations" that "are not contrary the one to the other", the human will "subject to his divine and omnipotent will" (l.25862-25869). It does not name Maximus or Martin in its own voice. Macarius of Antioch's profession, read there, curses "infaustum Maximum cum impiis ejus discipulis" (M11 l.74364-74367; again at l.35300-35322). The council then anathematizes Macarius (NPNF l.25749) and deposes him (l.25997). It also anathematizes Sergius, Cyrus, Pyrrhus and Paul (l.25744-25747), the men Martin's synod condemned. Pope Agatho's letter, written with a Roman synod of 125 bishops to the emperors as instruction for the legates (l.25511-25526), calls the two-wills faith the one "set forth in a council over which Pope Martin presided" (Percival's summary, l.25595-25599). The Maximus card's first two traces and the Martin card's Agatho trace describe the council as those lines do, with one slip in the Agatho trace (A-M20). The Maximus card's Macarius trace leaves out the council's verdict on Macarius (A-B1).

**Martin's trial and exile: the witnesses.** Seizure, the Lateran church, the voyage, Naxos and Cherson come from Martin's own letters (M10 l.87158-87547, 88401-88560). Arrival, prison, trial, stripping, the chains and the death and burial come from the Commemoratio (l.87561-88357). Its writer calls himself "indignus ministerii beatissimi et pretiosi sacerdotis nostri" (l.87591-87592), and Duchesne calls him "un des clercs de sa suite" (DUCH l.162992-162995). The brief and card keep the two witnesses apart correctly, and "one of his clergy" rests on both lines. The census story's "Martin's own account ... describes the sentence" is wrong, as the drafter's notes say.

---

### Maximus the Confessor (major; 404 words, about 2:30; FK 8.45, Flesch 60.88)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (A-B1, A-M5, A-M6) |
| 2 | Quotes verbatim | FAIL (A-M8; card only, the brief has no quotation) |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (A-M3, A-M4, A-M7, A-M10, A-M11) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | FAIL (A-M2) |
| 7 | Contested claims both sides | PASS (the Lateran presence, the Life's author, the last exile and the three years are each on the card with both sides) |
| 8 | Common names | FAIL (A-M1, A-M9) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | FAIL (A-M3, A-M4) |
| 11 | Readability | PASS (Flesch 60.88, just above the floor; rescored after fixes) |
| 12 | Card order, fields, caveat repeated | PASS (`uncertain` 1 and 2 repeat the Life's and Duchesne's caveats) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Records | FAIL (A-B1, A-M12) |

**Sentences checked and found faithful.**
- P1: the Relatio, "circa solis occasum, venientes, duo mandatores cum decem excubitoribus, tulerunt eos e navi nudos nudique pedes" (PG90 l.6779-6787). "Without cloaks" takes the Life's "nudis pedibus ... ac sine amiculo" (l.4976). The senate, the sacellarius "cum multa ira et furore", and the exchange "Christianus es? ... Gratia Christi ... Christianus sum. Cui ille, Non est verum. Respondit ... Tu dicis; sed Deus scit esse me Christianum, et perseveranter esse" (l.6791-6803). The telling says what the Latin says. "Old" is "Senem".
- P2: "Tu enim solus Egyptum et Alexandriam et Pentapolim et Tripolim et Africam Saracenis tradidisti" (l.6813-6815). Naming three of the five places changes no sense. Duchesne dates the envoys' arrival to just before Pentecost, 17 May 655, "comme il résulte des dates fournies par les interrogatoires de saint Maxime" (DUCH l.163416-163421). The record has the envoys arrive "heri" on the evening of the first hearing (PG90 l.7497, 7648-7651). M11's admonition also has "anno 655" (l.808-812).
- P3: the Life, Constantinople, noble parents, Heraclius's "eorum qui a secretis imperatori essent, principem", and the monastery at Chrysopolis "cum Monothelitarum dogma consurgens" (PG90 l.3534-3538, 3710-3718, 3753-3762). The heading names it a Life of a saint and confessor (l.3371-3378).
- P4: the Typos as "nec unam, nec duas voluntates, aut operationes ... definiens confiteri" (M10 l.81990-81996, and in Martin's speech, l.89931-89938). Pyrrhus "ex-patriarcha Constantinopol." (PG90 l.279-280); the debate "in Africa" (PG91 l.15055-15060; PG90 l.7499-7504).
- P5: "quatuor concilia ejecerunt, per illa novem capitula ... et per ecthesim, quae in hac urbe Sergio auctore edita est; et per typum ... ipsique seipsos toties deposuerunt" (PG90 l.7535-7546). "Plane necesse ... Nam Patres palam dicunt, neque esse neque cognosci ullam quoquomodo naturam, absque substantiali sua operatione" (l.7690-7698). Both tellings say what the Latin says. "Two" wills is the hearing's sense (l.7655-7660, "secundum utrumque").
- P6: Theophanes, "Maximus ex Africa Romam transfretatus, Martini papae sanctum in Deum ardorem accendit ... Sergium et Pyrrhum, Cyrum et Paulum anathemate perculerunt" (THEO l.60745-60752). The year 649 and the condemnation are the Book of the Popes' (M10 l.82052-82082).
- P7: Bizya "provinciae Thraciae castro" (PG90 l.8274-8275). Theodosius's pledge, Maximus's "Suscipiant horum damnationem, quae Romae ... synodice edita est", Theodosius's "Non habuit robur ... injussu imperatoris", and the answer on the synods "contra homoousion" (l.9566-9586). The tellings say what the Latin says. "Nicene faith" for homoousion is fair.
- P8: the condemnation of "sanctum Maximum, ejusque discipulum beatum Anastasium" and the other Anastasius (l.11469-11477); the decree on tongue, right hand, the twelve regions and Lazica (l.11518-11538).
- P9: the envoy's letter, the litter of woven branches, "in castro Schemari ... juxta gentem illorum qui dicuntur Alani" (l.11685-11704); the foretold day and its fulfilment, 13 August, "feria septima", fifth indiction (l.11744-11752); Migne's running head "ANNUS 662" (l.140). The writer is the envoy: he names the disciple separately as "dominum vero Anastasium abbatem" (l.11703).
- P10: "Ego dogma proprium non habeo, sed commune Ecclesiae catholicae" (l.7507-7508), said to Troilus and Sergius Eucrates.

**Card.** I checked these against their lines:
- `otherNames`: Fabricius's "Theologus et confessor a Graecis appellatur" (PG90 l.275-276).
- `dates`, `place` and `role`: Fabricius on 645, "abbas Chrysopolitani" (l.274-281); "Electus praepositus" (l.3751); "in adverso situm littore" (l.3762); Schemaris; "feria septima".
- `keyWorks` 1 and 3 (PG91 l.15117-15119; PG90 l.17168-17180, the salutation "Maximus humilis monachus").
- `legacy.traces` 1 and 2 (NPNF l.24572-24575, 25862-25869).
- `legacy.remembered`: the three lamps (PG90 l.11756-11765); Theophanes on tongue and right hand and "quae multa adversus ejus impietatem ... conscripsisset" (THEO l.63016-63024); Fabricius (PG90 l.275-277).
- `uncertain` 1 to 6 and 9: Fabricius and Allatius (l.282-286); the Life's "(Anastasius scilicet apocrisiarius) tradidit" (l.6540-6541); Duchesne (above); Binius, "Quod in actis concilii nulla mentio reperiatur Maximi ... non decidendi & subscribendi, sed tantum consulendi facultatem" (M10 l.117103-117112); "Maximus monachus, similiter." among the Greek abbots' and monks' petition (l.92105-92140, 92672); Theophanes on Cherson (THEO l.60845-60849); "[triennium]" (PG90 l.6570); 8 June and 13 August (l.11685-11688, 11748-11752); the nine chapters.

**Drafter's census differences, checked.** 2 (arrest in Rome with Martin) is confirmed: the Life's section XVII brings both to Constantinople and does not set an arrest in Rome (PG90 l.4905-4930). 3 (no author line for the Relatio) is confirmed. 1 is right in its conclusion but rests on an incomplete reading (A-B1).

#### Findings

- **A-B1 BLOCKING (card `legacy.traces` 3; notes "Census differences" 1; item 1 and the coordinator's question on the 680-681 council).** The trace tells that Macarius of Antioch's profession cursed Maximus at the council, and stops there. The held council answered that profession. It cried "To Macarius the heretic, anathema!" (NPNF l.25749), and its sentence says "with the best of cause we anathematize and depose Macarius, who was bishop of Antioch" (l.25997). Read after traces 1 and 2, the trace as it stands leaves open how the council treated the curse, and the notes rest their census difference on the curse alone. Fix, for `traces` 3: "At the same council, Macarius of Antioch held to one will. His profession of faith cursed Maximus and his disciples among the heretics. The council anathematized Macarius and deposed him." (8, 11 and 7 words; the quotation marks around "Maximus" also go, A-M8.) In the notes, change difference 1 to: "The held council text defines two wills and does not name him. Macarius's profession read there curses him, and the council anathematizes and deposes Macarius (NPNF l.25749, 25997)." Add the deposition to the records claim on Macarius.

- **A-M1 MINOR (brief P1; item 8; the subject's own name at first mention).** "the old monk Maximus" carries no identifier, and the name is common (Maximus of Turin, of Riez, the Cynic in NPNF). The record's epithet is the Greeks' "confessor" (PG90 l.275-276). Fix: "At sunset, guards took the old monk Maximus the Confessor and a companion off a ship at Constantinople, barefoot and without cloaks." (22 words.)

- **A-M2 MINOR (brief P2; item 6; the main witness for the trials is partisan and unmarked).** The Relatio calls him "Dei servus" and "sanctus senex" throughout (PG90 l.6802, 8276), and the court's charges reach us only through it and the last sentence. The card says so (`uncertain` 8). The brief does not. Fix, splitting the 22-word sentence: "The scene comes from his own side's record of that hearing. Louis Duchesne, editor of the Book of the Popes, dates it to 655."

- **A-M3 MINOR (brief P4; items 4 and 10; two facts with no link, told out of order).** "Later the emperor Constans ... In Africa, Maximus had debated Pyrrhus" puts the 648 Typos (FOULKE l.9936-9939) before the 645 debate (PG90 l.279-281) and joins them with nothing. "Later" has no point to count from. Fix: "In Africa he debated Pyrrhus, a former patriarch of Constantinople. Later the emperor Constans, in an edict, the Typos, forbade talk of one will or two."

- **A-M4 MINOR (brief P5; items 4 and 10; a scene with no anchor, and an undefined term).** P5 returns to the first hearing's evening (PG90 l.7497-7546) straight after P4's Africa and Typos, so the listener cannot place "Asked why". "Ekthesis" is never explained; the Relatio calls it the statement issued in the city "Sergio auctore" (l.7539-7540). Fix: "His questioners asked why he shunned communion with Constantinople's church. He named the Typos and an earlier statement by the patriarch Sergius." (Card `uncertain` 9 still holds: "The brief names the last two.")

- **A-M5 MINOR (brief P8; card `uncertain` 1; item 1; "followers" for both men is the Life's and Theophanes's word, and the editor disputes it for the envoy).** The sentence calls only one Anastasius "discipulum" (PG90 l.11469-11473). Combefis's notes say the envoy and Maximus were "quasi sodales ..., non alter alterius discipulus", and that Maximus "nunquam tamen ... discipulum vocat" the envoy (l.16351-16362, under "FR. COMBEFISII NOTAE AD VITAM S. MAXIMI", l.15517). Fix, brief: "A synod then condemned him with two companions, both named Anastasius." For `uncertain` 1, add: "François Combefis, who edited it, notes that Maximus never calls the envoy his disciple." (15 words.)

- **A-M6 MINOR (brief P9; items 1 and 4; a witness came loose, and a name with no context).** "He foretold the day of his death and died on it" tells a prophecy in the narrator's voice; the envoy is attached only to the sentence before. "By Migne's date" means nothing to a listener. Fix: "He foretold the day of his death, the envoy adds, and died on it, 13 August." The year 662 stays on the card (`dates`). If the year is wanted aloud, use instead "..., 13 August, in 662 by Migne's edition", and score again (it adds 4 words to a brief at the cap).

- **A-M7 MINOR (brief P7; item 4; a pronoun with no referent).** "He asked them first" follows a sentence with one bishop in it. "Suscipiant" (PG90 l.9576) means the court's side. Fix: "Maximus asked that the Roman synod's verdict be accepted first."

- **A-M8 MINOR (card `uncertain` 8 and `legacy.traces` 3; item 2; Latin rendered into English inside quotation marks).** "the servant of God" renders "Dei servus" (PG90 l.6802), and "Maximus" renders "infaustum Maximum" (M11 l.74366). Neither is a quotation of the vendored text. Fix: drop the marks ("calls him the servant of God"; "cursed Maximus and his disciples", as in A-B1).

- **A-M9 MINOR (card `dates`, `remembered` 3; item 8; names with no context at first mention).** "by Fabricius's date" is the card's first mention of Fabricius. His initials are held ("J. A. Fabricius", ten files). "Migne sets the year" names Migne with no context. Fix, `dates`: "Debated Pyrrhus in Africa in 645, by J. A. Fabricius's date. Tried at Constantinople in 655, by Louis Duchesne's dates. Died on 13 August, a Saturday, in the fifth indiction, as Anastasius the envoy writes; Migne's Patrologia sets the year at 662". Each sentence runs 15 words or fewer.

- **A-M10 MINOR (card `keyWorks` 2; item 4; the count overread).** "a hundred for each Gospel" goes past "pari quatuor Evangeliis numero, centenis comprehensum capitibus" (PG90 l.76078-76079), which matches the number of hundreds to the Gospels and gives none to any one Gospel. Fix: "four hundred short chapters, set in hundreds to match the four Gospels, sent to Father Elpidius."

- **A-M11 MINOR (card `uncertain` 7; item 4; process register).** "the year in that line is lost in the scan" talks about our OCR. Fix: "His age. Fabricius says he died aged eighty-two; the year in that line cannot be read in the held copy. No held source gives his birth year."

- **A-M12 MINOR (notes, "Searches run"; an absence that does not hold).** "NPNF 14 (no hit for the Confessor beyond the council's text)": NPNF names "St. Maximus the Abbot" on a heresy of his day (l.18898) and "the demands of Maximus Confessor" in the canons of the Quinisext (l.40117). Neither changes the card. Fix: correct the notes line.

After the fixes (A-M1 to A-M7 in the brief; "to noble parents" dropped to stay within the cap, a cut and not a finding): 405 words, about 2:30, FK 8.16, Flesch 61.2, longest sentence 25 words (scratch copy scored).

---

### Martin I of Rome (major; 402 words, about 2:29; FK 6.45, Flesch 73.0)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (A-M14, A-M15, A-M16, A-M17, A-M18) |
| 2 | Quotes verbatim | PASS (Bede; the Breviary's "Martin, Pope of Rome, Martyr" and "worn out by his sufferings for the Catholic faith's sake.") |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (A-M14, a 26-word sentence) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS (his letters and "one of his clergy" in the brief; `uncertain` 1 on the card) |
| 7 | Contested claims both sides | FAIL (A-B2, A-M13) |
| 8 | Common names | PASS |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | FAIL (A-M15) |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | PASS (`uncertain` 1 repeats the own-side caveat) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Records | FAIL (A-M19) |

**The coordinator's question: written from his stand, not his office alone.** Mostly yes. The brief tells the Typos, his speech against Paul, the synod's condemnations, the trial where Troilus cuts off his account of the Typos, his prayer for the faith of Rome, and Bede's copy of the synod's decision. One gap: the brief never says what the synod condemned the patriarchs for, so his position on the wills is left for the listener to infer (A-M15).

**Sentences checked and found faithful.**
- P1: letter XV, "ante altare ecclesiae lectulum meum habebam in quo jacebam"; "tenentes lanceas & spathas suas, quin & arcus suos paratos"; the candles struck "quemadmodum ... in hiemali tempore vento valide flante folia ... cadunt" (M10 l.87316-87339); ill since October (l.87399-87400); "melius judicavi decies mori, quam unius cujuscumque sanguinem in terram fundi" and "dedi meipsum" (l.87435-87444). The tellings say what the Latin says. June 653 is the Breviary's bracket and Foulke's (BREV l.89160-89163; FOULKE l.9966-9970); his letter dates the removal to "tertiodecimo Kalendas Julias" (M10 l.87470-87472). The church is the Lateran (l.87369-87374, 82074-82077).
- P2: "Martinus Theodoro sincera affectione dilecto fratri" (l.87160). Todi in Tuscany (l.81970-81972; BREV l.89110-89111); 649 (BREV l.89114).
- P3: Martin's speech, held in the Lateran acts: Paul urged the emperor "typum exponere"; the Typos "nec unam, nec duas voluntates aut operationes ... definiens confiteri"; the altar "in domo Placidiae ... subvertens", so the envoys could not offer (M10 l.89931-89958). October 649 is Duchesne's five sessions (DUCH l.162757-162758). The condemnation of Cyrus, Sergius, Pyrrhus and Paul (M10 l.82078-82082).
- P4: Olympius sent, "Et non illum omnipotens Deus permisit" (l.82119-82170); Calliopas (l.82111-82118); "in insula Naxia, quoniam ibi annum fecimus" (l.87520-87521).
- P5: the Commemoratio: 17 September (l.87655-87656); "nonaginta tres dies" and "in portatoria sella: erat enim penitus aeger" (l.87746-87755); the oaths, "unius consilii fuit cum Olympio" (l.87790-87826); "Quando factus est typus ... Non inferas nobis hic de fide, de duello nunc scrutaris", from "praefectus Troilus" (l.87734-87745, 87767). The telling says what the Latin says.
- P6: the crowd up to the hippodrome, the stripping, "circumposuerunt ferrea vincula", "dehonestantes per medium civitatis" (l.87877-87996); Paul's plea and "non morieris" (l.88057-88079); "navigantes sancta quinta feria cenae domini" (l.88441-88442); "panis in ea tantum nominetur, non tamen penitus videatur" (l.88456-88457); the forgotten church of Peter and the prayer "praecipue pastorem qui eis nunc praeesse monstratur" (l.88474-88540). Duchesne reads the same complaint (DUCH l.163019-163021).
- P7: 16 September, fourteenth indiction, burial outside Cherson (M10 l.88324-88357). Bede's quotation is verbatim (GILES l.10401-10403); the monastery is Benedict's "at the mouth of the river Were" (l.10367, 10406).
- P8: "De humili namque hoc corpore meo & ipse dominus curam erit ... sive in tribulationibus indefinentibus, sive in modico refrigerio. Dominus enim prope est, & quid sollicitus sum?" (M10 l.88548-88555). The telling says what the Latin says.

**Card.** I checked these against their lines:
- `otherNames`: "Martinus papa" (DUCH l.163024).
- `dates` and `place` (Duchesne's 26 March 655 at l.163015-163016; Blachernes at M10 l.88355-88357).
- `keyWorks` 1, "vivens & moriens ... fidem defendam" (M10 l.87280-87282); `keyWorks` 2 and 3 (DUCH l.163017-163021, 162716-162717).
- `legacy.traces` 2 (GILES l.10358-10361, 10401-10406).
- `legacy.remembered`: BREV l.2524, 88983-89002; the Missal, "XII. St. MARTIN, p. m." (l.35208); "recens revera confessor & martyr" (M10 l.88324); "multa mirabilia operatur usque in hodiernum diem" (l.82236-82237); Gregory II, quoted by Binius (l.82406-82414).
- `uncertain` 3 to 8 and 10: BREV l.89160-89174 and its note l.89250-89252; Binius, "Anno Christi 654. duodecimo die mensis Novembris" (M10 l.82394-82396); Duchesne's 654 (DUCH l.163411-163413, 162832-162833); Foulke on Olympius (FOULKE l.12759-12761) and on the election and Eugenius (l.9937-9942, 9976-9977); the decree's "irregulariter & sine lege" (M10 l.87422-87424); Martin's answer (l.87836-87844); Theophanes on Agatho (THEO l.60850-60852).

**Drafter's census differences, checked.** 1 to 4 and 6 are confirmed against their lines. On 5, letters XVI and XVII, as held, pray for the church and its shepherd and not for the emperor; confirmed.

#### Findings

- **A-B2 BLOCKING (brief P3; item 7; a claim the records tag Contested, told as settled).** "In October 649 Martin gathered 105 bishops at the Lateran" tells the count in the narrator's voice. The records tag it Contested and the card gives Theophanes's 150 (`uncertain` 9; THEO l.60749-60751). The brief already gives 105 with Bede named, in P7's quotation. Fix: "In October 649 Martin gathered his synod at the Lateran. Its bishops condemned Cyrus of Alexandria and Sergius, Pyrrhus and Paul, patriarchs of Constantinople, for teaching one will." (10 and 21 words; the last clause is A-M15.)

- **A-M13 MINOR (brief P6; item 7; a reconstructed year told bare).** "Holy Thursday 655" is Duchesne's year (DUCH l.163015-163016). The Breviary's added dates bring him to Constantinople in September 655 (BREV l.89163-89165), which the card records (`uncertain` 5). The Commemoratio's counts put the sailing in the spring after a winter trial: 93 days and then 85 more from 17 September (M10 l.87748, 88181-88182), with "intolerabilis hiems" at the trial (l.87958). Fix: "Spared death, he sailed for Cherson the next spring, on Holy Thursday."

- **A-M14 MINOR (brief P7; card `legacy.traces` 1 and 2; items 1 and 4; the edition's year given to Bede, and length).** "About 680, Bede says" and "In 680, Bede says" take the year from the bracketed "[a.d. 680.]" in the chapter heads of the English edition (GILES l.10268, 10355). Bede himself dates Heathfield by regnal years, "the seventeenth of October, the eighth indiction" (l.10284-10286). Plummer's Latin carries no year there (PLUMMER l.24160-24220). The brief sentence also runs 26 words. Fix, brief: "Bede says a Roman abbot sent by Pope Agatho brought "the decision of the synod of the blessed Pope Martin and 105 bishops" to Wearmouth." (25 words; Agatho at GILES l.10360-10361.) Fix, `traces` 1: "Bede says the bishops of Britain met at Heathfield under Theodore, archbishop of Canterbury, in the eighth indiction. They received the synod held at Rome in the time of the blessed Pope Martin." `traces` 2: replace "came from Rome that year" with "had lately come from Rome".

- **A-M15 MINOR (brief P3; items 1 and 10; his stand left to inference).** The brief names the men the synod condemned but not their teaching, so the listener hears no statement of what Martin defended. Bede gives the synod's aim, "principally against those who taught but one will and operation in Christ" (GILES l.10403-10405). Fix: the clause "for teaching one will" in A-B2's replacement. To keep the brief within the cap, P4's first two sentences become one: "After the exarch Olympius failed to seize him, the Book of the Popes says, a later exarch, Theodore Calliopas, took him." (21 words; M10 l.82111-82170.) P2's "a letter to Theodore, a dear friend" becomes "a letter to his friend Theodore".

- **A-M16 MINOR (card `keyWorks` 1; item 1; a gloss the Latin does not carry).** "beyond small alms to servants of God who came from there" reads "exceptis dumtaxat quibusdam illuc venientibus servis Dei causa eleemosynae, quibus & modicum quid praebuimus minime ad Saracenos transmissum" (M10 l.87254-87257). The letter says some servants of God came "illuc" for alms and were given a little, none of it sent to the Saracens. It does not say where they came from. Fix: "In the first he denies ever sending letters or money to the Saracens. He gave only a little alms to some servants of God, none of it sent to the Saracens."

- **A-M17 MINOR (card `legacy.traces` 3; item 1; the letter's addressees).** "Pope Agatho wrote to the council" does not fit the held heading. The letter is from "Agatho ... together with all the synods subject to the council of the Apostolic See", to the emperors Constantine, Heraclius and Tiberius, as "an Instruction to the Legates Sent to Attend the Sixth Synod" (NPNF l.25511-25526). Fix: "Pope Agatho and a Roman synod of 125 bishops wrote to the emperors, for the legates they sent to that council. The letter calls the faith of two wills the faith set out in a council over which Pope Martin presided, as Henry R. Percival sums it up." (19 and 25 words.)

- **A-M18 MINOR (card `uncertain` 2; item 1; "its own telling" reads as one witness).** The Roman Breviary's fifth lesson tells the blinding as well: the lictor "was struck with blindness" (BREV l.89131-89152). Fix: "The Book of the Popes adds that the sword-bearer sent to kill him at Mass was struck blind. The Roman Breviary's lessons repeat the story."

- **A-M19 MINOR (records, contested claim "How many bishops"; card `uncertain` 9; a third reading not counted).** Binius, quoting Theophanes in his note on the synod, reads "synodo centum decem episcoporum collecta" (M10 l.117105-117107; OCR "contum decem"), where Migne's Latin of Theophanes reads "centum et quinquaginta". Fix: add the reading to the records' sides with its OCR form. For the card: "Theophanes the Confessor gives 150 in Migne's Latin; Severinus Binius, quoting him, reads 110." (17 words.)

After the fixes (A-B2, A-M13, A-M14, A-M15 in the brief): 405 words, about 2:30, FK 6.7, Flesch 72.2, longest sentence 25 words (scratch copy scored).

---

**Verdicts.**
- Maximus the Confessor: NOT CLEAR. 1 blocking (A-B1, the council's verdict on Macarius) and 12 minor.
- Martin I of Rome: NOT CLEAR. 1 blocking (A-B2, 105 bishops told as settled) and 7 minor.


## R1 review, part B: Dionysius of Tel Mahre, Jacob of Edessa (era 4 Who batch 2)

Reviewer: independent Opus, first sight of these drafts. I edited no profile, records or notes file. I made no git, web, paid or model calls, and used local scripts only.

### Method

Bar: `Who_Profile_Pattern.md` checklist 1 to 14; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; the Decision-Log entries for era 3 batches 6 to 8 and era 4 batch 1 with their cap rulings; part A of the era 4 batch 1 R1 review for format; the era 4 scan rulings (Who_Scan_Era4.md l.1-25). As in those rulings, false absences are blocking wherever they sit, and a missing place on a common name is minor.

For each id I read the `.brief.txt`, the `.card.json`, `audio/<id>.audio.txt`, the scratch records and the drafting notes. I opened every cited line in its vendored file and read it in context, folding OCR noise, long s, double spaces and hyphen breaks. The French (Chabot's Michael, Kugener and Triffaux) and the Latin (Abbeloos and Lamy's Bar Hebraeus, Assemani, Elias of Nisibis, Brooks) were each read against the English telling, sentence by sentence.

Files, with the short names used below: `barhebraeus_chronicon-ecclesiasticum-vol1-lat_abbeloos-lamy1872.txt` (BH1); `barhebraeus_chronicon-ecclesiasticum-vol3-lat_abbeloos-lamy1877.txt` (BH3); `michael-the-syrian_chronique-tome1-livres-i-vii-fra_chabot1899.txt` (MICHAEL1); `michael-the-syrian_chronique-tome2-livres-viii-xi-fra_chabot1901.txt` (MICHAEL2); `assemani_bibliotheca-orientalis-tomus1-de-scriptoribus-syris-orthodoxis-lat_1719.txt` (ASSEMANI1); `elias-of-nisibis_opus-chronologicum-lat_brooks-chabot-csco1910.txt` (ELIAS); `patrologia-orientalis-tomus16_...graffin-nau1922.txt` (PO16); `chronica-minora-pars-prior-versio-lat_guidi1903.txt` (CHRONMIN); `mai_scriptorum-veterum-nova-collectio-tomus10-ebedjesu-synodus-timothei-lat_mai1838.txt` (MAI10); `renaudot_historia-patriarcharum-alexandrinorum-jacobitarum-lat_1713.txt` (RENAUDOT); `nicholas-mystikos_epistolae-with-eutychius-alexandrinus-pg111-grc-lat_migne1863.txt` (PG111); `charon_histoire-des-patriarcats-melkites-t2-t3-fra_1911.txt` (CHARON); `joshua-the-stylite_chronicle_wright1882.txt` (WRIGHT); `jerome_eusebii-chronici-canones-lat_fotheringham1923.txt` (FOTHERINGHAM).

Absence searches across all of `cic/texts/`, OCR-tolerant: Tel Mahre in every spelling (`tell?[ -]?ma[hḥ]r`, `telmah`, `tellmah`: 27 files); Jacob of Edessa in every spelling (`Jacques d'É/Edesse`, `Iacob(us|i) Edess`, `Jacobus Edessenus`: 22 files); "Iacobi Edessae" in Bar Hebraeus's Nomocanon; Philoponus; Bimai/Biamit/Byamit, Almamon/AlMamun, Afschin in Renaudot and Eutychius; Triffaux's first name; grammar near Jacob.

Mechanical, both profiles. I checked by script that each audio file equals its brief once `[calmly] ` (start) and `[warmly] ` (start of the last paragraph) are removed: both match. No tag is in a brief or card. Both cards have batch 1's field order (`name, otherNames, knownFor, dates, place, tradition, role, briefLength, keyWorks, legacy, uncertain, sources`), no null or empty field, and every `sources` file exists and holds the named work. Both card traditions are "Syriac Orthodox Christianity under Islam", a census name (`syriac-orthodox-under-islam`, c. 650-1054) that fits 818-845 and the 680s-708. The drafts carry no list lines, so the list-line half of item 14 was not checked. Every brief fix below must be carried into the audio.

Scored scratch copies with all brief fixes applied: `/tmp/claude-0/-home-user-CIC-Project/46148d77-0e3f-56b5-a386-901106a72590/scratchpad/review/fixB/dionysius-of-tel-mahre.brief.txt` and `/tmp/claude-0/-home-user-CIC-Project/46148d77-0e3f-56b5-a386-901106a72590/scratchpad/review/fixB/jacob-of-edessa.brief.txt`.

---

### Dionysius of Tel Mahre (major, recorder; 405 words, about 2:30; FK 7.2, Flesch 68.5)

**Length call.** I agree that the held life carries the full length. Bar Hebraeus gives a long life (BH1 l.20330-22475): his election in his own words, two journeys to Egypt, the hearing before al-Ma'mun, his report on the Coptic church and the pyramids, his last letter, his death and burial. Michael keeps his preface (MICHAEL2 l.27478-27540). This is the Bede case, not the Nennius case.

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (B-M1, B-M2, B-M4, B-M5) |
| 2 | Quotes verbatim | PASS (brief and card carry no quotation marks; every English telling is a paraphrase with its witness named; the census person-list quote at MICHAEL2 l.36788-36790 re-checked word for word) |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (B-M2, B-M3) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS (Bar Hebraeus and Michael are of his church; the Theophilus charge is "He says" in the brief and "His own side" on the card) |
| 7 | Contested claims both sides | FAIL (B-B1) |
| 8 | Common names | PASS |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS (at the cap) |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | PASS (`uncertain` 1 repeats the brief's "Bar Hebraeus tells this") |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder rule; his own preface and letters are held) |
| — | Records | FAIL (B-B1, B-M6, B-M7) |

**Sentences checked and found faithful.**
- P1: Baghdad and the decree of ten men, BH1 l.21384-21393. The audience "ipsi soli, absque episcopis ... in horto", l.21491-21496. The answer on the cities and the promises, l.21509-21518. The ruling on deposing and on prayer, l.21700-21708. "mense Adar (Martio) anni 1140 (Chr. 829)", l.21714-21715. "Let him come to him alone in his garden" stays neutral on whose the participles are, as the records note.
- P2: Bar Hebraeus born 1226, BH1 l.238-239.
- P3: the years 818 and 845 are the editors' glosses inside Bar Hebraeus's years, l.20614-20616 and l.22470-22471. Kenneshre: "e coenobio Mar Joannis Bar-aphtonii, quod est monasterium Kenserinense", l.20401-20408. "Ait hic ipse Dionysius", l.20416-20417. "apprehenderunt me et custodierunt tanquam malefactorem", "cum fletu et prostrationibus", l.20526-20537. Friday, Saturday and Sunday, l.20612-20620.
- P4: Mohammed, the emir's brother, and the Edessa buildings, l.21042-21058. The storm and Tanis, "ad triginta prope millia", l.21059-21068. The tax, five denarii a head against 48, 24 and 12 zuzae, l.21171-21181.
- P5: BH1 l.21798-21822, with "Eodem anno" at l.21798. "Byamitas, in regione inferiore Aegypti", "pacem noluit", "denuntiavit Byamitas opprimi".
- P6: MICHAEL2 l.27478-27540. "ô mon fils spirituel, Iwannis, métropolitain de Dara"; "de village en village"; "des stations et des prostrations à la porte des princes avec le mépris et l'humiliation"; Theophilus "laissa frauduleusement de côté toutes les histoires dans lesquelles on faisait mémoire de l'un des nôtres". Michael's dates, MICHAEL2 l.39-41.
- P7: BH1 l.22334-22344 and l.22449-22468. "noctes absque somno"; "Fleo ... vitam meam ... quando oculis meis video clades ... filii Ecclesiae"; "Unica igitur mihi superest a malis liberatio, mors scilicet, quam tanquam rem bonam faustamque appeto"; "Hic absolvit beatus ille vir Chronicon suum".

**Card.** Checked and faithful:
- `otherNames`: "Denys de Tell Mahrê" (MICHAEL2 l.27478) and "Dionysius Telmaharensis" (BH3 l.11094).
- `dates` (BH1 l.20614-20616, 22468-22471) and `place`, including the burial at Kenneshre (l.22472) and Baghdad, Tagrit, Damascus and Egypt.
- `keyWorks` 1: MICHAEL1 l.278-279 and the preface.
- `legacy.traces` 1: the marginal note, MICHAEL2 l.28658-28660; Peter of Antioch, l.28025-28029.
- `traces` 2: l.36788-36791.
- `traces` 3: BH1 l.21905-21923. Darics are rightly "gold coins", and "summum pontificatum" is rightly the office of bishop.
- `traces` 4: l.22129-22136. The "and not the granaries" contrast is the source's own ("nec horrea sunt Josephi ... sed").
- `traces` 5: "ordinavit centum episcopos", l.22474-22475; the maphrian, l.22251-22255; Thomas in BH3 l.11090-11094.
- `remembered` 1 and 2: l.22467; MICHAEL1 l.63030-63041.
- `uncertain` 1, 6.

#### Findings

- **B-B1 BLOCKING (records `contested_claims` 1, side 2; card `uncertain` 3; item 7; a witness made to hold a side he does not hold).** The records put Bar Hebraeus's editors on the side against Dionysius's authorship of the shorter chronicle, because they note it is addressed to George of Amida and not to John of Dara. They hold the opposite view. Their note follows Assemani throughout. They read Bar Hebraeus's ending as proof that Dionysius's chronicle ran to about 844, "idque de prolixiori ejusdem Chronico intelligendum". The shorter chronicle of Scete is "ejusdem", the same man's, ending about 775 and dedicated "non Joanni Darensi, sed Georgio Amidae chorepiscopo". They close "Ita Assemanus" (BH1 l.22351-22366). Their earlier note (l.20441-20442 and the lines after) also gives Assemani's two editions, a longer and a shorter. The card's "Bar Hebraeus's editors, citing Assemani, note that it is addressed to George ... not to John of Dara" sits between Assemani and Chabot. Read there, the address seems to count against Dionysius, which the editors never say. The held witnesses against Dionysius are Chabot and Fotheringham. Chabot already writes "Pseudo-Denys" in 1899 (MICHAEL1 l.13650, l.59560), not only in 1901. J. K. Fotheringham, in his Jerome of 1923, calls these "chronica anonymi cuiusdam monachi olim per errorem Dionysio Telmaharensi tributa" (FOTHERINGHAM l.190-191). For Dionysius there is also William Wright, who in 1882 calls the Vatican chronicle Dionysius's "own larger work" (WRIGHT l.293-296).
  - Fix, records: move Abbeloos and Lamy to side 1 with Assemani, citing l.22351-22366. Side 2 becomes Chabot (MICHAEL1 l.13650, 59560; MICHAEL2 l.36430) and Fotheringham (l.190-191). Add Wright to side 1 (l.293-296).
  - Fix, card `uncertain` 3, replacing sentences 2 to 4: "Bar Hebraeus's editors follow him, and say it is addressed to George, a country bishop of Amida, and others, not to John of Dara. In 1895 Chabot published part of it as Dionysius's. By 1899, in his Michael, he calls its author Pseudo-Denys. J. K. Fotheringham, in 1923, says it was once given to Dionysius in error." Each sentence runs 22 words or fewer.

- **B-M1 MINOR (brief P1, l.1; item 1; the scene loses its two hinges).**
  - (a) "Lazarus ... claimed that any ten men of a faith could choose their own leader" drops what makes it a case before the caliph. Lazarus was citing al-Ma'mun's own decree: "nobis edictum datum est" (BH1 l.21500-21505). The decree is at l.21384-21389.
  - (b) "A law, he said, cannot be kept without a lawgiver" stops before its point: "una porro ex legibus nostris est principatus noster ecclesiasticus" (l.21516-21518). Without it, the listener cannot tell what the lawgiver is.
  - (c) "the church could depose a bishop who sinned" narrows the caliph's "peccatorem" (l.21702-21706), which answers the patriarch's rule for bishops, priests and laymen alike (l.21695-21699).
  - Fix: replace sentences 2 to 5 with "Lazarus, a deposed bishop of Baghdad, cited the caliph's decree that any ten men of a faith could choose a leader. The Christians' fathers, Dionysius answered, had handed many cities to the Muslims on promises that their laws would stand. A law, he said, cannot be kept without a lawgiver, and the church's leadership was one of those laws. Al-Ma'mun ruled that the church could depose a sinner."

- **B-M2 MINOR (brief P4, l.7; items 1 and 4).**
  - (a) "the emir's brother" comes before any emir has been named.
  - (b) "The emir ... asked why he had not written instead" softens "reprehendit eum ... de navigatione" (BH1 l.21162-21166). The emir rebuked him, and Bar Hebraeus gives the reason: he was "Emiro gratissimus".
  - (c) The Edessa grievance that sent him to Egypt is left with no outcome. The emir "propria manu scripsit fratri suo eum reprehendens jubensque ne laederet aut vexaret patriarcham neve ecclesias impeteret" (l.21169-21172).
  - (d) "sailed for Egypt" gives no reason. Bar Hebraeus does: the emir had gone down to Egypt (l.21050-21053), and Dionysius went to him (l.21160-21161).
  - Fix, the whole paragraph: "The emir Abdallah, son of Tahir, had gone down to Egypt, and his brother tore down new church buildings in Edessa. Dionysius sailed after the emir, and a storm drove him into Tanis. The emir scolded him for coming instead of writing, then wrote to his brother forbidding attacks on the churches. Dionysius won the people of Tanis a tax graded by wealth, in place of five dinars a head." To stay inside the cap, this drops "some thirty thousand Christians", which the card can carry.

- **B-M3 MINOR (brief P6, l.11; item 4; the preface told without its frame).** "There he writes of old age and long journeys ... He writes of waiting and bowing at princes' doors, and of the contempt it brought." In the preface these are not memoir. They are his protest that John "n'as pas considéré la vieillesse ... ni que je passe de village en village ... des stations et des prostrations à la porte des princes" (MICHAEL2 l.27493-27508), before he agrees to write (l.27510-27515). The two "He writes of" sentences also run as a list with no point. Fix: "There Dionysius protests that John forgot his old age and the contempt of waiting at princes' doors." In the next sentence, "anyone of Dionysius's church" becomes "anyone of his church".

- **Word budget for B-M1 to B-M3.** The brief is at the cap, so two sourced cuts are needed. In P5, "The general Afshin refused terms, burned their villages, killed many, and shipped the rest away as captives." In P3, "The bishops made him deacon on a Friday, priest on Saturday, and patriarch on Sunday." With all of these, the scratch copy is 404 words, FK 7.6, Flesch 67.6, and no sentence is over 22 words.

- **B-M4 MINOR (card `uncertain` 4; item 1).** "Bar Hebraeus sets the first voyage in the year the emir Abdallah ... went down to Egypt." He gives his own year: "Anno autem Graecorum 1136 (Chr. 823), quum Emirus Abdallah descendisset in Aegyptum" (BH1 l.21050-21053). Fix, for the second and third sentences: "Bar Hebraeus sets the first voyage in the year 1136 of the Greeks, when the emir Abdallah, son of Tahir, went down to Egypt. The editors give that year as 823."

- **B-M5 MINOR (card `uncertain` 2; item 1; whose chronicle).** "the only chapter of the chronicle whose text we have" can be read as Michael's chronicle. Chabot writes "le seul chapitre de sa Chronique", meaning Dionysius's (MICHAEL2 l.27771-27773). Fix: "...is the only chapter of Dionysius's chronicle whose text we have."

- **B-M6 MINOR (records `absent_details` 2 and the census notes 1; card `uncertain` 5 "says only"; held witnesses to the Egyptian events left out).**
  - The Bashmuric revolt has two more held witnesses. Eutychius of Alexandria's Annals (PG111 l.87139-87156) say the "Al Bimaidae" of Lower Egypt refused tax and tribute. Al-Ma'mun sent al-Mu'tasim, who routed them and took their women and children captive to Baghdad. Renaudot reports Makrizi, who has Afshin lead the army from the year 216 of the Hijra until al-Ma'mun came, and al-Ma'mun condemn many and sell women and children (RENAUDOT l.17703-17711). He also quotes the Eutychius passage (l.17714-17726).
  - The editors' "totidem verbis" (BH1 l.21826-21828) overstates: Eutychius names al-Mu'tasim, not Afshin, and leaves out the patriarchs.
  - The first voyage has an independent held witness. Renaudot, from the Coptic History of the Patriarchs, writes "Dionysius Patriarcha Jacobitarum Antiochenus ... advenit, & dies multos apud illum [Jacobum] ... transegit" (RENAUDOT l.17621-17624).
  - Fix: add these to the records. Card `uncertain` 5 becomes "The rebels of Lower Egypt. Bar Hebraeus calls them Byamites and has Afshin burn their villages. Eutychius of Alexandria has al-Mu'tasim lead the army, and says the rebels refused their tax. Neither he nor Makrizi, as Renaudot reports him, names the patriarchs. Bar Hebraeus's editors give other names for the rebels from Renaudot and Le Quien." The brief can stand: Afshin's refusal is Bar Hebraeus's, and the brief tells the scene as his.

- **B-M7 MINOR (records `absent_details` 1; an absence narrowed only by "used here").** "No held source used here gives ... where Tel Mahre was." Charon lists "Tell-Mahrê (Macédonopolis ?)" among the eleven sees of the province of Edessa (CHARON l.33957). Fix: "Charon lists a see Tell-Mahrê, with his query 'Macédonopolis ?', in the province of Edessa (CHARON l.33957); no held line ties it to Dionysius's name or birth." The card's "No source used here gives his birth" is true on my search and stands.

- **Not a finding, for the drafter.** Bar Hebraeus's Nomocanon, in Mai's Latin, gives a rule on kinship through the sponsors at a marriage "uti definiunt Dionysius patriarcha Telmaharensis, et religiosus Iacobus Edessae" (MAI10 l.45740-45750). It is a held trace of Dionysius as a lawgiver, if the card wants one.

**Verdict, Dionysius of Tel Mahre: NOT CLEAR. 1 blocking (records and card), 7 minor (3 in the brief).**

---

### Jacob of Edessa (major; 405 words, about 2:30; FK 7.2, Flesch 69.5)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (B-M12, B-M14, B-M15) |
| 2 | Quotes verbatim | PASS (no quotation marks anywhere; the gloss and the canon-burning cry are paraphrases with Jacob, Michael and Bar Hebraeus named) |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (B-M10, B-M11) |
| 5 | Named witnesses | FAIL (B-M13) |
| 6 | Partisan witness marked | PASS (brief P2) |
| 7 | Contested claims both sides | PASS (death year: Bar Hebraeus, Michael's manuscript and Assemani in place; faith: on the card. The brief's "Jacob's own Syriac Orthodox church" is not the disputed point. Assemani himself has him at the synod "à Juliano Jacobitarum Patriarcha", ASSEMANI1 l.97541-97545, and argues only for his doctrine.) |
| 8 | Common names | PASS |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | FAIL (B-M8, B-M9) |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | FAIL (B-B2: an own-words source is held and not listed) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Records | FAIL (B-B2, B-B3, B-M13) |

**Sentences checked and found faithful.**
- P1: MICHAEL2 l.36392-36399, "il discuta avec le patriarche et les évêques au sujet de l'observation des canons ... tous lui conseillaient de s'accommoder au temps ... le fit brûler devant la porte du monastère du patriarche ... Je brûle dans le feu, comme superflus et inutiles, les canons que vous foulez aux pieds". BH1 l.17320-17332 and l.17407-17411 agree word for word in sense. "Julianus cognomine Romanus", l.17535-17536.
- P2: Michael 1166-1199, MICHAEL2 l.39-41; Bar Hebraeus 1226, BH1 l.238-239.
- P3: 'Ayndaba and the country of Antioch, MICHAEL2 l.36356-36359. "Monasterio Aphtonii seu Kenserinensi", BH1 l.17305-17309. Alexandria and Edessa, MICHAEL2 l.36366-36372. Athanasius, l.36346-36353. Four years and "ceux auxquels il avait interdit le ministère à cause de leurs dérèglements", l.36374-36376; Bar Hebraeus has "improbis clericis", l.17314-17316.
- P4: Kaisum and the two treatises, MICHAEL2 l.36399-36402. Eusebona, "renouveler (l'étude de) la langue grecque, qui avait disparu", eleven years, the brothers "qui jalousaient et détestaient les Grecs", Tell 'Ada, nine years, l.36404-36414.
- P5: the preface, MICHAEL1 l.56573-56576. Michael's tables, MICHAEL2 l.40776-40778. Assemani on Elias, ASSEMANI1 l.98794-98800.
- P6: PO16 l.45708-45748, "en l'an 700/1 de notre ère"; "reviser minutieusement la version du vie siècle"; "corriger, d'après le grec"; "Jacques reproduit ... littéralement la version de Paul chaque fois qu'il n'y a pas lieu de la remanier".
- P7: MICHAEL2 l.36415-36423 and l.36741-36753. Bar Hebraeus's 1019 and the fifth of Haziran, BH1 l.17519-17522. The 1015 and Chabot's note, MICHAEL2 l.36422, 36433-36434. Assemani's 1021 and 710, ASSEMANI1 l.97591-97596.
- P8: the gloss, PO16 l.49676-49765. "Si donc quelqu'un lit ces mots avec amour du travail, il comprendra peut-être la diversité des mots du maître (Sévère) en cet endroit" is told as a paraphrase and not as a quotation.

**Card.** Checked and faithful:
- `otherNames`: "Jacques le Rhéteur" (MICHAEL2 l.36346); "cognomento Commentator, seu Interpres Librorum" (ASSEMANI1 l.97527-97531).
- `knownFor`, `place` and `role`.
- `keyWorks` 1: the three-year correction, MICHAEL2 l.40776-40779.
- `keyWorks` 2: the British Museum manuscripts, BH1 l.17435-17437.
- `legacy.traces` 1 to 4: ELIAS l.4805, 50077-50081, 52965; ASSEMANI1 l.98794-98818, 97855-97864.
- `remembered` 1 to 3: MICHAEL2 l.36422; MICHAEL1 l.293-297; ASSEMANI1 l.97955-97960.
- `uncertain` 2: MICHAEL2 l.37212-37224.
- `uncertain` 3.
- `uncertain` 4: ASSEMANI1 l.97955-97990 and BH1 l.17441-17452. "Retractavit, cum aliqua tamen haesitatione" is rightly told as with some hesitation.
- `uncertain` 6, which is true for "first grammar".

#### Findings

- **B-B2 BLOCKING (notes, "Open-Gaps candidates", Wanted; card `sources.ownWords`, `keyWorks` 1, `dates`, `uncertain` 1 and 2; a false absence of his own Chronicle).** The notes list "Brooks's edition of the Chronicle fragments (ZDMG 53, 1899)" as wanted, and the card's own words for the Chronicle are only the preface as Michael keeps it.
  - The Chronicle itself is held. CHRONMIN l.14453-14454 reads "CHRONICON IACOBI EDESSENI. INTERPRETATUS EST E.-W. BROOKS". Brooks's introduction is at l.14455-14519. The preface in Latin begins at l.14528, "Eusebius quidem Pamphili, Caesareae Stratonis ...", and the canon follows. His "Testimonia Iacobi Edesseni apud Eliam Nisibenum recitata" are at l.19369 and after. Brooks says the text is printed whole for the first time ("textus integer totius operis nunc primum vulgatur", l.14505-14506).
  - Brooks's introduction bears on the card. The manuscript calls the author "Iacobus Philoponus", whom Brooks, with Wright, takes to be Jacob of Edessa (l.14459-14462). The surviving fragments reach only 942 of the Seleucids, 631 (l.14472-14474). The canon ran to 1021, Michael says, and Michael supposes a disciple added the last two years (l.14474-14477). If Elias's 692 is right, eighteen years belong to a continuator (l.14477-14480).
  - Fix, card:
    - add to `sources.ownWords`: `{"title": "Chronicle: preface and fragments of the canon, in Chronica minora (tr. E. W. Brooks)", "author": "Jacob of Edessa", "language": "Latin translation", "file": "cic/texts/chronica-minora-pars-prior-versio-lat_guidi1903.txt"}`;
    - `keyWorks` 1, add: "Its preface and fragments of the canon survive in a British Museum manuscript, which E. W. Brooks translated into Latin. The fragments reach only the year 631. The manuscript names the author Jacob Philoponus, whom Brooks takes to be Jacob of Edessa.";
    - `uncertain` 2, add: "E. W. Brooks gives this note to Michael. He adds that if Elias's year 692 is right, someone carried the work on for eighteen years."
  - Fix, notes and records: strike the Wanted entry and add the Chronicle as held, with its own claims.
  - Library note, to flag only, not to touch: the header of the CHRONMIN file reads "pars prior ... Guidi", while the file also carries Brooks's texts (CSCO Syr. III, 4, l.29550-29560). That is for the Library thread.

- **B-B3 BLOCKING (records `absent_details` 2, "his letters and canons ... Not held as texts"; a false absence).** Bar Hebraeus's Nomocanon, in Angelo Mai's Latin (MAI10, from "NOMOCANON" at l.38229), quotes canons headed "Iacobi Edessae" more than twenty times. Examples: l.38646-38650, on the priests selling leftover offering flour; l.39368, 40175, 41009, 42331, 44700; and l.45745-45750, with Dionysius of Tel Mahre. Mai's preface names the Nomocanon as Bar Hebraeus's (l.838-844). This bears straight on the brief's opening scene, the man who burned the canons and wrote against "ceux qui transgressent ... les canons". Fix, records: "His canons are held in part. Bar Hebraeus's Nomocanon, in Mai's Latin, quotes more than twenty under his name (MAI10 l.38646 and after). His letters and the Responses to Addai are not held as texts." Fix, card, a new `legacy.traces` item: "Bar Hebraeus's Nomocanon, his book of church law, quotes more than twenty of Jacob's canons." (16 words.)

- **B-M8 MINOR (brief P1 and P3, l.1 and l.5; item 10; the scene is placed out of time).** The brief opens with "Jacob, bishop of Edessa" burning the canons, and two paragraphs later "he gave up the see". In Michael and Bar Hebraeus the burning comes as he leaves: "il renonça à la charge pastorale ... Avant de partir, il discuta ..." (MICHAEL2 l.36392-36395; BH1 l.17317-17320, "munus pastorale reliquit. Sed et cum patriarcha ..."). Fix, P1 sentence 1: "Leaving his see at Edessa, Jacob argued with the patriarch Julian the Roman and the bishops over keeping the church's canons." P1 sentence 3, to save words with the same sense ("le fit brûler devant la porte"): "So he burned the book of canons at the door of the patriarch's monastery."

- **B-M9 MINOR (brief P3, l.5; item 10; no time in the who-line).** The listener first hears a year in P6 ("In about 701"). Fix, P3 sentence 1: "Jacob, who lived around the year 700, came from 'Ayndaba, a village in the country of Antioch." Every held dating agrees with "around 700": Kugener and Triffaux's "un interprète du début du viiie siècle" (PO16 l.44785); the revision of 700/1 (l.45743-45745); bishop under Athanasius, who took the see in 995 of the Greeks (MICHAEL2 l.36339-36341); death 708 to 710 (BH1 l.17519-17522; ASSEMANI1 l.97591-97596).

- **B-M10 MINOR (brief P4, l.7; item 4; a floating phrase).** "wrote two tracts of reproach" says nothing about whom they reproach. Michael names them: "un contre les pasteurs de l'Église; l'autre contre ceux qui transgressent la loi et les canons ecclésiastiques" (MICHAEL2 l.36400-36402). This is the thread of the opening scene. Fix: "He withdrew to a monastery at Kaisum. There he wrote two tracts of reproach, against the church's shepherds and against those who break its canons."

- **B-M11 MINOR (brief P7, l.13; item 4; the books' journey is unclear).** "The monks there hurried to bring back his books before they crossed the Euphrates" makes no sense without Michael's "fit charger ses livres et les expédia devant lui" (MICHAEL2 l.36420-36421). Fix: "He held the see four months, then went to fetch his books and pupils. At Tell 'Ada he sent the books ahead, but died there. The monks there hurried to bring the books back before they crossed the Euphrates."

- **Word budget for B-M8 to B-M11 and B-M12.** Four sourced trims keep the brief at the cap:
  - P2: "Michael the Syrian, a twelfth-century patriarch, tells this, and so does Bar Hebraeus a century later. Both belonged to Jacob's own Syriac Orthodox church, which refused the Council of Chalcedon."
  - P4: "At the monastery of Tell 'Ada he spent nine years correcting the Old Testament."
  - P5: "In his chronicle's preface, which Michael keeps, ..." and drop "Michael drew his year tables from it." (`keyWorks` 1 keeps it).
  - P7: "When the next bishop died, Edessa called Jacob back."
  - P3: "After four years, troubled by clergy he had barred for their disorders, he gave up the see."
  - P6: "who edited one"; P8: "print his note on how".
  - With all of these, the scratch copy is 405 words, FK 7.1, Flesch 68.9, and no sentence is over 21 words.

- **B-M12 MINOR (brief P6, l.11; card `keyWorks` 3; `sources.ownWords` 2 and `about` 6; item 1; a first name not held).** "Edgar Triffaux". The only held form is "Edg." (PO16 l.1, 76, 44590, 44599). Kugener calls him "mon élève, M. Edg. Triffaux" (l.44598-44599). Fix: in the brief, "M.-A. Kugener and his student Triffaux, who edited one, say ..."; in the card prose, "M.-A. Kugener and his student Triffaux"; in the source lines, "M.-A. Kugener and Edg. Triffaux", as printed.

- **B-M13 MINOR (card `uncertain` 5; records `contested_claims` 4, side 2; items 5 and 1; an unnamed passage made into a witness).** "A passage that Kugener and Triffaux quote says twelve, and has him study Greek at Kenneshre." The passage is Kugener's own, written with Fr. Cumont, in their Recherches sur le Manichéisme, p. 88. Kugener and Triffaux give it in their note 1 (PO16 l.45728-45734, note at l.45768; the book is dated Brussels, 1912, at l.44831). It is a modern summary, not an older witness, so the records' "Contested" over eleven or twelve years overstates it. Fix, card: "His teaching years. Michael and Bar Hebraeus say he taught at Eusebona for eleven years. M.-A. Kugener and Fr. Cumont, in a book of 1912, say twelve, and place his Greek studies at Kenneshre." In the records, name Kugener and Cumont, and cite PO16 l.45768 and l.44831.

- **B-M14 MINOR (card `dates`; item 1; a witness fused to another's number).** "Wrote his chronicle in the year 1003 of Alexander, Elias of Nisibis says, which J.-B. Chabot gives as 692." Chabot does not convert Elias's year. He dates the Chronicle to 692 from the reigns it names, Justinian II and 'Abd al-Malik (MICHAEL1 l.56636-56638). Brooks is the one who sets "1003 Sel. — 692 p. Chr." beside Elias (CHRONMIN l.14477-14478). Fix: "Wrote his chronicle in the year 1003 of Alexander, Elias of Nisibis says, which E. W. Brooks gives as 692; J.-B. Chabot reaches 692 from the reigns it names."

- **B-M15 MINOR (card `uncertain` 1; item 1; a witness's year left out).** "Elias of Nisibis records Jacob's death beside that of the patriarch Julian the Roman, but his line is broken." Elias's entry stands under the year 89 of the Hijra, which "iniit ... anni 1019 Graecorum" (ELIAS l.6495-6503), so he too points to 1019. Fix: "Elias of Nisibis records Jacob's death beside the patriarch Julian's, in the year of the Hijra that began in 1019 of the Greeks, though his line is broken."

- **Not a finding, for the drafter.** Malech (1910) reports Bar Auraia's claim that Jacob "was the first one to use dots and syllables in the Syrian language" (`malech_history-of-the-syrian-nation...1910.txt` l.3549-3551). It is a late and secondary witness on his work on Syriac writing, if `uncertain` 6 wants it. The card's "first grammar ... only through Assemani's report of Elias" stays true.

**Verdict, Jacob of Edessa: NOT CLEAR. 2 blocking (a held Chronicle and held canons marked absent; card sources and records), 8 minor (5 in the brief).**


## R1 review, part C: Timothy I of Baghdad, Photius of Constantinople (era 4 Who batch 2)

Reviewer: independent Opus, first sight of these drafts. I edited no profile, records or notes file. I made no git, web, paid or model calls, and used local scripts only.

### Method

Bar: `Who_Profile_Pattern.md` checklist 1 to 14; `CLAUDE.md`, "Trust and source fidelity" and "Accessible and rigorous"; the Decision-Log entries for era 3 batches 6 to 8 and era 4 batch 1, with their cap rulings; part A of the era 4 batch 1 R1 review for format; the rulings block of `Who_Scan_Era4.md`. Following those rulings, false absences and witness swaps are blocking, and a missing common-name identifier is minor. Punctuation inside quotation marks follows the era 3 batch 8 cap check: a mark the source does not have sits outside the quotation marks.

For each id I read the `.brief.txt`, `.card.json` and `audio/<id>.audio.txt`, the scratch records and the drafter's notes. I opened every cited line in its vendored file and read it in context, folding OCR noise, double spaces and hyphen breaks. Files, with the short names used below:
- Timothy: Mari ibn Sulayman, Gismondi 1899 (MARI); Amr ibn Matta, Gismondi 1896-1897 (AMR); Thomas of Marga, Budge 1893, vol. 2 (TM); Bar Hebraeus, Chronicon Ecclesiasticum vol. 3, Abbeloos-Lamy 1877 (BH); Elias of Nisibis, Brooks-Chabot 1910 (ELIAS); Synodicon Orientale, Chabot 1902 (CHABOT); Assemani 3.1 (1725) and 3.2 (1728); Mingana 1926 (MINGANA); Braun 1900; and, outside the records, Malech 1910 (MALECH) and Wigram 1929.
- Photius: Freese 1920 (FREESE); Mansi vols. 15, 16 and 17-18 (MANSI15, MANSI16, MANSI17); PG 109, Theophanes Continuatus and Symeon (PG109); Liber Pontificalis 2, Duchesne 1892 (LP2); Will 1861 (WILL).

Absence searches across all of `cic/texts/`, OCR-tolerant:
- Timothy: the text of the al-Mahdi disputation ("Mahdi", "Commander of the Faithful", Woodbrooke): not held, so the census difference stands. Every file that names Timothy beside a death year: MALECH gives "780-820" (l.14435-14438) and MINGANA "A.D. 779-823" (l.1685-1686), neither in the records. An Elias line placing the enthronement: there is none.
- Photius: his death year and birth year ("Photi" within 80 characters of 89x, "obiit", "mort", "died"); the 879 Creed decree outside Nilus; Tarasius as a brother by birth; the census apse homily.

Readability comes from `engine.m1.gates.grade_text`, run from the repo root. I applied every suggested brief fix to scratch copies and scored them again: `/tmp/claude-0/-home-user-CIC-Project/46148d77-0e3f-56b5-a386-901106a72590/scratchpad/review/fixC/timothy-i-of-baghdad.brief.txt` and `/tmp/claude-0/-home-user-CIC-Project/46148d77-0e3f-56b5-a386-901106a72590/scratchpad/review/fixC/photius-of-constantinople.brief.txt`.

**Applies to both.** I checked by script that each audio file equals its brief once `[calmly] ` (at the start) and `[warmly] ` (at the start of the last paragraph) are taken out. No tag appears in a brief or card. Every brief fix below has to be carried into the audio. Both cards follow batch 1's field order, with no null or empty fields. Every `sources` file exists and holds the named work. Each card has three `keyWorks`. Both card traditions are census movements that fit the dates. The Church of the East on the Silk Road runs c. 635-845, and Timothy's years are 780 to 819/823. The Church of the East under the Abbasids starts c. 845, so the drafter rightly left it out. The Byzantine Imperial Church (Macedonian Era) runs 843-1054. The drafts carry no list lines, so the list-line half of item 14 was not checked.

---

### Timothy I of Baghdad (major; 402 words, about 2:29; FK 6.8, Flesch 69.0)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (C-B1, C-B2, C-M2, C-M4, C-M6, C-M7) |
| 2 | Quotes verbatim | FAIL (C-M4, punctuation only) |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (C-M3) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS (Joshua bar Nun's hostility is Mari's, on the card; Thomas's "by fraud" is on the card) |
| 7 | Contested claims both sides | FAIL (C-B3). The death year is told with two witnesses and not settled (brief P9; card `dates`, `uncertain` 3 and 4). |
| 8 | Common names | FAIL (C-M1) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS (opens on the election) |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | PASS (`uncertain` 3 repeats the brief's death-year caveat) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Records | FAIL (C-M9) |

**Sentences checked and found faithful.**
- P1. The convocation and the rival candidates are at MARI l.13072-13078 and AMR l.13002-13007. Chabot's "huit mois de violentes contestations" is at CHABOT l.40256-40258. The sacks and the consecration "octo post menses" are at MARI l.13079-13084 and AMR l.13008-13015. The refusal, "sacerdotium nequaquam pecuniis venditur", and the stones are at MARI l.13084-13086, rightly told in reported speech.
- P3. Hazza is at MARI l.13066 ("e genere optimatum Hazzae"), AMR l.13001, CHABOT l.40255 and TM l.17316. Bashosh, Abraham, George and his resignation are at TM l.17166-17229. May 780 rests on CHABOT's index, l.49679 ("7 mai 780"); the note at l.40259 loses the month to OCR, and ELIAS l.3716 gives 7 Iyyar 1091 Gr. Ephrem and the split of about two years are at CHABOT l.40262-40266. The year 790 is at l.39904-39906. The letter ("par orgueil ou par négligence … aller six fois en sa présence") is at l.40540-40546, told in reported speech.
- P5. The phrase "since the time of the Apostles" is at TM l.21500-21504, said of Shubhhal-Isho's mission. His chapter is headed "Metropolitan of Gilan and Dailom" (l.21451-21454), and Yahbalaha, Kardagh and Elijah's countries are "Dailomaye and … Gilaye" (l.21003-21017). Budge's gloss on Gilan is at l.21047, and Thomas read the letter (l.21966-21985). David, Beth Sinaye and "i. e., China" are at l.20155-20158 and 20166. The Khagan is at MARI l.13041-13043. "Writing about 840" follows Budge's title, "A. D. 840" (TM l.94).
- P7. Harun's question, Timothy's answer and the caliph's verdict are at AMR l.12939-12950, told in reported speech.
- P9. Elias's Friday ("die praeparationis") 9 Kanun II 1134 Gr. is at ELIAS l.3720-3722. Bar Hebraeus's AH 204, "inchoato 28 Jun. 819", is at BH l.10257-10260. The conversion is his editors', but it is arithmetic and makes no claim.
- P11. The quotation is verbatim at MINGANA l.1689-1691.

**Card.** I checked these against their lines:
- `knownFor`: the five caliphs are at MARI l.12985-12986.
- `place`: ASSEMANI 3.2 l.42424-42427. "Scjoftie" is OCR for "solitus", which the record flags. Burial is at AMR l.12960, and restoration at MARI l.12988-12989.
- `keyWorks` 1 and 2: CHABOT l.39906-39917 and 40283-40291; BH l.10402-10405; TM l.17405-17410; MINGANA l.1702-1704.
- `legacy.traces` 3 to 5: BH l.9802-9813; MINGANA l.1719-1736; CHABOT l.40289-40291 and 40361-40365.
- `legacy.remembered` 1, 3, 4 and 5: TM l.17205-17215. MARI l.12986-12992, 12955-12957, 12857-12858 and 12882-12884. MARI l.12861-12863 names Joshua as successor.
- `uncertain` 1, 2, 4, 5, 7, 8 and 10. Braun's namesake is at l.11564 and 14885.

**The drafter's census differences, checked.**
1. The al-Mahdi debate is **confirmed**: no held text of the disputation.
2. "780 to 823" is **confirmed**. The death year is contested (Elias and Chabot's note give 823, Bar Hebraeus 819, Amr AH 205, Chabot's index 825, Budge 819-821). Add to the list MALECH's 820 and MINGANA's 779 to 823 (C-M8).
3. Distant provinces is **confirmed** for Gilan, Dailom and Beth Sinaye. It does not stand for Peter of Yaman (C-B2).

#### Findings

- **C-B1 BLOCKING (card `dates`, l.8, and `uncertain` 9, l.52; witness given a claim he does not make).** Both say Elias of Nisibis places the enthronement at Seleucia. Elias gives only the day: "Institutus est Timotheus die dominica 7° iyyar anni 1091 Graecorum" (ELIAS l.3716-3717). He names no place, and he says nothing of eight months. The place comes from Chabot ("intronisé à Séleucie", CHABOT l.40258), Bar Hebraeus ("deduxerunt Seleuciam", BH l.9612) and Amr ("consecraverunt Modainae", AMR l.13017). The eight months come from Chabot (l.40257) and Mari (MARI l.13083-13084). Fix:
  - `dates`, first sentence: "Enthroned on Sunday 7 May 780, by Elias of Nisibis and J.-B. Chabot. Chabot places it at Seleucia, after eight months of dispute."
  - `uncertain` 9: "His name. Chabot and Bar Hebraeus place his enthronement at Seleucia, and Amr ibn Matta at Madaina. Joseph Assemani says the patriarchs then lived at Baghdad, Timothy at the monastery of Kelilisho."

- **C-B2 BLOCKING (card `legacy.traces` 1, l.29; unsupported).** "Thomas of Marga names monks of his own monastery made bishops in Timothy's time. Among them were Elijah, bishop of Mukan, and Peter, bishop of Yaman and San'a." Thomas's list holds the bishops the old man foretold for the community (TM l.20112-20117). It is not tied to Timothy's time. Peter is dated only as bishop "when I was secretary to Mar Abraham" (l.20160-20162), a later catholicos. Elijah is the one man Thomas says Timothy ordained (l.21003-21005). Fix: "Thomas of Marga lists monks of his own monastery who became bishops. One was Elijah, bishop of Mukan, whom Thomas says Timothy ordained."

- **C-B3 BLOCKING (brief P7, l.7; card `keyWorks` 3, l.24, and `uncertain` 6, l.49; an editor's reading told as the source's, and a dispute that rests on it).** Amr never mentions the disputation. He says only that al-Hadi "Saepe admodum eum accersebat … ut cum eo colloqueretur de religione" (AMR l.13027-13029). The link to the al-Mahdi disputation is Joseph Assemani's: "Amrus … Hadium pro Mohdio legit" (ASSEMANI 3.1 l.29817). The brief's "it was the caliph al-Hadi who" sets Amr against 'Abdisho, and the card has Amr "name" the caliph of the disputation. Fix:
  - Brief: "Amr says the caliph al-Hadi often called Timothy in to argue about religion."
  - `keyWorks` 3 `about`: "named in 'Abdisho's list of his works. Amr says the caliph al-Hadi often called Timothy to argue about religion. Joseph Assemani takes Amr to mean the same debate. Its text is not among the sources used here."
  - `uncertain` 6: "The caliph of the disputation. 'Abdisho's list names al-Mahdi. Joseph Assemani reads Amr's report of al-Hadi's debates as naming al-Hadi instead."

- **C-M1 MINOR (brief P1, l.1; card `place`, l.9; item 8).** "Amr" is the first mention in both texts, and the name is common. The Library's form is Amr ibn Matta (Gismondi, "Amrum Matthaei tirhanen-", AMR l.6436). Fix: in the brief, "Mari ibn Sulayman and Amr ibn Matta, tell how…". In `place`, write "Amr ibn Matta says he was buried there".

- **C-M2 MINOR (brief P5, l.5; item 1).** "did not strictly need three bishops". The letter reads "doth not absolutely require [the presence of] three persons" (TM l.21976-21977). Fix: "did not strictly need three persons."

- **C-M3 MINOR (brief P7 and P9, l.7 and l.9; item 4, names with no context).** 'Abdisho of Nisibis and Elias of Nisibis come with no word on who they are. Fix: "'Abdisho, metropolitan of Nisibis, lists a disputation…". Mai heads him "Ebediesu Sobae, id est Nisibis, metropolitae" (MAI l.171). Also: "The chronicler Elias of Nisibis says he died on a Friday in January 823."

- **C-M4 MINOR (brief P11, l.11; items 1 and 2).** "he spoke for churches" leaves out what he said about them. The letter says that in those lands "there is no addition of Crucifixus es pro nobis" to the hymn (MINGANA l.1687-1692). The period inside the closing mark is not in the source, which runs on: "the Turks, and in all the provinces". Fix: "In a letter Alphonse Mingana translates, he said a hymn had no added words "among the Indians, the Chinese, the Tibetans, the Turks"." (23 words.)

- **C-M5 MINOR (card `legacy.traces` 2, l.30; a hedge dropped).** Bar Hebraeus opens with "Fertur" (BH l.9750), "it is said". Fix: "Bar Hebraeus reports it was said that the bishops of the Persians had worn white, eaten meat and married. They had not obeyed the catholicos of Seleucia."

- **C-M6 MINOR (card `legacy.remembered` 1 and 2, l.36-37; item 1).** Item 2's "that monastery" has no antecedent, because item 1 names none. "First shown" adds "first": the source says "it was here pointed out to him" (TM l.21413-21414). Fix:
  - 1: "Thomas of Marga tells of an old monk of his own monastery, Beth 'Abhe, who met the boy Timothy on his way to school. The monk foretold that he would be patriarch for forty-two years." Sources: TM l.17164 ("in this monastery") and l.215.
  - 2: "Thomas says Timothy loved Beth 'Abhe and gave it many gifts, because there it was shown to him that he would be patriarch."

- **C-M7 MINOR (card `uncertain` 3, l.46; item 1).** "Chabot follows him in his notes" is an inference. Chabot's note gives the same day but cites no witness (CHABOT l.40361). Fix: "Elias of Nisibis gives Friday 9 January 823, and so does Chabot's note, though Chabot's index gives 825."

- **C-M8 MINOR (card `uncertain` 3 and 4; the death-year witnesses incomplete).** The records' contested claim has Mari: Timothy died in the year al-Ma'mun entered Baghdad, which Mari places in AH 204 (MARI l.12983-12985). Mari also has Joshua elected "anno 205" (l.12867). The card leaves Mari out. MALECH gives "780-820" (l.14435-14438) and MINGANA "A.D. 779-823" (l.1685-1686). Fix: add to `uncertain` 4: "Mari ibn Sulayman says he died in the year al-Ma'mun entered Baghdad, which Mari puts in the Arab year 204." Add MALECH and MINGANA to the records' death-year sides.

- **C-M9 MINOR (records; OCR forms flagged unevenly).** The records list some OCR forms as if they were the full set and leave others out. Examples:
  - MARI l.12984-12990: unflagged "quadragesiraotertio", "Maraun", "quera" (twice), "dooueritque" and "sedera". The flagged "raverat" is a line-break hyphen ("restaura- verat"), not an OCR error.
  - MARI l.13041-13043: "rcgni" and "epistolac".
  - AMR l.12941-12950: the record's own text keeps the OCR "respoude" for "responde", and leaves "cliristianorum", "le", "ost", "cl", "conforinia", "Dous", "cuin" and "nc([uil excoptio" unflagged. At l.13008-13018 the file reads "iapidibus", not "Iapidibus".
  - BH: "nutn-mis" (l.9598-9599); "catbolicus" (l.10259); "Tmotheua", "Dejudiciis", "ettomos xynodicos", "prater ea" and "distributaa" (l.10402-10405); "vestiraenta", "sse-culares", "praeterca" and "eniin" (l.9800-9803).
  - Fix: flag each form as batch 1 did, and correct "respoude" to "responde" with the OCR form flagged.

**Not a finding, for the coordinator.** The brief tells the election as Mari and Amr tell it, with both named. Bar Hebraeus has real copper coins in the bags in place of stones (BH l.9598-9608), and the card carries his version. All three agree on the promise and the deceit.

After the fixes (C-B3, C-M1 to C-M4 in the brief): 403 words, about 2:29, FK 7.2, Flesch 67.2 (scratch copy scored).

---

### Photius of Constantinople (major; 405 words, about 2:30; FK 7.0, Flesch 66.7)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (C-B4, C-B5, C-M11, C-M14, C-M15) |
| 2 | Quotes verbatim | FAIL (C-M13, punctuation only) |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | FAIL (C-M12) |
| 7 | Contested claims both sides | FAIL (C-M12, C-M16) |
| 8 | Common names | FAIL (C-M10) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS (at the cap) |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | PASS (`uncertain` 1 repeats the brief's P2 caveat) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Records | FAIL (C-B4, C-B5, C-M17) |

**Partisan witnesses, checked one by one (the coordinator's point).**
- The 869 acts are placed and marked in the brief: "comes from the council that condemned him" (P2). The card marks them in `uncertain` 1.
- Nicetas's Life of Ignatius is placed and marked: "an enemy too. Yet he calls…" (P3). The card marks it in `uncertain` 2. His hostility is at MANSI16 l.23514-23528.
- Nicholas I's letters are told as his own side of the quarrel, by name (P4). Photius's encyclical answers them in the same paragraph, so both sides are named.
- The Lives of the Popes and Binius are marked on the card (`uncertain` 2 and 5).
- The chronicle that continues Theophanes is marked as Basil's (`uncertain` 3).
- Symeon is marked for the forged-genealogy story (`uncertain` 3). His communion story (P5) does not damage Photius.
- Nilus of Rhodes is used in the brief and is not marked (C-M12).

**Sentences checked and found faithful.**
- P1. The fifth session, the 20 October date and the third indiction are at MANSI16 l.7912-7922. The summons and "sponte non venio … invitos nos traxistis … nolentem te" are at l.7971, 8132 and 8143, and "in novissimo loco" at l.8148. The silence and the two replies are at l.8221-8236, all in reported speech.
- P2. Anastasius's version is at MANSI16 l.852-858, and his title, "Anastasio s. sedis ap. bibliothecario", at LP2 l.55298.
- P3. The chief secretary is at MANSI16 l.23391-23392 and PG109 l.17962-17965. Nicetas on his learning, books and nights is at MANSI16 l.23396-23411. The six days and Christmas are at l.23526-23537. Freese's 858 is at FREESE l.1284-1286.
- P4. Nicholas's refusal, "nullatenus nos Photium recipere", is at MANSI15 l.18376-18378. "de laicali habitu vos prosilistis" is at MANSI16 l.8241-8245. The encyclical's charges (Saturday fasts, married priests, the Creed and the Filioque) are at WILL l.3456-3483. The year 866 is at WILL l.3486 and MANSI16 l.48676-48678.
- P5. Symeon's communion story is at PG109 l.63686-63690. The restoration "legitimeque ac canonice" is at l.25381-25390. The 879 council with John VIII's legates is at MANSI17 l.37996-38034, and Binius's "pseudo-octavam" at l.38225.
- P6. Gordon is at PG109 l.64642-64646.
- P7. The dedication and the quotation are at FREESE l.1698-1703 and 1739-1741.

**Card.** I checked these against their lines:
- `knownFor`, `dates` (Freese's list, the fifth session, 879, Gordon) and `place` (Skepe, PG109 l.63693).
- `keyWorks` 2 and 3: WILL l.3446-3490.
- `legacy.traces` 2 and 4: MANSI17 l.38904-38915 and 38227-38242.
- `legacy.remembered` 1 to 3. LP2 has "invasorem" at l.49594 and "pervasorem" at l.53412. The book thrown down at Santa Maria Maggiore is at l.53422-53423 and 53540. The palace rooms and the tutor are at PG109 l.25394-25397.
- `uncertain` 1, 2, 3 and 5. Bellarmine is quoted at MANSI17 l.38159-38176, and Duchesne on the last session at LP2 l.55302-55304.

**The drafter's census differences, checked.** 1 (the apse homily) is **confirmed**: there is no held line. 2 (279) is **confirmed** (FREESE l.1713). 3 and 4 are **confirmed** as held.

#### Findings

- **C-B4 BLOCKING (card `uncertain` 6, l.43, and `legacy.traces` 1, l.25; records `contested_claims` 2; a false absence).** "What the council said of the Creed is known here through Nilus of Rhodes." The council's own acts are held, and so is Cornelius Will's print of the decree:
  - Mansi prints the Greek and Latin acts of 879 in the same volume, sessions one to seven (index MANSI17 l.371-394). The sixth session's definition reads: "Si quis … aufit alterum … symbolum … conscribere vel proponere, aut detrahere … sit condemnatus" (l.53399-53406). It goes on: "aut adjicere vel demere in tradito nobis a sancta et oecumenica Nicaea primum magna synodo, anathema sit" (l.53430-53432).
  - A note printed in the Latin column before the sixth session says the last two sessions "confictas esse ab ipsomet Photio, nec vere factas fuisse" (l.52604-52606). It says Photius wrote them in order to set out that nothing may be added to the Creed (l.52615-52628).
  - Cornelius Will quotes the same decree "In ultimo consessu" (WILL l.3975-3979).
  - Fix, `uncertain` 6: "Binius does not deny that John VIII restored Photius after Ignatius's death. The council's own acts, in Mansi, curse anyone who adds to the Creed or takes from it. An unsigned note printed with them says Photius made up those last two sessions himself. Nilus of Rhodes, whom Mansi heads a schismatic, reports the same decree."
  - Fix, `legacy.traces` 1: "In 879, by its own acts and by Nilus of Rhodes, the council that received Photius cursed anyone who added to the Creed or took from it."
  - Records: add the acts and Will as witnesses on that side, and the note as a witness on the other.

- **C-B5 BLOCKING (card `uncertain` 9, l.46; records `absent_details` 1; a false absence in a source the card cites).** "His birth and the year of his death. The held sources used here give neither year." The records list Will among the files read. Will says Leo VI shut him in a monastery, "ubi anno 891 decessit" (WILL l.3988-3992). Will also gives Leo's motive: to raise his brother Stephen (l.3990-3991). The Freese scan's library label "Photius I, ca. a20-ca. 891" (FREESE l.14209) is a catalogue line, not a witness. Fix:
  - `uncertain` 9: "His birth year. None of the sources on this card gives it. Cornelius Will dates his death to 891. Symeon the Logothete gives no year."
  - `dates`: add "Cornelius Will dates his death to 891."
  - Records: replace `absent_details` 1 with a Will claim.

- **C-M10 MINOR (brief P3, l.5; card `legacy.remembered` 1, l.31; item 8).** Ignatius is a common name (Ignatius of Antioch is in the census), and both first mentions are bare. In the brief, "his rival Ignatius" also reads as Nicetas's rival. Fix: in the brief, "who wrote the Life of his rival, the patriarch Ignatius, was an enemy too." In the card, "Nicetas the Paphlagonian, in his Life of Ignatius, patriarch of Constantinople, calls him…" (MANSI16 l.21720-21724).

- **C-M11 MINOR (brief P4, l.7; item 1, overstated).** "who printed the letter in Latin in 1861". Will prints one passage of it, which the card says rightly. Fix: "Cornelius Will, who printed part of the letter in Latin, dates it to 866." The book's year stays in the card's sources.

- **C-M12 MINOR (brief P5, l.9; items 6 and 7).** "Nilus of Rhodes reports that it cursed anyone who added to the Creed." This tells a partisan, later witness unmarked. Mansi heads the extract "Ex Nilo Rhodi metropol. schismatico" (MANSI17 l.38859). Nilus even has Pope John present in person (l.38874). The council's own acts carry the decree (C-B4). Fix: "Its own acts curse anyone who adds to the Creed." Binius's "false synod" then answers it by name.

- **C-M13 MINOR (brief P7, l.13; item 2, punctuation).** The source has a semicolon after "record it" (FREESE l.1741), not a comma. Fix: `…to remember and record it", he wrote.`

- **C-M14 MINOR (brief P5, l.9; card `uncertain` 4, l.41; item 7, a contested cause told from one side).** "Symeon the Logothete says Photius called the next emperor, Basil, a robber and a murderer when he came to communion. Basil put him out." Placed side by side, the two sentences tell Symeon's cause as fact. The records mark the cause as contested. The Life of Hadrian II gives Rome's ruling: "secundum Romanae aecclesiae constitutum, pervasorem Photium pepulit" (LP2 l.53410-53412). "Next" has no antecedent, because Michael is not named. Fix:
  - Brief: "Symeon the Logothete says Photius called the new emperor, Basil, a robber and a murderer at communion, and that Basil then put him out." (24 words.)
  - `uncertain` 4: "Why Basil put him out. Symeon says Photius called Basil a robber and a murderer, unworthy of communion, and that Basil then sought Rome's ruling. The Life of Pope Hadrian II says Basil drove him out by the Roman church's ruling. Cornelius Will gives Basil's taking of the throne as the turn." Symeon's "Romam misit, tomoque impetrato" is at PG109 l.63690.

- **C-M15 MINOR (card `keyWorks` 1, l.12, and `uncertain` 7, l.44; a citation read as a view).** Freese's note reads "To the caliph of Bagdad ; according to others, to Persia, or one of the Eastern emirs (Bury)" (FREESE l.1725-1726). "(Bury)" cites the note as a whole. It does not make the caliph Bury's view against the others. Fix:
  - `keyWorks` 1, last sentence: "J. H. Freese's note, citing J. B. Bury, takes this to mean the caliph of Baghdad."
  - `uncertain` 7: "His embassy "to Assyria." J. H. Freese's note, citing J. B. Bury, takes it to mean the caliph of Baghdad. It adds that others take it as Persia or one of the eastern emirs."
  - Freese names "Professor J. B. Bury" at l.1732.

- **C-M16 MINOR (card `legacy.traces` 3, l.27, and `uncertain`; held sides left out).**
  - (a) Will says the Mystagogy was much excerpted by the defenders of the schism "et ab unionis sociis ad suas sententias tuendas in usum conversus est" (WILL l.3488-3489). The card gives only the first half. Fix: "Cornelius Will says later defenders of the split between the churches often drew on his Mystagogy, and so did those who worked for union."
  - (b) Will says Photius deceived John VIII about the decrees of 879. He says the pope then "palam anathemate Photium percussit", and that Marinus, Hadrian III and Stephen V repeated it (WILL l.3980-3987). Binius notes the same popes' condemnation (MANSI17 l.38244-38246). The card does not carry this side of the 879 dispute. Fix, a new `uncertain` item after 6: "Cornelius Will says Photius misled John VIII about what the council decreed, and that the pope then cursed him publicly. He says Popes Marinus, Hadrian III and Stephen V repeated it."
  - (c) `legacy.remembered` 4, l.34: "In the same Life" points back past item 3, which is the chronicle. Fix: "In Hadrian II's Life, Basil's spatharius says…".

- **C-M17 MINOR (records; OCR forms flagged unevenly, as C-M9).** Examples:
  - PG109 l.63686-63689: "mySleria", "egct", "ae" and "indignem" are unflagged.
  - PG109 l.25396: "institulorem".
  - LP2 l.53544-53545: "MichaeUs" and "noclu".
  - MANSI17 l.52604 onward: the note in C-B4 has OCR margins ("Pofita de in- duftriaa Gree evle qucpiam adnoratioef#"), so its owner should be left unnamed.
  - Fix: flag each form as batch 1 did.

After the fixes (C-M10 to C-M14 in the brief): 404 words, about 2:30, FK 7.1, Flesch 67.2 (scratch copy scored).

---

### Verdicts

- **Timothy I of Baghdad:** NOT CLEAR. 3 blocking (C-B1 Elias given Seleucia, C-B2 Peter put in Timothy's time, C-B3 Assemani's al-Hadi reading told as Amr's) and 9 minor (C-M1 to C-M9). The death year is rightly told with its witnesses and not settled.
- **Photius of Constantinople:** NOT CLEAR. 2 blocking (C-B4 the 879 acts and Will's decree held, C-B5 Will's 891 held) and 8 minor (C-M10 to C-M17). Every partisan witness the coordinator named is placed and marked, apart from Nilus of Rhodes (C-M12).


## R1 review, part D: Benjamin I of Alexandria, Gregory of Narek (era 4 Who batch 2)

Reviewer: independent Opus, first sight of these drafts. I edited no profile, records or notes file. I made no git writes and no web, paid or model calls. I used local scripts only.

### Method

Bar: `Who_Profile_Pattern.md` checklist 1 to 14; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; the Decision-Log entries for era 3 batches 6 to 8 and era 4 batch 1, with their cap rulings; part A of the era 4 batch 1 R1 review for format; the rulings block of the era 4 scan. As in those rulings, a missing common-name identifier is minor and a false absence is blocking wherever it sits.

For each id I read the `.brief.txt`, the `.card.json`, `audio/<id>.audio.txt`, the scratch records and the drafter's notes. I opened every cited line in its vendored file and read it in context, folding OCR noise, double spaces and hyphen breaks.

Files, Benjamin: Evetts's History of the Patriarchs, PO 1 (`severus-al-muqaffa_history-patriarchs-coptic-church-v1_evetts1904.txt`, "HIST"); its PO 5 continuation (`chronicle-of-seert_..._scher-dib1910.txt`, "PO5"; the header confirms it holds Evetts's Agathon to Michael I); John of Nikiu (Charles 1916, "NIKIU"); Michael the Syrian (Chabot, tome 2, "MICHAEL"); Renaudot 1713 ("RENAUDOT"); Basset's Arabic Synaxarium, PO 11 ("BASSET"); Budge's Ethiopic Synaxarium v2 ("BUDGE"); Abu Salih (Evetts 1895, "ABUSALIH").

Files, Gregory: Chamich in Avdall's English ("CHAMICH"); Issaverdens's Ecclesiastical History ("ISSAV") and Armenian Ritual ("ISSRIT"); Serpos t2 and t3; Ormanian 1912; Conybeare's Rituale Armenorum; Macler's and Gelzer-Burckhardt's Stepanos of Taron ("MACLER", "GELZER"); Boré 1837; Alishan 1888; Nurikhan 1915; and, found in the absence search, Parisot's Aphrahat, Patrologia Syriaca I.1, 1894 ("PARISOT").

Absence searches across all of `cic/texts/`:
- Benjamin: "Benjamin" with patriarch, archbishop, Alexandria or Abba, every hit read. This found the Assemani homily (D-B1) and the Ludolf note below.
- Gregory: an OCR-tolerant pattern for Narek, Nareg, Narekatsi, Naregatzi, Narekensis, Narekese and Nareguensis, every hit read. This found Parisot (D-B2), a second Chamich passage, an Issaverdens footnote and the Serpos t3 lines on Sergius.
- Also checked: "Lament" and "elegie" in every Gregory file; Issaverdens as a Mekhitarist; Ormanian's index for every Gregory mention; who signs the Abu Salih notes ("(A. J. B.)" marks Butler's notes; unmarked notes are the editor Evetts's, l.129-134).

Mechanical checks:
- Readability is `engine.m1.gates.grade_text`, run from the repo root.
- Each audio file equals its brief once `[calmly] ` (at the start) and `[warmly] ` (before the last paragraph) are taken out. Each file carries the two tags only. Every brief fix below must be carried into the audio.
- Both cards follow batch 1's field order and have no null or empty field. Benjamin has no `otherNames` and no `ownWords`, which the notes explain.
- Every `sources` file exists and holds the named work.
- The card traditions are census names that fit the dates. Coptic Christianity under Early Islam runs 642 to 1013 and The Church of Alexandria and Miaphysite Egypt 328 to 642, so Benjamin's 622 to 661 straddles them. Bagratid Armenian Christianity runs 884 to 1045, against Gregory's death in 1003.
- The drafts carry no list lines, so the list-line half of item 14 was not checked.

I applied every suggested brief fix to scratch copies and scored them again:
- `/tmp/claude-0/-home-user-CIC-Project/46148d77-0e3f-56b5-a386-901106a72590/scratchpad/review/fixD/benjamin-i-of-alexandria.brief.txt`
- `/tmp/claude-0/-home-user-CIC-Project/46148d77-0e3f-56b5-a386-901106a72590/scratchpad/review/fixD/gregory-of-narek.brief.txt`

---

### Benjamin I of Alexandria (major; 405 words, 2:30; FK 8.15, Flesch 60.7)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (D-M1, D-M5, D-M6) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (D-M2, D-M3) |
| 5 | Named witnesses | FAIL (D-M7) |
| 6 | Partisan witness marked | PASS (Renaudot "calls their line heretical"; the History is "Benjamin's own church") |
| 7 | Contested claims both sides | PASS in the brief (the return: the History and John of Nikiu against Michael; the Macarius account: Agathon against Renaudot). Card `knownFor`: D-M5 |
| 8 | Common names | FAIL on the card (D-M8); PASS in the brief ("Cyrus, bishop of Phasis", "John, the Coptic bishop of Nikiu") |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS (at the cap) |
| 11 | Readability | PASS (Flesch 60.7, just over) |
| 12 | Card order, fields, caveat repeated | PASS (`uncertain` 1 repeats "a later history of his own church") |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Records | FAIL (D-B1, D-M6) |

**Sentences checked and found faithful.**
- P1: Sanutius, "the believing duke", tells 'Amr of Benjamin, "a fugitive from the Romans". 'Amr writes "to the provinces of Egypt" that Benjamin may "come forth secure and tranquil, and administer the affairs of his Church" (HIST l.44459-44588). "I have never seen a man of God like this man" is at l.44683-44685.
- P2: the heading "BENJAMIN I, THE THIRTY- EIGHTH PATRIARCH. A. D. 622-661" is at l.42834. Barshut, the "very rich" parents and Theonas are at l.42836-42847. Andronicus ordains him and names him successor at l.43225-43230.
- P3: Cyrus as "prefect and patriarch" is at l.43240-43241, and Evetts's note making the Mukaukas "Cyrus, bishop of Phasis" is at l.43588-43591; as a first-mention identifier from a vendored note this is in order. The affliction "in order that they might enter into the Chalcedonian faith" is at l.43559-43562. The angel, the bishops told to hide, Mareotis by night, Wadi Habib and Upper Egypt are at l.43420-43447. Mennas is at l.43572-43582 and l.43750-43752 ("Say that the council of Chalcedon is good ... But Mennas would not do so").
- P4: Charles's "probably born about the time of the Mohammedan invasion" is at NIKIU l.175-176. "The thirteenth year after his flight" and "every one said" on Heraclius's "persecution of the Orthodox through the patriarch Cyrus" are at l.12005-12012.
- P5: "nous avons trouvé dans des histoires ... promit de leur livrer Alexandrie, si seulement ils voulaient chasser Cyrus et lui rendre les églises" is at MICHAEL l.33096-33125. "Patriarche jacobite d'Antioche (1166-1199)" is on Chabot's title page.
- P6: Agathon's account and the canons are at HIST l.46143-46150 and l.47715-47910. The quotation is verbatim at l.48051-48052. Renaudot's "haereticum, Jacobitarum" is at RENAUDOT l.10992-10993, and his "a Coptitis recentioribus inventa ... fabula" at l.11541-11548.
- P7: "patriarch thirty-nine years" is at HIST l.45954-45955. BUDGE l.8455-8456 and BASSET's text (l.40875-40876) say the same. Agathon's words are verbatim at l.45959-45964.

**Card, checked against its lines.**
- `dates`, `place` and `role`. The Agathon heading 661 to 677 is at PO5 l.336.
- `keyWorks`: seven canons, l.47715-47910. The Ethiopic "wrote a Canon and placed it in the church" is at BUDGE l.8253-8254. Renaudot's "comminationes non videntur aetati Benjamini convenire" is at l.11541-11542.
- `traces` 1, 2, 4 and 5: HIST l.45701-45712; PO5 l.343-347; MICHAEL l.33128-33132; PO5 l.2536, 3036-3038.
- `remembered` 1 to 3: BASSET l.40494-40497 and l.40726; BUDGE l.8190-8197 and l.8485-8486, the salutation verbatim; RENAUDOT l.11577-11580. Renaudot's "13 Januarii" is as printed, and it fits a Gregorian date for 3 January Julian.
- `uncertain` 1 to 4, 6, 7 and 9. Renaudot's "sequester pacis fuisse dicitur" is at l.11427-11433.

**Census.** The drafter's three census differences hold. The "641-42" year is not in the lines read. Michael's account is missing from the census, which tells the return one way.

#### Findings

- **D-B1 BLOCKING (records `absent_details` 1; a false absence).**
  - The records say "No letter or treatise of his was found in the held files searched ... and a grep for 'Benjamin' across cic/texts."
  - Assemani's catalogue of a manuscript copied in the year of the Martyrs 781 (1065) lists "Benjamini Patriarchae Alexandrini Homilia de Nuptiis Canae Galilaeae" (`assemani_bibliotheca-orientalis-tomus1-de-scriptoribus-syris-orthodoxis-lat_1719.txt` l.124080-124089; OCR "Patriarche", "Canz Galilez"). The text itself is not held, but a held witness names a homily of his.
  - Fix: change the detail to "The text of any writing of Benjamin's beyond the canons and words in Agathon's account". Change the note to "No text is held. Assemani's Bibliotheca Orientalis lists a homily of his on the wedding at Cana in a manuscript of 1065 (ASSEMANI l.124080-124089)."
  - Optional, for the drafter: a card `keyWorks` item, "Homily on the wedding at Cana", about "known here only from Joseph Assemani's catalogue entry for a manuscript of 1065".

- **D-M1 MINOR (brief P6, l.11; item 1; softened).** "won back by gentleness many whom Heraclius had led astray". The History says "most of the people whom Heraclius ... had led astray" (HIST l.44831-44833). Fix: "Back in his see, the History says, Benjamin won back by gentleness most of those Heraclius had led astray."

- **D-M2 MINOR (brief P6, l.11; item 4; a quotation with no context, and an undefined term).** The listener hears "these anathemas" and has not been told that the rules carry curses. In the History canon V ends "let him be anathema" (HIST l.47896-47898), and the others threaten casting out or degrading. Fix: replace "His spiritual son Agathon tells how he consecrated a church of Saint Macarius in Wadi Habib and wrote rules for its sanctuary." with "His spiritual son Agathon tells how he consecrated a church of Saint Macarius in Wadi Habib. Some of Benjamin's rules for its sanctuary end in curses." The quotation sentence that follows stays as it is.

- **D-M3 MINOR (brief P1 and P2, l.1 and l.3; item 4).**
  - (a) "a fugitive from the Romans" will be heard as Rome; the History's "Romans" are the emperor's government. Fix: "a fugitive from the emperor's men."
  - (b) P2 runs four short sentences in a row. Fix: "He came from a rich family at Barshut and became a monk under an old man named Theonas."
  - To keep the brief within 405 words after D-M2, two further changes are needed. "B. Evetts, who translated the History, heads his life 622 to 661." becomes "B. Evetts, its translator, heads his life 622 to 661." "R. H. Charles, who translated John, the Coptic bishop of Nikiu, thinks John was born about the time of the conquest." becomes "John, the Coptic bishop of Nikiu, was born about the time of the conquest, thinks his translator, R. H. Charles." Both keep the witness named.

- **D-M4 MINOR (brief P3, l.5; card `uncertain` 8, l.37; Mennas built up inside Benjamin's profile, and a forward reference).**
  - Mennas is a separate STORY row (era 4 scan l.79). The card item on where he drowned (the sea, seven bowshots, the river) is Mennas's story, not an uncertainty about Benjamin.
  - Its last sentence, "Mennas's own story is told apart from this profile", points to a page that does not exist yet, and it narrates the profile itself.
  - Fix: delete `uncertain` 8, and keep the drowning variants in the records for the Mennas story. In the brief, cut the torture detail, which the Mennas story will carry: "Heraclius had Benjamin's brother Mennas tortured and drowned for refusing to call Chalcedon good." The source is HIST l.43572-43582 and l.43750-43752; the change saves five words.

- **D-M5 MINOR (card `knownFor`, l.3; items 1 and 7).** "He came back after the Arab conquest, under a safe-conduct from 'Amr" tells the History's account as settled, though `uncertain` 1 makes "How he came back" an open point. Fix: "Patriarch of the Coptic church of Alexandria who hid in Upper Egypt from the Chalcedonian patriarch Cyrus. He came back after the Arab conquest. The History says he came under a safe-conduct from 'Amr and won back many who had left his church."

- **D-M6 MINOR (card `dates`, l.4, and `uncertain` 5, l.34; records `contested_claims` 3; item 1).**
  - The card sets "René Basset's French of the Arabic Synaxarium gives 630 to 648" against the History's thirty-nine years. In Basset the dates stand in parentheses after "le trente-huitième de la liste (630-648)" (BASSET l.40726-40727). The parentheses read as the editor's.
  - The same text ends "mourut après avoir exercé le patriarcat pendant trente-neuf ans" (l.40875-40876; also l.40597). That agrees with the History and the Ethiopic Synaxarium.
  - Fix, in `dates`, the last sentence: "René Basset's French of the Arabic Synaxarium adds 630 to 648 in parentheses, though its text also counts thirty-nine years".
  - Fix, in `uncertain` 5, the second sentence: "Basset's synaxarium has 630 to 648 in parentheses, though its text counts thirty-nine years."
  - In the records, add the text's own count to side 2.

- **D-M7 MINOR (card `legacy.traces` 3, l.19, and `uncertain` 5, l.34; item 5).** "A note in the 1895 English edition of Abu Salih" and "the 1895 edition gives 622 to 660" put a role where a witness belongs. The notes carry no "(A. J. B.)", so by the preface they are the editor's (ABUSALIH l.129-134, 9662-9665, 11738-11741).
  - Fix, `traces` 3, second sentence: "B. T. A. Evetts, in a note to his 1895 English Abu Salih, says those monasteries were restored in Benjamin's time."
  - Fix, `uncertain` 5, third sentence: "In a note to his 1895 Abu Salih, B. T. A. Evetts gives 622 to 660 with a question mark."

- **D-M8 MINOR (card `uncertain` 5, l.34; item 8; names with no context).** "the count of Abulbircat" and "Elmacinus" mean nothing to a general reader. Renaudot means the "Canon Chronologicus" as Abulbircat gives it (l.11590-11591; elsewhere "Canon Chronologicus apud Abulbircat", l.16823). He calls the second "Georgius filius Hamd, vulgo Elmacinus dictus", who wrote a history from the creation (l.441-442).
  - Fix, fourth sentence: "Renaudot rejects the count of the Chronological Canon that Abulbircat gives, which would put the death in 648."
  - Fix, fifth sentence: "That is a decade earlier than the historian Elmacinus and others give, Renaudot says."

**Note, not a finding.** Hiob Ludolf (1691) also has the Jacobites, under Melkite persecution, side with the Saracens invading Egypt, and he names Benjamin there (`ludolf_commentarius-ad-historiam-aethiopicam-lat_1691.txt` l.51955-51961). The records' contested claim on the return could list him beside Renaudot.

After the fixes (D-M1 to D-M4 in the brief): 405 words, 2:30, FK 8.21, Flesch 60.28, no sentence over 24 words (scratch copy scored).

---

### Gregory of Narek (major; 401 words, 2:29; FK 8.06, Flesch 62.8)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (D-B2, D-M11, D-M12, D-M13) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (D-M9, D-M10, D-M15, D-M16) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS (Ormanian names the Mekhitarists among the orders that won Armenians to the Catholic side; the card adds his judgment of Chamich) |
| 7 | Contested claims both sides | PASS, with D-M10. The Chalcedon reading is told as Chamich's and Issaverdens's, their order is marked, and Serpos's milder version follows. The other side is the Stepanos ruling, which only becomes legible with D-M10. The card adds Lebeau and Ormanian's silence. The pigeons are "the story goes" with Issaverdens's "merely as an anecdote" |
| 8 | Common names | FAIL on the card (D-M13) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | FAIL (D-M9: the who-line comes at the ninth sentence) |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | PASS (`uncertain` 1 repeats the anecdote caveat) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |
| — | Records | FAIL (D-B2, D-M18) |

**Sentences checked and found faithful.**
- P1: the assembly at Ani, the messengers, the roasted pigeons, Friday and "arise ye, and depart" are at CHAMICH l.4837-4856 and ISSAV l.5279-5308.
- P2:
  - Chamich: "the Mukhitharian society of Venice, of which Chamich was a member" (CHAMICH l.23413-23421); "Father Mikael Tchamtchian, of the Mekhitarists of Venice" (Ormanian l.8838-8839).
  - "printed in the year 1784" (Nurikhan l.7504-7505).
  - The quotation is verbatim at ISSAV l.5316-5319.
- P3: "brought up from his infancy in the convent of Narek, and in process of time became its abbot" is at CHAMICH l.4813-4816, and "the province of the Rushtunians" at l.4026-4027. Serpos's "discepolo, ed allievo del testé nominato Dottore, ed Abbate di Narek Anania" is at t3 l.17994-17996, and "Anania Dottore, ed Abbate del famoso monistero di Narek" at t3 l.17970-17972.
- P4:
  - Chamich l.4817-4842 and ISSAV l.5273-5288.
  - Ormanian l.9124-9135, and "formerly Armenian Patriarch of Constantinople" on his title page (l.90).
  - Serpos t2 l.1697-1712.
  - Stepanos at MACLER l.4346-4350 and GELZER l.6502-6505.
- P5: the vision, the book and the twenty-six are at CHAMICH l.4877-4892. Serpos's "nel ventesimo anno ... a conforto d'un pio Re Bagratida" is at t2 l.1688-1693.
- P6: "The two following prayers were composed by the celebrated Doctor St. Gregory Naregatzi" and "we implore Thee with out-stretched arms and deep groans" are at ISSRIT l.837-848. The Conybeare incipit is verbatim at l.34473-34477, in MS β after the Hour of Rest.
- P7: "On his attaining his fiftieth year he died" is at CHAMICH l.4893. "(† 1003)" and the talisman line are at Ormanian l.7744-7748, verbatim.

**Card, checked against its lines.**
- `otherNames`: "Grigor of Narek" (Ormanian), "Gregorius Narekensis" (CHAMICH), "Naregatzi" (ISSAV l.5271).
- `dates`: Macler's "né en 951, mort en 1003" (l.4005-4006); Conybeare's "circa 960".
- `keyWorks` 1: "that wonderful book of prayers called Narek" (CHAMICH l.4884-4885), and 95 prayers (Serpos t3 l.17997).
- `traces` 2 and 5: Conybeare l.35681-35688; Alishan l.15219-15224.
- `remembered` 1 to 4: Ormanian l.8582-8583, under "The Commemoration of Saints"; ISSAV l.5251-5253; Boré l.2408-2414; Nurikhan l.2386-2388.
- `uncertain` 1 to 6: Macler on Lebeau at l.7770-7774; Serpos on Le Quien at t2 l.1720-1740; the father at CHAMICH l.4562-4578. Ormanian's index shows two mentions only (l.14832-14833).

**Census.** The drafter's four census differences hold. "Book of Lamentations" appears in no held source.

#### Findings

- **D-B2 BLOCKING (records `absent_details` 1 and 4; card `keyWorks` 2, l.21, and `sources`; a false absence).** Joannes Parisot's preface to Aphrahat quotes Gregory twice, Armenian with his Latin.
  - **The commentary on the Song of Songs**, "Explicatio Cantici Canticorum, Venetiis, 1789": "Ea praecipue apud nos quae de lingua graeca vel syriaca interpretata fuerunt, obscure versa sunt in linguam armeniacam" (PARISOT l.1881-1884).
  - **His first panegyric on Jacob of Nisibis**, "Liber precum, Constantinopoli, 1726, p. 322": "Ipse ... arianam haeresim gladio verbi destruxit et dissolvit". Later Jacob is said to have written books "salutares mundo, in quibus [fidem] definivit, maledicentium ora repressit, et indelebiles canones perpetuo stabilivit" (l.1663-1672, 1720-1721; OCR "lacobum", "indelebilQS"). Parisot also says Gregory, "qui circa annum 1003 obiit", was it seems the first Armenian writer to count Jacob among the writers (l.1663-1664).
  - So `absent_details` 4 ("Neither text is held; they are known here only from Chamich, Serpos and Alishan") is false for the commentary. `absent_details` 1 ("Only the opening lines of discourses xii and xli are given") misses the panegyric lines from the 1726 Book of Prayers.
  - Fix, records: add two Documented claims with those quotations and lines. Rewrite `absent_details` 4 to cover the Life by Nerses of Lambron only. Rewrite `absent_details` 1 as "Only the opening lines of discourses xii and xli (CONYBEARE) and two lines of the first panegyric on Jacob of Nisibis, in Parisot's Latin from the 1726 Book of Prayers (PARISOT l.1663-1672), are held."
  - Fix, card `keyWorks` 2, `about`: replace "The text is not among the sources used here" with "Joannes Parisot quotes one line of it in Latin, from a Venice printing of 1789. In it Gregory says that works translated from Greek or Syriac were put into Armenian obscurely."
  - Fix, card `sources.ownWords`: add {"title": "Aphraatis Sapientis Persae Demonstrationes, preface: lines of the commentary on the Song of Songs and the first panegyric on Jacob of Nisibis, in Latin (ed. Joannes Parisot)", "author": "Gregory of Narek", "date": "1894", "language": "Latin translation", "file": "cic/texts/aphrahat_demonstrationes-1-22-syr-lat_parisot1894.txt"}.
  - Optional `traces` item: "Joannes Parisot finds that Gregory was, it seems, the first Armenian writer to count Jacob of Nisibis among the church's writers. His first panegyric on Jacob praises him for destroying the Arian heresy with the sword of the word." This is a paraphrase, with no quotation marks.

- **D-M9 MINOR (brief P2 and P3, l.3 and l.5; items 4 and 10; the who-line is late, and "Mekhitarist" is used before it is explained).**
  - The who-line, "Gregory of Narek was a monk of tenth-century Armenia", is the brief's ninth sentence. The pattern puts it within the first few.
  - "a Mekhitarist monk of Venice" is undefined until Ormanian's sentence in P4.
  - Fix, P2: "Gregory of Narek was a monk of tenth-century Armenia. Michael Chamich tells this story in his History of Armenia, printed in 1784. James Issaverdens retells it in 1875. Both were Mekhitarists, monks of an Armenian order at Venice. "We, however, report this merely as an anecdote," Issaverdens adds, "as it shews the public esteem towards the holy man.""
  - Fix, P3, first sentence: "Chamich says Gregory was raised from infancy at Narek, in the land of the Rushtunians, and in time became its abbot."
  - Sources: CHAMICH l.23413-23421; Nurikhan l.17931 and l.18205 ("Fr. Issaverdenz, Mechitarist of Venice").

- **D-M10 MINOR (brief P4, l.7; items 4 and 7; the Stepanos sentence floats, and it runs to 26 words).** "records a ruling by church fathers" does not say why the ruling matters to Gregory. Stepanos lists the teachers of that time, among them "Anania, le grand philosophe, moine [du monastère] de Narek" (MACLER l.4303-4316; GELZER l.6482-6483). Then "Diese alle ordneten ... an", all of these ruled, that those baptized in the Chalcedonian confession be baptized again (GELZER l.6502-6505; MACLER l.4346-4350). The listener has just heard, in P3, that Anania of Narek was Gregory's teacher. Macler takes the "seigneur Anania" who ordered the ruling to be the catholicos and not the vardapet (l.4392-4394), and the fix does not name who gave the order.
  - Fix: "Stepanos of Taron wrote Armenian history in the same century. He says teachers including Anania of Narek ruled that anyone baptized in the Chalcedonian faith be baptized again."

- **D-M11 MINOR (card `legacy.traces` 1, l.30; item 1; overstated).** "two of his meditations used in the breviary". Conybeare gives only their opening lines. They come in one manuscript, after "a break, intended to show that the rite proper is finished" (l.34470-34477, 34530-34531). Fix: "In F. C. Conybeare's Rituale Armenorum, one manuscript adds the opening lines of two of his meditations after the prayers before sleep. These are discourses xii and xli. The second begins "Sons of the living God.""

- **D-M12 MINOR (card `legacy.traces` 3, l.32; item 1; overstated).** "Armenian manuscripts set that story apart from the Gospel". Issaverdens says it "is found at the end of that gospel, written separately" (ISSRIT l.16079-16081). Fix: "Armenian manuscripts, he says, place it at the end of John's Gospel, written separately."

- **D-M13 MINOR (card `legacy.traces` 4, l.33; items 1 and 8).** "King Sennacherib" needs his place, since the name is the Assyrian king's. "Moved his people" overstates Chamich's "about one-third of the inhabitants" (CHAMICH l.5685-5689). Fix: "In 1021, Chamich says, King Sennacherib of Vaspurakan gave his land to the emperor and took about a third of its people to Sebastia. Monks of Narek went with him, carried Gregory's body, and built a new convent called Narek there."

- **D-M14 MINOR (card `place`, l.10; item 1).** "the province of Rshtunikh in Stepanos of Taron". Gelzer spells it "Rstunikh" (GELZER l.6327-6328), and no held file has "Rshtunikh". Fix: "the province of Rstunikh in Stepanos of Taron".

- **D-M15 MINOR (card `uncertain` 7, l.50; item 4; a loose "only").** "Macler says only that one passage brings Gregory to mind". The card itself cites Macler for Gregory's years and for Lebeau's 977. Fix: "Macler notes that one passage brings Gregory to mind."

- **D-M16 MINOR (card `uncertain` 8, l.51; item 4; a statement with no point).** The item names no uncertainty. What is at stake is the title the census uses. Fix: "The name of the book. The held sources call it the Narek or the book of prayers, and none calls it the Book of Lamentations." I searched every Gregory file for "Lament": none uses the title.

- **D-M17 MINOR (card `keyWorks` 3, l.25; item 1).** The setting "said in a low voice at the foot of the altar" belongs to the first prayer. The second is introduced with "They then say this prayer on the same subject" (ISSRIT l.837-840, 907). Fix: "two prayers in James Issaverdens's English. The first is said in a low voice at the foot of the altar by the one leading the service. In it, the Spirit is implored "with out-stretched arms and deep groans"".

- **D-M18 MINOR (records, claim on Issaverdens; item 1).** The records cite only the title page and Ormanian's San Lazaro to make Issaverdens a Mekhitarist. Neither says he belonged to the order. Fix: add Nurikhan l.17931 ("Fr. Issaverdentz (Mechitarist)") and l.18205 ("Fr. Issaverdenz, Mechitarist of Venice") as the witness.

**Notes, not findings (held, unused; for the drafter).**
- Chamich says Gregory "addressed two harangues" to the crucifix of David's convent (CHAMICH l.4278-4282).
- Serpos says Sergius the Doctor wrote a learned commentary on Gregory's book of prayers (t3 l.18203-18217).
- Issaverdens's Ritual footnote counts Gregory among the Armenian fathers who quote a disputed book as Scripture (ISSRIT l.15956-15958).

After the fixes (D-M9 and D-M10 in the brief): 405 words, 2:30, FK 8.03, Flesch 61.53 (scratch copy scored). The longest sentence is the unchanged P6 line at 25 words.

---

**Verdicts.**
- Benjamin I of Alexandria: NOT CLEAR. 1 blocking (D-B1, records false absence), 8 minor.
- Gregory of Narek: NOT CLEAR. 1 blocking (D-B2, false absence of his held words in Parisot), 10 minor.


