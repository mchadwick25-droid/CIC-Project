# Card apply, batch 9

Each change is from the folder's `Card_Check.md`, applied word for word to `<slug>.card.json` (indent 2, valid JSON).

## apollinaris-of-laodicea
- `quotationOriginals[3].uncertain`: "epitithesin" to "epititheasi".

## basil-of-caesarea
- `legacy.traces[6]`: "defence" to "defense" (both places).
- `uncertain[0]`: "self-defence" to "self-defense".
- `briefReferences[0]`: "self-defence" to "self-defense".
- `briefReferences[9]`: Sozomen 6.34 sentence removed; "World census, Cappadocian Christianity: his tradition." remains.

## cyril-of-jerusalem
- `legacy.traces[5]`: "first lecture" to "Procatechesis".
- `uncertain[13]`: "the priesthood" to "the bishop's office".

## damasus-of-rome
- `knownFor`: "clubs and swords" to "deadly violence".
- `quotationOriginals[0]`: added `original`, `originalFile`, `originalLines` (before `uncertain`, the order other cards use).
- Same entry, `uncertain`: "42056-42058" to "42058-42060"; "The English print stands alone." to "The Latin is printed with Romanae as Mansi reads it."
- `sources.about`: Mansi entry appended.
- `briefReferences[6]`: Theodoret sentence removed.
- `uncertain[15]`: "The sources give no reason" to "The Liber Pontificalis gives no reason".
- `tools/quote_scan_readings.json`: two readings added at the end (lines 27958 and 27959 of the Jerome PL 23 file).

## epiphanius-of-salamis
- `uncertain[10]`: "the last" to "the pretense".
- `tools/quote_scan_readings.json`: three readings added at the end (HOLL1 lines 12388, 12390, 12391), kind "OCR misread" as `Card_Edits.md` gives it (the check's optional kinds not used).

## eunomius-of-cyzicus
- `briefReferences[5]`: Dorner attribution applied.
- `sources.about`, Prolegomena entry: author to "Blomfield Jackson".
- NOT applied (Mark's quotation): changes 1 and 2, `quotationOriginals[5].work` and `.uncertain`, left as they were.

## eusebius-of-nicomedia
- `briefReferences[4]`: "I.9-10" to "I.9-10 and II.5-7".

## evagrius-ponticus
- PASS, no change.

## gregory-of-nazianzus
- `legacy.traces[3]`: "His modern translators" to "Gregory's modern translators".
- `sources.about`: Socrates and Sozomen entry appended.

## gregory-of-nyssa
- PASS, no change.

## hilary-of-poitiers
- PASS on the card; no change. The Gallic bishops' letter quotation is untouched.

## Not placed exactly
- Nothing failed to place. Judgment call: Eunomius change 3 (`briefReferences[5]`) was applied, since it is a reference line and not the quotation entry; reverse it if Mark wants the Basil-answer wording held as it was.
- Damasus' `original` text was copied from the check; not re-verified against the Latin file.
- The check's two asides (British "honoured" in the Apollinaris brief; Basil census conflicts) are not card changes and were not touched.
