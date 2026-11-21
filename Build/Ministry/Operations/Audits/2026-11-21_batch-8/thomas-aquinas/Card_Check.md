# Card check: Thomas Aquinas

Card checker, batch 8 (2026-11-21), under `Card_Check_Prompt.md`. Read: `thomas-aquinas.brief.txt` (and `brief.v1.txt`, to see what the final brief dropped), `thomas-aquinas.card.json`, `Card_Edits.md`, and each quoted line in its file. There is no starting card: Thomas has no census entry yet.

**Verdict: FIX** (four changes below).

## 1. Each field is justified

Every field was checked against the evidence `Card_Edits.md` gives. Spot re-reads:
- uncertain[12], the road to Lyon: the live `bonaventure` entry does say "In 1273 Pope Gregory X named him a cardinal and bishop of Albano", so the oddity the card states is real. It stands.
- uncertain[9], the end of the writing: Bartholomew's "Raynalde, non possum: quia omnià, qua seripsi, videntur mihi palez" (ASM 187860-187861) and the secret added to Reginald, "Omnia, qu: scripsi, videntur mihi paleee respectu eorum, quie vidi et revelata sunt mihi" (ASM 187886-187888). It stands.

## 2. Nothing else moved

Not applicable: new card, no starting card, no existing entry. The card does not contradict the tradition entry `the-dominican-order`.

## 3. References

The final brief dropped "Others finished it from his earlier books", the burning brand, the carrying to Fossanova and the miracles John XXII asked for. The references no longer name the last three. One still names the Supplement, and one names a detail the brief never told.

**FIX 2.** `briefReferences[3]`
- Old: "Bollandists and Tocco: the counts of Aquino, born at the start of 1225 by Tocco's age; Naples, and entry into the Dominicans."
- New: "Bollandists and Tocco: the counts of Aquino, born around 1225 by Tocco's age; Naples, and entry into the Dominicans."
- Why: the brief says "born around 1225", not at the start of the year.

**FIX 3.** `briefReferences[9]`
- Old: "Leonine edition: the third part breaks off at question 90 on the parts of penance, where the Supplement begins."
- New: "Leonine edition: the third part breaks off at question 90 on the parts of penance."
- Why: the final brief no longer tells that others finished it.

References kept as they stand: [0], [1], [2], [4], [5], [6], [7], [8]. [8] carries one followeth Duns, another St Thomas without quotation marks; those words stand verbatim in the brief, so marks would also be allowed.

## 4. Census rules

Only allowed keys; no `briefLength`. The brief has four quoted spans (paragraphs 1, 11, 13 and 17); the card has four entries, each `modern` word for word as the brief has it. Each `printed` stands at its lines: ST4 5807-5809, ST4 4099-4104 (the "^"" after vero is a note mark), ASM 187860, TYN 11872 (the note figures 4 and 5 are as the page prints them). Every cited file is in `sources`. No quotation marks in `briefReferences`. No audit, review or ruling named. All four spans are six words or more (Tyndale's is exactly six) and carry no `secondReading` yet, as the new-card prompt asks.

**FIX 4. American spelling.** `sources.about[11].title`
- Old: "Opera omnia (Patrologia Graeca 160), with the editors' catalogue of Greek versions of Thomas"
- New: "Opera omnia (Patrologia Graeca 160), with the editors' catalog of Greek versions of Thomas"

## 5. Originals

**FIX 1. `quotationOriginals[0]`, the case against God.** The card prints only the last three sentences, saying the first lines have "stray marks and a misprint". On re-reading, there is no misprint. The three faults are all marks set into the line, which the batch 6 ruling allows as plainly no part of the text:

| ST4 line | Scan | Reads | Kind |
|---|---|---|---|
| 5801 | `*rum` | `rum` (with "contrario-" at 5799: contrariorum) | stray mark run into the word |
| 5803 | `jaliud` | `aliud` | OCR set the edition's margin letter into the line |
| 5805 | `P  mine` | `mine` (with "no-" at 5803: nomine) | OCR set the edition's margin letter into the line |

"scilicet'^" (5805) and the quotation mark after "destruetur" (5801) fold away. Every word of the objection then stands clean.
- `printed` old: "Si ergo Deus esset, nullum malum inveniretur. Invenitur autem malum in mundo. Ergo Deus non est."
- `printed` new: "Videtur quod Deus non sit. Quia si unum contrariorum fuerit infinitum, totaliter destruetur aliud. Sed hoc intelligitur in hoc nomine Deus, scilicet quod sit quoddam bonum infinitum. Si ergo Deus esset, nullum malum inveniretur. Invenitur autem malum in mundo. Ergo Deus non est."
- `work` old: "Summa theologiae I, question 2, article 3, first objection, Latin of the Leonine edition (the last three sentences)"
- `work` new: "Summa theologiae I, question 2, article 3, first objection, Latin of the Leonine edition"
- `lines` old: "5807-5809"; new: "5797-5809"
- `uncertain` old: "The rendering follows the whole objection in Latin (lines 5797-5809). In the first lines of the Latin the scan has stray marks and a misprint in contrariorum, aliud and nomine, which no second print of this part of the Summa confirms, so only the last three sentences are printed. No English of the Summa is held."
- `uncertain` new: "In the first lines the scan sets stray marks into contrariorum, aliud and nomine; they are no part of the text. Good without limit renders bonum infinitum. No English of the Summa is held."
- The three readings go to `tools/quote_scan_readings.json` for `cic/texts/thomas-aquinas_opera-omnia-t4-summa-theologiae-lat_leonine1888.txt`.

**Reginald, I cannot: no change.** Three held copies of the straw words exist: ASM 187861 ("omnià, qua seripsi, ... palez"), ASM 187887 ("Omnia, qu: scripsi, ... paleee") and the 1735 print, ASM35 117763-117764 ("omnia, quxfcripfi, videntur mihipalcx"; `Card_Edits.md` gives 117761-117762, which are blank and page furniture). Together they give omnia and scripsi cleanly. None prints quae or paleae cleanly, so under the ruling the card rightly prints only "Raynalde, non possum", which is clean.

**Faith and reason, and Tyndale: no change.** Both are printed in their original language and are clean.

## 6. Not found, and anything clearly wrong left in

The four searches that found nothing are rulings of absence, and the card states each as not held: the Summa in English, a date for the title Angelic Doctor, the year he began the Summa, and a source giving the reason for the seizure (uncertain[2] says so). Ruling: no change. Walter's 1318 for the canonization is kept and marked as against every other held source, which is right. Nothing in the card is clearly wrong.
