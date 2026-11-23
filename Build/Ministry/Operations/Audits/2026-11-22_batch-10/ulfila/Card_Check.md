# Card check: Ulfila

Checked `ulfila.card.json` against `Card.existing.json`, `Card_Edits.md`, `ulfila.brief.txt`, `Outline.md` and the cited files.

## Verdict: FIX (one change)

### Fix 1: what the outline sends to the card, not carried

- **Field:** `keyWorks[0].about`
- **Old:** `the Gospels survive in part in the Codex Argenteus at Uppsala, written in silver and gold on purple parchment`
- **New:** `the Gospels survive in part in the Codex Argenteus at Uppsala, written in the fifth or sixth century in silver and gold on purple parchment`
- **Evidence:** Outline cut list item 11 sends "the Codex Argenteus's description (silver and gold on purple, fifth or sixth century)" to the card; outline Do not say (line 92) relies on the date to keep the codex from reading as Ulfila's own copy. STR 1352: "Geschrieben im 5./6. Jh. mit Silber- und Goldbuchstaben auf purpurgefärbtem Pergament". Every other "To the card" item in the cut list and every "Card" item under Leave out and For the card is on the card. `Card_Edits.md` should list this edit under New.

## Checks that pass

1. **Edits justified.** The four `quotationOriginals`, ten `briefReferences`, four `legacy.traces`, seven `uncertain` and two `sources.about` additions were each read against their cited lines (AUX 15273-15277, 15310, 15324, 15209-15223, 15290-15302, 3733-3762; STR 836-842, 886, 902, 1290-1297, 1322-1339; NP2 34560-34568, 9604-9609, 14446-14460, 16695-16706, 40186-40200; PHI 120; THD 15298-15324; JOR 3286-3297, line 57 for 551). Each holds.
2. **Nothing else moved.** Every existing field is word for word; `legacy`, `uncertain` and `sources` lists are the existing items in order, with appends only.
3. **briefReferences.** Each names what the brief tells; none for a dropped matter. No quotation marks.
4. **Census rules.** Keys all in `CARD_KEYS` and `QUOTATION_ORIGINAL_KEYS`; no `briefLength`. Four quoted spans in the brief, four entries. Each `printed` is verbatim at its lines (Q1 omits only the margin junk after "suum"; the "substance" entry spans a page-break tag). Every cited file is in `sources`. No audit named; American spelling. Q1's OCR original is confirmed by Streitberg's print, and the dependence is stated in `uncertain`.
5. **"Checked at card".** "substance" matches Sozomen's English; "alone unbegotten" renders solum ingenitum. Both correct.
6. **Not found / clearly wrong.** None listed; none found. Sozomen's burnings are told as his reports.
7. **Census entry.** None (entry exists).

Note, no change required: outline cut item 1 sends Sozomen's tribute "whole"; the card's `legacy.remembered` already carries its substance in Hartranft's held English.
