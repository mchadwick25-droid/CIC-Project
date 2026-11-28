# Fresh read: the first-time listener (Tacitus)

A new first-time visitor: no church background, English as a second language. I saw no source, outline, other read, `Revision.md` or earlier draft. I heard the final `tacitus.brief.txt` once, then ran the two tools.

## Counts

| Item | Count | Blocking |
|---|---|---|
| 1. Test lines not filled | 0 of 4 | 0 |
| 2. Opening gaps after three sentences | 2 (when, why there) | 0 (who and where are clear) |
| 3. Sentences that fail on one hearing | 2 | 0 (MINOR) |
| 4. Bare statements | 0 | 0 |
| 5. Citations read aloud not called for | 0 | 0 |
| 6. Tells Part 1 names | 0 | 0 |
| 7. Unexplained words / short-sentence runs / talking down | 2 / 0 / 0 | 0 (MINOR) |

**Listener verdict: PASS.** Nothing here is BLOCKING.

## 1. The test

- **Who:** Tacitus, a Roman historian who thought the Christians guilty and despised them. Filled.
- **What happened:** after the fire of 64, Nero blamed the Christians and killed them cruelly, and Tacitus wrote the fullest outside account of it. Filled.
- **What it was about:** the passage names Christ, put to death under Pilate, and gives an enemy's view of the Christians. It is a few sentences, about 140 Latin words. Filled.
- **Why the connection matters:** Tertullian answered Tacitus by name, on another passage. Sulpicius Severus retold the scene in nearly Tacitus's words and called the dead innocent. Filled.

## 2. The opening

After the first three sentences, who (Christians, Nero, Tacitus) and where (Nero's gardens, Rome) are clear. Missing: **when**, which comes in sentence 4 ("in 64"), and **why there**, meaning why the Christians were burned. The fire, which comes in sentence 4, points to it, and paragraph 4 says it. I was not lost, so this does not block.

## 3. Sentences that fail on one hearing (MINOR)

1. "Their crime, he says, was less setting the fire than hatred of the human race." On one hearing, "less setting ... than hatred" is hard to parse, and I lost that this is about what they were convicted for. **Exact change:** "They were convicted, he says, less for setting the fire than for hatred of the human race."
2. "First those who confessed were seized." Confessed to what: to the fire, or to being Christians? **Noted only.** Supplying an answer could add an assumption the record does not hold. Leave the sentence as written.

## 4. Bare statements

None. The Annals, the Apology, "Christus", the rumor, the punishments and Tertullian's charge of lying each come with what they were and why.

## 5. Citations read aloud

None counted. See the craft tool below.

## 6. Tells

None. No dash for drama, no stock word, no question answered by itself, no moral close. The story ends on Tacitus's own words. The "not for the public good, but for one man's cruelty" turn is inside his quote, not the narrator's voice.

## 7. Words, runs, tone

- "caught him out" (an idiom that a second-language listener may not know). **Exact change:** "and caught him out:" becomes "and pointed to his own words against him:".
- "the most refined cruelty": "refined" in this sense may puzzle some listeners, but the meaning comes through from what follows. **Noted only.**
- No runs of short one-act sentences. Nothing talks down.

## 8. Attention

The opening pulls me in strongly. Attention first drifts at "Later, one Christian, Tertullian, answered him by name on another matter, and another, Sulpicius Severus, retold his scene...". Two new names and "another" used twice arrive before the story itself has started. It drifts again in the donkey's-head paragraph, which moves away from the fire. The temple argument pulls me back. I would listen to the end.

## The tools

- `engine.m1.profile_readability`: 570 words, grade 9.4 (8.3 with names left out), reading ease 70.9, 19.7 words a sentence, longest sentence 34 words. **Pass.**
- `check_brief_craft.py`: three lines flagged "names a source".
  - s11 "He punished them, Tacitus writes, with the most refined cruelty." This is a judgment of blame, so crediting the witness is called for. Not counted.
  - s21 and s23 "Tertullian says". Tertullian acts and speaks in the story; he is not a citation. Not counted.
