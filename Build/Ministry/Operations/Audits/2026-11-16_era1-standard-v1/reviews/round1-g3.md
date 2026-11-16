# Round 1 review, group g3

## Step 0: the blind pair (written before opening the pattern, the bar or the batch)

Text X (a bishop of Alexandria in 306, the fallen, Meletius) and Text Y (a Cappadocian bishop recalled in 378, Eunomius, the Great Catechism).

My judgment: **X is the stronger Standard-v1 brief**, by a modest margin. Reasons:

1. **One through-line.** Every paragraph of X serves one story: the persecution produces the fallen, Peter's terms for them, the rival bishop, the split, the split outliving him, the rules outliving him. Y carries three separate stances (Eunomius, the Spirit, restoration of all) and links them only by sequence.
2. **Stance then consequence.** X ties its main stance to its outcome in held-source terms ("Epiphanius ... says the two ... split over the fallen"; "In 325 the council of Nicaea left Meletius the name of bishop"). Y has to say "The sources we have do not show what came of this teaching in his own day" for its third stance, and its 381 law "gives no reason", so the link from stance to result is thinner.
3. **Wandering.** Y's first paragraph spends a long sentence on charges about church money and an imperial official, which does not set up any stance that follows. X's weakest stretch is paragraph 3 ("An old account kept with their letter says he then came to Alexandria..."), which is dense but still moves the story.
4. **Disagreement handled plainly.** X's "Why the two broke is disputed" sets out two ancient witnesses side by side, each named with their stake (Athanasius as "the Meletians' enemy"). That is the right shape for a contested claim.

Where Y is better: its quotations are shorter and more striking ("is above every name"), and its opening places the reader in a wider political frame faster. X's paragraph 3 is the one place a listener may lose the thread (three groups of actors in two sentences).

Which was which (added after the full read): **X was the batch brief (`peter-of-alexandria`); Y was the bar (`gregory-of-nyssa`).** I preferred the new brief, for the concrete reasons above (one through-line, a sourced consequence for each stance, a dispute set out in place). That is not the "preferred without a concrete reason" case, but the coordinator should know the batch brief was preferred over a bar brief. The one place I marked X as weakest (paragraph 3) holds the brief's one blocking finding (Peter B1).

## Bar briefs compared against

Gregory of Tours and Benedict of Nursia (opening, witnesses, impact half); Athanasius, Methodius of Olympus, Origen, Gregory of Nyssa, John Chrysostom and Ephrem (prose); Constantine for the council (Nicaea, a gathering told through acts). All ten read in full before the batch.

## Readability

`python3 -m engine.m1.profile_readability --report <path>`, run 2026-11-16.

| Brief | Words | Grade (full) | Grade (names out) | Reading ease (names out) | Words a sentence | Joining words /100 | Short sentences | Result |
|---|---|---|---|---|---|---|---|---|
| peter-of-alexandria | 302 | 8.8 | 7.2 | 71.9 | 15.9 | 0.7 | 16% | pass |
| anatolius-of-alexandria-and-laodicea | 291 | 9.1 | 7.1 | 76.6 | 18.2 | 0.3 | 0% | pass |
| eusebius-of-caesarea | 302 | 9.5 | 7.6 | 72.4 | 17.8 | 1.0 | 18% | pass |
| councils-of-rome-and-carthage-251 | 415 | 9.0 | 7.7 | 70.8 | 17.3 | 0.5 | 25% | pass |

Signals: Anatolius's 0.3 joining words sent me to read its links harder (Anatolius B1). The council's 25% short sentences are spread out, not a run; two are joinable (non-blocking). Eusebius's 18% short sentences include three one-line paragraph hinges (Eusebius B2). No brief opens on "The X was Y". No brief closes on a quotation. No modern scholar, editor or translator is named in any brief; none uses "the tree", "on the map" or "the census".

---

## 1. peter-of-alexandria (batch3): BLOCKED, 1 blocking finding

### Blocking

