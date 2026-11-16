# Round 2, group g1: targeted recheck of the round 1 findings

Reviewer: Opus, independent, the same reviewer as round 1. I made no model or API calls and changed no file but this one. I read `git diff 8e856fc3..HEAD` on `claude/cft-era1-standard-v1` for the four briefs, their refs files and `renderings/`. The brief changes are in commit 7b66d232. I rechecked only what changed. Every new or changed sentence was checked by hand against `cic/texts/`; the lines are quoted below.

Bar briefs compared against: Gregory of Tours and Benedict of Nursia (Standard v1), and Methodius of Olympus (the bar brief round 1 used for Hermas and Polycrates), all in `Who-Profiles/bar/`.

## Readability (`python3 -m engine.m1.profile_readability --report`)

| Brief | Words | Grade (full) | Grade (names out) | Reading ease (names out) | Words a sentence | Joins /100 | Short sentences | Tool |
|---|---|---|---|---|---|---|---|---|
| hermas | 354 | 8.4 | 8.0 | 72.6 | 19.7 | 1.1 | 11% | pass |
| ignatius-of-antioch | 302 | 8.3 | 7.6 | 74.0 | 18.9 | 1.3 | 12% | pass |
| polycrates-of-ephesus | 348 | 9.0 | 7.5 | 76.0 | 19.3 | 0.6 | 6% | pass |
| josephus | 312 | 9.3 | 7.5 | 76.3 | 19.5 | 1.3 | 12% | pass |
| ignatius, split FINAL (scratch copy, not in repo) | 301 | 7.8 | 7.2 | 75.0 | 17.7 | 1.3 | 18% | FAIL, below 8 |

All four briefs sit inside grade 8.0 to 10.0 on the full text, with reading ease above 60 with names out. None uses "the tree", "on the map" or "the census". None names a modern scholar. Every word in quotation marks matches a FINAL in `renderings/comparison.md`, except the Ignatius wheat line, which matches E15's A form (see Ignatius B1).

---

## hermas (batch1)

**B1, the second ancient report: CLOSED.**
- New: "Around the year 150, by the earliest report we have, ..." and "Eusebius of Caesarea and Jerome took him instead for the Hermas whom Paul greets in his letter to the Romans." (brief line 1)
- Eusebius III.3.6 (npnf201 14735-14736, 14753, 14848): Paul "has made mention among others of Hermas, to whom the book called The Shepherd ... is ascribed". Jerome, Lives 10 (npnf203 39614-39627): the Hermas of Romans 16 "is reputed to be the author". Both sides are now named. "The earliest report" is true of the held sources: the Muratorian list says "very recently in our times" (anf05 60178-60180); Origen and Eusebius come later.

**B2, the scope of the second repentance: CLOSED.**
- New: "... and in mercy has set one repentance more for those baptized before this time." (line 5)
- Commandment 4.3 (anf02 1999-2003): "those who have now believed, and those who are to believe, have not repentance ... For to those who have been called before these days, the Lord has set repentance." The context is baptism ("when we descended into the water", 1992-1993), so "baptized" for "called" is fair. "In mercy": "being merciful, has had mercy on the work of His hand" (2010-2011).

**B3, the sentence the ear lost, and the flow hinge: CLOSED.**
- New: "Afraid, he asked himself how he could now be saved." and "The book takes its name from an angel dressed as a shepherd, sent to live with him. This angel agrees that the baptized ought not to sin again. But the Lord knows human weakness, he says, ..." (line 5)
- Vision 1.2 (anf02 733-734): "I was overwhelmed with sorrow and fear, and said to myself, 'If this sin is assigned to me, how can I be saved'". Vision 5 (1695-1699): "dressed like a shepherd ... 'I have been sent by a most venerable angel to dwell with you'". Commandment 4.3 (1994-1996): "he who has received remission of his sins ought not to sin any more".
- Craft test 2 (flow) now reaches the level at this hinge. The accusation leads to his fear, his fear to the teachers' rule, and the rule to the angel's answer. Model: Methodius, "His chief quarrel with Origen was over the body." The book and the angel are now told apart once, and "he says" has a clear subject.
- Other changes checked: "The Muratorian list said that ..." (taken from my note); "since some thought beginners in the faith needed it" against Eusebius's "quite indispensable, especially to those who need instruction in the elements of the faith" (npnf201 14855-14857). Both hold.

