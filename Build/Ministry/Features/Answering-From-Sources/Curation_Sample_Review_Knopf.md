# Curation sample review: Knopf (redo of PR #1335)

Reviewer: Opus 5.5, 2026-10-30. Reviewed fresh against the vendored file `cic/texts/knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929.txt` (10,597 lines). `check` and `sample` were run with the `answering_library` code exported from origin/main.

## Verdict

| stem | verdict | what was checked (line numbers) | defects / notes |
|---|---|---|---|
| knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929 | sampled-ok | `check`: RESULT PASS, class curated, 58 divisions (56 body, 2 apparatus), coverage 100%, 0 oversize, 190 of 190 byte ranges exact, act series 1-33 and pionius-chapter series 1-23 with no repeats, backward steps or gaps. All 13 evidence quotes found on their lines. Pionius chapters II (3624), III (3668), IV (3688), VIII (3906) judged below. All 23 chapter heads I-XXIII seen in 3607-4435. Act heads 1-33 seen at 737, 1215, 1546, 1613, 1821, 2437, 2531, 2909, 3546, 3603, 4454, 4702, 4820, 4975, 5166, 5629, 6248, 6411, 6454, 6556, 6704, 6753, 6839, 7034, 7334, 7534, 7665, 7757, 7928, 8062, 8184, 8384, 8607. Divisions checked against the printed head: 737, 1546, 2437, 3603, 3607, 3624, 3668, 3688, 3835, 3850, 3906, 4018, 4232, 4245, 4358, 4435, 4820, 5629, 6411, 6839, 7757, 8184, 8607 (start, middle, end, the 3 largest: act5 1821, act8 2909, act16 5629; the 3 smallest: act10 3603, ch17 4245, ch1 3607). Apparatus 11-736 (front matter, contents, literature list) and 8904-10597 (Verzeichnis der Bibelstellen, then der Eigennamen, from 8904). | Minor notes only (below). |

## The judgment calls

- **Chapter II, line 3624, printed `Il.`** Read through `ocr_map` l to I. This is a reading of the printed glyphs (two vertical strokes, the second taken as lower-case l), not a number set from sequence. The map is confined to the hand-listed range 3607-4442, and no other line in that range matches the pattern through it. Gebhardt's own II head is damaged (`I. Mnvos` in the Gebhardt file), so it adds no second instance; the opening words match (`Mnyvocg éxtov devtéoa` = Gebhardt `Mnvos !xtov devrigg`). Accepted.
- **Chapter III, line 3668, printed `HI.` after scan debris.** Set by a `fix` with quote `HI. LMeocev`. Verified in `cic/texts/gebhardt_acta-martyrum-selecta-lat-grc-deu_1902.txt`, the edition Knopf states he follows (Knopf line 4443, `Text nach O. v. Gebhardt, Das Martyrium des heil. Pionius`): Gebhardt line 5246 prints `III. MNooosvsausvav de avıav za Außovrov` (the same opening, Προσευξαμένων δὲ αὐτῶν καὶ λαβόντων, as Knopf's `LMeocevéapuévar dé aitay nal AaBovtwy`), and Gebhardt line 5236 is the running head `VIII. Martyrium $. Pionii III. IV. 97`. The reading has a second printed instance, not sequence alone. Accepted.
- **Chapter IV, line 3688, printed `; . IV.`** The numeral is printed plainly; the widened pattern only admits the stray `; .` marks before it. Gebhardt line 5267 prints `IV. ’Eormoav` with the same opening. Accepted.
- **Line 3906, printed `VII.` a second time (after VII at 3880), set to VIII.** Gebhardt line 5510 prints `VIII. Hol de IHıovio einev Hol£uwv` (Πάλιν δὲ Πιονίῳ εἶπεν Πολέμων), the same opening as Knopf's `Wddw 6€ IMioviw einev Hohéuwv`. Backed by a second printed instance. Accepted. (The redo report also cites a page-102 running head for VII and VIII; that head, Gebhardt line 5486, actually reads `Pionii VIU.` in the OCR. The VIII head at 5510 carries the backing on its own.)
- **Act 3, line 1546, printed `8.`, set to 3.** Backed by the contents line 160 `3. Martyrium des Ptoleméus und Lucius`. Accepted.
- **Line 3511 `44. Martyrium der Potamiina ...`** is the running head for page 44 (page number plus act title, as at 1540 `14 Martyrium des Ptolemius und Lucius.`), correctly kept out by the split line range [737, 3510], [3512, 8903].

## The 71 look-alike warns

Every one of the 71 lines listed by the warn was read. Each is one of: an editors' arabic section number inside the Greek text (for example 3656 `3. Ov`, 3737 `11. tic`, 4172 `11. ody`), a margin line number followed by such a number (3894 `20 ar. 4.`, 4379 `25 7.`), or an apparatus line of Bible references (3629, 3782-3786, 3857, 3860, 3924-3926, 4063-4065, 4122-4123, 4198, 4406). A few are plain text lines (3679, 4004, 4171, 4222). None is a roman chapter head. A separate scan of 3600-4445 for lines opening with roman-like numerals found exactly the 22 pattern hits plus 3668, and the sequence I-XXIII is complete, matching Gebhardt's 23 chapters. No head was missed.

## Minor notes (no redo needed)

- The scheme says "other section numbers are the editors' own and are not used", yet the Pionius roman chapters are also an editorial division (Gebhardt's). Other acts print roman chapters as well (for example act 5 `I, 1.` at 1827, act 13 `I.` at 4823, act 28 `50 I.` at 7760) and are left unsplit. This is a legitimate granularity choice (act 10 needs its chapters to stay under the size cap; the others fit), but the scheme sentence could say so. No numeral is invented and every division stays addressable.
- Act 33 runs to 8903 and so carries its own headnote and bibliography (8887-8899), as every act does; consistent.

## Tooling observations

- The `check` warn lists every look-alike line in full on a single line; at 71 entries it is hard to read. A count plus a per-kind summary (arabic section, margin number, apparatus) would make the reviewer's job easier.
