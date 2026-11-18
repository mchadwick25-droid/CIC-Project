# Curation sample review: Bruder (redo, PR #1352)

Reviewer: Opus 5.5, 2026-10-30. Fresh review of the redone curation `Sandbox/answering-library/curation/augustine_doctrina-christiana-enchiridion-lat_bruder1838.yaml` against `cic/texts/augustine_doctrina-christiana-enchiridion-lat_bruder1838.txt`. Drafter report: `Curation_Redo_bruder_Report.md`.

`check` and `sample` were run with the `answering_library` code exported from origin/main. The checker passes: 279 divisions (278 body, 1 apparatus); doctrina1 40, doctrina2 42, doctrina3 37, doctrina4 31, enchiridion 122; no gaps, repeats or backward steps. The known holes in the checker (PR #1346) mean its silence was not relied on. Every finding below comes from my own scan of the file.

## Verdict

| Stem | Verdict | Checked | Defects / notes |
|---|---|---|---|
| augustine_doctrina-christiana-enchiridion-lat_bruder1838 | sampled-ok | All 272 numbered heads in the five series; my own scan of the body for chapter-head-like lines; the front-matter argumentum; NPNF 102 and 103 for every head with no argumentum; quotes; apparatus; size extremes | Minor notes only (below). No numeral rests on sequence alone. |

## What was checked

**My own head scan.** I scanned every body line (1647 on) that starts with `C`, `G`, `O`, `0`, `V` or `<`, followed by a short numeral-like token, or with `Caput`. I also scanned every line whose first token is roman-like, to catch heads whose `C.` is lost. I searched for `C.` plus a numeral in the middle of a line. Result: every head-like line is a division start except three footnote lines (4563 `O ,,Hnc…`, 10130 `Gj Rom. 3, 20.`, 11622 `0 C. 4, 11.`). The only division missed by the shape scan is 2547 `i\ XX\ I.`, whose `C.` is lost; it is a quoted fix. The roman-first-token scan found only footnote lines (`Ij …`, 11360 `II, 37. ss.`) and lone `I` lines. No printed head is left out. Each rule's pattern, run over its own line range, matches only division starts (no extra hits).

**Clean heads.** 229 of the 272 numbered heads print a numeral that is clean once `l`, `1` and `i` are read as I. Each one equals the number assigned. No clean head was overridden.

**Damaged heads: all 43 have a second printed instance by content.**
- Argumentum in the front matter (clean Arabic number and a summary that matches the head's opening words). Doctrina1: 1860 (arg 395), 1991 `\T` VI (411), 2547 XXVI (449), 2724 `XWI` XXXI (464), 2882 `XXWI` XXXVI (475). Doctrina2: 3536 `XFil` XIII (541), 3942 `XVH` (553), 3976 `XVTII` (554), 4343 `XXVT` (572), 4363 `XXVIL` (573), 4372 `XXVIIL` (576). Doctrina3: 5197 `IV^` (644). Doctrina4: 7640 `XY` (674), 8541 `XXIL` (689), 8694 `XXVT` (693), 8770 `XXV'11` (696), 8820 `XXVTII` (697). Enchiridion: 9431 (760), 9521 `XV''!!!` (770), 9751 `XXU` (786), 10460 `XIjV` (859), 10511 `\LV II` (867), 10606 `IjII` (884), 10816 `LVHl` (905), 10905 `IjXI` (912), 11047 `IjXVI` (933), 11470 `LXXV III` (971), 11545 `V . LXXIX.` (972), 11604 `LXXX[` (976), 11637 `LXXXn` (979), 11649 `rjXXXni` (982), 12390 `CVUI` (1059).
- Enchiridion 84 (11658 `TjXXXIV`) and 87 (11716 `LXXX^'!!`): the argumentum entries are themselves damaged (989 `C. S4. Quaestionum de carnis resurrectione…`, 996 `V. 8T. Quaestio de foetibus monstrosis`). Their content matches the heads (`Iam vero de resurrectione carnis`, `Neque enim et monstra`). NPNF 103 ch. 84 (resurrection of the body) and ch. 87 (monstrous births) confirm both.
- Doctrina3 (argumentum lost after ch. 4, near line 644). I checked against NPNF 102, Book III (ids `v.vi.*`), by opening words: 5197 IV (ambiguities "not … punctuation or pronunciation"), 5310 `\T1` VII ("if ever any of them endeavored … signs"), 5499 `XU` XII, 5622 `XV\` XV ("tyranny of lust being thus overthrown"), 5893 `XXV^` XXV ("when it is shown to be figurative, the words…"; NPNF ch. 24 ends just before it), 5960 `XXVT` XXVI, 5975 `XXVTI` XXVII, 6006 `XXVHl` XXVIII, 6255 `XXXI V^` XXXIV ("fourth rule of Tichonius"), 6399 `XXXV'` XXXV ("fifth rule"). All match.
- Doctrina4 ch. 1 to 6: all heads are clean. I checked 6720 `ill` III ("theories and rules on this subject") and 6831 `iV` IV ("duty … of the interpreter and teacher") against NPNF 102 Book IV (id `IV_1`). Both match.
- Book I heads 6, 26, 31 and 36 also match NPNF 102 Book I (`v.iv.*`).

**Judgment calls.**
- 2724 `XWI` as XXXI and 2882 `XXWI` as XXXVI: the W stands for a different merged pair in each (XX, then XV). Both are confirmed by the argumentum (31 "Deum quidem diligere nos, sed non frui nobis"; 36 "Interpretatio scripturae licet vitiosa…") and by NPNF. Accepted.
- 2547 `i\ XX\ I.` as XXVI: argumentum 26 and NPNF ch. 26 ("no need of a command that every man should love himself") match. Accepted.
- The trailing `L` (4363, 4372, 8541, 9431, and `Caput L` at 1860): the values set (27, 28, 22, 16, 1) are right and content-backed. The L stands for the last `I` fused with its full stop (`XXVI` + `I.`). It is not a bare damaged stop, as the report words it: a bare stop would give 26, 27, 21 and 15. The wording is loose; the readings are correct.
- 11545 `V . LXXIX.`: the numeral is clean, and `V .` is the damaged `C.`. Argumentum 79 and NPNF 79 match. Accepted.
- Per-series `ocr_map` (doctrina2 T=I, H=II, F=I; doctrina3 T=I, U=II, H=II; doctrina4 Y=V, T=I; enchiridion H=II, U=II, n=II, `[`=I): every map-read head in each series was checked by content (above). None of these letters stands for a different numeral anywhere in its own series. Where a glyph reads differently, it is set by a quoted fix and not by the map: `\` is V at 1991 and 2547 but X at 10511; `Tj` is L at 11658 in the enchiridion, whose map has no T. The patterns, run over their ranges, match no extra lines, so the wider letter class takes no prose line as a head.
- The 43 `warn` lines (`Christ-`, `Cal.`, `Cui`, `Corrupto`, `Cincta`, `Cf.`, `Cedar`, `Contritus`, `CMitus`, `Craeci`, `Cur`, `C/iristo` and the like) are all running prose or footnotes. None is a heading.
- The explicit division at 9521 is gone. 9521 is now a quoted fix (`C. XV''!!!.`).

**Apparatus.** Lines 11 to 1646 are front matter: title page, Praefatio (49 to about 360), Argumentum librorum (361 to 1101, holding the table-of-contents lines such as 572 `C. 26. Necessaria et commoda…`), Index locorum (1102 on), the Retractationes extracts (1577 to 1636), and the work's title page (1637 to 1646). None of it is taken as body. The Prologus begins at 1647.

**Quotes.** All 78 evidence quotes and all quoted fixes are on their stated lines (whitespace-normalised).

**Sample and size extremes.** The sample's 12 divisions (1647, 2454, 3282, 4663, 5631, 6720, 8820, 9713, 10475, 11250, 11947, 12767) each open on the printed head of the addressed chapter. The 3 largest are doctrina4 ch. 7 (6978, 2352 words, the Paul and Amos examples), ch. 20 (7900, 1822) and ch. 21 (8200, 1816). My scan finds no head inside them, and their length matches NPNF's long chapters 7, 20 and 21. The smallest are the book and work markers: 5017 LIBER TERTIUS (2 words), 8978 ENCHIRIDION (10), 1857 LIBER PRIMUS (11), 3009 LIBER SECUNDUS (13). Each is the edition's printed title.

## Minor notes (no redo needed)

1. Seven fixes carry no `quote`: 1860, 4363, 4372, 6255, 8541, 9431, 11470. These are the earlier fixes kept. Each line has an `evidence` entry quoting the damaged head, and each value is content-backed.
2. The report describes the trailing `L` as "a damaged full stop". It is the last `I` fused with its stop. The values are right.
3. Lines 8975 to 8977 (`S. AURELII` / `A U G U S T 1 N I`, the start of the Enchiridion title) and the scan debris before them end up in doctrina/book4/ch31, because the enchiridion marker starts at 8978. The library stamp and scan debris at the end of the file (12780 to 12801: `DATE DUE`, `GAYLORD`, `WELLESLEY COLLEGE LIBRARY`) sit in enchiridion/ch122 rather than in back apparatus. No text is lost and no numbering is affected.
4. The NPNF checks for doctrina3 and doctrina4 ch. 1 to 6 cannot be recorded in this yaml's `evidence`, which quotes only this file. They are recorded here and in the drafter's report.

## Tooling observations

- The checker's `warn` list is all noise for this file now, because the pattern's letter class is wide. A reviewer still has to scan by hand for lost-`C` heads like 2547, which the shape filter does not report (see PR #1346).
- Separately, it would help to have a way to cite a second instance in another vendored file (here NPNF 102/103) in the curation.
