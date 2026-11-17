# Review: Dhuoda brief

Brief reviewed: `dhuoda.brief.txt` (389 words). Bar: `2026-11-17_varied-batch/kit/Standard.md` and `Shapes.md` (Teacher or thinker).

## 1. Listener read (one pass, before the trace)

**Where I got lost or drifted.**
- Paragraph 2, "Bernard had the baby brought to him with the bishop of Uzès". On one hearing it is unclear whether the bishop is going with the baby or the baby is going to the bishop, and nothing says where the child went or why it mattered. I heard an event, not its meaning.
- Paragraph 2, "while William was sent to King Charles, to commend himself as his sworn man". The passive hides who sent him, and nothing says what hung on it. The listener gets no sense of why a mother would now be writing to a son at a king's court.
- Paragraph 3, first sentence: "which she dictated and had written out and sent, to be read as often as one looks in a mirror". The "and ... and ... and" chain blurs, and I briefly lost what "to be read" attached to.
- Paragraph 4, "while in 850 William was killed at Barcelona". "While" sets the two deaths up as a contrast that is not there; I waited for a point that never came.

**Children's-book or talking-down passages.** None. There is no run of short one-act sentences, no definition tacked on after a comma, and the one short sentence ("She worked on it for more than a year.") earns its place as a pivot. The register is adult throughout. The only weakness of this kind is the one noted above: in paragraph 2 two events are told without what was at stake.

## 2. Trace against the outline

Every sentence traces to `Outline.md`. Nothing from the Do not say list appears: no "snatched", no "exile" as fact, no "hostage", no age at the sending, no death date, no "beheaded", no motive for William's death, no "first woman writer in France" (said as the editor's claim), "dictated and had it written out" is kept.

- **Setting** (S2, S3, S6, S7): verbatim from the outline's spoken words. Good.
- **"in discord", because after ... Louis died ... his sons fought"**: the outline places the two side by side (S4, beats 2); her own prose ties the discords of the kingdom to the emperor's death (DH 2227–2230), so the "because" is supported.
- **Second son and the bishop** (beat 2, E4): correct, but drops "in Aquitaine". Not wrong.
- **"at my lord's command"** (E5): matches.
- **William sent to Charles** (beat 3, E7): matches, but drops the condition ("if Charles would grant the lands and offices held in Burgundy") and that Bernard sent him after the battle. Not wrong; it loses the stakes (Finding 1).
- **Book begun that November, dictated, handbook, mirror** (beat 4): matches. "That November" correctly follows "In 841". The board game is dropped; fine.
- **What it asks** (beat 5): a fair subset. Pilgrims and fair judging dropped; fine.
- **"a noblewoman, not one of the clergy"** (S7, Do not say line): matches.
- **"She worked on it for more than a year"** (beat 7, Do not say line): matches.
- **844 and 850** (beat 7, E19, E20): exact outline wording.
- **"The chronicles of her day name her husband and her son, but not her"** (Who tells it, line to say aloud): matches. **"no record tells when or where she died"** (E18): matches; uncertainty stated plainly.
- **Copies** (What came 1): "an early copy, now in fragments, agrees with a later one, scholars could show the text is hers". Matches; no century claimed.
- **Benedictines** (What came 2): matches.
- **1887** (What came 4): said as the editor's claim. Matches.
- **1923** (What came 5): matches.

No added feeling, weather or thought. The "But" in "but before the child was baptized" leans slightly toward a grievance the outline says she never voices (Finding 2).

**Quotes re-checked word for word against `cic/texts/dhuoda_liber-manualis_bondurand1887.txt`:**
- Q1 (DH 1893–1899): source Latin present as cited. The brief uses the outline's first two sentences of the rendering exactly.
- Q3 (DH 3168–3171): source Latin present as cited. The brief's text matches the outline's rendering exactly.
- "in discord" (DH 2078–2080, "Licet sit discors regni et patriae"): present.
- "a respectable monument of literature and piety" (DH 348–351, "Un monument respectable de literature et de piété"): present; fair translation.
- Bondurand's 1887 claim (DH 1854–1857): present; paraphrased as his claim.
- "the manual of Dhuoda" (`council-of-trent_roman-catechism_mchugh-callan1923.txt` 812–830): present, with the Luther claim at 813–815.

All quotes verified.

## 3. Score

`python -m engine.m1.profile_readability` : 389 words, grade 8.1 (names out 7.5), reading ease 77.5, 20.5 words a sentence, 0% short sentences, longest sentence 28 words — pass. Inside the limits and at the floor of the 8–9 aim; the listener read confirms the low score is not a list of short acts.

| Dimension | Score | Reason |
|---|---|---|
| **voice** | 4 | Adult documentary register throughout; never talks down; ideas linked by cause and contrast ("because", "yet", "while"). Docked for the passive "was sent" and the stacked "and ... and" clause, and one misused "while". |
| **craft** | 3 | Strong hook in her own voice; setting in the first sentence; ends on an event from the record. But paragraph 2 tells two events (the baby taken, William sent) with no sense of what hung on them, and the impact section is about a quarter of the story, a little under the third asked for. |
| **rigor** | 5 | Every sentence traces; two short quotes, not quote-driven; witnesses named only where needed (Benedictines, the editor, the translators); her death stated plainly as unrecorded. |
| **accessibility** | 4 | Followable on one hearing overall, grade 8.1. The bishop clause and the paragraph 3 opener each cost a moment. |

## 4. Verdict: PASS

Nothing is wrong, unsupported, misquoted or past a limit; nothing lost the listener outright; nothing reads as a children's book; the shape is Teacher or thinker, not a martyr arc. The findings below are MINOR.

## 5. Findings

1. **MINOR — paragraph 2, William sent to Charles: stakes missing.** The sentence gives the act but not what it meant. **Change:** make Bernard the subject and carry the condition the outline holds, for example: "After the battle of 841, Bernard sent William to King Charles, to commend himself as his sworn man if Charles would grant the lands and offices held in Burgundy." This also gives the listener the reason the book is addressed to a son at a king's court.
2. **MINOR — paragraph 2, the baby and the bishop.** "Bernard had the baby brought to him with the bishop of Uzès" is ambiguous on one hearing, and the preceding "but" hints at a grievance she never states. **Change:** use the outline's place and order: "Before the child was baptized, Bernard had him brought to him in Aquitaine, together with the bishop of Uzès." Drop the "but".
3. **MINOR — paragraph 3, first sentence.** "which she dictated and had written out and sent, to be read as often as one looks in a mirror" stacks three verbs and leaves "to be read" loosely attached. **Change:** split the handbook-as-mirror image from the dictation, e.g. "...she began a book for William, which she dictated and had written out. She called it a handbook, to be read as often as one looks in a mirror."
4. **MINOR — paragraph 4, "while in 850".** "While" implies a contrast between the two deaths that is not there. **Change:** "In 850 William was killed at Barcelona" as its own clause or sentence, joined by time, not contrast.
5. **MINOR — balance of impact.** "What came of them" is about 90 of 389 words. If Findings 1–3 add words, take them from the list of what the book asks (paragraph 3), not from the closing paragraph.

No BLOCKING findings, so no new Do not say entries.
