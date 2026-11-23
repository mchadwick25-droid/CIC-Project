# Fresh read, "what it was about" pass: Frumentius (`frumentius`)

Read: `frumentius.brief.txt`, against `Kit.md` as it now stands, `Outline.md` (including "What it was about" and "Room for it"), `Source_Sheet.md`, and the held texts in `cic/texts/`. Not opened: `Review.md`, `Revision.md`, `Fresh_Read.md`, `Fresh_Read_Applied.md`, `About_Check.md`, `Writer_About_Reply.md`, `Gaps.md`, `Outline_Synced.md`, any `.v1`/`.v2`.

## 1. The test, from one hearing

**The four lines.**
- Who: Frumentius, a boy from a family of Tyre, taken captive at a foreign court, who became the first bishop of Aksum, in what is now Ethiopia and Eritrea.
- What happened: spared when his ship's company was killed, he rose to help rule the kingdom, gathered the Roman Christian traders to pray, went to Alexandria to ask Athanasius for a bishop, and was sent back as that bishop.
- What it was about: planting a church among the traders and tying it to Alexandria, a tie the emperor Constantius then tried to break in his quarrel with Athanasius.
- Why the connection matters: Aksum's church began as a daughter of Alexandria's and kept taking its bishops from there; that is why the emperor demanded its bishop come to Egypt to be judged by Athanasius's replacement.

All four come through on one hearing.

**Each charge, teaching, book, quarrel or decision named, and whether a listener could explain it:**
- The broken treaty and the custom of killing every Roman: yes, told as the cause of the killing.
- Frumentius's request at Alexandria and Athanasius's choice: yes, with Rufinus's reason and Athanasius's words.
- The disputed date: yes, both dates and the editor credited.
- The teaching the emperor demanded: yes, now. The Arian sentence says what Arius taught and what Athanasius held, and credits the label "Arians" to Athanasius.
- "A man guilty of countless crimes": yes, now. The two main charges are given in their own content, and his denial.
- "Restore him only if found fit": yes, the examination is explained.
- The Ethiopian book of saints and the name Abba Salama: yes, glossed and dated.

**Essence and what is also told.** Essence (from the census and the record): a captive at the court of Aksum who gathered its first Christians and came back from Alexandria as their bishop, the root of the Ethiopian church's tie to Alexandria. The hook (three sentences) leads straight into it, and it is told by about word 115, inside the first minute. Also told, each with its weight: Rufinus's sole witness through Edesius (paragraphs 3 and 6), the traders' places of prayer (paragraph 5), the emperor's letter and its stakes (paragraph 11), the date dispute (paragraph 8), and the Ethiopian memory as Abba Salama (last paragraph).

**Order.** After the essence, the life runs once, in order: the voyage, the court, the traders, the return, Alexandria, the date, the bishop's work, the letter, what came after, the late memory. The killing is told in the hook and its cause in paragraph 3. That is the hook reaching ahead, which the kit allows, and not a retelling.

**Ending.** It ends on the person: his death in peace, in the book of saints' voice.

**Names heard once.** Constantine (link), Arius (link, on the census), Constantius (acts). None loses the listener.

**Where a listener might stumble.** "With once turning the emperor's brother against him": the "him" just after "Athanasius" can be heard as Athanasius (MINOR 1). Nothing reads as a children's book or talks down.

## 2. The bar

Judged against Kit Part 1 and the bar in Part 4. Nothing is unsupported or misleading, nothing essential is missing, and there is no failure on one hearing.

## 3. The source check

Every sentence traced to `Outline.md` and from there to the held texts.
- Rufinus, `eusebius_werke-bd2-2-historia-ecclesiastica-vi-x-rufinus-x-xi-grc-lat_schwartz-mommsen1908.txt` 27300-27386. The hook, voyage, harbour for water, custom, cup-bearer, accounts and records, freedom, the queen's plea, "deo ... instigante", the meeting places, the return, Tyre, Alexandria, "aequum non esse opus occultare dominicum", the wonders as "dicitur" and countless converts all match. Quote 1 ("et quem alium invenimus virum talem ... qui haec ita possit implere?", 27376-27377) and Quote 2 ("quae nos ita gesta non opinione vulgi, sed ipso Edesio ... referente cognovimus", 27383-27386) were re-checked verbatim. The renderings keep every clause and add nothing.
- The emperor's letter, PG25 92806-92814 and N204 36142-36162. "Οὐκοῦν Φρουμέντιον τὸν ἐπίσκοπον ἐκπέμπετε τὴν ταχίστην εἰς Αἴγυπτον" = "So send Frumentius the bishop to Egypt with all speed." "τὸν Φρουμέντιον τοῦτον εἰς ταύτην τὴν τάξιν ... κατέστησεν Ἀθανάσιος, μυρίοις ἔνοχος ὢν κακοῖς" = "This Frumentius was set in this rank by Athanasius, a man guilty of countless crimes." Both verbatim. The demand for "the same doctrine" (36143-36144), George's judgement and the restoration "if ... he has any right to be a Bishop" (36157-36162) are told in the narrator's words, correctly.
- Date: N204 1519 (328) and 5676-5684, 10405-10408 (Robertson: the chronology "forbids this altogether"; earliest "End of year" 346). Correct.
- Ending: Budge's Synaxarium (v2-v4 microform) 43608-43612, "preached the peace of Christ in all the regions thereof, and because of this he was called 'Abba Salama' ... he died in peace". Told in the narrator's words, credited, matches.
- "Around 400": the editor says "probably 401" (N203 44550-44552). "Around" holds it.

