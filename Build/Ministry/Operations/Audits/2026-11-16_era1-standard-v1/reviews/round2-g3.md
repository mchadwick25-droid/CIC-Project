# Round 2: targeted recheck of the round 1 findings, group g3

Reviewer: Opus, the same independent reviewer as round 1. I made no model or API calls and changed no file but this one. I read `git diff 8e856fc3..HEAD` on `claude/cft-era1-standard-v1` for the four briefs, their four refs files and `renderings/`. I rechecked only what changed. Every new or changed sentence was checked by hand against `cic/texts/`. The writer's "Round 1 revision" notes were read as claims and checked.

Bar briefs compared against: Gregory of Tours and Benedict of Nursia (read again in full), and, as in round 1, Origen and Gregory of Nyssa for flow, Methodius for the placed aside, and Constantine for the council.

## Readability of the changed briefs (all pass)

`python3 -m engine.m1.profile_readability --report <paths>`, run 2026-11-16 from the repo root.

| Brief | Words | Grade (full) | Grade (names out) | Reading ease (names out) | Words/sentence | Joins/100 | Short sentences |
|---|---|---|---|---|---|---|---|
| peter-of-alexandria | 304 | 9.0 | 7.3 | 71.0 | 16.0 | 0.7 | 16% |
| anatolius-of-alexandria-and-laodicea | 298 | 8.6 | 6.8 | 77.2 | 17.5 | 0.7 | 6% |
| eusebius-of-caesarea | 302 | 9.4 | 7.5 | 73.0 | 17.8 | 1.0 | 18% |
| councils-of-rome-and-carthage-251 | 424 | 9.1 | 7.8 | 70.9 | 17.7 | 0.7 | 21% |

The writer's figures match the tool. No brief contains "the tree", "on the map" or "the census". No modern scholar is named in any brief. No quotation in these four briefs was added, removed or reworded. The two `comparison.md` additions (E15, E34) belong to Ignatius and Pontius, not this group.

---

## 1. peter-of-alexandria

**B1: CLOSED.**
- New sentence (brief line 5): "In the same persecution, another Egyptian bishop, Meletius of Lycopolis, was ordaining clergy in other bishops' districts, and four bishops in prison wrote to protest."
- This is the fix I asked for. It claims only what the witnesses give: Athanasius and Epiphanius place the break in that persecution, nothing closer. The tie to the time of the canons is gone, and Epiphanius's framing no longer comes before the dispute.

**Non-blocking note taken, checked: sound.**
- New clause (line 7): "Epiphanius of Salamis, who writes kindly of Meletius, says ..."
- Epiphanius calls Meletius's case "a veritatis amore profecta, et divini ardoris plenissima ratio" (`epiphanius_panarion-haer-48-69-..._oehler1860.txt` 43803-43805). That carries "writes kindly". It also praises Peter ("sanctissimus Petrus, utpote benignus ac misericors", 43807-43808), so "kindly of Meletius" is not a claim that he takes Meletius's side. Fair, and it balances "the Meletians' enemy".

Nothing new is broken. **Verdict: CLEARS.**

---

## 2. anatolius-of-alexandria-and-laodicea

**B1 (storytelling and flow): CLOSED.**
- New text (brief lines 1-3): "... in arithmetic, geometry and astronomy. / Earlier, by a story Eusebius tells, Roman troops had besieged a quarter of Alexandria. When the bread ran out, Anatolius persuaded the city's council to send out the old and the children. Under that cover he got nearly all the besieged away by night. After that war he left Alexandria. On the road to the synod he passed through Laodicea in Syria, where the bishop had died, and the Christians there kept him as their own."
- Order of events against Eusebius (`npnf201_eusebius-church-history-life-of-constantine.xml`): the siege, while Eusebius the deacon "was still there before his transfer to Syria" (42718-42724); the two pastors came "after the aforesaid war from Alexandria to that city" (42765-42767); later "the synod which was held to consider Paul's case called him to Antioch, and as he passed through the city of Laodicea, Eusebius being dead, he was detained by the brethren there" (42930-42940). The brief now runs siege, leaving Alexandria, the road to the synod, Laodicea. That matches.
- "Earlier" marks the step back from 270 plainly, and the paragraph returns to the synod by its last sentence. No sentence hangs. The siege now leads somewhere: out of Alexandria and to Laodicea.
- "A story Eusebius tells" is carried by "They relate of him" (42696) and "They say" (42718). The siege stays marked as a report.
- "After that war" follows Eusebius's own "the aforesaid war" (42766).
- Flow test, weakest link now: "Under that cover he got nearly all the besieged away by night. / After that war he left Alexandria." Beside Origen's "because everyone else had fled", it is close to that level and is sound. Storytelling test: the line is now one story, a scholar of Alexandria who saved the besieged, came to Laodicea, set down an Easter rule, and was claimed by both sides at Whitby. Both tests pass. "One story about him was still told in Eusebius's day" is gone; the sentence test now marks 0.

**B2: CLOSED.**
- New sentence (line 7): "Bede, who tells it, says the king ruled for Wilfrid because Christ had given Peter the keys of heaven."
- Bede (`bede_ecclesiastical-history-english-people_giles1903.txt` 8202-8217): the king asks whether "the keys of heaven were given to him by our Lord", and decides to obey Peter, "lest, when I come to the gates of the kingdom of heaven, there should be none to open them"; all present then "resolved to conform". The ground of the ruling is Bede's. The inference put in his mouth is gone.

