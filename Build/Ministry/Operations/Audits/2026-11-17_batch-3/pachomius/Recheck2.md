# Pachomius: second recheck

Reviewer, 2026-11-18. This is the one recheck of a story rewritten by a fresh writer (Decision Log, "Batch 3: the three held pieces get a second revision, on Opus", 2026-11-18). It was reviewed as new prose under `roles/reviewer.md`, against `Standard.md`, `Shapes.md`, `Process.md`, `Outline.md` and `Source_Sheet.md`. No `*.brief.v*.txt` draft or census text was read. `Review.md` and `Recheck.md` were read only after this review was done.

## Verdict: FAIL

One new BLOCKING finding (N1): the last sentence makes Pachomius's rule the sole ground of Benedict's Rule, set under every chapter. The fix takes one sentence and costs about eight words. Every earlier BLOCKING finding is resolved.

## The three lines, from one hearing

- **Who:** Pachomius, born to pagan parents in Upper Egypt and conscripted for Constantine's war. He became a Christian and, in the early fourth century, gathered monks into a shared life under one rule at Tabennisi on the Nile.
- **What happened:** Christians fed him in prison and he vowed to serve people. He was baptized, trained under the hermit Palamon, and built a community at Tabennisi with the same clothes and food for all. He hid from ordination, housed his sister and the women who joined her, survived a sword attack at Esneh, and died of plague in 346 or 348, sending back a better blanket. His fellowship split after him.
- **Why the connection matters:** Latin-speaking monks could not read his rule, so Jerome dictated a Latin version from books sent to him. Through that Latin the rule went west, where Benedict of Aniane set it under Benedict's Rule. As told, the listener hears it as the ground Benedict's Rule stood on (see N1).

All three lines can be given. Nothing reads as a children's book or talks down. Where I got lost:
- "the abbot Benedict of Aniane set it beneath each chapter of Benedict's Rule": two Benedicts in one breath, and no time cue for the second step, so the listener cannot tell how far the rule travelled in time.
- The Esneh sentence runs to 32 words. Its stake (he was being questioned over claims that he read hidden thoughts) arrives as "about reading hidden thoughts" and is easy to miss.
- "Cassian drew on 'the monks of Tabenna'": Cassian is not placed, and on one hearing he seems to draw on people rather than on their rule.

## Score

`python -m engine.m1.profile_readability`: 472 words, grade 7.9 (names out 6.8), reading ease names out 77.7, 17.5 words a sentence, 0% short sentences, longest sentence 32 words. Pass, with the under-8 note. Listener read: not flat. The prison, the "new plants" work, the hiding, the sister at the door and the blanket keep the world's own detail.

- **Voice 4.** Adult documentary narrator throughout. Witnesses are named where they matter: Coptic Life, Greek Life, Palladius.
- **Craft 4.** The life now runs in order to the death, and the split, the spread and the translation follow it. The connection is carried through acts (monks who cannot read, a priest sending books, Jerome dictating, an abbot compiling).
- **Rigor 3.** The quotes are verbatim and every Do not say line on the list is honoured, but the final sentence overstates the Concordia (N1).
- **Accessibility 4.** Plain words. Eustochium and Cassian go by unplaced, but the sentences still work.

## Source check

Every sentence was traced to `Outline.md`. The quotes were re-checked in `cic/texts/`:
- Quote 1: `amelineau_histoire-de-saint-pakhome-annales-guimet-17_leroux1889.txt` 5145-5146, "Ce sont des gens chrétiens : ils agissent ainsi avec nous, par amour pour le Dieu du ciel." This matches the outline's rendering.
- Quote 2: same file, 6246-6248, with note e at 6260. The story says "called him three times" and gives the name twice. Correct.
- Quote 3: `acta-sanctorum_maii-tomus-3-lat-grc_palme1866.txt` 86631-86633, "Istud ... straguli absque mora hinc aufer; non enim aequum est ut in re quapiam melius mihi sit quam Fratribus ceteris." Matches.
- First community, rules and stewards: Amélineau 6252-6300, 6333-6336. Concordia purpose: `benedict-aniane_concordia-regularum-with-ardo-vita-pl103-lat_migne1851.txt` 30903-30911 ("suam ex aliorum fultam esse Regulam"). The file holds about 50 "Ex Regula sancti Pachomii" sections among excerpts from other rules.

## Earlier findings, line by line

From `Review.md`:
- **B1 (BLOCKING), Palladius's seven thousand heard as users of the Latin: resolved.** The story uses the outline's own Do not say wording ("Palladius, visiting Egypt, counts about seven thousand monks there under the rule"), and the count comes before Jerome.
- **B2 (BLOCKING), split after his death missing: resolved.** "The fellowship split, and Theodore's letters urged the breakaways back." Theodore is not made the successor: "Petronius, his chosen heir, died within days, and Horsiesius and Theodore led on."
- M1, Esneh out of order: resolved. Esneh and the death now sit in the life, and the life runs in order.
- M2, "That Life" with no referent: resolved ("The Coptic Life says an angel...").
- M3, "A priest sent Jerome the books from Alexandria": **not resolved.** The old wording is back. It is still MINOR (see N5).
- M4, "in his houses" for Metanoia: resolved as far as it matters. "in those houses" points to the Egyptian houses under the rule, and nothing false is said.
- M5, length: see the length ruling below.

