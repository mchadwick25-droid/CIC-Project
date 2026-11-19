# R4 cap check: Venantius Fortunatus card (Mark's cap ruling, 2026-11-14)

## Scope

One targeted check, ordered in Mark's cap ruling, of three strings for the profile `venantius-fortunatus` in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch5/`:

1. `venantius-fortunatus.card.json`, `uncertain` item 1: "Gregory of Tours calls him a priest and never bishop."
2. `records.json`, entry `venantius-fortunatus`, the claim beginning "Gregory calls him presbyter in HF V.8", with its witness.
3. `records.json`, same entry, contested claim "Whether and when he was bishop of Poitiers", second side, beginning "Gregory of Tours calls him presbyter and never bishop".

Nothing else in the profile was reviewed. No other review or change file in this folder was read before this verdict.

## Method

- Read each cited line, with context, in `cic/texts/gregory-tours_opera-mgh-srm-1-lat_arndt-krusch1885.txt` (Arndt and Krusch, MGH SRM 1) and `cic/texts/gregory-tours_history-of-the-franks-v2_dalton1927.txt` (Dalton, vol. 2).
- Searched both Gregory files for every mention of Fortunatus, with OCR-tolerant patterns: `fortunat`, `rtunat`, `unatu[sm]`, `unati`, `unato`, line-final `fortu-`, and the OCR variants found (`Furtunat`, `Forfunat`, `Foitunat`, `Forlunat`, `Foriunat`, `For/unatus`, `J'\)rtunatuD`). About 124 hits in the Latin file, about 70 in Dalton.
- Sorted each hit into Gregory's own text versus editors' preface, notes, apparatus and index. Checked every hit for a nearby word for bishop (`episcop`, `pontif`, `antistes`, `sacerdo`).
- Compared each quotation with the cited line character by character.
- The Leo-Krusch Fortunatus file is not cited by any of the three strings, so it was not needed.

### Every mention of Fortunatus in Gregory's own text (both files)

