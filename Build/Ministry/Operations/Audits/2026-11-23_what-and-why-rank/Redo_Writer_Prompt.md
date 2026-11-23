# What-and-why redo: writer (Opus)

You rewrite one Church Family Tree text so that every finding listed for it is resolved and the text meets the project's writing standard. Batch 1 of this work was undone because its texts read as generated: dramatic statements, hollow endings, and lines that told the listener what the sources do not say. Do not repeat it.

## Read first, in full

1. `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`: Part 1 (the standard), Part 2 (the shapes), and "The bar" in Part 4.
2. `Build/reference/method/Pass2-decisions/VR_1A_Writing_Standard_2026-08-09.md`.
3. Your packet: the text, where it shows on the site, its findings, and where its sources are.

## The rules this work adds

- **Explain it or leave it out** (Kit, Part 1). For each finding, say in plain words what the thing was and why it mattered to the people in it, from a source you open. If the sources you can find do not hold the answer, take the mention out and close the gap so the text reads whole. Never write a line saying the sources do not say, are silent, or did not survive, unless the absence is itself the story and the kit's "Where the doubt is itself the story, make it a scene" applies. A finding is not a reason to add a line about our sources.
- **No modern opinion in the text** (Mark, 2026-11-23). No modern scholar, editor, translator or "historians" is named or referred to. No guess or reconstruction is told as story. A source-bound modern work may support a fact without being named. List any modern work you take out of the text under Modern works, with every field read from a file in the repository, never from memory.
- **Never invent.** Every added fact, and every "so" or "because", points to a file and lines you opened.

## Faults that fail the piece on sight

- A closing line that sums up, draws a moral, or lands a point: "But this danger came and went — never constant, never empire-wide." "It was never settled." "The question remained open."
- A sentence that only says what is missing: "Corinth's own side is not preserved." "Neither blessing tells the story of the Last Supper." "The sources do not say why."
- Dashes used for drama, the "not X but Y" or "never X, never Y" turn, the colon reveal, and the "X did Y — but Z" twist.
- A pile of short claims in a row, each one a separate act, with no cause, contrast or time joining them.
- Stock words that sound generated: tapestry, testament to, pivotal, profound, shaped, forged, enduring, legacy as a closer, "in a world where", "it is worth noting", "real" used for emphasis ("real danger", "real command language").
- Reporting on the record in place of telling the story: "an account that survives only in", "one early manual", unless who tells it is the point and the kit's witness rules call for it.

## How it should read

The kit's voice: an adult documentary narrator, BBC or National Geographic. Sentences that link events by cause, contrast and time; none past about 25 words; no run of one-act sentences. The text should sound like the best of the tree's own briefs, not like a summary. Keep within about 15 percent of the present length unless the packet says otherwise. Keep every sentence that has no finding and no fault, word for word. Quotes stay word for word. American spelling outside quotes.

When it is written, save it to the path you are given and run `python -m engine.m1.profile_readability <that file>`. It must pass the limits (grade 10 and reading ease 60). If the grade is under 8, link the short sentences; never simplify the thought to move a score. Then read it once aloud in your head as a listener who has never heard of the subject, and fix whatever would lose them or talk down. Re-read it for the kit's four faults and the faults above.

## What you write

Two files, at the paths you are given:

1. The text alone, plain, a blank line between paragraphs.
2. A notes file:

```
## <piece key>
### Resolutions
- <finding>: explained / cut | <one sentence on what you did> | source: <file:lines, or "cut">
### Revised title
<only if the piece has a title that repeats something you cut; else leave out>
### Revised teaser
<the same, for a teaser>
### Modern works
<a JSON array of {title, author, year, publisher, url, note}, or []>
### Scorer
<the profile_readability line>
### Not resolved
<anything you could not resolve and why, or "none">
```

Do not edit any other file and do not commit.
