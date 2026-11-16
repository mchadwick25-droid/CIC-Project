# Round 2, group g5: targeted recheck of the round 1 findings

Reviewer: Opus, the same independent reviewer as round 1. I made no model or API calls and changed no file but this one. I read `git diff 8e856fc3..HEAD` for the four briefs, their four refs files and `renderings/`. The brief changes are all in commit 41308adc. The only change under `renderings/` is two "Brief carries" lines for E15 and E21, which belong to other groups. I rechecked only what changed. I checked every new or changed sentence by hand against `cic/texts/`. Each refs file's "Round 1 revision" section was read as a claim to check.

Bar briefs compared against: Gregory of Tours and Benedict of Nursia (Standard v1 openings and witnesses), Methodius of Olympus (my round 1 comparator for a thin, hostile record). I also read `Who_Profile_Pattern.md`, the sections "Standard v1", "The brief", the review checklist and "Working rules".

## Readability (`python3 -m engine.m1.profile_readability --report`)

| Brief | Words | Grade (full) | Grade (names out) | Reading ease (names out) | Words a sentence | Joins /100 | Short sentences | Tool |
|---|---|---|---|---|---|---|---|---|
| marcion-of-pontus | 344 | 8.7 | 6.9 | 79.6 | 19.1 | 0.6 | 11% | pass |
| valentinus | 337 | 9.3 | 7.7 | 71.8 | 17.7 | 0.9 | 11% | pass |
| hippolytus-of-rome | 315 | 9.8 | 7.9 | 75.8 | 21.0 | 0.3 | 0% | pass |
| novatian | 316 | 9.1 | 7.3 | 73.9 | 17.6 | 0.9 | 6% | pass |

All four are inside grade 8.0 to 10.0 on the full text, and all have reading ease above 60 with names out. The figures match the writer's claims in each refs file. Hippolytus sits near the ceiling, with 0.3 joins per 100 and no short sentences, so I read it again for long sentences. None loses the ear.

No brief says "the tree", "on the map" or "the census". No modern scholar is named. No quotation was added, removed or reworded. The quotations in all four still match `comparison.md` E24, E25, E28, E32 and E33 FINAL word for word.

---

## marcion-of-pontus: CLEARS

**B1, the Polycarp exchange: CLOSED.**
- New sentence (line 1): "Once Marcion met him and, asking to be owned as a brother, said, "Do you recognize us?""
- Irenaeus III.3.4 (`anf01` 39882-39886): "Polycarp himself replied to Marcion, who met him on one occasion ... Such was the horror which the apostles and their disciples had against holding even verbal communication with any corrupters of the truth". Eusebius IV.14 has the same (`npnf201` 22977-22984). The verb in every held witness is "recognize, acknowledge" (E24, original check). So "asking to be owned" is the plain sense of the verb, and Irenaeus's next sentence makes the reply a refusal of fellowship. "Once" matches "on one occasion". The listener now hears the reply as a refusal.
- The gloss is a reading of the verb. The card must keep the E24 card note under What is uncertain, as the refs file says it will.

**B2, the opening: CLOSED.**
- New lines (line 1): "Around 150, rival teachers were at work in the church of Rome. Irenaeus of Lyon names Valentinus and Cerdo, and after them Marcion of Pontus ..." and "When Polycarp, the old bishop of Smyrna, came to Rome, Irenaeus says, he turned many away from these teachers."
- Irenaeus III.4.3 (`anf01` 39968-39984): "Valentinus came to Rome in the time of Hyginus ... Cerdon, too, Marcion's predecessor, himself arrived in the time of Hyginus ... Marcion, then, succeeding him, flourished under Anicetus". The wording "after them Marcion" is exact.
- III.3.4 (`anf01` 39870-39873): "coming to Rome in the time of Anicetus caused many to turn away from the aforesaid heretics to the Church of God". The "aforesaid heretics" are Valentinus and Marcion (39871). Holds.
- The opening now gives the year, the place and region, the tradition (Marcionism) and what was going on. Item 16 passes.

