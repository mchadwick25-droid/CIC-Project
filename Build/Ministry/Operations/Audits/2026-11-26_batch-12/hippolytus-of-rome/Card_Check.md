# Card check: Hippolytus of Rome (`hippolytus-of-rome.card.json`)

**Verdict: FIX** (one change, in `quotationOriginals[0].uncertain`). Everything else passes.

## The fix

**Q2, the Greek "carried by hand".** I checked the note letter by letter against Lagarde's file (`cic/texts/hippolytus_quae-feruntur-omnia-contra-noetum-grc_lagarde1858.txt`). The file prints these lines:

- 3705: `ἕτερος. ἕτερον δὲ λέγων οὐ δύο θεοὺς λέγω, ἀλλ ὡς φῶς ix φωτὸς`
- 3706: `À c ὁ ) vo095 t ? ΄ν j V ες / / M /. ε` (stray marks)
- 3707: `Ἡ ὡς ὕδωρ ἐκ πηγῆς ἡ ὡς ἀκτῆα ἀπὸ ἡλίου. δύναμις γὰρ µία ἡ` (`µ` here is U+00B5, the micro sign)
- 3708: `ἐκ τοῦ παντός, τὸ δὲ πᾶν πατήρ, ἐξ οὗ δύναμις λόγος. ...`

The note's Greek does not match the file in six places. It gives `ἀλλ᾽` where the file has `ἀλλ` with no elision mark, `ἐκ` for `ix`, `ἢ` twice for `Ἡ` and `ἡ`, `ἀκτῖνα` for `ἀκτῆα`, and `μία` (Greek mu) for `µία`. No other held file prints Against Noetus 11 in Greek. I searched `cic/texts/`: Lagarde is the only Greek witness, and the other hits for `ὡς φῶς ἐκ φωτὸς` are unrelated works. Salmond's English (HIP 23614-23626) is a translation. It cannot confirm Greek letters. So the readings `ἐκ`, `ἢ`, `ἀκτῖνα` and the elision mark are restorations that no held file shows. The note also contradicts itself: it says "the Greek is not printed here" right after printing it. The rendering itself holds, since "from", "or" and "ray" follow Salmond where the scan cannot be read.

- **Field:** `quotationOriginals[0].uncertain`
- **Old:** "The modern English is rendered from Lagarde's Greek, lines 3705 to 3708 of its file, which reads by hand ἕτερον δὲ λέγων οὐ δύο θεοὺς λέγω, ἀλλ᾽ ὡς φῶς ἐκ φωτὸς ἢ ὡς ὕδωρ ἐκ πηγῆς ἢ ὡς ἀκτῖνα ἀπὸ ἡλίου. δύναμις γὰρ μία ἡ ἐκ τοῦ παντός, τὸ δὲ πᾶν πατήρ, ἐξ οὗ δύναμις λόγος. The scan is damaged there: it prints ix for ἐκ, Ἡ and ἡ for ἢ, and ἀκτῆα for ἀκτῖνα, with a line of stray marks inside the sentence, so the Greek is not printed here; Salmond's English confirms the reading. The words I mean it as supply the verb the Greek leaves understood in the second clause."
- **New:** "The modern English is rendered from Lagarde's Greek, lines 3705 to 3708 of its file, and follows Salmond's English where the scan cannot be read. The scan is damaged inside the sentence. It prints ix φωτὸς where Salmond has of light, Ἡ ὡς and ἡ ὡς where he has or as, and ἀκτῆα where he has a ray, and line 3706 is a row of stray marks. No other held print gives this Greek, so the Greek is not printed here. The words I mean it as supply the verb the Greek leaves understood in the second clause."

(`Card_Edits.md`, "The two quotations", Q2, makes the same restorations in its "checked by hand" Greek. It is not a card field, but release should not take that Greek from it.)

## The other checks

1. **Edits and routed items.** Each field's evidence was checked at its cited lines. I spot-read LP 66805-66810, 67682, 109159-109166 and 204190-204192, EUS 35434-35449, JER 40690-40703, PHO 11632-11635, EPI 32965-32966, PRU 23413-23418, 23444-23445 and 23677-23681, HIP 13280-13304, 13952 and 23614-23626, and THG 20467-20468 and 35178-35181. All support their lines. The items the outline, review and fresh read send to the card are on it: Epigonus and Cleomenes, the bank and the mine, Eusebius's many books, the Easter table with Jerome, Prudentius in the poet's voice, Hadrian, Photius, and the Spirit as a third in God's ordering. No modern opinion, date or identification is stated as content. The statue is told as a modern identification, and the attribution is told as resting on the modern editors. Modern works appear only in `modernWorks` (Entry fields), and each note says what the work covers.
2. **Nothing else moved.** This is a full new card. The kept fields (`otherNames`, Mommsen, Jerome, the HIP own-words entry) are word for word.
3. **`briefReferences`.** All ten match the brief now. The old lines on the ark, the bank, Portus and the others are gone.
4. **Census rules.** I ran the validator on a census copy outside the repository. The only card errors are the two missing `secondReading` values, which release sets, and the renderings listing still waits for its update, as `Card_Edits.md` says. There are two `quotationOriginals`, one for each quoted span in the brief. Q2 `printed` is verbatim at HIP 23614-23626, read past the endnotes. Q3 `printed` is verbatim at HIP 1129-1140, and its `original` is verbatim at RG 1348-1351 as the scan prints it (ϑ, χαὶ, zal). The quoted spans in card prose, "the Holy Hippolytus, Bishop and Martyr" (THG 20467-20468) and "attempt to call themselves a Catholic Church" (HIP 13952), are verbatim. Every cited file is in `sources`. No audit file is named, and the spelling is American.
5. **"checked at card".** None. Both quotations run six words or more.
6. **Not found.** None listed, and none found. Nothing clearly wrong was left in, apart from the fix above.
7. **Census entry.** There is no new entry file. The `teaser` change says no more than `knownFor` and the brief.