## 4. The score

`python -m engine.m1.profile_readability .../frumentius/frumentius.brief.txt`: **675 words** (at the 675 limit), grade 7.9 (names out 6.0), reading ease 79.8, 15.7 words a sentence, longest sentence 30, pass. Grade 7.9 is just under 8. On the listener read it is not flat: the longer sentences carry chains of cause, and the world's own wording survives ("a Christian seed might grow there", "signs like the apostles'").

## Comparison with `frumentius.brief.v3.txt`

`diff` shows six cuts and two additions, and one word changed.
- Cut: ", and calls Frumentius its bishop" (paragraph 2); ", whom he found sharp and wise," and ", leaving his wife and small son as heirs" (paragraph 4); ", and gave them sites for buildings," (paragraph 5); ", and says the emperor's letter reads more naturally if it was recent" (paragraph 8); "By 1681, a German scholar recorded, the Ethiopians counted ninety-five chief bishops in order from him." and ", Socrates almost word for word, one editor says" (paragraph 12). Each is "Room for it" cuts 1 to 7. Each removes detail, not meaning, and leaves no sentence untrue: the queen's "until her son grew up" still carries the heir, and the letter's own quote still says who made him bishop.
- "It ordered:" → "The letter ordered:". "Room for it", for clarity after the inserted sentences.
- Added: "Athanasius called the emperor's bishops Arians, after Arius, who taught that the Son had a beginning, before all time, and God had none. Athanasius held that the Son shares the Father's own being." This is "What it was about" item 1, word for word. Traced:
  - N204 35938-35940: churches given "to the professors of Arianism". The label is credited to Athanasius, as the item's Contested note requires.
  - N203 6043-6046, Arius to Eusebius: "subsisted before time, and before ages ... the Son has a beginning, but that God is without beginning".
  - N204 19675-19679, the creed: "from the essence of the Father ... One in essence with the Father".
- Added: "The emperor's side had charged Athanasius, among other things, with once turning the emperor's brother against him, and writing to a rebel emperor. He denied it all." This is item 2, word for word. Traced:
  - N204 34917-34924, the first charge, "setting Constans against Constantius".
  - N204 35099-35104, the second charge, letters "to the tyrant" (Magnentius, per N204 5748-5752).
  - N204 35396-35405 and 35618-35624, the two lesser charges, covered by "among other things".
  - The Apology as a whole is his denial.
- The one quote in a changed sentence ("So send Frumentius the bishop to Egypt with all speed.") was re-checked verbatim against PG25 92806-92807 and N204 36144-36145. It holds.

No changed sentence adds a claim beyond the outline. None breaks a Do not say line: Frumentius is not said to refuse, no Theophilus appears, the letter is "about 356", and the label "Arians" is Athanasius's.

## Scores

- **Voice 4.** An adult narrator's register throughout, with the record's own imagery kept. The two inserted explanation sentences are a little denser and more lecture-like than the rest, but they stay plain and credited.
- **Craft 4.** Strong hook into the essence, the life told once and in order, the connection carried through the letter's own words, an ending on the person. Paragraph 11 is now heavy, with seven sentences and three things to hold. It still lands.
- **Rigor 5.** Every sentence traces to the outline and the held texts, the quotes are verbatim, the sole witness is said once in his own voice, the hostile view is told openly and credited, the enemy's charge is given in its content, and the disputed label and date are credited, not settled.
- **Accessibility 4.** Grade 7.9, reading ease 79.8, longest sentence 30. "The Son" and "the Father's own being" are the hardest words, and they are the precise ones. The one stumble is the "him" in MINOR 1.

## Verdict: PASS

## Findings

1. **MINOR.** Paragraph 11. Heard once, "against him" can attach to Athanasius, the nearest name, and not to the emperor. Exact change: "with once turning the emperor's brother against him, and writing to a rebel emperor." → "with once turning the emperor's brother against Constantius, and writing to a rebel emperor." This changes no word count and no source. Its wording is the reader's, so the kit asks for a targeted check if it is applied.

No BLOCKING findings. No Do not say line is needed.