**Changed sentences from the non-blocking notes: checked.**
- "The cut-down Scriptures drew answers." Holds. It fixes the round 1 note.
- "... which put him out. His own churches spread all the same." The split reads cleanly.
- "A century later Theodoret of Cyrrhus, a bishop in Syria, led eight villages of them over to his own faith." Letter 81 (`npnf203` 31511-31513) carries it. "Them" points back to "his followers". "A century later" from Epiphanius, about 375, gives about 450. Letter 81 is about 448. Holds.

**Non-blocking note N1 (new).** The Theodoret sentence used to say "wrote that he had led". It now tells his own report flat. It rests on one source, Theodoret's own letter about his own work. The rule names a witness where a point rests on one source. Nothing in it is false, so this is not blocking. "... Theodoret of Cyrrhus, a bishop in Syria, wrote that he had led eight villages of them over to his own faith" would restore the marking for three words.

**Length: the stated reason holds.** 344 words is about 2:18 spoken. That is inside the 2:30 stretch (about 375 words), so no batch note is owed. The added words are the setting that round 1 asked for under item 16, plus Polycarp turning many away. That is a real consequence, and it also sets up the scene. Theodoret's sentence was shortened to pay for part of it. I ran the sentence test again on the new opening. Every new sentence serves the line, so no padding was added.

---

## valentinus: CLEARS

**B1, "wrote independently": CLOSED.**
- New sentence (line 5): "Clement had Valentinus's own letters before him, and on two points he and Irenaeus agree."
- Clement, Stromata II.20 (`anf02` 34289-34302): "Valentinus too, in a letter to certain people, writes in these very words". The second witness now rests on Clement's access to Valentinus's words, which the record carries. The claim of independence that Eusebius VI.13 contradicts is gone.

**B2, "only in Clement": CLOSED.**
- New sentences (line 3): "Valentinus's own words survive only in a few passages his opponents quote. Most are in Clement of Alexandria, who quotes them in order to answer them."
- This is true against the held files. The Refutation's psalm (`anf05` 9787-9802) and vision (10053-10057) are passages quoted by an opponent. Clement holds more of them than the Refutation does. "Only" is now exact within what is held.

**B3, the opening: CLOSED, with non-blocking note N2.**
- New sentences (line 1): "Other rival teachers came in those years too, Irenaeus of Lyon says: Cerdo, and Marcion after him. Irenaeus, who wrote against them all, says Valentinus arrived when Hyginus was bishop ..."
- Irenaeus III.4.3 (`anf01` 39968-39984) carries the setting, as quoted under Marcion B2. "Who wrote against them all" holds, since Book I covers all three.
- Note N2 (NON-BLOCKING): Irenaeus says Cerdo "arrived", but of Marcion he says only that he "flourished under Anicetus". "Came ... Marcion after him" gives Irenaeus a verb he uses for Cerdo, not for Marcion. Tertullian, who puts Marcion in the church at Rome, carries the fact itself, so nothing false reaches the listener. Two sentences in a row also say "Irenaeus ... says". A version that is exact and avoids both: "Irenaeus of Lyon, who wrote against them all, says Valentinus arrived when Hyginus was bishop and stayed through the time of two more bishops. In those same years, he says, Cerdo arrived, and Marcion followed him."

**Tertullian sentence (paid-for fold): checked.** "Tertullian of Carthage, another opponent, says Valentinus expected to be made bishop, because he was an able and eloquent man. When a man who had suffered for the faith was chosen instead, he broke with the church." This matches Against the Valentinians 4 (`anf03` 43109-43112): "had expected to become a bishop, because he was an able man both in genius and eloquence ... another obtained the dignity by reason of a claim which confessorship had given him, he broke with the church". Holds.

