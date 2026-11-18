# R4 cap check: era 7 batch 2, Trent, Poissy and Regensburg fix strings

- Ordered by: Mark's cap ruling on round 3 of era 7 batch 2. One targeted check of the three reader-facing strings applied for B3-B1 (Part B), D3-B1 (Part D) and A3-S1 (Part A) of `R3_recheck.md`. Unchanged text not reviewed.
- Scope: commits `cc12dbd3` (A3-S1) and `ecac1a5d` (B3-B1, D3-B1), in `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/`:
  - `council-of-trent.brief.txt`, `audio/council-of-trent.audio.txt`
  - `colloquy-of-poissy-1561.brief.txt`, `audio/colloquy-of-poissy-1561.audio.txt`
  - `colloquy-of-regensburg-1541.entry.json` (`uncertain[7]`)
- Brief figures (`working/grade.py`): Trent 398 words, 2.49 min, FK 7.74, Flesch 61.63, longest sentence 22 words. Poissy 400 words, 2.50 min, FK 7.58, Flesch 65.01, longest sentence 25 words.
- Reviewer: Opus, fresh, full effort. Read and grep only. No paid calls, no network.

Abbreviations: S = `cic/texts/sarpi_history-of-the-council-of-trent_brent1676.txt`; P2 = `cic/texts/pallavicino_istoria-del-concilio-di-trento-parte2-ita_1664.txt`; P3 = `cic/texts/pallavicino_istoria-del-concilio-di-trento-parte3-ita_1664.txt`; FAB = `cic/texts/faber_memoriale-lat_1873.txt`. OCR quoted with long s normalised.

## Verdict: CLEAR

B3-B1, D3-B1 and A3-S1 are closed, each as R3 worded it. No new finding.

## Checks

### 1. Trent brief, paragraph 4 (B3-B1)

Brief p.4 (file l.7): "In 1552 envoys from Saxony came. Sarpi says they asked the council to first affirm it stood above the pope." (The second sentence is 14 words.)

- S l.36582-36586: "Afterwards the Saxon Ambassadors were brought in; where being entred, and having made their Obeysance to the Assembly, Badehornus spake ... The Substance of his Speech was this: That Maurice, Elector of Saxony ..." The margin year is 1552 (l.36639).
- S l.36602-36612: first the safe-conduct "in the form of that of Basil", then "That all may be deferred until his Divines be heard". S l.36612-36621: then re-examination of the decided articles.
- S l.36622-36627: "the Councils of Constance and Basil having determined, That the Pope, in Points of Faith, and which concern himself, is subject to the Council, it is fit the same should be done in this Place".
- S l.36639-36641: "Therefore prayeth the Assembly, That they would first repeat, approve, and ratifie the Article of the Superiority of the Council above the Pope".

Findings on the sentence:
- "First" now sits on the council's act ("to first affirm"), as Sarpi has it ("That they would first ... ratifie"). It no longer makes this the envoys' first demand, which it was not: Sarpi gives the safe-conduct, the delay and the re-examination before it, and Pallavicino counts it "In quarto luogo" (P2 l.22532). The sentence says only what Sarpi says.
- "They." The referent is "envoys from Saxony" in the sentence before. In Sarpi the request is Maurice's, spoken by his envoy Badehorn to the assembly. Envoys presenting their prince's request are fairly said to ask it. The subject is right.
- "Affirm" renders "repeat, approve, and ratifie"; "it stood above the pope" renders "the Superiority of the Council above the Pope". Faithful, nothing added.
- The paragraph still reads cleanly: Calvin 1545, the envoys 1552, Jewel 1562, each with his own witness tag.

B3-B1: CLOSED.

### 2. Poissy brief, paragraph 2 (D3-B1)

Brief p.2 (file l.3), last two sentences: "The Catholic side speaks through Jesuits: those with the pope's legate, and Sforza Pallavicino, a historian of Trent. Another historian of Trent, the Venetian friar Paolo Sarpi, was hostile to the papal court." (18 and 15 words.)

