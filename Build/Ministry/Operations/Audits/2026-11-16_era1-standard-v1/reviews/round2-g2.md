# Round 2: targeted recheck of the round 1 findings, group g2

Reviewer: Opus, independent. I made no model or API calls and changed no file but this one. I read the diff `8e856fc3..HEAD` on `claude/cft-era1-standard-v1` for the four briefs, their refs files and `renderings/`. For these four the only change is commit 012f04ce, plus the two "Brief carries" lines under E15 and E34 in `comparison.md`. I rechecked only what changed. Every new or changed sentence was checked by hand against `cic/texts/`.

Briefs: tacitus (batch2), suetonius (batch2), pliny-the-younger (batch3), pontius-the-deacon (batch2).

## Bar briefs compared against

Gregory of Tours and Benedict of Nursia (the Standard v1 examples), and Methodius of Olympus, as in round 1. Each brief's own round 1 text served as the drift check.

## Readability (`python3 -m engine.m1.profile_readability --report`, all pass)

| Brief | Words | Grade (full) | Grade (names out, info) | Reading ease (names out) | Words a sentence | Joining words /100 | Short sentences | Result |
|---|---|---|---|---|---|---|---|---|
| tacitus | 317 | 8.7 | 7.5 | 74.7 | 18.6 | 0.6 | 12% | pass |
| suetonius | 287 | 9.8 | 8.8 | 68.7 | 20.5 | 1.0 | 7% | pass |
| pliny-the-younger | 299 | 9.1 | 8.4 | 67.8 | 18.7 | 0.7 | 6% | pass |
| pontius-the-deacon | 285 | 8.5 | 7.8 | 75.5 | 20.4 | 1.4 | 7% | pass |
| pontius, split FINAL (scratch copy, not in the repo) | 285 | **7.9** | 7.3 | 76.9 | 19.0 | 1.4 | 13% | FAIL, below 8.0 |

The last row is my own test of the Pontius B1 answer. I copied the brief to my scratch space and changed only ", yet I grieve" to ". Yet I grieve", which is the E34 FINAL.

No brief says "the tree", "on the map" or "the census". No modern scholar is named in any brief.

---

## tacitus (era1/batch2)

**B1, "his one chapter on the Christians": CLOSED.**
- Line 1 now reads: "He was not a Christian, and his chapter on the Christians treats them as criminals."
- "One" is gone. The sentence now claims only what the held chapter carries (TA header 37-43; TA 68). It was the fix I gave.

**Non-blocking note taken, "confessed": checked, holds.**
- Line 5 now reads: "Those who confessed, he says, were arrested first. On their word a vast number were convicted, less for setting the fire than for hatred of the human race."
- TA 68: "an arrest was first made of all who pleaded guilty; then, upon their information, an immense multitude was convicted, not so much of the crime of firing the city, as of hatred against mankind."
- "He says" now marks the word as Tacitus's. Moving it off the second sentence leaves that sentence still carried by him, since it follows at once. Nothing broke.

Quotations: unchanged; Q1 and Q2 still match E6 and E7 FINAL word for word.

---

## suetonius (era1/batch2)

**B1, the two connector sentences: CLOSED.**
- "The first is in the life of Claudius." is now folded into the quotation's lead (line 3): "The first, in the life of Claudius, reads: "The Jews were constantly causing disturbances at the instigation of Chrestus, and he expelled them from Rome.""
- "Jerome looked to Suetonius for something else." is gone. Line 7 now reads: "Yet near the end of the fourth century Jerome wrote that he had been urged to follow the example of Suetonius and do for the church's writers what he had done for the famous authors of the pagans."
- "Yet" carries a real turn: no Christian writer quotes the notices, yet a Christian writer took Suetonius as his model. Jerome's preface carries it (npnf203 38773-38780: "You have urged me, Dexter, to follow the example of Tranquillus ... and to do for our writers what he did for the illustrious men of letters among the Gentiles"; the note there names Tranquillus as Suetonius).

**Q1, now unbroken: checked, matches.**
- E8 FINAL is the two halves "The Jews were constantly causing disturbances at the instigation of Chrestus," ... "and he expelled them from Rome." The gap was the brief's own "Suetonius writes". The brief now joins the same words with nothing added or lost. Rolfe's Latin (SR 25843-25844) is one sentence, so the joined form is closer to it.

**Non-blocking note taken, "around 120": checked, holds.**
- Line 1: "Around 120 Suetonius was secretary to the emperor Hadrian in Rome. He was not a Christian, and his lives of twelve Caesars, from Julius Caesar to Domitian, give the Christians two short notices."
- The year now attaches to the office only (SR 232-235: secretary "probably during the period when ... Septicius Clarus was a prefect of the praetorian guard (119 to 121)"). No year of writing is claimed. My round 1 point is met.

**Non-blocking note taken, Tertullian and Lactantius: checked, holds.**
- Line 3: "Romans did get the name wrong. Tertullian of Carthage complained that they said Chrestian for Christian, and Lactantius later wrote that the ignorant changed one letter and called Christ Chrestus."
- Tertullian, Apology 3 (anf03 1713-1715): "even when it is wrongly pronounced by you 'Chrestianus' (for you do not even know accurately the name you hate)". The "you" are the Roman authorities he addresses, so "Romans" is carried.
- Lactantius, Institutes IV.7 (anf07, line 3162): "the error of the ignorant, who by the change of a letter are accustomed to call Him Chrestus".
- The short sentence states a claim, and the two witnesses that carry it follow at once, so it is not a beat line. It leans toward the second reading of Chrestus, as the old "did complain" did. It does not settle it: the sentence before still says "may" for both. Not made worse. The card must still name who holds each reading, under What is uncertain.

