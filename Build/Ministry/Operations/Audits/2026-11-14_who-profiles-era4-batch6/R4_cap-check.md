# R4 cap check: era 4 batch 6

**What this is.** The one targeted check Mark ordered in his cap ruling for era 4 Who batch 6 ("Fix + one check (Recommended)", 2026-11-14). It sits outside the three-round cap. It was done by a fresh Opus reviewer who had not seen the drafting or any earlier round, at full effort.

**Scope.** Only the strings changed in round 3, row by row as `R3_changes.md` lists them, plus the opening line of the Severus brief, which changed beyond the counted points. The diff is `git diff 67e32d72 3143636c -- Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch6/` (commit 3143636c, "round 3 fixes under Mark's cap ruling"). The working tree matches 3143636c.

**Method.** I read CLAUDE.md ("Trust and source fidelity", "Accessible and rigorous"), `Who_Profile_Pattern.md` (14-point checklist), `R3_changes.md` and `R3_recheck.md`. For each changed string I:
1. reopened the cited lines in `cic/texts/` and read them in context;
2. read it as a listener would hear it: what each pronoun points to, which witness goes with which claim, identifiers at first mention in that text, and repetition;
3. checked for AI tells, narrator contrasts and beat lines;
4. counted sentence lengths by script, and graded each changed brief with `engine.m1.gates.grade_text`;
5. checked each records row's line numbers against the words it quotes.

I checked each audio script against its brief in two ways: a scripted rebuild (brief, "[calmly] " at the start, "[warmly] " at the start of the last paragraph) compared for equality, and a `sed` tag-strip `diff` against the brief. All four match both ways.

**Files.** PO5 = `chronicle-of-seert_histoire-nestorienne-premiere-partie-fasc2-patrologia-orientalis-5-ara-fra_scher-dib1910.txt` (Evetts's History of the Patriarchs). REN = `renaudot_historia-patriarcharum-alexandrinorum-jacobitarum-lat_1713.txt`. PO11 = `synaxaire-arabe-jacobite_po11-toubeh-amshir-fra_basset1915.txt` (Porcher's Mina). PO17 = `john-ephesus_lives-eastern-saints-po17_brooks1923.txt` (Basset, 24 Abib, bound in). BUD1 = `ethiopian-synaxarium_book-of-saints-ethiopian-church-v1-maskaram-khedar_budge1928.txt`. BUDM = `ethiopian-synaxarium_book-of-saints-ethiopian-church-v2-v4-microform_budge1928.txt`.

---

## 1. Agathon card, `keyWorks[0].about` (R3-1-M2): CLEAR

"told in his voice inside the History's life of Benjamin I. Benjamin's vision and his rules for the church come through it. Eusèbe Renaudot called it a fable under Agathon's name"

The card no longer claims the account is his own. It now agrees with the brief ("an account told in Agathon's voice"). "his" refers to Agathon, the card's subject. Sentences run 11, 11 and 9 words. No tells.

## 2. Agathon card, `uncertain[1]` (R3-1-M1): CLEAR

"The account told in his voice in Benjamin's life. Eusèbe Renaudot, a Catholic scholar writing in 1713, calls the Coptic patriarchs heretics. He calls the account a fable under Agathon's name, and judges Benjamin's canons in it the work of later Copts."

Source: REN l.8589-8590, "de haereticis illis Patriarchis", in his plan to treat the Jacobite line of Alexandria. REN l.11542-11543 has the canons, "a Coptitis recentioribus inventa esse non dubitamus". "The Coptic patriarchs" now has a referent, and Agathon is one of them, so the reader sees the bias. The label no longer settles who wrote the account. Sentences run 9, 13 and 20 words.

## 3. John III records, Renaudot claim row (R3-1-M3): CLEAR

The witness is now REN l.12072-12074, 12092, 12096-12097, 12198. Checked:
- l.12073-12074: "fed diverfx fidei , nam erat Jacobi-/ta";
- l.12092: "centum aureorum millia";
- l.12096-12097: "ne centum quidem drachmas / habere fc";
- l.12198: "an. Hcg. ^7% J. C. 686", which is AH 67 = 686.

The OCR notes match l.12072 ("Semnudarus", "Apthonis") and l.12198.

