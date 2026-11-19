# R1 review: era 3 batch 8

Round 1 ran in five parts, each by a fresh Opus agent that had not seen the drafting. The parts follow, unchanged.

## R1 review, part A: John Climacus, Liberatus of Carthage (era 3 Who batch 8)

Reviewer: independent Opus, first sight of these drafts. I did not edit any profile file, and made no git, web, paid or model calls. I used local scripts only.

### Method

Bar: `Who_Profile_Pattern.md` (checklist 1 to 14), `CLAUDE.md` ("Trust and source fidelity", "Accessible and rigorous"), batch 6's README and `john-of-biclaro` as the form model, and batch 6's R1 to R5 for the format and the faults they caught. For each id I read the `.brief.txt`, `.card.json`, `audio/<id>.audio.txt` and the scratch records. I opened every cited line in its vendored file and read it in context, folding OCR noise and line breaks. Before accepting any absence I searched all of `cic/texts/`: for `Climac*` / `κλίμακ*` (about 60 files) and for `Liberat*` next to diacon-, archidiacon-, Carthag- and Breviar- (about 45 hits). Brief references are to paragraphs (P1, P2...). Readability comes from `engine.m1.gates.grade_text`, run from the repo root. All the suggested brief fixes for each profile were applied together to scratch copies and scored again: `/tmp/claude-0/-home-user-CIC-Project/9440743b-c163-5ede-bda7-008353992a86/scratchpad/fixA/`.

**Applies to both.** I checked by script that each audio file equals its brief once `[calmly] ` (at the start) and `[warmly] ` (at the start of the last paragraph) are taken out. No tag appears in a brief or card. Every brief fix below has to be carried into the audio. Both cards follow Mark's order, have no empty or null fields, and have at most three `keyWorks`. Every `sources` file exists. I found no British spellings ("marveled" is American). The drafts carry no list lines, so item 14's list-line half was not checked.

---

### John Climacus (drafted as major; 407 words, 2:31; FK 6.5, Flesch 75.0)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (A-M4, A-M6) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (A-M1, A-M2, A-M3) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | FAIL (A-M3: the saint's Life is not marked in the brief) |
| 7 | Contested claims both sides | FAIL (A-B1) |
| 8 | Common names | PASS |
| 9 | One term for one thing | FAIL (A-M2, "Moses") |
| 10 | Story, scene, disputes in place, length | PASS (at the cap) |
| 11 | Readability | PASS |
| 12 | Card order, fields, caveat repeated | FAIL (A-B2) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Sentences checked and found faithful.** P1: John of Raithu's letter, "uti nobis rudibus per litteras aperias quae ad veteris exemplum Mosis in eodem monte divino [viso] spectaculo dignatus inspexisti" (PG88 l.43736-43741). Also "qui ad coelum enituntur, veluti per scalarum gradus" (l.43814-43815) and "Nam si Jacob ovium duntaxat custos … quanto magis gregis ratione pollentis magister … ad Deum iter omnibus ascendet" (l.43821-43823). The brief's "could" softens the "how much more", but this is a paraphrase outside quotation marks. P2: "nisi metus et ingens periculum, ne sanctae obedientiae … jugum … abjicerem, coercuisset … ut onus, quod impar humeris vires meas excedit" (l.43869-43876). The name comes from the book (Labbe l.41325-41327; Barmby npnf213 l.5363-5364). P3: Daniel, "sextum jam decimum aetatis annum", "cervicem … rectori … submisit" (l.42170-42182); Tholas, "ad quintum ab aede sacra lapidem … quadraginta ipsos annos" after "praemisso … suo praeside" (l.42287-42297). P4: the rock, "in suo latibulo … aspicit virum … « …tu securus hic stertis, et Moses vita periclitatur? »", "Sub vesperam", "Immane saxum … minimo minus oppressisset" (l.42620-42630). Also "garrulum nugatoremque … per totius anni spatium tam altum siluit" and "alterum quemdam Moysen ad coenobii praefecturam vi pertraxerunt" (l.42705-42716; AS Mar. 3 has the same Life). P5: step 1 "De abdicatione vitae saecularis" (l.44300). The end of the Ladder is "qui cum esset, ut videbatur, triginta annorum baptizatus, tricesimum gradum … sortitus est: quandoquidem Deus est charitas" (l.86425-86433), which is John's own closing exhortation and not a scholion. P6: Labbe, l.41392-41420 and 41474-41495; Ewald-Hartmann "600, (Sept. 1.)" (l.7718-7719); Barmby "No doubt the John called Climacus" (npnf213 l.5356-5357). P7: Thomas, "Sometimes he read the book of John Climacus" (kempis l.12186; OCR "Climacusr"); "so that wise men marvelled that he had so good an understanding of the book" (l.12188-12191); "the House of Florentius" (l.11821) and "when I resorted oft to Deventer" (l.11829-11830).

**Card.** `knownFor`, `place`, `role`, `keyWorks`, `legacy` and most of `uncertain` match their lines. I checked Labbe's Greek users and Elias of Crete (l.41361-41366, 41434-41435), Clareno 1295 and Venice 1590 (l.41445-41462), Baronius (l.43145-43147; AS l.209384-209387), Gerson and Rader (l.43170-43188), Magister's reckoning (l.41334-41385), Trithemius (l.41429-41434, 43170-43177), Barlaam (l.41465-41470, 41747-41754), Moschus (PG87.3 l.14546-14695), the Menologium (AS l.209399-209404) and the Bollandists' 580 (AS l.209545-209551).

