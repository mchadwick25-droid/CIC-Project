# Review: John Chrysostom (`john-chrysostom.brief.txt`)

Reviewed 2026-11-23 under the change order of 2026-11-19: approved wording is kept wherever it passes; a fix touches only what fails.

## The test, from one hearing

1. **Who:** John, a preacher from Antioch, who was bishop of Constantinople, the eastern capital.
2. **What happened:** He preached hard at the powerful. One example is his sermon over the fallen eunuch Eutropius. He moved the bishop's money to hospitals. His rebukes turned the court and Theophilus of Alexandria against him. Two councils deposed and silenced him, and he died on the road into exile.
3. **Why the connection matters:** His deposition split the church at Constantinople. In 438 Bishop Proclus brought his body home and, Socrates says, won his followers back into communion.

None of the three lines is blank or wrong.

**Essence** (from the census entry): John preached at Antioch, then at Constantinople. He spoke plainly about money, cruelty and the poor, and he aimed that plain speech at the court as well. In the end it led to his exile and his death on the road. **Also told:** his Antiochene way of reading Scripture, his care for the poor (the hospitals and the Homily 50 line), the synods against him and his recall, and his restoration in 438.

- **Hook to essence.** The hook is the Eutropius scene. At seven sentences it runs well past "about three", but it is approved wording, and it leads straight into the plain speech aimed at the powerful (by about word 120). The other half of the essence, the poor, arrives only at about word 170–195. It comes in a sentence placed in his Constantinople years, when the sermon was preached at Antioch (see B1). With B1 applied, the poor arrive at about word 163, at Antioch, within about the first minute. Without B1, they arrive late and misplaced.
- **Told once, in order.** The hook reaches ahead to 399. The life then runs from Antioch (Diodore) to 398, the hospitals, the rebukes, the Oak in 403, the recall, 404, 407 and 438. The one break is the Matthew sermon, an Antioch event heard among the Constantinople events (B1). "The sermon over Eutropius made it worse" refers back to the hook without retelling it, so it is not a repeat.
- **Ending.** It ends on John's body brought home and his followers reconciled. This is the connection landing on the person, so it passes.
- **Names heard once that neither act nor link:** none that lose the listener. Diodore is heard once and his act is slight ("trained"). Eudoxia acts in a clash. Eutropius, Theophilus and Proclus act. Socrates and Palladius are links on the tree.
- **Where I got lost:** in the last sentence, "the followers who had left it over John's deposition". The listener has never heard that anyone left (M2).
- **Children's book or talking down:** nowhere.

## Scores

- **Voice 4.** A serious documentary register, vivid in the altar scene and the forced march. Witnesses are credited where trust turns on them.
- **Craft 3.** The hook is long. The Antioch paragraph is a one-sentence stub. The Matthew line sits out of its time and place. The essence is shown but never quite said.
- **Rigor 4.** Every claim traces to a held text, and the one quote is verbatim. One detail is set in the wrong period (B1).
- **Accessibility 4.** Grade 8.7 (names out 7.4), reading ease 72.0, 16.8 words a sentence. The closing sentence runs 35 words.

Score run: `python -m engine.m1.profile_readability …/john-chrysostom.brief.txt` gives 352 words, grade 8.7 (names out 7.4), reading ease (names out) 72.0, 16.8 words a sentence, longest sentence 35 words: pass.

## Verdict: REVISE (one BLOCKING finding, a small move)

## Findings

**B1 — BLOCKING (a misleading implication: a detail moved onto the wrong time and place; it is also the late half of the essence).** In paragraph three, "In a sermon on Matthew, John told his listeners that if they wanted to honor the body of Christ, they must not neglect Him when He is naked." follows Palladius's account of his Constantinople spending. That placement says the sermon was preached at Constantinople. The Homilies on Matthew "were undoubtedly delivered at Antioch" (`cic/texts/npnf110_chrysostom-homilies-matthew.xml` line 535, editor's preface; the line itself is at 29929–29931).
- **Change:** delete that sentence from paragraph three. Insert it into paragraph two, after "…who kept to the literal sense of Scripture.", and open it with "There," and change "John" to "he": "There, in a sermon on Matthew, he told his listeners that if they wanted to honor the body of Christ, they must not neglect Him when He is naked."
- This adds one word. No other wording changes. Paragraph three still reads correctly: "…and built more hospitals. He rebuked men in office too."
- **Do not say (add to the outline):** "Do not place the Homily 50 on Matthew line in his Constantinople years or after his consecration. The Matthew homilies were preached at Antioch (npnf110 line 535). Tell it with his Antioch years."

**M1 — MINOR (card, not the brief).** The card's briefReference reads "Socrates, Church History VI.3, tr. Zenos: John's training under Diodore, who kept to the literal sense of Scripture". This gives Socrates the "literal sense". Socrates says only "under the guidance of Diodorus". The literal sense comes from the translator's note there (`npnf202…xml` about lines 17172–17178) and from Prevost's preface (`npnf110…xml` lines 730–732). The brief states the literal sense in the narrator's voice, which is widely accepted, so the brief needs no change.
- **Change on the card:** "Socrates, Church History VI.3, tr. Zenos: John's training under Diodore; Zenos's note and Prevost's preface (NPNF 1.10): Diodore's literal sense."

**M2 — MINOR (closing sentence: 35 words, past the kit's "about 30", and it brings in new information at the end).** It passes the score and is understandable with effort. Leave it unless the reviser is already re-recording, in which case use the smallest split: "…in procession. By this, Socrates says, he brought back to the church's communion the followers who had left it over John's deposition."

No other findings. These were all re-checked against the held texts:
- **Socrates VI.2** (`npnf202` lines 17097–17110): the court's choice, and Eutropius forcing Theophilus.
- **Socrates VI.3 and VI.5** (lines 17128–17172 and 17319–17384): Antioch, Diodore, the rebukes and the tide against him, the sanctuary law, the man trembling under the altar table, "added insult to cruelty", and Isidore.
- **Socrates VI.15** (lines 18262–18300): the Oak, the refusal and the deposition.
- **Socrates VI.18** (lines 18427–18500): Eudoxia, the second council, "silenced", and the decree of exile.
- **Socrates VII.45** (lines 21450–21476): Proclus, the procession, and the communion restored.
- **Homily I on Eutropius** (`npnf109`, about lines 17698–17722): soften their minds; "like an affectionate mother has concealed him under her cloak".
- **Palladius** (`palladius_dialogue…moore1921.txt`): the hospitals (3745–3776), the soldiers and Pityus (6390–6410), and the death (6434–6499).
- **The quote** "Glory to God for all things" (lines 6498–6499, with a line break after "God"). It is verbatim by two methods: a whitespace-normalized search and a reading by eye.

**Quote overlap.** There is none with this batch's drafts or with the live Epiphanius of Salamis story.
