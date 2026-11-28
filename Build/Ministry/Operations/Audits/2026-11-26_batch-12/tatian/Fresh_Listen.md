# Tatian: fresh first-time listen

A first-time visitor with no church background and English as a second language. I heard the final `tatian.brief.txt` once. I opened no source, outline, other read or earlier draft. Judged against Part 1, the bar in `Kit.md`, and `kinds/person.md`.

**Verdict: REVISE on one BLOCKING finding (1 below).** Everything else is MINOR: apply it word for word, or note it.

## Counts

| Item | Count |
|---|---|
| Test lines unfilled | 0 (one line weak, see finding 1) |
| Opening gaps (who, where, when, why there) | 2, MINOR (what kind of man he was; why he was at Rome) |
| Sentences that fail on one hearing | 4, MINOR |
| Bare statements | 1, BLOCKING |
| Citations read aloud not called for | 1, MINOR |
| Tells Part 1 names | 0 (one near-miss, MINOR) |
| Unexplained words | 4, MINOR |
| Runs of short one-act sentences | 0 |
| Talking down | 0 |

## 1. The test

- **Who this was:** filled. A man born in Assyria, trained in Greek learning and public speaking, who became a Christian at Rome in the mid-second century and heard Justin teach.
- **What happened:** filled. He turned to the "barbarian" writings, attacked Greek learning in his Address, left the church after Justin died, wove the four Gospels into one book, and in the 400s a bishop put that book away.
- **What it was about:** filled. Greek learning set against the older writings of Moses, his teaching against marriage, and the one-book gospel.
- **Why the connection matters:** filled, but weak at the close. I can tell that the Syriac-speaking churches read his book in worship, and that Ephrem explained it. I cannot tell why the bishop thought it harmful (finding 1).

## 2. The opening

After three sentences I know: Tatian; Rome; the middle of the second century; that he took part in pagan rites and went looking for the truth. Missing: what kind of man he was (a writer, a speaker, a foreigner at Rome?), and why he was at Rome. I am not lost about who or where. MINOR, no change needed: paragraph 3 gives his birth and training soon after.

## Findings with exact changes

### BLOCKING

**1. Bare statement: the harm Theodoret saw.**
"Tatian, he says, had cut out the lists of Jesus's ancestors and other passages showing the Lord born of David's line." A listener with no church background does not know who David is, or why it matters that Jesus came from his family. So "not seeing the harm" in the next sentence is empty, and the closing act (the bishop putting the book away) has no reason I can follow. This is the story's last scene and the end of its connection.
Change to: "Tatian, he says, had cut out the lists of Jesus's ancestors and other passages showing that the Lord was born as a man, from the family of King David."
(The trust reader confirms "as a man" against Theodoret's "according to the flesh" in the outline; if the outline does not hold it, use "from the family of King David" alone.)

### MINOR

**2. Failing sentence.** "Eusebius, a bishop, makes Tatian the source of the Encratites, about 172." I cannot tell what happened in 172: Tatian's founding, his break, or Eusebius's writing.
Change to: "Eusebius, a bishop, makes Tatian the source of the Encratites, and places this about 172." (Use the outline's own wording of what the date marks.)

**3. Failing sentence.** "Irenaeus puts him among the Encratites, the self-controlled, who refused marriage, and some of them meat, a group he says sprang from earlier teachers." "And some of them meat" trips on one hearing, and the last clause trails.
Change to: "Irenaeus puts him among the Encratites, the self-controlled. They refused marriage, and some of them refused meat. Irenaeus says the group sprang from earlier teachers."

**4. Failing sentence.** "A later Roman teacher gives the reason: disobedience began with Adam." I could not tell whose reason this is: Tatian's, or the later teacher's own.
Change to: "A later Roman teacher gives Tatian's reason: disobedience began with Adam." (Only if the outline's line reports Tatian's reasoning; otherwise leave it.)

**5. Failing sentence.** "Tatian's most used book, he says, was the Address." Heard right after the Diatessaron, read in worship across the East, this sounds like a contradiction, and I could not tell who used it. The Address is already told. The draft runs at 675 against an approved 650, and the heart does not need this.
Change: cut the sentence.

**6. Citation read aloud not called for.** The same sentence's "he says" (finding 5). Cutting it resolves both.

**7. Near-miss on "no sentence that only says what is missing."** "Eusebius, about 150 years after the break, did not know how Tatian combined the Gospels into one." It carries content, so it is not a tell, but it leads with what is unknown.
Change to: "Eusebius, writing about 150 years after the break, says Tatian combined the Gospels into one in a way Eusebius did not know."

**8. Unexplained words.**
- "a pupil from Asia": a listener today hears the continent. Change to "a pupil from the Roman province of Asia" (if the outline holds the province; otherwise leave it).
- "fornication": many second-language listeners will not know it. It sits inside Irenaeus's charge, so keep it; MINOR, noted.
- "bishop of Cyrrhus under Antioch": "under Antioch" is unclear. Change to "Theodoret, a bishop in the region of Antioch," only if the outline holds that wording; otherwise noted.
- "Nisibis": heard as a place name, and understood as that. Noted, no change.

**9. Names.** About seventeen names are heard (Tatian, Jupiter, Moses, Irenaeus, Justin, Homer, Crescens, Rhodon, Valentinus, Marcion, Adam, Eusebius, Epiphanius, Ephrem, Theodoret, David, Jesus). Most act or link. Rhodon is heard once and does nothing else. Justin is first heard bare ("he heard Justin teach") and only later known as a Christian teacher killed for his faith. MINOR, noted: I was not lost.

## Attention

- **Does the opening pull me in?** Yes. Secret rites and Jupiter honored with human blood, then a man going off alone to find the truth.
- **Where attention first drifts:** "Irenaeus says Tatian spoke of aeons, invisible heavenly powers, like the followers of Valentinus, a teacher at Rome." From here to the end of that paragraph come Valentinus, Marcion, Adam, an unnamed later teacher, the Encratites, Eusebius, a date and Epiphanius in eight sentences. Each teaching is a short label next to another teacher's name, so I hold names and lose what Tatian himself believed. Findings 2 to 4 ease it.
- **Would I listen to the end?** Yes. The Diatessaron and Theodoret gathering two hundred copies bring me back. The last scene lands once finding 1 is fixed.

## The tools

`python -m engine.m1.profile_readability`: 675 words, grade 8.4 (names out 7.4), reading ease 72.6 (names out), 17.3 words a sentence, 3% short sentences, longest sentence 31 words. **Pass.**

`python tools/check_brief_craft.py`: 6 to look at, judged by Part 1:
- s1 "Tatian says he had been initiated...": names a source. Tatian is the subject speaking of himself. Fine.
- s16 "Every art the Greeks boast of, his Address says...": his own book, part of the story. Fine.
- s25 "Irenaeus says Tatian spoke of aeons...": an enemy's charge, which Part 1 says to credit. Fine.
- s31 "Some two centuries later Epiphanius...": a witness writing long after, and one who adds to the others. Fine.
- s33 "He says Tatian called it the Diatessaron...": Eusebius, writing long after. Fine.
- s35 "Later writers of the Church of the East say Ephrem...": flagged as a possible bare statement. It says what the commentary was ("explaining the Diatessaron"), and it shows the Syriac church used the book. Not bare. Fine.
