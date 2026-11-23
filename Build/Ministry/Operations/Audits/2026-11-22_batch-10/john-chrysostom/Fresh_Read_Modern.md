# John Chrysostom: fresh read, modern pass

Read: `john-chrysostom.brief.txt` against the kit as it now stands (Part 1, "Nothing in the story rests on a modern opinion, guess or reconstruction, credited or not", Mark, 2026-11-23), `Outline.md` and the texts in `cic/texts/`. I opened none of the files this step bars.

## The four lines

- **Who:** John, a preacher from Antioch who became bishop of Constantinople.
- **What happened:** he preached against the rich and powerful, crossed a fallen minister, a general, the bishop of Alexandria and the empress. Two councils removed him, and soldiers marched him toward the Black Sea until he died on the way in 407.
- **What it was about:** honoring Christ in the poor rather than in display, and a bishop's blunt freedom of speech against men and women in power.
- **Why the connection matters:** his followers broke from the church over his deposition. In 438 Proclus brought his body home and, Socrates says, brought them back by it.

All four come from one hearing. Every named charge, teaching, quarrel and decision is explained: the sanctuary law, the sermon over Eutropius, the Matthew sermon, the hospital spending, Gainas and the Arians, the grudge, the monks' quarrel, the Oak's charges and the deposition for refusing, the statue and the games, the second council's ground, and the reconciliation.

**Essence and order.** The essence ("He preached plainly about the poor, and his blunt words to the powerful led to his exile") opens paragraph 2, at about word 106, inside the first minute. The Eutropius hook (399) reaches ahead. After the essence the life runs once, in order: Antioch, 398, the rebukes and Theophilus, the Oak, Eudoxia and the second council, 404, the death in 407, 438. Nothing is told twice. The last line is a later bishop, but it is the connection, and it closes on John's body coming home. Names: John, Eutropius, Socrates, Diodore, Theophilus, Palladius, Gainas, Eudoxia, Proclus; each acts, is a credited witness or is a link. Nowhere did I get lost, and nothing talks down.

**Length:** 445 words by `python -m engine.m1.profile_readability`, grade 8.2 (names out 7.2), reading ease names out 71.4, longest sentence 29: pass, under 450.

## Scores

