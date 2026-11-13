# R2 recheck: nine Who profiles, era 2 batch 3

Scope: only what changed, checked against `R1_review.md` and `R1_changes.md`, using `git diff 4ce54a14 HEAD` (the commit that added `R1_review.md`; one fix commit, f9a7d6e6, since). Unchanged text was not re-reviewed. Every new or changed quotation and every new factual claim brought in by the changes was searched again in its vendored file with `wsfind.py` (whitespace-tolerant, tags stripped, quote marks straightened) and read in context, with the nearby translator's and editor's notes. The trims made for length were checked one by one, to make sure each still says only what its source says. No drafts were edited. No model calls and no paid calls were made.

Mechanical checks, all nine:
- `records.json` parses. All confidence tags use the five-level vocabulary.
- Each audio script matches its brief word for word once `[calmly]` and `[warmly]` are removed. `[calmly]` opens each one. Each has one `[warmly]`, right before the closing sentence. No tags appear in the briefs or cards.
- `grade_text` passes for all nine. The highest FK is Ammianus at 8.4. The lowest Flesch is Ammianus at 60.2 and Didymus at 60.5, just above the floor.
- Each card's `briefLength` fits its brief.
- No narrator sentence in a brief runs past 25 words. The long sentences are quotation-led: Didymus's close (28), Fabiola's close (28), Olympias's answer (27), all as in R1, and the changed Gennadius line in Evagrius (26 words, 9 of them his).
- No new "not X but Y" shape appears in a brief. The one on the Marcella card is gone (M4).

| Profile | Words | Est. length | FK | Flesch | Cap |
|---|---|---|---|---|---|
| Ammianus Marcellinus (outside witness) | 324 | 2:00 | 8.4 | 60.2 | 324, at the cap |
| Martin of Tours (major) | 405 | 2:30 | 6.9 | 69.0 | 405, at the cap |
| Didymus the Blind | 322 | 1:59 | 7.9 | 60.5 | 324, within |
| Evagrius Ponticus (major) | 405 | 2:30 | 7.8 | 63.9 | 405, at the cap |
| Fabiola of Rome | 324 | 2:00 | 6.0 | 75.4 | 324, at the cap |
| Epiphanius of Salamis (major) | 405 | 2:30 | 7.7 | 63.4 | 405, at the cap |
| Olympias of Constantinople | 323 | 2:00 | 7.5 | 62.4 | 324, within |
| Melania the Elder | 323 | 2:00 | 6.8 | 68.2 | 324, within |
| Marcella of Rome | 324 | 2:00 | 6.6 | 68.1 | 324, at the cap |

Length assumes 162 words a minute.

## 1. The R1 blocking finding

