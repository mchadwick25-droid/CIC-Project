# Ignatius of Antioch: length cut after the revision

Ruling: Mark, 2026-11-27, "Batch 12: lengths measured by the draft" ("approve as recommended"): the draft is the measure, 675 words the ceiling. The revised draft ran 683 words.

## What was cut

The Neapolis sentence, which `Review.md` (Length note) names as what the heart does not need, since this ending does not use it. Source: Pol. 8, ANF 8854–8856 (`cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml`), re-read in the file: "because I must suddenly sail from Troas to Neapolis".

Deleted from the Troas paragraph:

> He could not write to every church, he told Polycarp, because he had to set sail suddenly, across the sea to Neapolis.

Added to `Outline.md`, Cut first, as item 8, marked Card, with its source.

## The join

No words were needed. The sentence closed its paragraph, so the paragraph now ends on the sentence before it, unchanged:

> News had come that the church at Antioch, which he had left in chains, was at peace and whole again, and he asked them to send a messenger to Syria to rejoice with it.

Every other sentence is word for word as it was.

## New count

- `wc -w`: 661 words (from 683), under the 675 ceiling. No further cut needed.
- `python -m engine.m1.profile_readability`: 661 words, grade 7.4 (names out 6.8), reading ease names out 81.0, 19.4 words a sentence, 0.9 joining words per 100, 15% short sentences, longest sentence 44 words - pass (note: grade 7.4 is under 8: the listener read checks it is not flat).
