# R3 targeted recheck: era 3 batch 4


Reviewer: independent (Opus). Did not draft these profiles and did not write R1 or R2. Review only: no repo file edited, no paid or model-API call, no web.

Scope: each R2 finding (R2-B1, R2-M1 to R2-M8, and the Jacob card order) checked against the current files, with every cited line re-read in its vendored file. Then only the text R2 changed (diff `797b32e4..3894d4a3`) checked for new faults. Audio scripts compared to briefs with `[calmly] ` and `[warmly] ` removed. Readability by `engine.m1.gates.grade_text`, run from the repo root. All cards and `records.json` parse as JSON.

Line numbers: briefs and cards at HEAD; other files under `cic/texts/`.

## R2 findings

| Finding | Verdict | Evidence re-read |
|---|---|---|
| R2-B1 (David: Brefi year) | resolved | Card l.32 as proposed; `absent_details` entry gone; claim added, Inferential-Thin. Acta Sanctorum March I l.15583-15584, "in Brtvienfi Synodo (ejnam Spelmann/tt, Vf- fa-ins , aUitfmt anno dxix. habit am tradnnt)" (OCR). The speaker is the Bollandists' annotation column: l.15569 (note 13) reads "Eodem anno DXIX Synodum a S. David collectam ita describit Giraldus". No other "no year" remains in the batch. |
| R2-M1 (Theodosius `knownFor`, `place`) | resolved | `knownFor` l.7 no longer says "near Constantinople". `place` l.9 now "by John of Ephesus"; John, PO18 l.32350-32353, "a certain fortress ... called Dercus" in Thrace. |
| R2-M2 (Jacob `uncertain` 1) | resolved | l.26. Michael (Chabot) l.25322-25325: "il ne se sépara point d'eux; mais il avertit et blâma les deux partis", where "eux" are "les partisans de Jacques". |
| R2-M3 (David sources) | resolved | Acta Sanctorum file added to `sources.about`. |
| R2-M4 (David `uncertain` 5) | resolved | "The scan" is gone. l.15511-15513 (Patrick's attempt "ante annos octodecim" the mission of 432) and margin "An. 414" (l.15519) support 414; the result "ad annum CCCCXIV. pervenitur" (l.15528) stays unstated. Records claim updated. See R3-M1 on length. |
| R2-M5 (John `uncertain` 6) | resolved | No English in quote marks. Michael l.26288-26289, "l'évèque Jean, qui était gardé en prison à Chalcédoine depuis un an"; l.26302-26303, "il mourut au jour qu'il avait indiqué". No other identifier in the passage, so "named only as John" stands. See R3-M2 on length. |
| R2-M6 (Victor death) | resolved | Hodgkin index l.25466 (not 25465), "Victor Tunnunensis, chronicler (died in 569)"; Kugener l.26977, "Victor mourut vers l'an 569". Both files now in `sources.about`. |
| R2-M7 (Cassiodorus sources) | resolved | Strauch l.22202, "Cassiodori Senatoris (f 563)"; Williams l.286, "Cassiodorus, who died a.d. 570". Both files now in `sources.about`. |
| R2-M8 (David brief l.1, audio) | resolved | "Paulinus, an old bishop who had once taught David, told them to send for him." Welsh Life (Rees) l.18377, "an old holy bishop"; l.18117-18119, "he taught David"; Latin Life l.6677-6678, "episcoporum quidam, Paulinus dictus, cum quo quondam Sanctus David pontifex legerat" (tr. l.19605-19606). Both Lives support the sentence the brief gives as "the Lives of David say". Audio script carries the same change. |
| Jacob card order | resolved | `sources.ownWords` (l.36) now comes before `about` (l.43), as in the other cards that have own words. |

All ten R2 items are resolved.

## New findings (text changed in R2 only)

### R3-M1 MINOR (item 4; sentence past about 25 words). David of Wales card, `uncertain` 5 (l.30)

The sentence R2-M4 added runs to 29 words, and "which they put in 414" can be read as the valley: "The Bollandists, in the Acta Sanctorum for the first of March, count his birth thirty years after Patrick's stay in the valley of Rosina, which they put in 414."

Fix: "The Bollandists, in the Acta Sanctorum for the first of March, put Patrick's stay in the valley of Rosina in 414. They count his birth thirty years after it." (21 and 9 words; same evidence, l.15511-15528 and margin.)

### R3-M2 MINOR (item 4; sentence past about 25 words, stacked clauses). John of Ephesus card, `uncertain` 6 (l.40)

The sentence R2-M5 rewrote runs to 30 words with three stacked qualifiers: "His source is Michael the Syrian, who tells of a bishop named only as John, held a year in prison at Chalcedon, who died on the day he had foretold."

Fix: "His source is Michael the Syrian, who tells of a bishop named only as John. He had been kept a year in prison at Chalcedon, and he died on the day he had foretold." (15 and 19 words; Michael l.26288-26289, l.26302-26303, "gardé en prison ... depuis un an", "il mourut au jour qu'il avait indiqué".)

Neither touches a brief, so no readability score or audio script changes.

### Checked and not findings

- False absences: R2 removed one absence (Brefi) and added none. No new absence wording in the changed text.
- Editor's view told as settled: the 519 year is "The Bollandists report that Spelman, Ussher and others put it in 519", attributed, tagged Inferential-Thin in records. The 414 start is given as the Bollandists'. Hodgkin's flat 569 and Kugener's hedged "vers" are now told apart.
- Witness swaps: Jacob l.26 gives Michael's own narration as Michael's; Theodosius `place` gives Dercus to John, who names it. None found.
- Contested points one way: the 575 quarrel now has Brooks and Michael by name.
- Unplaced common names: "Spelman" (David l.32) appears once, as the Bollandists' "Spelmannus", alongside "Ussher", whom the card already names bare (l.29) and R1/R2 accepted. Not raised.
- English in quote marks not in the file: none in the changed text.
- "X, not Y" and colon-reveals: none. Jacob's "did not break with Jacob's party but rebuked both sides" renders Michael's "ne se sépara point ... mais il avertit et blâma"; it reports the source, not a rhetorical contrast.
- "Held": the new uses are ordinary English (records "was held in 519"; no new participant-facing use). The R2-M5 card text now avoids the word.
- Audio: all ten scripts equal their briefs once `[calmly] ` and `[warmly] ` are removed. Each has one `[calmly]` at the start and one `[warmly]` at the start of the last paragraph. No tags in briefs or cards.
- `briefLength` matches each word count.

## Length and readability (current files)

| Profile | Words | FK | Flesch | Cap | Pass |
|---|---|---|---|---|---|
| Theodosius I of Alexandria (major) | 401 | 7.2 | 66.1 | about 405 | yes |
| Jacob Baradaeus (major) | 402 | 6.0 | 75.6 | about 405 | yes |
| Cassiodorus (major) | 405 | 6.3 | 75.8 | about 405 | yes, at the cap |
| Gildas (major) | 403 | 6.2 | 75.8 | about 405 | yes |
| Longinus, bishop of the Nobadae | 320 | 7.1 | 70.2 | about 325 | yes |
| John of Ephesus | 320 | 6.2 | 74.2 | about 325 | yes |
| Victor of Tunnuna | 321 | 8.0 | 60.6 | about 325 | yes, near the Flesch floor |
| Agathias of Myrina | 323 | 6.2 | 73.6 | about 325 | yes |
| David of Wales | 323 | 6.4 | 74.3 | about 325 | yes |
| Radegund | 326 | 5.7 | 76.6 | about 325 | yes |

All ten briefs pass `grade_text` (FK 10 or below, Flesch 60 or above) and sit within their caps.

The batch clears: all ten R2 items are resolved, there is no blocking finding, and the two new minor findings (R3-M1, R3-M2) are one-sentence splits in card fields, to be applied as worded with no further review round.
