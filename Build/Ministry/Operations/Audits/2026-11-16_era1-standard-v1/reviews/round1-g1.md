# Round 1 review, group g1

Briefs: `hermas` (batch1), `ignatius-of-antioch` (batch1), `polycrates-of-ephesus` (batch3), `josephus` (batch1, outside witness).

## Step 0: the blind pair (written before opening the pattern, the bar or the batch)

Judgment: **Y is the stronger Standard-v1 brief**, by a clear but not wide margin.

Reasons, concretely:

1. **Personal first, then impact.** Y opens on the one external report, then gives the man (sold to Rhoda, the vision in which she accuses him), then the stance, then what came of it. X moves from setting straight into how two partisan writers described Methodius's inconsistency, then a thin bio paragraph ("Little else about Methodius is certain"), and only reaches his stance in the fourth paragraph. The order in X puts reception ahead of the stance it is reception of.
2. **Stance followed by what came of it.** Y has one stance (a second repentance after baptism), states the teaching it answered ("the only repentance is the one made in baptism"), shows the practical rule that followed, and then gives four named reactions (Irenaeus, Tertullian, Muratorian list, Eusebius), each a consequence of the book's standing. X has two stances (the body against Origen; the reply to Porphyry) and gives each a consequence (Epiphanius copied him; Jerome and Theodoret valued him), but the Porphyry paragraph's consequence is only that later writers praised a lost work.
3. **Where the record stops.** Y names its limit twice and plainly ("Everything else about him comes from inside his own visions"; "What became of Hermas himself, no source says"). X says "Little else about Methodius is certain" and then lists Jerome's uncertain claims flat, without saying whether anything earlier or independent backs them.
4. **Sentence test.** X's second paragraph is mostly about Socrates' and Eusebius's view of Methodius's consistency and ends on a source-criticism note ("neither is a neutral witness"); that is the kind of sentence that does not move the story. Y has fewer such sentences.

Where X is stronger: X's fig-tree-in-the-temple image is the most vivid single passage in either text, and its quotation lands the stance. Y's weakest sentence is a garbled one: "In his book the Shepherd, an angel sent to live with him, agrees ..." reads as if the book and the angel are the same thing; the ear loses who is speaking.

After the full read: **X was the bar brief (Methodius of Olympus); Y was the batch brief (Hermas).** I preferred the batch brief, for the concrete reasons above (shape, stance-to-consequence, a plainly named limit). The coordinator should note the result. The weak sentence I flagged in Y before I knew which was which is finding B3 under Hermas below.

## Bar briefs compared against

Methodius of Olympus (the thin-record model, for Hermas and Polycrates), Gregory of Tours and Benedict of Nursia (the Standard v1 opening, witnesses and impact), Origen, Ephrem the Syrian, Athanasius of Alexandria, Gregory of Nyssa and John Chrysostom (prose and closes). All from `Who-Profiles/bar/` as they stand on this branch.

## Readability (`python3 -m engine.m1.profile_readability --report`)

| Brief | Words | Grade (full) | Grade (names out, info) | Reading ease (names out) | Words a sentence | Joining words /100 | Short sentences | Tool |
|---|---|---|---|---|---|---|---|---|
| hermas | 314 | 9.4 | 9.0 | 70.6 | 22.4 | 1.3 | 14% | pass |
| ignatius-of-antioch | 305 | 8.3 | 7.7 | 74.0 | 19.1 | 1.3 | 12% | pass |
| polycrates-of-ephesus | 331 | 9.3 | 7.8 | 74.0 | 19.5 | 0.6 | 12% | pass |
| josephus | 295 | 9.9 | 8.3 | 73.4 | 21.1 | 1.0 | 14% | pass |

All four are inside the floor and ceiling. Hermas runs long a sentence (22.4) and Josephus sits near the ceiling (9.9); both are noted under access. No brief uses "the tree", "on the map" or "the census" (item 18), and none names a modern scholar (see the one naming note under Hermas).

---

## hermas (batch1): BLOCKED, 3 blocking findings

### Blocking

