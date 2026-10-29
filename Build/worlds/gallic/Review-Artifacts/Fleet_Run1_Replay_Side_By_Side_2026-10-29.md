# gallic: six-question replay, fleet graded run 1 (29 October), side by side with the older 13 October answers

## Scope

- **New replay.** `engine/m3/reports/fleet-graded-run-1/replay/gallic.json`. Live test "fleet graded run 1". Package `packages/gallic/2026-10-28T03-49-52Z`. Voice: Sonnet 4.5. Safety and reader calls: Haiku 4.5. One conversation of six questions. All six went to the voice (`voice_with_directive`).
- **Older answers.** `engine/m4/reports/live-turn-report-gallic-2026-10-13-eleven-world-test.json` (package `2026-10-13T20-51-45Z`). This is older data, from a different format and a different engine. It is read only for what the text does. It is not scored.
- **Method.** As `Build/worlds/lpc/Review-Artifacts/Run3_Access_And_Craft_Review_2026-10-28.md` and `Build/worlds/lpc/build/lpc_Probe_Results.md`. Four criteria: Rigor, Accessibility, Craft, Focus. P1 is wrong, invented, misleading or damaged, and makes the row FAIL. P2 is small and plainly fixable, and leaves the row PASS with the criterion graded `concern`. Each fix is at the source: a record, a caution or an engine item.
- **Checks.** Every shipped sentence was read against its cited records and against `gallic.core.gallic` (cautions, thinness). I read the citations, `reply_shape.placed` and `removed`, and the grounding verdicts. The one placed quote (`gallic.quote.martin-on-the-christ-with-wounds`) matches its `modern_rendering` exactly, checked by script against `quotes.json`. I scored readability with `engine.m1.gates.grade_text`. The per-turn gate is FK 10 or under and FRE 60 or over (`engine/m7/turn_readability.py`). A turn past it is graded an Accessibility `fail`, because the project treats that gate as a hard fail.
- **Not done.** No model was called. No git command was run. Only this file and its `.counts.json` were written.

## Readability

| Q | Words | FK | FRE | Longest own sentence | Sentences over 25 | Sentences per paragraph |
|---|---|---|---|---|---|---|
| 1 | 230 | **12.9** | 60.9 | 58 | 3 | 2, 4 |
| 2 | 180 | 5.9 | 81.7 | 28 | 1 | 5, 5, 1 |
| 3 | 138 | 5.8 | 78.1 | 32 | 1 | 5, 3, 2 |
| 4 | 137 | 6.4 | 73.7 | 21 | 0 | 10 |
| 5 | 141 | 8.8 | 63.4 | 31 | 2 | 8 |
| 6 | 146 | 7.2 | 72.2 | 33 | 2 | 9 |

## Grades (new replay)

| Q | Question | Result | Rigor | Access | Craft | Focus | Fabrication | Basis |
|---|---|---|---|---|---|---|---|---|
| 1 | Who is Jesus? | FAIL | pass | fail | fail | pass | no | **P1 damaged.** The quote lead-in says the same thing twice: "refused a devil dressed as a crowned Christ: Sulpitius reports Martin telling a devil disguised as a crowned Christ that he would believe only...". The second half is the quote record's own `use_note.means`, read aloud. That 58-word sentence takes the turn to FK 12.9, past the per-turn gate. The quote matches. Content is faithful to `gallic.dw.the-christ-who-bears-the-wounds`. P2: "the fathers of Egypt taught the same meeting in a different form" is unclear and uncited (grounding marked it withhold). The engine removed the elder's quote, so the sentence points at nothing. |
| 2 | What did he do? | PASS | pass | pass | concern | concern | no | Faithful to `gallic.dw.the-christ-who-bears-the-wounds`: the sixth and ninth hours, the descent, "laid it down himself". The cloak story is rightly framed as Christ met in the poor. P2 craft: most of paragraph 1 repeats Q1 nearly word for word. "Among the brethren at Marseilles an elder of Egypt taught the same meeting" is left over from a removed quote lead-in, and it seems to put the Egyptian elder at Marseilles. |
| 3 | A word I might not know | PASS | concern | pass | concern | pass | no | Humility, from `gallic.term.humility`: ten signs, the count's son, Martin's stool, set above miracles, both houses held it. The record says "Across every voice of ours it is the same thing". P2 rigor: "An elder of Egypt taught that we ought to refresh Christ in guests. Humility was what made that act right" is uncited (withhold). The record calls the fast-breaking an act of charity, not humility. "not any power shown afterward" refers to nothing. |
| 4 | Why did your people believe this? | FAIL | fail | concern | concern | concern | no | **P1 against world_core caution:** "The disciples who came to Marmoutier". The caution says Ligugé, Marmoutier, Saint-Victor and Saint-Sauveur are editors' names, so "Never use them as ours". `gallic.voice.craft` says the same. P2 focus: Q3 was about humility, but the answer is about Christ in the beggar. P2 access: one 10-sentence paragraph. P2 craft: the uncited Marseilles/Egypt sentence again. "We believed it because..." is said twice. |
| 5 | Someone who lived this out | PASS | pass | concern | concern | concern | no | Vincent, from `gallic.term.commonitory-peregrinus`, `gallic.term.the-rule`, `gallic.term.the-deposit` and `gallic.figure.vincent`. Peregrinus, the remembrancer, "everywhere, always, by all", gold for gold, the harbour: all match. "He never told his own story" keeps the figure's limit. P2 access: "heretical pravity", "remembrancer" and "Apostolic See" are not explained. One 8-sentence paragraph. P2 craft: "He read the letter from the Apostolic See the same way" is left over from a removed Celestine lead-in. P2 focus: a writer of a rule, more than a life "lived out". |
| 6 | What I haven't asked | FAIL | fail | concern | pass | pass | no | **P1 misleading:** "At Marseilles two friends came back to morning prayer troubled by one sentence an old man had added the night before". In `gallic.story.germanus-scruple-at-morning-service` it happens in Egypt, "at an elder's cell near Panephysis". Cassian wrote it down later, in Gaul. The sentence is tagged to that story and was graded "grounded 100%" on shared words, so the net missed the wrong place. The rest is good: "Which one began the good... we left open", the free-will quotes, and "Massilians" as a hostile outsider's label, as `gallic.contested.massilian-label` holds. P2 access: one 9-sentence paragraph. |

