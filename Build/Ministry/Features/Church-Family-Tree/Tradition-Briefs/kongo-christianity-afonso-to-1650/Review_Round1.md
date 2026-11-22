# Review, round 1: kongo-christianity-afonso-to-1650

Reviewer: Opus, independent of the writer. Brief read: `kongo-christianity-afonso-to-1650.brief.txt` (408 words). Sources checked by opening the lines myself in `cic/texts/`: `paiva-manso_historia-do-congo-documentos-por_1877.txt` (PM) and `lopes_report-of-the-kingdom-of-congo_hutchinson1881.txt` (Lopes).

## Verdict: REVISE

Three BLOCKING findings, all fixable with the exact wording below. The quotes, dates, numbers and the 1540 ending check out against the sources.

## 1. One hearing, as a new listener

- **Who or what:** Kongo's Christian court under Afonso I, a king whose own letters to Portugal and the pope survive.
- **What happened:** Kongo's king and then his son were baptized after the Portuguese came in 1491. Afonso fought off a brother who opposed the faith, sent kin to Portugal to learn, and in 1526 begged Portugal to send priests and teachers and no merchants, because the slave trade was emptying his land. In 1540 he accused a friar of trying to have him shot at Mass.
- **Why it matters:** the faith and the slave trade reached Kongo through the same contact, and a Kongo king set the one against the other in writing. I could only say this after the fifth paragraph (see B3).

Where I got lost: at "so that he could reach the capital in time". In time for what? The story drops the struggle there. Nothing reads as a children's book. The voice is plain and adult.

## 2. Fidelity, sentence by sentence