## 4. Isaac brief and audio, paragraph 3 (R3-1-M4, R3-1-M5): CLEAR

"Meneson served the governor of Egypt. The History says John III called Isaac and made him his partner in governing the church."

Source: PO11 l.21562-21563, "administrateur (chartularius) au service de Georges, qui était éparque ... au pays d'Égypte". PO5 l.1172-1178: John "wrote and summoned that brother", Isaac, and "commanded him to become his partner in administering the affairs of the Church".

Listener read: "called Isaac" removes the wrong referent. Dropping the governor's name ends the run of three Georges. The switch from Mina to the History is spoken aloud. The governor of Egypt is never confused with the Amir Abd al-Aziz, since the brief calls the Amir only "the Amir".

Grade: 344 words, FK 6.96, Flesch 68.64. Audio matches.

## 5. Simon brief and audio, paragraph 5 (R3-1-M6): MINOR

"At sunset on the second day, Simon's spiritual son found the Indian priest. The next morning the priest told the Amir all that had happened, and the Amir saw that Simon had told the truth."

**Source: sound.** PO5 l.2179-2181: "at sunset on the second day his spiritual son, the monk, ... saw walking there that black Indian priest". l.2217-2218: "when the morning of the third day came". l.2228-2230: the Indian priest "made known to him all that had happened". l.2256: the Amir "acknowledged his honesty". The two days are now apart, and the listener learns why finding the priest proved Simon right. The sentences run 13 and 22 words.

**Listener point.** "The second day" counts from nothing the listener has heard. The brief goes straight from the night questioning and Simon's quoted reply to "at sunset on the second day". The source gives the count: the Amir "will grant thee a delay of three days" (PO5 l.2173-2174), and that comes after the quoted reply (l.2121), so the order holds. Without the delay, the listener also misses that Simon was working to a deadline.

**Fix (brief and audio):** after the quote, insert one sentence.

> ... "If a voice came from heaven, bidding me deviate from the truth, I would say no otherwise." The Amir gave him three days. At sunset on the second day, Simon's spiritual son found the Indian priest. ...

Rescored: 381 words (about 2:21), FK 5.80, Flesch 76.97. Records: add PO5 l.2173-2174 ("I will grant thee a delay of three days") to the row that holds the questioning.

## 6. Simon card, `place` (R3-1-M7): MINOR

"Born in the East, the History says. Brought up at the monastery of Az-Zajaj, and buried there. The History says the body of Saint Severus lies in a shrine there. Budge's Ethiopic names him Severus of Antioch, and the synaxaria place the monastery west of Alexandria"

**Source: sound.**
- PO5 l.1537-1542: Simon was given to the Church "for the sake of the body of the holy Saint Severus; for it lies in a shrine in that monastery". This is Abba John's monastery, Az-Zajaj (l.1503).
- BUDM l.3449-3451: "the body of Saint Abba severus, Archbishop ... of the city of Antioch, to dabra ZEGAG which is outside the city of Alexandria".
- PO17 l.58449-58450 and BUDM l.42752-42753 place the monastery that holds Severus's body west of Alexandria.

"Where" no longer attaches to Alexandria, and Severus now has his identifier.

**Clarity point.** This string is the first place the card mentions Budge. "Budge's Ethiopic" is shorthand that the card explains only later, in `legacy.remembered[1]` ("The Ethiopic Synaxarium, in E. A. Wallis Budge's English"). A reader at `place` does not know what "Ethiopic" names. The round 3 change created this first mention; before it, `place` named only "the synaxaria". The `dates` field has already introduced the Arabic Synaxarium, so once the Ethiopic is named, "both synaxaria" is exact.

**Fix:**

> Born in the East, the History says. Brought up at the monastery of Az-Zajaj, and buried there. The History says the body of Saint Severus lies in a shrine there. The Ethiopic Synaxarium, in E. A. Wallis Budge's English, names him Severus of Antioch. Both synaxaria place the monastery west of Alexandria

(The sentences run 6, 10, 13, 13 and 7 words.)

## 7. Simon records, the Az-Zajaj row (R3-1-M9): MINOR