**B1. The date and "the one early report we have" hide a second ancient report.**
- Sentence: "Around the year 150, by the one early report we have, a Christian named Hermas lived at Rome ..."
- Evidence: Eusebius, Church History III.3.6, says the book called The Shepherd "is ascribed" to the Hermas whom Paul greets in Romans (npnf201 lines 14753-14760 and 14848-14860, the same passage the brief draws on for "read in churches"). Jerome, Lives of Illustrious Men 10, says the same: the Hermas of Romans 16 "is reputed to be the author of the book which is called Pastor" (npnf203 lines 39614-39627). So the held ancient sources carry two reports: the Muratorian list's (brother of Pius, about 150) and the Origen–Eusebius–Jerome ascription (Paul's time). The refs record moved the second to the card as "a mere guess" (refs (a), on McGiffert's word, E 14793-14796). That makes the brief's choice rest on a modern scholar's judgment, and "the one early report we have" is not true of the held sources. This is a date dispute that touches the story (the brief's whole setting), so under "The brief", Witnesses, it is either told in a sentence with each side named or the brief claims only what both sides accept.
- Fix I would accept: either (a) keep the Muratorian report as the earliest and add one clause naming the other side: "Eusebius of Caesarea and Jerome took him instead for the Hermas whom Paul greets in his letter to the Romans"; or (b) open on what both sides accept (a Christian of Rome who wrote the Shepherd) and give the two datings in one sentence. Drop "the one early report we have" in either case; "the earliest report" is accurate.

**B2. The "one repentance more" is told wider than the source gives it.**
- Sentence: "... agrees that the baptized ought not to sin again, but says the Lord knows human weakness and in mercy has set one repentance more."
- Evidence: Commandment 4.3, anf02 lines 1996-2003: "For those who have now believed, and those who are to believe, have not repentance for their sins; but they have remission of their previous sins. For to those who have been called before these days, the Lord has set repentance." The Shepherd's concession is for those already baptized before this revelation, not a standing second repentance for all. The brief's sentence reads as a general rule, which is the point the later quarrel (Tertullian) turned on. This is the stance itself, so the scope matters.
- Fix I would accept: carry the limit in the same sentence, e.g. "... in mercy has set one repentance more for those already baptized", or "for those called before this time". No added length is needed beyond a few words.

**B3. A sentence the ear loses: two things called "the Shepherd".**
- Sentence: "In his book the Shepherd, an angel sent to live with him, agrees that ..."
- Evidence: the first paragraph has already named the book "the Shepherd". A listener hears "In his book the Shepherd," as the book's title in apposition and then "an angel sent to live with him" as a second apposition; the subject is lost. The source (anf02 1697-1705, 1724-1725) makes the shepherd "the angel of repentance" sent "to dwell with you". Item 4 (rhythm) and item 11 (a sentence the ear loses) both fail here, and it breaks the flow test (below) at the stance's own hinge.
- Fix I would accept: a rewrite of the hinge that says once that the book is named for the angel, e.g. "The book takes its name from an angel dressed as a shepherd, sent to live with him. This angel agrees that ..." Joining is allowed; the reason ("for those already baptized", B2) should sit in the same sentence as the concession.

### Non-blocking

- "So a husband must take back an unfaithful wife who repents": the husband's rule is in Commandment 4.1 (anf02 1924-1934), before the concession of 4.3, and carries its own reason ("for he ought to take back the sinner who has repented. But not frequently. For there is but one repentance"). The "So" is the writer's joining; it is fair to the doctrine but "In the same book" or "For this reason, he says," would track the source more closely.
- "The Muratorian list ruled that ...": "ruled" gives an anonymous list an authority it does not claim; "judged" is closer to "it also ought to be read" (anf05 60180). The "because it was written so recently" reads the list's "And therefore" (60180) in the usual way; acceptable.
- "Muratorian Canon" carries its 1740 editor's name (the writer's own flag). It is the document's name, not a scholar cited as authority, and I do not count it as naming a modern scholar. The writer's alternative ("an early Roman list of the church's books") is also fine.
- Jerome's chapter 10 (npnf203 39623-39627) is held and opened here: the book is "read publicly in some churches of Greece" but "among the Latins it is almost unknown". The refs say it was not opened. It is a fair card line; the brief does not need it.
- Words a sentence 22.4 is above the bar's range; the long sentences are the Tertullian and Eusebius ones in the last paragraph. They read in one breath; no change asked beyond B3.

### Craft tests (beside the bar)

