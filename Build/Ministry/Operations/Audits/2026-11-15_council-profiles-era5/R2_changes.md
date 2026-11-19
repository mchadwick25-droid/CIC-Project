# Round 2 changes: era 5 council profiles (2026-11-15)

The coordinator applied the brief fixes; Opus fixers applied the entry and records fixes, each re-checking the evidence in cic/texts/ first. One line per finding.

Coordinator's actions and calls:
- Clermont brief: A2-S1 (the canon on prebends in two cities, which the Beauvais record heads as Urban's, replaces the investiture ban, whose heading names no pope) and A2-M2 (Lambert 'writing about 1120') applied as the recheck worded them. 400 words, FK 7.08, Flesch 68.77. The FK sits below grade 8; nothing in the text is padded or flattened, and raising it would mean joining sentences past the 25-word limit (as with era 4's Whitby).
- B-M10 (an optional close on Trent for Lateran IV): not taken. The Vitry close stays; era 4 accepted sourced closes of this kind.
- The census items of B-S6 and C-S3 are logged in Open-Gaps 268, 'Major councils, era 5' (2026-11-15; drafted as 267 and renumbered at merge, since 267 was taken on main by era 6 Who batch 2), with Clermont's.
- Outside the findings: one Opus pass split every entry sentence over 25 words in all three entries without changing content, and Henry IV and Gregory VII were taken off the Clermont Who click (neither took part; the era 4 rule).

---

## Round 2 changes: council-of-clermont-1095 (entry.json and records.json)

Evidence for every finding was re-read in cic/texts/ (M21 l.12040-12084, 27443-27450, 45236-45242; PL152 l.4325-4352, 26585-26665; LP1 l.47693-47699; LP2 l.71346; CART l.13305-13308). All held.