Quotations: Q2 unchanged, matches E9 FINAL.

---

## pliny-the-younger (era1/batch3)

**B1, "asked each prisoner three times": CLOSED.**
- Line 3 now reads: "He asked the accused whether they were Christians. Those who said yes he asked twice more under threat of punishment, and those who held firm he sent to be punished."
- npnf201 19469-19474: "with those who have been brought before me as Christians I have pursued the following course. I have asked them if they were Christians, and if they have confessed, I have asked them a second and third time, threatening them with punishment; if they have persisted, I have commanded them to be led away to punishment."
- Each clause now matches the letter: only those who confessed were asked again, the threat is kept, and "the accused" follows "brought before me". It is the fix I gave, in two sentences.

**Non-blocking note taken, the Tertullian sentence: checked, holds.**
- Line 9 now reads: "Later Tertullian of Carthage, defending the Christians, argued from the governor's report that Pliny had found no crime in their worship."
- anf03 1563-1581: Tertullian sets the alleged crimes ("some Christian who had devoured a hundred infants") against Pliny's report that "except an obstinate disinclination to offer sacrifices, he found in the religious services nothing but meetings at early morning for singing hymns to Christ and God, and ... a united pledge ... forbidding murder, adultery, dishonesty, and other crimes." "No crime in their worship" is a fair summary of his argument. It no longer restates the worship and the oath.

**Non-blocking, the number of the accused and the spread of the faith: left by the writer.** The writer weighed it and sent it to the card. I do not reopen it; the revision did not make it worse.

Quotations: unchanged; Q1 to Q4 still match E10 to E13 FINAL.

---

## pontius-the-deacon (era1/batch2)

**B1, the closing quotation differs from the E34 FINAL: CLOSED, on my own judgment.**

The writer made no change. The brief still reads (line 7): "I rejoice greatly, very greatly, at his glory, yet I grieve more that I remained behind." The FINAL splits it at "glory. Yet". The record now says why, in `renderings/README.md` and the "Brief carries" line under E34 in `comparison.md`. A writer cannot close a blocking finding by saying so, so I judged it myself.

1. The grade claim is true. On a scratch copy with the split FINAL, the tool gives grade 7.9, a fail below the floor of 8.0 (table above). The joined form gives 8.5.
2. The joined form is the closer rendering on its own merits, not only for the number. The Latin is one sentence, with "tamen" joining the two clauses (Hartel, `cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` 41409-41410: "multum ac nimis multum de gloria eius exulto, plus / tamen doleo quod remansi."). The printed English is one sentence too (anf05 28302-28303: "Much and excessively I exult at his glory; but still more do I grieve that I remained behind.").
3. It is one thought, not two. The "more" of the grief is measured against the joy, so the clauses belong together. It runs 17 words, well inside the rendering bar of about 25.
4. The comparison (Opus) judged this exact wording "same" in meaning. The two forms differ only in a comma for a full stop. No word inside the marks differs from the FINAL.
5. The exception is recorded where a reader of the rendering record will find it.

I would not accept a quotation reshaped only to meet a grade. That is not what happened here: the brief keeps the form that follows the source more closely, and the record says so. Closed.

**B2, the Bede sentence: CLOSED.**
- "In the eighth century Bede copied Jerome's words into his chronicle." is gone from the brief and recorded for the card (refs (d), Legacy).
- Line 7 now ends: "That rests on Jerome, about 130 years after Cyprian's death, who writes that Pontius, Cyprian's deacon, shared his exile to the end and left a notable book on his life and death. Beyond Jerome, our sources do not show who read the Life or what became of Pontius."
- Jerome, Lives 68 (npnf203 40833-40835): "Pontius, deacon of Cyprian, sharing his exile until the day of his death, left a notable volume On the life and death of Cyprian."
- The negative still holds without Bede, since Bede only repeats Jerome and shows nothing of who read the Life. I searched `cic/texts/` again for "Pontius diaconus", "Vita Cypriani" and "life of Cyprian". Every hit is a modern or early-modern editor (for example the editor's note in Migne PL 103, line 114015, and Mansi XVI, line 89698), Koch, Monceaux, von Soden, and ANF's own notes. No ancient reader is held. Craft tests 4 and 5, failed in round 1 on this sentence, now pass: the close follows Jerome directly and finishes the story.

**Non-blocking note taken, "on every page": checked, holds.** Line 3 now reads "praising Cyprian throughout". The loose quantifier is gone.

---

## Summary

| Brief | Round 1 blocking | Round 2 | New findings | Verdict |
|---|---|---|---|---|
| tacitus | B1 "one chapter" | CLOSED | none | **CLEARS** |
| suetonius | B1 two connector sentences | CLOSED | none | **CLEARS** |
| pliny-the-younger | B1 "three times" | CLOSED | none | **CLEARS** |
| pontius-the-deacon | B1 closing quotation form | CLOSED (judged independently; split tested at 7.9) | none | **CLEARS** |
| pontius-the-deacon | B2 Bede sentence | CLOSED | none | **CLEARS** |

No STILL BLOCKING or NEW BLOCKING finding, so no round 3 recheck is owed for this group. The cards must still carry what the briefs sent to them: the Shaw and Jones question (Tacitus), both readings of Chrestus with their holders (Suetonius), the number and spread of the accused (Pliny), and Bede (Pontius).
