# R1 review: era 4 batch 9

Round 1, the full checklist review, by three fresh Opus agents that had not seen the drafting, at full effort. Part A covers John of Damascus and Theodore the Studite. Part B covers Cyril and Methodius and Clement of Ohrid. Part C covers Antony and Theodosius of the Kyiv Caves, Anskar, Rimbert and the README. Each part is given as its reviewer wrote it.

## Era 4 Who batch 9, round 1 review: PART A

**Scope.** `john-of-damascus` and `theodore-the-studite`: brief, card, audio script and each one's `records.json` entry. Also the README's statements about these two, including "John of Damascus, the live entry", checked against `cic-website/data/world-census.json` (movements `melkite-arabic-christianity` and `iconophile-byzantine-monasticism`, people named John of Damascus).

**Method.** I read CLAUDE.md, `Who_Profile_Pattern.md` and its 14-point checklist, the brief, the first part of the batch 8 and era 6 batch 2 R1 reviews for form. I opened every line range the two records cite, with context, and read each one for who is speaking. I checked each quotation against its file. I ran `engine.m1.gates.grade_text` on both briefs and on my proposed rewrites, counted words and sentence lengths by script, and compared each audio file with its brief by script. I searched all of `cic/texts/` before accepting any absence. I edited no repo file.

**Quotations.** Every quotation in double quotes matches its file.
- John brief: "Anathema to Mansur, who has an evil name and Saracen opinions!" matches NPNF14 l.39468-39469.
- John brief: "we fall down and worship not the material but that which is imaged." matches NPNF9 l.36278-36279 (the file runs on with a colon).
- Theodore brief: "copied it out, and established it in his own monastery." matches CROSS l.11868-11869. The file runs on without a stop ("… monastery to govern the singing …"); the brief closes the quote at "monastery", which is fair.

**Audio.** Both scripts equal their briefs with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, and carry no other tag. Checklist 13 passes for both.

**Scores.** John: 400 words, FK 7.09, Flesch 69.36. Theodore: 405 words, FK 6.96, Flesch 69.68. Both pass, both inside the 2:30 cap for majors (Theodore is at it). Two John sentences and two Theodore sentences run 26 words; none past that.

---

### john-of-damascus

**Verdict: one blocking finding (A-B1). Otherwise passes with minor fixes.** The Life is placed early and well, the cut hand is told as the Life's with Fabricius and Allatius on either side, and the dates are owned by name. The proposed fixes below, applied together, bring the brief to exactly 405 words (FK 7.24, Flesch 68.61); the word budget is noted on each.

**A-B1 (brief para 6; card `legacy.remembered[1]`; records claim on Stephen the Deacon): Stephen the Younger's words given to Stephen the Deacon.**
- Brief: "In it he recalled that John kept writing against the emperor Constantine V. The tyrant called him Mansur, Stephen wrote, but we call him holy and God-bearing."
- Card: "Stephen the Deacon, writing in 808, says the tyrant called him Mansur, but we call him holy and God-bearing."
- In the Life these words are a speech by Stephen the Younger to the monks before they scatter. The narrator closes it in his own voice. Evidence: PG100 l.92531-92537: "Inter quos etiam honoratissimus et sapientissimus Joannes Damascenus presbyter (quem hic tyrannus Mansur nominabat, nos autem sanctum et deiferum appellamus) eidem scribere … non destitit"; then l.92547-92549: "His pluribusque aliis animae perutilibus sermonibus a beatissimo Stephano dictis, Patres preces lugubres peregere". The speech opens at l.92459-92460: "ex imo suspirans Pater ait". Allatius reads it the same way: PG94 l.7276-7277: "verba S. Stephani Junioris, apud Stephanum Byzantinum qui ejusdem Vitam descripsit".
- Fix, brief: "In it Stephen the Younger tells the monks that John kept writing against the emperor Constantine V. The tyrant called him Mansur, he says, but we call him holy and God-bearing." (+4 words.)
- Fix, card `remembered[1]`: "In the Life of Stephen the Younger, written by Stephen the Deacon in 808, Stephen the Younger tells the monks that the tyrant called John Mansur, but we call him holy and God-bearing."
- Fix, records: in the Stephen the Deacon claim, change "in it John … kept writing against the emperor" to "in it Stephen the Younger, speaking to the monks (l.92459-92460, 92547-92549), says John … kept writing against the emperor".

