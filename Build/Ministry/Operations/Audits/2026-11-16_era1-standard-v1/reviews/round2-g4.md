# Round 2: targeted recheck of the round 1 findings, group g4

Reviewer: Opus, the independent reviewer of round 1. I made no model or API calls and changed no file but this one. I read `git diff 8e856fc3..HEAD` on `claude/cft-era1-standard-v1` for the three briefs, their refs files and `renderings/`. I rechecked only what changed. Every new or changed sentence was checked by hand against `cic/texts/`.

Bardaisan of Edessa and Dionysius of Alexandria cleared round 1. `git diff 8e856fc3..HEAD` shows no change to their briefs or refs files, so they are not reviewed here.

Bar briefs compared against: Gregory of Tours and Benedict of Nursia (the Standard v1 examples), with Origen and Methodius of Olympus, as in round 1.

## Readability (`python3 -m engine.m1.profile_readability --report`)

| Brief | Words | Grade (full) | Grade (names out) | Reading ease (names out) | Words a sentence | Joining words /100 | Short sentences | Tool |
|---|---|---|---|---|---|---|---|---|
| justin-martyr | 320 | 9.1 | 8.2 | 70.1 | 18.8 | 0.6 | 12% | pass |
| tatian | 323 | 9.5 | 7.6 | 72.3 | 17.9 | 0.0 | 6% | pass |
| clement-of-alexandria | 301 | 9.2 | 7.5 | 72.6 | 17.7 | 0.3 | 6% | pass |

All three sit inside grade 8.0 to 10.0 on the full text and above reading ease 60. Clement's refs claim 72.8; the tool gives 72.6. That does not matter.

No brief says "the tree", "on the map" or "the census". No modern scholar is named. No quotation was added, removed or reworded; each still matches its FINAL in `renderings/comparison.md` (E20 to E22, E23, E29, E30). The only change to `comparison.md` is two notes for E15 and E34, outside this group.

---

## justin-martyr: BLOCKED (2 new, both one-word fixes)

**B1 (the Tatian sentence): CLOSED.** "His hearer Tatian did not follow him here ..." is cut. Paragraph 2 now ends on Socrates (brief line 3). The refs send Irenaeus I.28.1 and Address 35 to the card.

**B2 ("No answer to him survives"): CLOSED.** New, brief line 5: "Eusebius follows the petition with an edict that he gives as the emperor's, sent to Asia after Christians there told him how they suffered. No one was to be punished for being a Christian alone."
- Eusebius IV.12-13 (`npnf201_...xml` 22652-22655): "And the same emperor having learned also from other brethren in Asia of the injuries of all kinds which they were suffering from the inhabitants of the province, thought it proper to address the following ordinance to the Common Assembly of Asia." The chapter heading is "The Epistle of Antoninus" (22676-22680).
- The ruling, IV.13.7 (22802-22805): "if any one still persists in bringing accusations against any of these people as such, the person who is accused shall be acquitted of the charge, even if it appear that he is one of them". The ANF form says the same (`anf01_...xml` 16615-16619). "For being a Christian alone" is a fair plain telling.
- "That he gives as the emperor's" keeps the brief from vouching for the edict. The doubt goes to the card (refs). The brief claims order only, not cause. That is what Standard v1 asks.

**N1. NEW BLOCKING (item 8, first mention of a common name).** The new sentence brings "Eusebius" in bare: "Eusebius follows the petition with an edict ..." (line 5). The place now comes only at the second mention: "Eusebius of Caesarea says the plot succeeded ..." Item 8 asks for the place at the first mention, and several Eusebii are in play in this era. The revision moved the first mention without moving the place.
- Fix I would accept, exact wording: "Eusebius of Caesarea follows the petition with an edict that he gives as the emperor's, ..." and, later in the same paragraph, "Eusebius says the plot succeeded, though the surviving account of his trial never names Crescens."