**B1. "While he made room for the fallen, another Egyptian bishop, Meletius of Lycopolis, was ordaining clergy in other bishops' districts, and four bishops in prison wrote to protest."**
The writer flagged it, and the held sources do not carry "while". The canons are dated by Peter only to "the fourth passover of the persecution" (ANF 6, `anf06_...xml` 26607-26608). The four bishops' letter (ANF 6, 16709-16724) and the old account after it (16820-16844) give no date. The account says only that Meletius entered Alexandria after "all these bishops and presbyters and deacons had suffered martyrdom in the prison" (16822-16824). Athanasius (`npnf204` 24777-24781) and Epiphanius (`epiphanius_panarion...oehler1860.txt` 43676-43683) place the break "in that persecution", nothing closer. "While he made room" ties the ordinations to the time of the canons. It also gives the break Epiphanius's framing (mercy against rigor) one paragraph before the brief tells us that cause is disputed. Unsupported and slightly leading.
Fix I would accept: "In the same persecution, another Egyptian bishop, Meletius of Lycopolis, was ordaining clergy..." (or the writer's "In those years"), with nothing else changed.

### Checked and sound

- "In 306 ... in its fourth year" and "That Easter": Peter's "fourth passover of the persecution" (26607-26608) against Eusebius's edict "in the month Dystrus ... when the feast of the Saviour's passion was near" in Diocletian's nineteenth year (`npnf201` 43480-43489). The year is reckoned arithmetic on two ancient anchors, of the same kind as the bar's opening years. It is not a modern scholar's own claim told flat. The card keeps McGiffert's reckoning, as the refs say. Accept.
- Canon I's terms, the forty days (26609-26624); "then be received" is Balsamon's and Zonaras's reading (26636-26641, 26660-26665), and it is a fair reading of the canon's "it is sufficient". Canon XIII (27536-27538): "neither is it lawful to accuse those who have left all, and have retired for the safety of their life". Matches.
- The four bishops' protest at ordinations "in parishes having no manner of connection with thee" (16709-16724); in prison (16821-16824). The account: he suspended presbyters "to whom the blessed Peter had given power" and ordained two in their place (16836-16844). Peter's letter: "hold no communion with him, until I meet him" (27790-27804). All match.
- Athanasius: Meletius "convicted of many crimes, and among the rest of offering sacrifice to idols, Peter deposed him in a general council" (24777-24781); "like dogs unable to forget their vomit" (24804) carries "the Meletians' enemy"; "even yet called Meletians" (24782-24784); reports spread "as they had practised against Peter" (24838-24844). Match.
- Epiphanius: both held together, the dispute over the fallen, Meletius for waiting "pace constituta", Peter "benignus ac misericors", and "maior numerus" of bishops, monks, presbyters and others joining Meletius (43676-43683, 43786-43806, 43894-43933). Match.
- Beheaded, "seized for no cause and quite unexpectedly", in the ninth year (`npnf201` 43266-43268, 47993-47998). Nicaea's letter: Meletius to "exercise no authority either to ordain", keeping "a nominal dignity" (`npnf202` 3204-3211). Trullo canon 2 and its penalty clause (`npnf214` 26731-26760); 692 at 26350. Match.

### Quotation

"did not come to this by their own choice, but were betrayed by the weakness of the flesh." This matches FINAL E36 (`comparison.md`) word for word. The printed span stands at ANF 6 lines 26616-26617 (checked; the refs record's 26614-26615 is two lines off, which is a records fix, not a brief fix). The reading covers "they did not come to this of their own will, but were betrayed by the frailty of the flesh" and adds nothing. Sound.

### Non-blocking

- Epiphanius is named without a leaning. He writes warmly of Meletius's side ("a veritatis amore profecta, et divini ardoris plenissima ratio", 43806-43808). Three words ("who writes kindly of Meletius") would balance "the Meletians' enemy" and help the listener weigh the two.
- The held fragments carry a theological stance the brief does not tell: "On the Godhead" and "Of the Soul and Body" (ANF 6, 27808 onward and 28084). The note that the first comes "from the Acts of the Council of Ephesus" is Galland's (27810), an editor's note. If the Acts are not held, it is rightly left out. If they are held, a consequence may exist, but it would not outweigh either stance the brief tells.

### Craft tests (bar beside brief)

1. **Storytelling: passes.** The line: a bishop took the fallen back on mild terms, lost much of his clergy to a stricter rival, and left behind both a split and a body of church law. Weakest: "That Easter Peter set the terms." Beside Origen, "His father died a martyr. In his eighteenth year Origen took charge...". It carries the scene, at the same level.
2. **Flow: passes, after B1.** Weakest link: "...four bishops in prison wrote to protest. / An old account kept with their letter says he then came to Alexandria and replaced priests Peter had appointed." The "then" skips the account's own link, that he came after the four had died in prison. Beside Gregory of Nyssa, "After Basil died, Gregory wrote, he 'inherited the controversy with Eunomius.'" It is close to that level; "after the four had died in prison" would close the gap.
3. **No AI tells: passes.** Weakest: "Peter's rules lasted too." It mirrors "but the split outlived him" two sentences earlier, a small paired cadence. Beside Athanasius, "Either way, the council deposed him." It sits at the bar's level. It would be better joined, without a colon reveal: "His rules outlived him as well, for in 692 the council in Trullo..."
4. **No hanging sentences: passes.** The close, "In 692 the council in Trullo set its seal on his canons, making them church law", finishes the story. It is the same close as the bar's Gregory of Nyssa.
5. **Everything relevant: passes.** Weakest: "He also forbade anyone to accuse those who had fled to save their lives." It is a second example, with no consequence of its own. It still belongs to the same stance (his terms for those the persecution broke) and is one line. Beside Athanasius's "Sozomen adds a rumor that Athanasius had hidden the man himself", it is at that level.

### Sentence test: 19 sentences, 1 marked

- "Peter's rules lasted too." It is a transition that only connects; join it into the Trullo sentence (craft test 3).
- Borderline, not counted: "He also forbade anyone to accuse those who had fled..." (above).

Length: 302 words, under 325. No judgment needed.

---

## 2. anatolius-of-alexandria-and-laodicea (batch3): BLOCKED, 2 blocking findings

### Blocking

**B1 (craft: storytelling and flow). "...and the Christians there kept him as their own. / One story about him was still told in Eusebius's day. When Roman troops besieged a quarter of Alexandria..."**
The brief opens around 270 in Laodicea, then steps back to an undated siege in Alexandria, with only a sentence that connects and nothing that says it came earlier. Eusebius places the siege before Anatolius left Alexandria: the two pastors came to Laodicea "after the aforesaid war from Alexandria" (`npnf201` 42764-42767, VII.32.12). A listener will place the siege after Laodicea. The siege also leads nowhere: the next sentence ("Eusebius says he wrote little...") does not follow from it. This is the weakest link in the brief, and it fails the flow test beside Gregory of Nyssa ("After Basil died, Gregory wrote, he 'inherited the controversy...'") and Ephrem, where the famine scene opens the brief and the life follows from it. Signal: 0.3 joining words in every hundred. With "One story ... Eusebius's day", the siege sits as a block of its own, not part of the story.
Fix I would accept: rewrite the first two paragraphs so the siege is told in its place in the life, before Laodicea. For example, tell of the scholar of Alexandria and the siege he saved people from, then the journey to the synod and Laodicea. Or move the siege to the card and let the brief run from Laodicea to Easter to Whitby. Either way, drop "One story about him was still told in Eusebius's day."

**B2. "Bede, who tells it, says the king ruled for Wilfrid, though on the authority of the apostle Peter and not of Anatolius."**
Bede does not say "not of Anatolius". The king's ruling rests on Peter's keys (`bede_...giles1903.txt` 8186-8212), and Bede says nothing of Anatolius there. "And not of Anatolius" is the writer's own inference, put in Bede's mouth. The inference is fair, but under "Bede ... says" it becomes a claim the witness never makes.
Fix I would accept: "Bede, who tells it, says the king ruled for Wilfrid because Christ had given Peter the keys of heaven." The listener draws the contrast from that alone.

### Checked and sound

- "Around the year 270": Eusebius puts the final synod against Paul "during his reign", Aurelian's (`npnf201` 41936), and Aurelian's reign begins in 270 (Eusebius's own reckoning of reigns, 42377-42382). The editor's 268 (41945-41951) also falls inside "around 270". Both ancient and modern readings agree on the approximate year. Accept.
- Synod called him; passing through Laodicea, Eusebius dead, "detained by the brethren" (42929-42940); appointed successor (42683). "Stood first among the ablest men of our time" in arithmetic, geometry, astronomy (42684-42687). Match.
- Siege: "They say"; bread failed; the senate; "old women and children and old men"; "he saved almost all the besieged"; "under cover of these"; "by night" (42691-42763). Match.
- "Did not write very many works"; extracts on the passover (42769-42773). The nineteen-year cycle and the new moon of the first month on 26 Phamenoth (42787-42800), the fourth day in the first segment, the mistake of putting the first month in the segment before (42810-42817). "Starts each cycle with the new moon at the spring equinox" compresses "already passing through the fourth day" of the segment that begins at the equinox. Acceptable for a listener.
- "The sources we have do not show what came of his reckoning in his own lifetime": Eusebius goes on only to his death and successor (42942-42944). I searched the held Greek and Latin files that name Anatolius. The hits are other men of the name, or later writers. Accept.
- Whitby, 664: Colman's question (8117-8121), Wilfrid's answer (8133-8143), "kept by the whole church of Christ" (8140), 664 (8236-8238). Match.
- "Whitby": Bede's own word is "Streaneshalch, which signifies the Bay of the Lighthouse" (7958-7960). "[Whitby]" is the 1903 editor's bracket (10952). It is a place identification, not a claim about Anatolius. The synod is known everywhere under that name, and the pattern treats modern place names as plain geography (Peter's "In Egypt"). I accept it, as non-blocking. If the coordinator wants it carried by Bede alone: "at a synod in the kingdom of Northumbria, in England" (Bede: "the province of the Northumbrians", 7950-7951).

### Quotation

"no small or ordinary mistake." matches FINAL E35. The printed "commit no slight or common blunder" is at 42816-42817, and the reading covers it, with the verb outside the marks. Sound. (The refs note that the Greek is lost in the scan is wrong, per E35's original check. That is a records fix.)

### Non-blocking

- Bede III.3 (`bede_...giles1903.txt` 5749-5757) says that the northern Scots and the Picts kept Easter "believing that they therein followed the writings of the holy and praiseworthy Father Anatolius." That is a held consequence wider than Whitby. It also carries "his name carried far" better than the narrator's pivot does. Consider it in the rewrite for B1, if words allow.
- Paul of Samosata is named with no word on why he was judged. "No statements that have no context." Half a clause would do: "for his teaching about Christ" (Eusebius VII.27, 41753-41755).
- Mark's condition (only what the held sources show; say plainly where the record stops) is kept: "The sources we have do not show what came of his reckoning in his own lifetime."

### Craft tests (bar beside brief)

1. **Storytelling: fails (B1).** Line: an Alexandrian scholar became bishop of Laodicea, set down a rule for Easter, and four centuries later both sides of an English quarrel claimed him. The siege does not fit that line. Weakest: "One story about him was still told in Eusebius's day." Beside Methodius: "Little else about Methodius is certain. Jerome says he was bishop of Olympus and later of Tyre..." Methodius's aside is short and in its place. This one is out of time and leads nowhere.
2. **Flow: fails (B1).** Weakest link: the one quoted in B1. Beside Origen: "In his eighteenth year Origen took charge of teaching the faith in Alexandria, because everyone else had fled."
3. **No AI tells: passes.** Weakest: "The sources we have do not show what came of his reckoning in his own lifetime, but his name carried far." It is close to the bar's own Gregory of Nyssa line ("The sources we have do not show what came of this teaching in his own day"). "But his name carried far" is a mild narrator's pivot; Bede III.3 would carry it.
4. **No hanging sentences: passes after B2.** The close finishes the Whitby story. With B2's fix, it ends on the ruling and its ground, the way the bar ends Gregory of Tours on "his is the only account we have".
5. **Everything relevant: passes.** The Easter passage and Whitby are the brief's reason to exist. The siege is the only part in question, and B1 covers it.

### Sentence test: 16 sentences, 1 marked

- "One story about him was still told in Eusebius's day." It is a transition that only connects (B1). The two siege sentences are personal and are allowed by "personal first"; they are not counted, but they must be placed (B1).

Length: 291 words, under 325.

---

## 3. eusebius-of-caesarea (batch1): BLOCKED, 2 blocking findings

### Blocking

**B1. "Socrates himself copied the letter into his account of Nicaea and treated it as an authority."**
Socrates's words, "treating what he has said as an authority" (`npnf202` 2866-2870), are said of Eusebius's account of the council quoted just before them (from 2837, "it may be well to hear what Eusebius says"). They are not said of the letter, which Socrates brings in later, at 2978-2979 ("what was written by Eusebius was as follows in his own words"). The brief joins the phrase to the wrong text. The writer flagged this and offered a fix.
Fix I would accept: "Socrates himself built his account of Nicaea on Eusebius's words, treating them, he says, as an authority, and copied the letter in full." Or the writer's version: "Socrates built his account of Nicaea on Eusebius's words and treated them as an authority."

**B2 (craft: no AI tells). "Arius was the test of Eusebius himself."**
It opens a paragraph on a thesis (item 4: "a paragraph that opens on a thesis"), and the judgment is the narrator's own. No held source frames Arius as Eusebius's "test". It also hinges on the last word of the paragraph before ("passed lightly over Arius"), a turn built for effect. With "Later historians built on it." and "That letter followed him.", it makes the third one-line paragraph hinge in a 302-word brief. The bar uses that move once at most (Athanasius: "That stand cost him his city again and again.").
Fix I would accept: cut it, and open the paragraph "In 325, at the council of Nicaea, Eusebius read out his own creed before Constantine." That is the writer's own alternative.

### Checked and sound

- 303 and the edict (`npnf201` 43480-43489). Pamphilus, "my dearest friend" (46694-46698), "the only one honored with the position of presbyter at Cæsarea", with "most sincere devotion to the Divine Scriptures" (47072-47080), tortured and put in prison (46700-46709), sentence of death (47186). The Martyrs of Palestine is itself Eusebius's account. Match.
- Q1 context: from the apostles (6925-6937). Built from older writers, "having plucked like flowers from a meadow the appropriate passages" (6961-6965). Match.
- Socrates I.1: Eusebius "but slightly treated of matters regarding Arius, being more intent on the rhetorical finish of his composition and the praises of the emperor, than on an accurate statement of facts" (1860-1866); "since his time to our own day" (1866-1867). Theodoret: "I shall begin my history from the period at which his terminates" (`npnf203` 5219-5222). "Each began ... where his ended" is exact for Theodoret and close enough for Socrates, who says he begins with "the particulars which he has left out". Accept.
- The letter: "our own paper ... read in the presence of our most pious Emperor" (`npnf204` 19565-19568); the emperor's approval and "the insertion of the single word" (19655-19661); "we did not let it pass without inquiry" (19699-19702). Socrates: "held aloof for a short time ... at length acquiesced ... subscribed it" (`npnf202` 2971-2979). Match.
- Socrates II.21: some "stigmatize even Eusebius Pamphilus himself as having favored the Arian views" (6918-6920). Athanasius, De Decretis 3: "who had denied the day before, but afterwards subscribed ... I have subjoined at the end the letter of Eusebius" (`npnf204` 26780-26795). "To show that even Eusebius had signed its creed" is a fair reading of Athanasius's purpose. Match.

### Quotations

- "Since I am the first to take up this subject," he wrote, "I am trying to travel what is, so to speak, a lonely and untrodden road." This matches FINAL E37. The printed span (6936-6937) is covered.
- "of the same essence": matches FINAL E38, and the brief has "as the Father", as the comparison requires. Sound.

### Non-blocking

- Item 5: the held sources show one more stance with a consequence, Eusebius against Eustathius of Antioch over the meaning of homoousios (Socrates I.23-24). It ends in Eustathius's deposition, with Eusebius offered the see of Antioch and refusing it. It bears on the brief's own Nicaea thread more directly than Athanasius's use of the letter does. The writer moved it to the card. That is defensible at this length; I note it for the coordinator.
- Athanasius is a hostile witness to the party Eusebius was later linked with. "Defending Nicaea" gives his leaning well enough.

### Craft tests (bar beside brief)

1. **Storytelling: passes.** Line: a scholar of Caesarea who came through the persecution wrote the church's first history, hesitated at Nicaea and explained his signature in a letter, and the writers after him both leaned on him and doubted him. Weakest: "He became bishop of Caesarea and wrote the story of the church from the apostles to his own day." Beside Gregory of Tours ("so he wrote ten books of History himself"). The brief's sentence states the fact but gives no reason; Gregory's gives one. It is acceptable, because the quotation that follows supplies the reason.
2. **Flow: passes.** Weakest link: "...copied their own words into his pages. / Later historians built on it." Beside Athanasius's "That stand cost him his city again and again." It is at the level of the bar's own hinge.
3. **No AI tells: fails (B2).** "Arius was the test of Eusebius himself." Beside John Chrysostom's opening paragraph: a scene, two witnesses and a judgment on each, with no device.
4. **No hanging sentences: passes after B1.** The close, on Socrates using Eusebius, finishes the second consequence. With B1's fix it is sound. "That letter followed him." is a hinge, but it leads straight into its proof.
5. **Everything relevant: passes.** The Life of Constantine sentence earns its place, because it is the doubt that later writers raised. Each sentence serves either the History or the Nicaea letter.

### Sentence test: 17 sentences, 1 marked

- "Arius was the test of Eusebius himself." (B2).

Length: 302 words, under 325.

---

## 4. councils-of-rome-and-carthage-251 (Council-Profiles/era1): BLOCKED, 1 blocking finding

### Blocking

**B1. "Eusebius of Caesarea, working from letters of Cornelius that survive only through him, says sixty bishops met there."**
"Survive only through him" rests on McGiffert's note, "These epistles are no longer extant" (`npnf201` 38324). Eusebius says only that the letters "have reached us" (38320-38327, VI.43.3). This is a claim resting only on a modern editor, told flat in the brief, which Mark's rule forbids (Who pattern, "No later scholars"; council C9). The writer flagged it.
Fix I would accept: "Eusebius of Caesarea, working from letters of Cornelius that had reached him, says sixty bishops met there." McGiffert's note goes to the entry's `record`/`uncertain`, by name.

### Checked and sound

- "In 251": no ancient year number. The witnesses tie it to the end of Decius's persecution (Cyprian, "when the persecution was quieted", `anf05` 33506-33507; Socrates IV.28, `npnf202` 14069-14082). The year is where the historians agree, which C4 allows. Accept; `datesNote` must say it is reckoned.
- Cyprian's delay "so that when quiet and tranquillity should be granted ... the bishops [might] assemble" (`anf05` 33476-33481). "A large number of bishops ... we met together", the "wholesome moderation", hope not wholly denied "lest ... they should, like the world, live as heathens", long repentance, the cases examined, "a little book" of the decisions (33506-33524). Certificate-holders admitted in the meantime and the sacrificed assisted at death (33780-33783). The letter to Cornelius, and Rome's agreement (33524-33529). All match. "The book of their decisions is lost": it is not in the held Cyprian files, and Cyprian himself only sent it. This is an honest limit of the held record, said once and early (C2).
- Rome: "a very large synod ... of bishops in number sixty"; Novatus and his followers "strangers"; the fallen healed "with the medicines of repentance" (`npnf201` 38272-38299). Socrates: a presbyter who separated "because Cornelius ... received into communion believers who had sacrificed", made bishop "by such bishops as entertained similar sentiments", whose letters asked the churches not to admit them "to the sacred mysteries" but leave "the pardoning of their offense to God" (`npnf202` 14061-14090). The "strict discipline" kept "even to the present day, in the provinces of Phrygia and Paphlagonia" (14057-14061). Match.
- The East: Dionysius to Novatian (`npnf201` 38922-38925); "all the churches throughout the East and beyond, which formerly were divided, have become united"; "had rejected the novelty of Novatus" (39350-39360). Match.
- The later African letter: "now, when we see that the day of another trouble is again beginning to draw near ... we have decided that peace is to be given" to those who "have not ceased from the first day of their lapse to repent" (`anf05` 34270-34299). Match.
- "Novatian's clergy" at Nicaea: canon 8, "those who call themselves Cathari ... shall continue as they are in the clergy", with the written promise to communicate with "those who having lapsed in persecution have had a period [of penance] laid upon them" (`npnf214` 3768-3779). The Cathari are tied to Novatian by an ancient witness: Eusebius, Novatus "became leader of the heresy of those who ... call themselves Cathari" (`npnf201` 38265-38270). Two ancient sources carry the link. Accept.
- "The way back itself held, for in 325...": "for" gives the canon as evidence that the rule stood. It does not claim that Nicaea cited 251. Acceptable as worded.
- Novatian's teaching has two witnesses: Socrates, and Cornelius in Eusebius ("as if there was no longer for them a hope of salvation", 38266-38267). The brief says it "reaches us mostly through such opponents" (C3). Sound.

### Quotation

"It would have been right to suffer anything at all rather than split the Church of God." matches FINAL E39, which covers the printed "For it were better to suffer everything, rather than divide the Church of God" (38924-38925; "For" is left outside, and it adds nothing). Sound.

### Council checklist (C1 to C9, brief only; entry and records out of scope this round)

- C1: entry, not reviewed. In the brief, each witness has its kind and side: Cyprian as the one "who called the meeting and defended it afterward"; Eusebius working from Cornelius; Socrates "nearly two centuries later".
- C2: passes. "The book of their decisions is lost. What they decided reaches us from Cyprian..."
- C3: passes.
- C4: passes. "Sixty" is given with its witness, and Carthage's "large number" is Cyprian's own. No modern month. "In 251" is within the agreed range.
- C5: passes. The issue (the lapsed), the decision (case by case and long penance; Novatian outside) and what came of it (Rome's agreement, Novatian's churches, the East, Carthage's change, Nicaea) are kept apart.
- C6: not applicable. No creed.
- C7: entry, not reviewed.
- C8: passes. 415 words is about 2:45, inside the stretch toward 3:00.
- C9: fails on B1 only. The opening gives the year, the places, North Africa, the three traditions and what was going on; each decision is followed by its consequence.

### Non-blocking

- The closing sentence runs about 41 words, past the guide of about 25. It reads straight through, but splitting it would help the ear: "The way back itself held. In 325 the council of Nicaea let Novatian's clergy keep their rank, but only if they promised in writing to share communion with those who had lapsed and done penance." (That leaves the judgment standing alone, so the writer may prefer to keep the "for" and split later in the sentence instead.)
- "The book of their decisions is lost. What they decided reaches us from Cyprian, who called the meeting and defended it afterward." Two short sentences the bar would join: "The book of their decisions is lost, so what they decided reaches us from Cyprian..."
- The opening names "Novatian's strict churches" before the listener knows who Novatian is (paragraph 3). It is acceptable, since the traditions must come early, but a word would help: "the strict churches of the Roman presbyter Novatian".
- Socrates was friendly to the Novatians, and his own chapters show it. Where he is the one witness to Novatian's own rule, a few words of leaning would sharpen trust. Optional.

### Craft tests (bar beside brief)

1. **Storytelling: passes.** Line: after Decius, Carthage and then Rome agreed that the fallen could come back through long, case-by-case penance; Novatian's party refused and became churches of its own; the East first divided and then rejected him; Carthage itself eased its rule when persecution came near; and Nicaea made the way back a condition for receiving Novatian's clergy. Weakest: "Two councils took up their case, one of the Latin church of North Africa and one of the church of Rome, and Novatian's strict churches grew out of the quarrel." It reads as a summary ahead of the story. Beside Constantine: "That year Constantine marched on Rome ... and with him begins Imperial and Juridical Christianity." It is at that level.
2. **Flow: passes.** Weakest link: "The book of their decisions is lost. / What they decided reaches us from Cyprian..." (see non-blocking). Beside Methodius: "Both men admired Origen, so neither is a neutral witness." It falls a little short of the bar, but it does not fail.
3. **No AI tells: passes.** Weakest: "Carthage's long penance did not last. ... The way back itself held, for..." This "did not last ... held" pairing is the one near-device. Each half carries a sourced fact, so it is not a "not X but Y" reveal. Beside Gregory of Nyssa's plain close, it is close to the bar's level.
4. **No hanging sentences: passes.** "The quarrel divided the East as well." and "Carthage's long penance did not last." are topic lines that lead straight into their proof, like Athanasius's "That stand cost him his city again and again." The close finishes the story on the council's reach.
5. **Everything relevant: passes.** Weakest: "In Phrygia and Paphlagonia, Socrates says, the strict churches still kept that rule." It is the one held sign of how long Novatian's churches lasted under their own rule, and Nicaea shows only that they were there in 325. It earns its place.

### Sentence test: about 24 sentences, 0 marked

Every sentence moves the issue, a decision or a consequence. The nearest candidate is the Phrygia sentence (above), and it stays.

### Length (415 words, aim 2:00, stretch toward 3:00)

It stands at about 2:45, inside the stretch, and each paragraph earns its place. Paragraph 1 is the setting and the traditions. Paragraph 2 is Carthage, from its one participant witness. Paragraph 3 is Rome and the break with Novatian. Paragraph 4 is the condemned side in its own terms, which C3 requires. Paragraph 5 is the reach east, the only reach beyond Rome and Africa before Nicaea. Paragraph 6 is the two later consequences. Nothing must go. If Mark wants it nearer 2:00, cut in this order: (1) the Phrygia sentence, 16 words, because Nicaea already shows Novatian's churches standing; (2) join the "book is lost" pair, about 4 words; (3) the closing clause "and been given a term of penance" could become "and done penance", 3 words. Together that is about 25 words, bringing it to about 390, or 2:35. Going further would cut a consequence, which the pattern forbids. Keep the East paragraph.