1. **Storytelling.** Line: a Roman Christian, accused in a vision of his own sin, writes that the baptized have one repentance more, and the churches split over whether his book is Scripture. Weakest: "Everything else about him comes from inside his own visions." Model: Benedict, "Nearly all we know of his life comes from Gregory's Dialogues ..." Reaches the level.
2. **Flow.** Weakest link: "Then, in a vision, she greeted him from the sky ..." to "Hermas had heard teachers say that the only repentance is the one made in baptism.", followed by the B3 sentence. Model: Methodius, "His chief quarrel with Origen was over the body." The Methodius pivot names the quarrel; here the listener must supply that the accusation raises the question of repentance, and then loses the subject in the next sentence. **Does not reach the level**, at that hinge only; the fix is the rewrite under B3, which should also carry the link from his sin to the question (one clause: the vision accuses a baptized man of sin, so the question is whether he can still repent; in Vision 1.1 she tells him God "is angry with you for having sinned against me", that the desire which arose in his heart was "sin ... and the sin is great" (anf02 692-705), and he asks "If this sin is assigned to me, how can I be saved" (anf02 734), if the writer wants a source for the link).
3. **No AI tells.** Weakest: "What became of Hermas himself, no source says." Model: Gregory of Tours, "He does not say his stand cost him anything." Reaches the level; the inversion is mild.
4. **No hanging sentences.** Last line as above; it finishes the story by saying where the record stops, as Mark's Whos ruling requires. Reaches the level.
5. **Everything relevant.** Weakest: "That report, a list of the church's books known as the Muratorian Canon, says ..." Model: Methodius, which weighs a thin record in a few sentences and moves on. Trust turns on the one source, so it earns its place. Reaches the level.

### Sentence test

0 sentences marked. Every sentence serves the line (the Rhoda sentences set up the accusation the stance answers).

---

## ignatius-of-antioch (batch1): BLOCKED, 2 blocking findings

### Blocking