## Findings and fixes

**P1**

- **G1. Quote lead-in reads the record's `means` aloud (engine), Q1.** The voice copied `use_note.means` as the lead-in to its own placed quote, after its own lead-in. Fix (engine):
  - The prompt should not offer `means` as text the voice can speak.
  - Placement should reject a lead-in that matches a record's `means` word for word.
  - The per-turn readability gate should hold a turn over FK 10, not ship it.
- **G2. Editors' place-name (caution and engine), Q4.** "Marmoutier" ships even though the caution names it. Fix (engine): an output check for the four banned place-names in the caution. The caution is already plain. The voice did not follow it, and nothing caught it.
- **G3. Wrong place for a story (engine and record), Q6.** Fix:
  - Engine: grounding should check proper nouns of place in a story-tagged sentence against the story's own text. Shared words alone should not count as grounding.
  - Record: give `gallic.story.germanus-scruple-at-morning-service`'s `tellable_as` its place ("in Egypt"). Add the not_for "a claim that the scene took place at Marseilles". Today `tellable_as` names no place, so the voice filled one in from the conversation.

**P2**

- **Residue from removed quotes (engine).** `gallic.quote.receiving-christ-in-you` was offered and removed in five of six turns. Each time it left a stub ("taught the same meeting", "refresh Christ in guests"). Fix: the same item as LPC E1. A removal should take its announcement with it. Also narrow this quote's `retrieve_when`, so it stops being offered for every question.
- **Repetition (engine).** Q2 repeats Q1's hours passage. Q1, Q2 and Q4 repeat the Marseilles/Egypt sentence. Same as LPC R-1.
- **Paragraph length (engine and prompt).** Paragraphs of 8 to 10 sentences in Q4, Q5 and Q6. Same as LPC A1.
- **Unexplained terms (records).** "heretical pravity" and "remembrancer" come from `gallic.term.the-rule` and `gallic.term.commonitory-peregrinus`. Render them plainly there.

## Side by side: older (13 Oct) and new (29 Oct)

| Q | Older answer (13 Oct, older data) | New answer (29 Oct) | New vs older |
|---|---|---|---|
| 1 | Plain and short. It tells the Martin story but cuts it off: "he said he would not believe that Christ had come", with no condition. That reads as Martin refusing Christ. | Gives Martin's full condition in the placed quote, which is the better substance. But the lead-in says the same thing twice, and the turn is FK 12.9. | **Same.** One damage replaced by another. |
| 2 | The cross, the debt, the hours, "the least of these", "without him we can do nothing". Clear, on the question. | Similar content, plus the cloak. It repeats Q1 and carries a stub sentence. | **Same.** |
| 3 | "Merit", with two senses at Tours and Marseilles. Grounded in `gallic.term.merit`. One causal leap: "so the word carried both meanings at once". | "Humility", concrete and well grounded. One uncited stretch (the guest story as humility). | **Same.** Both sound. Each has one stretch. |
| 4 | Answers about Jesus. The Martin quote is pasted after "He laid it down himself and took it again:", where it does not belong. | Coherent and on Christ in the beggar. But it uses "Marmoutier", which the caution bars, and drifts from the humility question. | **Same.** A misplaced quote then. A caution breach now. |
| 5 | Cassian, with a list of fragments (twelve psalms, mill-wheel, two old men). It is loose but faithful. | Vincent, faithful, clearer as a portrait. Some archaic words and one stub. | **Same.** |
| 6 | The soldier who changed service. The trick at Tours and the monk kept inside the bishop. Faithful and vivid. | The grace argument held open, well. But it moves the Germanus story from Egypt to Marseilles. | **Worse.** The older answer had no factual error. The new one puts the world's key story in the wrong country. |

**Overall.** About the same as the older test, slightly worse. The new answers are more tightly tied to records. They place a quote correctly once, and they hold the grace question open in the world's own way. But they have three P1s, and the older six had two of a similar kind. The new kinds are a caution breach, a misplaced story and a damaged lead-in. What changed in the system between the two runs is not known to me. This compares only the text.

NEW: PASS 3, FAIL 3, NOT SCORED 0 of 6; versus older: better 0, same 5, worse 1
