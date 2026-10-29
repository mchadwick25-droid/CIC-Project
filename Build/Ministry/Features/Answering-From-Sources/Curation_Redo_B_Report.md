# Curation redo, group B: status report

Status: partial. Three of seven files redone; four left at `needs-redo`, untouched.

## Done (status `drafted`, `curate check` exit 0, review packet written by `curate sample`)

| Stem | Defects fixed | Check |
|---|---|---|
| `optatus_against-the-donatists` | Line 2294 `APPENDIX TO BOOK III.309` was declared running-head furniture. Removed the `ignore`; a context-only rule (`division: false`) now sets it, so the heading stays printed text at the head of Book III ch. XIII (division starts at 2294). Scheme now states that Book II prints XXIV (1233) then XXVI (1307) with no XXV heading. Evidence added for 1233, 2294, 2296. | PASS; furniture 0, words 123196 = 123196 |
| `codex-theodosianus_latinlibrary` | Added a `paragraph` rule on the 616 printed `CTh.b.t.l.n` lines (locus `cth{b}.{t}.{l}.{n}`), so `pr` now covers only the principium (e.g. 6.35.3pr at 2167, paragraphs .1 to .3 at 2169-2173). Duplicate 16.7.3: the Breviary text at 7311 takes `cth16.7.3=[brev.16.2.1]` (restates its printed reference; explicit one-line rule), the full text keeps `cth16.7.3pr` (7314) and `cth16.7.3.1` (7316). Scheme and evidence updated. | PASS; 3534 body divisions; all addresses unique |
| `acta-martyrum-selecta_gebhardt1902` | Missed headings added: Perpetua Greek ch. VII (3729, `VIL`, margin 25), VIII (3821, dropped I), XI (4043, Greek-letter ΧΙ), XII (4128, dropped I), XIII (4191, dropped I), XVIII (4416, dropped I); each set by `fixes` and backed in evidence by the page running head and the facing Latin heading. Pionius ch. IX (5132, Greek-letter ΙΧ), XVII (5465, margin number), XX (5558, `AX.`, running head 5533 `XX`) now match; the series reads 1 to 23 with no gap. Piece numerals damaged by the scan (V, IX, XI, XV, XVII, XIX, XX, XXI) each have a second printed instance in evidence (1735, 5708, 6078, 7631, 7994, 8647 `Anmerkungen zu Nr. XIX.`, 8716, 9476). Titles that were corrected spellings of OCR-damaged headings were dropped (pieces 4, 5, 9, 11, 21); piece 19 title now `Die Inschrift von Arykanda (c. 312)` as printed. | PASS; Greek series 1 to 21, Pionius 1 to 23, no gaps |

Tooling note: the Perpetua Greek and Pionius headings are still matched by line-restricted rules plus `fixes`, not by explicit `divisions`; the existing tooling expressed every case.

## Left (still `needs-redo`, yaml unchanged)

- `gebhardt_acta-martyrum-selecta-lat-grc-deu_1902`
- `knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929`
- `perpetua-scillitan-martyrs-lat-grc_robinson1891`
- `possidius_vita-augustini_weiskotten1919`

The sampler never reviewed these four, so no defect list exists. First thing on resume: for each, list heading lines with a margin number before the numeral, Greek-letter numerals, dropped-I numerals and running heads, as done for `acta-martyrum-selecta_gebhardt1902` (the same edition family, so its Perpetua and Pionius findings are a guide).

## Open points for the reviewer

- Codex: the paragraph series has one gap at line 1063 (3.30.3.6 after 3.30.3 head), which the edition itself prints; title 3.18 is followed by 3.30 in the vendored file.
- Gebhardt Greek ch. XIII (4191) prints `XII.`; read as XIII from the page running head (4161) and the facing Latin XIII (4173).
