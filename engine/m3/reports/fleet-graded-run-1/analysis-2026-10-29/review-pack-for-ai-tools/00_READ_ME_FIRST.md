# Independent review pack: "Church in Conversation" fleet test, run 1

You are being asked to act as an outside specialist reviewer. This pack is self-contained. You do not need access to any other system.

## 1. What this is

"Church in Conversation" is a project that lets a person talk with a **representative** of a historical Christian community, for example the Donatist church of North Africa or the Reformed city of Geneva. The representative is an AI voice. It is supposed to speak from inside the community, in the first person, using only a curated set of that community's own records and sources, and to stay inside the community's time window. It must not invent, must say plainly what it does not know, and must be clear and readable to a general adult reader.

In this test, **12 worlds** each answered the **same 28 questions** (file 02). The answers are in the `worlds/` folder, one file per world. The worlds and their time windows are in file 01.

These answers were produced by a test harness, not by the finished product. Some sentences may have been removed by an automatic step, which can leave a dangling "he", "so" or "that" with nothing before it. Some raw system tags such as `[[thin:liturgy]]` or build words such as "this turn" or "the records I am holding" may also appear. Report these as defects (section 5) but keep them apart from your judgment of historical accuracy.

## 2. What we want from you

For every answer, judge two things.

**A. Rigor (accuracy and context).** The standard is **scholarly acceptability, not perfection.** Would a competent historian of this period and tradition let this stand in a textbook or a museum panel?
- **SOUND**: accurate and in context; honest about uncertainty.
- **ACCEPTABLE**: a small imprecision, thin coverage, a loose generalisation, or an omission, but nothing misleading.
- **NOT ACCEPTABLE**: a specialist would object. Use only for: a factual error; an invention (a person, text, place, event or attribution that does not exist); an anachronism (knowledge from after the world's window); a quotation used against its context or given to the wrong person; a contested question stated as settled; a **false silence** (see below); or an answer to a different question than the one asked.

**B. Access and craft.** Grade each of these GOOD, FAIR or POOR.
- **Readable**: plain adult English; sentences mostly 12 to 20 words, none past about 30; no unexplained jargon.
- **Understandable**: a non-specialist could follow it unaided. POOR if there are dangling pronouns or connectives, announced points never made, raw tags, or the voice talks about its own records, evidence or "this turn".
- **Succinct**: the length fits the question. POOR if it is padded, repeats itself, lectures, or pastes in material the question did not ask for. Good answers are often 120 to 260 words, but judge against the question.

**Overall call per answer:** SHIP (rigor is SOUND or ACCEPTABLE and nothing is POOR), FIX (rigor is fine but something is POOR), or BLOCK (rigor is NOT ACCEPTABLE).

## 3. The most important thing to look for: false silence

The representative often says that no source, record or voice exists on a topic, or that "we never said" something, when the period's sources do say it. An example from outside this test, to show the kind of error: a representative from seventh-century Ireland who says no Christian text survives from his own country, when Muirchu's Life of Patrick and Adomnan's Life of Columba both do.

A representative is allowed to say "our records do not hold this" or "I cannot recall a saying on this". It is **not** allowed to say "no such source exists" unless that is true of the whole period. If an answer claims an absence, check it. Name the source that contradicts it, or say you could not find one.

## 4. How to work

1. Read file 01 (worlds and windows) and file 02 (questions). **Use the window given for each world.** Anything after the end year is outside what the community can know. Anything inside it is fair, even if later scholarship named it.
2. Review **one world at a time**, in a fresh session if your tool has limited memory. Give your tool this README plus that world's file from `worlds/`.
3. For each answer: check each factual claim and each quotation from your own knowledge. If your tool can search the web, use it for claims you doubt and say you did.
4. Be fair. Credit what is right. Do not mark an answer NOT ACCEPTABLE for style alone, and do not mark it down for being brief and honest.
5. **Do not guess.** If you are unsure, write "unverified" and grade ACCEPTABLE, not NOT ACCEPTABLE. Never invent a source, a page number or a quotation yourself. Name a primary text or standard scholarship for a correction only when you are confident of it.
6. Do not ask for, or look at, our own grades (file 99) until you have finished.

## 5. Defects to log separately from rigor

Count and quote these where you see them: (a) dangling pronoun or connective with nothing before it; (b) an announced teaching never given; (c) raw tags such as `[[thin:...]]`; (d) build or system talk such as "this turn", "the ground given", "the records I am holding", "vendored", "I am a representative of..."; (e) chatbot phrasing such as "The short answer first. Yes."; (f) whole paragraphs reused word for word across answers; (g) stray characters.

## 6. Output format

For each world, return a table, then a short summary.

| Answer | Rigor | Readable | Understandable | Succinct | Overall | Doubted claim, and what the sources say | Defects (section 5) |
|---|---|---|---|---|---|---|---|

Then:
- Counts of SHIP, FIX and BLOCK.
- The three most serious rigor problems, each with the exact words from the answer and the correction.
- The recurring access or craft problems.
- One paragraph: would you put your name to this world's answers if the problems you named were fixed? What is the single biggest change?
- A line saying whether you used web search and which claims you could not verify.

If your tool can return structured data, also give JSON: `{"world":"...","answers":[{"n":1,"rigor":"SOUND|ACCEPTABLE|NOT ACCEPTABLE","readable":"GOOD|FAIR|POOR","understandable":"GOOD|FAIR|POOR","succinct":"GOOD|FAIR|POOR","overall":"SHIP|FIX|BLOCK","doubted":[{"claim":"exact words","problem":"...","source":"..."}],"defects":["..."]}],"summary":"..."}`

## 7. Pack contents

- `00_READ_ME_FIRST.md` this file
- `01_WORLDS.md` the twelve worlds, with windows
- `02_QUESTIONS.md` the 28 questions
- `worlds/<code>.md` 28 answers per world (lpc, gallic, desert, ijc, alx, witt, rzg, pahc, hal, syr, cappadocian, don)
- `99_OUR_GRADES_key_do_not_share_first.md` our own verdicts, for comparison after your review

## 8. Known limits of this pack

- Time windows come from each world's own definition record. They are the project's choice, not a settled scholarly boundary. Flag a window you think is wrong, but grade against the stated one.
- The "community" is a reconstruction from a curated source set. An answer may be accurate to the sources and still miss the wider period; judge the wider period.
- The answers come from one test run and are not the final product.