| Finding | Status | Note |
|---|---|---|
| Evagrius B1 ("Didymus the Blind" added to Evagrius Scholasticus's report, and the Inferential-Thin identification told as his statement) | RESOLVED | The sentence is gone from the brief. The card keeps his report as "Origen, Didymus and Evagrius" (Walford l.9724) with the caveat "He does not say which Evagrius. That it is this one is a reading of the passage, not his statement." records.json splits the claim: the suppression on Clarke's note 255 alone ("having been suppressed for their Origenistic tendency", Clarke l.1149), and "Justinian condemned this Evagrius" as its own claim, Inferential-Thin, matching `absent_details`. The new tag on the suppression claim is a small new fault (N3). |

**Resolved.**

## 2. R1 minor findings

**Ammianus Marcellinus**
- M1: fixed. "He says Julian gave the Christian sects freedom, expecting it to deepen their quarrels. For Julian had found that 'no wild beasts...'" Ammianus: Julian wished that "each without any hindrance might fearlessly follow the religion he preferred ... because, as long licence increased their dissensions, he thought he should never have to fear the unanimity of the common people, having found by experience that no wild beasts..." (Yonge l.15127). "For Julian had found that" is a fair short form of "having found by experience". records.json claim 5 matches.
- M2: fixed. "Julian's law on teachers of rhetoric and grammar" matches "his forbidding masters of rhetoric and grammar to instruct Christians" (l.15972). records.json claim 6 uses the held words.
- M3: fixed. "Ammianus believes he never 'knowingly perverted' the truth" keeps "as I believe" (l.32333).
- M4: fixed. "The age's belief in omens had some hold on him" fits "did not entirely escape the contagion" and "evidently exercised no small influence over his mind" (l.809).
- M5: fixed. Card knownFor: "outside the church by the general belief that Yonge reports" (l.750–752). The claim is now Dominant Modern Reconstruction, with the note "Yonge reports a general belief, not a certainty". The brief's new line, "Yonge says even his religion is uncertain, though the general belief is that he kept the old Roman faith", is exact to the preface.
- M6: partly. Ramsay's dictionary is named on the card ("in Smith's Dictionary of Greek and Roman Biography", exact, l.774), and the brief keeps "Professor Ramsay, whom Yonge also quotes" for length; that decline holds at 324 words. Jackson now has "notes to Theodoret". E. A. Abbott still has no context in the brief (Jackson's note calls him "Dr. E. A. Abbott" and cites his Philomythus, npnf203 l.12380). See N1, which the same trim made worse.
- M7: fixed. "Theodoret of Cyrrhus" on the card.

**Martin of Tours**
- M1: fixed. "Martin pressed Ithacius to drop the charge" matches "did not cease to importune Ithacius, that he should give up his accusations" (Chronicle II.50, npnf211 l.11653).
- M2: fixed. "Back in Italy he lived as a monk at Milan until Auxentius, the Arian bishop, drove him out." The Life: "again betaking himself to Italy ... he established a monastery for himself at Milan. There, too, Auxentius, the originator and leader of the Arians, bitterly persecuted him; and ... violently expelled him from the city" (l.946–951). The Life does not call Auxentius bishop, but Sulpicius's own Chronicle does: Dionysius, "priest of Milan", was banished, "while Auxentius was immediately chosen as bishop in his place" (II.39, l.11114, l.11132). "The Arian bishop" stands.
- The trims: "His hardest test came at Trier" (no witness for "hardest") is gone, which is right. "He had only his cloak left to give" matches "He had nothing except the cloak in which he was clad" (l.777). "The Life by his disciple Sulpicius, who visited and questioned him" and "in his eighty-first year" (Gregory) say no more than before.

**Didymus the Blind**
- M1: fixed. "Each listing different animals": Jerome's ants, flies and gnats; Socrates's gnats and flies; Sozomen's rats, mice and the lowest animals; Rufinus's mice, flies and lizards.
- M2: fixed. "Has him flourishing from about 309 to 399" fits "Flourished c. 309–399".
- M3: fixed. The card now says the Greek column "did not survive the scan, and his Latin translation is usable", language "Latin (the Greek is unreadable in the scan)". This matches the vendored file's header: zero Greek characters, and a "degraded-but-legible OCR of Mingarelli's 18th-century LATIN translation" (l.48–63). The `title` of that source still reads "(Greek, with Mingarelli's Latin translation)". That names the edition, not what the scan holds, so it is not counted.
- M4: fixed. "Palladius of Helenopolis" in `dates`, "Socrates of Constantinople" in keyWorks, "Theodoret of Cyrrhus" in sources.
- M5: fixed. "A blind scholar of Alexandria named Didymus". The next paragraph's "Didymus, called the Blind, taught in that city" now points back to Alexandria correctly.

**Evagrius Ponticus**
- M1: fixed. "The first to mention the eight, 'or among the first at least to teach these.'" Gennadius: "He was first to mention or among the first at least to teach these" (npnf203 l.42329). The card and records.json match.
- M2: fixed, with a new ordering problem (N2). Palladius: "having put all his belongings into the ship he went to Jerusalem. And there he was received by the blessed Melania" (l.457). Sozomen: "proceeded from Constantinople to Jerusalem" (npnf202 l.39676). Socrates: ordained deacon by Gregory of Nazianzus, "and afterwards went with him into Egypt" (l.13528).
- M3: fixed. "Palladius of Helenopolis" in `dates`, "Socrates of Constantinople" in keyWorks.
- M4: fixed. "Palladius of Helenopolis, who wrote it down in praise of him." The trim "He took ship for Jerusalem" is a fair short form of the line above.
- M5: fixed in structure; see N3 on the tag.

**Fabiola of Rome**
- M1: fixed. "Halting-places", Jerome's word (77.7, npnf206 l.17605).
- M2: fixed. "Jerome writes in his praise". "Remarried" for "married again" changes nothing.

**Epiphanius of Salamis**
- M1: fixed. "In the church of an estate beside his monastery" fits "the church of the villa which adjoins our monastery" (Jerome, Letter 51.1, l.10691).
- M2: fixed. "In the same letter he turned his charges on Origen" has no superlative.
- M3: fixed. "Richardson's note to the Lives of Illustrious Men by Jerome of Strido" in `dates`, and "Palladius of Helenopolis" in the uncertain line. The trims ("say" for "both say", "judged" to "judged") change nothing.

**Olympias of Constantinople**
- M1: fixed. "Names bishops she provided for, Nectarius and Epiphanius of Salamis among them." The Dialogue names Nectarius and "Epiphanius Bishop of Cyprus" among those she gave "lands and money" (Moore l.9583–9588).

**Melania the Elder**
- M1: fixed. "Rufinus, her companion and by then Jerome's opponent".
- M2: fixed. "The name of Thecla, an early woman saint" is a plain reading aid of the kind R1 asked for. It adds no claim about her.
- M3: fixed. "Palladius of Helenopolis says she was widowed at twenty-two and sailed first to Alexandria." Palladius: "Having become a widow at twenty-two ... she sailed with all speed to Alexandria" (46.1, l.499). "First" marks the difference from Jerome's "took ship for Jerusalem" without overstating it.
- M4: fixed. "The letters of Jerome of Strido" in otherNames, "Palladius of Helenopolis" in `dates`, "Rufinus of Aquileia" in the Fremantle line.
- M5: fixed. Turner and Butler are given the continuation, and "Clarke takes Palladius's 'we' as Palladius and Melania" gives note 324 to Clarke.
- The trims, each checked:
  - "Before he was buried, two of her sons died": Jerome, "while the dead body of her husband was still unburied, still warm, had the misfortune to lose at one stroke two of her sons" (Letter 39.5, npnf206 l.8094). Holds.
  - "Jerome of Strido tells it to Paula of Rome": the words "in a letter" were dropped. It is still true, since Letter 39 is to Paula.
  - "He apologised and released her": Palladius, the judge "both made an apology and honoured her, and gave orders that she should succour the saints without hindrance" (46.4). "Released" is not his word, but she was in prison and is then free to serve the saints, so the release follows from what he says. It holds. "Let her go on" was a little closer to "without hindrance", but nothing in the new wording is wrong.
  - "Jerome cut her from every copy of the Chronicle, for disapproving of some of his deeds": Rufinus, "when he found that some of his deeds were disapproved by this lady ... he erased her name from all the copies of his work" (Apology II.26, npnf203 l.49974). Holds.
  - "A pun on her name, meaning black" matches the note "The name means 'black.'"

**Marcella of Rome**
- M1: fixed. "A few days after the soldiers came, she died in Principia's arms."
- M2: fixed. "Tells this in a memorial letter, written in her praise to her friend Principia."
- M3: fixed. "By the account of Jerome of Strido" in knownFor. "Of Strido" is dropped from the later legacy line, which is right.
- M4: fixed. "The notes in W. H. Fremantle's English edition name the translator of Origen's book as Rufinus of Aquileia. Jerome's letter does not name him."
- The trims, each checked: "Pachomius's monasteries in Egypt" fits "the monasteries in the Thebaid founded by Pachomius" (127.5, l.26086). "In the 380s Jerome lived in Rome", "several on Hebrew words", "Paul had written", "He and Jerome later wrote against each other" and "An old nobleman, Cerealis," say no more than before.

## 3. New or changed quotations, checked word for word

All exact:
- Ammianus: "no wild beasts are so hostile to men as Christian sects in general are to one another." (l.15127). "a cruel action, and one deserving to be buried in everlasting silence." (l.15972). "knowingly perverted" (l.32333). Card: "did not entirely escape the contagion" (l.809). Ramsay "in Smith's Dictionary of Greek and Roman Biography" (l.774; OCR "Dictionar3r").
- Evagrius: "or among the first at least to teach these." (npnf203 l.42329), in the brief and the card.
- Fabiola: "She was the first person to found a hospital," / "into which she might gather sufferers out of the streets." Unchanged words, with the new frame "in his praise".
- Marcella card: "giving vent to my own rancour." Unchanged.
- Martin, Didymus, Epiphanius, Olympias, Melania: no new quotations. The quotations next to changed text were re-read and are unchanged.

## 4. New faults in changed text

### New blocking

None.

### New minor

- **N1 (Ammianus, brief, first mentions).** The trim cut "Edward Gibbon" to "Gibbon, whom Yonge quotes". The new Abbott line brings in "Theodoret" with no identifier. "E. A. Abbott" is still given no context (M6). The card has "Edward Gibbon" and "Theodoret of Cyrrhus". Fix: "Edward Gibbon, the historian of Rome, whom Yonge quotes" and "E. A. Abbott, a scholar quoted in Blomfield Jackson's notes to Theodoret of Cyrrhus". The brief is at 324 words, so the drafter will need to cut a few words elsewhere. "Professor Ramsay, whom Yonge also quotes" could become "Ramsay, also quoted by Yonge".
- **N2 (Evagrius, brief, paragraph 3).** "Palladius and Sozomen take him to Jerusalem, where Melania the Elder took him in. Socrates of Constantinople has him go into Egypt with Gregory. He wavered and fell ill for six months. When Melania asked..." There are two problems. First, the "where" clause gives Melania to Sozomen too, and Sozomen does not mention her (npnf202 l.39676). Melania is Palladius's alone. Second, Socrates's other route now sits between Melania taking him in and her nursing him. A listener can hear "He wavered" as part of Socrates's Egypt account. Fix: "Palladius and Sozomen take him to Jerusalem. Socrates of Constantinople has him go into Egypt with Gregory. In Jerusalem, Palladius says, Melania the Elder took him in. He wavered..." This adds about three words to a brief at the cap, so the drafter will need a small trim elsewhere.
- **N3 (Evagrius, records.json).** The split suppression claim, "His works were later suppressed for their Origenist tendency", went from Widely Accepted to Documented. Its only witness is a 1918 editor's note (Clarke, note 255), not a source from the time. In this batch, a modern editor's statement is tagged Widely Accepted or Dominant Modern Reconstruction with the writer named. Documented is used for a direct report in a source. Put it back to Widely Accepted, with the witness as Clarke's note.
- **N4 (cards, sentence length; report, as era 2 batch 1 N8).** Several new or changed card sentences run past 25 words, mostly because identifiers were added: Ammianus knownFor (43) and the Ramsay line (36), Epiphanius `dates` (26) and the Theophilus line (32), Evagrius keyWorks `about` (27) and the Gennadius trace (31), Marcella knownFor (36) and the memorial line (26). The briefs are clean.

Report only, unchanged text: the Epiphanius card's `briefLength` reads "about 2 and a half minutes", where Evagrius and Martin read "about 2 minutes 30 seconds". Use one form when the profiles are placed.

## Summary

| Profile | R1 blocking | Resolved | New blocking | New minor | R1 minors partly or not fixed |
|---|---|---|---|---|---|
| Ammianus Marcellinus | 0 | – | 0 | 1 (N1) | M6 partly |
| Martin of Tours | 0 | – | 0 | 0 | none |
| Didymus the Blind | 0 | – | 0 | 0 | none |
| Evagrius Ponticus | 1 | 1 | 0 | 2 (N2, N3) | none |
| Fabiola of Rome | 0 | – | 0 | 0 | none |
| Epiphanius of Salamis | 0 | – | 0 | 0 | none |
| Olympias of Constantinople | 0 | – | 0 | 0 | none |
| Melania the Elder | 0 | – | 0 | 0 | none |
| Marcella of Rome | 0 | – | 0 | 0 | none |
| **Total** | **1** | **1** | **0** | **3 + N4 across cards** | **1 partly (Ammianus M6)** |

The one R1 blocking finding is resolved. Of the 34 R1 minors, 33 are fixed and one is partly fixed (Ammianus M6: E. A. Abbott still has no context; the Ramsay decline holds). No new blocking findings came in with the changes. Every trim flagged for checking still says only what its source says: Martin at Milan, Melania's sons, her release, the erasure, Thecla, Ammianus's "For Julian had found that", and Evagrius's Jerusalem route. No witness swaps, roles for witnesses, dropped hedges or unsourced superlatives were found in the changed text. The one superlative R1 did not flag, Martin's "hardest test", is now gone.

Martin, Didymus, Fabiola, Epiphanius, Olympias, Melania and Marcella are clear. Ammianus and Evagrius have only minors (N1; N2, N3). None of these is blocking. Under the review cap they can be fixed without another full round: three short line changes and one tag.