The claim quotes the History, "'lies in a shrine in that monastery' (PO5 l.1540-1541)", and the witness reads "PO5 ... l.1472, 1536-1541". In the file, l.1541 ends "for it lies in a shrine in that" and "monastery," is on l.1542. Both the claim's citation and the witness range stop one line short. This is the same off-by-one that R3-1-M9 found for BUDM, carried over from R3's own evidence line.

The other cites are right: "Archbishop of the city of Antioch" is at BUDM l.3450, "Dabra Zegag" at l.3450-3451, Basset's words at PO17 l.58449-58450, and Budge's "wherein is the body of Saint severus" at BUDM l.42752-42753.

A second point: the row leaves one step unstated. The card's "names him Severus of Antioch" rests on reading Budge's Dabra Zegag as Az-Zajaj. No vendored line states that equation; it rests on the name form and on both lying outside, or west of, Alexandria. The record should say so.

**Fix, claim:** replace "(PO5 l.1540-1541)" with "(PO5 l.1541-1542)", and add at the end: "; Dabra Zegag is read as the Ethiopic form of Az-Zajaj, from the name and from both lying outside (west of) Alexandria; no held line states the equation".
**Fix, witness:** replace "l.1472, 1536-1541;" with "l.1472, 1503, 1537-1542;".

## 8. Simon brief and audio, paragraph 3 (R3-1-M8): CLEAR

"B. Evetts, who translated it, dates Simon's patriarchate 689 to 701."

Source: PO5 l.1535, "SIMON I, THE FORTY-SECOND PATRIARCH. A. D. 689-701". This is clear aloud, and it matches the John III brief's "dates John's patriarchate". Audio matches. 375 words, FK 5.93, Flesch 76.43. The one sentence over 25 words (26) carries Simon's quotation and did not change.

Not counted (unchanged text): the Simon card `dates` still says "B. Evetts heads his life 689 to 701". This is the same unchanged-line point R3-1-M8 made for the Agathon and Isaac briefs.

## 9. Simon card, `uncertain[1]` (R3-1-B1): CLEAR

"Who wrote these years. John the deacon says George's history ran from Cyril to the days of Alexander II, down to the time of the caliph Sulaiman. Renaudot gives George the same end point. He says many wrote the lives from Cyril to Simon, George above all."

**Source.** PO5 l.4501-4505: "from the time of the Father Cyril ... down to the days of the father and confessor Alexander, we may consult ... Abba George". PO5 l.4531-4535: George informed us "down to the time of Sulaiman, son of Abd al-Melik". REN l.13765-13770: "historiam a Cyrillo usque ad Simonem scriptam esse testatur a multis, atque praesertim a Georgio ... qui persecutus est ... usque ad Solimanum".

The false dispute is gone. The card now agrees with the Alexander II card and with Simon's own records row.

The grammatical subject of Renaudot's "testatur" is the History's author, whom Renaudot is reporting. "He says" is still a fair attribution, because the sentence stands in Renaudot's own narrative. "The same end point" follows a sentence that names two end points, but Alexander's days and Sulaiman's reign overlap, and the next word the reader needs is Sulaiman. It reads cleanly.

Identifiers: `legacy.traces[2]` already names Cyril of Alexandria and Simon's archdeacon George, and `dates` introduces Renaudot. Sentences run 23, 7 and 13 words. No contrast frame and no tell.

## 10. Simon records, Renaudot claim row (R3-1-B1): CLEAR

"the lives 'a Cyrillo usque ad Simonem' written 'a multis, atque praesertim a Georgio', who carried his account 'usque ad Solimanum'".

The words are at REN l.13765 ("a Cyrillo"), l.13766 ("usquead Simonem", "a multis, atque prarsertim", OCR), l.13767 ("a Georgio") and l.13770 ("usque ad Solimanum"). All fall within the cited l.13765-13770. The row's other quotes did not change.

## 11. Simon records, contested row "How far George's history ran" removed (R3-1-B1): CLEAR

No witness holds the second side, so the removal is right. The JSON parses. Nothing else in the batch refers to the row (grep). The `absent_details` note at Simon ("George is named only in Michael I's life") still holds.

## 12. Alexander II card, `uncertain[1]` merged (R3-2-M1, R3-2-M2): CLEAR