| Brief sentence | Source | Result |
|---|---|---|
| July 1526 letter; wine and flour for the Mass; land emptied | PM 2339-2343 (heading, 6 July 1526), 2349-2351, 2405-2410 | Holds |
| "Portuguese ships reached the mouth of the Zaire River in 1491." | Lopes 3510-3512 | Holds (Lopes's date) |
| "A report written down a century later says Kongo's king was baptized and took the name Dom João" | Lopes 1-2, 53 (Pigafetta, Rome, 1591); 3670-3672 | Holds |
| "...his son, who took the name Afonso, soon followed." | Lopes 3687-3689: "his fon, who foon alfo became a Chriftian, taking the name of Affonfo" | Holds; "soon" is Lopes's word |
| "That report is the main source for how the faith began." | Sheet: Lopes is the only *vendored* source for 1491 | **Unsupported (B1)** |
| Afonso's letters survive; almost all else by outsiders | Sheet, Who tells it | Holds (the scribes are dropped; see M4) |
| 1512 letter to the pope, later printed by a chronicler; religious men led his people from idols | PM 533-545; footnote 551 (Damião de Góis, *Chron. de D. Manuel*, part III) | Holds; the Góis framing is right |
| 1517: sent kin to learn the faith, to bring light to the blind after his death | PM 1931-1937 | Close, but "after my death" is moved (M1) |
| Brother Pango stood against him | Lopes 3711-3716 | Holds |
| Rule of one wife turned some nobles and their wives against it | Lopes 3700-3720 | Holds |
| Lost his province on a charge he wanted the throne; won it back | Lopes 3722-3740 | Holds |
| Mother kept the death secret three days so he could reach the capital | Lopes 3755-3777 | Holds; but the war that follows (Lopes 3795-3830, Pango routed about 3999-4029) is left out (B2) |
| Merchants and thieves carry off his people every day, sons of nobles, his kin | PM 2399-2405 | Holds |
| Asked for priests and teachers for his schools, and no merchants | PM 2406-2411 | Holds ("padres e algumas poucas pessoas pêra emsynarem nas escollas"; "nam mande ca mercadores nem mercadorias") |
| "The sources read for this brief do not say what Portugal did." | Sheet, Do not say | True, but process narration (M3) |
| "Fourteen years later, he wrote again." | 1526 + 14 = 1540 | Arithmetic holds; "again" misleads (M2) |
| Friar; seven or eight white men; Easter Mass; shot by the skirts of his robe; killed one, wounded two | PM 3425-3433 | Holds. The letter says "Ja escrevemos" (we have already written), so the attack is told again here, not first. It also says the ball struck the chief bailiff beside him before it killed one man and wounded two. The brief's wording is not wrong |
| "That is his claim alone, and no second witness was found." | Sheet C6 | True, but process narration (M3) |
| Last sentence: calls the king of Portugal brother; signs himself king | PM 3389 ("seu muito lear Irmaô"), 3456 ("príncipe irmão"), 3459 ("ElRey + dom affomso"); also 1517 at 1928, 1526 at 2423, 2428 | Holds |

The four faults (Kit Part 1):
- One witness's claim told as fact: no. Lopes is credited ("the report says", "the report adds"), and the 1540 charge is credited to Afonso.
- Editor's view given to the source: no. The Góis footnote is reflected correctly.
- Detail on the wrong event: only M1, a small one.
- Force or conflict softened: yes, B2.

## 3. Quoted and rendered spans

- **Q1** (quoted): "It is our will that in these kingdoms there be no trade in slaves, and no outlet for them." Source PM 2411-2412: "nossa vontade he que nestes Reynos nam aja trato de esprauos nem sayda pêra elles". Verified verbatim in the file. The rendering is faithful: every clause is there and nothing is added. 'esprauos' is OCR for escravos.
- **Q2** (rendered, not quoted): "bring light to the blind". Source PM 1935-1936: "por alumiar os cegos que sam em meus Reynos". This is faithful, but see M1 for the clause attached to it.

## 4. Scorer

`python -m engine.m1.profile_readability .../kongo-christianity-afonso-to-1650.brief.txt`:
408 words, grade 6.8 (names out 5.7), reading ease names out 82.9, 16.3 words a sentence, 0.7 joining words per 100, 12% short sentences, longest sentence 30 words: pass. Grade 6.8 is under 8, so I judged it by ear: it does not sound flat or talk down. Long and short sentences alternate and the chains hold together. No change for the score.

## Findings

**B1. BLOCKING: unsupported claim.** "That report is the main source for how the faith began."
The sheet says Lopes is the only source *vendored* here for 1491. It does not say he is the main source in the record, and the Portuguese chroniclers are earlier. The credit "A report written down a century later says" already does the work.
Change: delete the sentence.
Do not say line to add to the Sheet: "Not that Lopes is 'the main' or 'only' source for 1491. He is only the one vendored here."

**B2. BLOCKING: conflict softened by leaving it out (fault four); misleading implication.** The paragraph ends: "When the old king died, the report adds, Afonso's mother kept the death secret for three days so that he could reach the capital in time."
The record goes straight on to a war for the throne: Pango "came armed againft his brother" (Lopes 3804-3806) and was routed (about Lopes 3999-4029). Without it, the story implies a peaceful succession and leaves the listener asking "in time for what?".
Change: after that sentence add: "Then, it says, Pango brought a great army against him, and Afonso defeated it and kept the throne."
This keeps the battle's numbers and the vision out, as the Sheet asks.

**B3. BLOCKING: the essence is not told in the first minute** (reviewer method, step 1; Kit Part 1, Craft). In the first 150 words the listener hears a letter, a land "emptied of its people", and the 1491 baptisms. They do not hear that the faith and the slave trade came through the same contact, or that Afonso set one against the other. That is the connection the Sheet says to carry, and it arrives only at word 260 or so. The opening also uses the held-back reveal "The writer was Afonso I", which the Kit names as not a stock hinge.
Change: replace the first paragraph and the first sentence of the second ("The writer was Afonso I, king of a kingdom that had become Christian.") with:
"In July 1526, Afonso I, the Christian king of Kongo, wrote to the king of Portugal. He asked for wine and flour for the Mass. Then he warned that his land was being emptied of its people, who were being carried off to be sold. Contact with Portugal had brought Kongo both the faith and this trade, and in his letters Afonso set the one against the other."
The second paragraph then begins "Portuguese ships reached the mouth of the Zaire River in 1491." Support: PM 2349-2351, 2399-2412; the Sheet's Connection to carry.

**M1. MINOR: clause moved.** "...so that they could bring light to the blind in his kingdom after his death."
In the letter, "after my death" belongs to upholding the faith, not to bringing light (PM 1935-1937).
Change: "In 1517 he wrote that he sent his kin to Portugal to learn the faith and bring light to the blind in his kingdom, so that after his death they could uphold it."

**M2. MINOR: misleading "again".** "Fourteen years later, he wrote again. In December 1540, he accused a friar of arranging..."
"Again" suggests this was his next letter, when other letters lie between 1526 and 1540 (PM 3298-3380, 4 December 1540, for one). The 1540 letter also says he had already written about the attack.
Change: "In December 1540, fourteen years on, he wrote to Portugal of an attempt on his life. He said a friar had arranged for seven or eight white men to fire at him during Easter Mass."

**M3. MINOR: process narration and stock how-we-know sentences** (Kit Part 1, Rigor; participant-facing text names no "brief").
- "The sources read for this brief do not say what Portugal did." Change to: "His letter is a plea. It does not tell us what came of it."
- "That is his claim alone, and no second witness was found." Change to: "That charge rests on his word alone."

**M4. MINOR: optional, the scribes.** "Afonso spoke for himself in letters, and they survive, ..."
The Sheet says the letters were written by scribes in his name (PM 2428, 3458). If there is room, change to: "Afonso spoke for himself in letters his scribes wrote down, and they survive, ..." This is not required: the letters are his words as he sent them.

PRE-EXISTING: none.
