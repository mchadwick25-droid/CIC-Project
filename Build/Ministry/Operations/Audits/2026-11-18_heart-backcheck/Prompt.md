# Heart check prompt (batches 1 and 2)

You are a fresh, independent reader for the Church Family Tree, a set of short spoken stories about people and councils in church history. Each story is heard, read by a narrator. The writing standard now requires **the heart of the life in the first minute**: the person's major contributions, the essence of their work, and why they are on the tree. It is not a headline, and it is not "how we know". This story was written before that rule.

Piece: `{SLUG}`. Folder: `{FOLDER}`. The first minute is about **{WORDS} words**.

## Read, in this order
1. The census entry `{SLUG}` in `cic-website/data/world-census.json` (`knownFor`, `card` or `council`, and NOT `longDescription` yet). {CENSUS_NOTE}
2. `{FOLDER}/Source_Sheet.md`, then `{FOLDER}/Outline.md`.

Do NOT read Review*.md, Recheck*.md, OneHearing_Test*.md, Fixes_R50.md, Card_*.md, Second_Readings.md, or any other `.brief.*` file. Do not edit any file except the one you write.

## Step 1: write the heart before you hear the story
In two or three sentences, say the heart of this life: what they did, what it changed, and why they are on the tree. Write it from the census card and the source sheet, not from the outline's own framing. Batch 3 showed that outlines can aim at how-we-know instead of substance. Then say what the sources hold for each part, with the project's confidence levels (Documented / Widely Accepted / Dominant Modern Reconstruction / Contested / Inferential-Thin). If something central to why this person matters is missing from the source sheet and the outline, say so plainly. That makes it FIX-OUTLINE.

## Step 2: hear the story once
The story is `{TEXT_SOURCE}`. Count words. Give what the first {WORDS} words carry, by word range. Does the heart land there, in full, in part, or not at all? Give the word number where each part of the heart first arrives. Is the heart given its weight later, or passed in one clause? Where does the time go: scene, witnesses and how-we-know, procedure?

## Step 3: verdict
Give one of these:
- **PASS**: the heart is in the first minute.
- **FIX**: the material is in the outline and sources, but the story doesn't put it in the first minute.
- **FIX-OUTLINE**: the outline itself lacks the heart, so research comes first.

For FIX, list what is missing from the first minute and what in the outline can carry it, with no new claims. Never invent. A story's fierce or strange historical moments are design, not faults.

## Output
Write `Build/Ministry/Operations/Audits/2026-11-18_heart-backcheck/{SLUG}/Heart_Test.md`, headed `# Heart test: <name>`. Then a line saying what you read and did not read, then sections 1 to 3 as above. Plain, short sentences. Reply with one line: the verdict, plus the missing part in under 25 words.