**On the major mark (the coordinator's call).** I found no reason against it. The held record shows his work reaching far beyond his time. Labbe names the Greek writers who used him and Elias of Crete's commentary. The Ladder was put into Latin by 1295 and into everyday Greek in 1590. Thomas à Kempis and Gerard Zerbolt quote him (zerbolt arthur1908 l.6514, 6781). Fourteenth- and fifteenth-century Franciscan witnesses, held in Oliger, record Angelo Clareno's translation and the book's standing in their order (see A-M9). As drafted, though, the extra length goes mostly to the dating dispute, and the Ladder's teaching gets two sentences.

#### Findings

- **A-B1 BLOCKING (brief P6 and audio; item 7; a reading that the sources dispute is told as settled).** "An unnamed monk of Sinai tells that his brother George died within ten months of him." The records list this as a `contested_claim`, and card `uncertain` 6 gives both readings. Rader's Latin reads "intra decimum enim mensem" (PG88 l.43036-43037) and his Greek reads δέκα μηνῶν (l.43027). The Bollandists' Latin reads "Intra decimum enim annum" (AS Mar. 3 l.210144-210145). Both texts carry the promise that comes before it: "non patiar ut annum hunc absolvas, quin me sequaris" (PG88 l.43034-43035; AS l.210142-210143). Fix: tell the promise, which both readings share: "An unnamed monk of Sinai tells that John, as he died, promised his brother George that George would follow him within the year."

- **A-B2 BLOCKING (card `dates`; items 4, 12; process narration and a year from no source in participant text).** "No source used here gives his years. The Library file's header gives about 579 to 649, which is a header and not a source." A participant card should not talk about a Library file header. No other era 3 card does this (checked by grep across batches 1 to 8). It also puts in front of the reader a year that, by the records' own note, rests on no held line. "No source used here gives his years" is also loose, since Labbe, Barmby and Antonius Magister all give years. Fix: replace both sentences with "No source used here gives a firm year of his birth or death." Delete "The Library header's 579 to 649 rests on no held line." from `uncertain` 2 for the same reason.

- **A-M1 MINOR (brief P2; item 4; an undefined term).** "From his book, the Ladder, he was called John Climacus." The listener is not told that the name means "of the ladder". Barmby gives the link: "Scala (κλὶμαξ) Paradisi, whence his name of Climacus" (npnf213 l.5363-5364). The brief also gives no time for John until P6 (Pattern, "who they were, with time and place"). Every held source puts him in the sixth century: "Vixit extremo Christi seculo sexto" (Labbe l.41329-41330); "seculo Christi sexto floruit" (AS l.209389-209390). Barmby's "died early in the 7th century" also has him living through the 500s. Fix: "From his book, the Ladder, he was called John Climacus, from the Greek word for a ladder. He lived in the 500s."

- **A-M2 MINOR (brief P4; items 4, 9; one name for two people).** P1 uses "Moses" for the lawgiver, and P4 then names "his disciple Moses". P4 then ends "like a second Moses", which a listener will take to mean the disciple. Fix: "Later the monks made him head of the monastery by force." If the image is kept, it needs an anchor, for example "…by force, as a second Moses on the mountain of Moses."

- **A-M3 MINOR (brief P3; items 6, 4; the saint's Life not marked, and a place with no context).** The card marks Daniel's work as a saint's Life with a vision and a cure (`uncertain` 1), but the brief tells the vision with no such marking. The Pattern asks that a biographer's record be marked as hagiography. "Raithu" is also never placed. The Bollandists place it: "De Raithu vicino monasterio versus Rubrum mare" (AS l.209523-209524). Fix: "His life comes mainly from a short saint's Life by Daniel, a monk of Raithu, near the Red Sea."

- **A-M4 MINOR (brief P6; items 1, 4; a statement left without its point, and editors with no context).** The brief gives the Gregory letter and Barmby's identification without saying what follows from them: Barmby has John still alive in 600, against Labbe's 560 to 565. "Paul Ewald and Ludwig Hartmann" arrive with no word on who they are. Fix: "…in a letter that its editors, Paul Ewald and Ludwig Hartmann, date to 600. Gregory's English translator, James Barmby, takes this John to be Climacus, still alive then."

- **A-M5 MINOR (brief P7; item 4; no time anchor).** The brief jumps from about 600 to Thomas à Kempis with no time given. The file gives Thomas's years (kempis l.3, "c. 1380-1471"; l.13229). Fix: "In the 1400s, Thomas à Kempis remembered John Ketel…"

- **A-M6 MINOR (card `dates`; item 1; Labbe's statement shifted).** "Labbe and the Bollandists say the Greeks keep his day on 30 March." Labbe says he died on 30 March, "si Menaeis Graecorum fides … ut habet etiam Martyrologium Romanum" (l.41330-41331). It is the Bollandists who say the Greeks keep his memory that day (AS l.209393-209396). Fix: "Labbe gives 30 March as the day he died, from the Greek Menaea and the Roman Martyrology. The Bollandists say the Greeks keep his memory on that day."

- **A-M7 MINOR (card `uncertain` 2 and `dates`; items 1, 7; where Labbe's tale comes from, and a held side missing).** (a) Labbe's link to Peter of Jerusalem comes from Antonius Magister's retelling: "quae ipse parum cautus refert sub finem capitis XV ex narratione monachi Sinaitae" (l.41392-41394). The tale as Rader and the Bollandists print it names no Peter (I searched PG88 l.42840-43060 and AS l.210060-210200 for Petr-/patriarch-). The brief's "a form of the tale" is careful, but the card's "if the Sinai monk's tale is true" is not. (b) Rader reports a further date: "vere Bellarminus anno 530 collocavit" (l.41752). Fix: in `uncertain` 2, "He then argues, from the tale as Antonius Magister retells it, with Peter of Jerusalem's death in it, that if it is true John died between 560 and 565." Then add: "Matthew Rader reports that Robert Bellarmine placed him about 530." Add the Bellarmine side to the records' "When he died".

- **A-M8 MINOR (card `uncertain` 3 and 1; item 1).** (a) "Gregory sent cloaks, blankets and beds … in Barmby's English." Barmby leaves the word untranslated: "15 cloaks, 30 *rachanæ*". His note says the word's meaning is uncertain, "usually supposed to mean some woollen article of dress … Others understand *blankets*" (npnf213 l.5391-5398). Fix: "Gregory sent fifteen cloaks, thirty rachanae, a word Barmby says may mean woolen garments or blankets, and fifteen beds, for a house for the aged…" (b) `uncertain` 1, "an unnamed monk of Sinai, of John's own time", gives Rader's and the Bollandists' label as fact ("synchrono", PG88 l.42962; AS l.210071). Fix: "…from an unnamed monk of Sinai, whom Matthew Rader and the Bollandists call a man of John's own time and print after the Life."

- **A-M9 MINOR (card `legacy.traces` 2; records; a held witness unused).** "Labbe reports that the Ladder is said to have been first put into Latin in 1295 by Angelo Clareno." Livarius Oliger's introduction to Clareno's Expositio (`clareno_expositio-regulae-fratrum-minorum-lat_oliger1912.txt`) prints medieval witnesses to the translation. Bartholomew of Pisa: "loannem Climacum de graeco transtulit in latinum" (l.1793-1794). Bernardino of Aquila: "Iste liber in nostra familia magnae reputationis habetur" (l.1825-1830). Mariano of Florence (l.1846-1848). Fix: add a second clause to the trace: "Franciscan chroniclers of the 1300s and 1400s, printed by Livarius Oliger, credit the translation to Angelo Clareno. Bernardino of Aquila says the book was held in great repute among the Observant friars." Add Oliger to `sources.about` and a records claim, Documented. Optionally, add Zerbolt's quotations as a trace of his reading in the New Devotion.

**Note on brief length.** With A-B1 and A-M1 to A-M5 applied, the brief runs over the cap. I applied them with one trim: P4's silence episode ("Some envied John … begged him to speak.") was dropped, because the date paragraph must keep both sides. The drafter may instead trim the rock vision. With that trim the brief is 408 words.

After the fixes: about 408 words, 2:31, FK 6.6, Flesch 75.3 (scratch copy scored).

---

### Liberatus of Carthage (recorder, standard length; 336 words, 2:04; FK 8.4, Flesch 61.1)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (A-B3, A-M11) |
| 2 | Quotes verbatim | PASS (no direct quotes; the paraphrases match) |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL (A-M12) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS |
| 7 | Contested claims both sides | FAIL (A-M14) |
| 8 | Common names | PASS (Victor of Tunnuna needs context: A-M12) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | FAIL (A-M13, over 2 minutes) |
| 11 | Readability | PASS, narrowly (Flesch 61.1) |
| 12 | Card order, fields, caveat repeated | FAIL (A-M10: the brief has no caveat for the card to repeat) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (a recorder) |

**Sentences checked and found faithful.** P1: ch. 20, "Joannes cognomento Mercurius", the bishops sent "consulere sedem apostolicam, contra legatos Acumicorum Cyrum et Eulogium, negantes … beatam Mariam vere et proprie Dei genitricem", and "papa Joannes, nobis ibi positis, hoc confitendum epistola sua firmavit" (PL68 l.81229-81240). Garnier's reading "Acoemetas" is at l.81349-81350. P2: Agapetus, "Gaius atque Petrus … sed et Liberatus diaconus filius noster, ut apud nos agerent uerbo" (Avellana l.24974-24977); Günther "die 9 Sept. 535" (l.24928). P3: the prooemium, "Peregrinationis necessitatibus defatigatus … contra falsiloquos utrarumque partium sectatores, qui … aliter loquuntur de suis auctoribus quam veritas habet" (PL68 l.75538-75553). P4: ch. 24, "Origenis autem defensor acerrimus … dolore damnationis ejus … damnationem molitus est in Theodorum Mopsuestenum" and "Quod si Theodorus cum dictis suis et hac epistola [Ibae]" (l.82326-82388). "unum in damnationem trium capitulorum condidit librum, pro delictis nostris" is at l.82401-82404. Garnier III is at l.74969-74972, and Mommsen at mommsen1894 l.17574-17576. P5: Victor (mommsen1894 l.19068-19073, 19289-19291); Garnier, "non nisi post episcopi mortem ab Euchayda recesserit" (PL68 l.75566-75568). P6: l.82406-82413. The card's `knownFor`, `dates`, `place`, `role`, `keyWorks` (ch. 2 and 3 are headed "quod auctor sit Nestorianae / Eutychianae haeresis", l.75610-75612, 75770-75772), `legacy` and `uncertain` 1, 2, 4, 5, 6 and 9 all match their lines.

**Absence searches.** The card says "Victor … does not name him in the lines used here". That holds: Victor's chronicle text does not name him. Other held lines name him, but only in editors' notes and notices (Monceaux 1905 l.4556; PL48 l.91067-91073; Hefele v3 l.20198; Mansi 5 to 7, many hits). None is an ancient witness to his life. One is worth recording. The notice of the Council of Carthage of 535 in PL11 says the envoys "Caius et Petrus cum Liberato … Hos Joanne II mortuo appulsos" (`pl11-zeno-optatus-collatio-carthaginiensis_migne.txt` l.75113-75114). That supports Garnier's reason in A-M14 and could be added to the records as a further witness on that side.

#### Findings

- **A-B3 BLOCKING (card `uncertain` 8; item 1; Garnier misreported).** "Who was deposed. … Garnier's note names Reparatus of Carthage, Firmus of Numidia, Primasius, Verecundus and Victor of Tunnuna as those meant." The card presents all five as the deposed. Garnier's note is on "Muneribus ditabantur", and he says Liberatus means "his own Africans" across the whole sentence: rewarded, deposed and hiding alike. He then sorts them. Reparatus "depositus est ac in exsilium missus Euchaidam". Primasius was "ad suam sedem cum muneribus remissus, post damnationem trium capitulorum", that is, rewarded. Verecundus and Victor were "e carcere in carcerem traducti … in monasteria detrusi" (PL68 l.82524-82535; OCR "Iloriim primus" at l.82529). Victor of Tunnuna says that Firmus, "donis principis corruptus", consented (mommsen1894 l.19074-19075). Fix: "Who is meant. The last chapter names no African bishop. It speaks only of bishops rewarded, deposed, exiled or hiding. Garnier's note says Liberatus means his own Africans. Reparatus of Carthage was deposed and exiled to Euchaida. Primasius, primate of Byzacena, was sent back to his see with gifts after he condemned the Three Chapters. Verecundus and Victor of Tunnuna were moved from prison to prison and shut in monasteries. Victor of Tunnuna says that Firmus, primate of Numidia, was won over by the emperor's gifts." Correct the records' claim to match.

- **A-M10 MINOR (brief P2; item 12; no caveat in the brief).** Card `uncertain` 1 opens "His own life is thin in the sources. Nearly all of it comes from his Breviarium and one letter of Pope Agapetus." The brief never says this, so the card has no brief caveat to repeat. My search bears it out (see above). Fix: after "Otto Günther dates the letter to 535." add "His life is known almost only from this letter and his own book." Let `uncertain` 1 open with that sentence.

- **A-M11 MINOR (brief P1; item 1; half of what the pope confirmed is dropped).** The envoys denied two things: Mary as "vere et proprie Dei genitricem; et unum de Trinitate incarnatum et carne passum" (PL68 l.81235-81237). "This teaching" in the next sentence then covers only the first. Nothing is false, but the scene is cut short. Fix, if the words allow (see A-M13): "These two denied that Mary is truly and properly the Mother of God, and that one of the Trinity suffered in the flesh."

- **A-M12 MINOR (brief P3, P4, P5, P6; item 4; wording and context).** (a) "the followers of both sides, who speak of their leaders otherwise than the truth" reads archaic. "Both sides" can also be heard as the two sides of the Three Chapters quarrel, which comes later, when Liberatus means both heresies. Fix: "He wrote to answer the followers of both, who tell of their own leaders other than the truth." (b) "Victor of Tunnuna" appears in P4 and P5 with no word on who he is. Mommsen calls him and Liberatus "aequales et conterranei" (mommsen1894 l.17574). Fix: at first mention, "the African chronicler Victor of Tunnuna". (c) P6, "bishops who agreed": agreed to what? The Latin is "consentientes … in trium damnationem capitulorum" (PL68 l.82407-82408). Fix: "bishops who agreed to condemn them". (d) The brief never says plainly what Liberatus stood for, though the card's `knownFor` does. Garnier: "unus de Africanis trium Capitulorum defensoribus" (PL68 l.74960-74962). Fix: in P4, "Garnier, whose edition Migne reprints, counts him among the African defenders of the Three Chapters."

- **A-M13 MINOR (brief; item 10; length).** 336 words is 2:04, over the 1-to-2-minute range for a recorder at standard length (batch 6 held these to about 325). The fixes above add words, so something must go. The cleanest cut is P4's last two sentences (Garnier's charge of partiality and Mommsen's answer). The card keeps that dispute in full (`uncertain` 6, `legacy.remembered` 3), and A-M12(d) gives the brief Garnier's plain statement of his stance. The full text with A-M10, A-M12 and A-M13 applied is at `…/scratchpad/fixA/liberatus-of-carthage.brief.txt` (328 words). With A-M11 as well it is `…/fixA/lib_alt.txt` (338 words). The drafter chooses. If P4's dispute is kept, A-M11 should be left out to hold the length.

- **A-M14 MINOR (card `uncertain` 3; item 7; a dispute without its reason).** "Garnier reasons that either Liberatus's words are false … or he came to Rome twice." The card leaves out why, so the dispute has no context. Garnier's reason is that the envoys of Agapetus's letter left Africa only after Pope John had died: "non nisi tamen post obitum Joannis … legati solverunt ex Africa" (PL68 l.81394-81395). The PL11 council notice says the same (l.75113-75114). Fix: "…or he came to Rome twice, since the envoys named in Agapetus's letter, Garnier says, left Africa only after Pope John had died."

- **A-M15 MINOR (card `legacy.traces` 3; item 12; misplaced field).** "He reports, as a thing that is said, that Eutyches won leave…" This is something the Breviarium reports, not something that traces to Liberatus. Fix: delete it. It could go to `keyWorks` `about` if wanted.

- **A-M16 MINOR (card `uncertain` 7 and `knownFor`; items 1, 4).** (a) "Mommsen says both, bitter against Pope Vigilius…" drops Mommsen's own judgment, "iusto odio exacerbati" ("embittered by a just hatred", mommsen1894 l.17577). Fix: "Mommsen says both, embittered against Pope Vigilius by a hatred he calls just, give a letter of his that some think forged." (b) `knownFor` uses "the Three Chapters" undefined. Bossuet defines them (npnf214 l.22886-22888). Fix: "…down to Justinian's book against the Three Chapters: Theodore of Mopsuestia, Theodoret's writings against Cyril and the letter of Ibas of Edessa."

After the fixes (A-B3 is card only; A-M10, A-M12 and A-M13 in the brief): 328 words, 2:01, FK 8.5, Flesch 60.7 (scratch copy scored). Flesch sits near the floor. Any further additions should be checked again with `grade_text`.

#### Verdicts

- John Climacus: NOT CLEAR (2 blocking, 9 minor).
- Liberatus of Carthage: NOT CLEAR (1 blocking, 7 minor).

---

## R1 review, part B: Dionysius Exiguus, Marius of Avenches (era 3 Who batch 8)

Reviewer: independent Opus, first sight of these drafts. I edited no profile file, ran no git, web or paid calls, and used local scripts only.

### Method

Bar: `Who_Profile_Pattern.md` checklist 1 to 14; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; batch 6 README and the `john-of-biclaro` profile as the form model; batch 6 R1 to R5 for the finding format and the recurring faults (false absences, editor's years told as the source's, partial sides). Majors are capped at about 405 words (2:30); recorders at standard length, at most about 325 words (2:00).

Files read for each id: `.brief.txt`, `.card.json`, `audio/<id>.audio.txt`, and `scratchpad/records/<id>.json`. I opened every cited line under `cic/texts/` and read it in context, folding OCR noise and hyphen breaks. Files: PL 67 (`facundus-ferrandus-caesarius-dionysius-pl67-lat_migne1865.txt`, "pl67"), PL 70 Institutions ("pl70"), PL 72 (`john-biclaro-leander-pl72-lat_migne1878.txt`, "pl72"), Mommsen's Chronica minora 2 ("chron-min-2"), Maassen 1893, Krusch's Fredegar, Plummer's Bede, Brehaut, Hodgkin, Percival (npnf214), Duchesne's Liber pontificalis I ("LP1"), Alcuin PL 100-101, and Dalton's Gregory of Tours v2. Before accepting any absence I searched all of `cic/texts/` for the person and the point. That search found a held critical witness the Dionysius draft leaves out: Louis Duchesne, already on the card, at LP1 l.16343-16347 and l.30095-30152. Brief paragraph lines are given as file lines, with blank lines counted (paragraphs sit on l.1, 3, 5 and so on). Readability came from `engine.m1.gates.grade_text`, run from the repo root. I applied all suggested brief fixes for each profile to scratch copies and re-scored them: `/tmp/claude-0/-home-user-CIC-Project/9440743b-c163-5ede-bda7-008353992a86/scratchpad/fixB/dionysius.txt` and `/tmp/claude-0/-home-user-CIC-Project/9440743b-c163-5ede-bda7-008353992a86/scratchpad/fixB/marius.txt`.

**Applies to both.** Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). Each has one `[warmly]`, at the start of the closing paragraph, and no tag appears in a brief or card. Every brief fix below must be carried into the audio. Batch 8 has no README yet. When one is written, it should record the Dionysius major mark and his tradition placing as the coordinator's calls (B-M10).

---

### Dionysius Exiguus (drafted as major)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (B-B1, B-M5) |
| 2 | Quotes verbatim | PASS (no quotation marks; reported speech checked) |
| 3 | No invention | PASS |
| 4 | Reading aids, no AI tells | FAIL (B-B2, B-M1, B-M2, B-M3) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS (Cassiodorus knew him; card `uncertain` 2 says so) |
| 7 | Contested claims both sides | FAIL (B-B1, B-M4) |
| 8 | Common names | FAIL (B-M6) |
| 9 | One term for one thing | PASS |
| 10 | Story, scene, disputes in place, length | PASS (404 words, 2:30) |
| 11 | Readability | PASS (FK 7.6, Flesch 68.4) |
| 12 | Card order, fields, caveat | FAIL (B-M7, B-M8, B-M9) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Sentences checked and found faithful.** L.1: "ut quoscunque libros Graecos in manibus acciperet, Latine sine offensione transcurreret, iterumque Latinos Attico sermone relegeret; ut crederes hoc esse conscriptum, quod os ejus inoffensa velocitate fundebat" (pl70 l.83504-83511). L.3: "Dionysius monachus, Scytha natione, sed moribus omnino Romanus" (pl70 l.83555-83557, clean at pl67 l.11038-11042); "Qui mecum dialecticam legit" (pl70 l.83585); "ut in nullo se vel extremis famulis anteferret, cum dignus esset regum … colloquiis" (l.83597-83601). Rome: Bede's "abbas Romanae urbis" (pl67 l.11088) and Cave's "abbas Romanus" (l.413). L.5: "petitus a Stephano episcopo Salonitano ex Graecis exemplaribus canones … composuit, quos hodie usu celeberrimo Ecclesia Romana complectitur. Hos etiam oportet vos assidue legere" (pl70 l.83605-83620); the preface to Stephen, "canones qui dicuntur Apostolorum … quibus quia plurimi consensum non praebuere facilem" (pl67 l.11155-11161). L.7: "Juliano presbytero tituli Sanctae Anastasiae … praeteritorum sedis apostolicae praesulum constituta … collegi" (pl67 l.18475-18480); the letter to Eugippius, "librum De Conditione hominis e Graeca locutione converti … aliqua quae possunt merito reprehendi, nullus lector in his meum putet obligatum esse consensum; quia officio translatoris explicui, non censoris judicio comprobavi" (l.27739-27775). L.9: letter II, "diu sancto ac venerabili Petronio episcopo commonente" (l.1418-1420); letter I on Nicaea, the nineteen-year circle and Cyril (l.1105-1151), and Diocletian and the Incarnation with both purpose clauses (l.1157-1165). L.11: Cave, "istam aeram primus omnium annis supputandis adhibuit" (l.500-502); Janus's note (f), "Alii eam Dionysio juniorem faciunt, et Bedae auctoritate demum invectam putant" (l.36727-36730); Plummer (plummer1896 l.2666-2688). L.13: "Interveniat pro nobis, qui nobiscum orare consueverat, ut cujus hic sumus oratione suffulti, ejus possimus nunc meritis adjuvari" (pl70 l.83601-83605), written of him as dead (l.83555-83559 right column).

**Card.** I checked each `keyWorks`, `legacy` and `uncertain` statement at its cited lines: Ceolfrid (plummer1896 l.29186-29189), Mommsen (chron-min-2 l.9390-9392), the Alcuin treatise (l.78417-78430), Duchesne on Hadrian (LP1 l.34721-34723), Bede and Bellarmine in the testimonia (pl67 l.11085-11115), the Easter rules' 525 (l.39553-39562) and Janus on the argumenta (l.36681-36682), Janus to Hoffmann on Cassiodorus, the monastery, Pagi and Felix (l.41270-41308), Cave on Proclus and Garnier (l.470-473), Hodgkin (l.3428-3434), Brehaut (l.6743-6745), and Percival (npnf214 l.2198-2200). All are faithful except as noted below.

**Major mark.** I support the major mark. He made the canon collection the Roman church used (Cassiodorus) and that Pope Hadrian sent to Charlemagne (Duchesne). He drew up the Easter table received in Italy (Mommsen) and numbered it from the Incarnation. The brief carries all three and stays inside the cap after the fixes. If the coordinator rules him standard length, the cut to about 325 words should drop paragraph 7's Eugippius sentences and paragraph 3's servants line before it touches the Easter or canon paragraphs.

#### Findings

- **B-B1 BLOCKING (brief l.9, audio; card `keyWorks` 3, `uncertain`; records `contested_claims`; items 1, 7; a claim the held witness calls false is passed on without him).** The brief says: "Dionysius followed the bishops of Nicaea, he wrote, and their nineteen-year cycle, which Cyril of Alexandria had kept." A listener hears that Nicaea laid down the nineteen-year cycle. Louis Duchesne, whose Liber pontificalis the card already cites, says that ruling never existed. He says Dionysius worked it out of an Alexandrian letter: "Cette décision n'a jamais existé ; c'est Denys qui l'a déduite, par une exégèse habile, de la lettre de Proterius d'Alexandrie au pape saint Léon sur la question pascale (Krusch, l. c. p. 107)" (LP1 l.16343-16347). Elsewhere: "il a transformé en Pères du concile de Nicée les beatissimi patres nostri de Proterius, c'est-à-dire ses prédécesseurs sur le siège d'Alexandrie. Il y a évidemment ici, comme l'a fait remarquer M. B. Krusch …, une pia fraus mise au service d'un bon comput" (l.30101-30152). Neither the card nor the records carry this. Fix, brief l.9 (and audio), replacing its first two sentences: "At the urging of Bishop Petronius, Dionysius set out the rule for Easter. He wrote that he followed the bishops of Nicaea and their nineteen-year cycle, which Cyril of Alexandria had kept. Louis Duchesne says Nicaea made no such ruling, and that Dionysius drew it from a later letter from Alexandria." To keep the paragraph within the cap, its next two sentences become one: "Cyril had counted his years from the emperor Diocletian, but Dionysius would not tie his tables to the memory of a wicked persecutor." Fix, card: add to `uncertain`, after item 1: "The Nicene rule. Dionysius says the bishops of Nicaea fixed the nineteen-year cycle. Louis Duchesne, after Bruno Krusch, says Nicaea made no such ruling, and that Dionysius drew it from the letter of Proterius of Alexandria to Pope Leo. With Krusch, he calls it a pious fraud put to the service of a sound reckoning." Fix, records: add a `contested_claim`, "Whether the Council of Nicaea fixed the nineteen-year Easter cycle", with the sides "Dionysius, letter I (pl67 l.1105-1151) and letter II (l.1421-1423)" and "Duchesne after Krusch (LP1 l.16343-16347, 30101-30152)".

- **B-B2 BLOCKING (brief l.11, audio; card `uncertain` 1; item 4; a thesis opener that does not parse).** The sentence "Whether the count of years from Christ spread from him is a later judgment." says that a question is a judgment. It opens the paragraph on an abstraction, and a listener cannot tell what is being claimed. The card's `uncertain` 1 opens the same way, so the caveat repeats the fault. Fix, brief l.11 (and audio): "Later writers differ over his part in the count of years from Christ." In the same paragraph, "notes that some give the credit to Bede" becomes "notes that some credit Bede", for length. Fix, card `uncertain` 1, first sentence: "Later writers differ over his part in the count of years from Christ."

- **B-M1 MINOR (brief l.9; item 4; narrator's "our").** "That way the start of our hope would be better known …" has no speaker in its own sentence. A listener hears the narrator say "our hope". Fix: "That way, he wrote, the start of our hope would be better known, and the Redeemer's passion would shine more clearly." Dropping "the cause of our renewal" keeps the length. This is paraphrase, not a quote, and both purpose clauses stay.

- **B-M2 MINOR (brief l.3, l.5; item 4; undefined terms).** "Dialectic" and "canons" are technical terms with no gloss. Fix: "The two studied logic together." And: "… to put the church's canons, or council rulings, into Latin from Greek copies." Also, "warned" is used twice in two paragraphs (l.5 and l.7), and on l.5 the source only says he did not want Stephen to be unaware: "hoc ipsum vestram noluimus ignorare sanctitatem" (pl67 l.11161-11162). Fix, l.5: "… and noted that many did not readily accept them."

- **B-M3 MINOR (brief l.13; item 4; tense break in the close).** "Cassiodorus wrote after his death … He asks him now …" changes tense in the middle. Fix: "He asked him then to plead for them, so that those once upheld by his prayers may be helped by his merits."

- **B-M4 MINOR (card `uncertain` 1; records `contested_claims` 1; item 7; a held side left out).** Janus's note (f) gives two opposed camps, not one. Some make the era later than Dionysius and credit Bede. Others make it older, among them Jean Hardouin: "alii contra Dionysio antiquiorem statuant. In his Joannes Harduinus, aeram vulgarem Christianam, jam saeculo v ineunte, in toto orbe Christiano usitatam fuisse, contendit, annis fere 129 ante Dionysium" (pl67 l.36730-36734). Janus argues against Hardouin (l.36736-36760) and keeps the common view (l.36823-36825). Fix, card `uncertain` 1, after the Janus sentence: "Janus also reports Jean Hardouin's view that the era was in use across the Christian world early in the fifth century, before Dionysius, and argues against it." Add the same line to the records' second side. The brief can stay as it is.

- **B-M5 MINOR (card `uncertain` 5; records; item 1; a held charge about his translations left out).** The card's item on his translations gives only the Proclus dispute. Duchesne, after Friedrich Maassen, says Dionysius's version of the Alexandrian council's letter against Nestorius, which Cave lists among his works (pl67 l.453-455), was copied: "Sa version du concile alexandrin de l'année 430, qu'il présente comme la première qui en ait été faite et comme son œuvre personnelle, est tout simplement copiée sur celle de Marius Mercator (Maassen, Quellen, t. I, p. 132-135)" (LP1 l.30096-30099). Fix, card `uncertain` 5, add: "Louis Duchesne, after Friedrich Maassen, says that his Latin version of the Alexandrian council's letter against Nestorius, which he presents as the first and as his own, is copied from that of Marius Mercator." Add a records claim with these lines.

- **B-M6 MINOR (brief l.9; records `absent_details`; item 8; a common name with no place, and no gap logged).** "Bishop Petronius" has no see. Neither letter names it (pl67 l.1103, 1420), and neither does Janus (l.36450). The Pattern lets the name stand where no vendored source gives a place, but only if the gap is logged. The records do not log it. Fix: add to `absent_details`: "Petronius's see. Searched pl67 and all of cic/texts for Petroni* near Dionys*/Exigu*; no held line names it. The brief gives him as 'Bishop Petronius'." Log it in Open-Gaps.

- **B-M7 MINOR (card `dates`, `uncertain` 3; item 12; a print-damage note in participant text).** "Cave's year for when he flourished is damaged in the print and reads "5 5"" tells a participant nothing about Dionysius. It is a note about how the text was checked. Fix: delete that clause from `dates` and the sentence "Cave's year for when he flourished is damaged in the print." from `uncertain` 3. Keep it in the records' Cave claim.

- **B-M8 MINOR (card `role`; item 12; at odds with the card's own `uncertain` 4).** "Monk, called abbot by later writers" conflicts with `uncertain` 4, which says Cassiodorus's own chapter heading calls him abbot ("De abbate … Dionysio", pl70 l.83524). Fix: "Monk, called abbot in some sources; translator from Greek; collector of church canons and papal rulings; maker of Easter tables".

- **B-M9 MINOR (card `uncertain` 6, `sources.about`; item 12; jargon and a witness folded into another).** (a) "No held line ties him to the writings under the Areopagite's name" uses the Library's word "held". Fix: "No source used here ties him to the writings under the Areopagite's name." (b) The source entry "Ecclesiastical History V.21, with Ceolfrid's letter, and Charles Plummer's introduction", with author "Bede", puts Plummer's words under Bede. Fix: split it into "Ecclesiastical History V.21, with Ceolfrid's letter" (author Bede, Latin) and "Introduction to Bede's Historical Works" (author Charles Plummer, 1896, English), both with the same file. (c) If B-B1 and B-M5 are applied, check that Duchesne's title in `sources.about` still covers both the introduction and the notes. "Le Liber pontificalis, volume 1" does.

- **B-M10 MINOR (card `tradition`; README; process).** The records list "Early Benedictine / Italian Monasticism" as the "drafter's call". The supplement scan placed him in "Byzantine imperial church (Justinianic); Latin canon law" (`Who_Scan_Supplement.md` l.144). The placing is reasonable: he was an Italian monk, and Cassiodorus pairs him with Eugippius. But as with Severinus of Noricum in batch 6, it needs the coordinator's confirmation. It should also be logged in Open-Gaps and in the batch 8 README, together with the major mark. Fix: the coordinator confirms or changes the placing and logs it. No card text changes unless the placing does.

Not a finding: Duchesne also says Dionysius published his cycle in 525 (LP1 l.16126-16127). That would give the card's 525 a witness besides the example year in the Easter rules, if wanted.

After the fixes: 406 words, 2:30, FK 7.9, Flesch 66.0 (scored on the scratch copy).

---

### Marius of Avenches (recorder, standard length)

| # | Item | Result |
|---|---|---|
| 1 | Each sentence sourced | FAIL (B-M12) |
| 2 | Quotes verbatim | PASS (no quotation marks; Chronicle paraphrase checked) |
| 3 | No invention | PASS |
| 4 | Reading aids, no AI tells | FAIL (B-M13, B-M14) |
| 5 | Named witnesses | PASS |
| 6 | Partisan witness marked | PASS (the epitaph is named as such) |
| 7 | Contested claims both sides | PASS |
| 8 | Common names | FAIL (B-M14) |
| 9 | One term for one thing | FAIL (B-M13) |
| 10 | Story, scene, length | FAIL (B-M11) |
| 11 | Readability | PASS (FK 6.6, Flesch 70.7) |
| 12 | Card order, fields, caveat | FAIL (B-M15, B-M16) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder) |

**Sentences checked and found faithful.** L.1: the Tauretunensis fall, the fort and villages, the lake "ita totum movit, ut egressus utraque ripa vicos antiquissimos cum hominibus et pecoribus vastasset", the bridge at Geneva "cum molinas et homines", and the city (chron-min-2 l.21582-21590), under "p. c. Basili ann. XXII", which Mommsen's margin makes 563. L.3: "MARII EPISCOPI AVENTICENSIS CHRONICA A. CCCCLV-DLXXXI" and "subiungere chronicis Prosperianis" (l.20691-20697, 20797-20798). "Burgundian lands": "quae pertinent ad Burgundionum regionem" (l.20927-20928) and Gallandi's "Burgundiae regnum in quo Aventicus et Lausanna censebantur" (pl72 l.59546-59548). L.5: "Marius episcopus ecclesiae Auentice subscripsi" under "anno XXIIII regni … Gunthramni" (Maassen l.13745; chron-min-2 l.20710); Conon "quae composuit a. 1235" (l.20716-20717); the epitaph (l.20729-20768). L.7: Mommsen's 574, 587, 594, and his rejection of 601 and 581 (l.20769-20786); Gallandi after Chifflet, 596 (pl72 l.59565-59569). L.9: Mommsen on the move (chron-min-2 l.20792-20795); Gallandi, Le Cointe after Claude Robert (pl72 l.59536-59545). L.11: "potissimum respexit res gestas Agauni … et per universam Vallem Poeninam" (l.20925-20927); 515 and 565 (l.21183, 21594-21597); "Unicus per quem Marii chronica ad nos propagata sunt codex" (l.20936-20937); "Medio aevo Marii chronica non sunt adhibita" (l.20948). L.13: the necrology of about 1510 (l.20786-20790). All first names (Pierre-François Chifflet, Claude Robert, Charles Le Cointe) are in held files (pl72 l.59693, 59544, 6624).

**Card.** Checked: Maassen's "585. (Oct. 23?)" (l.13055); Conon's 20 years 8 months and 63 or 64 years (chron-min-2 l.20718-20725); the epitaph's "iusto bonus arbiter … norma sacerdotum pontificumque decus" (l.20745-20747); the consular reckoning "Mario nostro propria est et omnino perversa" (l.20823); the first writing to 567 (l.20780-20782); Krusch on Avenches (fredegar l.457-465); Chifflet's 1636 edition and his view of Gregory (chron-min-2 l.20955-20957; pl72 l.59600-59615); the burial at Saint Thyrsus (pl72 l.59578-59580). Plague and floods in `keyWorks` are in the Chronicle (chron-min-2 l.21682, 21689, 21761-21763). Faithful except as noted below.

#### Findings

- **B-M11 MINOR (brief, audio; item 10; over standard length).** The brief is 337 words, about 2:05, past the 2:00 standard for a recorder. The fixes in B-M12 to B-M14 bring it to 325 words. They drop the Gallandi sentence from l.7, since the card's `uncertain` 1 keeps it and the dispute still shows both sides in the brief (Mommsen against Conon and the annals). They also shorten l.9: "The bishop's seat later moved from Avenches to Lausanne. Mommsen thinks this came after Marius. Andrea Gallandi reports Charles Le Cointe's view that Marius moved it himself." And on l.5, "who wrote in 1235" becomes "writing in 1235".

- **B-M12 MINOR (brief l.5, l.11; item 1; epitaph praise told as fact, and a source softened).** (a) "He made sacred vessels for the church and worked his lands with his own hands. He fed the poor and ate sparingly himself." These lose the epitaph's attribution after the first sentence, so a verse eulogy is heard as biography. Fix: "He made sacred vessels for the church and worked his lands with his own hands, it says. He fed the poor and ate sparingly himself." (b) "Its monks, he says, later rose one night against their bishop Agricola" softens the source, which says they tried to kill him: "episcopum suum Agricolam cum clero et cives, qui cum ipso erant, occidere nitentes" (chron-min-2 l.21594-21596). Fix, folded into B-M14.

- **B-M13 MINOR (brief l.7, l.9, l.13; items 4, 9; loose wording and two terms for one thing).** (a) "Conon dates the start of his rule to 581" uses "rule" where the paragraph has just said "became bishop". Fix: "Conon gives 581 for his becoming bishop". (b) "later annals of Lausanne put his death in 601" is not quite what the source says. The annals were written in the late tenth century, and a later hand added the 601 entry: "adscriptum est manu recentiore ad a. 601" (l.20712-20714). Fix: "and a later hand in the annals of Lausanne puts his death in 601." (c) "The see of Avenches" uses "see" with no gloss. Fix: as in B-M11, "The bishop's seat later moved from Avenches to Lausanne." (d) On l.13, "still marked his day" implies an unbroken memory, which the 1510 necrology alone does not show. Fix: "marked his day".

- **B-M14 MINOR (brief l.11; items 4, 8; an unclear "he", an undefined place, a common name with no identifier).** "Mommsen says Marius looked most to Agaune and the Valais. He tells of King Sigismund founding the monastery at Agaune." Here "he" could be Mommsen or Marius. "Looked most to" is vague. "King Sigismund" needs his kingdom, which Dalton gives: "Sigismund, king of Burgundy" (dalton1927 l.30447). Fix, the whole paragraph: "Marius wrote most about Agaune and the Valais, Mommsen says. He records that King Sigismund of Burgundy built the monastery at Agaune, and that its monks later tried one night to kill their bishop, Agricola. A single manuscript keeps the Chronicle, which Mommsen says went unused in the Middle Ages." No held line gives Agricola's see. "Their bishop" identifies him, and the gap should be logged in `absent_details`.

- **B-M15 MINOR (card `keyWorks` 1, `legacy`; items 1, 12; wording the sources do not support).** (a) "a single manuscript of the tenth century, which closes "usque hic Marius aepiscopus"": the manuscript does not close there. Isidore's chronicle and an addition to 624 follow (chron-min-2 l.20941-20943). Fix: "… of the tenth century, in which his part ends "usque hic Marius aepiscopus"". (b) `traces` 1, "Mommsen says Marius and … Gregory of Tours drew on the same Gallic annals": Mommsen says Gregory "videtur adhibuisse" them (l.20910-20911). Fix: "Theodor Mommsen thinks Marius and his contemporary Gregory of Tours drew on the same Gallic annals …". (c) `remembered` 2, "held to have been enrolled among the saints on the day he died", can be heard as a canonization on his deathbed. Gallandi means that his feast falls on the day of his death, 31 December ("Qua quidem die Sanctorum ordinibus ascriptus traditur", pl72 l.59570-59571). Fix: "Andrea Gallandi says tradition counts him among the saints, with his day on the day of his death."

- **B-M16 MINOR (card `sources.about`, `uncertain` 3; item 12; a source with no statement, and an undefined name).** (a) Dalton's "History of the Franks IV.31" is listed, but no card sentence rests on it. It is worth using, because Gregory tells the same fall: "a great prodigy occurred at the fortified place of Tauredunum … the whole way down to the city of Geneva" (dalton1927 l.6697-6712). Dalton's note also says Sigismund "restored" the monastery at Agaune (l.30446-30447), where Marius says "constructum". Fix: add to `legacy.traces`: "Gregory of Tours tells the same fall of Tauredunum in his History of the Franks, and O. M. Dalton's note points to Marius's account of it." Add to `uncertain`: "Agaune. Marius says King Sigismund built the monastery. O. M. Dalton, in his notes to Gregory of Tours, says Sigismund restored it." (b) `uncertain` 3, "his birth among the Aedui": the name is not explained. Fix: "… among the Aedui, the people of the diocese of Autun." Conon's "episcopatu Eduensi" is the card's own "diocese of Autun".

After the fixes: 325 words, 2:00, FK 7.0, Flesch 68.3 (scored on the scratch copy).

---

#### Verdicts
- Dionysius Exiguus: NOT CLEAR (2 blocking, 10 minor). Major mark supported.
- Marius of Avenches: CLEAR (0 blocking, 6 minor). The minors, above all the length (B-M11), should still be applied.

---

## R1 review, part C: Martin of Braga, Brendan of Clonfert (era 3 Who batch 8)

Reviewer: independent Opus, first sight of these drafts. I edited no profile file and made no git, web, paid or model calls. I used local scripts only.

### Method

The bar was `Who_Profile_Pattern.md`, review checklist items 1 to 14, together with `CLAUDE.md` ("Trust and source fidelity", "Accessible and rigorous") and the batch 6 README form. Both profiles are standard length, at 1 to 2 minutes; batch 6 ran about 320 to 326 words. For each id I read the `.brief.txt`, the `.card.json`, `audio/<id>.audio.txt` and the scratchpad records file.

I opened every cited line in its vendored file, folding the OCR noise, and read each hit in context to see who speaks there: the ancient text, a translator, an editor's note, a margin or a file header. Where a claim rests on an absence ("say nothing", "no annal", "only"), I searched all of `cic/texts/`. The patterns were `Brend|Brenainn|Brandan|Brendin|Clonfert|Cluain.fert|maccu.?Alt|Navigatio` and, for Martin, `Dumi|Bracar|non 30|Mondonedo`. That search found held witnesses the drafts do not use:
- Brendan: the York prymer calendar's "brandani episcopi" on 16 May (Surtees `horae-eboracenses` l.4186, index l.18515).
- Brendan: a Bollandist note on the founding of Cluain-ferta by "S. Brandano", which became an episcopal see (`acta-sanctorum_augusti-tomus-1` l.58934-58941).
- Brendan: a second copy of the Barre-and-Brendan story in the Life of David (`acta-sanctorum_martii-tomus-1` l.16355-16367).
- Brendan: Hugh Williams's "Brendan, who founded Clonfert" (gildas williams1899 l.9111-9112).
- Martin: a note signed "R." in the MGH History that glosses Dumio as Mondonedo (arndt-krusch1885 l.18215).

The Tripartite Life index entry "Brenainn Maccu-Altai, xlii., 208" (stokes tripartite v2 l.21933) points to volume I, which is not held. It is not a missed witness.

Readability comes from `engine.m1.gates.grade_text`, run from the repo root. Brief line numbers are paragraph lines, with blank lines counted. I applied the brief fixes to scratch copies and re-scored them: `/tmp/claude-0/-home-user-CIC-Project/9440743b-c163-5ede-bda7-008353992a86/scratchpad/fixC/martin.txt` and `/tmp/claude-0/-home-user-CIC-Project/9440743b-c163-5ede-bda7-008353992a86/scratchpad/fixC/brendan.txt`.

#### Applies to both

- **Audio = brief.** Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). `[warmly]` sits at the start of the closing paragraph in each. No tag appears in a brief or card. Every brief fix below must be carried into the audio.
- **Readability as drafted.** Martin: 331 words (2:03), FK 7.7, Flesch 66.8. Brendan: 333 words (2:03), FK 6.7, Flesch 73.9. Both pass. No brief sentence passes 25 words.
- **Card form.** Both cards are in Mark's order, with no empty fields, and every source file exists. Brendan has no `keyWorks` and no `ownWords`, which is right, since none is held. Card sentences past about 25 words are noted under each profile.
- **No quotation marks in either brief.** All source matter is in reported speech, so the rendering rule is not engaged.
- **Item 14 (list line).** The drafts carry no list lines. Those belong to the map build and were not checked.

---

### Martin of Braga

| # | Item | Result |
|---|---|---|
| 1 | Sources establish each sentence | PASS with notes. Every brief sentence traces to a held line (below). Card: C-B2. |
| 2 | Quotes verbatim | PASS. There are no quotation marks. Every Latin line in the records matches its file through the OCR: VM I.11 l.46019-46028, HF V.37 l.18175-18181, PL72 epitaph l.3435-3440, PL83 l.122413-122429 and 120277-120286, Hispana l.56907-56955 and 57283-57322, caspari1883 l.3700-3712 and 4881-4887. |
| 3 | No invention | PASS. |
| 4 | Writing | FAIL (minor): C-M1, C-M2, C-M3, C-M4, C-M9. |
| 5 | Named witnesses | PASS. |
| 6 | Partisan witness | n/a. |
| 7 | Disputes both sides | PASS in the brief (Isidore against Gregory on the king, in place). Card: C-M6, C-M7. |
| 8 | Common names | Brief PASS. Card FAIL (minor): C-M8. |
| 9 | One term | PASS. |
| 10 | Story, scene, length | FAIL: C-B1 (no time anchor until the death paragraph). The length is about 2 minutes, which is in range. |
| 11 | Readability | PASS. |
| 12 | Card order, caveat repeated | PASS on order. The caveat is weak: the brief does not mark its opening as a miracle story, but `uncertain` 1 does (C-M1). |
| 13 | Audio tags | PASS. |
| 14 | Who test | PASS: own works (sermon, Formula, Capitula) and a council record. |

Brief sentences checked against their sources:
- **The scene (l.1).** The sick son, the relics, Martin coming "de regione longinqua" and entering a Galician port "simul cum ipsis pignoribus", the healing and the king's confession: VM I.11, arndt-krusch1885 l.45603-45605 and 46019-46028. The tomb is first sent gold and silver, then asked for relics (l.45950-46000). "Sent to the tomb … for relics" compresses this fairly.
- **The who-line (l.3).** "Bishop of the monastery of Dumio" is Isidore's "Dumiensis monasterii … pontifex" (PL83 l.122416-122417). "Later of Braga" rests on Braga II, "Martinus Bracarensis ecclesiae episcopus" (Hispana l.56912). The journey East is Gregory's (HF V.37 l.18176-18177).
- **The Leovigild sentence (l.3).** John of Biclaro, mommsen1894 l.20238-20244, under Mommsen's "585?".
- **The conversion (l.5).** Isidore, On Famous Men 35 (PL83 l.122417-122421) and History of the Sueves 91 (l.120280-120284).
- **The council (l.7).** Hispana l.56912 and 56943-56950.
- **The sermon (l.9).** Polemius and the sermon: caspari1883 l.3700-3712, and Polemius signs Braga II as bishop of Astorga (Hispana l.57276, Caspari's note l.3724-3726). The candles at stones, trees, springs and crossroads: caspari1883 l.4881-4887.
- **The death (l.11).** Gregory's "hoc tempore … magnum populo illi faciens planctum" (l.18175-18176). The 580 is the Bollandists' (acta-sanctorum martii-3 l.30876-30878) and Caspari's (caspari1883 l.288-289, "im fünften Jahre Childeberts des Zweiten oder im Jahre 580"; l.717).
- **The epitaph (l.13).** PL72 l.3435-3440. That Martin wrote it himself is Caspari's ("hat sich selbst ein Epitaph in Versen gesetzt", l.718-719) and the Bollandists' ("quod ipse sibimet composuit", l.31521). "The same in name but not in merit" carries the source's own contrast ("eodem Nomine, non merito"). It is not narrator rhetoric, so it passes.

#### Findings

- **C-B1 BLOCKING (brief l.3 to l.11; items 10, 4; the who-line has no time).** The Pattern's Order rule asks for "who they were, with time and place" right after the scene. The brief gives a place but no time at all until l.11 ("580"), near the end. A listener does not learn the century of the conversion, the council or the sermon until the death paragraph. Held anchors exist: Caspari's "Um 550" for his coming (caspari1883 l.261), and Braga II "im Jahre 572" (Caspari's note, l.3725-3726; the Bollandists' "Era DCX, sive anno Christi DLXXII", acta-sanctorum martii-3 l.31097). Fix: replace l.3 with: "The newcomer was Martin of Braga, a bishop among the Sueves, a people settled in Spain. C. P. Caspari, who edited his sermon, reckons he came there about 550. Isidore of Seville calls him bishop of the monastery of Dumio, which Caspari places near Braga. He was later bishop of Braga itself. Gregory says he had gone East to visit the holy places, and was held second to none in learning in his time." This also takes in C-M2, C-M3 and C-M4. Dalton supplies "the Suevi settled in Spain" (dalton1927 l.26871-26872), and Caspari puts Dumio "in der nächsten Nähe von Bracara" (l.450).
- **C-B2 BLOCKING (card `uncertain` 3 and the Gregory `sources.about` entry; records claim "Note in Krusch's Gregory to HF V.37"; items 1, 5; the wrong editor named).** The card says "a note printed in Krusch's edition also says about twenty". The source entry calls the History of the Franks V.37 "with Bruno Krusch's notes". The MGH History of the Franks is Wilhelm Arndt's edition, and Krusch edited the Miracula (contents, arndt-krusch1885 l.138 and 140). The note "non 30, sed 20 circiter annis" is in Arndt's History and is signed "R." (l.18215-18217, "… V. AA. SS. Ord. Bened. I, p. 257. R."). Krusch's own year, "Obiit a. 580", is in his VM note (l.46065), and that one is correctly given. Fix for `uncertain` 3, second sentence: "The Bollandists hold that a copyist put thirty for about twenty, and a note signed R. in Wilhelm Arndt's edition of the History also says about twenty." Fix for the source title: "History of the Franks V.37, ed. Wilhelm Arndt, and The Virtues of Saint Martin I.11, ed. Bruno Krusch, with their notes, in MGH Scriptores rerum Merovingicarum 1". Fix the records claim to: "Note signed 'R.' in Arndt's HF V.37 (arndt-krusch1885 l.18215-18217)".
- **C-M1 MINOR (brief l.1; items 10, 12; the miracle story is not marked).** Only the first sentence carries "Gregory of Tours writes". "The king's son was healed" is then told in the narrator's voice. The card's `uncertain` 1 rightly says the account "is a miracle story, in a book of the miracles of Martin of Tours", but the brief never says so, so the card's caveat is not the brief's own. Fix: replace l.1 with: "Chararic, a king in Galicia, had a gravely ill son, Gregory of Tours writes in a book of the miracles of Martin of Tours. The king sent to Martin's tomb for relics. A man named Martin, from a far country, came into a Galician port with them. The son was healed, and the king confessed the unity of Father, Son and Holy Spirit."
- **C-M2 MINOR (brief l.3; item 4; a statement out of place and out of time).** "The Sueves kept their own kingdom in Galicia until the Gothic king Leovigild made it a province of the Goths, John of Biclaro says." This event comes under a year Mommsen marks "585?", after Martin's death, but it sits before the conversion. Nothing ties it to Martin, so a listener can take it as background to his arrival. The card already carries it (`uncertain` 7). Fix: delete the sentence from the brief. The C-B1 wording replaces its one useful job, saying who the Sueves were.
- **C-M3 MINOR (brief l.3; item 1; a qualifier dropped).** "Was held second to none in learning" leaves out Gregory's "suis temporibus" ("in his time", l.18177; Dalton "among the men of his day", l.9928). The card keeps it. Fix: "… and was held second to none in learning in his time." This is folded into C-B1.
- **C-M4 MINOR (brief l.3; item 4; a term with no context).** A listener hears "bishop of the monastery of Dumio" and "Galicia" with no hint of where they are. Galicia is easily heard as the Galicia of eastern Europe. Fix: as in C-B1.
- **C-M5 MINOR (brief l.7; item 1; Martin's "we" turned into "they").** "They should correct whatever in themselves was at fault." Martin includes himself: "si quid … reprehensibile invenitur in nobis … corrigamus" (Hispana l.56945-56947). Fix: "The faith was in no doubt in this province, he told the bishops, so they should correct their own faults, his among them, by the Scriptures and the old canons."
- **C-M6 MINOR (card `uncertain` 6; item 7; a difference shown as a dispute).** The card sets the Bollandists' "church of Martin of Tours built by King Theudemir" against Caspari's "built by Chararic". But the Bollandists hold that Theudemir is the king Gregory calls Chararic (acta-sanctorum martii-3 l.30887-30889, in the card's own `uncertain` 2). So both put the epitaph in the same church, and they differ only on the king's name. Fix: "Where his epitaph stood. Caspari says it was to stand in the church of Saint Martin built by Chararic. The Bollandists say the same church was built by Theudemir, whom they take to be Gregory's Chararic."
- **C-M7 MINOR (card `place`; item 7; one side of the Dumio site).** "The monastery of Dumio, which C. P. Caspari places near Braga" is attributed, but a held note puts it elsewhere: "primo Dumiensis monasterii (Mondonedo)" (arndt-krusch1885 l.18215, signed R.). Fix: "… the monastery of Dumio, which C. P. Caspari places near Braga, while a note signed R. in Arndt's edition of Gregory glosses it as Mondonedo; Braga". Add the note to the records.
- **C-M8 MINOR (card `dates`; item 8; a namesake king).** "King Childebert's fifth year." There are two Frankish kings Childebert, and the place does not tell them apart. Caspari says "Childeberts des Zweiten" (caspari1883 l.288-289), and the Bollandists say "Childeberti Regis Austrasiorum Francorum" (l.30856-30857). Fix: "… among the events of the fifth year of King Childebert II of the Franks, which C. P. Caspari and the Bollandists reckon as 580 …". In the same field, "Spanish era 610" is undefined. Add: ", which the Bollandists give as 572".
- **C-M9 MINOR (brief l.11; items 4, 8; witnesses named but not placed).** "C. P. Caspari and the Bollandists" have had no introduction. With C-B1, Caspari is introduced at l.3. Fix for l.11: "Gregory places his death among events that Caspari and the Bollandist editors date to 580. His people mourned him greatly, Gregory says."
- **C-M10 MINOR (card `sources.ownWords` and the dates; item 12).** (a) Only Martin's signature represents him in the Braga I acts, so they are not "his own words". Fix the ownWords title to "Acts of the Second Council of Braga, with his speeches, and the Chapters of Martin, in Collectio canonum Ecclesiae Hispanae", and add Braga I to the Hispana entry under `about`. (b) The PL83 and Hispana entries lack dates their file headers give (Paris, Migne, 1860; Madrid, 1808). Add `"date": "1860"` and `"date": "1808"`. (c) `legacy.traces` 4 says "an English homily of Abbot Aelfric". Caspari has "angelsächsischen" (l.181), so read "an Old English homily of Abbot Aelfric".
- **C-M11 MINOR (card; item 4; long sentences).** These sentences run past about 25 words: `uncertain` 1's first sentence (39 words), `uncertain` 5's third (31), `uncertain` 7 (34), `legacy.remembered` 1 (31) and 2's first (32), and `legacy.traces` 1's first (29). Fix: split each at its natural joint. For example, `uncertain` 1 becomes: "His life rests on writers of his own time or soon after. Gregory of Tours tells of his coming while Martin was still bishop in Galicia. Venantius Fortunatus wrote to him. Isidore of Seville wrote later."

After the fixes: about 346 words (2:08), FK 7.6, Flesch 66.1 (scratch copy scored). This is a little past 2 minutes. If the drafter wants it nearer 2:00, deleting "He also founded monasteries." (it is on the card) brings it to about 342 words.

---

### Brendan of Clonfert

The coordinator's ruling is met. The brief stands on Adomnan for the man, and it says plainly that "Most of what is told of Brendan of Clonfert comes from Lives written centuries later". It gives Stokes's later-1400s date for the Book of Lismore and Rees's about-twelfth-century date for his Lives. `uncertain` 1 repeats both. The voyage is told only inside "In that Life".

| # | Item | Result |
|---|---|---|
| 1 | Sources establish each sentence | PASS (below). Card: C-M17, C-M18, C-M19, C-M20. |
| 2 | Quotes verbatim | PASS. There are no quotation marks. The records' English quotes match huyshe1905 l.3933-3937 and 10229-10251, stokes lismore1890 l.21207-21225, 21301, 21466-21467, 21680-21702 and 21815-21817, rees1853 l.25214-25221 and 25381-25386, williams1899 l.23790-23815 and 24027-24034, and Mirk l.4583-4602 (OCR). |
| 3 | No invention | PASS. |
| 4 | Writing | FAIL (minor): C-M12, C-M13, C-M14. |
| 5 | Named witnesses | PASS. |
| 6 | Partisan witness | n/a. The Lives are marked late. |
| 7 | Disputes both sides | PASS in the brief (Huyshe's identification is given as his). Card: C-M15. |
| 8 | Common names | FAIL (minor): C-M12 (Adomnan in both texts). Columba of Iona, Brendan of Clonfert and Brendan of Birr are placed. |
| 9 | One term | FAIL (minor): C-M13 (Brendan and Brenainn). |
| 10 | Story, scene, length | PASS. It opens on the Hinba scene, and the length is about 2 minutes. |
| 11 | Readability | PASS. |
| 12 | Card order, caveat repeated | PASS. |
| 13 | Audio tags | PASS. |
| 14 | Who test | PASS on the coordinator's ruling (a founder, carried by Adomnan, Supplement scan answer 3). |

Brief sentences checked against their sources:
- **The scene (l.1).** huyshe1905 l.10229-10251: four founders, Hinba, Mass at their request, the globe of fire rising like a pillar, Brendan telling Comgell and Cainnech.
- **Huyshe's identification and years (l.3).** The note at l.10277-10282. "Once more": I.26, l.3933-3937, "as is said". Huyshe names no source for the years (l.10281; intro l.1481).
- **Brendan of Birr (l.5).** Adomnan III.3, l.9318-9345, and Huyshe's note at l.9370-9375. The Welsh annals entry is "Brendan Byror dormitatio" (annales-cambriae l.2501), the only Brendan entry in the file.
- **The Lismore Life (l.7).** Stokes on the compiling, l.218-219. The angel and the Land of Promise, l.21466-21467. Five years at sea, l.21519. Easter on the whale, l.21533-21534. The devil reveals the gate of hell, l.21569. Ita is "his foster-mother" (l.21681), and "those dead stained skins", "a holy consecrated land" are at l.21685-21686. The great vessel built in Connaught is at l.21695-21697, and reaching the land at l.21815-21817.
- **Rees's Latin Life (l.9).** "Triumque millium fere monachorum pater" (rees1853 l.11370) and "The Manuscript here ends abruptly" (l.25386). Rees's dating of the Lives is at l.321-323.
- **The close (l.11).** stokes lismore1890 l.21219-21222.

#### Findings

- **C-M12 MINOR (brief l.1 and l.3; card `knownFor`; items 8, 4; Adomnan unplaced at first mention, with no date).** At first mention the brief has "Adomnan writes", and his identity comes a sentence later as "a later abbot of Iona". The card's `knownFor` has a bare "Adomnan". "Later" does not tell the listener what the coordinator's ruling rests on: Adomnan is the witness from near Brendan's time. Huyshe's title page gives "ninth abbot of the monastery of Iona", "a.d. 679-704" (huyshe1905 l.87-88), and Columba's years are "A.D. 521-597" (l.1). Fix for brief l.1: "… Adomnan of Iona writes." Fix for l.3, first two sentences: "Adomnan was abbot of Iona about a century later, from 679 to 704, his translator Wentworth Huyshe says. Huyshe takes this Brendan to be Brendan of Clonfert, founder of that Irish monastery." Fix for the card's `knownFor`: "… whom Adomnan of Iona names as Brendan Mocu Alti …".
- **C-M13 MINOR (brief l.7 and l.11; item 9; two names for one man).** The brief switches from "Brendan" to "Brenainn" for the retold Life ("an angel promises Brenainn", "Brenainn will raise"). A listener can hear a second person. The name form is given once ("calls him Brenainn son of Finnlug"), which is enough. Fix: keep that sentence, and read "an angel promises Brendan the Land of Promise" and "Brendan will raise his monks and households …".
- **C-M14 MINOR (brief l.5 and l.11; item 4).** (a) "The Welsh annals record the death of Brendan of Birr, and say nothing of Brendan of Clonfert" is a context-free absence that adds nothing to the life. It also tells the editor's identification of "Byror" with Birr (Williams ab Ithel, l.892, "Brenda, abbot of Birre") as the annal's own. The card's `uncertain` 4 already carries it. Fix: delete the sentence from the brief, leaving l.5 as its first sentence. (b) "The fire of Doom" keeps Stokes's archaic English, and a listener will not know "Doom" means the Last Judgment. Fix: "… over the fire of Judgment Day."
- **C-M15 MINOR (card `uncertain` 2; records `contested_claims` 1; item 7; the identification rests on more than Huyshe).** The card names only Huyshe as joining Brendan Mocu Alti to Clonfert. The records' side "Late Lives … without naming Adomnan" misses a held link: the Book of Lismore story has "Brenainn maccu Altai … in Clonfert" (stokes lismore1890 l.878-879), and the card itself cites that story under `traces` 3. Hugh Williams also writes "Brendan, who founded Clonfert" (williams1899 l.9111). Fix: after "and Mocu Alti to be his clan name." add "A late Lismore story joins the two, setting Brenainn maccu Altai at Clonfert." Add the Lismore line to the records' sides.
- **C-M16 MINOR (card `uncertain` 6; item 1; a death date read as a feast).** O'Flaherty, as O'Donovan quotes him, writes "Enaghdun, dedicated to St. Brendan, the 16th of May, Anno Christi 577, there deceased" (odonovan1856 l.4248-4250). The 16 May is his death day there, not a feast. A held calendar does give the feast: the York prymer has "brandani episcopi" on 16 May (Surtees l.4186). "The seventh of the calends of June" is left unexplained for a general reader. Fix: "His feast. Huyshe gives his day as 16 May, and the calendar of the York prymer keeps Brandan, bishop, on that day; O'Flaherty, as O'Donovan quotes him, says he died on the 16th of May. The Lismore Life, in Whitley Stokes's English, places his festival on the seventh of the calends of June, which is 26 May." Add the prymer file to `sources.about`.
- **C-M17 MINOR (card `legacy.remembered` 3; item 1; a partial list told as the list).** "Likens him to Abraham, David, Moses and Noah." The Life runs through Abraham, David, Solomon, Moses, a prophet, Augustine, Origen, John, Matthew, Paul, Peter, John the Baptist and Gregory of Rome, and ends with Noah (l.21208-21219). Four names told as the comparison misreport it. Fix: "The Lismore Life likens him to a long line of saints and patriarchs, from Abraham to Gregory of Rome, and last to Noah. As Noah raised the ark …".
- **C-M18 MINOR (card `uncertain` 7; items 1, 4; the wrong scope and an X-but-Y).** "The saints there, he says, were not Cambro-British, but natives of Ireland who had passed much of their time in Wales." Rees says this only of "the three latter, those of St. Aidus, St. Brendanus, and St. Tathan". The appendix also holds Catharine and Margaret, whom he ties to Wales by Welsh churches (rees1853 l.454-465). Fix: "Rees says he put this Life in his appendix with those of Aidus and Tathan, saints who were natives of Ireland and had passed much of their time in Wales."
- **C-M19 MINOR (card `legacy.traces` 1; item 1; "from" implies a beginning).** "Name bishops of 'Clonfert-Brendan' from the 1170s on." The held volume begins in 1172 ("THE AGE OF CHRIST, 1173", l.760), so the 1170s is where the held volume starts, not where the bishops start. Fix: "The Annals of the Four Masters, in John O'Donovan's English, name bishops of \"Clonfert-Brendan\" in the volume held here, which begins in 1172."
- **C-M20 MINOR (card `legacy.remembered` 4; item 1; a file header's year told bare).** "An English preacher active about 1403" rests only on the Library file header (mirk erbe1905 l.2). I found no source line giving it. Fix: "John Mirk, an English preacher, tells in a sermon for the feast of Matthias …".
- **C-M21 MINOR (card; item 4; long sentences).** `remembered` 4 runs to 36 words, `uncertain` 5's second sentence to 31, and `uncertain` 1's third sentence to 29. Fix: split each, for example "Whitley Stokes says the Book of Lismore was compiled in the later 1400s. He calls its language mixed, with Old Irish forms beside late Middle and even Modern ones."
- **Note, not a finding (records).** The `absent_details` entry on the Navigatio is correct as worded. Huyshe does mention "the narrative of the voyage of St. Brendan" in a note (huyshe1905 l.5470-5471). The records could add that so the absence stays exact.

After the fixes: about 328 words (2:02), FK 6.6, Flesch 73.8 (scratch copy scored).

#### Verdicts

- Martin of Braga: NOT CLEAR (2 blocking, 11 minor).
- Brendan of Clonfert: CLEAR (0 blocking, 10 minor). The minor fixes should still be applied.

---

## R1 review, part D: Barhadbeshabba 'Arbaia, bishop of Halwan (era 3 Who batch 8)

Reviewer: independent Opus, first sight of these drafts. I did not edit any profile file, made no git, web or paid calls, and used local scripts only.

### Method

Bar: `Who_Profile_Pattern.md`, checklist items 1 to 14; `CLAUDE.md`, "Trust and source fidelity" and "Accessible and rigorous"; the batch 6 R1 format; recorder length at most about 325 words. Read: `barhadbeshabba-arbaya.brief.txt`, `.card.json`, `audio/barhadbeshabba-arbaya.audio.txt` and the scratchpad records (32 claims, 5 contested claims, 4 absent details). I opened every cited line in Chabot 1902 (l.31386-31432, 31470-31490, 31910-31935, 48154), Scher's PO 4 (l.16780-16792, 16875-16895, 16925-17172, 20730-20750, 20820-20830, 21000-21125, 21720-21728), Seert PO 13 (l.28655-28780, 29176-29183), Nau's PO 9 (l.31550-31610 and the file header), Connolly 1909 (l.268-316, 4485-4525), Guidi 1903 (l.1950-1980), Labourt 1904 (l.12678-12704), and Assemani BO III.1 (l.30768-30876) and III.2 (l.49910-49917). I checked the approved cards that touch this man: batch 1 `narsai` and `barsauma-of-nisibis`, and batch 5 `henana-of-adiabene`. The coordinator's ruling was the test: the History goes to Barhadbeshabba 'Arbaia of the school of Nisibis, the Cause to the bishop of Halwan, and Nau's view that they may be one man is told as his.

Quotes re-checked: Connolly's "Edessa was darkened, but Nisibis shone forth ; and the dominions of the Romans were filled with error, but those of Persia with the knowledge of true religion" (connolly1909 l.4494-4496) matches the brief word for word. The only change is the closed space before the semicolon. The audio equals the brief once `[calmly] ` (start) and `[warmly] ` (closing paragraph) are removed (checked by `diff`). Brief: 328 words (2:01), FK 7.2, Flesch 68.7.

### Barhadbeshabba 'Arbaia, bishop of Halwan

1. Sources establish the sentences: **FAIL** (D-B2, D-B3; D-M4). Most sentences check. The synod scene, signature no. 27 and "Holwan", the king's beasts, Gregory "originaire de Pherat", Scher's identification (scher1908 l.16973-16975), the title "ÉVÊQUE DE HALWAN" (l.17169-17170), Henana praised and prayed for (l.21006-21121), Scher's note on hiding the truth (l.21073-21075), Nau's attribution and his "pas impossible" (po09 l.31557-31607) and Guidi's "Nominis famam adeptus erat in libris conscribendis Bàr Hadhbésabba urbis Holwan" (guidi1903 l.1975-1976) all hold. "Khosrau the Second" is inferred from the king's fifteenth year in 605. It is sound and needs no finding.
2. Quotes verbatim: PASS.
3. Nothing invented: PASS.
4. Writing: **FAIL** (D-M2, D-M3, D-M6). There are no "X, not Y" contrasts, colon reveals or rhetorical questions in the brief. The faults are one spliced 24-word sentence, a 26-word sentence, the undefined "epithet", the run-on card fields, and the "also survives" lead-in.
5. Named witnesses: PASS. Chabot, Scher, Nau, Guidi and Connolly are all named.
6. Partisan witnesses: PASS. Seert is not used for doctrine here.
7. Contested claims both sides: **FAIL** (D-B1, D-B2). Nau's view is told as his in the brief, which follows the ruling. The card, though, files the History and its legacy under this man, and the brief gives the Seert identification without its owner.
8. Common names and namesakes: **FAIL** (D-B4; D-M5).
9. One term: PASS. "Head" is used for the catholicos in both places, and Halwan and Holwan are explained on the card.
10. Story, scene, length: **MINOR** (D-M1). It opens on a sourced scene. At 328 words it runs past the recorder cap of about 325, and the walk-out is told without the event behind it (D-B2).
11. Readability: PASS (FK 7.2, Flesch 68.7).
12. Card order and caveat: PASS on order. The brief's caveat (Scher and Nau's identification) opens `uncertain` 1. No field is empty. Source grouping fails (D-B1, D-M4).
13. Audio tags: PASS.
14. Who test: PASS. A recorder whose Cause is the first history of the school of Nisibis (scher1908 l.16890-16892).

Consistency with the approved cards. Batch 1 credits the History to "Barhadbeshabba 'Arbaia" and the Cause to "Barhadbeshabba 'Arbaia, bishop of Halwan" (`narsai.card.json` sources; `barsauma-of-nisibis.card.json` l.25, 50-61). `narsai.card.json` `uncertain` 1 gives Nau's "not impossible that they are one man" as Nau's. Batch 5 has the Cause's author as Henana's pupil, and says "Scher says Barhadbeshabba was among" the walkers-out (`henana-of-adiabene.card.json` l.37). This draft's brief agrees on the History, which it gives to Nau. It disagrees in four places: the card's `keyWorks`, `ownWords` and `legacy`, which file the History under this man (D-B1); the brief's Seert line, which drops the "Scher says" that batch 5 carries (D-B2); and the display name, which is the one batch 1 uses for the History's writer (D-B4).

#### Findings

- **D-B1 BLOCKING (card `keyWorks` 2, `legacy.traces` 3, `legacy.remembered` 3, `sources.ownWords` 3; items 1, 7, 12; the other man's work filed as this man's).** The card lists the History as this bishop's key work, puts it in "Their own words" with author "Barhadbeshabba 'Arbaia", and gives Nau's praise of it ("the oldest church history of the Church of the East ... the source of the Syriac legend of Nestorius") as a trace of this man. Under the ruling and in batch 1, the History belongs to the priest of the school of Nisibis. Nau ties it to the bishop only as "pas impossible" (po09 l.31601-31602). A caveat inside a title does not undo the grouping: a page reads `keyWorks`, `ownWords` and `legacy` as his. `remembered` 3 does the same with Abdisho's list. Nau gives that list to the History's writer ("Il semble donc identique a Barhadbesabba 'Arbaia ... mentionne par Ebedjesu", l.31558-31561), and Scher gives it to the Cause's author (scher1908 l.16980-16984). The card tells it as this man's with no owner. Fix: (a) Delete `keyWorks` 2. (b) Delete `sources.ownWords` 3. Nau's introduction stays in `about`, which already lists the same file. (c) Delete `legacy.traces` 3. (d) Replace `legacy.remembered` 3 with: "Abdisho of Nisibis lists books of a Barhadbeshabba 'Arbaia: the Treasures in three volumes, controversies against all sects, a church history, a work on the followers of Diodore, and a commentary on Mark and the Psalms. Addai Scher gives the list to the Cause's author, and François Nau to the History's writer." (e) In the brief, para 6, replace "Part of a history of the holy Fathers persecuted for the truth also survives." with "Part of a history of the holy Fathers persecuted for the truth survives from the same school." The rest of para 6 stands.

- **D-B2 BLOCKING (brief para 4, l.7, and audio; items 1, 7, 10; an identification given without its owner, and a walk-out with no event behind it).** "The Chronicle of Seert names a Hadbeshabba 'Arbaya among the students who walked out of the school in protest. It says he was later made metropolitan of Halwan." The chronicle names "Hadbsabba 'Arbaya", a different spelling (seert l.28720-28721). The man becomes Barhadbeshabba only by Scher's note, "Ou plutot Barhadbsabba" (l.28731), and his note tying the man to the 605 synod (l.28774). The brief gives the line with no owner, right after the Cause's praise of Henana, so the listener takes it as fact about this man. Batch 5's card says "Scher says". "In protest" also leaves out what the protest was about. The students left over Sabrisho's choice, "qui avait repousse la parole du metropolitain pour accepter celle de Hnana" (l.28672-28673), so they walked out against the master the Cause praises. That is the point of Scher's puzzle (scher1908 l.17025-17028). Fix: replace the two sentences with: "The Chronicle of Seert says some three hundred students walked out of the school when the head of the church took Henana's side. It names among them a Hadbeshabba 'Arbaya, later made metropolitan of Halwan. Scher takes him for the Cause's author." ("environ trois cents", l.28707.)

- **D-B3 BLOCKING (card `place`; item 1; the place rests on a volume the card does not cite, and the cited volume says something else).** "a place Joseph Assemani puts in the diocese of Nisibis". "oppidum in dioecesi Nisibena" is in BO III.2 (tomus3-pars2 1728 l.49913), which is not in the card's sources. The volume the card does cite, BO III.1, says "pago apud Nisibin", a village near Nisibis (l.30868-30869). Fix: "Beth 'Arbaye by origin, by his second name, Addai Scher says; Joseph Assemani puts it near Nisibis. The school of Nisibis, in the Persian empire. Halwan, spelled Holwan in the synod's acts, as bishop". (Or keep "in the diocese of Nisibis" and add BO III.2 to `about`.)

- **D-B4 BLOCKING (card `name`; items 8, 14 and Naming, "Namesakes"; the display name merges two men).** The card's `name` is "Barhadbeshabba 'Arbaia". That is the exact form batch 1 uses for the History's writer (`narsai.card.json` sources author; `narsai.brief.txt` l.1; `barsauma-of-nisibis.brief.txt` l.9). Batch 1 marks this man as "Barhadbeshabba 'Arbaia, bishop of Halwan". With this name, a tree link or listener would take Narsai's biographer to be this bishop, which is the merge the ruling forbids. Under Naming, a namesake carries the place where the name is not enough. Fix: `name`: "Barhadbeshabba 'Arbaia of Halwan". Keep "Barhadbeshabba 'Arbaia, bishop of Halwan" first in `otherNames`. The id can stay, since it is not yet live.

- **D-M1 MINOR (brief; item 10; length).** 328 words, past the recorder cap of about 325. The fixes above add words. Fix: delete para 7 ("A chronicle that Ignazio Guidi edited says that after Gregory's death, Bar Hadbeshabba of Halwan won fame for writing books."). The card keeps it (`legacy.remembered` 1, `uncertain` 8). It also carries an identification of its own, of a man "of Halwan" with this bishop. Also in para 3, "from Adam down to the schools" becomes "from Adam to the schools".

- **D-M2 MINOR (brief para 2; item 4; a spliced sentence, an undefined term, and a pronoun that can point to Scher).** "His epithet marks him as a man of Beth 'Arbaye, Scher says, and he studied at the school of Nisibis under Henana of Adiabene." This is 24 words and two ideas, and "epithet" is not a B2 word. Fix: "Scher says his second name marks him as a man of Beth 'Arbaye, and that he studied at Nisibis under Henana of Adiabene." Also "The title Scher prints calls its author bishop of Halwan." becomes "The title Scher prints calls him bishop of Halwan."

- **D-M3 MINOR (brief para 4; item 4; a 26-word sentence with two claims).** "Scher says Henana's own church always charged him with leaving Theodore of Mopsuestia's reading of Scripture, and thinks the author probably hid this to praise him." Fix: "Scher thinks the author probably hid the truth to praise him. Henana's own church, Scher says, always charged him with leaving Theodore of Mopsuestia's reading of Scripture." ("Il est probable que l'auteur dissimule ici la vérité pour louer son maitre ... les Nestoriens ont toujours accusé Hnana", scher1908 l.21073-21075.)

- **D-M4 MINOR (card `sources`; items 1, 12; witnesses named on the card but not listed).** `uncertain` 9 names Mari ibn Sulayman (gismondi1899 l.13591-13592) and Ishoyahb III's letters (duval1905 l.5517, 11494). Neither is in `about`. Fix: add `{"title": "Commentaries on the Patriarchs of the Nestorians (Latin version by Henricus Gismondi)", "language": "Latin translation", "date": "1899", "file": "cic/texts/mari-ibn-sulayman_de-patriarchis-nestorianorum-commentaria-pars-prior-ara-lat_gismondi1899.txt"}` and `{"title": "Letters of Ishoyahb III (Latin version by Rubens Duval)", "language": "Latin translation", "date": "1905", "file": "cic/texts/ishoyahb-iii_liber-epistularum-versio-lat_duval-csco1905.txt"}`. Take the exact titles and authors from the files' headers.

- **D-M5 MINOR (card `uncertain` 9; item 8; a common name with no identifier).** "whom Sabrisho wanted as his successor". Several Church of the East heads bear this name. Fix: "whom Sabrisho of Lashom, head of the church, wanted as his successor" ("Sabriso de Lasom (+ 604)", scher1908 note 5, l.16953).

- **D-M6 MINOR (card `uncertain` 4, `dates`; item 4; a garbled appositive, an emended reading told as the witness's, a missing period).** (a) `uncertain` 4, "Nau gives the History to Barhadbeshabba 'Arbaia, priest and head of the overseers of the school of Nisibis by its title, the writer Abdisho of Nisibis lists." does not parse. Fix for the whole item: "The History and the Cause. The History's title calls its writer a priest and head of the overseers of the school of Nisibis. François Nau takes him to be the Barhadbeshabba 'Arbaia whose books Abdisho of Nisibis lists. He thinks it not impossible that this man is also the bishop of Halwan, who would then have written the History young and the Cause in old age. Scher treats them as one, giving the Cause's author Abdisho's list of books, and notes that the list does not name the Cause." (b) `dates` ends "Scher thinks he probably died in the first half of the seventh century" with no period. The scan reads "dans la première moitié du vi siè-cle" (scher1908 l.16976-16977). "Seventh" is the drafter's sound emendation from the next clause, but it is not a reading of Scher's text, and the field already gives 605 and the 609-628 vacancy. Fix: delete that last sentence and end the field with "... which François Nau and Scher give as 609 to 628."

After the fixes, the brief reads (the fixes applied, nothing else changed; the audio takes the same text with its two tags):

> The bishops of the Church of the East met at the Persian king's court to choose a new head. J.-B. Chabot, who edited their acts, dates the meeting to April 605. The acts say King Khosrau the Second had the distant bishops brought on his own beasts. They chose Gregory of Prat. The twenty-seventh to sign is Bar Hadbeshabba, bishop of Halwan.
>
> Addai Scher and François Nau take this bishop to be Barhadbeshabba 'Arbaia, who wrote the Cause of the Foundation of the Schools. The title Scher prints calls him bishop of Halwan. Scher says his second name marks him as a man of Beth 'Arbaye, and that he studied at Nisibis under Henana of Adiabene.
>
> The Cause tells of the schools through which God taught angels and people, from Adam to the schools of Edessa and Nisibis.
>
> The Cause speaks of Henana as a living master. It praises his humility and prays that God will lengthen his days. Scher thinks the author probably hid the truth to praise him. Henana's own church, Scher says, always charged him with leaving Theodore of Mopsuestia's reading of Scripture.
>
> The Chronicle of Seert says some three hundred students walked out of the school when the head of the church took Henana's side. It names among them a Hadbeshabba 'Arbaya, later made metropolitan of Halwan. Scher takes him for the Cause's author.
>
> Part of a history of the holy Fathers persecuted for the truth survives from the same school. Nau gives it to Barhadbeshabba 'Arbaia, a priest of the school of Nisibis, and dates it to the end of the 500s. He thinks it not impossible that this writer is the bishop of Halwan.
>
> Of the school that Narsai of Nisibis founded, the Cause says, in R. H. Connolly's English, "Edessa was darkened, but Nisibis shone forth; and the dominions of the Romans were filled with error, but those of Persia with the knowledge of true religion".

After the fixes: 323 words, 1:59, FK 6.5, Flesch 72.3 (measured with `grade_text` on the text above). `briefLength` "about 2 minutes" stands.

#### Verdicts
- Barhadbeshabba 'Arbaia, bishop of Halwan: NOT CLEAR (4 blocking, 6 minor).

---

## R1 review, part E: Theopistus (era 3 Who batch 8)

Reviewer: independent Opus, first sight of this draft. I reviewed it against the coordinator's ruling. He is a recorder, at the length the Library carries (about 1 to 1:30 expected). Nau's view of a post-512 reworking in the school of Peter the Iberian sits at the center, with a contested_claim on authorship. The narrator's account is told as the book's account, never as settled fact. I also checked it against the approved Dioscorus of Alexandria profile (`Who-Profiles/era3/batch1/`).

### Method
I read `CLAUDE.md`, the Who Profile Pattern and its 14-item checklist, the batch 6 README form, and the brief, card, audio and `records/theopistus.json`. I re-opened every cited line in `cic/texts/theopistus_histoire-de-dioscore-journal-asiatique-1903-fra_nau1903.txt`:
- the introduction: l.176-180, 364-369, 415-487, 493-534, 544-595, 636-647, 712-718, 739-742, 798-809, 877-883, 926-933;
- the translation: title l.13482-13500, §4 l.13915-13982, §6 l.14225-14251, §10 l.15200-15240, §11 l.15330-15352 and 15582, §14 l.16040-16074, §16 l.16395, §19-20 l.16865-16930 and 17010-17063;
- the London ending, l.17070-17105, and the Crum note, l.17171-17178.

I also checked the other witnesses:
- `po08` l.430-482;
- the PO 13 file l.12185-12212 and 12632-12642;
- Duchesne tome 3 l.15895-15908 and 17628-17633;
- Evetts l.35100-35109;
- the Basset synaxary l.14419-14438;
- Budge's Ethiopic synaxary v1 l.7420-7440;
- Budge 1913 l.1923-1974.

All quotes hold verbatim (OCR aside). To test the absences, I grepped all of `cic/texts/` for `th[ée]opist`, `Theopistos`, `θεόπιστ` and `ΘΕΟΠΙΣΤ`, and opened every file that hit. The ones the records do not list are only namesakes: Assemani BO 3.1, Cyril of Scythopolis, Mansi 14, Budge 1915, the Ethiopic synaxary v2-4, Nikodemos, PO 11 and PO 16 (Theopiste/Theopista, the martyr Theopistus). I ran `grade_text` on the draft and on a fixed text. The audio was diffed against the brief.

### Theopistus

1. Sources: mostly pass. Every sentence has a line. Two sentences claim more than their line (B2, M1), and one card field misplaces a reading (M4).
2. Quotes: pass. Assemani's "Fabulosa narratio a jacobitis recentioribus excogitata" (l.503-504), Nau's "panégyrique ... quelques faits servent de cadre à des visions, à des discours et à des prodiges" (l.640-643), the Macarius title (l.807-808), Duchesne's "apocryphe et de nulle valeur" (l.15906-15907), "Je témoigne devant Dieu que j'ai écrit la vérité" (l.17052) and the Evetts line (l.35106-35107) all match.
3. Nothing invented: pass.
4. Writing: fail (B1, M2, M3). The brief is clean of contrasts, colons, dashes and aphorisms, and the sentences stay under 25 words. But it leaves the listener without its two anchors: which council, and which death. One "He" points the wrong way.
5. Named witnesses: pass. Nau, Assemani, Duchesne, Amélineau, Revillout, Crum and Budge are each named.
6. Partisan witness: pass. The book is placed as the narrator's own account. The card has Nau call it a panegyric.
7. Contested: fail on one sentence (B2). The authorship dispute itself is laid out well. The book's claim sits against Nau's reworking, with "he suggests" and "he thinks" kept, and the card gives Assemani's side and Nau's answer. But one sentence tells the book's account of its own writing as fact.
8. Common names: pass. "Dioscorus of Alexandria" and "Theopistus, a disciple of Dioscorus" are named at first mention. "Severus" is tied to Antioch, Peter has his epithet, and "the archdeacon Peter" is fixed by his role. The card's knownFor gives "Dioscorus of Alexandria".
9. One term: minor fail (M5). Nau's tentative view is "he suggests" in the brief but "he holds" in the card.
10. Story: pass. It opens on a sourced scene and tells the dispute in place, at 259 words, 1:36.
11. Readability: pass, FK 7.39 and Flesch 70.78.
12. Card: fail on one item (B3). The order is right and no field is empty. The caveat opens `uncertain`. But `uncertain` item 5 states a false absence.
13. Audio: pass. The only differences from the brief are `[calmly] ` at the start and `[warmly] ` before the one-line closing paragraph.
14. List line and Who basis: pass. He is a recorder whose History is, in Nau's words, the only early writing given over to Dioscorus.

Consistency with the approved Dioscorus of Alexandria profile: pass.
- Both use "The Church of Alexandria and Miaphysite Egypt" and "François Nau".
- Both have Nau give 454 and the History give the fourth of Elul, or September, for the death.
- Both report Nau's date for the present form, after 512, and Assemani's charge of fiction.
- The Evetts line on no biography after the banishment agrees, and this card renders it closer to verbatim.
- The Dioscorus card's "Gangra in Paphlagonia" is not contradicted, though this card omits Paphlagonia (M4).

One point for the coordinator, outside this profile's text. The Dioscorus `records.json` absent-detail note calls Theopistus's legend "the only held account of the exile". This card's own `uncertain` item 5 cites the Basset Arabic and Budge Ethiopic synaxaries, which tell of the exile with Macarius (Basset l.14421-14437; Budge v1 l.7429-7431). That approved record note is a false "only". It is record text, not participant text, so I flag it here and do not count it as a finding on Theopistus.

#### Findings

- **E-B1 BLOCKING (brief, paragraphs 2-4; item 4; statements with no context).** Paragraph 2 says the narrator never left Dioscorus "from the council's summons to his death". Paragraph 3 opens "After the death". Paragraph 4 speaks of "the council and the exile" and "those written in Egypt soon after the death". The brief never names Chalcedon, never says that Dioscorus was exiled, and never says that he died. "Those" has no noun to refer to. A listener cannot tell which council is meant or whose death. The sources carry all of it:
  - Nau names "concile de Ghalcédoine" (l.178-179);
  - the History has Dioscorus say "c'est pour elle que je meurs en exil" (l.17012-17013), and puts "deux mois après sa mort" (l.17022);
  - Nau writes "un certain nombre de récits en sa faveur" (l.582).

  The fix also settles the ambiguous "He tells how a heretic slapped him". As drafted, it follows a sentence whose subject is Nau.

  Fix, paragraph 2, sentences 3-4: replace "François Nau, who put the Syriac into French, notes his claim never to have left Dioscorus from the council's summons to his death. He tells how a heretic slapped him for begging an envoy not to mock the old man." with "François Nau, who put the Syriac into French, notes one claim the narrator makes. From the summons to the Council of Chalcedon, by his own account, he never left Dioscorus until the bishop died in exile. He tells how a heretic slapped him for begging an envoy not to mock the old man."

  Fix, paragraph 3, sentence 1: replace "After the death, the book says," with "Two months after the death, the book says,".

  Fix, paragraph 4: replace "may have been among those written in Egypt soon after the death." with "may have been among the stories in Dioscorus's favor written in Egypt soon after his death."

- **E-B2 BLOCKING (brief, paragraph 3, sentence 2; items 1, 7; the book's account told as fact).** "He hid in the city of Pentapolis and wrote this history there." The coordinator ruled that the narrator's account is told as the book's account, never as settled fact. This sentence starts outside the reported speech of the sentence before it. It states as fact the very claim that Nau's reworking view disputes, and that the contested_claim records as one side. Nau's view is that the present text was reworked after 512 and then translated (l.577-595), so "wrote this history" cannot stand as fact.

  Fix: "He says he hid in the city of Pentapolis and wrote this history there."

- **E-B3 BLOCKING (card, `uncertain` item 5; items 1, 12; false absence).** "No source used here besides the History and the Coptic sermon on Macarius names him." Two of this card's own sources name him. They are Nau 1912 ("l'Histoire de Dioscore, écrite par son disciple Théopiste", po08 l.447-448) and Nau's PO 13 note ("écrite par son disciple Théopiste", PO 13 file l.12638-12639). They name him only as the History's writer. The point the card means, that no witness tells of him apart from the book, is true. As written, though, the sentence is false.

  Fix: "His life outside the book. No source used here tells of him apart from the History and the Coptic sermon on Macarius. François Nau's later notes name him only as the History's writer."

- **E-M1 MINOR (brief, paragraph 1, sentences 1-2; item 1; small additions to the scene).**
  - "came up behind the reader": the History has "je vins par derrière et la regardai" (l.13952), "I came from behind and looked at it", and does not say behind whom.
  - "He saw in it the names of men he calls evil counselors": the line is "j'y lus les noms de ces mauvais conseillers". The History has just said Marcian "les louait et les exaltait comme ses conseillers" (l.13928-13930). As drafted, the listener hears "counselors" without knowing whose.

  Fix: "The emperor Marcian's letter was being read out in Alexandria, the History of Dioscorus says, when its narrator came up from behind and looked at it. He read in it the names of men the emperor praised as his counselors, men he calls evil."

- **E-M2 MINOR (brief, paragraph 4, sentences 2-3; item 4; context).**
  - "In one vision" does not say whose. It is Dioscorus's ("J'ai vu cette nuit", l.16865-16866).
  - "which puts the present text after 512" asks the listener to supply the year Severus took the see. Nau's note gives it: "Sévère fut patriarche de 512 à 518" (l.498).

  Fix: "In one of Dioscorus's visions, a saint blesses a small child named Severus. Nau reads this as a sign that Severus will be patriarch of Antioch. Severus took that see in 512, so Nau puts the present text after that year."

- **E-M3 MINOR (brief, paragraph 4, sentence 5; item 4; undefined term and unplaced figure).** "a rhetor of the school of Peter the Iberian". "Rhetor" is an undefined technical term. Peter the Iberian appears with no anchor, although Nau's note places him: "Pierre, évêque de Maiouma, près de Gaza" (l.15346-15347).

  Fix: replace "After 512, he suggests, a rhetor of the school of Peter the Iberian reworked it, probably in Greek." with "After 512, he suggests, a writer trained in rhetoric reworked it, probably in Greek. Nau places that writer in the school of Peter the Iberian, a bishop near Gaza."

- **E-M4 MINOR (card, `place`; items 1, 9; the History's word and Nau's reading merged).** The History reads "la ville de Pentépolis" (l.17029-17030), "the city of Pentapolis", which the brief keeps. Nau's note reads "Ou plutôt : Dans la Pentapole (Cyrénaïque)" (l.17034), and his introduction puts it with a question mark, "(la Pentapole?)" (l.445). The card's "a city of Pentapolis" is neither the History's word nor Nau's. "Takes rather" is also firmer than Nau's question mark. The card also drops "Paphlagonia", which the approved Dioscorus card carries. That word is in the Coptic panegyric as Nau quotes it: "Gangres, île de la Paphlagonie" (l.801).

  Fix: "Alexandria; Constantinople and Chalcedon; Gangra in Paphlagonia, which the History calls an island; the city of Pentapolis, as the History names the place where he says he hid and wrote, which François Nau suggests is rather the Pentapolis of Cyrenaica"

- **E-M5 MINOR (card, `uncertain` items 1 and 3; items 7, 9; Nau's hedges hardened).**
  - Item 1: "He holds that after 512 a rhetor ... reworked it". Nau gives this as "la plus probable pour l'instant" (l.578-579), and the brief rightly says "he suggests".
  - Item 3: "Nau holds the Syriac is translated from Greek". Nau writes "semble être une traduction du grec" (l.594-595).
  - Item 3: the Crum fragments "will help to show which text is the original". The note says only "ils serviront à rechercher avec plus de sûreté quel est le texte original" (l.17175-17176).

  Fix, item 1: "He suggests, as the most likely answer for now, that after 512 a writer trained in rhetoric, of the school of Peter the Iberian, reworked it, probably in Greek, and that the Syriac comes from that Greek."

  Fix, item 3, sentence 1: "Nau thinks the Syriac seems to be translated from Greek".

  Fix, item 3, last sentence: "A note at the end of the translation reports that Crum found old Coptic fragments matching parts of the History, which it says will help in working out which text is the original."

- **E-M6 MINOR (card, `legacy.remembered` item 2; item 4; undefined term).** "made up by later Jacobites" leaves "Jacobites" undefined for the reader.

  Fix: "Assemani, in the Vatican Library's catalogue, called it a fabulous tale made up by later Jacobites, as he called the Syriac churches that rejected Chalcedon, Nau reports."

  If the gloss is judged to rest on no held line, use this instead: "called it a fabulous tale made up by later writers of Dioscorus's party". That matches the card's own wording in `uncertain` item 1.

After the fixes, the brief is 308 words, 1:54 at 162 a minute, with FK 7.66 and Flesch 68.91 by `grade_text` on the fixed text. That is above the coordinator's expected 1 to 1:30 but within the 1-to-2-minute rule. The added words are context the listener needs (Chalcedon, the exile and death, the year 512, Peter's place), not padding. If length must come back down, the sentence placing Peter the Iberian near Gaza can go to the card, which costs about 12 words.

#### Verdicts
- Theopistus: NOT CLEAR (3 blocking, 6 minor).

---
