# Round 1 review, group g2

Briefs: tacitus (batch2), suetonius (batch2), pliny-the-younger (batch3), pontius-the-deacon (batch2).

## Step 0: the blind pair (written before opening the pattern, the bar or the batch)

Y is the stronger Standard-v1 brief. Concrete reasons:

1. Stance followed by what came of it, carried by the source. Y gives a stance (refusing Chilperic's decree), the cost of it in the king's words, and the outcome in Gregory's own words ("So the king gave up this plan"), then says plainly what the source does not say ("He does not say his stand cost him anything"). X has one stance (caring for strangers in the plague) and its outcome is only "They did good to all, he says", which repeats the stance rather than telling what came of it.
2. The person acts in Y. Gregory refuses, argues, answers an envoy. In X the writer mostly watches and records; the only things he does are go into exile by choice and write. That is honest to a recorder, but X spends a sentence on the writer's attitude ("He writes as an admirer, praising Cyprian on every page, and begins only at the conversion") that does not move a story forward.
3. Impact. Y ends on why he matters (most of what is known of the church in Merovingian Gaul comes from his books; his is the only account of these stands). X ends on how the name is known (Jerome, then Bede), which is necessary honest-limit material but is weaker as an ending; the Bede sentence in particular adds a step without adding to the story.
4. X has strengths: a vivid, concrete opening (the dream and the flat hand like a blade) and an honest "our sources do not show" close. Its quotation of the writer's grief is the best single line in either text. But the middle paragraph of X carries Cyprian's story more than the writer's.

Weaknesses of Y: "Arians" is not explained for a general listener; the creed sentence and the Chilperic exchange run long for the ear.

After the full read: X was `pontius-the-deacon` (this batch); Y was `gregory-of-tours` (the bar). My preference for the bar text had concrete reasons, so there is no blind-pair finding to raise. One caution for the coordinator: the pair set a recorder beside a bishop who acted, and part of the gap (reason 2) is the difference in kind, not only in craft.

## Bar briefs compared against

Methodius of Olympus (the thin-record model), Gregory of Tours and Benedict of Nursia (the Standard v1 examples for opening, witnesses and impact), with Athanasius, Constantine the Great and Ephrem the Syrian for flow and closes. The current texts in `Who-Profiles/bar/` were used.

## Readability (`python3 -m engine.m1.profile_readability --report`)

| Brief | Words | Grade (full) | Grade (names out, info) | Reading ease (names out) | Words a sentence | Joining words /100 | Short sentences | Result |
|---|---|---|---|---|---|---|---|---|
| tacitus | 318 | 8.7 | 7.5 | 74.8 | 18.7 | 0.6 | 12% | pass |
| suetonius | 298 | 9.6 | 8.5 | 69.2 | 19.9 | 0.7 | 13% | pass |
| pliny-the-younger | 300 | 9.7 | 9.0 | 66.2 | 20.0 | 0.7 | 0% | pass |
| pontius-the-deacon | 298 | 8.4 | 7.7 | 75.0 | 19.9 | 1.3 | 7% | pass |

All four are under 325 words, so no length judgment is owed. No term or name was found that a general adult listener could not follow, except as noted under each brief.

## The coordinator's "told plainly" rulings, tested

- **Tacitus, "senator".** Uncontested in scholarship (his consulship and senatorial career are attested outside the Annals). Holds as widely accepted. The card must say it rests in the Library only on the vendoring header (TA 5).
- **Tacitus, "the year 64".** The year of the fire is uncontested. What is contested (TA header 53-59, Shaw against Jones) is whether a fire-linked persecution of Christians as a named group took place; the brief tells that only as Tacitus's account ("What Nero did next is told by Cornelius Tacitus"), so it is not told as settled. Holds. The card must carry the Shaw/Jones question.
- **Tacitus, "about fifty years later".** The Annals' date sits within general agreement (the 110s). Holds.
- **Pliny, Bithynia.** Uncontested (his tenth book of letters is addressed from the province). Holds; the card must say that in the Library it rests on McGiffert's note (E 19457).
- **Pliny, "around 112".** Scholarly datings run from about 110 to 113 for the governorship and the letter; "around 112" sits inside the general range and does not rest on one scholar's figure. Holds.
- **Suetonius, "secretary to the emperor Hadrian".** Attested by an ancient source (Spartianus, reported at SR 232-241) and uncontested. Holds.
- **Suetonius, "around 120".** For the secretaryship, holds (Rolfe's "119 to 121" and the usual dismissal date of about 122 both fall inside "around 120"). But the sentence ties the writing of the Lives to the same moment ("Around 120, Suetonius was in Rome as secretary ... and he wrote the lives of twelve Caesars"). When the twelve Lives were written is not settled: the dedication to Septicius as prefect dates the opening book to his prefecture, and whether the later Lives came then or after the dismissal is debated. "Published in 120" (SR 323) is Rolfe's flat figure. This is a non-blocking point (the brief does not state a year of writing), listed under Suetonius.
- **Suetonius, the two readings of "Chrestus".** Both readings (another man of that name; a confused or second-hand report of quarrels over Christ among Rome's Jews) are the two long-standing positions in general scholarship, not one scholar's reading; the brief offers them with "may", does not settle them, and sets the ancient evidence on the spelling (Tertullian, Lactantius) beside them. The test passes. The pattern's "each side named" cannot be met in the brief without naming modern scholars, which Standard v1 forbids; the card's What is uncertain must therefore name who holds each reading (the refs record already plans Rolfe and Thomson-Forester there).

---

## tacitus (era1/batch2)

**Verdict: BLOCKED** (1 blocking finding).

### Blocking

**B1. "his one chapter on the Christians" is unsupported, and the corpus holds evidence against it.**
- Sentence: "He was not a Christian, and his one chapter on the Christians treats them as criminals."
- Evidence: the held Tacitus file is one chapter only and its header warns that "Nothing here licenses a claim about what Tacitus says elsewhere" (`tacitus_annals-15-44_church-brodribb1876.txt`, header lines 37-43). Tertullian says the fifth book of the Histories spoke of Jewish worship and that the charge passed to Christians (`anf03_tertullian.xml` 2570-2582). The Library also holds Sulpicius Severus's account of Titus's council resolving to destroy the temple "in order that the religion of the Jews and of the Christians might more thoroughly be subverted" (`npnf211_sulpitius-severus-vincent-lerins-cassian.xml` 10724-10736), a passage widely taken to come from the lost Histories of Tacitus. "One chapter" is a loose quantifier (item 4) that the held files do not carry and that is open to dispute.
- Fix accepted: "his chapter on the Christians", or "the one chapter of his that we hold on the Christians". Nothing else in the sentence needs to change.

### Rigor checks that held (by hand, TA line 68 throughout)
The blame "to get rid of the report"; Q1 and Q2; the superstition checked and breaking out in Judaea and Rome; the arrest of those who "pleaded guilty" and the multitude convicted "not so much of the crime of firing the city, as of hatred against mankind"; skins and dogs, crosses, burned as lights; "criminals who deserved extreme and exemplary punishment"; the compassion "not ... for the public good, but to glut one man's cruelty". No source for Christus and no particular of the abominations: confirmed by reading the whole chapter. Tertullian, Apology 16 (T3 2567-2584): "first put this notion into people's minds", the ass's head, "from this, I suppose, it was taken for granted that we too", "the very opposite of tacit in telling lies". Sulpicius, Sacred History II.29 (SS 10645-10666): same details in the same order, "inflicted upon the innocent", "In this way, cruelty first began to be manifested against the Christians"; a search of the file finds Tacitus named only in modern notes (810, 11454). "Of Aquitania" (SS 349-351, 470-471); "around 400" (SS 441-443, the work runs to 400).

### Quotations
Q1 and Q2 match `comparison.md` E6 and E7 FINAL exactly. E7's FINAL drops Church-Brodribb's "one of our" on the strength of the Latin as quoted in Mansi II 41697-41699 ("per procuratorem"); the reading covers the original and adds nothing. Pass.

### Non-blocking
- "Those who confessed were arrested first" leaves "confessed" without an object. Tacitus's own "pleaded guilty" is famously ambiguous, so the brief should not resolve it, but a listener will ask "confessed to what?". "Those who admitted they were Christians" would settle what Tacitus leaves open; better is "Those who confessed, he says, were arrested first", which at least marks the ambiguity as his.
- "His Histories had said the Jews honored the head of an ass" is told flat; it is carried by Tertullian, named in the sentence before, which the pattern allows. Fine as is.

### Craft tests
1. **Storytelling.** Line: a Roman historian hostile to the Christians tells how Nero blamed and killed them for the fire, and who Christus was, without saying where he learned it; later Christian writers both attacked him and retold his account. Weakest: "He calls the faith a harmful superstition that was checked for a moment and then broke out again, in Judaea where it began and in Rome itself." Beside Methodius, "Socrates of Constantinople says Methodius attacked Origen in many places and then, as if taking it all back, praised him in a dialogue." Tacitus's sentence is report, but it is the report the outside-witness form asks for. **Reaches the level.**
2. **Flow.** Weakest link: "...by the procurator Pontius Pilate." / "He calls the faith a harmful superstition...". Carried only by "He". Beside Gregory of Tours, "Gregory refused. Only the Son was made man and suffered, he answered...". The link is thin but the sentences follow the chapter's own order. The pity sentence ("Tacitus thought they deserved the harshest punishment. Yet he records that people came to pity them, because...") is as good as the bar. **Reaches the level.**
3. **No AI tells.** Weakest: "This, Sulpicius wrote, was how the cruelty against Christians began." Beside Ephrem, "From that time on, Sozomen says, the Syrians sang the songs of Ephrem." It is Sulpicius's own claim (SS 10665-10666), not a narrator's tag. **Reaches the level.**
4. **No hanging sentences.** Weakest: "He does not say where he learned of Christus, and he names none of the shameful acts." Beside Methodius, "Both men admired Origen, so neither is a neutral witness." It is the trust judgment and is tied to the chapter just told. The close finishes the story. **Reaches the level.**
5. **Everything relevant.** Weakest: "Around 400, Sulpicius Severus ... told of the fire with the same details in the same order: the animal skins and the dogs, the crosses, the bodies burned for light when the day ended." The list repeats details, but it is the evidence for "same details", so it earns its place. Beside Methodius on Epiphanius copying "word for word". **Reaches the level.**

### Sentence test
17 sentences; 0 marked. Nearest to the line: the "harmful superstition" sentence, which adds the spread to Judaea and Rome and so is kept.

---

## suetonius (era1/batch2)

**Verdict: BLOCKED** (1 blocking finding).

### Blocking

**B1. Two sentences fail the sentence test (transitions that only connect).**
- Sentences: "The first is in the life of Claudius." and "Jerome looked to Suetonius for something else."
- Evidence: checklist item 10, the sentence test names "transitions that only connect" as sentences that go. Neither moves the story or sets up a stance; each only announces the next sentence. Beside the bar: Benedict, "The Rule is Benedict's own words", which is short but carries a claim (whose words they are) that bears on trust.
- Fix accepted: fold each into its neighbor, for example "The first, in the life of Claudius, reads: 'The Jews...'" and "Near the end of the fourth century Jerome looked to Suetonius for something else: he wrote that he had been urged to follow his example ...". A rewrite of the two paragraph openings, not a deletion that leaves the quotation unintroduced.

### Rigor checks that held
Claudius 25.4 Latin and English (SR 25843-25844, 25907-25909); nothing more said of Chrestus (the next sentence turns to the German envoys, SR 25844-25847). Acts 18:2 (WEB 88523, "Claudius had commanded all the Jews to depart from Rome"). Tertullian, Apology 3 (T3 1713-1715, "wrongly pronounced by you 'Chrestianus'"). Lactantius, Institutes IV.7 (L7 3163, "by the change of a letter are accustomed to call Him Chrestus"). Nero 16.2 between the taverns and the chariot drivers, in a list of "abuses ... severely punished and put down, and ... new laws" (SR 28454-28462, 28517-28529). Nero 38, "he set fire to the city" (SR 30560-30563), with no link to the Christians. Jerome's preface (J3 38773-38780). The negative, "no early Christian writer quoting either notice": I searched `cic/texts/` for "impulsore Chresto", "Chresto assidue", "Iudaeos impulsore" and "superstitionis novae ac malefic"; the only hits are Rolfe, Schanz-Hosius, Duchesne, Mirbt and an editor's note in Mansi II (41693, a 17th-century annotation), all modern. Orosius, who does quote the Claudius line, is not held, and the brief says "the sources we hold". The negative stands as worded.

### Quotations
Q1 and Q2 match `comparison.md` E8 and E9 FINAL exactly. Pass.

### Non-blocking
- "Around 120, Suetonius was in Rome as secretary to the emperor Hadrian, and he wrote the lives of twelve Caesars" ties the writing to the year. The date of the whole work is not settled (see the rulings above). Split the clauses so the year attaches only to the office ("Around 120 Suetonius was secretary to the emperor Hadrian in Rome. His lives of twelve Caesars, from Julius Caesar to Domitian, give the Christians two short notices."), which also removes a sentence. The card should say the Lives' date is modern reckoning, and that at least the first book is dated by its dedication.
- Item 16: the opening gives year, place and office but not what was going on. For an outside witness this is light but acceptable.
- "Tertullian of Carthage did complain" leans on an emphatic "did" to carry the turn; "Tertullian of Carthage complained that..." with "though" or "and" from the previous sentence would join it better.
- Card: the two readings of Chrestus must be named with their holders under What is uncertain, since the brief cannot name them.

### Craft tests
1. **Storytelling.** Line: a court biographer gives the Christians two short notices, one of them unclear, and later Christians valued him as a model for writing lives, not for those notices. Weakest: "The second notice is in the life of Nero, in a list of abuses he put down, between a rule on what taverns could sell and a curb on chariot drivers." Beside Methodius, "Little else about Methodius is certain. Jerome says he was bishop of Olympus..." The placement pays off (it shows how little weight Suetonius gives the Christians, and leads to "he does not connect the Christians with the fire"). **Reaches the level.**
2. **Flow.** Weakest link: "...among Rome's Jews." / "Tertullian of Carthage did complain that Romans said Chrestian for Christian...". Beside Athanasius, "Sozomen adds a rumor that Athanasius had hidden the man himself. Either way, the council deposed him." The relation (ancient evidence that Romans confused the names) is left for the listener to supply. Weak, but the Chrestus paragraph's own reasoning ("because", "and Tacitus puts", "So") is well joined. **Reaches the level, narrowly**; the fix in the non-blocking list would strengthen it.
3. **No AI tells.** Weakest: "Jerome looked to Suetonius for something else." It is a connector that sounds like a set-up line. Beside John Chrysostom's opening paragraph. Covered by B1; once folded, no tell remains.
4. **No hanging sentences.** "The first is in the life of Claudius." and "Jerome looked to Suetonius for something else." both stand as beats to the next line (B1). The close, Jerome's preface, finishes the story the way Gregory of Tours's close on Paul the Deacon does. **Fails until B1 is fixed.**
5. **Everything relevant.** Weakest: "The book of Acts also says that Claudius ordered all the Jews to leave Rome, so the expulsion has a second witness." Beside Constantine, "Lactantius, who wrote in Constantine's own day, knows only a dream". It bears directly on trust. **Reaches the level.**

### Sentence test
15 sentences; 2 marked: "The first is in the life of Claudius."; "Jerome looked to Suetonius for something else." (B1).

---

## pliny-the-younger (era1/batch3)

**Verdict: BLOCKED** (1 blocking finding).

### Blocking

**B1. "He asked each prisoner three times" says more than the letter.**
- Sentence: "He asked each prisoner three times whether they were Christians, and sent those who held firm to be punished."
- Evidence: `npnf201_eusebius-church-history-life-of-constantine.xml` 19471-19474: "I have asked them if they were Christians, and if they have confessed, I have asked them a second and third time, threatening them with punishment; if they have persisted, I have commanded them to be led away to punishment." Only those who confessed were asked again, and the second and third questions came with the threat of punishment, which is the substance of his method and is dropped.
- Fix accepted: "He asked each prisoner whether they were Christians. Those who said yes he asked twice more, threatening punishment, and those who held firm he sent to be punished." (or the same in one sentence).

### Rigor checks that held (E = npnf201, inside McGiffert's note)
Never present at trials, so ignorant of the custom (E 19461-19463): the "So" is carried by Pliny's "therefore" and "Meanwhile ... I have pursued the following course" (E 19463-19469). Release after invoking the gods and cursing Christ (E 19481-19486). Former Christians, "some three years, some several years, and one even twenty years before" (E 19487-19490), and the worship is theirs (E 19490-19494). Oath against theft, robbery, adultery (E 19494-19497). Two female slaves called deaconesses examined under torture "in order to ascertain the truth" (E 19502-19505). "Insanity" (E 19477). Trajan's reply (E 19526-19527). Tertullian, Apology 2 (T 1565-1586), argued from the report; Q4. Eusebius III.33.2-3 (E 19541-19560): the persecution "to a certain degree checked", "many of the faithful endured martyrdom", and the account taken from Tertullian's Apology. "His own inquiry turned up no crime" is the writer's reading (flagged), but it is supported by Pliny's "not with a view to the commission of some crime" (E 19495) and "nothing except a superstition" (E 19505-19506), and read the same way by Tertullian (T 1575-1581) and Eusebius ("he had not heard of their doing anything profane or contrary to the laws", E 19533-19535). Holds.

### Quotations
Q1 to Q4 match `comparison.md` E10 to E13 FINAL exactly (Q1 with "as to a god", Q2 with "perverse"). Pass.

### Non-blocking
- The held letter gives a second reason for writing: "especially on account of the number of persons involved", with the spread "not only the cities, but also the villages and even the country districts" and the temples "almost deserted" (E 19507-19517). The brief gives only his inexperience. For an outside witness this is among the weightiest facts he reports, and it bears on what Trajan's ruling then checked. One clause would carry it ("and because, he said, so many of every age and rank, in the cities and the countryside, were being brought to trial"). It matters more than the Tertullian paraphrase sentence (below).
- "Later Tertullian of Carthage, defending the Christians, argued from the governor's report that Pliny had found nothing in their worship but early meetings to sing hymns to Christ and a pledge against crime." This largely restates what the brief has just told; its new content is that Tertullian used the report. It could shrink to a clause, freeing room for the point above.

### Craft tests
1. **Storytelling.** Line: a governor who had never tried Christians tried them his own way, learned from former Christians how they worshipped, found no crime, and got a ruling from Trajan that Christian writers later turned against the empire. Weakest: "They also swore an oath to keep from theft, robbery and adultery." Beside Benedict, "His monks promise 'stability, a changed way of life, and obedience'". It is report, but it sets up "no crime". **Reaches the level.**
2. **Flow.** Weakest link: "...yet his own inquiry turned up no crime." / "Trajan answered that Christians...". Beside Gregory of Tours, "Gregory refused. Only the Son was made man ... he answered". "Answered" ties back to the request for advice in the first paragraph. **Reaches the level.**
3. **No AI tells.** Weakest: "Pliny writes as the judge who had already sent Christians to punishment, and he calls their faith insanity, yet his own inquiry turned up no crime." Beside Methodius, "Both men admired Origen, so neither is a neutral witness." Balanced, but every clause is sourced and it is the trust judgment the form asks for. **Reaches the level.**
4. **No hanging sentences.** Weakest: "He found 'nothing except a perverse and excessive superstition.'" Ends a paragraph on a quotation, but it is the result of the torture in the sentence before. The close (Eusebius, with its limit) finishes the story, as Ephrem's close does. **Reaches the level.**
5. **Everything relevant.** Weakest: the Tertullian paraphrase sentence (see non-blocking). Beside Constantine, "Maxentius was driven into the Tiber at the broken bridge." It is relevant (it is the consequence) but partly restates. **Reaches the level.**

### Sentence test
15 sentences; 1 marked as partial: the Tertullian paraphrase sentence (restates the worship and oath; its new content, Tertullian's use of the report, should stay as a clause). Non-blocking, because it carries the consequence beat.

---

## pontius-the-deacon (era1/batch2)

**Verdict: BLOCKED** (2 blocking findings).

The brief keeps to Mark's condition for the five (tells only what the held sources show and says plainly where the record stops): the Life never names its writer (checked through AN 27664-28303; the "By Pontius the Deacon" heading is the edition's), the name and the office rest on Jerome (J3 40833-40835), and the close says where the record stops.

### Blocking

**B1. The closing quotation does not match the final reading.**
- Brief: "I rejoice greatly, very greatly, at his glory, yet I grieve more that I remained behind."
- `comparison.md` E34 FINAL: "I rejoice greatly, very greatly, at his glory. Yet I grieve more that I remained behind." (two sentences, one thought each). The brief carries rendering A as first written, not the FINAL.
- Fix accepted: use the FINAL wording inside the marks.

**B2. The Bede sentence fails the sentence test.**
- Sentence: "In the eighth century Bede copied Jerome's words into his chronicle."
- Evidence: `bede_chronica-maiora-in-chronica-minora-3-mgh-aa-13-lat_mommsen1898.txt` 23906-23909 repeats Jerome's line and adds nothing; the writer's own notes say "He adds nothing to Jerome; the sentence shows only that the attribution was passed on". It is a side fact that does not move Pontius's story (item 10, sentence test), and it sits between the Jerome sentence and the close, so the close's "Beyond these" has to reach back past it.
- Fix accepted: move Bede to the card (Legacy, How they're remembered) and let "Beyond Jerome, our sources do not show who read the Life or what became of Pontius" close the brief.

### Rigor checks that held (AN = anf05; V = Hartel)
Banishment to Curubis by the proconsul on the emperors' letters (V 41415-41432; AN 28054-28055); 257 from the consuls (V 41415-41416), widely accepted. "Chosen me among his household companions to a voluntary exile" (AN 28056-28058). The dream: a young man, the proconsul's tribunal, a sentence noted "for he had asked nothing of me with the accustomed interrogation", the hand "expanded and flattened like a blade" (AN 28061-28074). A year to the day (AN 28098-28102). Why he wrote, laypeople and catechumens recorded, a bishop "who, independently of his martyrdom, had much to teach" (AN 27677-27685). Begins at the conversion and passes over earlier pursuits (AN 27701-27708). Sold his goods and gave nearly the whole price (V 40376-40378, followed against Wallis's "entire estates", AN 27730-27732; flagged by the writer and correctly handled). The plague, the abandonment of "their own friends", "nothing wonderful in our cherishing our own people only", sun and showers "to aliens also" (AN 27939-27969); good done "to all men, not to those only who are of the household of faith" (AN 27990-27992). Jerome, Lives 68 (J3 40833-40835). "About 130 years": the preface's fourteenth year of Theodosius (J3 38785) less 258, a reckoning within general agreement.

### Non-blocking
- "praising Cyprian on every page" is a loose quantifier; "praising Cyprian throughout" says what the Life shows.
- "He tells how the new convert sold his property and gave nearly all the price to the poor." This is a second example of Cyprian's charity beside the plague, which carries both the teaching and its result; on Mark's "a second example where one is enough" it is the next sentence to cut if room is wanted. Kept here only because it is the Life's first act after the conversion it says it begins from.
- Item 16: the opening gives the year, place, region and tradition; "what was going on" (the Valerian persecution) is carried only by "the emperor Valerian's governor banished". Acceptable.

### Craft tests
1. **Storytelling.** Line: a man of Cyprian's household followed him into exile by choice, wrote his Life because a bishop's life and not only his death deserved a record, and is known by name only because Jerome named him. Weakest: "He writes as an admirer, praising Cyprian on every page, and begins only at the conversion." Beside Benedict, "Gregory wrote to show what God did through a saint, so the book is full of wonders." The bar ties the leaning to its consequence ("so the book is full of wonders"); this sentence states the leaning without saying what it does to the record. **Reaches the level, narrowly.**
2. **Flow.** Weakest link: "...to fellow believers." / "The Life ends on its writer's grief:". Beside Gregory of Nyssa, "After Basil died, Gregory wrote, he 'inherited the controversy with Eunomius.'" A jump from the plague to the last page, carried only by the paragraph break; but the grief line turns at once to the question of the name, and that link ("It never gives his name. That rests on Jerome") is well made. **Reaches the level.**
3. **No AI tells.** Weakest: "Beyond these, our sources do not show who read the Life or what became of Pontius." Beside Gregory of Nyssa, "The sources we have do not show what came of this teaching in his own day." Plain honest limit. **Reaches the level.**
4. **No hanging sentences.** Weakest: "In the eighth century Bede copied Jerome's words into his chronicle." (B2). The close on the record's limit finishes the story, as Mark's condition for this Who requires. **Fails until B2 is fixed.**
5. **Everything relevant.** The sentence that says why he mattered, as an idea, is there: a bishop "who had much to teach apart from his death ... must not be passed over". Weakest: the Bede sentence (B2). Beside Methodius, which weighs a thin record and moves on. **Fails until B2 is fixed.**

### Sentence test
16 sentences; 1 marked: "In the eighth century Bede copied Jerome's words into his chronicle." (B2). The property-selling sentence is noted as the nearest candidate after it (non-blocking).
