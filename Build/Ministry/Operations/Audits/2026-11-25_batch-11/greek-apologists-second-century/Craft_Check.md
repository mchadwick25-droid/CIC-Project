# Craft check: The Second-Century Greek Apologists

Kit Part 3, step 5: the one craft pass after the fresh read, checked. Read: `Fresh_Read.md`, `Fresh_Trust.md`, `Fresh_Trust_Second.md`, `Fresh_Listen.md`, the live `greek-apologists-second-century.brief.txt`, `Outline.md`, `Source_Sheet.md`, and the cited source lines. No `.v1`/`.v2`/`.v3` file opened.

**Verdict: FIX.** Two brief changes (below), and the Marcion cut stands with the outline changes given.

## Each change

1. **Tertullian** ("Writing against teachers he held false, he said he followed earlier Christian writers, and named Justin first."). Says no more than anf03 43150–43163 (*Against the Valentinians* 5: not "of our own mind fashioned our own materials, since these have been already produced … in respect of the opinions and their refutations … for instance Justin"). "Teachers he held false" glosses the heresy without naming the Valentinians, as Cut first 8 requires. Fixes the BLOCKING finding in both trust reads. Reads on one hearing after "took up the same task in Latin". Holds.
2. **"root and branch"**, with "with their wives and children" cut. The cut was Cut first 20, which the outline allows "only if a draft still runs past 675". With the Marcion sentence out the brief runs 659, so the condition no longer holds. `Fresh_Listen.md` also notes the clause carries the idiom's sense for a second-language listener. **FIX A: restore it** (below).
3. **Do not say line** in `Outline.md`: word for word from `Fresh_Trust_Second.md`. Holds.
4. **Sentence 10 left unchanged.** Right: "the cities' gods" is the outline's own wording, and `Fresh_Trust_Second.md` rules it a fair gloss (1apol-grc 678, 683–686). Holds.
5. **Marcion cut.** Ruled below: the cut stands.
6. **Eusebius folded into Melito** ("In the passages of his petition that Eusebius copied, he wrote that the godly in Asia were driven about by new decrees, new written orders."). npnf201 25818–25822 holds it ("in his book addressed to the emperor … being driven about in Asia by new decrees"). It no longer says only a sentence about what is missing, which fixes `Fresh_Listen.md`'s BLOCKING tell. It does not claim the petition survives, so it keeps the Do not say limit. Reads on one hearing. Holds.
7. **"a church historian"**. Places Eusebius and adds no claim. But it pushes the Quadratus sentence to 36 words, with 15 of them set between "because" and its reason. That breaks the kit's limit of about 25 words with nothing nested, at the very sentence `Fresh_Listen.md` names as where attention first drifts. **FIX B: split it** (below). The scorer marks "a church historian" as a modern-scholar word. That is a false match: Eusebius is the old witness.
8. **"hunted for the name Christian alone"**. athen-grc 104–108, "ἐπὶ μόνῳ ὀνόματι", puts "alone" on the name, so the change says no more than its source. It fixes the second-language MINOR. "Only Christians … Christian alone" is heavy, but it is understood on one hearing. Holds.
9. **"such a death" left unchanged.** No read gave a change for it. Holds.

## Brief changes

**FIX A.** Old: "If the charges were true, Athenagoras said, let the emperors destroy the Christians root and branch."
New: "If the charges were true, Athenagoras said, let the emperors destroy the Christians root and branch, with their wives and children."
(athen-grc 180–182, "σὺν γυναιξὶ καὶ παισὶ προῤῥίζους"; +5 words.)

**FIX B.** Old: "In the reign of Hadrian, Quadratus addressed a defense to the emperor because, says Eusebius, a church historian who still had the book in the early 300s, certain wicked men were trying to trouble the Christians."
New: "In the reign of Hadrian, Quadratus addressed a defense to the emperor. Eusebius, a church historian who still had the book in the early 300s, says Quadratus wrote because certain wicked men were trying to trouble the Christians."
(npnf201 21045–21050; +2 words; the new sentences run 12 and 26 words.)

## The Marcion sentence: ruling (b), the cut stands

The outline gives Justin's reason at beat 2 (1apol-grc 706–709): the demons put forward men "who were not only not persecuted by you, but even thought worthy of honours". Marcion is named as one of them (729–743). The reason cannot be told without the demons. That needs a gloss, plus "another god above the Creator" made plain, which the listener could not follow. The old sentence ran 22 words, and the reason with its gloss needs at least 10 more. After FIX A and FIX B only 9 words are free, and the outline also bars telling the "hunted for the name" contrast again. Any sentence that fits would still be bare. So the cut stands, and the Marcionism card carries Justin against Marcion.

Outline changes (exact):
- **Never cut.** Old: "Justin on atheists, his taxes and loyalty, Marcion, his death as a clause;" New: "Justin on atheists, his taxes and loyalty, his death as a clause;"
- **Cut first**, add after item 20: "21. Justin naming Marcion (beat 2, 1apol-grc 729–743): his reason for naming him (1apol-grc 706–709) needs the demons, a gloss and more words than the 675 ceiling leaves, and without it the sentence is bare (`Fresh_Listen.md`), about 22 words: **for the card** (the Marcionism card carries Justin against Marcion)."
- **Sibling.** Old: "**Marcionism** (this batch; no outline yet): Justin against Marcion, one clause." New: "**Marcionism** (this batch; no outline yet): Justin against Marcion, card only (Cut first 21)."
- **Names.** Old: "Marcion: link (`marcion-marcionism`)." New: "Marcion: card only (Cut first 21); the link stays under Links."

For Mark: the slate's Siblings line gave Justin against Marcion "a clause". With this ruling it goes to the card instead (`Fresh_Read.md`, To Mark).

## Count and scorer

- Live brief: 659 by `wc -w`. `engine.m1.profile_readability`: grade 8.6 (names out 7.9), reading ease names out 71.3, 18.3 words a sentence, longest 36, pass.
- With FIX A and FIX B (scratch copy): 666 by `wc -w`, inside 675. Grade 8.5 (names out 7.7), reading ease names out 71.6, 18.0 words a sentence, 5% short sentences, longest 31, pass. `check_brief_craft.py` lists 5 items, all judged by Part 1:
  - the Eusebius sentence twice: a credited old witness, and "historian" is a false match;
  - Justin's death: the reason is given;
  - "Athenagoras said": he is a speaker in the story;
  - Theophilus: the friend's charge explains it.