- Pallavicino a Jesuit and a historian of Trent. P3 l.25-31, the printed title page in the OCR: "DELL'ISTORIA DEL CONCILIO ... SCRITTA DAL PADRE SFORZA PALLAVICINO DELLA COMPAGNIA DI GESV ORA CARDINALE". Each part's catalogue title (P2 l.1) reads "Istoria del Concilio di Trento, scritta dal padre Sforza Pallavicino della Compagnia di Gesù ... ove insieme rifiutasi ... un'istoria falsa divolgata nello stesso argomento sotto nome di Pietro Soave Polano". Both claims held. (Records `claims` "Pallavicino is of the Society of Jesus (title)" cites P2 l.1, the vendored header; P3 l.25-31 is the same fact in the printed text. Not reader-facing; not a finding.)
- Jesuits with the legate. Unchanged in substance from R2 ("who came with"). Records hold it: "The History says Lainez (called 'Lieva') was in the legate's train" (`beza_histoire-ecclesiastique-t1-fra_baum-cunitz1883.txt` l.30495-30503), and the legate came to court on 19 September (l.30472-30475).
- Sarpi a historian of Trent: S is his History of the Council of Trent, and he tells Poissy in it (S l.42795-42845: the Chancellor's charge "not to be averse from the Protestants, who were their Brethren", l.42805; Beza "spake with such heat, that it gave ill satisfaction to those of his own party; so that he was commanded to conclude", l.42836-42838; "The Cardinal Tornon, full of disdain, rose up", l.42838-42840).
- The side. Sarpi now stands in a sentence of his own, outside "The Catholic side speaks through". He is given no side, so no witness speaks for a party he does not carry. The colon keeps "Jesuits" over both the legate's men and Pallavicino; the parallel "those with ..., and ..." reads as two groups of Jesuits, not as Pallavicino being with the legate. "Hostile to the papal court" is the batch label word for word (Trent brief p.2: "The Venetian friar Paolo Sarpi was hostile to the papal court"); records `claims[112]` holds it.
- In its paragraph. The paragraph moves from the History (Reformed side, prelates' decisions) to the Catholic witnesses, then to Sarpi. "Another historian of Trent" tells the listener Sarpi is a second source of the same kind, which the brief then uses ("Sarpi says he was told to conclude", p.4). Clear. "Historian of Trent" for the council is the batch's usage and was in the text before this fix; it says nothing false. Not a finding.

D3-B1: CLOSED.

### 3. Regensburg entry, `uncertain[7]` last sentence (A3-S1)

Entry: "He says the business of the faith went forward 'valde ambigue', very doubtfully, in such a way that trust rests directly on God alone." (24 words.)

- FAB l.13476-13481: "Negotium fidei valde ambigue procedit, et eo modo ut in Deo solum immediate confidamus, cum media quibus utimur nihil sint in hominum judicio." Dated FAB l.13514, "Ratisbonæ, 12 Maii 1541".

Findings on the sentence:
- "Valde ambigue" is quoted verbatim; "very doubtfully" renders it. "Went forward" for "procedit" in reported speech, as R3 accepted.
- "In such a way that" renders "eo modo ut", with no purpose sense.
- "Directly" renders "immediate", "on God alone" renders "in Deo solum". "Trust rests ... on" is "confidamus" turned impersonal. It gives the "we" no subject the Latin does not give, and so drops the unsupported "he and his readers". It adds no claim: the omitted "cum media ... judicio" is left out, not contradicted.
- The sentence before ("The Jesuit Faber, writing from the city on 12 May, does not name the talks.") keeps the witness tag; "He says" governs this one.
- Records claim 88 keeps Faber's own "we"; the entry and records do not conflict. The brief does not carry this clause.

A3-S1: CLOSED.

### 4. Audio, limits, JSON, tells

- Audio: for each of Trent, Poissy and Regensburg, `audio/<id>.audio.txt` with "[calmly] " and "[warmly] " removed is identical to the brief (`diff`: no difference). The Trent and Poissy audio files carry the fixed sentences. No other tag.
- No sentence over 25 words: Trent longest 22, Poissy longest 25 (unchanged, not a fix string), Regensburg `uncertain[7]` longest 24. The fix sentences are 14, 18, 15 and 24 words.
- Word caps: Trent 398, Poissy 400 (cap 400).
- JSON: `colloquy-of-regensburg-1541.entry.json`, `colloquy-of-poissy-1561.entry.json` and `records.json` parse.
- AI tells: none in the three strings. No filler, hedging or assistant cadence.

## Findings

### Blocking
None.

### Substantial
None.

### Minor
None.

## Counts

Fixes checked: 3. Closed: 3 (B3-B1, D3-B1, A3-S1).
New: Blocking 0. Substantial 0. Minor 0. Total 0.
