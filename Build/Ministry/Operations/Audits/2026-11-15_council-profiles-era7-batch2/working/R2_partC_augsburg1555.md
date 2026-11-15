## Council profiles, era 7 batch 2, round 2: Part C (Diet of Augsburg and the Religious Peace 1555)

**Council.** `diet-of-augsburg-1555` (distinct from `diet-of-augsburg-1530`).
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/diet-of-augsburg-1555.brief.txt`, `audio/diet-of-augsburg-1555.audio.txt`, `diet-of-augsburg-1555.entry.json`, `records.json` key `diet-of-augsburg-1555` (equal to `working/records_diet-of-augsburg-1555.json`, checked by script: 105 claims, 8 contested claims, 12 absent details), and the README "Batch 2" line "Diet of Augsburg 1555 (about 2:30)". Scope: `git diff f6c9d034 HEAD` on branch `claude/cft-councils-era7-batch2`, checked against `R1_review.md` Part C and `R1_changes.md` Part C.
**Brief.** 400 words (2.50 min at 160 wpm, at the ceiling). `grade_text`: FK 7.81, Flesch 63.11. Longest sentence 25 words ("Religion was to be handled in an assembly of Catholics and heretics, and he thought a legate no fit witness to such a monstrous thing."). None over 25.
**Audio.** Equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and no other tag. Checked by `diff`.
**Entry.** JSON parses. No sentence in any entry string runs past 25 words (script check).
**Reviewer.** A fresh Opus reviewer at full effort, who has not seen the drafting or the round 1 fixing. Read and grep only. No repo file edited. No model, network or paid calls.

Abbreviations as in round 1: POL5, PALL2, SARPI, MIRBT, BOSS, SAL, NAD1, CAL4.

## Verdict: PASS WITH MINOR FIXES (no blocking, no substantial, two minor)

Both round 1 blocking points are closed, and their fixes are right against their source lines.

- **Polanco (C-B1).** The brief now says "The rest comes from Polanco's chronicle". In context Polanco writes of the Jesuits at Augsburg in the third person ("praeparabant se nostri", POL5 l.15377). The editors' note has him writing from Rome to Nadal at Augsburg ("Ita Polancus, ex com., Patri,Nadal, 1.* Aprilis 1555", l.15394-15395). "Chronicle" is the right kind for him. The earlier sentence that carries his scene ("writes the Jesuit Juan Alfonso de Polanco") makes no claim that he was there. The entry's new `uncertain[0]` names "Nadal's and Salmerón's letters from the city". That holds: Nadal dates letters "Augustae, 30 Martii 1555" and "Da Augusta, 30 di Margo 1555" (NAD1 l.16761, l.17057), and Salmerón writes "De Augusta oy primero de Setiembre de 1555" (SAL l.8585).
- **Pallavicino and Sarpi (C-B2).** The join is gone. Sarpi's quote now stands in its own sentence with Sarpi, and his cities are the Interim cities (SARPI l.38433-38442). The next two sentences each sit with Pallavicino. Their words match PALL2 l.27522-27529: "inuogliati dalla dissoluzione de' circonuicini", "di viuere anch'essi sciolti dall'osseruanza de' mandamenti ecclesiastici", "seguir la Religion de' Padroni, ò à partirsi". "Their neighbors' freedom" is fair for the neighbors' "dissoluzione" that the subjects asked to share.

Two minor points remain. First, "pleading plain necessity" does avoid the lost word, but it turns Ferdinand's view ("parendogli") into something said in his answer (C2-M1). Second, one length cut (C2-M2).

## Round 1 findings

| ID | Status | Evidence |
|---|---|---|
| C-B1 | CLOSED | Brief p.5 and entry `uncertain[0]` as above. POL5 l.15369-15381, l.15394-15395; NAD1 l.16761, l.17057; SAL l.8585. |
| C-B2 | CLOSED | Brief p.11 as above. PALL2 l.27522-27529; SARPI l.38433-38442. Each of the three sentences keeps its own witness. |
| C-S1 | CLOSED, with a new point | The brief no longer uses the lost word. PALL2 l.27568-27576 reads "Mà il Rè, parendogli e che / nelle concezioni dannofe acattolici la ma- / nifefia necessità l'hauefse tenuto lungi da-* / e che nelle cofe arbitrarie à sé ... rifpofe con maniere più rifentitc". Entry `outcome[2]` ("felt that plain necessity had kept him 'lungi da' ('far from') something ... The next word is lost in our copy"), records `claims[76]` and the new `absent_details[11]` are faithful. The absence holds (searches 1-3). On "pleading", see C2-M1. |
| C-S2 | CLOSED | "Its editor, Gustav Bossert, notes that the duke added the Zwinglians in his own hand." BOSS l.2 "(Gustav Bossert the elder, Editor ...)"; l.9280 "Zwinglischer über der Zeile, von Herzog Christophs Hand". |
| C-S3 | CLOSED | MIRBT l.21736-21742: "caeteris catholicis et Augustanae confessioni addictis statibus et subditis tribuuut, id eliam iis, qui inter illos reformati vocantur, competere debeat". The brief now has "It gave both religions' rights also to those among them called the Reformed." That is faithful, and "among them" keeps the Latin's own reach. Entry `outcome[16]`, `traditions[4].note`, `uncertain[8]` and `record[8].note`, and records `contested_claims[3]` and the claim at the old l.574, all agree. Westphalia now has its own side. "Kept holy and inviolable": l.21625-21627 "rata habeatur sancteque et inviolabiliter servetur". |
| C-S4 | CLOSED | PALL2 l.27415-27438 is one indirect speech, running from "Scusauasi egli di ciò con addurre" to "conchiudeua il Rè in sua discolpa". `calledBy`, `issue[9]`, `uncertain[10]` and records `claims[26]`, `[30]`, `contested_claims[4]`, `absent_details[2]` and `[8]` now give the speech as Ferdinand's defence. `calledBy`'s "sickness and war kept him from German affairs" matches l.27421-27423 ("per malattia di corpo, e per distrazione di guerra applicar l'animo agli affari dell'Alemagna"). Its narrowed absence, "No held source disputes that Charles called it", agrees with SARPI l.38051-38052 ("which the Emperour had intimated") and l.38056-38057 ("in the Emperours name"). |
| C-S5 | CLOSED | `uncertain[14]` and the old records claim on the brief are deleted. |
| C-S6 | CLOSED | The three absence claims are deleted. Each is still in `absent_details`. Sarpi's "very few were come" remains as a claim. |
| C-S7 | CLOSED | `absent_details[4]` now cites CAL4 l.19188-19439 for the two 1555 letters. The fixer's range is right: the Tarnow letter runs on to where Varaglia begins. |
| C-M1 | CLOSED | "A draft order of Duke Christoph of Württemberg, begun in 1556, ordered Anabaptists and Schwenckfelders punished, since the peace did not include them." BOSS l.9113 ("1556 nach September 11. — Mandat ... (ohne Datum)"); l.9310-9313 ("in jüngstem zuo Augspurg ufgeriebtem religionsfridenstand ... mit nichten begriffen, sonder darvon usgesohlossen, an er, leub und gut zu strafen"); l.9322-9326 ("Der erste ... Entwurf ... stammt aus dem Jahr 1556 ... noch Anfang 1557 wurde der Entwurf beraten"). |
| C-M2 | CLOSED | "either religion"; MIRBT l.16317. |
| C-M3 | CLOSED | `knownFor` is one sentence of 25 words. |
| C-M4 | CLOSED | Tail deleted from `issue[5]`. |
| C-M5 | CLOSED | The labels are statements. The fixer rightly applied the "for ever" label at `[5]`. |
| C-M6 | CLOSED | `uncertain[13]` as proposed. |
| C-M7 | CLOSED | `decided[8]` keeps "not held directly from the empire" ("reichsmittelbaren"). |
| C-M8 | CLOSED | SAL l.8448-8450 ("llegamos ... á 20 de Agosto en esta çibdad de Augusta, y con quanta charidad reçebidos de monseñor Rmo. de Verona"); l.8500-8503 ("el Rmo. de Verona se parta luego para Polonia ... nos partyremos de Augusta"). `attended[6]`, `people` Salmerón, `traditions[3].note` and `claims[42]` agree with these lines. |
| C-M9 | CLOSED | SARPI l.38148-38150 "no ſooner arrived in Awsburg, but Pope Julius died, whereof he received advice cight days after". |
| C-M10 | CLOSED | `claims[50]` witness as proposed. |
| C-M11 | CLOSED | PALL2 l.27479-27481 "rimar, effe pur la prefente ferma cd inaiai abile". The quote is in the print's spelling, and the OCR reading is flagged. |
| C-M12 | CLOSED | SARPI l.38469-38470 "did de-|dare with conſent of the Eccleſiaſtical Order". The notes now say the phrase is legible and the terms break off. |
| C-M13 | CLOSED | "vna" (PALL2 l.27399 "vna pende rofa_»"; l.27429 OCR "vua"). |
| C-M14 | CLOSED | The README now reads "The room comes only from Catholic writers, the Jesuits Polanco and Pallavicino and the friar Sarpi". Pallavicino is a Jesuit, as the brief itself says ("the Jesuit historian Sforza Pallavicino"). |

## New findings

### Blocking

None.

### Substantial

None.

### Minor

**C2-M1. Minor (a thought told as speech).** Brief p.13: `Ferdinand answered sharply, Pallavicino says, pleading plain necessity.`
- PALL2 l.27568-27576: "Mà il Rè, parendogli e che nelle concezioni dannofe acattolici la manifefia necessità l'hauefse tenuto lungi da-* e che nelle cofe arbitrarie à sé ... rifpofe con maniere più rifentitc". Pallavicino gives necessity as how things seemed to Ferdinand ("parendogli"). That view is why he answered sharply. Pallavicino does not say what the answer contained. "Pleading" puts necessity into the answer to Paul IV.
- The fixer grounds "pleading" also on "Scusauasi egli di ciò con addurre" (l.27415). But that excuse is the earlier defence in chapter 13: Charles's curt reply, the feuds, Naumburg, and approving what both sides had agreed. It is not the answer to the December complaints in chapter 14, and the word "necessità" is not in it.
- The fix keeps to the legible words, "la manifesta necessità" and "concessioni", and does not use the lost word. Fix, brief (10 words): `Ferdinand answered sharply, Pallavicino says, feeling the concessions plainly necessary.`
- Optional, same point: `uncertain[9]` and `contested_claims[4]` say Pallavicino has him plead necessity. For the chapter 13 excuse, that is fair as a gist. Leave them.

**C2-M2. Minor (length; scene detail with no decision, side or source).** Brief p.1: `Ferdinand, King of the Romans, came out almost a league with bishops and princes to meet him, writes the Jesuit Juan Alfonso de Polanco.`
- "Almost a league" ("fere leucam unam", POL5 l.15371-15372) is true. But it is the only clause in the brief that carries no decision, side or source. The scene and its witness stay without it.
- Fix, brief (21 words): `Ferdinand, King of the Romans, came out with bishops and princes to meet him, writes the Jesuit Juan Alfonso de Polanco.`

## Length test

Each sentence was tested for a decision, a side or a source that the story would lose without it. Numbers are sentence numbers; there are 29.

- 1-4 (scene, Julius's death, Morone's going). These form the opening scene (C8). They show Rome gone before the business began, and they bring in Julius before sentence 5 names him. Sentence 4 is the only place the listener learns the legate took no part. Keep. Cut "almost a league" from sentence 2 (C2-M2).
- 5-6 (Julius's reluctance). This is Rome's stance, in the pope's own terms. Keep.
- 7 (Pallavicino, a century later). This is a witness tag, and it dates the witness. Keep.
- 8 (Mirbt's recess). This names the source and defines "recess" before it is used. Keep.
- 9 (Polanco's chronicle, Pallavicino, Sarpi). This tells the listener whose account stands in (C2), and it is the C-B1 fix. I tested dropping the second and third "from". That saves 2 words but leaves a ragged list of a book and two persons. Not proposed.
- 10 (no Lutheran). This is the absence, stated once (C3). Keep.
- 11 (not 1530). The README requires it. Keep.
- 12-13 (caller, purpose, opening, thin attendance). These carry C4 and C5. "His brother" says why Ferdinand acts for Charles (SARPI "his Brother"). Keep.
- 14-20 (the recess). There are six clauses plus the date. Each is a decided article. "With their wives and children" gives the article's own scope ("mit iren weib und kindern"). Sentence 20 is the acts' side of the Contested "for ever" claim. Keep.
- 21-23 (Sarpi's bargain; Pallavicino's subjects). These are the two witnesses for "rulers choose", each in its own sentence. Keep.
- 24-25 (Paul IV; Ferdinand's answer). This is a decision rejected, with both voices. Keep. Reword sentence 25 per C2-M1.
- 26-27 (Duke Christoph; Bossert). This is the exclusion in use, with its witness tag. Keep.
- 28-29 (Westphalia). This is the reach of the close, and the other side of the Contested exclusion of the Reformed (C-S3). Keep.

No sentence repeats another, and none restates the README's reason. There are no double attributions. Polanco is named twice, but once as the voice of the scene and once in the list of whose account stands in. Each mention does its own job, and the second is the round 1 blocking fix.

**Counts.**
- Now: 400 words, 2.50 min. FK 7.81, Flesch 63.11. Longest sentence 25.
- After C2-M2 alone: 397 words, 2.48 min. FK 7.78, Flesch 63.08.
- After C2-M1 and C2-M2: 399 words, 2.49 min. FK 7.87, Flesch 62.60. Longest sentence 25.

All three were checked with `grade_text` and the batch's `grade.py` on scratch copies (`aug1555.r2.txt`, `aug1555.r2c.txt` in this scratchpad). The Flesch floor holds, and no sentence passes 25 words.

The brief earns close to its full length. It is at the ceiling because it carries six recess clauses, four witnesses and two later texts, not because it was padded. Only one cut is proposed.

**README line.** "Diet of Augsburg 1555 (about 2:30)" is still true at 397-399 words (2:29). No change.

## Verified

- **Every changed or added brief string**, against its source in context: p.5 (POL5 l.15369-15395); p.9 "either religion" (MIRBT l.16317); p.11 (SARPI l.38433-38442; PALL2 l.27522-27529); p.13 (PALL2 l.27560-27576); p.15 (BOSS l.2, l.9113, l.9240-9244, l.9280, l.9308-9326); p.17 (MIRBT l.21622-21627, l.21733-21742).
- **Quotes re-verified verbatim** (OCR and long s allowed for):
  - Sarpi, "The Catholicks were content that the Cities should do as they pleased" (SARPI l.38441-38442, unchanged).
  - Entry, changed or added: 'lungi da' (PALL2 l.27571); 'vna ponderosa scrittura' (l.27399); 'quasi in vna Contradieta' (l.27429); 'in secca forma' and 'Onde à esso Ferdinando ne rimettea la dispositione' (l.27422-27424); 'qui inter illos reformati vocantur' (MIRBT l.21737-21738); 'rata habeatur sancteque et inviolabiliter servetur' (l.21626-21627); 'ferma ed inuiolabile' (PALL2 l.27481); 'with consent of the Ecclesiastical Order' (SARPI l.38469-38470); 'eight days after' (l.38150); 'die Konfession zu Augsburg' (unchanged wording).
- **Translations.** "far from" for "lungi da"; "as if in a counter-diet" for "quasi in vna Contradieta"; "who among them are called Reformed" for "qui inter illos reformati vocantur". All are faithful and add nothing.
- **Split and joined sentences.** All were checked: brief p.11 (one sentence became two) and p.17 (one became two); entry `issue[9]` (three sentences), `outcome[2]`, `uncertain[0]`, `uncertain[8]`, `record[8].note` and `traditions[4].note`. Each claim still sits with its witness. In p.17 the subject "It" is the Peace of Westphalia, and both sentences rest on the same treaty text.
- **Salmerón's letters** dated from Augsburg (SAL l.8435, l.8585), and Nadal's (NAD1 l.16761, l.17057, l.17084, l.17228). These support "letters from the city" in `uncertain[0]`.
- **Schaff** on Frederick III, "threatened with exclusion from the benefits of the Augsburg Treaty of Peace (concluded in 1555)" (schaff file l.1819-1820), supports the new `traditions[4].note`.
- **Audio** matches the brief with the two tags. **AI tells.** None in the changed strings: no empty contrast, no "X and never Y", no summing-up line, no filler.
- **README.** All three batch 2 lines for this council were checked against the brief. "About 2:30" stands.

## Searches run

All over `cic/texts`, case-insensitive. Each one tests the new absence, "the end of Pallavicino's clause is lost; no other copy of book 13 is held".
1. `temperata +natura`: one file, PALL2 (l.27576). The only other `lungi da colpa|tenuto lungi` hit is Muratori 1748 (unrelated).
2. `concessioni +dann|concezioni +dann`: PALL2 only.
3. Files whose title line names Pallavicino: parte1, parte2 and parte3 (1664), and tomo3 libri 17-24 (1846). Book 13 is only in parte2. No Latin version (Giattini) is held. `manifest[ae] +necessit|manifesta +necessità` finds only unrelated medieval and patristic files.
4. "Letters from the city" in `uncertain[0]`: `august` in NAD1 l.16700-17400 and `augusta` in SAL l.8400-8620. Both are held, as listed under Verified.

## Counts

Blocking 0, Substantial 0, Minor 2. Brief: 400 words, 2.50 min now; 399 words, 2.49 min after both proposed fixes (397 words, 2.48 min after the length cut alone).
