# Card check, "what it was about" pass: Ulfila

Checked `ulfila.card.json` against `Card.pass2.json` (starting card), `Card_Edits.md` section "Third pass: what it was about (2026-11-23)", and `ulfila.brief.txt` as it now stands (diffed against `ulfila.brief.v3.txt`). The checker did not write the card.

## Verdict: PASS

## What was checked

1. **Nothing else moved.** A field-by-field diff of the starting card and the card shows changes only at `briefReferences[0]`, `[4]`, `[7]`, `[8]`, the new `[10]`, `uncertain[16]`-`[18]` (appended), and `sources.about[2].title` and `[4].title`. Each one is listed in the edit list. The key order is the same. `quotationOriginals` is identical.
2. **Each edit against its evidence** (every cited line opened):
   - `[0]`: the brief no longer tells the judge or the forty years (v3 to now). "to stop his opponents teaching in his churches" matches the brief, paragraph 21, and AUX 15283-15286 (*ne Cristi eclesias ... docerent et infestarent*).
   - `[4]`: matches the brief, paragraph 7. PHI 120 has the court and "Eusebius and the other prelates". The forebears and the embassy were cut from the brief.
   - `[7]`: NP2 9564-9573 ("the holy Scriptures have nowhere mentioned the substance of the Father and of the Son"), NP2 14428-14449 (Valens's troops, Fritigernes "embraced the religion of his benefactor"), NP2 14460-14465 ("a violation of the privileges of the religion of his ancestors"). The text is paraphrase with no quotation marks.
   - `[8]`: NP2 34561-34567 has the bishops. NP2 40141-40146 has the embassy asking for land. NP2 40163-40171 has "it is said" and the chiefs of the Arian faction promising to forward the request "if he would conform". This matches the brief, paragraph 17.
   - `[10]` (new): NP2 2064-2099 (Socrates 1.5: "If the Father begat the Son, he that was begotten had a beginning of existence"). THD 6002 and 6044-6046 (Theodoret 1.4, Arius's letter: "the Son has a beginning, but that God is without beginning"). NP2 14446-14449 and 40180-40181 name the faith after Arius. This matches the brief, paragraph 5.
   - `uncertain[16]`: NP2 34559-34568 (in number about fifty; the formulary of Ariminum; substance and hypostasis). The outline's cut 5 sends this "To the card".
   - `uncertain[17]`: PHI 120 (the captives from Cappadocia brought "a great number" to the faith, with "the ancestors of Urphilas" among them). The outline's cut 2 sends this "To the card".
   - `uncertain[18]`: AUX 15270 and 15279-15283 (seven years, then *triginta et tribus annis*, then *conpletis quadraginta annis* at the imperial order). The outline's cut 6 sends this "To the card", and the Do not say rule (credit the count to Auxentius) is kept.
   - `sources.about`: the titles now list Socrates 1.5 and Theodoret 1.4, so every chapter cited in `[10]` is in `sources`.
3. **briefReferences against the brief.** No entry names something the brief no longer tells. The cut items from v3 (the godless judge, about fifty, the forty years, the forebears, the consecration embassy, the other bishops "with him") are gone from the references. Only the not-quotation wording of the card is affected.
4. **Census rules.** Only allowed keys are used, and there is no `briefLength`. The brief still quotes four spans, and `quotationOriginals` keeps one entry for each, unchanged. No audit file is named. Spelling is American. The new prose has no quotation marks.
5. **"Checked at card" quotations.** These are "substance" and "alone unbegotten". Neither changed, and both still match the brief.
6. **Not found or clearly wrong.** No claim is unsupported, and nothing clearly wrong is left in.

## Note (the edit list, not the card)

`Card_Edits.md` third pass, item 6, says the "usual date" wording "was in the removed reference clause". That is not so: `briefReferences[8]` still says "360 is the usual date, and Sozomen gives the reign, not the year". So `uncertain[16]` repeats it. The repeat is true and supported, so the card does not need a fix.