**"Irenaeus sets out a fuller system, which Clement does not confirm": checked.** It is exact against the held files, as round 1 proposed.

**Non-blocking note N3 (pre-existing, slightly sharpened).** In "Most are in Clement of Alexandria, who quotes them in order to answer them. In one letter he compares the heart ...", the "he" now follows a sentence whose only man is Clement. The quotation tag "Valentinus wrote" sorts it out a sentence later. "In one letter Valentinus compares the heart ..." with the tag shortened to "he wrote" would fix it. This is not blocking.

**Length: the stated reason holds.** 337 words is about 2:15, inside the stretch. The growth is the item 16 setting. The folded Tertullian transition paid for part of it. I ran the sentence test on the new sentences and found no padding.

---

## hippolytus-of-rome: CLEARS

**B1, rank told as settled: CLOSED.**
- New sentence (line 1): "Hippolytus was a teacher and writer there, in the Roman church of the third century."
- The opening now gives no rank. "Presbyter" stays as the list of 354's word: "Pontianus episcopus et Yppolitus presbiter" (`chronica-minora-liber-genealogus_mommsen1892.txt` 13078). "Bishop and martyr" stays as Theodoret's (`npnf203` 20261-20262). Each title is told as its witness's word. Nothing is told as settled, and the brief no longer contradicts itself. "Teacher" is carried by the Refutation's author acting with authority over his own following ("by us forcibly ejected from the Church", `anf05` 13885-13887), and by Theodoret counting him among the teachers. Eusebius's and Jerome's wording goes to the card, as the refs file says.

**Changed sentences from the non-blocking notes and the sentence test: checked.**
- "In a second quarrel, over grave sins, Hippolytus had put offenders out of the church." `anf05` 13884-13887. Holds.
- "By his own account, crowds went over to Callistus, whose following still stood when he wrote and called itself a Catholic church." `anf05` 13913-13919 ("crowds of these dupes stream together into his school") and 13950-13960 ("attempt to call themselves a Catholic Church", "whose school continues"). Holds. The unsourced "lost this fight" is gone.
- "A calendar of martyrs in the same book names the two together, in one entry, among the martyrs buried at Rome." The entry "Ypoliti in Tiburtina. et Pontiani in Calisti" (`chronica-minora-liber-genealogus_mommsen1892.txt` 12911-12913) names two Roman cemeteries in one line of the martyrs' burial list. Holds, and it now says what the entry shows.
- "His books outlived the quarrel, and Jerome says his table for the date of Easter moved Eusebius of Caesarea ..." (`npnf203` 40692-40695). Holds.

**Non-blocking note N4 (new).** "By his own account" used to come with Hippolytus named in the same sentence. Now it follows "Callistus, he charges, took them in ...", so "his" could be heard as Callistus's account. "He charges" points to Hippolytus, so a careful listener will get it, but trust turns on whose account this is: an enemy granting the crowds. "By Hippolytus's own account, crowds went over to Callistus ..." makes it plain.

---

## novatian: BLOCKED, 1 new blocking

**B1, the story in two passes: CLOSED.** I checked the reorder as one story.
- The line now runs: 251, Rome, Decius, the lapsed taken back; Novatian refuses, and Novatianism comes of it (lines 1). The rival consecration is told by both witnesses at once, with Socrates's leaning and Cornelius's enmity each marked. Then comes his letter to the churches, which is his case (line 3). Then the synod, the provinces taking sides, Nicaea, Socrates's own day and Rome under Celestinus (line 5). The book On the Trinity comes last, as the second stance with its consequence (line 7).
- A listener could retell it. The transition "For the split itself, most of what we have comes from his enemies" is gone. The hostile marking now sits in "A letter of Cornelius, kept by Eusebius of Caesarea, tells it as an enemy."
- Sources for the moved sentences: Socrates IV.28 (`npnf202` 14082-14087), "on being afterwards elevated to the episcopacy by such bishops as entertained similar sentiments, he wrote to all the churches". So "Novatian then wrote" follows Socrates's order. Cornelius (`npnf201` 38518-38532), "by the tenth hour, when they had become drunk and sick, he compelled them by force". No claim is added. The writer's account holds.
- Craft, flow: the weakest link is now "... until Bishop Celestinus took them away." to "Novatian also wrote a book On the Trinity." It steps back two centuries. Beside Gregory of Tours, "He held the same ground against the Arians of Spain", it is a plainer turn, but it opens a second stance that is told with its consequence. It reaches the level. Storytelling reaches the level.

