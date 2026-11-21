# Review: Lactantius

Batch 7, 2026-11-20. Reviewer, per `Brief-Kit/roles/reviewer.md` and the batch 7 reviewer prompt. Read: `lactantius.brief.txt` (once, straight through, before anything else), the Kit, `Hearts.md` (Lactantius), the Decision-Log entries "Batch 7: …" (2026-11-20), "Batch 6: where sources disagree" and "Change order: the stories approved before the kit…" (2026-11-19), the census entry `lactantius`, `Outline.md`, `Source_Sheet.md`, `Outline_Check.md`, `Fixes.md`, `Recheck.md`, `Cut_Check.md`, and the cited lines in `cic/texts/`. Paragraph numbers (P1–P12) are the brief's paragraphs.

## Verdict: REVISE

Two BLOCKING findings, both fixable without adding words: the approved essence is not complete in the first minute (Crispus), and one sentence misstates his teaching on the end of the world.

## 1. The test, from one hearing

- **Who:** a teacher of Latin public speaking from Africa, working at Nicomedia, the emperor's city, when the Great Persecution began there in 303.
- **What happened:** he answered the persecution with the *Divine Institutes*, a case for the faith made to educated pagans from their own authors, holding that religion cannot be forced; later his *On the Deaths of the Persecutors* told how each persecuting emperor died, and kept the edicts' texts.
- **Why the connection matters:** Jerome and Augustine read and used the *Institutes*, Jerome praising the style and faulting the teaching; the book on the persecutors is the close, partisan record of those years and keeps the Latin of the edict of Milan.

None blank or wrong. I did not get lost. Nothing reads as a children's book or talks down.

## 2. The heart

**My own essence first** (from the census entry and what he is known for): a Latin teacher of public speaking from Africa, at Nicomedia when the Great Persecution began in 303, who answered it with the *Divine Institutes*, the reasoned Latin case for the faith made to educated pagans in their own terms, holding that belief can be won but never forced; and who left, in *On the Deaths of the Persecutors*, the inside record of that persecution. Also to be told: why and how he wrote (the two men, the method against Tertullian and Cyprian), what the books say, the force of the persecution, the fire's disputed cause, and his readers, Jerome and Augustine.