**Non-blocking note taken, checked: sound.** "... Paul of Samosata, for his teaching about Christ" is carried by "low and degraded views of Christ" (41839-41840).

**Non-blocking (new, not a finding):**
- "Earlier, by a story Eusebius tells, ..." "By a story" is not idiomatic English, and the ear may snag on it. "In a story Eusebius tells, Roman troops had earlier besieged ..." or "Earlier, Eusebius tells, Roman troops had besieged ..." would read more easily. Nothing in it is wrong.
- "After that war he left Alexandria. On the road to the synod ..." Eusebius has Anatolius serve first as assistant bishop under Theotecnus at Caesarea (42926-42929). The brief passes over that step, as Eusebius's own section 12 does ("from Alexandria to that city"). It is supported, so it stands; the Caesarea step belongs on the card.

**Verdict: CLEARS.**

---

## 3. eusebius-of-caesarea

**B1: CLOSED.**
- New text (brief line 11): "Socrates himself built his account of Nicaea on Eusebius's words, treating them, he says, as an authority. He copied the letter in full."
- Socrates I.8 (`npnf202_socrates-sozomen-ecclesiastical-histories.xml`): "it may be well to hear what Eusebius says on this subject, in his third book of the Life of Constantine" (2837-2838); "treating what he has said as an authority, have introduced it here for the fidelity of this history" (2866-2869). The phrase is now joined to the right text. The letter follows "in his own words" (2978-2979) and runs to "Such was the letter addressed by Eusebius Pamphilus to the Christians at Cæsarea" (3156-3157). "In full" holds.

**B2 (no AI tells): CLOSED.**
- New sentence (line 9): "In 325, at the council of Nicaea, Eusebius read out his own creed before Constantine."
- The thesis opener is gone, and the paragraph opens on the act. Paragraph 2 ends on "passed lightly over Arius", and paragraph 3 opens on the council about Arius, so the link still reads without the device. Two hinge lines remain ("Later historians built on it." and "That letter followed him."). Each carries a claim the paragraph proves; round 1 counted them only beside the cut one. No-AI-tells test now passes, beside John Chrysostom's opening.

**Non-blocking (new, not a finding):** the close was split into two sentences, and the last one, "He copied the letter in full.", is a six-word tail. It adds a fact, so it is not a beat line. The joined form I offered in round 1 ("..., treating them, he says, as an authority, and copied the letter in full.") would end the brief in one breath. A rhythm note only.

**Verdict: CLEARS.**

---

## 4. councils-of-rome-and-carthage-251

**B1 (C9): CLOSED.**
- New sentence (brief line 5): "Eusebius of Caesarea, working from letters of Cornelius that had reached him, says sixty bishops met there."
- Eusebius VI.43.3: "There have reached us epistles of Cornelius, bishop of Rome, to Fabius" (`npnf201` 38302, 38326-38327). McGiffert's "These epistles are no longer extant" (38324) is no longer told in the brief. C9 now passes.

**Non-blocking notes taken, checked: sound.**
- "the strict churches of the Roman presbyter Novatian" (line 1): Eusebius, "Novatus, a presbyter of the church at Rome" (`npnf201` 38265); Socrates, "a presbyter of the Roman Church" (`npnf202` 14068). Carried.
- "The book of their decisions is lost, so what they decided reaches us from Cyprian, who called the meeting and defended it afterward." (line 3). The "so" gives the honest limit as the reason for the witness. Sound, and the short pair is joined.
- "The way back itself held, for in 325 the council of Nicaea set terms for Novatian's clergy. They could keep their rank only if they promised in writing ..." (line 13). Canon 8 (`npnf214_seven-ecumenical-councils.xml` 3768-3779) carries both sentences, as in round 1.

**Non-blocking (new, not a finding):**
- After the split, the "for" clause gives "set terms" as its evidence, and the terms that prove the point come in the next sentence. The logic still reads, since the next sentence follows at once.
- The opening's last sentence is now about 36 words ("Two councils took up their case, ... and the strict churches of the Roman presbyter Novatian grew out of the quarrel."). It is a plain compound and reads in one breath. Watch it if the sample read finds it long.

Length: 424 words, about 2:50, inside the council stretch the writer cites. **Verdict: CLEARS.**

---

## Summary

| Brief | Round 1 blocking | Round 2 | New blocking | Verdict |
|---|---|---|---|---|
| peter-of-alexandria | B1 | B1 CLOSED | none | CLEARS |
| anatolius-of-alexandria-and-laodicea | B1, B2 | both CLOSED | none | CLEARS |
| eusebius-of-caesarea | B1, B2 | both CLOSED | none | CLEARS |
| councils-of-rome-and-carthage-251 | B1 | B1 CLOSED | none | CLEARS |

No STILL BLOCKING or NEW BLOCKING finding. The non-blocking notes above are rhythm notes only ("by a story" in Anatolius, the split close in Eusebius). No round 3 recheck is needed for this group. The batch still does not go live until Mark has read the coordinator's sample.