- A2-S1 — fixed (entry and records; the brief line is the coordinator's and already reads cap. 14). `decided[3]` replaced with the reviewer's text: investiture dropped, "or promoted to church offices" restored, the 62-word sentence split. Its lead clause is now a sentence of its own ("The Beauvais record gives these under headings that name Urban II at Clermont."), which keeps every sentence at 25 words or fewer. New `uncertain[1]` on the investiture item's heading and Hugh of Die's Clermont of about 1077, split into short sentences. Records: claim 34 now says "with no pope named". New claim on Hugh of Die's council (PL152 l.4329-4351, Dominant Modern Reconstruction). New contested claim "Which council of Clermont made the ban on lay investiture recited at Beauvais" (Inferential-Thin), using the reviewer's wording. The cap. 14 claim was already there and covers the new brief sentence.
- A2-M1 — fixed. `uncertain[5]` (was [4]): "The same notice has Urban die in 1096, where Duchesne dates his death to 1099." Lambert's `record` note adds "The same notice has Urban die in 1096." Records: the Lambert claim adds the death line and its witness range is widened to l.47693-47699. The "The year" contested claim adds the death year (LP1 l.47699) against 1099 (LP2 l.71346). New claim: Duchesne's heading "URBANUS II (1088-1099)" (LP2 l.71346).
- A2-M2 — the brief was applied by the coordinator ("writing about 1120, gives 310 bishops"; the three 1-word cuts are present). Entry `attended[1]` now reads "Lambert, a canon of Saint-Omer writing about 1120, gives 310 bishops".
- A2-M3 — fixed, with one wording change. In `uncertain[9]` the false "only" is gone and "No witness of the time among ours says so." now follows the Hours sentence directly. The last sentence reads "The editor questions the Carthusian vision told beside it, and says Petreius gives no proof that the Carthusians took up the Hours before Clermont." I wrote "says Petreius gives no proof" in place of "rejects the claim" because PL152 l.26653 says Petreius "nullo plane argumento probat", which is a charge of no proof, not an outright rejection. In the records Hours contested claim, "doubts the apparition and Petreius's order" now reads "questions the apparition, without denying it outright (l.26582-26604), and says Petreius proves by no argument that it came before the council (l.26645-26654)".
- A2-M4 — fixed. `calledBy` now reads "speaks of the council he held at Clermont". The field also had no final period, so I added one.
- A2-M5 — fixed. `uncertain[0]` now reads "Canons reach us only in later copies, chiefly Mirbt's sourcebook and the Beauvais record of 1114. Editors' notes printed by Mansi describe a few more." This is split to stay under 25 words a sentence. The `absent_details[0]` note adds "Baluze describes one more (M21 l.27445-27448)". New records claim for Baluze's note on the monks' canon (l.27445-27448). The note at M21 l.45240 ("cap. 5") is in the "adnotationes collectoris", not Baluze's notes, so it is covered only by "editors' notes" in general.
- A2-M6 — fixed. A final period was added to `datesNote`.

## Unresolved, for the coordinator
- Coordinator's FK note (7.02): no finding was raised. Left as it is.
- Older long sentences in the entry, which no round 1 or round 2 finding named, were left unchanged: decided[0], [1], [2], [4], [6], [8], [9]; uncertain[0] second sentence (26); uncertain[9] Hours sentence (32); datesNote sentence 3 (42 words). Split them in a later pass if the 25-word rule is meant for entry fields as well as the brief.
- No census or scan items are new this round.

---

## R2 changes: fourth-lateran-council-1215 (part B)

- B2-B1 — fixed — records `absent_details[10]`: detail now "A Cathar or Waldensian voice of the time on the council"; note adds that a later Waldensian voice is held (Jean Léger, 1669, livre 1 l.17714-17715, 20345-20347), with the recheck's text. Evidence checked in the Léger file: header Creator line ("pasteur et modérateur des Églises des Vallées") and both passages.
- B2-M1 — fixed — entry `traditions` notes for `cathars-albigensians` and `the-waldensians` now say the name is "a heading in Denzinger's Enchiridion, in Bannwart's edition of 1911" (Denzinger header l.1-2 names the Bannwart eleventh edition; headings at l.13857-13858). Optional part also applied: records `contested_claims` "Denzinger's heading" became "the heading in Denzinger's Enchiridion (Bannwart, 1911)" (one place).
- B2-M2 — fixed — added `sources.fromTheCouncil` row for Cajetan's commentary (thomas-aquinas_opera-omnia-t12-summa-theologiae-lat_leonine1906.txt; header title names Cajetan; canon 1 phrases at l.30506-30512, 33675-33677). Optional `record` rows also added after the Bollandists' canon 13 row: Glassberger's editors (Analecta Franciscana II, 1887) and Cajetan (Leonine Summa, 1906).
- B2-M3 — fixed — `people` name "Almaric of Paris" became "Almaric"; part unchanged.
- B2-M4 — fixed — records `claims[1]` now ends "...Jordan tells this a paragraph after the two men of Toulouse gave themselves to Dominic" (Acta Sanctorum l.93023-93026 "obtulerunt se servo Christi Dominico probi viri ... de Tholosa"; l.93047-93050).
- B2-M5 — fixed — `issue[2]`, `attended[4]`, `attended[5]` (closing period added; title "Lives of the Brethren" left to `record`/`sources`), `decided[2]`, `outcome[1]`, `outcome[3]`, `outcome[6]` replaced with the recheck's split text; Bartholomew of Trent `record` note given its closing period. Checked Denifle (Ehrle-Denifle bd1 l.5149-5150, "zu Anagni im J. 1255") and Röhricht l.6802-6805.
- B-M10 (R1, optional close) — not applied — decided by the coordinator: the Vitry close stays, since era 4 accepted sourced closes.

## For the coordinator

- Unchanged entry sentences the R2 recheck did not flag still run past 25 words (e.g. `issue[0]`, `issue[2]` sentence 3, `decided[0]`, `decided[5]`, `decided[6]`, `outcome[2]`, `outcome[7]`). They were not edited this round, being outside the R2 findings; worth a decision whether the cap binds them.
- B-S6 census items still await an era 5 councils entry in Open-Gaps.md.

---

## Round 2 changes, Part C: second-council-of-lyon-1274

- C2-S1 — fixed. Lea l.1854-1866 and Mirbt l.23009-23016 read in place: Lea has confirmed orders frozen (no new members, houses or sales without license); Clement XIV says nothing of confirmed orders. Entry `uncertain[4]` replaced with the four-sentence text from the recheck ("only" gone). Records contested claim "What the mendicant decree did": Lea side now gives the full condition, cited l.1856-1865 ("license", American spelling); Clement XIV side "Banned for ever only the..." changed to "Banned for ever the..." (same false "only").
- C2-S2 — fixed. Glassberger editors' note and Coulton l.15762-15766, l.16091-16094 read in place. Entry `decided[3]` second sentence replaced with the recheck's text. Records Salimbene side replaced with the recheck's text, with one correction: the Latin note sits at glassberger l.7319-7321 (full note with Innocent III's decretal l.7319-7324), not l.7323-7325; grep -n "cassavit"/"Saccatorum" gives l.7319/7320, only one copy of the file exists. The same wrong range (l.7323-7328) on the claim "Glassberger's editors quote Salimbene's Latin..." corrected to l.7319-7324. The recheck's "Verified" list carried this offset too.
- C2-M1 — fixed. PG 147 l.21320-21336 (Latin) and l.21391-21411 (Greek) read: John nine years, Athanasios restored, then the count "ἔτει ςω΄" [1292]. Claim reworded as the recheck asked (kept as one claim string, records convention); witness adds l.21391-21411.
- C-S3 (round 1, Open-Gaps census entry) — left for the coordinator, as the recheck says; still not in Open-Gaps.md.

Brief unchanged since round 1; entry and records agree with it. Both JSON files validate; records.json changed only under this key.