"Who wrote it. John the deacon, who wrote the History's life of Michael I, says the archdeacon George's history ran down to the time of the caliph Sulaiman. John says he himself told what followed, down to the death of Theodore, patriarch of Alexandria. Eusèbe Renaudot, a Catholic scholar writing in Latin in 1713, reads John the same way. He puts the years under the governor Usamah in John's part."

**Source.** PO5 l.4531-4535 (Sulaiman). PO5 l.4584-4585: "having related what took place down to the death of the blessed Father Theodore, patriarch of Alexandria". REN l.13770-13772: "quibus ipse autor adjecit quae usque ad Theodori mortem, sub Asama & aliis Aegypti Praefectis ... secuta sunt".

**Clarity.** "He himself" now sits where it belongs. "John" has no rival in this card. "He" in the last sentence refers to Renaudot, the subject of the sentence before. Usamah is introduced with his role. Sentences after the label run 25, 16, 15 and 11 words.

Not counted (unchanged words): "the archdeacon George" has no anchor in this card. The Simon card's "Simon's archdeacon George" would anchor it, if the drafter wants it.

## 13. Michael I card, `dates` (R3-2-M3): CLEAR

"B. Evetts heads the life 744 to 768, and the title of his volume gives 766."

PO5 l.4414 has "A. D. 744-768". PO5 l.138 and l.302 have "AGATHO TO MICHAEL I (766)". "The life" is the card subject's, and "his volume" now has only Evetts in reach. The rest of the field did not change.

## 14. Michael I card, `uncertain[3]` (R3-2-M3): CLEAR

"His years. B. Evetts's heading gives 744 to 768, and the title of Evetts's volume gives 766. ..."

The sources are the same as in section 13. Saying "Evetts's" twice is deliberate: it keeps "his" from pointing at Michael, and on the page it reads cleanly. This is a card field, read by eye.

## 15. Joseph I brief and audio, paragraph 5 (R3-2-M4): CLEAR

"In the Ethiopic Synaxarium and in Renaudot, Joseph also begged the governor to spare the two bishops."

**Source.** BUD1 l.14725-14731: "I therefore beseech thee to have mercy upon them". Budge's man is "the King of Egypt" (l.14695). REN l.18214-18215: "Cumque Afschinus supplicium de illis sumi juberet, intercessit & obtinuit, ut illis parceretur". Renaudot's man is the prefect Afshin (l.18194).

"The governor" now names the same man as the paragraph's first sentence, so no new ruler seems to appear. Audio matches. 362 words, FK 7.07, Flesch 66.65. No sentence runs past 25 words.

## 16. Joseph I records, sword row (R3-2-M5a): CLEAR

The row adds "Budge 'his sword struck a pillar, and broke'", with BUD1 l.14697-14701. The words are at l.14701, inside the range, and the range takes in the king's brother drawing the sword (l.14698). The other cites are as before. "In columnam marmoream" is at REN l.18208 and "patrem suum ... misit" at l.18197/18207, both inside l.18193-18211.

## 17. Joseph I records, Renaudot plea row (R3-2-M5b): CLEAR

The witness is now REN l.18197-18215. "In Ecclesiam" spans l.18197 and l.18207 ("in Eccle-" / "siam misit"). "Interceffit & obtinuit , ut illis parceretur" is at l.18215. Afshin's order is at l.18214-18215. All fall in range.

## 18. Severus records, Wadih row (R3-2-M6): CLEAR

The witness is now REN l.23439-23442, 23446-23527 and 23576-23577, and the claim adds "baptised, 'baptismum petiit & obtinuit' (l.23526-23527)". Checked:
- l.23440: "juvenis inter nobiliores urbis Misrae";
- l.23442: "in Muhamedana Religione";
- l.23526-23527: "baptifi- / mum petiit j & obtinuit";
- l.23576-23577: "Scripsit quoque Vazah filius Reja, libros aliquot lingua Arabi-/ca".

## 19. Severus brief and audio, paragraph 1, "fast today" (R3-2-M7): CLEAR

"Muslims do not fast today, and drink no wine."

REN l.23093-23094: "Muslemani non jejunant / hodie nec vinum bibunt" (OCR "Mujlemani", "hodte", "btbunt"). The quip no longer states a falsehood about Muslims in general.