- **Voice 4.** A grown narrator's register throughout. The hook is a real scene, and John's mother-and-cloak image carries it. A few later sentences are bare reports ("Socrates says ...") strung one after another.
- **Craft 4.** A strong hook leads straight to the essence, and the life runs in order. Paragraph 4 is dense: four witnesses' claims stack up in five sentences.
- **Rigor 3.** One sentence rests on a modern identification of a witness (BLOCKING 1). Every other date, place and charge traces to an old source at its lines. Every credit is in place.
- **Accessibility 4.** Plain words, glosses worked into the sentence (the Arians, the monks' quarrel), and scores well inside the limits.

## Verdict: REVISE

One BLOCKING finding. The change is three words and keeps the brief at about 447 words.

## Findings

### BLOCKING 1. "Palladius, who stood by John to the end" rests on a modern identification

- **Sentence:** paragraph 3, "Palladius, who stood by John to the end, says he moved the bishop's extravagant spending to the hospital."
- **Why it rests on a modern source:** the Dialogue is anonymous as it stands. Its heading names Palladius of Helenopolis as the bishop who speaks in it, not as its author. That Palladius of Helenopolis, John's companion who suffered for him, also wrote it is the translator's and Butler's reconstruction. Moore, introduction: "The treatise as it stands is anonymous, but it is generally attributed to Palladius, Bishop of Helenopolis" (`palladius_dialogue-life-of-chrysostom_moore1921.txt` 728-730), and "There is nothing except the title to suggest that the interlocutor is Palladius" (755-756). He also weighs the theory that another Palladius wrote it (895-903). The old sources do hold two separate things. One is a bishop Palladius who wrote John's life as a dialogue: Photius, Codex XCVI, "bishop Palladius, who has written an admirable and careful life of Chrysostom in the form of a dialogue" (`photius_library-v1_freese1920.txt` 9983-9985). The other is a Palladius of Helenopolis who was on John's side: the Oak's minutes (Photius 3947-3948, 3977-3978) and the Dialogue itself, where he flees to Rome (Palladius 2631-2633). "Stood by John to the end" joins the writer to the companion, so it rests on the modern identification. "To the end" also claims a loyalty up to John's death, and no held old line gives that.
- **Change:** "Palladius, who stood by John to the end, says" → "Palladius, who wrote John's life and took his side, says".
- **Traced:** "wrote John's life": Photius, Codex XCVI (`photius_library-v1_freese1920.txt` 9983-9985). "Took his side": the Dialogue's own voice, "that he would spare the saint" and "the head of the blessed bishop" (Palladius 6411, 6418), and "the blessed bishop" (4822). This keeps the partisan credit the kit asks for in praise and the outline asks for in item 5 ("Credited to Palladius, his partisan"). The second credit, "Palladius says soldiers hurried him toward Pityus", needs no change.
- **Do not say line for the outline:** "Do not call Palladius John's companion, or say he stood by John to the end. The Dialogue is anonymous; its author's identity with Palladius of Helenopolis is the translator's view (Moore, introduction, 728-756, 895-903). Say he wrote John's life and took his side (Photius, 9983-9985; Palladius 6411, 6418)."

### MINOR 1. "A second council silenced him": the silencing was the emperor's act

- Socrates VI.18: the bishops "immediately condemned him". Then the emperor "sent to tell John that he could not go to the church, because two Synods had condemned him. Accordingly Chrysostom was silenced" (`npnf202` 18480-18489). The outline's plain sense is "it condemned him" (item 15). As written, the emperor's act moves onto the council: a small case of one of the four faults.
- **Change:** "A second council silenced him for taking back his see" → "A second council condemned him for taking back his see". It is the same length, and it traces to Socrates VI.18, 18468-18473 and 18480-18481.

### MINOR 2. "There," placing the Matthew sermon at Antioch, leans on the editor's step from one homily to the whole course

- John's own words in Homily VII, "our city first crowned itself with the name of Christian" (`npnf110` 5302-5303), place that homily at Antioch. Homily 50 names no city. Applying Homily VII's place to Homily 50 is the Oxford editor's move: "undoubtedly delivered at Antioch (see Hom. vii. p. 43)" (`npnf110` 534-536). The Modern pass (place 4) judged that this holds, and the series does run as one course. I do not block it. The story loses nothing without the word, though, and dropping it takes the place off any modern step.
- **Change:** "There, in a sermon on Matthew, he told his listeners" → "In a sermon on Matthew, he told his listeners". It is one word shorter and traces to `npnf110` 29929-29931 for the sermon's words.

## Source check: the rest, held

- **P1.** "In 399": Eutropius fell while consul, and his name was struck from that year's list (Socrates VI.5, `npnf202` 17361-17366; Homily I, "thy consulship", `npnf109` 17589). The AD figure is only the conversion. "Chief eunuch", the law and its quick reversal: 17324-17334, 17345-17348. "Trembling ... under the altar", "the pulpit" and "added insult to cruelty": 17351-17362. John's reason and the image "like an affectionate mother has concealed him under her cloak": `npnf109` 17699-17706, 17722-17724. "Socrates of Constantinople": Socrates V.24, "Constantinople, where I was born and educated" (`npnf202` 16777).
- **P2.** Diodore, "the literal sense of scripture": VI.3, 17166-17183. "At Antioch": native of Antioch, reader there (17130, 17211-17212). The Matthew line: `npnf110` 29929-29931.
- **P3.** 398 and "Eutropius made Theophilus ... ordain him": VI.2, 17097-17113. The hospital: Palladius 3745-3751.
- **P4.** The tide, Gainas ("It is said"), the grudge over Isidore: VI.5, 17316-17320, 17367-17381. The Arians: I.5, 2093-2096. The monks' quarrel: VI.7, 17578-17586, 17655-17693. The false report: VI.9, 17830-17840.
- **P5.** The Oak near Chalcedon, the citation, the refusal, deposition only for refusing: VI.15, 18278-18297. The charges: the minutes in Photius, Codex LIX (3868-3876, 3927-3933). The rising and the recall: VI.15-16, 18297-18323.
- **P6.** The statue, the games and Eudoxia: VI.18, 18427-18440. The second council's ground: 18468-18473. The exile in 404: 18496-18502. Palladius, the soldiers and Pityus: 6397-6413. Death near Comana with "Glory to God for all things": Palladius 6440-6498. Socrates VI.21 dates the death: 14 September, the seventh consulate of Honorius (`npnf202` 18609-18612).
- **P7.** Proclus, the body and the reconciliation: VII.45, 21455-21471.
- **Not in the story, rightly:** the Oak's year, "Antiochene", Origen, Isidore by name, the Herodias sermon, and the fire. Every Do not say line is honored.

## Step 2: the diff against `john-chrysostom.brief.v4.txt`

Three sentences changed, and each matches the outline's **Modern pass**:

1. **Paragraph 2, ", in the Antiochene way" cut** (Modern pass 1). The label is the editors': Zenos's note, "the Antiochian system of interpretation" (`npnf202` 17171-17179), and Prevost, "the so-called Antiochian school" (`npnf110` 730-732). The words that stay are in Socrates VI.3, Diodore "limited his attention to the literal sense of scripture, avoiding that which was mystical" (`npnf202` 17181-17183), and in Sozomen VIII.2, "avoided allegory" (42696-42697). Nothing added. Nothing the story needs is lost: the teaching is still explained in plain words.
2. **Paragraph 5, "In 403" cut** (Modern pass 2). Socrates VI.15 gives the Oak no year (18255-18300, checked), and neither do the minutes in Photius. The order (Oak, recall, then 404) still carries the time. Nothing added and nothing lost.
3. **Paragraph 6, the year moved from the march to the death** (Modern pass 3). Palladius gives the march no year (6392-6432, checked). Socrates VI.21 dates the death to the seventh consulate of Honorius (`npnf202` 18609-18612), and the editor's 407 is the conversion (18611). The new "He died on the way in 407" puts the year on the event it belongs to. Nothing added. The march's force ("hurried him", "hoping he would die") and the last words are kept whole.

The heart, the meaning of every named thing and the record's force all come through the diff unchanged. The Modern pass missed one modern step, BLOCKING 1 above.