**Against the approved heart** (`Hearts.md`; the outline's essence, Outline line 5, keeps all four sentences):

- Nicomedia and 303: P1–P2, by word 123. The summons itself is P3 (word ~140) and "Diocletian's capital" is implied by "watching from his palace", not said.
- The *Institutes*, to educated pagans from their own authors, religion cannot be forced: P2, by word 123.
- *On the Deaths of the Persecutors*: P2, "A second book told how the persecutors died", by word 123.
- "Late in life, Jerome says, he taught Constantine's son": P10, at about word 545.

**The word at which the essence is complete:** about word 547 ("…in Gaul.", P10). The essence's substance (what he did, what it changed) is complete at word 123 ("…how the persecutors died."), but the approved heart's fourth sentence comes only at word ~547. See B1.

Also told, each present with its weight: why and how he wrote (P5–P6, with Q1); what the *Institutes* say (P7, with Q2); what *the Persecutors* holds, the edicts copied, the children killed told as his verdict, "exact" and "partisan" credited (P8, P9, P11); the fire's three causes, one clause each (P4). Nothing of the approved heart or of a credited disagreement was left out to fit.

## 3. Order, names, ending

- **Order.** Hook at 303 (P1), essence (P2), then the life from the summons (P3), 303 (P4–P5), the *Institutes* (P6–P7), 311 and 313 (P8), about 314 (P9), Gaul (P10). The hook reaches ahead; the life then runs forward once. No event told twice; P4 opens on "the day after the church fell" without retelling the fall. PASS.
- **Opening.** The name is in the first sentence ("as Lactantius's own account tells it"); no held-back reveal. PASS.
- **Ending.** On the person, in Jerome's words on the man. PASS.
- **Names.** Lactantius, Diocletian, Galerius, Eusebius, Constantine, Tertullian, Cyprian, Cicero, Nero, Crispus, Jerome, Augustine. Heard once and neither acting nor linking: Nero only (P9). He is a household name and does not lose the listener; the cut in M5 removes him anyway. Tertullian and Cyprian are links, but heard bare (M2).

## 4. Length and sentences

`python -m engine.m1.profile_readability …/lactantius.brief.txt`: **674 words, grade 9.0 (names out 7.7), reading ease 69.7 (names out), 16.9 words a sentence, longest sentence 28 words — pass.**

674 words sits at the person ceiling (675, about 4:30), not past it: not BLOCKING. The fixes below are word-neutral or paid for by the cuts listed. No sentence passes 30 words.

## 5. Source check

Every sentence traced to the outline and, through `Source_Sheet.md`, to its line. Checked in the files:

- P1: AN 10161 (doors forced, Scriptures burned, pillage, Diocletian's fear of the city burning, guards with axes, "in a few hours"). AN 4487 ("When I was teaching rhetorical learning in Bithynia…"). Holds.
- P3: JE 41033–41038 (summoned in Diocletian's reign, taught rhetoric, few pupils, a Greek city, turned to writing). Holds.
- P4: AN 10174 (edict, rank, torture); AN 10185 (Galerius's emissaries); EU 43982–43984 ("I know not how"); EU 70323–70325 (lightning, "of whom I myself am one"); AN 10198 (presbyters led to execution, "a herd of them were encircled with the same fire", servants with millstones). Holds (one word, M3).
- P5–P6: AN 4487, 4567, 4569, 4472–4476, 4573–4581. Holds.
- P7: AN 5162 ("the blood of animals, and the smoke of incense … a good mind, a pure breast"); AN 6648–6650 (see B2).
- P8: AN 10462 (worms), 10486 ("again to be Christians"), 10501, 10680–10690 (Milan posted at Nicomedia; places of assembly restored to the Christians). Holds.
- P9: AN 10223 ("nine times"), 9987 ("all who shall arise hereafter, may learn"), 10712 (the boy of eight and girl of seven; "all the impious received according to the deeds that they had done"). Holds.
- P10: JE 41051–41054. Holds.
- P11: JL 14112–14114, JL 19203–19211, AU 35552–35555; the modern editor and historian per the sheet (EU-ed 50239–50242, MO 29275–29282). Holds.

**Quotes**, each against its Latin:

- Q1 (P5): DI-L 23206–23210, "et illorum superba inpietate stimulatus et ueritatis ipsius conscientia et, ut ego arbitror, deo, suscepi hoc munus". Word for word the outline's rendering (Outline line 52); the rendering is faithful. The trim is at the end (the purpose clause "ut … refutarem"), not inside the span. PASS.
- Q2 (P7): DI-L 26240–26242, "defendenda enim religio est non occidendo sed moriendo, non saeuitia sed patientia, non scelere sed fide". Word for word the outline's (line 53). PASS.
- Q3 (P12): JC 44982–44986, "uir omnium suo tempore eloquentissimus sed adeo in hac uita pauper ut plerumque etiam necessariis indiguerit". Word for word the outline's (line 54). PASS.
- No other quoted words in the story.

**Where held sources differ** (2026-11-19 ruling): the fire's cause (three witnesses, each credited), the authorship of *the Persecutors* ("Most scholars hold it his; some have doubted", once), the conversion ("not known"), Jerome's praise beside his charge, the historian's "exact" beside "partisan". PASS.

**Words to explain.** rhetoric (P3, "the art of public speaking"), the Great Persecution (P2), edict (P4, "an emperor's public order"), *Institutes* (P2, "a handbook of the true religion"), Sibyls (P7), Cicero (P7, first hearing), Bithynia (P1): each glossed where first heard, none saying more than the outline's gloss. Caesar is not used ("junior emperor" stands for it). Holy Spirit unglossed, as the outline says. No gloss on a word a grown listener knows. PASS.

**Do not say.** Honored throughout: "summoned … in Diocletian's reign", "was teaching in Bithynia", "from Africa", "not known", "Lactantius blames agents of Galerius", "in Gaul", "Constantine's son", "copied their text", "set them out together", the children told, the verdict as his.

## 6. Scores

- **Voice 4.** A documentary narrator throughout, plain and adult; the fire and the killings are told without softening. P7 runs close to a list of propositions.
- **Craft 4.** Strong hook into a clean essence, the life once in order, a good close on the man; the essence's last sentence arrives late (B1).
- **Rigor 4.** Every quote verbatim, every disagreement credited; one misstatement of his doctrine (B2), and one small word shift on Eusebius (M3).
- **Accessibility 5.** Grade 9.0, ease 69.7, glosses worked into the sentence, sentences 28 words at most.

## 7. Findings

### BLOCKING

**B1. The approved essence is not complete in the first minute.** The heart's fourth sentence, "Late in life, Jerome says, he taught Constantine's son", is heard only at P10, about word 547. Move it into the essence and do not tell it again. Word-neutral.
- P2: after "A second book told how the persecutors died." add "Late in life, Jerome says, he taught Constantine's son Crispus in Gaul."
- P10: delete "Late in life, Jerome says, he taught Constantine's son Crispus in Gaul." and keep "How and when Lactantius died is not known." as the paragraph.
- The essence is then complete at about word 135.
- **Do not say** line to add to the outline: "Crispus held back to beat 7, after the first minute → the essence's 'Late in life, Jerome says, he taught Constantine's son Crispus in Gaul' within the first 150 words; beat 7 then tells only that his death is not known."

**B2. "the world will end after six thousand years" (P7) misstates him.** Lactantius says the world continues "in its present state through six ages, that is, six thousand years"; at the end of the six thousandth year wickedness is abolished "and righteousness reign for a thousand years" (AN 6648–6650). The world does not end at six thousand years. The outline's beat 4 (line 40) left room for this; its Also told (line 8) had it right.
- P7: replace "and the world will end after six thousand years" with "and the world will run as it is for six thousand years". Net +1 word.
- **Do not say** line to add to the outline: "'the world will end after six thousand years' → 'the world will run as it is for six thousand years' (a thousand-year reign follows; AN 6648–6650)."

### MINOR

- **M1. Q1 heard without a speaker** (P5). The first-person quote follows a sentence about the two men, so the listener may hear the narrator's "I". Before the quote add "He wrote:". +2 words.
- **M2. Tertullian and Cyprian heard bare** (P6). Neither is placed, so the listener does not know they were the Latin Christian writers before him. Replace "Tertullian, he judged, had been obscure" with "Of the Latin defenders before him, Tertullian, he judged, had been obscure". +6 words.
- **M3. "does not know why"** (P4). Eusebius says "I know not how" (EU 43982–43984), which is the cause, not a motive. Replace "says he does not know why" with "says he does not know how it began". +2 words.
- **M4. "seventy years later"** (P3) sounds exact; Jerome wrote about 70 to 90 years after 303 (*Chronicle* about 380, *Lives* 392; Source_Sheet, Witness kinds). Replace "writing seventy years later" with "writing some seventy years later". +1 word.
- **M5. Cut: the book's span** (P9). Galerius's rotting death is told in P8; "worm-eaten body" tells it again, and Nero is heard once. The story does not need it for the heart, what is also told, the record's force, a gloss or the connection. Replace "It runs from Nero to Galerius's worm-eaten body, and ends with" with "It ends with". Saves 9 words.
- **M6. Cut: "Both were posted at Nicomedia, and"** (P8). Not needed for the heart or the connection, and it can imply that he copied the edicts from the wall there, which no source says (he had left Bithynia by about 305, a modern reconstruction). Replace "Both were posted at Nicomedia, and Lactantius copied their text into his book." with "Lactantius copied their text into his book." Saves 6 words.

With B1, B2 and every MINOR applied: about 674 + 1 + 2 + 6 + 2 + 1 − 9 − 6 = **about 671 words**, still under the ceiling. With only B1 and B2, 675.

No other part of the story fails the "does the story need it" test: every other sentence carries the heart, a part of what is also told, the record's force, a credited disagreement, a gloss or the connection.