**B2, the Trinity stance without consequence: CLOSED.**
- New close (line 7): "In Jerome's day many still read it, though under the name of Cyprian of Carthage, who had sided with Cornelius."
- Jerome, Lives 70 (`npnf203` 40895-40897): "a great volume On the Trinity ... which many mistakenly ascribe to Cyprian." Many ascribing it to Cyprian shows that many had it, which "still read it" says. This is the wording I accepted in round 1. The sentence now says what came of the book, and it finishes the brief.

**NB1. NEW BLOCKING: "Cornelius wrote that people were leaving him every day" now points to the wrong man (item 1; item 4, statements with no context or meaning).**
- Sentence (line 5): "A synod of sixty bishops at Rome ruled that Novatian and his followers were strangers to the church. Cornelius wrote that people were leaving him every day."
- Cornelius wrote of Novatian: "he has now been made bare and desolate; as the brethren leave him every day and return to the church" (`npnf201` 38776-38777).
- In round 1 this was one sentence, with Novatian earlier in it. The revision split it in two. Now the only man in the new sentence is Cornelius, so a listener hears that people were leaving Cornelius. That is the opposite of the source. The "Yet" that follows then reads as if it carried on Cornelius's losses. The revision broke this sentence, and it misleads.
- Fix I would accept, exact wording: "Cornelius wrote that people were leaving Novatian every day and returning to the church."
- A round 3 recheck of that one sentence can close it.

**Non-blocking items taken: checked.**
- "Nearly two centuries after the split" holds. Socrates writes after Celestinus (`npnf202` 19288-19293).
- "At Rome they had held many churches until Bishop Celestinus took them away." This is now its own sentence. It is still carried by Socrates, who is named in the sentence before it (19289-19293). Holds.

**Non-blocking note N5 (new, small).** "Socrates says the churches in each province took sides, and that others welcomed the stricter rule." Socrates has "this appeared to some a cruel and merciless course: but others received the rule as just" (`npnf202` 14099-14100). With the "some" gone, "others" has nothing to answer, and "others" next to "people leaving Novatian" can be heard as "other people". "... took sides: some thought the rule cruel, and others welcomed it as just" would be exact. Or use "and that some welcomed the stricter rule". This is not blocking, but it sits in the same passage as NB1 and could be fixed with it.

---

## Summary for the coordinator

| Brief | Round 1 blocking | Round 2 | Verdict |
|---|---|---|---|
| marcion-of-pontus | B1, B2 | both CLOSED; N1 non-blocking (Theodoret told flat) | CLEARS |
| valentinus | B1, B2, B3 | all CLOSED; N2 ("came" for Marcion), N3 ("he" after Clement) non-blocking | CLEARS |
| hippolytus-of-rome | B1 | CLOSED; N4 non-blocking ("By his own account") | CLEARS |
| novatian | B1, B2 | both CLOSED; NB1 NEW BLOCKING (pronoun turned to Cornelius by the split); N5 non-blocking | BLOCKED |

Lengths: the stated reasons for Marcion (344) and Valentinus (337) hold. Both fall inside the 2:30 stretch, so no batch note is owed, and the added words are the item 16 setting that round 1 asked for.

Round 3 for Novatian is a recheck of one sentence. Accepted wording: "Cornelius wrote that people were leaving Novatian every day and returning to the church."