From `Recheck.md`:
- The timeline jump at his death: resolved. The death is told in order, before the split.
- "hard work" in Palamon's rule and "at first" for the first community: both restored ("hard work"; "At the start").

## Outline must-tell check

All present: the conscription and prison, the vow, baptism and the epidemic, Palamon's older rule, Tabennisi with the voice and the angel in the Life's voice, the tablet credited to Palladius and denied in the Coptic Life, the first community and its rules, no priests and the hiding, Mary and the contested site of the women's house, the Esneh attack credited to the Greek Life, the plague with the outline's "a hundred or more", 346 or 348, the blanket, Petronius then Horsiesius, the split, Palladius's count, Cassian kept separate from Jerome, Jerome's books, his dictating for the Latin monks and for his own brothers and Eustochium's nuns, and Benedict of Aniane's Concordia. The three items the writer left out are ruled here:
- **The Ge'ez version: not essential, no finding.** It is the last clause of "What came of them" 1, and the outline's Connection section carries the Latin route alone. Leaving it out implies nothing false: the story never says Latin was the only translation.
- **The Coptic feast day: not essential. MINOR at most, optional.** It is the lowest item in "What came of them" (Remembered). The tradition already reaches the listener through "the monks of Egypt" and "Coptic Life". If words free up, "Egypt's Coptic church still keeps his day" would end the Coptic side of the story well, but nothing is missing that the test needs.
- **Benedict of Aniane's date (died 821, early ninth century): not BLOCKING on its own, MINOR.** The listener can still give the third line without it. But it is the only way to hear how long the rule lasted ("long after him", the outline's Thread). It costs three words, so add it inside the N1 fix.

## New findings

**N1. BLOCKING. The Concordia is overstated.** "set it beneath each chapter of Benedict's Rule, to show the ground that Rule stood on." Benedict of Aniane set passages from Pachomius's rule, among passages from other rules, under the chapters of Benedict's Rule. Ardo gives the purpose: to show that Benedict's Rule was "propped on others'" ("ex aliorum fultam", 30903-30911). The outline says "passages from the rule of Pachomius and others ... that Benedict's Rule stood on theirs". Its Do not say line already gives the safe form: "as one of the rules it agreed with". As heard, the sentence says that Pachomius's rule alone was the ground of Benedict's Rule, set under every chapter. That is a misleading implication about the connection itself. Change, for example: "Through that Latin the rule went west. In the ninth century the abbot Benedict of Aniane set passages from it and other old rules under the chapters of Benedict's Rule, to show that Rule stood on theirs." Do not say line to add to the outline: "Benedict of Aniane set Pachomius's rule under each chapter, or as the ground of Benedict's Rule" → "he set passages from it and other old rules under the chapters of Benedict's Rule, to show that Rule stood on theirs". (added from Recheck2.md, 2026-11-18)

**N2. MINOR. "He would have no priests among his monks"** drops "and kept them under the bishops", which is half of what he defended (outline beat 5; I3). Without it, the line could be heard as hostile to the clergy. Change: "He would have no priests among his monks, though he kept them under the bishops, ..." Or keep the line short and trust the hiding to carry it.

**N3. MINOR. The Esneh sentence** is 32 words. In the source the attack comes as he finishes his answer (Greek 86463), not while he is being questioned. Change, for example: "At Esneh, monks and bishops met in church to question him over claims that he could read hidden thoughts. As he finished his answer, a man with a sword burst in to kill him; the Greek Life says the Lord saved him."

**N4. MINOR. "Cassian drew on 'the monks of Tabenna'"** reads as drawing on people. The outline has the rule of "the monks of Tabenna". Change: "and Cassian, who had lived among Egypt's monks, drew on the rule of 'the monks of Tabenna'". Or cut the clause to make room for N1.

**N5. MINOR. "A priest sent Jerome the books from Alexandria"** (M3, back again). Jerome says the books had come to the priest from Alexandria (4336-4337). Change: "A priest sent Jerome books that had come from Alexandria."

**N6. MINOR. "daily fasting"** drops the outline's "until evening in summer" (beat 2). It is a small overstatement and needs no change unless the line is being reworked.

## Length ruling

472 words by the scorer (473 by `wc`) against "about 400 to 450". That is about 5% over a figure the outline gives as approximate. Nothing is filler: every paragraph carries a beat or the connection, and the outline's own reason for the length (two Lives that disagree, and a connection across three languages) is what the extra words are spent on. **Ruling: acceptable, not a finding.** The N1 fix should stay close to neutral in words. If trimming is wanted, "The monks of Egypt already had a way of life" repeats "an older rule" (−10), and N4's Cassian clause can go (−6).
