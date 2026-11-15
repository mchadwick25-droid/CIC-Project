## Council profiles, era 7 batch 2, round 3: Part C (Diet of Augsburg and the Religious Peace 1555)

**Council.** `diet-of-augsburg-1555` (distinct from `diet-of-augsburg-1530`).
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/diet-of-augsburg-1555.brief.txt`, `audio/diet-of-augsburg-1555.audio.txt`, `diet-of-augsburg-1555.entry.json` (`uncertain[9]`, the only changed string), `records.json` key `diet-of-augsburg-1555` (`contested_claims[4]`, the only changed string; the key equals `working/records_diet-of-augsburg-1555.json`, checked by script: 105 claims, 8 contested claims, 12 absent details), and the README "Batch 2" line "Diet of Augsburg 1555 (about 2:30)" (unchanged). Scope: `git diff 7ad6d2a2 HEAD` restricted to this council, checked against `R2_recheck.md` Part C and `R2_changes.md` Part C.
**Brief.** 399 words (2.49 min at 160 wpm). `grade_text` via the batch's `grade.py`: FK 7.87, Flesch 62.60. Longest sentence 25 words ("Religion was to be handled in an assembly of Catholics and heretics, and he thought a legate no fit witness to such a monstrous thing."; unchanged). None over 25. The changed sentence is 10 words.
**Audio.** Equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and no other tag. Checked by `diff`.
**Entry.** JSON parses. Changed `uncertain[9]`: four sentences of 4, 13, 12 and 11 words.
**Reviewer.** A fresh Opus reviewer at full effort, who has not seen the drafting or fixing. Read and grep only. No repo file edited. No model, network or paid calls.

Abbreviations: PALL2 = `cic/texts/pallavicino_istoria-del-concilio-di-trento-parte2-ita_1664.txt`; POL5 = `cic/texts/polanco_chronicon-v5-lat_1897.txt`.

## Verdict: PASS (no blocking, no substantial, no minor)

Both round 2 findings are closed, and the fixes say only what their witnesses say.

**The key sentence.** Brief p.13: "Ferdinand answered sharply, Pallavicino says, feeling the concessions plainly necessary." Pallavicino's sentence in context, PALL2 l.27564-27576 (book 13, chapter 14):

> "ERA vscito il Recesso in sù lo spirar di Settembre: e'l Papa informatone fé perciò asprissime querele col Rè Ferdinando espostegli dal Nunzio Delfino che di Roma sul principio dell'anno seguente 1556. ritornò ad esercitare il carico antico. Mà il Rè, parendogli e che nelle concezioni [concessioni] dannose a cattolici la manifesta necessità l'havesse tenuto lungi da-* e che nelle cose arbitrarie à sé, si fosse per lui dimostrato ogni maggior zelo, rispose con maniere più risentite di quel che portava l'uso della sua temperata natura."

- Who speaks: Pallavicino, telling Ferdinand's view ("parendogli", it seemed to him). The brief keeps it inside "Pallavicino says" and gives it as Ferdinand's feeling, not his words. The round 2 error (necessity put into the answer by "pleading") is gone.
- Which side and what: the concessions are the ones harmful to Catholics, made in the recess; necessity is "manifesta" (plainly). "Feeling the concessions plainly necessary" uses only legible words. Whatever the lost word after "lungi da" is, the legible clause has plain necessity governing the concessions in Ferdinand's view; the brief claims no more.
- Cause: Pallavicino gives this view as why he answered sharply ("parendogli ... rispose con maniere più risentite"). The participle "feeling" carries that link without stating what the answer said.
- Omitted, not misstated: the second half of Ferdinand's view (greatest zeal where the choice was his) and Pallavicino's further "fors'anche" cause (Paul's ill will toward the House of Austria, l.27576-27579; the latter is in entry `uncertain[11]`). Leaving them to the entry is fair at this length.
- Antecedent: "the concessions" follows "called the recess ruinous" in the same paragraph, so it reads as the recess's terms, which is Pallavicino's referent.

**The matching entry and records strings.**
- Entry `uncertain[9]`: "Pallavicino says he 'consented to very grave losses for the Catholic religion'. Pallavicino adds that Ferdinand felt the harmful concessions were plainly necessary." The first sentence is PALL2 l.27413-27414 ("consentì à grauissimi detrimenti della Religion Cattolica"), book 13 chapter 13; the second is l.27569-27572, chapter 14. "Adds" is right: two passages by the same author. "Harmful" renders "dannose". "Felt" renders "parendogli". The fixer was right to change these too, not leave them: chapter 13's excuse (l.27415-27434, "Scusavasi egli di ciò con addurre") names Charles's curt reply, the feuds and Naumburg, and has no "necessità" in it; "pleaded necessity" had no ground in either passage.
- Records `contested_claims[4]` `sides`: "He 'consentì à grauissimi detrimenti della Religion Cattolica', and Ferdinand felt ('parendogli') the harmful concessions plainly necessary: Pallavicino (... l.27413, 27568-27574)". Quote verbatim (PALL2 l.27413-27414, long s read as s). "Parendogli" is verbatim at l.27569. The cited range covers the "parendogli" clause (l.27569-27572). Agrees with the brief and with `claims[73]` and entry `outcome[2]`, which already say "it seemed to Ferdinand" / "felt".
- No "plead" or "pleaded" remains anywhere in the brief, entry or this records key (grep).

## Round 2 findings

| ID | Status | Evidence |
|---|---|---|
| C2-M1 | CLOSED; fix right, and the optional entry/records part rightly applied | Brief p.13, entry `uncertain[9]`, records `contested_claims[4]` as above. PALL2 l.27564-27576 ("parendogli ... la manifesta necessità ... rispose con maniere più risentite"); l.27413-27434 (chapter 13 excuse, no "necessità"). |
| C2-M2 | CLOSED | Brief p.1: "Ferdinand, King of the Romans, came out with bishops and princes to meet him, writes the Jesuit Juan Alfonso de Polanco." POL5 l.15370-15372 "magnifice a Rege Romanorum, Cardinali augustano et aliis Episcopis et Principibus excepti fuerunt; qui fere leucam unam obviam Legato processerunt". The cut removes only "almost a league"; the scene and its witness tag stay. Entry `issue` and records keep the distance, so nothing disagrees. "Five days later" still holds (vigil of the Annunciation, 24 March; death news "29.*", l.15373-15374). |

## New findings

### Blocking

None.

### Substantial

None.

### Minor

None.

## Verified

- **Changed brief strings**, against their source lines in context: p.1 (POL5 l.15369-15376); p.13 (PALL2 l.27564-27579, and l.27405-27440 for the chapter 13 excuse).
- **Quotes re-verified verbatim** (OCR and long s allowed for): 'consentì à grauissimi detrimenti della Religion Cattolica' (PALL2 l.27413-27414, "grauifsimi"); 'parendogli' (l.27569). Translation "consented to very grave losses for the Catholic religion" is faithful and adds nothing.
- **No new quote** in the brief. No new absence claim (`absent_details[11]` is unchanged from round 2).
- **Witness tags.** "Pallavicino says" still sits with the changed sentence; "writes the Jesuit Juan Alfonso de Polanco" still sits with the cut sentence. None orphaned.
- **Pallavicino given as his.** Every changed string attributes the view to Pallavicino; none gives it as settled fact.
- **Writing.** The changed sentence has no empty contrast, no summing-up line, no filler; 10 words. Brief 399 words, under the ceiling, Flesch 62.60 (at least 60).
- **Audio** matches the brief with the two tags (diff). **Entry JSON** parses. **records.json key** equals the working records file.
- **README line** "Diet of Augsburg 1555 (about 2:30)" still true at 399 words (2:29). Unchanged and needs no change.

## Searches run

1. `grep -n "parendogli\|temperata  natura\|grauifsimi  detrimenti\|Delfino  che"` in PALL2: confirms line numbers l.27413, l.27567, l.27569, l.27576.
2. `grep -n -i "plead\|necess\|18 December\|ruinous\|concession"` in the brief and entry: no "plead" left; `outcome[2]`, `uncertain[9]` and brief p.13 agree.
3. Script over records key `diet-of-augsburg-1555` for `necess|plead|parendo|lungi|ruin|December`: `claims[49]`, `claims[73]`, `claims[85]`, `contested_claims[4]`, `absent_details[11]`; all agree with the brief; no "plead" left.
4. `grep -rl "leucam"` over Polanco files, then POL5 l.15366-15382: confirms the scene for C2-M2.

## Counts

Blocking 0, Substantial 0, Minor 0. Brief: 399 words, 2.49 min, FK 7.87, Flesch 62.60, longest sentence 25.
