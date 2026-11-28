# Card check applied: Valentinus

All changes applied to `valentinus.card.json` by exact text replacement; nothing else changed.

1. `timeline[0].lines[2].text`: gloss added ("that of people who claimed a special knowledge"). Applied.
2. `timeline[5].lines[0].text`: new two-sentence text. Applied.
3. `timeline[3].lines[4].text` and `legacy.remembered[5]`: ", a name for God's Son" added to both. Applied. `timeline[3].lines[4].reference`: Prescription 13 reference added after the existing one. Applied.
4. `timeline[5].lines[3].reference`: Jerome, Lives of Illustrious Men 53 added. Applied.
5. `timeline[6].lines[0].reference`: file, entry and fields added. Applied.
6. `briefSources[0].title`: "Books 2, 4, 5 and 7". Applied.
7. `uncertain[1]`: two sentences inserted after "...is of Ptolemy's school." Applied. `sources.about[0].title`: "chapters 6, 10 and 11". Applied. `Card_Edits.md`, Conflicts and not found: the "not carried" line now says the claim is found at IR 30758-30763 (Against Heresies I.6.2) and is carried in `uncertain[1]`. Applied.

The card check gives no entry-field changes, so no "Entry fields (card check)" section was added.

Not applied: none.

JSON check: `python -m json.tool valentinus.card.json` passed.

Readability: `python -m engine.m1.profile_readability` on the card's running text (text fields only; references, sources, quotations and keys left out; extracted outside the repository, since Card_Edits.md does not state the extraction): 2569 words, grade 8.5 (names out 6.3), reading ease names out 78.7, 16.1 words a sentence, longest sentence 57 words - pass.