## 20. Severus brief and audio, opening line (beyond the counted points): MINOR

"A dog walked past while Severus, bishop of al-Ushmunain, stood before the chief judge."

**The line: sound.** REN l.23087-23090 has the scene ("apud supremum Judicem, praetereunte cane"), told of "eumdem Severum". REN l.23072-23074 has "Severum Episcopum Aschmonin" in the same passage, and l.23571 has "Episcopo Aschmonin". The identifier meets checklist item 8. The scene still opens the brief, and the sentence runs 13 words.

**The repetition: it trips.** Paragraph 2's second sentence still reads "Severus ibn al-Muqaffa was bishop of al-Ushmunain, in Upper Egypt, and was famous, Renaudot says, for his mastery of Arabic." The listener heard "bishop of al-Ushmunain" ten sentences earlier. Paragraph 2 now presents it as new information, which sounds unedited. The sentence has two jobs left: to give the full name and to say what Renaudot says he was famous for. "Upper Egypt" carries no witness in the brief (the card gives it as B. Evetts's). It can move to the opening line as plain narrator context without being credited to Renaudot.

**Fix (brief and audio, two strings):**
- Paragraph 1, first sentence: "A dog walked past while Severus, bishop of al-Ushmunain in Upper Egypt, stood before the chief judge."
- Paragraph 2, second sentence: "The bishop was Severus ibn al-Muqaffa, and Renaudot says he was famous for his mastery of Arabic."

"The bishop" points back to the scene, and "Eusèbe Renaudot ... tells this story" comes just before it. Each sentence runs 17 words. Rescored: 350 words, FK 6.58, Flesch 71.90. In the audio, "[calmly] " stays at the start.

## 21. R3 change log, row R3-2-M8 (audit trail, not participant-facing): MINOR

The row says: "The cards use 'B. Evetts' in prose throughout, except 'Evetts's 1895 English' in a few `place`, `dates` and `uncertain` strings after B. Evetts is named in the same card." A script over every card's prose fields finds more bare forms than that:
- John III `uncertain[2]` "Evetts's English does not say" and `uncertain[3]` "Evetts heads Isaac's life";
- Michael `uncertain[3]` "the title of Evetts's volume", new in round 3;
- Severus `uncertain[2]` "Evetts says the lives" and `uncertain[5]` "Evetts said the ninth".

In every card the first prose mention is "B. Evetts", and every bare form comes after it. The card text is acceptable. The log describes it wrongly for the third time.

**Fix:** this log is a lasting record. Leave `R3_changes.md` as the round 3 record, and log the correction where the next change log or the batch build log records this check:

> The R1, R2 and R3 change logs describe the Evetts forms wrongly. Each card names "B. Evetts" at its first prose mention. Later mentions in the same card use "B. Evetts" or "Evetts" ("Evetts's 1895 English", "Evetts's English", "Evetts heads", "Evetts says", "Evetts said", "Evetts's volume"). "B. T. A. Evetts" stays only in the 1895 source title.

---

## Overall verdict: NOT CLEAR (0 blocking, 5 minor, 16 clear)

- **Blocking: 0.** R3-1-B1 is fixed correctly in the card and in both records changes.
- **Minor: 5.**
  - §5: Simon brief, "the second day" has no count. Add "The Amir gave him three days."
  - §6: Simon card `place`, first mention of Budge's Ethiopic.
  - §7: Simon records, PO5 line 1542, and the Zegag = Az-Zajaj step stated.
  - §20: Severus brief, "bishop of al-Ushmunain" said twice.
  - §21: the change log's Evetts description.
- **Clear: 16.** §1-4, §8-19.

Every source check passed. No quoted words are misplaced except the one-line shortfall in §7. No AI tells, narrator contrasts or beat lines were found in any changed string. All changed card sentences run 25 words or fewer. All four changed briefs pass `grade_text`, and all four audio scripts equal their briefs with the two tags, checked two ways.

The five minors are wording or citation fixes given here in exact form. Each has been checked against its source line, and the brief changes have been rescored. When they are applied as worded, the batch is CLEAR. None of them needs another review round. Two are brief changes, and their audio scripts must be rebuilt from the edited briefs.