| Work | Line(s), Arndt-Krusch | Reading (OCR as printed) | Title |
|---|---|---|---|
| HF V.8 | 15834-15835 | "librum vitac illius, qui a Fortunato'' prcsbi- / tero^ conpositus est" | presbiter |
| HF V.8 (Dalton) | Dalton 8393-8394 | "the book of his Life composed by the priest / Fortunatus" | priest |
| Gl. Mart. 41 | 39955 | "Quod Fortunatus presbiter his versibus prosecutus est" | presbiter |
| Virt. Mart. I prol. | 45002-45003 | "aut / certe Fortunatus ' adesset, qui ista discriberent!" | none |
| Virt. Mart. I.2 | 45245 | "Scd et Fortunatus presbitcr omne opus" | presbiter |
| Virt. Mart. I.13 | 46089-46090 | "vcucrjihilciii (•Mnscrvim» imMim Furtunatiiiii / prosbitiMniiu" (badly garbled: venerabilem conservum nostrum Fortunatum presbiterum; read with the editors' list at 35851-35854) | presbiter |
| Virt. Mart. I.15 | 46124-46126 | "Sibi quoquc liavenna ... confessus est" (he is not named; "Idem" carries over from I.13-14) | none |
| Gl. Conf. 44 | 58768 | "a Fortunato pvcsbitero conscript.am" | presbiter |
| Gl. Conf. 94 | 61148-61149 | "a Fortunato est con- / scriptus presbitero" | presbiter |

Dalton's Gregory text names Fortunatus once, at HF V.8 (8394). All other Dalton hits are Dalton's notes or index. One is the index entry "Fortunatus, poet, bishop of Poitiers" (l.31891), which is Dalton speaking, not Gregory.

Bishop test: Gregory never calls him bishop in either file. The only "episcopus" next to his name in the Latin file is the codex lemma at l.328, "'Fortunatus Pictavensis episcopus ad laudem bcati Gregorii hoc optis sub- / sequens fecit'. Quod aperte falsum esse, non est quod fusius dicamus." That is the editors' preface quoting a 15th-century manuscript heading and calling it false. Every other bishop-word hit near his name is in editors' notes and is about someone else (Gregory, Martin of Braga and others).

## String 1 — card `uncertain` item 1: PASS

"Gregory of Tours calls him a priest and never bishop."

- Every time Gregory gives him a title, the title is presbiter/priest (table above). He never gives him the title bishop.
- The sentence does not claim that every mention carries a title, so the untitled prologue and I.15 do not contradict it.
- The rest of the item matches its records: Paul (priest, then bishop), Baudonivia ("episcopus"), Dalton's view held as his opinion with his Introduction marked as not held, Luchi, and the unsigned Migne note. Nothing in the item says more than the sources show.

## String 2 — records claim "Gregory calls him presbyter in HF V.8 ...": FAIL (MINOR)

The substance holds: HF V.8, Virt. Mart. I.2, I.13 and Gl. Conf. all say presbyter, and Gregory never says bishop. The l.328 lemma is described correctly. The HF V.8 quotation is word for word (Dalton 8393-8394: "the book of his Life composed by the priest / Fortunatus"). Two citation defects remain:

- **MINOR 1 — the witness lines and the works named do not match.** The claim names Virt. Mart. I.13, but no cited line holds it; it is at Arndt-Krusch l.46089-46090. The witness cites l.39955, but that line is Gl. Mart. 41 ("Quod Fortunatus presbiter his versibus prosecutus est"), a work the claim never names. Fix: name Gl. Mart. 41 for l.39955 and add l.46089-46090 for Virt. Mart. I.13 (marked as garbled OCR).
- **MINOR 2 — a quoted phrase runs past its cited line.** The claim cites 'aut certe Fortunatus adesset' to l.45003, but "aut" stands at the end of l.45002 ("Utinam Severus aut Paulinus viverent, aut"). l.45003 reads "certe Fortunatus ' adesset" (the apostrophe is a footnote mark). The words are verbatim; the line reference should be l.45002-45003.

Observation (not counted as a finding): the Gl. Conf. quotation 'a Fortunato presbytero conscriptam' is word for word with l.35573. But that line is the editors' preface quoting Gregory ("postea haec addidit: Vitam tamen huius, postquam haec scripsimus, a Fortunato presbytero conscriptam cognovimus"). Gregory's own text of Gl. Conf. 44 is at l.58768 and reads "a Fortunato pvcsbitero conscript.am" (presbitero, in OCR). Citing l.58768 next to l.35573 would point to the primary text. The quotation is not wrong.

## String 3 — contested-claim side 2: PASS

"Gregory of Tours calls him presbyter and never bishop (gregory-tours dalton1927 l.8393-8394; gregory-tours arndt-krusch1885 l.45245, 35573); Dalton (... l.26296-26299) and Luchi (...) explain this by a consecration after Gregory's death; no held source gives the year"

- Dalton l.8393-8394 holds "the priest / Fortunatus"; l.45245 holds "Fortunatus presbitcr" [OCR presbiter]; l.35573 holds Gregory's Gl. Conf. 44 words, quoted by the editors ("a Fortunato presbytero conscriptam"). Each cited line holds what it is cited for.
- "never bishop" is confirmed by the full search above.
- Dalton l.26296-26299: "Gregory never alludes to / Fortunatus as bishop, because the latter was only consecrated to the / see of Poitiers after his death (cf. Introduction, p. 83 n. i)." The side reports this as Dalton's explanation, not as fact. That is accurate.
- Luchi was not re-read (outside the scope of the three Gregory-text checks).

## Verdict

NOT CLEAR

Nothing is BLOCKING. Strings 1 and 3 pass. String 2 has two MINOR citation defects (MINOR 1: Gl. Mart. 41 / Virt. Mart. I.13 line mismatch; MINOR 2: l.45003 should be l.45002-45003). No string says Gregory ever calls Fortunatus bishop, and none claims more than the sources show.