**A-M1 (brief para 2: "Mansur" left unexplained, and "son of Mansur" told plainly).**
- "Mansur was John of Damascus … The chronicler Theophanes the Confessor names him as the son of Mansur". A listener hears the cursed name, then hears he was the son of a man of the same name, with nothing joining the two. "Son" is also contested (card `uncertain[2]`: Anastasius's Latin says grandson).
- Theophanes himself says Mansur was the ancestral name. Evidence: THEO l.75289-75291 (Goar): "et Mansur aviti nominis, quod … redemptus [interpretatur]"; THEO l.121040 (Anastasius): "pro Mansur, quod est avitum nomen ejus".
- Fix: "Theophanes the Confessor, a chronicler, says Mansur was his family's name, and that John was rightly called Chrysorrhoas, golden-flowing, for the grace of his speech." (-1 word.)

**A-M2 (brief paras 3-4: two Leos, and two scholars with no context).**
- "while Leo Allatius counts the healing …" comes one sentence after "The emperor Leo the Isaurian". Para 4 then opens "says Leo began to move against the images", where the last Leo named is Allatius.
- "Johann Fabricius" and "Leo Allatius" enter with no word on who they are (checklist 4, "statements with no context"; the pattern's common-name rule covers "any name a general listener would not know"). Le Quien gets his context. Fabricius's notice is headed "Notitia ex Bibliotheca Fabricii" (PG94 l.603), and Le Quien prints Allatius's prolegomena; "bibliographer" and "scholar" add no claim beyond that.
- Fix, para 3: "The bibliographer Johann Fabricius dates its author …" (+2) and "while the scholar Leo Allatius counts …" (+2).
- Fix, para 4: "Michel Le Quien, John's editor in 1712, says the emperor began to move against the images in 726." (-1.)
- Budget trim to pay for this, para 1: "Its bishops cursed three men by name." to "They cursed three men by name." (-1.)

**A-M3 (card `uncertain[3]` and records: Le Quien's dissent on the Life's order is missing).**
- The Life has John at the caliph's court while he writes against Leo, and makes him a monk only after the healing. Le Quien holds he was already a monk and a cleric of Jerusalem early in Leo's reign. Evidence: PG94 l.31104-31109: "eum monasticae vitae nomen dedisse, atque in clerum Hierosolymitanum accensitum fuisse, sub primis temporibus Leonis Isauri imperatoris"; and his note at the forgery, PG94 l.32300 ff.: "gravis me incessit suspicio, Joannem Damascenum jam tunc in clerum … nomen dedisse".
- The brief attributes the order to the Life ("Then, the Life says"), so it is not wrong. The card should carry the dissent.
- Fix, `uncertain[3]`: "His post at court. Only the Life says the caliph made him first counselor, and it has him become a monk after the healing. Le Quien thinks he was already a monk and a cleric of Jerusalem early in Leo's reign." Add a matching `contested_claim` ("When he became a monk": the Life, PG94 l.33011-33035; Le Quien, l.31104-31109).

**A-M4 (card `uncertain[2]`, `otherNames[1]`, records: the name's early witnesses are not used).**
- `otherNames`: "Mansur, his family's name by Michel Le Quien; the name the council of 754 cursed". "By Michel Le Quien" is unclear English, and the early witness is Theophanes (A-M1).
- `uncertain[2]` sets Allatius against Le Quien on "family name or insult". Both sides have early witnesses. Family name: Theophanes (THEO l.75289-75291, l.121040). Insult: Stephen the Younger's speech (PG100 l.92532-92533) and the council of 787, act 6, as Allatius quotes it (PG94 l.7286-7287: "Joannes vero, qui ab eodem per contumeliam cognominatus est"). Fabricius weighs both and sides with Theophanes: the name came from his grandfather, and the insult was Constantine's twisting of it into Manzeros. Evidence: PG94 l.552-578: "per contumeliam dictum, esse Mansur ab Iconomachis, tradit synodus septima Act. VI … Assentior tamen Theophani, qui … Mansur … quod avus ejus ita diceretur … Non tam itaque contumeliosum erat nomen ipsum Mansur … quam quod per contumeliam illud Constantinus Copronymus corruperat".
- Fix, `otherNames[1]`: "Mansur, his family's name, Theophanes the Confessor says; the name the council of 754 cursed".
- Fix, last sentence of `uncertain[2]`: "Theophanes says Mansur was his grandfather's name, and Fabricius and Le Quien agree. Stephen the Younger, in his Life, and the council of 787 say his enemies called him Mansur as an insult; Fabricius answers that the insult was Constantine V's twist of it into Manzeros. Allatius leaves it open."
- Fix, records: re-witness the "Mansur the family's name" claim to Theophanes (THEO l.75289-75291, l.121040) with Le Quien, and add the Fabricius (PG94 l.552-578), 787 and Stephen sides to the contested_claim "Mansur: family name or insult".

**A-M5 (card `uncertain[5]` "Where he died": a held witness left out).**
- The Roman Martyrology keeps his day "at Damascus". Evidence: PG94 l.37215: "Damasci natalis beati Joannis Damasceni". That is a third place beside the Bollandists' exile and Le Quien's Mar Saba.
- Fix: add "The Roman Martyrology keeps his feast at Damascus." to `uncertain[5]`, and a third side to the records contested_claim "Where he died" (PG94 l.37215).

**A-M6 (card `keyWorks[2]`: the hymn judgment is the Suda's, reported by Le Quien).**
- "Le Quien says that in hymns he, like Cosmas of Maiuma, had no superior and no equal among the Greeks." Le Quien gives it on the Suda's word. Evidence: PG94 l.4596-4599: "neminem e Graecis superiorem habuit, non parem alterum, ipso fatente Suida."
- Fix: "Le Quien, citing the Suda, says that in hymns he, like Cosmas of Maiuma, had no superior and no equal among the Greeks". Same in the records claim.

**A-M7 (card `legacy.remembered[0]`: half of Theophanes' reason dropped).**
- "says he was rightly called Chrysorrhoas for the grace of his speech." Theophanes gives speech and holiness. Evidence: THEO l.75283-75285: "ob eloquii sanctitatisque velut aureo fulgore radiantem spiritualem gratiam Chrysorrhoas recte cognominatus"; Anastasius l.121037-121038: "quae in ipso tam in verbo quam in vitae actu effloruit".
- Fix: "… and says he was rightly called Chrysorrhoas for the golden grace that shone in his speech and his holiness." The brief may keep "the grace of his speech" for budget; it is a compression and not wrong.

**A-M8 (card `dates`: "his speeches").**
- "Le Quien dates his speeches on the images to 727 or 728 and to 730." He dates two of the three.
- The 730 is also an emendation: the scan reads "anno Christi 750. quo Germanus solio detrusus est" (PG94 l.32112-32113). The records already flag it. The reading is sound, since the clause ties it to Germanus's fall, but README and card should not hide it.
- Fix: "Le Quien dates the first two speeches on the images to 727 or 728 and to 730 (the held scan reads 750; his clause ties it to Germanus's fall)." Or keep the card short and leave the note in records only.

**A-M9 (brief para 5: the Exposition line drops its condition; optional).**
- "When we see the image of Christ's crucifixion, 'we fall down …'" In Salmond the image first brings the passion back to mind. Evidence: NPNF9 l.36276-36279: "when we have not the Lord's passion in mind and see the image of Christ's crucifixion, His saving passion is brought back to remembrance, and we fall down …". The compression is not wrong, but the recall is John's point. If the budget allows (+6): "When we see the image of Christ's crucifixion, his passion comes back to mind, and 'we fall down and worship not the material but that which is imaged.'" Only with an equal trim elsewhere; the other fixes already reach 405.

**A-M10 (card `keyWorks[0]`: a doubt about the third speech; optional).** Humphrey Hody suggested the third speech might not be John's, and Wilhelm Dindorf rejects this. Evidence: PG97 l.496-499: "ita ejus testimonium eludit ut orationem illam posse suppositam esse dicat. Quae quam levia sint facile apparet." The profile uses Hody for the death year. One card line would be enough: "Hody thought the third might not be John's; Dindorf calls his reasons slight."

**Proposed brief with A-B1, A-M1 and A-M2 applied** (405 words, FK 7.24, Flesch 68.61):

> In 754 a council of bishops at Constantinople ruled against the holy images. They cursed three men by name. In Henry Percival's English, one cry runs: "Anathema to Mansur, who has an evil name and Saracen opinions!"
>
> Mansur was John of Damascus, a monk and priest in Palestine. He came from a Christian family of Damascus, a city then ruled by the Muslim caliphs. Theophanes the Confessor, a chronicler, says Mansur was his family's name, and that John was rightly called Chrysorrhoas, golden-flowing, for the grace of his speech.
>
> Most of his story comes from a Life headed as the work of a John, patriarch of Jerusalem. The bibliographer Johann Fabricius dates its author after the middle of the tenth century, and the Life says it reworks an older Life in Arabic. It tells that the caliph made John his first counselor. The emperor Leo the Isaurian, it says, forged a letter in John's hand offering to betray Damascus, and the caliph had John's right hand cut off. John prayed before an image of the Mother of God, and woke healed. Fabricius calls this a hardly credible tale, while the scholar Leo Allatius counts the healing the main thing in it. Then, the Life says, John gave away his goods and went to the monastery of Mar Saba, near Jerusalem.
>
> Michel Le Quien, John's editor in 1712, says the emperor began to move against the images in 726. John answered with three speeches in their defense. Le Quien dates the first to 727 or 728, and the second to 730, when Leo drove Patriarch Germanus of Constantinople from his see. Once, John wrote, no image could show God, who had no body. Now God has been seen in the flesh. I do not worship matter, he wrote, but the maker of matter, who became matter for my sake. Emperors, he said, have no power to make laws for the church.
>
> His Exposition of the Orthodox Faith says the same in S. D. F. Salmond's English. When we see the image of Christ's crucifixion, "we fall down and worship not the material but that which is imaged."
>
> In 808 Stephen the Deacon wrote the Life of Stephen the Younger, who died for honoring the images. In it Stephen the Younger tells the monks that John kept writing against the emperor Constantine V. The tyrant called him Mansur, he says, but we call him holy and God-bearing.

Checked and passing, with evidence: the 754 cry and "three men" (NPNF14 l.39463-39471: Germanus, George, Mansur; "The Trinity has deposed these three!"); "monk and priest" (Cedrenus via Allatius, PG94 l.7287; Martyrology and many testimonia, l.37277-37281); first counselor (PG94 l.31877-31880); forged letter offering Damascus (l.32279-32294 and the letter text that follows); the hand and the healing (l.32497-32508, 32735-32746); goods given away and the laura of Sabas (l.33011-33035); Fabricius "post medium saeculi decimi clarus", "parum credibilem", "videtur non ante a. C. 756" (l.616-620); Allatius "quod potissimum erat" (l.7181-7182); Le Quien 726, "727, aut subsequenti 728" (l.32050-32056); the Life an Arabic rework, as Le Quien reads it (l.30255-30259, 30582-30589); Oration I and II (l.89146-89155, 93182-93183, under "DE IMAGINIBUS ORATIO I" from l.88098); Fabricius on 808 and the Benedictines on the 42nd year (PG100 l.88570-88588); Le Quien's 1712 edition (PG94 l.920-926); Hody c. 750 (PG97 l.4840-4841); Le Quien "obscurum prorsus" and "ante exitum saeculi septimi" (PG94 l.31096-31101); the 104 years (l.35170-35173); the Bollandists and John Phocas (l.35138-35199); Sergius the logothete of Abd al-Malik (THEO l.66239-66243); friends Cosmas and Peter of Maiuma (PG94 l.640-643; THEO l.75236-75282); Salmond's Le Quien on his authority (NPNF9 l.27524-27527); the Martyrology's 6 May (PG94 l.37211-37218); Fabricius's Fount of Knowledge and "post a. c. 743" (l.936-943). Card order is Mark's; the brief's caveat (the late Life) opens `uncertain`.

---

### theodore-the-studite

**Verdict: one blocking finding (T-B1). Otherwise passes with minor fixes.** The opening scene is sourced and well told, the two Lives are named before their story is used, and the years are owned by Fabricius and the Sirmond chronology. The proposed fixes below, applied together, bring the brief to 404 words (FK 7.21, Flesch 68.70).

**T-B1 (brief para 5; card `keyWorks[1]`): the Testament's slave rule loses its condition.**
- Brief: "In his Testament Theodore told the abbot after him to own no slave, for a slave is a man made in God's image." Card: "own no slave, since a slave is a man made in God's image".
- Heard alone, this is a rule against slavery. Theodore bars slaves to monks only, and says owning them is allowed to people in the world, as marriage is. Evidence: PG99 l.155225-155230: "Non possidebis servum, nec tuos in usus, nec proprii monasterii, nec denique ad agros, hominem qui ad Dei imaginem factus est: hoc enim solis saecularibus concessum est, sicut nuptiae."
- Fix, brief: "In his Testament Theodore told the abbot after him to own no slave, a man made in God's image; that, like marriage, was for laymen only." (+5 words; paid for below.)
- Fix, card: "own no slave, a man made in God's image, since that, like marriage, is for laymen only; keep no female animals; …". Same in the records claim (add "hoc enim solis saecularibus concessum est, sicut nuptiae").

**T-M1 (brief para 2; README "Who the sources are"): what Mai says about the two Lives.**
- "Angelo Mai, who edited one, says they hardly differ." Mai says the wording always differs; only the events hardly vary. Evidence: PG99 l.18788-18789: "elocutio in reliquis semper ab illa edita Vita differt; sed tamen res narratae vix variant."
- Fix, brief: "Angelo Mai, who edited one, says their stories hardly differ." (+1.) Same sense in card `uncertain[0]` ("Mai says the two tell the same events in different words") and README ("which Angelo Mai says hardly differ in what they tell").

**T-M2 (brief para 4: the Prusa journey was a pretext).**
- "The emperor went to the hot springs at Prusa, expecting the two abbots to come and greet him." The Life says he pretended to go for the springs. Evidence: PG99 l.20523-20527: "Simulans enim se ad calidas aquas … fruendas pergere, Prusam cum regio comitatu venit, fore omnino putans, ut duumviri inclyti … ad se salutandum de more venirent."
- Fix: "The emperor went to Prusa, as if for its hot springs, expecting the two abbots to come and greet him." (+2.)

**T-M3 (brief para 7: one Kyiv account told as fact).**
- "More than two centuries later, Theodosius of the Kyiv Caves learned the Studion rule from a monk named Michael." Nestor's Life of Theodosius has him send to Ephraim the eunuch in Constantinople instead. Evidence: PAT l.2170-2171: "посла единаго оть брата блаженный въ Констянтинь градъ къ ЕфрЪму скопцю, да весь уставъ Студийскаго монастыря принесеть". The card already gives both; the brief should own its one.
- Fix: "More than two centuries later, Theodosius of the Kyiv Caves learned the Studion rule, the Russian Primary Chronicle says, from a monk named Michael. In S. H. Cross's English, he "copied it out, and established it in his own monastery."" (+1.)

**T-M4 (brief para 6: "the restored priest Joseph" has no context; optional).** A listener does not know what Joseph was restored to, or why. The Sirmond chronology says a synod restored the steward Joseph to his rank. Evidence: PG99 l.5639-5640: "a quibus Josephus oeconomus restituitur in pristinum gradum". If the budget allows (+3): "after he refused to accept the priest Joseph back in his old rank. Joseph had married the emperor to Theodote." The card also uses "Joseph" for this man (`knownFor`) and for Theodore's brother (`remembered[0]`, `traces[2]`). Fix, card: "the steward Joseph" in `knownFor`, and "his brother Joseph, later archbishop of Thessalonica" (THEO l.87768-87769: "ejus frater Joseph Thessalonicensis archiepiscopus") at the brother's first mention.

**T-M5 (card `keyWorks[2]`: the Antirrhetici opening).**
- "which opens: it is the time to speak, not to keep silent, now that heresy presses on us". The source has heresy rising against the truth, and the call is to whoever can speak at all. Evidence: PG99 l.27066-27067: "Tempus est ut loquatur, et non sileat qui loqui quoquomodo potest, cum instet haeresis adversus", continued in the next column: "veritatem latrans".
- Fix: "which opens: it is time for anyone who can speak at all to speak and not keep silent, now that heresy rises against the truth".

**T-M6 (card `legacy.traces[1]`: Meyer's claim widened).**
- "Athanasios the Athonite took his commands to the abbot almost word for word from the part of Theodore's Testament addressed to the abbot." Meyer says "with slight changes" for the section, and "almost word for word" for canons 1 to 5. Evidence: MEYER l.1043-1047: "Diese hat Athanasios mit geringen Abänderungen aus dem Abschnitt ἐντολαὶ τῷ καθηγουμένῳ … übernommen. Und zwar stimmen Can. 1—5 des Theodoros fast wörtlich mit den Eingangsworten bei Athanasios."
- Fix: "Philipp Meyer says Athanasios the Athonite took his commands to the abbot, with slight changes, from the part of Theodore's Testament addressed to the abbot, the first five almost word for word."

**T-M7 (card `legacy.remembered[1]`: the preface borrows its praise).**
- "The preface to Sirmond's edition says holiness made him a priest, learning a teacher, and faith all but a martyr." The preface says in this passage that it borrows Maximus of Turin's words on Cyprian. Evidence: PG99 l.3738-3746: "liceat enim hic usurpare quae a Maximo Taurinensi dicta sunt de Cypriano … in Theodoro perinde ac in Cypriano …"; the line follows at l.3751-3753.
- Fix: "The preface to Sirmond's edition, borrowing words Maximus of Turin used of Cyprian, says holiness made him a priest, learning a teacher, and faith all but a martyr."

**T-M8 (card `uncertain[2]` and records: Fabricius sides with 798).**
- "The Sirmond chronology gives 798. Philipp Meyer gives 789, but cites the same chronology." Fabricius puts the recall and the Stoudios abbacy in the year after Constantine VI's fall. Evidence: PG99 l.358-359: "sed mox anno proximo post Constantini mortem magno cum honore revocatus ab Irene, et abbas Studio praefectus fuit".
- Fix: add "Fabricius puts it the year after Constantine VI's fall." and add Fabricius as a side in the contested_claim.

**Budget trims for T-B1 to T-M3.** Para 5: "a chronicler of his own time, says up to 700 monks served under him there." to "a chronicler of the time, says up to 700 monks served under him." (-3). Para 6: drop "He was exiled twice more." (-5); "The second exile came in 809" still reads cleanly after the Thessalonica exile in para 4.

**Proposed brief with T-B1 and T-M1 to T-M3 applied** (404 words, FK 7.21, Flesch 68.70):

> An officer came to Theodore the Studite in exile with orders to give him fifty lashes. Theodore praised God, stripped off his clothes and said, My son, do what you were ordered to do to me. Struck with sudden fear, his Life says, the man threw himself at Theodore's feet and asked for his blessing.
>
> Theodore was abbot of the Stoudios monastery in Constantinople. His story is told in two Lives that carry the name of Michael the monk. Angelo Mai, who edited one, says their stories hardly differ.
>
> He was born in the city in 759, by Johann Fabricius's count. At 22, the Life says, he left the world with his family, led by his mother's brother Plato, for Sakkoudion, an estate outside the city. At 35 he became abbot there, against his will.
>
> The emperor Constantine VI then put away his wife and married Theodote, a kinswoman of Theodore's. Theodore and Plato broke off communion with him. The emperor went to Prusa, as if for its hot springs, expecting the two abbots to come and greet him. They stayed away. His men flogged Theodore and sent him with ten monks into exile at Thessalonica.
>
> Recalled, he took charge of Stoudios. Theophanes the Confessor, a chronicler of the time, says up to 700 monks served under him. In his Testament Theodore told the abbot after him to own no slave, a man made in God's image; that, like marriage, was for laymen only. Among the brothers all should be shared, nothing anyone's own, down to a needle.
>
> The second exile came in 809, after he refused to accept the restored priest Joseph, who had married the emperor to Theodote. The third came when he stood against the emperor Leo V's ban on images. When Christ suffers persecution in his image, he wrote to all the monks, even the disciple must speak the truth with a free and fearless voice.
>
> He died on Sunday the 11th of November 826, with his disciple Naukratios, the next abbot, beside him. The brothers were singing a psalm, and at the words I will never forget your precepts, for by them you have given me life, he died.
>
> More than two centuries later, Theodosius of the Kyiv Caves learned the Studion rule, the Russian Primary Chronicle says, from a monk named Michael. In S. H. Cross's English, he "copied it out, and established it in his own monastery."

Checked and passing, with evidence: the officer and the fifty lashes (PG99 l.23846-23861); the Lives' headings and Mai's Monitum (l.8205-8208, 18756-18786); Fabricius on 759, 794, 796, 809, 811, 814, 821, 823, 826 and the Confessor title (l.351-370); 22 and 35 (l.19232-19234, 10146-10149); Plato his mother's brother (l.8982-8983, 19328-19331); Sakkoudion an estate (l.19429-19431); the break and the Prusa episode, ten monks, Thessalonica (l.20502-20545); Theodote's kinship in both Lives (l.10266-10267, 20516-20518); Theophanes on the beaten monks and Plato's nephews (THEO l.85205-85215) and the 700 monks (l.87174-87176); Joseph's restoration and the synod of 809 (PG99 l.5638-5640, 5714-5726); Letter II.2 to those living the monastic life (l.93979-93991); the death on Sunday the 11th, Menas's day, at "In aeternum non obliviscar" (l.18586-18600; Naukratios l.157426-157436); 67 years (l.18234); the translation after 18 years (l.18684-18693); Kallistos and Allatius on the Lenten canons (l.832-837, 3594-3604); Cross on Michael and the rule (CROSS l.11864-11876). Card order is Mark's; the brief's caveat (the two Lives) opens `uncertain`.

---

### README statements on these two

**A-M11 ("John of Damascus, the live entry": the census quotation).** "The census lists him … with the year 730 and a quotation from the Exposition of the Orthodox Faith (Salmond's English, `npnf209` l.36233-36234)." Only the Iconophile Byzantine Monasticism row carries that quotation ("fault with us for worshipping and honouring the image of our Saviour and that of our Lady", which matches NPNF9 l.36232-36234). The Melkite Arabic Christianity row has the year 730 and a `held` pointer to the Exposition, with no quotation. Fix: "The census lists him in Melkite Arabic Christianity and in Iconophile Byzantine Monasticism, both with the year 730. The Iconophile entry quotes the Exposition of the Orthodox Faith (Salmond's English, `npnf209` l.36233-36234); the Melkite entry points to the same held file."

**A-M12 ("logged in Open-Gaps").** The README says "the difference is logged in Open-Gaps for the census fix." No such entry is in `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` (searched for Damasc, Damascene, 730 and batch 9; the only John of Damascus entry is the era 4 scan's WANTED line under 216). Either add the entry before this batch merges, or say "is to be logged". CLAUDE.md requires a gap to live in the tracking file.

**A-M13 (the 730 reading).** "In the held sources, 730 is Michel Le Quien's date for the second speech". True in sense, but the held scan reads 750 (PG94 l.32112). Add "(the scan reads 750; Le Quien ties it to Germanus's fall, which Theophanes puts in 730)". See A-M8.

Checked and passing: the two census tradition names match the card's `tradition`; "the profile … quotes the same chapter of the Exposition" (IV.16, Chapter XVI "Concerning Images", NPNF9 l.36222-36279); the README's Damascus corrections (Fabricius at l.616-621, "videtur", Anastasius's "nepotem", speeches held only in Greek and Latin) and Theodore corrections ("cum ipso vixit" at l.3723, Naukratios's letter) all match the files. John is the only one of these two with a census person entry (movement 69's people list holds John only; Theodore is a `voices` line).

---

### Files opened and searches

**Files opened (cic/texts/), line ranges.**
- PG94 = `john-damascus_opera-omnia-t1-with-vita-pg94-grc-lat_migne1860.txt`: l.560-648 (Fabricius), 912-950, 4585-4600, 7160-7190, 7255-7302 (Allatius), 30210-30262, 30575-30625, 30695-30712, 31080-31112, 31870-31885, 32040-32120, 32275-32512, 32735-32750, 33005-33040, 35135-35200, 37205-37222, 89135-89165, 93170-93190; headings 87913-88098.
- NPNF9 = `npnf209_hilary-poitiers-john-damascus.xml`: l.27475-27532, 36195-36290.
- NPNF14 = `npnf214_seven-ecumenical-councils.xml`: l.39200-39210, 39440-39480.
- THEO = `theophanes-confessor_chronographia-pg108-grc-lat_migne1863.txt`: l.66236-66246, 73555-73565, 73720-73745, 74135-74152, 75190-75295, 77075-77090, 85190-85225, 87165-87180, 87760-87776, 118350-118360, 120598-120606, 121036-121044, 121705-121722.
- PG100 = `nikephoros-cp_opera-with-vita-stephani-iunioris-pg100-grc-lat_migne1860.txt`: l.88560-88592, 92330-92560.
- PG97 = `theodore-abu-qurrah_opuscula-with-andrew-crete-malalas-pg97-grc-lat_migne1860.txt`: l.490-500, 4830-4846.
- PG99 = `theodore-studite_opera-omnia-pg99-grc-lat_migne1860.txt`: l.345-380, 830-838, 3310-3330, 3592-3606, 3718-3760, 5440-5452, 5575-5590, 5630-5645, 5710-5730, 5915-5935, 6380-6392, 7700-7752, 8205-8216, 8295-8305, 8978-8990, 10135-10152, 10255-10270, 18230-18238, 18570-18610, 18680-18700, 18755-18800, 19220-19460, 20462-20560, 23820-23870, 27040-27120, 93960-93995, 155205-155262, 157420-157442, 26680-26692.
- CROSS = `russian-primary-chronicle_cross1930.txt`: l.11850-11885.
- PAT = `kievan-caves-paterik_paterik-kievskago-pecherskago-monastyria-chu_abramovich1911.txt`: l.2160-2180.
- MEYER = `athos-monasteries_haupturkunden-fur-die-geschichte-der-athoskloster-ger-grc_meyer1894.txt`: l.935-980, 1000-1050.
- Also: `charon_histoire-des-patriarcats-melkites-t2-t3-fra_1911.txt` l.21235-21245; `chamich_history-of-armenia-v2_avdall1827.txt` (Mansur hits, another man); `mansi_sacrorum-conciliorum-collectio-tomus-14…` (Studite hits, Latin only).
- Census: `cic-website/data/world-census.json`, movements[65] and [69] people and voices, and every string naming Damascus, Damascene or Studite.
- Open-Gaps: `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` (grep, and l.2140-2160).

**Searches for absences (all of cic/texts, case-insensitive).**
- John's birth and death years, and an English of the image speeches: grep for Damascen-, Damascène, "Jean de Damas", Mansur, "maker of matter", "worship not matter", and file names with damasc, icon, image, allies. No held line gives a birth or death year beyond those the card names. No English of the image speeches is held; NPNF14 l.38289 names one that is not vendored. The absences stand.
- The 787 acts on John: NPNF14 grep for Damasc and Mansur (only the 754 acclamations and Percival's notes). The council of 787's act 6 on the name is held only as Allatius quotes it (PG94 l.7276-7278); see A-M4. The records note "no 787 acclamation of John" stands as worded.
- Theodore in English: grep for studite, stoudite, studites, Studion, Stoudios across all files. English hits are Milner (l.6118), Mouravieff (l.1475, another man), NPNF14 l.38905 (a mention) and Cross. None holds his own words in English. The absence stands.
- Dates of Theodore's Lives: no held line gives a year of writing. The Sirmond preface's "qui cum ipso vixit" (l.3723) is the only dating hint and is on the card. The absence stands.

---

## Era 4 Who batch 9, round 1 review: PART B

**Scope.** cyril-and-methodius (prefix C) and clement-of-ohrid (prefix K): brief, card, audio script, records.json entry, and the README's statements about them, including the Clement "needs-ruling" note.

**Method.** I read CLAUDE.md, Who_Profile_Pattern.md, the batch README, the Rescore's "Needs-ruling Lives" paragraph and the Clement row, and the batch 8 R1 review for its form. I read every cited line range in context in the held files. I checked each quotation and each unquoted paraphrase of Latin, Greek, German and Bulgarian against its file. I diffed each audio script against its brief and ran `grade_text`. I edited no repo file.

**Audio.** Both scripts equal their briefs once `[calmly] ` (start) and `[warmly] ` (start of the last paragraph) are removed. Checklist 13 passes for both.

**Readability.** Cyril and Methodius: 405 words, FK 6.9, Flesch 71.1. Clement: 366 words, FK 6.2, Flesch 72.6. Both pass `grade_text`. Both sit below the grade-8 floor, as every approved brief in batches 7 and 9 does except Niketas (FK 8.9), so I raise no finding on it. Sentences past 25 words: C para 6 (the Salzburg sentence, 30 words; see C-B3), K para 4 (the teaching sentence, 26 words; see K-M7).

**Quotations.** Neither brief uses quotation marks. The one card quotation, Cross's "The Slavs rejoiced to hear the greatness of God extolled in their native tongue." (C card, remembered[0]), matches RPC l.7900-7901 word for word. The records' Latin quotations match their files once OCR noise is allowed for.

---

## cyril-and-methodius

**Verdict: three blocking findings (C-B1 to C-B3). Otherwise it passes with minor fixes.** The relic scene, the Legend's Rome chapters, the two papal letters and the Dümmler and Ginzel views all check out against the held lines. Word budget for the brief: the suggested brief changes below net to 0 (405 words), as tallied at the end of this section.

**C-B1 (card `legacy.remembered[2]`: Theiner's dedication misread).**
- Text: "Augustin Theiner dedicated his Vatican documents of 1863 to the thousandth-year feast of Saints Cyril and Methodius."
- Evidence: Theiner dedicates the volume to a person, Bishop Strossmayer: THEINER l.99-104 "EXCELLENTISSIMO AC REVERENDISSIMO DOMINO DOMINO JOSEPHO GEORGIO STROSSMAYER BOSNENSI SEU DIACOVENSI ET SIRMIENSI EPISCOPO"; l.125 "opus hocce, clarissimo apud omnes nomini Tuo dicatum". The feast comes only at the close, as a compliment to the bishop: l.157-160 "solemnia in memoriam millenariam sanctorum Cyrilli et Methodii, gentium Tuarum Apostolorum, quam hoc anno Ecclesia celebrat, vix opportunius et sanctius peragere ... potuisti." The bishop sponsored the work, and Theiner says it was his fitting way to keep the feast.
- Replacement: "Augustin Theiner dedicated his Vatican documents of 1863 to Joseph George Strossmayer, bishop of Bosnia or Diakovo, and wrote that the work kept the thousandth-year feast of Saints Cyril and Methodius, which the Church celebrated that year."
- Records: the claim "Theiner's dedication for the millennium feast" (THEINER l.155-158) should read "Theiner's dedication to Bishop Strossmayer, naming the work his keeping of the millennium feast (l.99-104, 125, 157-160)".

**C-B2 (card `uncertain[4]`: false absence on the prison).**
- Text: "His prison. The Life of Methodius says the king's bishops held him two and a half years in Swabia. No other source used here tells it."
- Evidence: Count Lützow, a source the card itself uses, reports the arrest: LUTZOW l.1420-1423 "The German governors seized the Archbishop Methodius, and delivered him as prisoner to his enemies the German bishops." The Life: GIN l.12346-12359 "incitavit cor hostis Moravici regis cum omnibus episcopis contra nos ... illum vero miserunt in Suevos et detinebant annos duos et dimidium". The Life's subject is "the enemy of the Moravian king, with all his bishops", so "the king's bishops" is close but loose.
- Replacement: "His prison. The Life of Methodius says the enemy of the Moravian king and all his bishops sent him to Swabia and held him two and a half years. Count Lützow says the German governors seized him and handed him as a prisoner to the German bishops. Only the Life gives the place and the length."
- Records: the "Prison in Swabia" claim is tagged Inferential-Thin with "(Life of Methodius only)". Add LUTZOW l.1420-1423 as a second witness to the arrest. Retag the arrest as Documented, and keep the place and the length as the Life's alone.

**C-B3 (brief para 6, sentence 2: a hedge dropped, and 30 words).**
- Text: "A Salzburg account of about 873 complains that a certain Greek named Methodius, with newly invented Slavonic letters, made the Latin Masses cheap in the eyes of all the people."
- Evidence: GIN l.13641-13664 "quidam graecus, methodius nomine, noviter inventis sclavinis litteris, linguam latinam doctrinamque romanam atque litteras auctorales latinas philosophice superducens, vilescere fecit cuncto populo ex parte missas et evangelia ecclesiasticumque officium illorum, qui hoc latine celebraverunt." The account says "ex parte", in part. The brief drops it and makes a partial effect total. The sentence is also the longest in the brief.
- Replacement (31 words, +1): "A Salzburg account of about 873 complains of a certain Greek named Methodius. With newly invented Slavonic letters, it says, he partly made the Latin Masses cheap to all the people."

**C-M1 (brief para 2: an undefined term, and "Johann Ginzel" placed after it).**
- Text: "The finding is told in the Italian Legend. Johann Ginzel, who trusts it, follows the Bollandists in tracing it to Gauderich of Velletri, a bishop of the brothers' own time."
- Evidence: "Italian Legend" is Ginzel's own name for the translatio S. Clementis: GIN l.1468-1469 "Diese Legende, welche ich nach ihrem Vaterlande die italische nenne". A listener does not know what the Italian Legend is. Ginzel's hedge is that the Bollandists make it "very probable" (l.1457-1459, "machen es sehr wahrscheinlich, dass dieser Bericht von dem Bischofe Gauderich oder Gaudentius von Velletri herrühre").
- Replacement (32 words, +2): "The finding is told in what Johann Ginzel calls the Italian Legend. He trusts it, and follows the Bollandists in tracing it to Gauderich of Velletri, a bishop of their own time."
- Card `uncertain[0]`: change "which he and the Bollandists trace to Gauderich of Velletri" to "which the Bollandists, as Ginzel follows them, think very probably the work of Gauderich of Velletri".

**C-M2 (brief para 4: a partisan witness not marked; "Machwerk" softened).**
- Text: "Ginzel calls it the work of a Greek schismatic."
- Evidence: GIN l.1589-1592 "muss die pannonische Legende vielmehr als das Machwerk eines griechischen Schismatikers bezeichnen, der es darauf angelegt hat, seiner Erzählung das Gepräge zu geben, als rühre sie von einem Zeitgenossen des Methodius her". "Machwerk" is a concoction, not a neutral "work". Ginzel's polemic is open: GIN l.1704-1707 says the Greeks have always sought their weapon "in der Kunst der Täuschung und Fälschung". Checklist 6 wants a partisan witness placed once and marked as partisan. The Clement card already does this ("Ginzel, who writes against the Greek schism").
- Replacement (12 words, +3): "Ginzel, who writes against the Greek schism, calls it a schismatic's concoction."

**C-M3 (brief para 6: the 879 ban was a repeat).**
- Text: "In 879 Pope John VIII forbade him to sing the Mass in Slavonic."
- Evidence: GIN l.13797-13802 (also MANSI 17-18 l.14044-14048) "Audimus etiam, quod missas cantes in barbara, hoc est in sclavina lingua. Unde iam litteris nostris, per Paulum episcopum Anconitanum tibi directis prohibuimus". The 879 letter recalls an earlier ban sent through Paul of Ancona. It also allows preaching in Slavonic ("Predicare vero ... tibi licet").
- Replacement (14 words, +1): "In 879 Pope John VIII repeated his ban on singing the Mass in Slavonic."

**C-M4 (card `uncertain`: a held conflict missing; brief para 3 told on one witness).**
- The brief's "After four and a half years they left behind all the books the church needed" is the Legend's figure (GIN l.11422-11424 "Manserunt ergo in Moravia per annos quatuor et dimidium"). The Life of Methodius gives three (GIN l.12220-12221 "Ac tribus annis elapsis reversi sunt ambo ex Moravia"). Ginzel names the conflict and rules for the Legend (GIN l.3245-3249 "Unrichtig ist die Angabe der pannonischen L. c. 5: Ac tribus annis ..."). The brief's "the Legend says" covers the sentence before it, so the brief can stand. The card should carry the conflict.
- Add to `uncertain`, after "Who made them bishops": "How long they stayed in Moravia. The Italian Legend says four and a half years; the Life of Methodius says three. Ginzel follows the Legend and calls the Life wrong."
- Add the same pair to records `contested_claims`.

**C-M5 (card `knownFor`: two precision points).**
- Text: "Two brothers of Thessalonica who took the faith to the Slavs of Moravia in their own language. Pope John VIII praised the Slavonic letters found by Constantine and, in 880, allowed the Mass to be sung in Slavonic."
- Evidence: (a) Every held account has the Moravians already Christian or turning to Christ before the brothers came. The Legend (GIN l.11397-11398): "ab idolorum quidem cultura recesserat, et christianam legem observare desiderabat". The Life (GIN l.12202-12204): "intraverunt ad nos doctores multi christiani ex Italia et ex Graecia et ex Germania". Cross's Chronicle (RPC l.7884): "Our nation is baptized". (b) The 880 permission carries a condition: GIN l.13983-13986 "Jubemus tamen, ut in omnibus ecclesiis terrae vestrae propter majorem honorificentiam evangelium latine legatur et postmodum sclavinica lingua translatum ... adnuncietur".
- Replacement: "Two brothers of Thessalonica who taught the Slavs of Moravia the faith in their own language. Pope John VIII praised the Slavonic letters found by Constantine and, in 880, allowed the Mass to be sung in Slavonic, with the Gospel read first in Latin."

**C-M6 (brief para 5: "home" for "their monastery").**
- Text: "Methodius asked to take his body home, since their mother had begged them with tears to do so if one died abroad."
- Evidence: GIN l.11486-11490 "mater cum multis lacrymis obtestata est, ut si aliquem ex nobis, antequam reverteremur, obiisse contingeret, defunctum fratrem frater vivens ad monasterium suum reduceret".
- Replacement (20 words, -2): "Methodius asked to take his body back to their monastery, as their mother had tearfully begged if one died abroad."

**C-M7 (card `place`).**
- Text: "Pannonia, where Methodius was made bishop".
- Evidence: in the Life he is ordained in Rome, at Kocel's request, for the see of Saint Andronicus in Pannonia: GIN l.12321-12323 "iterum misit eum ad apostolicum ... ut illum ordinaret episcopum in Pannonia in sedem sancti Andronici apostoli".
- Replacement: "Pannonia, the see Methodius was made bishop for, by the Life of Methodius".

**C-M8 (card `legacy.traces[1]`: one term for two texts).**
- Text: "The Life of Clement of Ohrid names Gorazd, Clement, Naum, Angelarius and Sava as Methodius's chief disciples."
- Evidence: GIN l.12650-12661: they are chief among those who drank "ex eorum doctrinae fonte", the teaching of both brothers. The Clement card's traces[2] says "the chief disciples of Cyril and Methodius".
- Replacement: "The Life of Clement of Ohrid names Gorazd, Clement, Naum, Angelarius and Sava as the brothers' chief disciples."

**C-M9 (card `dates`: the Life's year is an annus mundi).**
- Text: "Methodius died on 6 April 885, by the Life of Methodius".
- Evidence: GIN l.12536-12541 "sexta die mensis Aprilis tertia indictione ... millesimo trecentesimo nonagesimo tertio". Ginzel restores "sexies" and works out 885 (GIN l.6187-6205). The brief's "the sixth of April 885, the Life says" is fine as spoken narration.
- Replacement: "Methodius died on 6 April, in the year 6393 from the creation, by the Life of Methodius; Ginzel works this out as 885".

**C-M10 (brief para 4: placement of the revelation; optional).**
- The Life sets the revelation of the letters in Constantinople, before the journey (GIN l.12216-12219 "Ibique manifestavit Deus philosopho Slovenicas litteras, et illico ... iter aggressus est Moravicum"). Told after the four and a half years, it can sound later. Replacement if the budget allows (+3): "A Life of Methodius says God revealed the Slavonic letters to the Philosopher before they set out."

**C-M11 (records citation).** The claim "Ginzel ... follows the Bollandists in tracing it to Gauderich" cites GIN l.1490-1505. Those lines describe the Moravian Legend (item 2). The Bollandist and Gauderich passage is at l.1452-1475.

**Word budget for the C brief.** The changes above add 7 words: C-B3 +1, C-M1 +2, C-M2 +3, C-M3 +1. C-M6 saves 2. These cuts, which lose no fact, save the other 5:
- para 4: "Ernst Dümmler thought one of Methodius's pupils wrote it soon after his death." becomes "Ernst Dümmler thought a pupil of Methodius wrote it soon after his death." (-1)
- para 5: "There Constantine took the name Cyril, and he died forty days later, on the fourteenth of February." becomes "There Constantine took the name Cyril and died forty days later, on the fourteenth of February." (-1)
- para 6: "The next year, after examining him in Rome, the pope wrote to Svatopluk, prince of Moravia." becomes "In 880, after examining him in Rome, he wrote to Svatopluk, prince of Moravia." (-3; the date is GIN l.13877 "Mense Junio, 880")

Net 0, so the brief stays at 405. C-M10, if taken, needs 3 more words cut.

---

## clement-of-ohrid

**Verdict: three blocking findings (K-B1 to K-B3). Otherwise it passes with minor fixes.** The prison scene, the expulsion, the raft, Boritakan, Kutmichevitsa, the 3,500 pupils, the sermons, Symeon's refusal, the Triodion and the closing prayer all check out against PG126. The authorship dispute is told in place and repeated first in the card's uncertain list. Word budget: the suggested brief changes net to +4 (370 words), within "about" 365; the tally is at the end of this section. (Some line numbers inside long cited ranges are given to within a line or two of the OCR line where the words sit.)

**K-B1 (brief para 2, card `uncertain[0]`, records `contested_claims`, README: a held Migne dating left out of the authorship dispute).**
- Text (brief): "Migne's editors leave it to the reader." Card: "Migne's editors leave it to the reader." README l.25: "Migne's editors leave it to the reader."
- Evidence: the PG 126 Monitum does end "Sed judicium penes Lectorem sit" (PG126 l.96745). But Migne's own Patrologia Graeca 111, which is held, lists the Life as anonymous, of the mid-tenth century, and ascribed to Theophylact only "by some". NICHOLAS-MYSTIKOS PG111 l.244-245: "ANONYMUS. Vita S. Clementis Bulgarorum episcopi (exstat tom. CXXVI, in appendice ad Theophylactum, cui a nonnullis tribuitur)"; l.36943-36947: "ANONYMI VITA S. CLEMENTIS BULGARORUM EPISCOPI. Exstat in Appendice ad Theophylactum, tom. CXXVI. CIRCA MEDIUM SECULUM X." That is a second held Migne placing, which dates the Life to about 950. It bears directly on the README's open ruling about whether the Life is early enough. Found by a proximity search over all of cic/texts for Clement forms near Bulgar/Ohrid/Gorazd forms.
- Replacement (brief, 15 words, +8): "One Migne volume leaves it to the reader; another dates it to the mid-tenth century."
- Replacement (card `uncertain[0]`): replace "Migne's editors leave it to the reader." with "Migne's editors leave it to the reader in Patrologia Graeca 126, but in volume 111 they list the Life as anonymous, from about the middle of the tenth century, and ascribed to Theophylact only by some."
- Card `sources.about`: add Patrologia Graeca 111 (contents and placing note), Migne, 1863, Latin, `cic/texts/nicholas-mystikos_epistolae-with-eutychius-alexandrinus-pg111-grc-lat_migne1863.txt`.
- Records: add a side "Migne, PG 111: anonymous, circa medium saeculum X (PG111 l.244-245, l.36943-36947)" to the contested claim on the author and date.
- README l.25 (Who the sources are, Clement): after "and Migne's editors leave it to the reader", add "in PG 126, while Migne's PG 111 lists it as anonymous, of about the middle of the tenth century". The Rescore row and the "Needs-ruling Lives" paragraph do not cite PG 111 either. The coordinator should carry this to Mark's ruling, since it is a held statement that dates the Life, of the kind that paragraph says answers a needs-ruling flag.

**K-B2 (card `uncertain[0]`: a sourcing statement the card contradicts).**
- Text: "Every detail on this card comes from this one Life."
- Evidence: the same card gives Ginzel's 886 (dates, uncertain[3]), Nikodemos's Saint Panteleimon and the tablets of Moses (remembered[1]), and Paisii's seven teachers (remembered[2]), none of them from the Life.
- Replacement: "Every detail of his life on this card comes from this one Life, except the year 886, which is Ginzel's, and the dedication to Saint Panteleimon, which is Nikodemos's."

**K-B3 (brief para 6, card `dates`, records: the date is the burial's).**
- Text (brief): "Clement fell ill, finished the hymns sung from the Sunday after Easter to Pentecost, and died on 27 July 916." Card: "Died 27 July 916, by his Life".
- Evidence: PG126 l.100258-100267: "ad Dominum migravit. Ipsius autem divinum corpus ... in monasterii monumento ... repositum est, Julii mensis vigesimo septimo die, regnante Symeone in Bulgaria, anno sexies millesimo quadringentesimo vigesimo quarto a creatione mundi." The day and year are given for the burial. The year of death, 916, is the Monitum's ("anno 916 defuncti", l.96726) and Miklosich's ("mortuo 916", GIN l.1680).
- Replacement (brief, 0 words): "Clement fell ill, finished the hymns sung from the Sunday after Easter to Pentecost, and was buried on 27 July 916."
- Replacement (card `dates`, first sentence): "Buried 27 July in the year 6424 from the creation of the world, under Symeon, by his Life; Migne's editors give 916 as the year of his death."
- Records: the claim already reads "buried in his monastery 27 July"; no change.

**K-M1 (brief para 2 and card `uncertain[0]`: the heading's title).**
- Text: "Its heading names Theophylact, archbishop of Ohrid, who died in 1107."
- Evidence: PG126 l.96785-96788 "archiepiscopus primae Justinianae ac totius Bulgariae Dominus THEOPHYLACTUS, qui Constantinopoli magister rhetorum fuit". The heading does not name Ohrid. Ginzel calls him "Metropoliten von Achrida" (GIN l.1659-1660), so "Theophylact of Ohrid" as a name is sound.
- Replacement (brief, +1; card the same wording): "Its heading names Theophylact, archbishop of all Bulgaria, who died in 1107."

**K-M2 (brief para 5: chronology of the monastery).**
- Text: "At Ohrid he built a monastery, and a church that later became the archbishop's seat."
- Evidence: PG126 l.99597-99606 "Deposuerat haec omnia in monasterio, quod in Achride construxerat, adhuc superstite beatissimo Borise, priusquam Velitzae episcopatum suscepisset ... cui etiam alteram adjecit ecclesiam, quae postea archiepiscopatus sedes constituta est." The monastery came before the bishopric. Placed after it, the sentence reads as later.
- Replacement (19 words, +4): "At Ohrid, while Boris still lived, he built a monastery, and a church that later became the archbishop's seat."

**K-M3 (card `uncertain[0]`: Miklosich's hedge).**
- Text: "and that Theophylact's name was added".
- Evidence: GIN l.1690-1691 (also PG126 l.96730-96731): "nomen vero Theophylacti additum esse videtur, quo major fides et auctoritas narrationi conciliaretur".
- Replacement: "and that Theophylact's name seems to have been added to give the story weight".

**K-M4 (card `dates`: Ginzel's reckoning).**
- Text: "Johann Ginzel reckons the expulsion from Moravia to 886, counting back from the Life's own years".
- Evidence: GIN l.6380-6386. Ginzel counts the Life's seven years back from 893, when Symeon is first named ("dass ... Symeon zuerst im J. 893 erwähnt wird; rechnen wir also von hier aus sieben Jahre zurück, so erhalten wir 886"). The anchor, 893, is his own and not the Life's.
- Replacement: "Johann Ginzel reckons the expulsion from Moravia to 886, counting the Life's seven years back from 893, when Symeon is first named".

**K-M5 (card `legacy.traces[0]`: two statements fused, one order dropped).**
- Text: "The Life says his pupils numbered 3,500, and that in each district 300 of them, ordained as readers, deacons and priests, took his orders."
- Evidence: PG126 l.99242-99244 "Habens quosdam ex aliis delectos in unaquaque dioecesi non paucos, ad tria enim millia et quingentos numerabantur"; l.99268-99271 "Ex illis lectores, subdiaconos, diaconos, et presbyteros ordinat. In unaquaque dioecesi trecentis jussa dabat discipulis". These are two separate statements, and the list includes subdeacons.
- Replacement: "The Life says he had 3,500 picked pupils, ordained readers, subdeacons, deacons and priests from among them, and in each district gave orders to 300 of them."

**K-M6 (card `legacy.remembered[1]`: a late witness not marked late).**
- Text: "Nikodemos the Hagiorite's book of saints says ..."
- Evidence: the records call it late (records claim "Nikodemos ... (late)"; absent_details "Nikodemos's Moesia is late"). NIK l.32789-32795 also departs from the Life: it says Methodius made Clement bishop of all Illyricum, and (l.32817-32820) that Clement baptized Boris. The card should mark the book as a much later witness.
- Replacement (opening): "Nikodemos the Hagiorite's book of saints, a much later work, says ..." (the rest unchanged).

**K-M7 (brief para 4: a 26-word sentence).**
- Text: "He showed some children the shapes of the letters, explained Scripture to others, and shaped others' hands for writing, by night as well as by day."
- Evidence: PG126 l.99252-99256 "aliis litterarum characterem monstrans, aliis scripturarum sensum illustrans, aliis ad scribendum manus efformans, et hoc non solum die, sed etiam nocte".
- Replacement (20 words, -6): "He showed some children their letters, explained Scripture to others, and shaped others' hands for writing, by night and day."

**K-M8 (brief para 1: the office named).**
- Text: "They kept the hours of prayer and sang psalms."
- Evidence: PG126 l.98417-98419 "canticis tertiae horae decantatis, psalmorum prosequebantur carmen". The Life names one office, the Third Hour.
- Replacement (0 words): "They sang the Third Hour's hymns, then the psalms."

**K-M9 (brief para 5: optional trim to fund K-B1 and K-M2).**
- "Symeon, the first to be called king of the Bulgarians, made him bishop of Dremvitsa, also called Velitsa." becomes "Symeon, the first to be called king of the Bulgarians, made him bishop of Dremvitsa." (-3; the card's place and role fields keep "also called Velitsa").

**Word budget for the K brief.** The changes add 13 words: K-B1 +8, K-M1 +1, K-M2 +4. K-B3 and K-M8 add none. K-M7 saves 6 and K-M9 saves 3. Net +4, giving 370 words, about 2:17, inside "about 2:15". If that is too long, drop "Old now," from para 6 (-2).

---

## README statements on these two

**R-1 (l.25 and the needs-ruling note).** See K-B1. The README and the Rescore leave Clement's Life undated in Migne. A held Migne volume (PG 111) dates it about the middle of the tenth century and calls it anonymous. This does not settle the Miklosich-Ginzel dispute. It is a third held placing, and Mark should see it when he rules on "early enough".

**R-2 (l.32, the Clement correction).** "The Monitum ... reports Miklosich's argument and leaves the judgment to the reader; it does not argue it in its own voice." Confirmed at PG126 l.96731-96746 ("fidem omnem negat novissimus Editor Vindobonensis ... putat. ... inquit ... Sed judicium penes Lectorem sit"). So the Rescore row's "the Monitum argues a 10th-c. contemporary" is the error, and the README is right to correct it. "The Saint Panteleimon dedication is not in the Life": confirmed. The Life's Ohrid passage (PG126 l.99597-99606) names no dedication.

**R-3 (l.21 and l.31, Cyril and Methodius).** Confirmed: the Salzburg account at GIN l.13125-13722, with the Methodius passage at l.13641-13664; Industriae tuae at GIN l.13870-13986, which the README gives as l.13878-13982. "No held line names Methodius's jailer or calls him 'of Sirmium'": confirmed by a search for Hermanric, Ermanric, Ermenric and Sirm* near Methodi* in Ginzel, Mansi 17-18 and Lützow. The README's "Pope John VIII's letters of 879 and 880" is accurate. Mansi 17-18 also holds a later letter to Methodius (l.20827, "CCLXVIII. Ad Methodium archie[piscopum]"), unused. That is not a defect.

**R-4 (l.9).** "Clement's life rests on one Life": accurate for the life. The card's late witnesses (Nikodemos, Paisii) add remembrance only; see K-B2 for the card's own wording.

---

## Files and line ranges opened

- GIN = ginzel_geschichte-der-slawenapostel-cyrill-und-method-deu-lat_1861.txt: l.1120-1200, 1430-1720, 1740-1830, 2885-2916, 3240-3250, 3600-3630, 6160-6210, 6330-6392, 11225-11335, 11390-11600, 12200-12240, 12300-12365, 12462-12490, 12490-12550, 12650-12665, 13125-13140, 13636-13668, 13770-13810, 13870-13990.
- PG126 = theophylact-ohrid_opera-t4-with-vita-clementis-pg126-grc-lat_migne1864.txt: l.96715-96800, 98270-98460, 98660-98700, 98940-99015, 99088-99125, 99236-99380, 99440-99640, 99820-99935, 100225-100290, 100490-100560.
- PG111 = nicholas-mystikos_epistolae-with-eutychius-alexandrinus-pg111-grc-lat_migne1863.txt: l.200-250, 36925-36950.
- RPC = russian-primary-chronicle_cross1930.txt: l.5645-5675, 7860-7935.
- THEINER = theiner_vetera-monumenta-slavorum-meridionalium-v1-lat_1863.txt: l.95-170.
- LUTZOW = lutzow_bohemia-historical-sketch_1920.txt: l.1325-1345, 1395-1432.
- NIK = nikodemos-hagiorite_synaxaristes-vol1-sep-feb-grc_1900.txt: l.32780-32880, and the 22 November heading.
- PAI = paisii-hilendarski_istoriia-slavianobolgarskaia-bul_ivanov1914.txt: l.1-10, 6660-6690.
- MANSI 17-18 = mansi_sacrorum-conciliorum-collectio-tomus-17-18-lat_welter-facsimile1902.txt: l.13940-14060, plus grep hits at l.13898, 19085-19165, 20827.
- Batch files: README.md, both briefs, cards, audio scripts and records entries. Rescore.md l.20-60, l.141-213.

## Searches run for absences

- All cic/texts for Methodi* co-occurring with Moravi/Sclav/Slav/Pannoni/Svatopluk forms, to find second witnesses. This led to Lützow on the arrest (C-B2) and confirmed Mansi 17-18's John VIII letters.
- Lützow, RPC and Ginzel (codex part) for prison, imprison, captiv, Swabia, carcer, Suev.
- Mansi 17-18 for Hermanric, Ermanric, Ermenric, Pataviens, Frisingens, Adalwin and Sclavin forms. No letter on Methodius's detention is held, and no jailer is named.
- All cic/texts (Python proximity scan, 250 characters) for Clemens/Clement/Kliment/Климент/Κλήμ- within reach of Bulgar/Βουλγ/Болгар/Achrid/Ohrid/Охрид/Velitz/Gorazd forms, outside the four known files. Hits were checked in Theiner, Mansi 17-18, Propaganda Fide, PG111 and the Vita Euthymii. Only PG111 bears on Clement of Ohrid (K-B1). The others are other Clements, popes, or index lines. No sermon or hymn of Clement is held, which confirms the records' absent_details.
- Ginzel for 863 and 886, to check the card's dates.

---

## Era 4 Who batch 9, round 1 review: PART C

**Scope.** `antony-and-theodosius-of-the-kyiv-caves`, `anskar`, `rimbert` (brief, card, audio script, records.json entry each), and the whole batch `README.md`, including its river counts of majors against `laneLabel` in `cic-website/data/world-census.json` and the tradition placing of the Kyiv pair, checked against `Build/Ministry/Operations/Audits/2026-11-14_who-rescore-eras4-5/Rescore.md`.

**Method.** I read CLAUDE.md, `Who_Profile_Pattern.md`, the first 120 lines of the era 4 batch 8 R1 review, and the batch README. I opened every cited line range and read it in context, with OCR noise allowed for. I checked each quotation against its file. I diffed each audio script against its brief. I ran `engine.m1.gates.grade_text` and counted words. I searched for absences across all of `cic/texts`. I edited no repo file. Suggested brief replacements were test-applied to scratch copies only, to check word counts and grades.

**Abbreviations.** CROSS = `russian-primary-chronicle_cross1930.txt`; PAT = `kievan-caves-paterik_paterik-kievskago-pecherskago-monastyria-chu_abramovich1911.txt`; MOUR = `mouravieff_history-of-the-church-of-russia_blackmore1842.txt`; ROB = `rimbert_anskar-the-apostle-of-the-north_robinson1921.txt`; WAITZ = `rimbert_vita-anskarii-accedit-vita-rimberti-lat_waitz1884.txt`; ADAM = `adam-bremen_gesta-hammaburgensis-ecclesiae-pontificum-lat_schmeidler1917.txt`; STEIN = `adam-bremen_hamburgische-kirchengeschichte-deu_steinberg1926.txt`; ANNBERT = `prudentius-troyes_annales-bertiniani_waitz1883.txt`; RFA = `annales-regni-francorum_kurze1895.txt`; MANSI14 = `mansi_sacrorum-conciliorum-collectio-tomus-14-lat_welter-facsimile1902.txt`; OP = `olavus-petri_samlade-skrifter-v1-swe_hesselman1914.txt`.

**Quotations.** Every quotation in the three briefs and cards matches its file word for word, once OCR noise is allowed for: ROB l.2652 "cloakf", ROB l.5596 "sixty-fourth*", and the running head plus stray quote mark inside CROSS l.11855-11860 ("Let him be ‘your prior.”’"). Two quotes end on a full stop where the source runs on with a comma: "Oh Lord, strengthen me in this place." (CROSS l.11777, comma, then "and may there rest...") and "Change not the traditions and the institutions of the monastery." (CROSS l.12665, comma, then "but follow..."). Those are acceptable truncations.

**Audio.** All three scripts equal their briefs with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph only (scripted diff, exact match). Checklist 13 passes.

**Scores.**
| id | words | FK | Flesch |
|---|---|---|---|
| antony-and-theodosius-of-the-kyiv-caves | 401 | 5.96 | 72.44 |
| anskar | 405 | 6.25 | 77.64 |
| rimbert | 366 | 5.97 | 80.35 |

All three pass `grade_text`. Rimbert is one word over the 365-word limit for a non-major (R-M1).

---

## antony-and-theodosius-of-the-kyiv-caves

**Verdict: one blocking finding (K-B1). Otherwise passes with minor fixes.** The opening scene, the Chronicle quotes, the 1073 rebuke, the death and the close are all sound. The dispute list on the card is good, but it misses the largest difference between the two sources.

**K-B1 (card `knownFor`; records: a contested point told as settled and missing from `uncertain` and `contested_claims`).**
- The card says: "Theodosius, whom he chose as prior, built the monastery above ground and gave it the rule of the Studion monastery of Constantinople."
- That is Nestor's Life. The Chronicle gives the first church, palisade and cells on the hill to the brothers under Barlaam, the first prior, before Theodosius took over. Evidence: CROSS l.11826-11834: "When Izyaslav heard these words, he rejoiced ... and gave to them the hill. The prior and the brethren founded there a great church, and fenced in the monastery with a palisade. They constructed many cells ..."; l.11840: "Now when the monastery was completed during the priorate of Barlaam". PAT l.1166-1173 (the Paterik's seventh discourse, headed as Nestor's) agrees with the Chronicle: "Игуменъ же и брала заложиша церковь велику и монастырь, оградиша столпемь".
- Nestor's Life says Theodosius built the church and cells and moved the brothers in 6570 (PAT l.2162-2168).
- S. H. Cross sets out the difference himself. Evidence: CROSS l.4635-4640: "in Nestor's account, Barlaam constructed only the one small surface church before his transfer to St Demetrius' ... The new prior, finding the previous quarters too small, selected a location not far from the old crypt, where he built a large church ... together with numerous cells."
- The brief's para 7 says "by Nestor's account", so the brief is safe. The card and records are not.
- Fix, `knownFor`: "The founders of the Caves monastery of Kyiv. Antony, made a monk on Mount Athos, lived in a cave on a hill outside the city, and the brothers who gathered to him chose Theodosius as prior on his word. Theodosius gave the house the rule of the Studion monastery of Constantinople."
- Fix, add to `uncertain` after the Studite-rule item: "Who built the monastery above ground. The Chronicle says the brothers under Barlaam, the first prior, built the church, cells and palisade on the hill Prince Izyaslav gave them. Nestor's Life says Theodosius built them and moved the brothers there in 1062. S. H. Cross points out the difference."
- Fix, records: add a `contested_claims` entry: claim "Who built the monastery above ground"; sides "Chronicle: the brothers under Barlaam, before Theodosius (CROSS l.11826-11841; PAT l.1166-1173, the seventh discourse)" and "Nestor's Life: Theodosius, moving in 6570 (PAT l.2162-2168)"; with Cross's note (CROSS l.4635-4640). Tag the 6570 claim "Contested" in place of "Documented", or keep "Documented" for the words and add the contested_claim.

**K-M1 (brief para 5: Barlaam is skipped, so Theodosius sounds like the first prior).**
- "Wanting to live alone, he moved to another hill. When the brothers asked him for a prior, he answered, 'Who among you ...'"
- In the Chronicle, Antony named Barlaam prior when he moved away. The brothers asked for a new prior only when Izyaslav took Barlaam to Saint Demetrius. Evidence: CROSS l.11797-11799: "So he appointed Barlaam as their prior, and betook himself to the hill"; l.11849-11852: "When Barlaam had departed to St Demetrius', the brethren ... visited the ancient Antonius with the request that he should designate them a new prior."
- Fix (all four Kyiv brief fixes K-M1 to K-M4 together keep the brief at 405 words, FK 5.91, Flesch 72.40, tested on a scratch copy): "He named Barlaam their prior and moved alone to another hill. When Barlaam left, the brothers asked Antony for another. He answered, ..." To make room, para 5's "His prior sent him home to Rus, so that other monks might follow his example." becomes "His prior sent him home to Rus, as an example to other monks."

**K-M2 (brief paras 5, 7, 13 and card `role`: "prior" and "abbot" for one office; checklist 9).**
- The brief quotes Cross's "Let him be your prior", then says "As abbot, the Chronicle says" and "Stephen, the next abbot". Cross says "prior" each time. Evidence: CROSS l.11861 "to be their prior"; l.12657 "appointed Stephen to be their prior". A listener hears two offices.
- Fix: "As prior, the Chronicle says, he gathered a hundred monks." and "He told Stephen, the next prior, ..." Card `role`: "Monks and founders: Antony, hermit of the cave; Theodosius, its prior".

**K-M3 (brief para 9: who sent Antony to Chernigov).**
- "Later Izyaslav turned against Antony, and Antony fled by night to Chernigov". The Chronicle says Svyatoslav had him escape, after Izyaslav came back from Poland angry with him over Vseslav. Evidence: CROSS l.12855-12858: "Izyaslav returned from Poland, and was angry with Antonius on account of Vseslav, so that Svyatoslav caused Antonius to escape by night to Chernigov."
- Fix: "Later Izyaslav grew angry with Antony, and Prince Svyatoslav sent him away by night to Chernigov, where he dug another cave." Then para 11 opens "In 1073 Svyatoslav drove his brother Izyaslav out of Kyiv.", since "Prince" has moved to the first mention.

**K-M4 (brief para 11: two princes sent the invitation, not one).**
- "Nestor says Svyatoslav invited Theodosius to dinner". The Life has the two brothers who had driven out Izyaslav send for him. Evidence: PAT l.3586-3590: "двоима братома брань сътворити на единаго старийшаго ихъ брата ... И онѣмь пришедшимь въ градъ той, посылають же по блаженнаго отца нашего Феодосия, зовуще того прийти к нимъ на обѣдъ".
- This is a small precision, and the letter that follows is to Svyatoslav alone. Fix, if the fixer wants it without a length cost: "Nestor says the two princes invited Theodosius to dinner". Otherwise leave it.

**K-M5 (card `uncertain[4]` and `uncertain[5]`: "Nestor" means two different texts).**
- `uncertain[4]`: "Nestor says he sent a brother to Ephraim the eunuch". The Paterik heads its seventh discourse, the founding account, as Nestor's too, and that discourse gives the Chronicle's Michael. Evidence: PAT l.1038-1039: "Нестера, мниха обители монастыря Печерьскаго, сказание что ради прозвася Печерьскый монастырь. Слово 7-ое."; PAT l.1230-1233: the monk Michael of the Studion, who had come with Metropolitan George.
- The same discourse ends with the narrator, named "Nesterь", saying Theodosius received him at seventeen (PAT l.1239-1241: "придохъ же азъ к нему, худый и недостойный рабъ Нестерь, и приятъ мя, тогда ми лѣт сущу 17"). That is what Mouravieff's "eye-witness" rests on (MOUR l.1617-1622, "entered himself into its retirement in the seventeenth year of his age"). Cross reads the same words in the Chronicle as one writer's and Nestor's own statement in the Life as another's (CROSS l.4651-4679).
- Fix, `uncertain[4]`: "Where the Studite rule came from. The Chronicle, and the Paterik's founding account headed as Nestor's, say Theodosius copied it from Michael, a Studite monk in Kyiv. Nestor's Life says he sent a brother to Ephraim the eunuch in Constantinople for it."
- Fix, `uncertain[5]`, last sentence: "Cross also says Nestor, by his own statement in the Life, did not know Theodosius and entered the monastery after his death. The Paterik heads its founding account as Nestor's, and there the writer says Theodosius received him at seventeen; A. N. Mouravieff, on that ground, calls Nestor an eyewitness."

**K-M6 (card `legacy.remembered[1]`: Theodosius's own words given to Nestor).**
- "Nestor's Life calls Theodosius a man who rebuked the prince for the salvation of his soul." In the Life it is Theodosius who says this, to Svyatoslav. Evidence: PAT l.3697-3698: "Но се подобаеть намъ обличати и глаголати вамъ, еже на спасение души".
- Fix: "In Nestor's Life, Theodosius tells Svyatoslav that a monk must rebuke a prince for the salvation of his soul. Svyatoslav came to the monastery and said he had not dared to come while the abbot was angry with him."

**K-M7 (card `otherNames[1]`: a form no held source spells).**
- "Antony of the Caves; Theodosius of the Caves". The records' own absence note shows these forms were searched for and not found. What the Paterik spells is the epithet: PAT l.1034: "отецъ нашихъ Печерьскыхъ Антония и Феодосия".
- Fix: "Antony and Theodosius Pecherskii (\"of the Caves\"), the Paterik's form", or drop the line.

**K-M8 (brief para 3 and card: Nestor has no identifier; checklist 8).**
- "and in Nestor's Life of Theodosius." The Life's heading gives him one. Evidence: PAT l.1250: "Списано Нестеромъ, мнихомъ того-же Печерьскаго монастыря".
- Fix, brief: "and in the Life of Theodosius by Nestor, a monk of the same house." This also splits the 26-word sentence: "Their story is told in the Russian Primary Chronicle. Sylvester, prior of Saint Michael's, says he wrote it in 1116. It is also told in the Life of Theodosius by Nestor, a monk of the same house." That adds about 9 words, so apply it only with a matching cut, or apply the identifier on the card alone (`dates`: "Nestor, a monk of the Caves, dates the move above ground to 1062.").

**Note (not a finding).** I searched the Paterik, the Laurentian text, Cross and Mouravieff for a death year for Antony. None gives one; CROSS l.12916 has only "Antonius was already dead". The absence holds. "Antony" in para 1 is anchored by Kyiv and the cave, and the who-line follows two sentences later. I accept that as the first mention.

---

## anskar

**Verdict: two blocking findings (N-B1, N-B2). Otherwise passes with minor fixes.**

**N-B1 (brief para 7: a contested date told from one side, with a dropped hedge and a dropped detail).**
- "Waitz and Robinson date the sack of Hamburg to 845. The Annals of Saint-Bertin say that in 845 Horic, king of the Northmen, sent 600 ships up the Elbe, and Waitz thinks the city they then took was Hamburg. Yet Anskar later visited Horic often ..."
- The card and records carry a contested claim on the year (Adam of Bremen: the last year of Louis the Pious). The brief gives only one side, which goes against checklist 7 and "disputes in place". Evidence: ADAM l.5454-5455: "Hoc, ut aiunt, factum est anno Ludvici senioris novissimo."; WAITZ l.2016-2017: "Minus recte Adamus I, 23. extremum annum Ludovici Pii (839/40) indicat".
- Robinson's date is hedged: ROB l.2665-2667: "the date given by Lambecius ... i.e., 845, is probably correct".
- The annal does not say the Northmen took Hamburg. It says the Saxons beat them, and then they took "a certain city of the Slavs". Waitz's note only "seems" to see Hamburg in it. Evidence: ANNBERT l.2177-2181: "Quibus Saxones occurrentes, commisso praelio ... victores efficiuntur. Unde digressi, Sclavorum quandam impetunt et capiunt civitatem¹"; l.2203: "Hamburgum innuere videtur". "Yet" then leans on an identification the sources hedge.
- Fix, para 7 (with the cuts listed under N-M1 the brief stays at 405 words, FK 6.03, Flesch 78.26, tested on a scratch copy): "The Annals of Saint-Bertin say that in 845 Horic, king of the Northmen, sent 600 ships up the Elbe. Then they took a city of the Slavs, which Waitz thinks was Hamburg. Adam of Bremen put the sack in the emperor Louis's last year, as others told it. Anskar later visited Horic often, became his friend and counselor, and won leave to build a church at Schleswig."
- Card `uncertain[1]` should keep Robinson's hedge: "Waitz, Bernhard Schmeidler and Sigfrid Steinberg give 845, and C. H. Robinson thinks it probably correct. Adam of Bremen, 'as they say', puts it in the last year of Louis the Pious, 839 or 840." (STEIN l.3710: "Die Zerstörung Hamburgs erfolgte 845, nicht wie Adam will, 839/40".)

**N-B2 (card `dates`; records claim and absent_details: Robinson misread on the birth).**
- The card says: "Born about 801, by C. H. Robinson's count back from the Life's 'sixty-fourth year of his age'; Robinson says the true date of his birth is unknown."
- Robinson states the year flatly. His "unknown" is about the day, since 8 September is the day the body was moved. Evidence: ROB l.1295-1298: "Anskar was born in 801. The date September 8th sometimes given as his birthday was the date of the translation of his body to the church of St. Peter, at Bremen ... The actual date of his birth is unknown."
- The count back is not shown in Robinson. His footnote on "sixty-fourth" says only "See chap. iii." (ROB l.5596, 5765). The card's "about" and "count back" are the drafter's inference, put in Robinson's name.
- The records' absent_details note, "Birth date ... No held source gives them; Robinson says so", is wrong for the year.
- Fix, card `dates`: "Born in 801, C. H. Robinson says; the Life puts his last illness in his sixty-fourth year. Robinson adds that the day of his birth is unknown: 8 September, sometimes given, was the day his body was moved at Bremen. Died 3 February 865, by Adam of Bremen and the Annals of Corvey; the Life gives no year or day, as Georg Waitz notes. The Danish mission began in 826. Robinson and Waitz date the sack of Hamburg to 845"
- Fix, records: the claim becomes "Born 801 (Robinson, ROB l.1295); the day unknown, 8 September being the translation (ROB l.1295-1298)", tagged "Dominant Modern Reconstruction" (Robinson's). The absent_details entry becomes "Birthday, birthplace, parents: Robinson says the day and place are unknown (ROB l.1295-1300); no held source names the parents."

**N-M1 (brief: cuts that make room for N-B1, each also a precision fix).**
- Para 5: "Pirates took his ships and nearly forty books, and his party walked the rest of the long way to Birka." The ships were the merchants', and the party crossed the seas by ship where it could. Evidence: ROB l.2144-2146: "the pirates, who took from them their ships"; l.2167-2170: "accomplished their long journey on foot, traversing also the intervening seas, where it was possible, by ship". Fix: "Pirates took the ships and nearly forty books, and the party went on, mostly on foot, to Birka."
- Para 5: "There Herigar, the town's prefect and the king's counselor, was baptized" becomes "There Herigar, the town's prefect, was baptized". The card can keep the counselor.
- Para 13: "When people spoke of the healings done through him, Anskar told a friend," becomes "When his healings were spoken of, Anskar told a friend,". This is closer to ROB l.5555-5556: "when these signs of power were spoken of on one occasion in his presence".

**N-M2 (brief para 9: the old man's case is pragmatic, and "spoke for the faith" smooths it).**
- The quote is verbatim but starts after its condition. Evidence: ROB l.4326-4328: "For, inasmuch as we cannot be sure that our gods will be favourably disposed, it is good for us to have the help of this God". He argues for adding a helpful god, from trade and sea perils (l.4302-4311). He does not argue for the faith as such.
- Fix: "On a second journey to Sweden, an old man argued for the Christian God at the people's assembly at Birka." (one word more; the N-B1 total above already allows for it).

**N-M3 (card `legacy.remembered[0]` and Rimbert card `uncertain[1]`: "writing about 1073").**
- No held line dates Adam to 1073. Schmeidler has him begin soon after Archbishop Adalbert's death (March 1072), finish books 1 and 2 perhaps in 1074, and books 3 and 4 in 1075-1076. Evidence: ADAM l.3551-3557.
- Fix: "Adam of Bremen, writing in the 1070s, calls him an apostle outside and a monk within." Apply the same wording in the Rimbert card.

**N-M4 (card `legacy.traces[2]`: two statements about different places set against each other).**
- "Robinson quotes Adam of Bremen that some small part of the Christianity Anskar planted remained, though the Corvey chronicle for 936 says it was well nigh extinct." The Corvey line is about Sweden, and Adam's is about the Danes, half a century or more after Anskar. Evidence: ROB l.802-806: "the Chronicon Corbeiensis for the year 936, referring to the Christians in Sweden ... was well nigh extinct"; l.806-823: Adam: "all the kings of the Danes had been pagans, and ... some small part of the Christianity that had been planted by Anskar had remained".
- Fix: "Robinson quotes the Corvey chronicle for 936, that the faith Anskar and his helpers preached in Sweden was well nigh extinct, and Adam of Bremen, that among the Danes some small part of it remained."

**N-M5 (card `legacy.remembered[2]`: "his claim", and an "X, not Y" frame in card prose).**
- "Robinson writes that his claim to be the Apostle of the North rests on his example, not on the outcome of his work." Anskar made no claim; it was made for him. Evidence: ROB l.238-242: "The claim to the title Apostle of the North, which was early made on his behalf, rests not upon the immediate outcome of his labours, but upon the inspiring example which he bequeathed".
- Fix: "Robinson writes that the title Apostle of the North, given him early, rests on 'the inspiring example which he bequeathed to those who were moved to follow in his steps'."

**N-M6 (card `legacy.traces[0]`: narrator's "X, not Y").**
- "The Life says the pope's decree made Hamburg and Bremen one diocese, not two." Quote the decree instead. Evidence: ROB l.3746-3748: "that these dioceses of Hamburg and Bremen shall henceforth be called not two dioceses but one diocese".
- Fix: "The papal decree in the Life rules that Hamburg and Bremen 'shall henceforth be called not two dioceses but one diocese'."

**N-M7 (card `otherNames[0]` and `legacy.remembered[1]`: Olavus Petri's form, and Paulus Helie without context).**
- "Ansgar, the form of Olavus Petri". Olavus writes "S. Ansgarius" (OP l.17031). "Ansgar" is the modern Swedish of the volume's introduction (OP l.872-875).
- "Paulus Helie" has no context. The same lines place him as a Carmelite in Denmark (OP l.862-863).
- Fix, `otherNames[0]`: "Ansgar, the modern Swedish form; Ansgarius, of Adam of Bremen's Latin and Olavus Petri's Swedish".
- Fix, `remembered[1]`: "In the Swedish debate of 1527-1528, the Danish Carmelite Paulus Helie said the Swedes had left the faith Ansgar preached, and Olavus Petri answered that they kept it."

**N-M8 (card `uncertain[7]`: Robinson's own hedge on the "good man" saying).**
- "His healings. The Life says they could not be counted. Robinson says Anskar never claimed the power himself." Robinson's note on the quotation that closes the brief is more careful. Evidence: ROB l.5582-5583: "It is uncertain whether these words should be regarded as a denial on the part of Anskar that any miracles had been wrought through him."
- Fix: add "Robinson also notes it is uncertain whether Anskar's words about being made a good man deny that miracles were done through him."

**Checks that passed.** Waitz on authorship and Hamburg (WAITZ l.163-184, l.180-183 "Hamburgi enim librum esse ortum, iam omnes fere consentiunt ... Ludovico ... quem a. 876. obiisse constat"); Harald, Wala and the reproaches (ROB l.1726-1855); Herigar (ROB l.2219-2224); Horic and Schleswig (ROB l.3804-3854); the death prayers and Rimbert (ROB l.5778-5792; WAITZ l.4832-4834); Adam's "foris apostolus, intus monachus" and 865 (ADAM l.6124-6155); the letter (MANSI14 l.43691-43725; ADAM l.6133-6142). The absence "no contemporary annal names him" holds: ANNBERT and RFA have only the count Ansgerus and the Hamburg index entry.

---

## rimbert

**Verdict: one blocking finding (R-B1). Otherwise passes with minor fixes.** The Schleswig scene, Pertz's dating, the Turholt boyhood, the alms saying, the altar vessels and Anskar's promise all match the Latin.

**R-B1 (card `uncertain[1]`: a sourcing error on the death).**
- "The year 888 and the burial day, 11 June, come from Adam of Bremen, writing about 1073, from a computus brought from Corbie".
- Adam says the computus gave Rimbert's years and his predecessor's death. He says nothing of the burial day coming from it. Schmeidler's margin sets the death passage against the Life of Rimbert, chapters 21 and 24, and chapter 24 is the one the held scan lacks. Evidence: ADAM l.6206-6207: "Annos eius et obitum decessoris sui repperimus in quodam compote a Corbeia delate. Ceterum Vita eius ... comprehendit."; l.6779-6784: margin "V. Rimb. c. 21" at "Tandem morbo confectus", and "V. Rimb. c. 24" at "depositio est III idus Iunii"; l.6826 footnote: "Ann. Corb. 888".
- The card `dates` field gets this right ("took the years from a computus"); `uncertain[1]` does not.
- Fix: "His death. The year 888 and the burial day, 11 June, come from Adam of Bremen, writing in the 1070s. Adam says he found Rimbert's years in a computus brought from Corbie. Bernhard Schmeidler's margin points the death passage to the Life of Rimbert's twenty-fourth chapter, which the copy used here lacks, and he cites the Annals of Corvey for 888."

**R-M1 (brief length: 366 words, one over the 365 limit; a recorder).**
- Mark's rule: non-majors up to about 2:15 (365 words), and recorders stay standard length. Recent era 4 recorders ran 348 to 365.
- Fix (this also covers R-M2): para 1 "To show she was a Christian, she raised her voice and began to sing psalms." becomes "To show she was a Christian, she began to sing psalms aloud." (WAITZ l.5244-5245: "elevata altius voce coepit cantare psalmos"). Para 13 "Once, the Life says," becomes "Once, the Life of Rimbert says,". Net 365 words.

**R-M2 (brief para 13: "the Life" is ambiguous).** The brief has just spoken of the Life of Anskar, which Rimbert wrote. The promise is in the Life of Rimbert (WAITZ l.4611-4632). The fix is in R-M1.

**R-M3 (card `place`: "where he died" is unsupported).**
- "Bremen, where he died and, Adam says, was buried outside Saint Peter's church on the east". No held line names the place of death. Adam gives only the burial (ADAM l.6782-6785: "Sepultus est extra basilicam sancti Petri ab oriente"), and the Life's scan breaks off before the death (WAITZ l.5410-5422).
- Fix: "Bremen, where, Adam says, he was buried outside Saint Peter's church on the east".

**R-M4 (brief para 7 / card `uncertain`: the "most faithful disciple" claim has a held dissent).**
- The brief, rightly, gives the claim as the Life of Rimbert's. But Robinson argues that in one passage the intimate priest is more likely Erimbert, against Klippel, who reads it through that very claim. Evidence: ROB l.4266-4277: "Klippel identifies this priest ... with Rimbert, Anskar's biographer. He deduces this from the statement in the Vita Rimberti, chap. ix ... It would appear however, that at this time Rimbert was still in deacon's orders ... It is more likely that the priest referred to is Erimbert."
- Fix: add to the card's `uncertain[3]`: "Robinson also doubts the Life of Rimbert's rule that every 'most faithful disciple' is Rimbert, since one such disciple says Mass when Rimbert was still a deacon; he thinks that one is Erimbert." Add the side to the records' contested_claims.

**R-M5 (card `keyWorks[0]`: which Corbie).**
- "addressed to the monks of Corbie". Robinson says this means Old Corbie, near Amiens, and that Adam of Bremen wrongly makes it New Corbey. Evidence: ROB l.1135-1137 (the greeting to "the sacred monastery of Corbey"), l.1164-1170: "i.e. Corbeja antiqua ... Adam of Bremen incorrectly identifies this Corbey with the New Corbey"; ADAM l.6202: "ad fratres cenobii ... Novae Corbeiae".
- Fix: "addressed to the monks of Corbie, near Amiens (Robinson; Adam of Bremen says New Corbey)".

---

## README.md

**Verdict: two blocking findings (D-B1, D-B2) and minor fixes.** The "Corrections to the re-score" I spot-checked hold: Fabricius at PG94 l.605-625 ("post medium saeculi decimi", "videtur non ante a. C. 756"); Le Quien's date for the second speech (PG94 l.32112-32116, OCR "750" for 730, "quo Germanus solio detrusus est"); Fabricius "post a. c. 743" for the Dialectica (l.943); the Salzburg account at Ginzel l.13130-13722 and Industriae tuae at l.13878-13982; the Monitum at PG126 l.96725-96749 ending "Sed judicium penes Lectorem sit"; "qui cum ipso vixit" at PG99 l.3725; the Turholt note (WAITZ l.1832-1833); Dahlmann's "Alium a Rimberto" (WAITZ l.3549-3550).

**D-B1 (README para "The river counts change": counts disagree with the census lanes).**
- The README says: "Greek East & Orthodoxy era 4 held five majors ... the river now holds nine, or eight if Antony and Theodosius are counted with their first tradition ... Latin West & Catholicism era 4 held ten, and Anskar makes eleven."
- The ten and five come from Rescore.md l.71-73, which counts Humbert of Silva Candida in Latin West era 4. The census does not support that. Humbert's card tradition is "The Latin Papal Church (Gregorian Reform to Innocent III); The Byzantine Imperial Church (Macedonian Era)" (`era4/batch4/humbert-of-silva-candida.card.json`). In `world-census.json` the first is era 5, laneLabel "Latin West & Catholicism", dates "c. 1049-1300". The second is era 4, laneLabel "Greek East & Orthodoxy".
- So Humbert's only era 4 tradition is in the Greek East. That is the same case as the Kyiv pair, whose first tradition is era 5 ("Kievan Rus' Christianity, 1054-1240") and second era 4. The README counts the pair in the Greek East but counts Humbert in the Latin West, so it does not apply one rule.
- The census lanes of the era 4 majors (batches 1, 2, 4, 5, 7 READMEs, each card's `tradition` mapped to `laneLabel`):
  - Latin West, era 4 tradition: Bede, Boniface, Aidan, Hild (Anglo-Saxon); Adomnán (Medieval Irish); Alcuin, Dhuoda, Hincmar (Carolingian Reform); Nennius (Medieval Welsh). That is 9. Humbert is Latin West only in era 5.
  - Greek East, era 4 tradition: Martin I, Maximus (Heraclian & Iconoclast); Photius, Athanasios, Symeon (Macedonian); and Humbert (Macedonian, his only era 4 entry). That is 6, or 5 if a person counts only by their first-listed tradition.
- Counted by any era 4 tradition: Latin West 9, plus Anskar, makes 10. Greek East 6, plus John of Damascus, Theodore, Cyril and Methodius, and Antony and Theodosius, makes 10. Counted by first-listed tradition: Latin West 10; Greek East 5 plus three makes 8, since both Humbert and the Kyiv pair go to era 5.
- Fix (README): "**The river counts change.** By the census lanes, Greek East & Orthodoxy era 4 held five majors by first tradition (Martin I, Maximus, Photius, Athanasios, Symeon), or six with Humbert of Silva Candida, whose only era 4 tradition is the Macedonian-era Byzantine church. John of Damascus, Theodore and Cyril and Methodius make it eight; Antony and Theodosius, whose first tradition begins in 1054, would make nine, and Humbert ten. Latin West & Catholicism era 4 held nine with an era 4 tradition, since Humbert's Latin Papal entry is era 5, and Anskar makes ten. The map shows five per river, and which five is Mark's choice." Then log in Open-Gaps that Rescore.md l.72-73 counts Humbert in the wrong river for era 4, so that the map build slice (Open-Gaps, "Map Who build slice: caps, major mark, placement", 2026-11-11) counts majors by one stated rule.

**D-B2 (README "Card traditions": "Only Antony's settling in the cave, after 1051, falls in it").**
- That holds for the Chronicle only. The 1462 Paterik, which the card itself cites, puts two more events inside 988-1054: Antony's first stay in Kyiv under Vladimir, with his flight back to Athos when Svyatopolk killed Boris and Gleb, and Theodosius's tonsure in 6540 (1032) under Yaroslav. Evidence: PAT l.1040-1041 ("Въ княжение ... великого князя Володимира Святославича"), l.1094-1099 (the flight, "пакы бѣжа въ святую гору"), l.1685-1686 ("в лѣто 6540, при князи благочестивемь Ярославѣ").
- The Chronicle's own placing also opens the pair's whole account under 6559 (1051) (CROSS l.11740-11744).
- Fix: "The re-score places them in Kievan Rus' Christianity (988 to 1054). In the Chronicle, only Antony's settling in the cave, after 1051, falls in it; the 1462 Paterik also puts Antony's first stay in Kyiv under Vladimir and Theodosius's tonsure in 1032 inside it. The gathering of the brothers comes after Yaroslav's death in 1054 in both, and Theodosius's abbacy, the move above ground in 1062, the Studite rule and both lives' ends fall later."

**D-M1 (README "Who the sources are", Antony and Theodosius: what the two sources differ on).**
- "Where the two differ (Antony's journeys, the source of the Studite rule, where Antony ended his life), the card gives both." "Where Antony ended his life" is a tension inside the Chronicle (CROSS l.11799-11802 against l.12856-12860), not between the Chronicle and Nestor. The largest difference, who built the monastery above ground, is missing (K-B1).
- Fix: "Where the two differ (Antony's journeys, Theodosius's tonsure year, who built the monastery above ground, the source of the Studite rule), the card gives both; it also gives the Chronicle's two accounts of where Antony ended his life."

**D-M2 (README "Majors and lengths": word counts).**
- "Their briefs run 401 to 405 words". `john-of-damascus.brief.txt` is 400 words (`wc -w`). "Rimbert is a recorder and Clement's life rests on one Life, so both stay near the 2:15 limit for non-majors, at 366 words each." 366 is over the 365 limit. And the recorder rule is "recorders stay standard length", which does not lead to "so ... near the 2:15 limit".
- Fix: "Their briefs run 400 to 405 words, about 2:28 to 2:30 ... Rimbert and Clement are not major and run up to the 2:15 limit for non-majors, at 365 words; Rimbert is a recorder at standard length, and Clement's life rests on one Life." The numbers must follow whatever lengths the fixes leave.

**D-M3 (README "Language and quotations": "Three brief quotations cross a scan mark").**
- "sixty-fourth*" is quoted in the Anskar card (`dates`), not in a brief, and it sits at ROB l.5596, not l.5594.
- Fix: "Two brief quotations and one card quotation cross a scan mark ...: a footnote mark in Robinson's 'cloakf' (l.2652) and 'sixty-fourth*' (l.5596, in the Anskar card), and a running head inside Cross's 'Who ... among you' (l.11855-11860)."

**D-M4 (README: a bare Open-Gaps number, and census dates).**
- "(Open-Gaps 217)". CLAUDE.md asks that cross-references cite subject and date, not a bare number. Also, entry 217 sets the caps but does not record the count of five. The count is the re-score's (Rescore.md l.73).
- Fix: "(Rescore.md, 'Major proposals'; caps in Open-Gaps, 'Map Who build slice: caps, major mark, placement', 2026-11-11)".
- "Card traditions" gives "(863 to 916)" and "(826 to 1104)". The census has "c. 863-916" and "c. 826-1104". Fix: "(about 863 to 916)", "(about 826 to 1104)".

---

## Files and line ranges opened

- CROSS l.4375-4392, 4625-4690, 4810-4830, 11740-11880, 11894, 11967, 12525-12700, 12845-12870, 12910-12920, 13331-13405, 15045-15060, 15100-15115.
- PAT l.100-120, 160-170, 1030-1255, 1310-1325, 1375-1395, 1640-1690, 2140-2185, 3580-3700, 9080-9125, 9185-9230, 10050-10062, 10430-10440.
- MOUR l.1570-1660; grep for Anthony/Antony and 1073/1074.
- ROB l.230-262, 580-590, 664-700, 785-826, 940-950, 1050-1060, 1121-1175, 1290-1302, 1700-1900, 2130-2230, 2394-2410, 2630-2705, 3740-3752, 3795-3860, 4132-4142, 4266-4335, 4762-4820, 5064-5095, 5540-5600, 5730-5800.
- WAITZ l.155-220, 1822-1834, 2005-2025, 2630-2642, 3545-3551, 4370-4400, 4515-4640, 4785-4915, 5040-5072, 5180-5330, 5410-5423.
- ADAM l.3540-3562, 5175-5180, 5394-5404, 5445-5505, 6120-6215, 6490-6536, 6772-6830.
- STEIN l.3705-3712 (grep 845). ANNBERT l.2155-2210. MANSI14 l.43680-43728, 99328-99352. OP l.860-880, 17020-17036.
- PG94 (john-damascus_opera-omnia-t1-with-vita-pg94-grc-lat_migne1860.txt) l.605-625, 938-946, 1285-1300, 32075-32128; Ginzel l.862-867, 13128-13134, 13718-13724, 13876-13882, 13978-13984; PG99 l.3720-3728; PG126 l.96722-96750.
- `cic-website/data/world-census.json`: movements' `laneLabel`, `era`, `dates` for every era 4 major's card tradition; `people` entries for the batch-9 names.
- Era 4 batch 1-8 READMEs (major lines) and all era 4 card `tradition` fields; Rescore.md l.67-101, 121-148; Who_Scan_Era4.md row 105; Open-Gaps 217; Decision-Log l.3069-3071, 3116.

## Searches run for absences

- Antony's death year: grep of PAT for every "престав/успе/кончин" line (none for Antony); CROSS (only "Antonius was already dead", l.12916); MOUR for 1073/1074 and Anthony; `grep -rli` across cic/texts for "Antony of the Caves", "Antonius of the Caves", "Antony Pechersk", "Антоний Печерск" (no hits). The absence holds.
- "of the Caves" forms: `grep -rl "of the Caves" cic/texts` gives only README.md, REGISTRY.yaml and an unrelated Ludolf line. No held source spells the card's English forms (K-M7).
- Anskar in annals: ANNBERT and RFA for ansc/ansg/ansk/anschar/hamma/hamburg. Only the count Ansgerus and Waitz's index "(Hamburgum) Sclavorum civitas" turn up. The absence holds.
- Anskar's birth: ROB grep for 801 and "sixty-fourth". Robinson gives 801 flatly (N-B2: the absence is false for the year).
- Rimbert: ROB grep "Rimbert" (no English of the Life of Rimbert; the Erimbert dissent found, R-M4); WAITZ and ADAM grep for Turholt/Thurholt/Thourout; ADAM death passage margins (R-B1).