**N2. NEW BLOCKING (a sentence that now hangs on the wrong person).** "He expected to be plotted against, he wrote, perhaps by Crescens, a Cynic philosopher." (line 5). Before the revision this followed "No answer to him survives", so "he" was Justin. Now it follows two sentences about Eusebius and the emperor. Heard aloud, "He expected to be plotted against, he wrote" reads as the emperor or Eusebius. That misleads on whose fear it was (Second Apology 3, `anf01_...xml` 16849-16851, is Justin's own).
- Fix I would accept, exact wording: "Justin expected to be plotted against, he wrote, perhaps by Crescens, a Cynic philosopher."
- With both fixes the tool gives 320 words, grade 9.1, reading ease 70.0 (checked on a scratch copy).

Non-blocking items left by the writer (the Crescens run, "Cynic philosopher", the Dialogue with Trypho) are not reopened. The revision did not make them worse. The Dialogue note is now in the refs, as round 1 asked.

Craft test 2 (flow), rechecked: round 1 passed it "once B2 is fixed". The B2 sentence itself is sound, and the edict sitting beside Justin's death is a fair juxtaposition the source gives. The link out of it is broken only by the pronoun (N2). Passes once N2 is fixed.

---

## tatian: CLEARS

**B1 (Theodoret): CLOSED.** Cut (old line 9). The refs mark it for the card, with Hogg named.

**B2 (Rabbula): CLOSED.** Cut (old line 9). Same.

**B3 (the label opening, no moment): CLOSED.** New, brief line 1:
- "In the middle of the second century, Tatian was in Rome as a hearer of the Christian teacher Justin Martyr, who was later beheaded there for refusing to sacrifice." Irenaeus I.28.1 (`anf01_...xml` 33663-33664): "He was a hearer of Justin's". Martyrdom of Justin 5 (29391-29402): "Let those who have refused to sacrifice to the gods ... suffer the punishment of decapitation". "In the middle of the second century" is the round 1 non-blocking note, taken; it claims only what Epiphanius's date (EpH 15997-15998) and the modern dating both allow.
- "After Justin's death, Epiphanius of Salamis says, he went east and set up his school in Mesopotamia." Panarion 46.1 (`epiphanius_panarion-haer-34-64-gcs-bd2-grc_holl1922.txt` 15996-16000): "τὸ δὲ αὐτοῦ διδασκαλεῖον προεστήσατο ἀπ᾽ ἀρχῆς μὲν ἐν τῇ Μέσῃ τῶν ποταμῶν ... ἀπὸ Ῥώμης γὰρ μετὰ τὴν τοῦ ἁγίου Ἰουστίνου τελείωσιν διελθὼν ἐπὶ τὰ τῆς ἀνατολῆς μέρη". That is exactly what the sentence says, and the hostile witness is named.
- "Syriac Christianity came to read the gospel book he made." The tradition is now said as a fact, not as our label or our reason (item 18). It rests on the Teaching of Addai (`anf08_...xml` 62103-62107), told in the last paragraph. That is the fix round 1 offered.
- Item 16 now holds: a time, Rome and then Mesopotamia, the tradition, and a moment (Justin's execution for refusing to sacrifice).

**B4 (marriage stance with no consequence): CLOSED.** New, brief line 7: "Later writers tied him to the Encratites, a movement that preached against marriage. Irenaeus says the movement sprang from earlier teachers, but Eusebius reports that Tatian was said to have founded it."
- Irenaeus I.28.1 (`anf01_...xml` 33656-33664): "Springing from Saturninus and Marcion, those who are called Encratites (self-controlled) preached against marriage ... A certain man named Tatian first introduced the blasphemy."
- Eusebius IV.28 (`npnf201_...xml` 26183-26186): "the heresy of the so-called Encratites ... It is said that Tatian was the author of this false doctrine." IV.29.6 (26424-26425): "their original founder, Tatian".
- The dispute is told in place, with each side named, in two sentences. "Was said to have founded it" follows IV.28's "It is said" and does not overstate Eusebius. Sound.

**"Pagan mysteries" (non-blocking, taken):** Address 29 (`anf02_...xml` 6962-6968) names "the Romans their Latiarian Jupiter" and "Artemis" beside "admitted to the mysteries". "Pagan" adds nothing the passage does not carry.

**Craft test 1 (storytelling), rechecked: PASS.** Line of the story: a Syrian pupil of Justin found the faith in non-Greek books, argued they were older than Greek learning, broke with the church in his opponents' telling, and left one gospel for four that the Syriac church read. Weakest sentence now: "Syriac Christianity came to read the gospel book he made." Bar: Benedict, "He was Benedict of Nursia, and the early Benedictines of Italy begin with him." It does the same work, as a fact the close then pays off.

**Craft test 2 (flow), rechecked: PASS, narrowly.** The five-witness row is gone. Weakest link now: "Eusebius says some still had it in his day. The Teaching of Addai, a Syriac legend ..., shows the people gathering each day to hear ... the Diatessaron read." Bar: Ephrem, "From that time on, Sozomen says, the Syrians sang the songs of Ephrem." The two sentences answer one question, what became of the book, and the second marks its legend. The tool counts no joining words, but "after", "later" and "but" carry the new links in paragraphs 1 and 4. A joining word here would read better; that is not a finding.

**Craft test 4 (hanging sentences), rechecked: PASS.** The close now finishes the book's story at Edessa and answers the opening's "Syriac Christianity came to read the gospel book he made". It is not a quotation and not a beat.

**Craft test 5 (everything relevant), rechecked: PASS.** The label sentence is gone.

Sentence test, rechecked: 0. All three sentences counted in round 1 are gone.

Non-blocking left by the writer ("Valentinus" not explained) is not reopened. Length 323 words, about 2:10, inside the stretch.

---

## clement-of-alexandria: BLOCKED (1 new, a one-phrase fix)

**B1 (no setting moment): CLOSED.** New, brief line 1: "Around the year 200, some people spoke against Greek philosophy, as if it dragged believers away from the faith. One who answered them was Clement, a presbyter of Alexandria in Egypt."
- Stromata I.2 (`anf02_...xml` 27670-27691): "I say thus much to those who are fond of finding fault ... although some have calumniated it ... nor does it drag us away from the faith, as if we were bewitched by some delusive art".
- **"Some people", not "some Christians": the writer is right.** Clement says only "some" and "those who are fond of finding fault". He does not say who they were or where. "Drag us away from the faith" says what they feared for believers; it does not say the fault-finders were believers. "Some Christians" would name a party the passage does not name. "Some people", with "as if it dragged believers away from the faith", keeps the source's own limit and still gives the listener the quarrel. The year rests on Eusebius's Severan date for the Stromata, as round 1 accepted.
- The opening now gives a time, a place, the city's church and what was going on. It no longer opens on "The X was Y".

**Jerome's list (non-blocking, taken):** "he pointed, among others, to Clement" (line 5). Letter 70 (`npnf206_...xml` 16475-16643) gives a long list with Clement in it. Correct.

**N1. NEW BLOCKING (a sentence that now hangs on the wrong person).** "His answer was that God is the cause of every good thing." (line 3). Moving the quarrel up put five sentences between the critics and Clement's answer. The sentence just before is "Eusebius of Caesarea judged that this teacher was Pantaenus, who led the school before Clement." Heard aloud, "His answer" belongs to Pantaenus or to Eusebius, and a listener also loses what it answers. The words are Clement's (Stromata I.5, `anf02_...xml` 27887-27888: "For God is the cause of all good things"). As written it misattributes the brief's central stance.
- Fix I would accept, exact wording: "Clement's answer to those critics was that God is the cause of every good thing."
- With the fix the tool gives 304 words, grade 9.3, reading ease 72.4 (checked on a scratch copy).

**Craft test 1 (storytelling), rechecked: PASS once N1 is fixed.** Line of the story: when some attacked Greek philosophy, the head of the Alexandrian school answered that it was God's preparation for Christ, and Origen and Jerome took that up. Bar: Origen's opening, "Around the year 202, the emperor Severus began to persecute the churches ..." The new opening reaches that level: it starts on what was going on and brings the person in as the one who acted in it.

**Craft test 2 (flow), rechecked: fails at one link, mended by N1.** Weakest link: "... Pantaenus, who led the school before Clement. / His answer was that God is the cause of every good thing." Bar: Gregory of Nazianzus, "Apollinarius held that Christ had no human mind. Against him Gregory wrote ...", where the answer names whom it answers. With "Clement's answer to those critics" the link is carried, and the passage then reads as one telling.

---

## Summary

| Brief | Round 1 blocking | Round 2 status | New blocking | Verdict |
|---|---|---|---|---|
| justin-martyr | B1, B2 | both CLOSED | N1 (first mention "Eusebius of Caesarea"), N2 ("Justin expected") | BLOCKED |
| tatian | B1, B2, B3, B4 | all CLOSED | none | CLEARS |
| clement-of-alexandria | B1 | CLOSED | N1 ("Clement's answer to those critics") | BLOCKED |
| bardaisan-of-edessa | none | not changed (diff empty) | not reviewed | CLEARS (round 1) |
| dionysius-of-alexandria | none | not changed (diff empty) | not reviewed | CLEARS (round 1) |

Each remaining finding is a one-sentence fix with exact wording above. A round 3 recheck of those three sentences closes them, within the cap.