**B1. The wheat quotation does not match the comparison's final reading.**
- Sentence: "I am God's wheat, and let me be ground by the teeth of the wild beasts, so that I may be found the pure bread of Christ."
- Evidence: `AUD/renderings/comparison.md`, E15, FINAL: "I am God's wheat. Let me be ground by the teeth of the wild beasts, so that I may be found the pure bread of Christ." (A's words split in two, "and" dropped). The brief carries A's first form. The printed span (anf01 7040-7042) is covered by either; the rule for this round is that the words in marks match the FINAL.
- Fix I would accept: put the FINAL into the brief; or, if the coordinator prefers the brief's form (which keeps the printed "and"), change the FINAL in `comparison.md` with the reason recorded there. One or the other, not both left as they are.

**B2. "In the reign of the emperor Trajan" claims one side of a held date dispute.**
- Sentence: "In the reign of the emperor Trajan, early in the second century, Ignatius was bishop of Antioch ..."
- Evidence: the writer's own flag; refs (a) records that the date of his death is disputed, with Harnack's Hadrian date going to What is uncertain (E 19810-19816, 19852-19875). Trajan rests on Eusebius's placing alone (E 19679-19742, 16977-17008). The pattern's rule for a date dispute that bears on nothing else: the brief claims only what both sides accept ("The brief", Witnesses, third point). "Early in the second century" is accepted by both; "in the reign of Trajan" is not.
- Fix I would accept: "Early in the second century, Ignatius was bishop of Antioch ..."; or keep Trajan with its one witness named ("in the reign of the emperor Trajan, Eusebius of Caesarea says"), since a point resting on one source may name its witness.

### Non-blocking

- "so that everything done would be secure and valid": in Smyrnaeans 8 (anf01 8286-8289) the purpose clause hangs on "whatsoever he shall approve of, that is also pleasing to God", not directly on "Let no one do anything ... without the bishop". The meaning is close; "so that, he said, whatever the bishop approved would be secure and valid" would be exact.
- The census sourcing note and the writer's flag record that some readers put the letters later or treat them as later work. The brief tells them as his, per the assignment; that is the dominant view and the doubt is on the card. Not reopened here.
- The bishop stance has one sentence of substance and one of absence. That is honest to the record (the writer's search, refs (b), is credible; I found no held ancient witness taking up the bishop rule from him). No change asked.

### Craft tests

1. **Storytelling.** Line: a condemned bishop on the road to Rome answers those who said Christ only seemed to suffer, with his own chains, and his letters outlive him in other churches' hands. Weakest: "On the road he wrote six more letters." Model: Ephrem, which opens on the famine and follows the life from it. Reaches the level; the opening scene is among the strongest in the batch.
2. **Flow.** Weakest link: "... testimony that Christ was truly crucified in the flesh." to "Ignatius also stood for the bishop." Model: Gregory of Tours, "He held the same ground against the Arians of Spain." Reaches the level.
3. **No AI tells.** Weakest: "The sources we have do not show what came of this rule in other churches." Model: Gregory of Nyssa's same sentence. Reaches the level. (Across the fleet this formula is now common; a varied wording would keep it from becoming a tic.)
4. **No hanging sentences.** Last line: "Eusebius of Caesarea, two centuries later, gives his death at Rome only as a report, but he names all seven letters and says that many still celebrated his fame." Model: Origen's close on the council list. It finishes the story (death, letters, memory) with the witness's caution. Reaches the level.
5. **Everything relevant.** Weakest: "Polycarp, the bishop of Smyrna, sent the church at Philippi every letter of Ignatius he had." Model: Methodius, "Decades later, Epiphanius of Salamis ... copied Methodius word for word". It is the consequence of the letters. Reaches the level.

### Sentence test

0 sentences marked.

---

## polycrates-of-ephesus (batch3): BLOCKED, 1 blocking finding

### Blocking

**B1. The relatives sentence has lost its point and hangs.**
- Sentence: "Seven of his own relatives had been bishops, and he was the eighth."
- Evidence: Eusebius V.24.6 (npnf201 31384-31390): "I also, Polycrates, the least of you all, do according to the tradition of my relatives ... seven of my relatives were bishops; and I am the eighth. And my relatives always observed the day ..." In the letter the relatives are the second ground of his stand: they kept the day. The brief keeps the count and drops the point, so the sentence stands as a side fact between the dead of Asia and his age. This fails craft test 4 (hanging) and the flow test at that link.
- Fix I would accept: carry the point in the sentence, e.g. "Seven of his relatives had been bishops before him and all had kept the day, he wrote, and he was the eighth." That is a rewrite of the passage's middle, not a cut, since the relatives are part of his ground.

### Non-blocking

- 325 and after: "Constantine the Great wrote that the churches of Asia already kept it as Rome did. Yet some held on." The sources give the order of events, not when or why Asia came round; the brief has already said "the sources we have say nothing more of Polycrates", but it does not say that the record does not show how the break with Rome ended. A clause ("How or when Asia came round, no source says") would meet Standard v1's "says plainly that the record shows what followed but not why". The writer's two cautions on Constantine's letter (the civil diocese of Asia is wider than the province; the letter does not name the fourteenth-day custom, E 64677-64691) are sound and the brief's wording does not go past the letter.
- "Socrates of Constantinople says that two centuries after Polycrates, John Chrysostom took churches ...": "two centuries after Polycrates" is the narrator's reckoning, but the word order gives it to Socrates. "Two centuries after Polycrates, Socrates of Constantinople says, John Chrysostom ..." fixes it.
- Socrates VI.11 (npnf202 17976-17977) and VI.19 (18561-18564) carry the churches taken; VI.19 gives it as what Chrysostom's enemies said, VI.11 as fact. The claim to John (V.22, 16317-16318) is of Quartodecimans generally. The brief's "they" joins them; acceptable.
- Joining words 0.6 per 100, the lowest of the four. The prose still joins at the key points ("At the request of", "for greater men than he had said", "after the council of Nicaea ruled"); the signal mostly reflects the reported-speech paragraph.

### Craft tests

1. **Storytelling.** Line: an old bishop of Ephesus refuses Rome over the day of Easter on the authority of Asia's dead and his own family, Rome tries to cut Asia off, and his custom shrinks to a remnant that still names John. Weakest: "He wrote to Victor for them all, and Eusebius of Caesarea copied part of the letter." Model: Gregory of Tours, "The king said he would find wiser men, and put the decree to Salvius". Reaches the level.
2. **Flow.** Weakest link: "... was buried at Ephesus." to "Seven of his own relatives had been bishops, and he was the eighth." Model: Gregory of Nyssa, "Macrina had turned him around once before ... But it was his sister who persuaded him". **Does not reach the level** at that link; B1.
3. **No AI tells.** Weakest: "Yet some held on." Model: Constantine, "Maxentius was driven into the Tiber at the broken bridge." Plain, carries a fact; reaches the level.
4. **No hanging sentences.** The relatives sentence fails (B1). The close, on Chrysostom and the claim to John, finishes the stance's story. Model: John Chrysostom's close, the body carried home. Close reaches the level.
5. **Everything relevant.** Weakest: "Churches elsewhere waited for Sunday, and synods of bishops from Gaul to Palestine ruled for it." Model: Athanasius, "Nicaea answered that the Son is 'begotten, not made.'" It sets up the stand; reaches the level.

### Sentence test

1 sentence marked: "Seven of his own relatives had been bishops, and he was the eighth." (as written; with B1's fix it serves the line).

### Length (331 words, over 325)

Each part earns its place: the setting with the two customs (needed for the stand to mean anything), the synod and letter, his grounds, Victor and Irenaeus (the first consequence), and 325 to Chrysostom (the end of the custom). What could go: "Other bishops rebuked him." can be folded into the Irenaeus sentence ("Other bishops rebuked him, among them Irenaeus of Lyon, who ..."), which saves a sentence; B1's fix adds about five words. The stretch is justified by the two-stage consequence, as the writer says.

---

## josephus (batch1, outside witness): BLOCKED, 2 blocking findings

The form is right: who he was, what he says, how far it can be trusted, no "what they fought for" beat. The two findings are on the trust half, which is the point of an outside witness profile.

### Blocking

**B1. "The longer report cannot be trusted as it stands" is a narrator's verdict that the held sources do not carry, raised by no named witness, and it opens a paragraph on a thesis.**
- Sentence: "The longer report cannot be trusted as it stands."
- Evidence, three parts:
  1. *The ancient facts bear on one line, not the passage.* Origen says Josephus "did not accept Jesus as Christ" (anf09 30627-30628; also "although not believing in Jesus as the Christ", anf04 37933-37934). Jerome's version (npnf203 39724-39733) reads "was believed to be Christ" for "He was the Christ", but keeps "if indeed it be lawful to call him man", "a worker of wonderful miracles" and "he appeared to them the third day alive". So the held ancient evidence shows that the line "He was the Christ" was not in the form our copies give it, for Origen or for Jerome. It does not show that the rest of the passage is untrustworthy. Doubt about the rest ("if it is right to call him a man", the third-day appearance) is the modern case, and the modern views split four ways (McGiffert's note, E 9181-9226: wholly genuine, wholly added, partly genuine, a hostile passage rewritten). That is a judgment on a text that rests on modern scholars, and under "The brief", Witnesses, it goes to the card; the brief may claim only what the ancient facts carry.
  2. *Each doubt names who raises it and why* ("The outside witness"). Neither Origen nor Jerome raises a doubt about the passage; the doubt is the narrator's, built on them. The writer says so in the coordinator notes.
  3. *Form.* It opens the paragraph on a thesis and states the verdict before the evidence (item 4, "a paragraph that opens on a thesis"), which also fails the AI-tells test below.
- On the coordinator's ruling ("widely accepted facts are told plainly"): that the longer report has been altered in some part is the majority modern view, but it is a modern reconstruction, not a documented fact, and its extent is contested. It is not one scholar's reading, but it is not a fact the brief can tell plainly either. What is documented is the ancient evidence against the one line.
- Fix I would accept: a rewrite of the paragraph that gives our copies' wording first, then Origen and Jerome, and draws only the conclusion they carry, said as an inference from them. For example: "In our copies Josephus calls Jesus 'a wise man, if it is right to call him a man,' says 'He was the Christ,' and says ... alive on the third day. Yet Origen, who knew the Antiquities, wrote that Josephus 'did not accept Jesus as Christ,' and Jerome's copy said only that Jesus 'was believed to be Christ.' So at least that line cannot be what Josephus wrote." (The Jerome clause may then move up from the last paragraph, which keeps Jerome's chapter and Eusebius's use as the reception.) The modern views of the rest go to the card, under What is uncertain, which refs (d) already plans.

**B2. The James report is told as the sound one, but Origen's Josephus says more of James than our copies do, and the brief gives that "more" to "this report".**
- Sentences: "Origen of Alexandria ... read this report in Josephus and used it against Celsus, a critic of the Christians. Here, Origen argued, was a writer who did not believe in Jesus as the Christ and still testified that James was a just man."
- Evidence: our copies of Antiquities XX.9.1 (Whiston, josephus_works lines 90990-91013) say only that Ananus brought "the brother of Jesus, who was called Christ, whose name was James" and others before the judges and had them stoned. They do not call James just. Origen's Josephus says the fall of Jerusalem was God's punishment for the death of "James the Just", "a man most distinguished for his justice" (Against Celsus I.47, anf04 37932-37942; Commentary on Matthew X.17, anf09 30621-30630, "he yet gave testimony that the righteousness of James was so great"). Jerome repeats that Jerusalem fell "because of the murder of James" (npnf203 39719-39720). None of this is in our text. So the listener hears that "this report" testified James was just, which our copies do not; and the brief's contrast (the shorter report used and sound, the longer one untrustworthy) hides that Origen's text differs from ours on James too. Refs (a) moved the gap to the card, but the brief's sentence still leans on it. Also, in Against Celsus I.47 the report used against Celsus is first Josephus on John the Baptist (anf04 37925-37932); the James line comes in passing.
- Fix I would accept: keep Origen's use but say what his Josephus said without tying it to "this report", and let the trust half note the gap in a clause through the ancient witnesses: e.g. "Origen of Alexandria ... cited Josephus on James against Celsus, a critic of the Christians: here was a writer who did not believe in Jesus as the Christ, yet said James was a just man and that Jerusalem fell for his death. Those words are not in our copies." Alternatively, drop "and still testified that James was a just man" and keep only what the shorter report and Origen's quoted phrase share ("the brother of Jesus who was called Christ", which Origen's Greek has at Lommatzsch 3729-3730 per comparison E1).

### Non-blocking

- "the emperor Vespasian gave him a house in Rome": Life 76 (josephus_works 5403-5411) has "an apartment in his own house, which he lived in before he came to the empire". "Lodging in his own former house" is closer.
- Grade 9.9 is at the ceiling. The long sentences are in the Origen and Eusebius paragraphs; B1's rewrite is a chance to shorten them, not a requirement.
- "Around the year 93" is Whiston's conversion of Josephus's own "13th year of ... Domitian" (josephus_works 91662-91666); it is a plain calendar reckoning, not a scholar's judgment, and stays.
- Every other plainly told fact checked: priest of a priestly family (1385-1397), born in Jerusalem (3323-3326), governed Galilee (106926-106929; Life 5104-5116), taken by the Romans (4741-4743), house, citizenship and pension (5403-5411), Eusebius's quotation and his argument against the forged acts (E 9227-9246), Jerome's chapter (npnf203 39706-39733). None is contested; none rests on a modern scholar.

### Craft tests

1. **Storytelling.** Line: a Jewish priest writing at Rome mentions Jesus twice, and Christian writers relied on both reports, though neither has reached us quite as they read it. Weakest: "There he wrote the Antiquities of the Jews, and twice in it he speaks of Jesus." Model: Methodius, "Methodius wrote against him, and two of Origen's admirers wrote about what he did." Reaches the level.
2. **Flow.** Weakest link: "... Josephus 'did not accept Jesus as Christ.'" to "Eusebius of Caesarea, early in the fourth century, quotes the passage as we have it". Model: Methodius, "Both men admired Origen, so neither is a neutral witness." Joined by time and by "as we have it"; reaches the level, just.
3. **No AI tells.** Weakest: "The longer report cannot be trusted as it stands." Model: John Chrysostom's opening paragraph, scene, two witnesses and a judgment on each, with no device. The verdict-first sentence is a device (thesis opener). **Does not reach the level**; B1.
4. **No hanging sentences.** Weakest: "He was not a Christian." It is short but connects both ways and sets the outside-witness frame. Close: Jerome's version, ending on a quotation (signal); it finishes the trust story. Reaches the level.
5. **Everything relevant.** Weakest: "After Jerusalem fell, the emperor Vespasian gave him a house in Rome, citizenship and a pension." Model: Benedict, "Benedict built twelve monasteries near Subiaco and later moved to Cassino". It says how he came to write at Rome; reaches the level.

### Sentence test

0 sentences marked.

---

## Summary

| Brief | Verdict | Blocking |
|---|---|---|
| hermas | BLOCKED | B1 second ancient dating hidden; B2 repentance scope told too wide; B3 "Shepherd" sentence loses the ear |
| ignatius-of-antioch | BLOCKED | B1 wheat quotation not the FINAL; B2 Trajan date one-sided |
| polycrates-of-ephesus | BLOCKED | B1 relatives sentence lost its point |
| josephus | BLOCKED | B1 longer-report verdict overreaches sources; B2 James "just man" not in our report |

All four fixes are local rewrites of a sentence or a paragraph; none needs a new source.
