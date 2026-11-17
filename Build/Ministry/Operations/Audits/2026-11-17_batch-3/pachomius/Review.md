# Pachomius: review

Reviewer, 2026-11-17. Story: `pachomius.brief.txt`. Judged against `Standard.md`, `Shapes.md`, `Process.md`, `Outline.md`, `Outline_Check.md` and `Outline_Recheck.md`. No earlier draft read.

## The test, from one hearing

- **Who:** Pachomius, a pagan-born young man from Upper Egypt, conscripted in Constantine's time, who became a Christian and gathered monks into a shared life under one rule at Tabennisi on the Nile, in the fourth century.
- **What happened:** Christians fed him in prison and he vowed to serve people; he was baptized, trained under the hermit Palamon, built a community at Tabennisi with common clothes, food and rules, refused ordination, set up a house for his sister and other women, faced a hostile hearing and a murder attempt at Esneh, and died of plague, refusing a better blanket than his brothers had.
- **Why the connection matters:** his communities' rules were put into Latin by Jerome for Latin-speaking monks and nuns who wanted to live that way, and through that Latin they went west, where Benedict of Aniane set them under Benedict's Rule as one of the rules it stood on.

**One-hearing test alone: PASS.** All three lines can be given after one hearing, and nothing reads as a children's book or talks down.

Where I got lost:
- The story goes from the ninth century back to "In his own lifetime" for Esneh, then to his death. The signpost saves it, but it is the one place a listener has to rebuild the timeline.
- "That Life says an angel..." follows "the Lives say". On one hearing "that Life" has no clear referent.
- "Soon after, Palladius counted about seven thousand monks living under it" comes straight after Jerome's Latin version, so "it" is heard as the Latin (see B1).

## Score

`python -m engine.m1.profile_readability`: 473 words, grade 7.4 (names out 6.3), reading ease 80.3, 16.9 words a sentence, longest sentence 32 words. Pass, with the note that grade is under 8. Listener read: not flat. The prison opening, the "new plants", the hiding and the blanket carry the world's own detail. The baptism-and-epidemic line is compressed but not childish.

## Scores

- **Voice: 4.** A documentary narrator throughout, with witnesses named where they matter (the Coptic Life for the prison words, the Greek Life for Esneh and the blanket). Wonders stay in the Lives' voice. One summary line ("he was not always welcomed") is the narrator's, but mild.
- **Craft: 3.** Strong opening and ending; the connection is carried through acts (monks who could not read, a priest sending books, Jerome dictating, an abbot compiling). The out-of-order Esneh section and the missing split after his death weaken the structure and the "what came of them" third.
- **Rigor: 3.** Quotes are verbatim to the outline and faithful to the files; the Do not say list is honoured. But one sentence implies something false (B1) and one outline item that carries the record's conflict is missing (B2).
- **Accessibility: 4.** Plain words, short paragraphs, place and time given early. "Eustochium's nuns" goes by without a word of who she was, but the sentence still works.

## Source check

Every sentence was traced to `Outline.md`. Quotes re-checked in `cic/texts/`:
- Quote 1: `amelineau_histoire-de-saint-pakhome-annales-guimet-17_leroux1889.txt` 5145-5146, "Ce sont des gens chrétiens : ils agissent ainsi avec nous, par amour pour le Dieu du ciel." Matches the outline's rendering.
- Quote 2: same file 6247-6248, with note e (6260) on the third name. The story uses the name twice and says "called him three times". Correct.
- Quote 3: `acta-sanctorum_maii-tomus-3-lat-grc_palme1866.txt` 86631-86633, "Istud ... straguli absque mora hinc aufer; non enim aequum est ut in re quapiam melius mihi sit quam Fratribus ceteris." Matches.
- Also checked: the prison and vow (A 5141-5184), the epidemic (A 5283-5288), Palamon as "vieillard" and his rule (A 5370, 5424-5434), Jerome's preface (`jerome_opera-pl23-part1-with-regula-pachomii-lat_migne1883.txt` 4326-4387), Palladius's 7,000 (`palladius_lausiac-history_clarke1918.txt` 405), the plague (G 86510-86512).

**Must-tell check.**
- Force and coercion: conscription and imprisonment are in. The Esneh hearing and the man with a sword are in, credited to the Greek Life.
- Conflict after his death: **missing.** The outline's "What came of them" item 2, added by the check (M5) because conflict is told as plainly as virtue: the fellowship split after his death, and Theodore's letters urged the breakaways back. See B2.
- Connection: in, through the acts the outline names (Latin-speaking monks, Silvanus's books, Jerome dictating for his brothers and Eustochium's nuns, Benedict of Aniane's Concordia). No "this matters because" sentence. Cassian is not tied to Jerome.
- Defended: equality (the blanket) and monks without clerical rank (no priests; he hid from ordination) are both in.
- Uncertainty: "346 or 348", "about seven thousand" with Palladius named, "he hid" without a place. In.
- Do not say list: honoured throughout.

**Length:** 474 words by `wc`, about 3 minutes 10 seconds at a narrator's pace. The outline sets about 400 to 450 words. It is just over, and adding B2 must not push it further.

## Verdict: REVISE

## Findings

**B1. BLOCKING. Palladius's seven thousand is heard as living under Jerome's Latin.** "Soon after, Palladius counted about seven thousand monks living under it" follows "Jerome dictated a Latin version", and "In Latin, the rule went west" follows it. Palladius (Clarke 405) counts the monks of Egypt's monasteries that kept the rule, in Egypt, not users of the Latin. Change: move the count out of the Jerome paragraph, into the life or the start of the "what came of them" section, and say where they were: "Palladius, who visited Egypt about seventy years later, counted about seven thousand monks there living under the rule." Do not say line to add to the outline: "Palladius's seven thousand placed after Jerome's Latin, or as 'living under it' where 'it' could be the Latin" → "Palladius, visiting Egypt, counts about seven thousand monks there under the rule".

**B2. BLOCKING. The split after his death is missing.** The outline ranks it second in "What came of them" ("The fellowship outlived him, but not unbroken") and the check added it as the record's conflict. The story gives only growth and spread. Change: add one sentence, from the outline only, e.g. "After his death his fellowship split, and Theodore wrote letters urging the breakaways back into unity." Place it with what came of him. Do not say line to add: "The fellowship carried on unbroken after him (by leaving out the split)" → "it split after his death, and Theodore's letters urged the breakaways back".

**M1. MINOR. Esneh is told out of order.** The jump from the ninth century back to his lifetime is the one hard place on one hearing. Change: put the Esneh paragraph in the life, after the sister, so the life runs in order to his death. Then either end on the connection or keep the blanket as the last scene with the connection just before it. This also lets "In his own lifetime, he was not always welcomed" go, which helps the length.

**M2. MINOR. "That Life says an angel..."** has no referent after "the Lives say". Change to "The Coptic Life says an angel..."

**M3. MINOR. "A priest sent Jerome the books from Alexandria"** can be heard as the priest sending from Alexandria. Jerome says the books had been sent to Silvanus from Alexandria (J 4332-4333). Change: "A priest sent Jerome books that had come from Alexandria."

**M4. MINOR. "Latin-speaking monks in his houses."** Jerome places them in the communities of the Thebaid and at Metanoia, near Alexandria, which was not one of Pachomius's own foundations. Change: "Latin-speaking monks in the communities of Upper Egypt and near Alexandria".

**M5. MINOR. Length.** 474 words against about 400 to 450. Trim to fit when making B1 and B2; M1 frees a sentence.