**Length, 355 words (`wc`; the tool counts 354): the stated reason holds.**
- The brief grew by 40 words. About 35 of them are the three fixes round 1 asked for: the second report (about 20), the fear sentence for the flow hinge (10) and the scope limit (6). The rest is the rewrite of the B3 sentence, offset by the shorter Eusebius clause.
- None of the added words is padding, and none could go to the card without the brief again claiming more than its sources (B1 and B2 were both "the brief says too much" findings).
- 355 is under the stretch of about 375 ("The brief", Length), so no batch line is required. The refs header says why it is over 300, which is enough.

**Non-blocking note, made slightly sharper by the revision.** "So a husband must take back an unfaithful wife who repents ..." now follows straight on "for those baptized before this time". The husband's rule is in Commandment 4.1 (anf02 1924-1934) and is not limited to earlier converts. A listener could take the rule as limited too. "In the same book he says a husband must take back ..." would avoid that. Not blocking: nothing in the sentence is false.

**Verdict: CLEARS.**

---

## ignatius-of-antioch (batch1)

**B1, the wheat quotation, answered with no change to the brief: CLOSED, on my own check.**
- The brief carries: "I am God's wheat, and let me be ground by the teeth of the wild beasts, so that I may be found the pure bread of Christ." (line 1)
- That is E15's A rendering word for word. E15 judged A and B "same" in meaning. Its FINAL split A into two sentences, a rhythm choice, not a correction of meaning.
- The printed text (anf01 7040-7042) is joined: "I am the wheat of God, and let me be ground by the teeth of the wild beasts, that I may be found the pure bread of Christ." So the joined form is the closer of the two to the source. That is the reason the answer holds. A grade figure alone would not be enough to choose a quotation's form.
- The grade claim is also true. I ran the tool on a copy with the split FINAL in my scratch space. On the current text it scores grade 7.8 and fails the floor. On the round 1 text it scores 7.9, the figure in the record.
- The record now says what the brief carries and why (E15 "Brief carries"; `renderings/README.md` line 15). That meets the round 1 fix ("change the FINAL ... with the reason recorded there").
- Non-blocking note: the E15 and README figure "7.9" was measured before the revision; it is 7.8 now. Either "below the floor of 8" or "7.8" would keep the record exact. The FINAL line itself still shows the split form; a reader of E15 has to read to the "Brief carries" line to learn what is spoken.

**B2, the Trajan date: CLOSED.**
- New: "Early in the second century, Ignatius was bishop of Antioch in Syria, ..." (line 1). This claims only what both sides of the held date dispute accept, as the pattern asks.

**Non-blocking note taken, checked.** "so that, he said, whatever the bishop approved would be secure and valid" (line 5). Smyrnaeans 8 (anf01 8287-8289): "whatsoever he shall approve of, that is also pleasing to God, so that everything that is done may be secure and valid." Close and fair.

**Verdict: CLEARS.**

---

## polycrates-of-ephesus (batch3)

