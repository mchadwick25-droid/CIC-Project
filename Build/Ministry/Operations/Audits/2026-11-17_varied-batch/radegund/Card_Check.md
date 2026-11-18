# Card check: Radegund

New card: `radegund.card.json` (this folder). Old card: `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch4/radegund.card.json`. Checked against `Source_Sheet.md` and the cited source files. Bar: `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Process.md`.

**Verdict: FIX**

## BLOCKING

B1. **`legacy.traces[2]` gives Gregory a detail he does not tell.** The card says: "Gregory of Tours tells how she sent to the East, with King Sigibert's letters, for wood of the Cross, and how the emperor sent it, set in gold." Gregory's account (History IX.40, `cic/texts/gregory-tours_history-of-the-franks-v2_dalton1927.txt` 19598–19607) says only that her clerics went east with Sigibert's letters and "duly returned with the relics". He names no emperor and no gold. The emperor and the gold come from Baudonivia ("the emperor sent the Cross adorned with gold and gems", sheet L16, VR-B 30246–30256) and from Dalton's note (DAL 29576–29578). The brief reference already credits Baudonivia correctly; the card misattributes it.
Correction, replace the second sentence of `legacy.traces[2]` with: "Gregory of Tours tells how she sent to the East, with King Sigibert's letters, for wood of the Cross; Baudonivia says the emperor sent it adorned with gold and gems."

## Checked and sound

- Quotation 1 (Life I.12), `fredegar-liber-historiae-francorum-vitae-mgh-srm-2-lat_krusch1888.txt` 28806 and 28808 (28807 blank): "Si me consecrare distuleris et plus hominem quam Deum / timueris, de manu tua, pastor*, ovis anima requiratur". Verbatim apart from the OCR mark. Modern wording matches the brief exactly.
- Quotation 2 (her letter, IX.42): printed DAL 19878–19879, "And since I cannot in person throw myself at your feet, I make prostration vicariously through this letter". Verbatim. Latin GRL 31516–31517 confirmed. Modern wording matches the brief (the brief splits it around "she wrote").
- Quotation 3 (X.16): DAL 21416–21418, "she had not introduced any new usage, but had continued the custom of the lady Radegund". Verbatim. Modern wording matches the brief.
- Dates: 13 August, the twelfth year of Childebert, 587 as the editors' reckoning, Dalton's "About A. D. 531" (sheet S2, S5, D8). Supported.
- Athies, the bishop of the city in her letter, the forty or more nuns, the abbess reading the letter and sending copies (DAL 19821–19824), the two hundred nuns at the bier, Gregory burying her in Maroveus's absence, Helena (Gregory and Baudonivia), the lamp and "from then on I preached", the relic still at Poitiers in Dalton's day, Fortunatus's damaged line and his poem to Justin and Sophia. All match the sheet.
- New uncertainties ("directa a rege", "a nun rather than a queen", who refused the Cross, the greeting, praise from inside) match sheet D3–D7.
- Card agrees with the brief.

## Not blocking

- `dates` says 13 August is given "by Gregory of Tours and Baudonivia". Gregory's own words are "the thirteenth day of the sixth month" (DAL 17577); "August" is Dalton's note. The sheet marks the day and month Documented, so this stands, but "by Baudonivia, and by Gregory's thirteenth day of the sixth month" would be more exact.

## Recheck

B1: `legacy.traces[2]` now reads "Gregory of Tours tells how she sent to the East, with King Sigibert's letters, for wood of the Cross; Baudonivia says the emperor sent it adorned with gold and gems." This agrees with DAL 19598–19607 and sheet L16 (VR-B 30246–30256). The rest of the entry is unchanged. The JSON is valid.

**Recheck: PASS**
