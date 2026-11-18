# Card edits: Macrina the Younger (batch 4)

Base: the census card for `macrina-the-younger` in `cic-website/data/world-census.json`. Everything not listed here is kept word for word. Brief: `macrina-the-younger.brief.txt` (370 words; no `briefLength` in the card, as the census allows none).

## New

1. **sources.about**: added Louis Petit, *Documents relatifs au concile de Florence, I: La question du purgatoire à Ferrare*, Patrologia Orientalis 15, 1927 (`cic/texts/patrologia-orientalis-tomus15_petit-documents-concile-de-florence-purgatoire-grc-fra_graffin-nau1927.txt`). The brief's Ferrara paragraph rests on it, and the card's Ferrara reference already cited "Petit" with no source behind it. Re-read: lines 2304-2306 (Macrinam loquentem), 8681-8688 (Homo erat), 10731-10734, 10758-10760 (frater erat Basilii magni beataeque Macrinae).
2. **briefReferences**, after the betrothal reference: "Life (Clarke, line 132): her resolve not to be separated from her mother." Brief: "She would not leave her mother." LIFE 132: "a resolve not to be separated from her mother even for a moment".
3. **briefReferences**, after the mother reference: "Life (Clarke, line 158): to them this round of prayer meant work, and work so called was rest." Brief: "For them, Gregory says, this prayer was their work, and what others call work was rest." LIFE 158.
4. **briefReferences**, after the Peter reference: "Life (Clarke, line 160): the life of the house grew with the lapse of time." Brief: "Over the years their house grew into one community". LIFE 160: "with the lapse of time their successes increased".
5. **briefReferences**, same place: "Life (Clarke, lines 274, 276): Vestiana, widowed while still young, chose Macrina as guardian of her widowhood." Brief: "a young widow came to live under her care". LIFE 274, 276.
6. **briefReferences**, after the dying-prayer reference: "Life (Clarke, lines 232, 234): her voice failed, she finished the evening thanksgiving in her heart and by moving her hands, and closed her life and her prayer together." Brief's last sentence. LIFE 232, 234.
7. **briefReferences**, after the dialogue reference: "Life (Clarke, lines 184-346): Gregory's own account of her last days, death and burial, the witness for almost all we know of her; Clarke's note (line 412): in the dialogue Gregory purports to reproduce their talk." Brief: "Almost all we know of her comes from her brother Gregory, who sat with her as she died, and how much of the teaching is hers, no one can say." LIFE 184-346; LIFE 412.

## Clearly wrong (contradicts the finished brief)

8. **quotationOriginals**: removed the Lampadia entry ("Here is the cloak, here is the head-covering, and the worn-out shoes on her feet. This is her wealth."). The brief no longer quotes it.
9. **briefReferences**: removed "Life (Clarke, lines 278, 284; Greek, PG 46): Lampadia, the deaconess, on her wealth." The brief no longer tells it.
10. **briefReferences**: removed "Life (Clarke, lines 64, 108, 402): written a few years after her death, as Clarke dates it." The brief no longer says when the Life was written.
11. **briefReferences**: removed "Clarke's introduction (line 84): the Life as a light on how such a community was run." The brief no longer says it.

## Kept

- **quotationOriginals**: one entry, the dying prayer. The brief's spans ("You, Lord," / "have set us free from the fear of death.") join to the census entry's modern words, and its source (PG 46, lines 71687-71690) is unchanged, so its `secondReading` ("same") is copied. Re-read: line 71687 and the Greek on line 71690 (OCR φόθον, as the entry notes); Clarke LIFE 230.
- Awaiting second reading: none (no new or changed span).
- All other references re-read against the brief and kept: LIFE 184, 192; the census setting; LIFE 124, 128; LIFE 138, 158; LIFE 164, 264, 356; Clarke LIFE 52; LIFE 230; LIFE 196 with the dialogue; Ferrara.

## Not found

None.


## Card check fixes applied verbatim, 2026-11-18

- `briefReferences[0]`: "on the floor" removed.
- `[2]`: "betrothed at twelve" became "the match her father planned".
- `[9]`: "Basil's death and" removed.
- `[11]`: "and by moving her hands" removed.
- `[13]`: lines 184-346 became 184-234; "death and burial" became "and death".
- `quotationOriginals[0].printed`: φόβον became φόθον (the printed OCR form).
