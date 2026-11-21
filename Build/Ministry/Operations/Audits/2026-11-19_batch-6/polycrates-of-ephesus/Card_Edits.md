# Card edits: Polycrates of Ephesus

2026-11-19. The existing card is the census `card` for `polycrates-of-ephesus` (folder copy `Card.existing.json`). Every existing field is kept word for word, in its order; `polycrates-of-ephesus.card.json` adds two keys after them, `briefReferences` and `quotationOriginals`. The brief was not changed. Short names follow `Source_Sheet.md`: **EUS** = `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` (EUS-ed = McGiffert's notes), **HEF** = `cic/texts/hefele_history-of-the-councils-v1-to-nicaea_clark1872.txt`, **SOC** = `cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml`, **HIPP** = `cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml`, **COUN** = `cic/texts/npnf214_seven-ecumenical-councils.xml`.

Keys used: only those `tools/validate-census.mjs` allows (CARD_KEYS, QUOTATION_ORIGINAL_KEYS). No `briefLength`, `label`, `secondReading` or connections.

## New

**briefReferences.** Twelve lines, one for each source the brief rests on, each re-read at its lines. No quotation marks.
1. Letter, V.24.2–8: EUS 31324–31413 (sheet L1–L6, E2, E4).
2. V.23, the two customs and the synods: EUS 31136–31140, 31216–31222, 31224–31301 (S4, E1).
3. V.24.1: EUS 31310–31316 (E3).
4. V.24.9–11, Victor and the objectors: EUS 31415–31419, 31431–31441 (E5, E6).
5. Whether the break took hold: EUS-ed 31419–31429, 31185–31187; SOC 16226–16228; HEF 20370–20377 (D1, E8).
6. III.31: EUS 19072–19079 (I1).
7. Later readers: Abelard 130335–130344, Smith 1936–1940, Synaxaristes 12048–12056 (I1).
8. Hippolytus VIII.11: HIPP 13064–13075 (I2).
9. Life of Constantine III.18 (chapter heading EUS 64601–64603): EUS 64606–64609 (I2).
10. Antioch canon 1: COUN 9438–9449 (I2).
11. His death not known: EUS-ed 31099–31101 (chap. 22, note 9); no early source on it (E8).
12. Census tradition entry `post-apostolic-house-church`, region and modern countries (S1).

**quotationOriginals.** One entry for each of the brief's two quoted spans; the outline's optional Quote 3 is not in the brief and has no entry. Each `modern` is the brief's span exactly; each `printed` was re-read and stands verbatim in EUS at its lines (tags aside; the printed curly quotes kept). Eusebius's Greek of Book V is not held as a clean text, so no `original` is given. The existing card had no `quotationOriginals`, so no `secondReading` could be copied.

## Clearly wrong

None. Each existing statement was checked against the sheet and its lines (EUS-ed 31094–31123, 19096–19110, 19154–19167, 31185–31187, 31241–31247, 31419–31429; JER 40413–40416; SOC 16226–16228; HEF 20370–20377) and against the brief. No held source and no sentence of the brief contradicts any of them.

## Not found

Nothing. Every existing claim was found at the lines above.

## Quoted spans, awaiting second reading

| # | Modern (the brief) | Printed |
|---|---|---|
| 1 | We keep the day exactly, neither adding nor taking away. For in Asia, too, great lights have fallen asleep. | EUS 31324–31326 |
| 2 | So, brothers, I have lived sixty-five years in the Lord. I have met the brothers all over the world, and I have gone through all of holy Scripture. I am not frightened by what is said to terrify us. For those greater than I have said, 'We must obey God rather than human beings.' | EUS 31396–31400 |

Both are awaiting second reading. Points from the outline (Quote 2) for that reading: "us" follows the ANF8 English (`anf08_…xml` 72621–72622) and Jerome's Latin "qui nobis minantur", where the Greek leaves it unstated; "human beings" renders ἀνθρώποις, where McGiffert has "man".

## Outside the card

`sources` was not expanded. The brief also rests on Hippolytus, the Life of Constantine, the Antioch canon and the later readers, which the card's `sources` do not list; they stand in `briefReferences` only. Once the brief becomes the entry's `longDescription`, its two quotations are renderings, not printed words, and may need listing in `tools/quote_renderings.json`.