**B1, the relatives sentence: CLOSED.**
- New: "Seven of his relatives had been bishops before him, and all had kept the day; he was the eighth." (line 5)
- Eusebius V.24.6 (npnf201 31385-31388): "seven of my relatives were bishops; and I am the eighth. And my relatives always observed the day". The sentence now carries his second ground. Craft tests 2 and 4 reach the level at this link (model: Gregory of Nyssa's "Macrina had turned him around once before").

**The three non-blocking changes, checked.**
- "Other bishops rebuked him, among them Irenaeus of Lyon, who kept Easter on Sunday himself and warned him ..." (line 7). Eusebius V.24.10-11 (31432-31440): "Words of theirs are extant, sharply rebuking Victor. Among them was Irenæus ...". Holds.
- "How or when Asia came round, no source says." (line 9). Constantine's letter gives only the state in 325, "in the dioceses of Asia and Pontus" (npnf201 64680-64682). Holds, and it meets Standard v1's "says plainly that the record shows what followed but not why".
- "Two centuries after Polycrates, Socrates of Constantinople says, John Chrysostom took churches away ... They claimed, he says, to have it from the apostle John." (line 9). Socrates VI.11 (npnf202 17975-17977): "deprived many of the Novatians and Quartodecimans of their churches". V.22 (16316-16318): "the Quartodecimans affirm that the observance of the fourteenth day was delivered to them by the apostle John". The reckoning is now the narrator's. Holds.

**Length.** 348 words, up from 331. The growth is the two sentences round 1 asked for, less the folded sentence. Under 375.

**Verdict: CLEARS.**

---

## josephus (batch1, outside witness)

**B1, the narrator's verdict on the longer report: CLOSED.**
- The thesis opener is gone. Paragraph 3 now opens "In our copies the longer report calls Jesus ..." (line 5), and the close is "So neither Origen nor Jerome read that line as our copies give it." (line 7)
- The conclusion now claims only what the two ancient witnesses carry, and only about the one line. Origen (anf09 30628-30629): "though he did not accept Jesus as Christ". Jerome (npnf203 39729): "was believed to be Christ". The sentence is true whether Origen's copy had the line in another form or lacked it.
- Craft test 3 (no AI tells) now reaches the level. The close is a plain inference that finishes the trust story, not a quotation. Model: John Chrysostom's opening, a judgment drawn from its witnesses with no device.

**B2, Origen's James: CLOSED.**
- New: "Origen ... cited Josephus on James against Celsus, a critic of the Christians. Here, Origen argued, was a writer who did not believe in Jesus as the Christ, yet said that Jerusalem fell because the Jews had killed James, a just man. Those words are not in our copies." (line 3)
- Against Celsus I.47 (anf04 37933-37942): "although not believing in Jesus as the Christ ... says nevertheless ... that these disasters happened to the Jews as a punishment for the death of James the Just ... the Jews having put him to death, although he was a man most distinguished for his justice". Holds.
- Our copies (Whiston, josephus_works 91005-91010): Ananus "brought before them the brother of Jesus, who was called Christ, whose name was James, and some others ... he delivered them to be stoned". No cause of the city's fall, and James is not called just. "Those words are not in our copies" holds.

**Non-blocking notes taken, checked.**
- "the emperor Vespasian gave him rooms in his own former house in Rome" (line 1). Life 76 (josephus_works 5408-5410): "an apartment in his own house, which he lived in before he came to the empire". Holds.
- The Eusebius and Jerome sentences are split (line 7). Grade 9.3, down from 9.9. Nothing in the split drops a reason or a contrast.
- The Q5 quotation "was believed to be Christ" is unchanged and still matches E5's FINAL.

**Verdict: CLEARS.**

---

## Summary

| Brief | Round 1 blocking | Round 2 | Verdict |
|---|---|---|---|
| hermas | B1, B2, B3 | all CLOSED; 355 words, the reason holds | CLEARS |
| ignatius-of-antioch | B1, B2 | B1 CLOSED on independent check (joined form is closer to the printed text; split scores 7.8, below the floor); B2 CLOSED | CLEARS |
| polycrates-of-ephesus | B1 | CLOSED | CLEARS |
| josephus | B1, B2 | both CLOSED | CLEARS |

No new blocking finding. Two non-blocking notes: the Hermas "So a husband" link (suggested wording above), and the E15 grade figure, now 7.8 rather than 7.9.
