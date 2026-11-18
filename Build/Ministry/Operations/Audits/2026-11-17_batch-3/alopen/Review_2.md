# Alopen — Review, round 2 (fresh draft from the revised outline)

Read: `alopen.brief.txt` (once, straight through), `Outline.md`, `Source_Sheet.md`, `Outline_Check_2.md`, the census entry `alopen`, and the kit's `Standard.md`, `Shapes.md`, `Process.md`. Voice: Neo, about 150 words a minute.

## 1. The test, from one hearing

- **Who:** Alopen, a man from the far west who led the earliest Christian mission to China that the record describes, for the Church of the East.
- **What happened:** In 635 he reached Chang-an, the Tang capital, with his church's books. The emperor Taizong had him received, the books were translated in the imperial library, and in 638 a decree let the faith spread and officials built a monastery for twenty-one priests. The church grew, met opposition, set up a stone telling its story in 781, and faded after the edict of 845. Workmen dug up the stone in 1625, and the Jesuits circulated it.
- **Why the connection matters:** We know Alopen only because his church carved his coming on a stone about 146 years later. When that stone came out of the ground in 1625, it gave back a church the world had forgotten.

No line is blank or wrong.

### The heart of his life (from the census entry and knownFor, written before checking the brief)

Alopen brought the Church of the East's sacred books from the far west to Chang-an in 635: the first Christian mission to China on record. The books were translated in the imperial library, the emperor Taizong studied the teaching and ordered it spread, and his decree of 638 licensed the faith and had a monastery built in the capital for twenty-one priests. Everything known of it comes from the stone his church set up in 781.

### Does the first minute carry it?

Yes. Counting words at about 150 a minute: the finding, the church's name, "the earliest Christian mission to China that the record describes", the arrival in 635, the reception, the translation and the emperor's order to spread it all fall inside the first 140 words. The decree of 638 begins at about word 140, its key line ends at word 167 (about 67 seconds), and the monastery for twenty-one priests lands at word 177. The heart is told, and given its weight, by about 70 seconds. The opening on the 1625 finding leads straight to him in its third sentence, so it draws the listener in without delaying the heart.

### Where I got lost, and register

Nowhere seriously. "Strange writing beside the Chinese" is clear enough heard once. Nothing reads as a children's book or talks down. The register is an adult documentary narrator's throughout.

## 2. Scores

- **Voice: 4.** A steady documentary narrator; the decree is the only quote and it does work the narrator's words could not. The closing line ("So a church the world had forgotten was known again") is a little tidy, close to a summing-up (MINOR 2).
- **Craft: 4.** Strong opening that leads to the heart; time, place and tradition arrive early inside the story; stakes are clear ("a foreign faith now had the emperor's open licence"). The connection is carried through acts: who carved the stone, who found it, what the Jesuits did with it. The after-life includes opposition and the end, as the outline asks. One transition implies an order the record does not hold (MINOR 1).
- **Rigor: 4.** Every sentence traces to the outline, and every Do not say line is honoured: no rank for Alopen, "the far west" not Syria, the books translated in the passive, workmen not Jesuits finding the stone, "the stone says" on the hundred cities, 845 as "sent back to ordinary life", the Jesuits' use of the stone credited to them. The only slip is the order implied in MINOR 1.
- **Accessibility: 5.** Grade 8.2, reading ease 71.5 (names out), 18.2 words a sentence; plain modern words, no puzzle left undefined.

## 3. Source check

Quote re-checked verbatim:
- LEGGE 1252–1254: "(the system) is helpful to (all) creatures, and profitable for men : — let it have free course throughout the empire". The brief's "It helps every creature, and it does people good. Let it spread freely through the empire." is the outline's rendering, word for word. Wylie (MAL 13708–13709) agrees, per Outline_Check_2.

Lines traced (opened in `cic/texts/` where noted):
- Finding in 1625, workmen digging in a suburb, a large stone, mostly Chinese with "others entirely different": LEGGE 3662–3670 (opened). Cross at the top: YULE 2929–2931 (opened). "A thousand years before": YULE 2914–2916, "a thousand years later" (opened); the outline's opening sanctions it.
- "With the favour of the Tang emperors": LEGGE 3674–3676, "sanction and encouragement of the most famous monarchs of the great T'ang dynasty" (opened).
- Arrival 635, minister sent to the western suburb to receive him and bring him to the palace, books translated in the Library, emperor convinced and ordered it spread, decree of 638: LEGGE 1227–1254 (opened).
- Monastery for twenty-one priests: outline beat 4, LEGGE 1256–1257, 1477.
- Monasteries filled "a hundred cities" under the next emperor, as the stone's claim: LEGGE 1633–1643 (opened); MAL 13738–13744 (opened).
- Buddhists spoke out, others mocked; priests held it together: MAL 13744–13751 (opened).
- Stone set up in 781: MAL 14141–14142 (opened); "about 146 years" and "his church looking back, in words that also praise the emperors": outline, Who tells it.
- "After 781, Chinese history keeps only slight traces": LEGGE 4249–4253 (opened).
- Edict of 845, "more than 3,000 persons", Ta Ts'in and Mu-hu-pi, "resume the ways of ordinary life": LEGGE 4346–4350 (opened).
- "Lay in the ground until 1625": outline Do not say form, held.
- Chinese Christian official sent a copy to the Jesuits, who circulated copies through the empire as proof of the early introduction of Christianity: LEGGE 3685–3712 (opened).

No unsupported claim and no factual error.

## 4. The score

`python -m engine.m1.profile_readability .../alopen.brief.txt`: 328 words, grade 8.2 (names out 7.8), reading ease names out 71.5, 18.2 words a sentence, 11% short sentences, longest sentence 31 words — **pass**.

Length: 334 words by `wc` (328 by the tool), about 2 minutes 13 seconds in Neo's voice, against the outline's "about 300". Within tolerance; not a finding.

## Verdict: PASS

No blocking finding. Two minor findings, neither required for acceptance.

## Findings

### BLOCKING

None.

### MINOR

**M1. "His church outlived him, and under the next emperor…" implies he was dead before the growth under Gaozong.** The stone has Gaozong (650–683) raising Alopen to a high title in the same passage as the monasteries (LEGGE 1633–1638; MAL 13738–13742), so he was alive in that reign as far as the record shows. Heard once, the sentence order suggests the expansion came after his death. *Change:* "Under the next emperor, the stone says, its monasteries filled a hundred cities, and Alopen was given a high title. His church outlived him." Or simply drop "His church outlived him, and" and begin "Under the next emperor…". The outline already holds both facts (beat 5; Connection).

**M2. The closing line leans toward a summing-up.** "So a church the world had forgotten was known again" states the connection after the acts have already carried it. The Standard allows ending on the connection once it has landed, so this is not a fault, but the story would end as strongly on the Jesuits circulating the stone. *Change (optional):* end on "…as proof that Christianity had come to China early", or keep the line if the listening review prefers it.
