# Round 1 review, group g4

Briefs: justin-martyr (batch1), tatian (batch2), bardaisan-of-edessa (batch2), clement-of-alexandria (batch1), dionysius-of-alexandria (batch2).

## Step 0: the blind pair (written before opening the pattern, the bar or the batch)

X (an Alexandrian teacher of Scripture) is the stronger Standard-v1 brief. Reasons:

- X opens on one concrete scene (persecution, the arrested father, the hidden clothes, the letter) and each later paragraph carries one stance and then what came of it, each link carried by a named witness (Jerome's defence of his Latin Job by the marks; the Philocalia opening with the reading chapters; Athanasius citing him for Nicaea; Gregory and Athenodorus becoming bishops). Almost every sentence moves the story.
- Y (Justin) has a strong opening and a strong trial scene, but it wanders in two places. The Tatian sentence ("His hearer Tatian did not follow him here...") is a side-step into another person's stance, not something that came of Justin's. The Crescens run takes four sentences (expected plot, Tatian says, Eusebius says, the trial account does not name him) to land a point that is partly a source-critical aside. "No answer to him survives in the sources we have" is a correct limit but a flat one. The Marcion paragraph sits at the end after the death, out of the life's order and with a consequence (Irenaeus quoting him) that is weaker than the ones X gives.
- X's weak spot: "Its church was Alexandrian Christianity" reads as a label inserted to meet the tradition rule, and is clumsy to the ear. Y names its tradition more naturally ("one of the second-century Greek apologists, the Christians who wrote in Greek to defend their faith").

Net: X is tighter and carries more stance-to-consequence links; Y is sound but has three sentences that do not move Justin's story.

After the full read: X was the bar brief (Origen), Y was the batch brief (Justin Martyr). The preference for the bar had concrete reasons, and they return below as Justin B1 and the Crescens note.

## Bar briefs compared against

All ten in `Who-Profiles/bar/` were read. The comparisons below use mainly Origen, Methodius of Olympus (for thin records: Tatian, Bardaisan), Ephrem the Syrian (for Bardaisan, which shares its Sozomen material), Athanasius of Alexandria (for witnesses set against each other: Justin, Dionysius), Gregory of Nazianzus (for briefs that move from one stance to the next) and Gregory of Tours (Standard v1 opening and impact).

## Readability (`python3 -m engine.m1.profile_readability --report`)

| Brief | Words | Grade (full) | Grade (names out) | Reading ease (names out) | Words a sentence | Joining words /100 | Short sentences | Tool |
|---|---|---|---|---|---|---|---|---|
| justin-martyr | 313 | 8.8 | 7.8 | 71.6 | 18.4 | 1.0 | 12% | pass |
| tatian | 322 | 9.6 | 8.2 | 70.1 | 18.9 | 0.3 | 6% | pass |
| bardaisan-of-edessa | 328 | 9.3 | 7.7 | 72.6 | 18.2 | 1.5 | 0% | pass |
| clement-of-alexandria | 298 | 9.6 | 7.9 | 71.9 | 18.6 | 0.3 | 6% | pass |
| dionysius-of-alexandria | 341 | 9.8 | 8.5 | 69.8 | 20.1 | 0.6 | 0% | pass |

Tatian now counts 322 words, not the 329 in the assignment, so only Bardaisan and Dionysius are over 325. Dionysius sits close to the grade ceiling of 10.

Every quotation in the five matches its FINAL reading in `renderings/comparison.md`: E20 to E22 (Justin), E23 (Tatian), E29 and E30 (Clement), E31 (Dionysius). Bardaisan has no quotation. Each final covers its printed span and adds nothing. I checked E20, E23 and E31 against the printed English and the Greek at the cited lines.

---

## justin-martyr: BLOCKED (2)

### Blocking

**B1. "His hearer Tatian did not follow him here, for Tatian's Address to the Greeks bids their learning farewell."**
- Evidence: Irenaeus, Against Heresies I.28.1 (`anf01_apostolic-fathers-justin-irenaeus.xml` 33663-33665), shows only that Tatian was Justin's hearer. Tatian, Address 35 (`anf02_...xml` 7258-7260), bids farewell to "the arrogance of Romans and the idle talk of Athenians, and all their ill-connected opinions". That farewell is to Greek pride and opinions; it is not a reply to Justin's teaching on the Word. In Address 18 (A2 6526) Tatian still calls Justin "most admirable". No held source says Tatian rejected that teaching. "Did not follow him here" is the writer's own joining (the writer flags it), and it is told as fact.
- It also fails the sentence test. It tells Tatian's stance, not what came of Justin's.
- Fix I would accept: cut the sentence and give the honest limit the writer offers ("The sources we have do not show who took this teaching up"), or end the paragraph on Socrates.

**B2. "No answer to him survives in the sources we have."**
- Evidence: Eusebius moves straight from the petition to an edict. "And the same emperor having learned also from other brethren in Asia of the injuries ... thought it proper to address the following ordinance to the Common Assembly of Asia" (IV.13, `npnf201_...xml` 22652-22667). The ANF prints that edict right after the First Apology (A1 16583-16625; its heading reads "[Regarded as spurious]"). The edict ends: "if any one has a matter to bring against any person of this class, merely as such a person, let the accused be acquitted". That is the very ruling Justin asked for. So the held record does not fall silent. Eusebius presents an imperial answer, though not one sent to Justin, and the document itself is doubted. A flat "no answer" misleads the listener on the outcome of the brief's central stance.
- Fix I would accept: say what the record holds, in one sentence. For example: Eusebius follows the petition with an edict, said to be the emperor's and sent to Asia after other Christians complained, that no one be punished for the name alone. Put the doubt about the edict on the card under What is uncertain, with no scholar named in the brief. Or narrow the sentence so it is plainly true and not misleading: no reply addressed to Justin survives, and the edict Eusebius sets after his petition was sent to Asia. "To him" alone does not do this, since a listener hears "nothing came of it".

### Non-blocking
- The Crescens run takes four sentences (Justin's expectation, Tatian, Eusebius, the trial account's silence). The dispute belongs in place, but "though the surviving account of his trial never names Crescens" is an argument about sources, McGiffert's argument told through ancient texts. It could be shortened.
- "Cynic philosopher" is not explained for a general listener.
- The Dialogue with Trypho, Justin's argument with a Jew from the prophets, is a real stance and the brief does not tell it. It draws on the Dialogue only for the conversion story. The held sources show no consequence for it, so leaving it out is defensible. The writer should say so in the refs.
- "In Rome ... wrote to the emperor": that he wrote in Rome is an inference from Martyrdom 2 (A1 29308-29310). It is acceptable as widely accepted.

### Craft tests
1. Storytelling. The line holds: a philosopher who asked to be judged by deeds and not by a name died for the name. Weakest: "Justin had also written against Marcion, who preached a god greater than the Creator." Bar: Gregory of Tours, "Two centuries later the historian Paul the Deacon sent readers to..." It reaches the level: a late stance with its consequence, joined by "also". **Pass.**
2. Flow. Weakest link: "No answer to him survives in the sources we have. He expected to be plotted against, he wrote, perhaps by Crescens". Bar: Origen, "because everyone else had fled". The step is by order only, and the B2 rewrite should mend it. Elsewhere "So, he wrote" and "since a name alone proves nothing" join act and reason at bar level. **Pass, once B2 is fixed.**
3. No AI tells. Weakest: "since a name alone proves nothing good or bad". It is Justin's own argument (A1 14037-14060), not a saying of ours. Bar: Chrysostom's opening. **Pass.**
4. No hanging sentences. Weakest: "Tatian says Crescens tried to have Justin killed." It is short but carried by the witnesses on either side of it. The close (Irenaeus quoting the book) finishes the Marcion thread. Bar: Ephrem's close. **Pass.**
5. Everything relevant. Weakest: the Tatian sentence (B1). Bar: Methodius, "That reply is lost, but Jerome counted it among the answers that had met Porphyry well." **Fails** on that sentence. The fix is B1.

### Sentence test: 1
- "His hearer Tatian did not follow him here, for Tatian's Address to the Greeks bids their learning farewell." (also B1)
- Borderline, not counted: the clause "though the surviving account of his trial never names Crescens".

---

## tatian: BLOCKED (4)

### Blocking

**B1. "Theodoret of Cyrrhus wrote that even people who held the apostles' teaching had used Tatian's book in all simplicity as a short version, without seeing the harm in how it was made."** It may not stand.
- Evidence: Theodoret's text (Compendium of Heretical Fables I.20) is in no held file. `npnf203` and the PG 82 Theodoret volume have no Diatessaron passage; I searched both for "Diatessaron" and διὰ τεσσάρων. What is held is Hope Hogg's introduction (`anf09_gospel-of-peter-diatessaron-origen-commentaries.xml` 1909-1914). It quotes two clipped fragments in English, and the verb that carries the claim is Hogg's own: Theodoret wrote, "…Even those that follow the apostolic doctrines, not perceiving the mischief of the composition," used "the book too simply as an abridgment." "Used" sits outside the quotation marks. So the sentence gives Theodoret a claim whose frame is a modern editor's and whose text no reviewer can check. Under the pattern ("What only a modern scholar establishes ... never told flat in the brief") and `CLAUDE.md`'s source-fidelity rule, it goes to the card with Hogg named.
- Fix I would accept: cut it. If Theodoret is wanted, vendor PG 83 (Haer. fab. I.20) and tell it from his own text.

**B2. "In the fifth century Rabbula, bishop of Edessa, ordered every church to keep and read a copy of the separate Gospels."** It may not stand.
- Evidence: the order is held only as Hogg quotes it from Overbeck's edition (A9 1914-1920). That edition is not held, and the order does not name the Diatessaron. "Separate Gospels" is Hogg's gloss ("i.e., not the harmonized or mixed gospel"), and so is the link to Tatian's book. Placed right after the Diatessaron, the sentence tells the listener that Rabbula acted against Tatian's book, and only a modern editor says that.
- Fix I would accept: cut it, with B1. The rewritten Diatessaron paragraph then ends on held ancient witnesses. Eusebius says some still had the book (E 26424-26433, 26478-26479). The Teaching of Addai, called a legend, shows it read at Edessa (A8 62103-62107). Epiphanius, Panarion 46.1, says "it is said the Diatessaron gospel was made by him" (`epiphanius_panarion-haer-34-64-gcs-bd2-grc_holl1922.txt` 16017-16031). Rabbula and Theodoret go to the card as Hogg reports them.

**B3. "He belongs to Syriac Christianity, the church that grew up around Edessa and Nisibis, because of a gospel book he made."** (items 16 and 18)
- This is our own classification and our reason for it, put into the brief. It is the "label of ours" that item 18 rules out. The opening also never says what was going on (item 16): it gives a year, Rome and a birthplace, but no moment.
- The held sources give the tie to Syria directly, so no label is needed. Epiphanius says he was "Syrian by race" and that after Justin's death he went from Rome to the East and set up his school in Mesopotamia (EpH 15994-16001). Clement calls him "Tatianum ... Syrum" (`anf02_...xml` 7493).
- Fix I would accept: rewrite the opening so that the tradition is said as a fact the sources carry. For example: Syrian by birth, he went back east after Justin's death, and Syriac Christianity read his gospel book. Give one fact about the moment, such as Justin's death or the persecution of the name, which the Justin brief already carries from held texts.

**B4. The teaching on marriage is told with no consequence and no stated limit** (item 15).
- The brief tells the stance through Irenaeus and Clement and then moves to the Diatessaron. The held sources do show what came of it. Irenaeus places Tatian among the Encratites, who "preached against marriage", and says he "first introduced the blasphemy" (A1 33655-33665). Eusebius says "It is said that Tatian was the author of this false doctrine" (IV.28, E 26181-26186) and calls him "their original founder" (IV.29.6, E 26424-26425). Epiphanius says the Encratites hold it from him "by succession" (EpH 16004-16007). The writer cut this as "a dispute about a label". It is the consequence of the stance, and the dispute (Irenaeus: the movement sprang from Saturninus and Marcion; Eusebius: "it is said") can be told in place in one sentence.
- Fix I would accept: one sentence after Clement. The Encratites, who refused marriage, were traced to him by Eusebius ("it is said"), while Irenaeus says they began before him. Or state plainly where the record stops. The space comes from B1 and B2.

### Non-blocking
- "Around 165" rests on modern dating of Justin's death (E 23774-23781, McGiffert). Epiphanius dates Tatian's school to the twelfth year of Antoninus Pius (EpH 15997-15998). "In the middle of the second century" would claim only what both sides accept.
- "Admitted to the mysteries" will not be clear to a general listener. "Valentinus" is not explained here.
- The rendering E23 is used exactly. Its card note (that the old English overstated the comparison) must reach the card.

### Craft tests
1. Storytelling. Line: a pupil of Justin found the faith in non-Greek books, argued that they were older than Greek learning, broke with the church in his opponents' telling, and left one gospel for four. Weakest: the tradition sentence (B3). Bar: Benedict, "He was Benedict of Nursia, and the early Benedictines of Italy begin with him." **Fails at the opening.** The fix is B3.
2. Flow. Weakest link: the Diatessaron paragraph, five sentences in a row each starting with a witness ("Eusebius says ... The Teaching of Addai ... shows ... In the fifth century Rabbula ... Theodoret ... wrote"), with no link between them. Joining words are 0.3 per 100. Bar: Ephrem, "Ephrem feared the people would absorb those ideas, so he learned the same meters...; From that time on, Sozomen says, the Syrians sang the songs of Ephrem." **Fails.** The fix is the paragraph rewrite that B1, B2 and B4 already require; it should be one joined telling of what became of the book.
3. No AI tells. Weakest: "His later teaching comes to us through opponents." It is a statement about sources at the start of a paragraph, but the hostile-witness rule asks for one. Bar: Benedict, "Nearly all we know of his life comes from Gregory's Dialogues". **Pass.**
4. No hanging sentences. Weakest: "Eusebius says some still had it in his day." The close (Theodoret) is a quotable judgment resting on an editor (B1). Bar: Chrysostom's close. **Pass once B1 is fixed**; the new close must finish the book's story.
5. Everything relevant. Weakest: the tradition sentence. Bar: Methodius. **Fails on that sentence** (B3).

### Sentence test: 3
- "He belongs to Syriac Christianity ... because of a gospel book he made." (B3)
- "In the fifth century Rabbula ... separate Gospels." (B2; as told it does not carry Tatian's story without the editor's gloss)
- "Theodoret of Cyrrhus wrote that ..." (B1)

---

## bardaisan-of-edessa: CLEARS

I checked every claim at its lines: A8 67896-67926, 68335-68342, 68394-68400, 68604-68612, 68959-68998; E 26522-26530, 26630-26657; EpH 26322-26336, 26418-26427, 26470-26510; EP 1938 and stanzas VIII, XI, XIII; S 32076-32104. All hold.

**The Epiphanius clause** ("who refused an emperor's companion when urged to deny his faith"): the Greek at EpH 26427 and 26476 reads Ἀπολλωνίῳ δὲ τῷ τοῦ Ἀντωνίνου ἑταίρῳ ἀντῆρε, παραιτούμενος ἀρνήσασθαι τὸ Χριστιανὸν ἑαυτὸν λέγειν. Holl's apparatus gives the variant παραινούμενος (manuscripts M and U). On either reading he stood up to Apollonius, the companion of Antoninus, and would not deny that he called himself a Christian. "When urged" follows the variant, and the main text implies it. The sense stands. Holl's note (after EpH 26510) confirms that Eusebius tells the opposite order ("die umgekehrte Behauptung"), so "two later writers tell his life in opposite orders" is sound.

**"Around 180"**: Eusebius sets him "in the same reign" as the chapters before, Marcus Aurelius (E 26525-26529). Epiphanius has him live past Abgar into the time of "Antoninus ... Verus" (EpH 26400-26402). 180 lies inside the ancient placing, and "around" is honest. It may stand, provided the card says it is approximate.

### Non-blocking
- "Epiphanius says he began as an excellent Christian, a friend of Abgar, who refused an emperor's companion..." The ear can hang "who" on Abgar. Recast it, for example: "...a friend of Abgar, and that he stood up to an emperor's companion who urged him to deny his faith."
- Eusebius and Epiphanius both write against heresies, and Epiphanius calls him a heretic who fell. A few words marking them as opponents ("two later writers, both hostile") would meet item 6 more plainly. Ephrem is clearly marked.
- The opening gives a place and a king but little of what was going on. Eusebius's "heresies were abounding in the region between the rivers" (E 26525-26527) is available.
- "Ephrem wrote hymns to the same melodies": Sozomen has Ephrem learn Harmonius's meters and write "according to the law of the ode established by Harmonius" (S 32096-32103). "The same meters" is closer, as the Ephrem bar has it.
- "Valentinians" is not explained.

### Craft tests
1. Storytelling. Line: a teacher at Edessa argued, in his pupil's record, that people are free of the stars; his opponents disagreed on when he went wrong; Ephrem's answer to him and his son gave the Syrians their hymns. Weakest: "Two later writers tell his life in opposite orders." Bar: Methodius, "Socrates of Constantinople says Methodius attacked Origen ... Both men admired Origen, so neither is a neutral witness." **Pass.**
2. Flow. Weakest link: "...put his Syriac works into Greek. Two later writers tell his life in opposite orders." Bar: Gregory of Nyssa, "After Basil died, Gregory wrote, he 'inherited the controversy'". The turn is abrupt, but the paragraph holds together. Elsewhere it joins well ("so its words are a pupil's report", "yet he denies", "so that those in Parthia"; 1.5 joining words per 100). **Pass.**
3. No AI tells. Weakest: "He grants the stars some power over health and fortune, yet he denies that they rule what a person chooses." It is the shape of his own argument (A8 68394-68400, 68994-68997). Bar: Athanasius, "If the Son were only a creature...". **Pass.**
4. No hanging sentences. Weakest: "Bardaisan admits there that he once followed the astrologers." It leads into the next sentence. The close (the Syrians sang Ephrem) ends the story of the body stance. Bar: Ephrem, "From that time on, Sozomen says, the Syrians sang the songs of Ephrem." **Pass.**
5. Everything relevant. Weakest: "A man named Avida had asked why God did not make people unable to do wrong." It is the question the whole book answers. Bar: Ephrem's famine exchange. **Pass.**

### Sentence test: 0

### Length (328, three words over 325)
Each part earns its place: the scene and its trust note, the freedom stance with Eusebius's consequence, the dispute over his life told in place, and the body stance with Ephrem and Sozomen. If words must go, take "Bardaisan admits there that he once followed the astrologers" and fold it into the next sentence ("He admits he once followed the astrologers, and still grants the stars...").

---

## clement-of-alexandria: BLOCKED (1)

I checked the claims at CA 27476-27500, 27668-27692, 27880-27896, 32104-32111, 40953-40960, 51302-51356; E 28695-28705, 33038-33086, 33595-33618, 34328-34357; J6 16475-16481, 16624-16643. All hold, with the notes below.

**"Around the year 200"**: Eusebius puts Clement in charge of the instruction "at that time" and says the Stromata were written under Severus (E 33040-33043, 33080-33086). Jerome says he flourished under Severus and his son (J3 40278-40279). It may stand, marked approximate on the card.

**Alexander as "pupil"**: Alexander calls Clement "my master and benefactor" and says it was through Clement and Pantaenus that he came to know Origen (E 34354-34357). "Pupil" is a fair reading of "my master"; McGiffert draws the same conclusion (E 34357), but the ancient words carry it. It may stand. "Alexander, who called Clement his master" would be tighter.

### Blocking

**B1. The opening has no setting moment** (item 16): "Around the year 200, Clement of Alexandria was a presbyter in that city in Egypt. He led the Christian school of Alexandria, where converts were taught the faith."
- It gives a year, a place and the tradition, but nothing of what was going on. It is also the "The X was Y" naming opening the signals warn of. Every bar opening gives the moment (Origen: Severus's persecution; Gregory of Tours: kings at war). The held sources offer one already in the brief: believers who spoke against Greek philosophy (CA 27668-27691).
- Fix I would accept: rewrite the opening so that its first two or three sentences carry the moment. For example, open on the quarrel over Greek learning among believers at Alexandria and bring Clement in as the school's head who answered it. Do not reintroduce McGiffert's 202 flight.

### Non-blocking
- "When Jerome was asked why he quoted pagan writers himself, he pointed to Clement": in Letter 70 Jerome points to a long list of writers, Clement among them (J6 16475-16643). Say "pointed, among others, to Clement".
- The brief tells the Valentinian stance with a plain limit ("The sources we have show no reply from the Valentinians"). That is sound.

### Craft tests
1. Storytelling. Line: a man who searched the Greek world for a teacher came to lead the school at Alexandria and argued that philosophy prepares for Christ, and Origen and Jerome took that up. Weakest: the opening (B1). Bar: Origen's opening. **Fails at the opening.** The fix is B1.
2. Flow. Weakest link: "...drawn from the heart of philosophy. / The followers of Valentinus, as Clement reports them, left faith to simple believers..." Bar: Gregory of Nazianzus, "Apollinarius held that Christ had no human mind. Against him Gregory wrote..." This is the same move the bar makes. Joining words are 0.3 per 100, but the acts are joined to their reasons ("as if it dragged believers away", "since they were saved by their nature"). **Pass.**
3. No AI tells. Weakest: "Clement answered that God is the cause of every good thing." It is his own words (CA 27887-27888). Bar: Origen, "He held that the Son had always been with the Father". **Pass.**
4. No hanging sentences. Weakest: "The sources we have show no reply from the Valentinians." Bar: Gregory of Nyssa, "The sources we have do not show what came of this teaching in his own day." The close finishes the pupils' thread with a contemporary witness. **Pass.**
5. Everything relevant. Weakest: "Eusebius of Caesarea judged that this teacher was Pantaenus, who led the school before Clement." It carries what Clement inherited. Bar: Chrysostom, "At Antioch John had trained under Diodore". **Pass.**

### Sentence test: 0

---

## dionysius-of-alexandria: CLEARS

I checked the claims at E 37636-37750, 38854-38860, 38922-38925, 39320-39405, 40108-40117, 20528-20552; A 28435-28448, 29440-29455, 29518-29528, 29540-29549, 29620-29625, 29868-29885; B 23706-23730. All hold.

**"Around 250"**: Eusebius gives "the very hour when the Decian persecution was commanded" (E 37644-37645). Decius's short reign makes "around 250" widely accepted and not one scholar's reckoning. It may stand, marked approximate on the card.

**Germanus and flight**: the brief does not say Germanus accused him of running away. It says "another bishop later spoke against him" (Eusebius VII.11, "endeavoring to slander him", E 40110-40116) and "Dionysius answered that he had not fled by his own choice" (VI.40, E 37640-37642, from the letter against Germanus). The inference is left to the listener, and the brief claims only what the two lines carry. It stands.

### Non-blocking
- Rebaptism is a stance the held sources show: Eusebius VII.5, 7, 9 (E 39445-39457, 39635-39696, 39809-39857), Jerome, Lives 69 (J3 40844-40846), and Basil 188. Item 15 asks for every stance, and the writer's reason for leaving it out (the witnesses differ on the stance) is not a ground the pattern gives. On weight it is close to Nepos and the Revelation, and adding it would take the brief past 2:30. I raise it for the coordinator rather than block. If it stays out, the card must carry it with its four witnesses.
- "Eusebius ... himself left open which John saw the Revelation": in III.39.6 Eusebius leans toward the second John, "it is probable that it was the second, if one is not willing to admit that it was the first" (E 20548-20552). "Leaned the same way but left it open" is more exact.
- Basil's sharper words, that Dionysius "first gave men the seeds" of the Anomoean impiety (B 23712-23714), are the stronger consequence. The brief's gentler gloss is accurate, though.
- The grade is 9.8 and sentences average 20.1 words. Read aloud, "Dionysius, who had ordered that the dying among them be forgiven, wrote to him:" carries a nested clause before the quotation.

### Craft tests
1. Storytelling. Line: a pupil of Origen, made bishop in a persecution, spent his letters holding the church together against Novatian, Sabellius and Nepos, and later writers leaned on or disputed each. Weakest: "An Egyptian bishop, Nepos, found in the Revelation of John a thousand years of bodily pleasure on earth." Bar: Gregory of Nazianzus, "Apollinarius held that Christ had no human mind." **Pass**, at the bar's level.
2. Flow. Weakest link: from the wedding rescue to "Then Novatian set himself up as a rival bishop at Rome". Bar: Athanasius, "That stand cost him his city again and again." "Then" carries only the order of events, and no source gives more. Inside each paragraph, act and result are joined ("For this he was accused", "because Dionysius had explained himself", "so unlike ... that he judged"). **Pass.**
3. No AI tells. Weakest: "Later he could tell the bishop of Rome that the churches of the East, once divided over Novatian, were all at peace." It is his own report (E 39345-39404). Bar: Gregory of Nazianzus, "In his farewell he said the city's other churches were full again". **Pass.**
4. No hanging sentences. Weakest: the close, "Eusebius of Caesarea copied the argument out and himself left open which John saw the Revelation." It finishes the Revelation thread, but it is the weakest close in the group: it is about Eusebius, not Dionysius. Bar: Gregory of Nyssa, "In 692 the council in Trullo set its seal on his canons". **Pass**, narrowly. The fix for "left open" above would strengthen it.
5. Everything relevant. Weakest: "He had been a pupil of Origen and had led the Christian school of Alexandria before he became bishop." It carries what he inherited and names the tradition. Bar: Chrysostom on Diodore. **Pass.**

### Sentence test: 1 (borderline)
- The close sentence on Eusebius. It is kept as the consequence, but it serves Dionysius's line only through "copied the argument out".

### Length (341, 16 words over 325)
The scene (two sentences) and its flight answer earn their place: they are the personal half, and they carry the charge he answered. Each of the three stances carries a consequence from held sources, and Basil's sentence is the other side of a contested point. Nothing here is padding. If words must go, the first candidate is "When another bishop later spoke against him, Dionysius answered that he had not fled by his own choice", which could be folded into the scene as his own words ("he wrote later, to a bishop who spoke against him, that he had not fled by his own choice"). The second is to shorten the close.

---

## Writers' flags: rulings

| Brief | Flag | Ruling |
|---|---|---|
| Justin | "His hearer Tatian did not follow him here" | May not stand (B1) |
| Justin | "No answer to him survives" | May not stand as written (B2) |
| Tatian | Theodoret sentence | May not stand (B1); card, with Hogg named |
| Tatian | Rabbula sentence | May not stand (B2); card, with Hogg named |
| Bardaisan | Epiphanius clause in rough OCR Greek | Sense confirmed, including the manuscript variant; stands |
| Bardaisan | "Around 180" | Stands; card says approximate |
| Clement | "Around the year 200" | Stands |
| Clement | Alexander as "pupil" | Stands, from Alexander's "my master" |
| Dionysius | "Around 250" | Stands |
| Dionysius | Germanus accused him of running away | The brief does not claim it; stands |
