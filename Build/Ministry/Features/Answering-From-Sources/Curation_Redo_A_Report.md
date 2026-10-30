# Curation redo, group A: status report

Status: checkpoint stop (allowance). No curation was finished. All four yaml files are unchanged and keep `status: needs-redo`.

Files done: none.
Files left: all four.

- augustine_doctrina-christiana-enchiridion-lat_bruder1838: started, then reverted. Findings to reuse:
  - Widening the head pattern to `^<?(?:Caput|[CGO0][.,]) ?(?P<c>[^\s.,]+)[.,]?\s` (with the line 9521 explicit division turned into a `fixes` entry `XVIII`) catches the OCR forms `C,` and `<C.`. The pattern then needs a `fixes` entry for every head whose numeral cannot be read through the ocr_map.
  - In this scan L is often printed `Ij`, `Tj` or `rj` (10460, 10606, 10905, 11047, 11649, 11658). That is a glyph reading, supported by the clean `C. LXX` heads.
  - The front matter (lines 395 to about 1646) prints each chapter summary with an Arabic numeral (`C. 12. Sapientia, puro interiori oculo ubique praesens`). It can serve as the second printed instance for damaged heads (body 2157 matches summary 12). Where neither the glyphs nor the summary settle a numeral, address by line.
  - Some chapters have no visible `C.` head at all (for example XVI in Book I, between 2244 and 2279). Each such gap needs a line-by-line look and must be listed with evidence.
  - The check run after the pattern change did not complete before the stop, so the new gap list is not yet known.
- augustine_sermones-1-340-lat_migne-pl38: not started. Split the 14 oversize sermons at their printed CAPUT heads.
- augustine_sermones-341-396-et-appendix-lat_migne-pl39: not started. Address line 66478 as unread-numeral-line66478; split sermo351, 361 and 362 at their CAPUT heads.
- augustine_sermones-post-maurinos-reperti-lat_morin1930: not started. Divide the Casinenses section by its four printed sermons and drop the word `survey` from the part7 locus.

First thing on resume: redo the Bruder file (rule change above, then a full list of gaps against the front-matter summaries), then PL38, PL39 and Morin.
