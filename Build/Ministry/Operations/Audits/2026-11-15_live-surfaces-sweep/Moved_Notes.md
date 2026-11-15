# Moved notes — live-surfaces sweep, 2026-11-15

Every passage this sweep cut from or rewrote on a live surface, verbatim, so nothing it held is lost. Each hunk shows the lines as they stood (`before`) and as they stand now (`after`). Where the substance also lives elsewhere, the note under the file says where; otherwise this file is the record.

Line numbers in vendored Library files (`cic/texts/*.txt`) are unchanged: every header was rewritten in place, so no quote's cited line moved.

## `Build/worlds/ijc/Source_Registry.md`

The verification history of row 30 is appended to `Build/worlds/ijc/build/BUILD-LOG.md`.

Lines -43 +43:

```text
before:
| 30 | Susan Wessel, *Leo the Great and the Spiritual Rebuilding of a Universal Rome* (Brill, Supplements to Vigiliae Christianae vol. 93, 2008) | S | B | Native | — | Strand A / Leo the Great | Title confirmed 2026-08-05 (full-system review) — matches the working recollection exactly; publisher/series/year added. Confidence raised C -> B (title now confirmed; still not independently re-collated against the book's own text this session, so not A) | Identified via `Archive/Syriac-Build-2026-07/CiC_Coach3_Step0_Critique_2026-07-06.md`'s own correction re-anchoring Wessel to "Cyril of Alexandria, Leo the Great"; Coach3's own numbering scheme used a different "world #6" label (Alexandria) than this project's final Step 0 Conclusion numbering (where #6 = this world) — the substantive scholarly anchor (Leo the Great) is what licenses this entry, not the numbering, which is not otherwise relied on | 2026-07-20; title confirmed 2026-08-05 |
after:
| 30 | Susan Wessel, *Leo the Great and the Spiritual Rebuilding of a Universal Rome* (Brill, Supplements to Vigiliae Christianae vol. 93, 2008) | S | B | Native | — | Strand A / Leo the Great | Title, publisher, series and year confirmed; not independently re-collated against the book's own text, so B, not A | Identified via `Archive/Syriac-Build-2026-07/CiC_Coach3_Step0_Critique_2026-07-06.md`'s own correction re-anchoring Wessel to "Cyril of Alexandria, Leo the Great"; Coach3's own numbering scheme used a different "world #6" label (Alexandria) than this project's final Step 0 Conclusion numbering (where #6 = this world) — the substantive scholarly anchor (Leo the Great) is what licenses this entry, not the numbering, which is not otherwise relied on | 2026-07-20; 2026-08-05 (title confirmed) |
```

## `cic-website/README.md`

The section "Known follow-ups, not yet done" was moved whole; its three items are carried in the Church Family Tree Open-Gaps entry this sweep files (see R1_changes.md).

Lines -13,5 +13,3:

```text
before:
- `support.html` — "Get Involved," rewritten with real cost figures; see its own
  header comment and the funding-strategy decision record under
  the project's private funding-strategy material for the full derivation. Currently
  unlinked from the site nav — needs a content refresh; the homepage's own
  "Keep the Door Open" section carries the real Stripe give links directly,
after:
- `support.html` — "Get Involved," with real cost figures; see its own
  header comment for the derivation. Unlinked from the site nav; the
  homepage's own "Keep the Door Open" section carries the real Stripe give links directly,
```

Lines -28,2 +26:

```text
before:
  shared script is `assets/go-deeper.js`. Decision record under
  the project's private funding-strategy material.
after:
  shared script is `assets/go-deeper.js`.
```

Lines -55,2 +52:

```text
before:
   `churchinconversation.com` (make it primary — the entity is now a for-profit
   PBC, and .org read as nonprofit-coded) and `churchinconversation.org` (set
after:
   `churchinconversation.com` (make it primary) and `churchinconversation.org` (set
```

Lines -71,15 +66,0:

```text
before:

## Known follow-ups, not yet done

- The "How It Works" and "Safety & Disclosure" sections on the About page
  were written directly from the Vision doc and Constitution's own
  commitments (Article 17/Article 6-adjacent language) — worth a brand-kit
  compliance pass before this goes fully public, same as any other CiC
  public copy.
- No favicon raster exports yet (BR-17 in the System Hub tracker covers
  this) — the SVG favicon works in modern browsers but a proper `.ico`/PNG
  set would cover older clients and app icons.
- Consider adding the Article 31 external-review disclosure once that
  process is further along — the positioning brief's own overclaim register
  says not to claim "scholarly validated" before that's true, and this site
  currently doesn't make that claim, which is correct for now.
after:
(cut)
```

## `cic/texts/INTAKE.md`

The 2026-09-25 ruling and the framing it replaced are recorded in `Build/worlds/_cross-world/LIBRARY-DECISION-LOG.md`.

Lines -7 +7:

```text
before:
**Trigger — two real paths, both fine (2026-09-03).** Mark finds a source
after:
**Trigger — two real paths, both fine.** Mark finds a source
```

Lines -22,3 +22,2:

```text
before:
this corpus so far is an English translation of an ancient work. Starting
2026-09-02, Mark is also sourcing **original-language texts** (Greek, Latin,
Syriac, ...) directly. Everything below applies to both; where they differ,
after:
this corpus is an English translation of an ancient work. Mark also sources
**original-language texts** (Greek, Latin, Syriac, ...) directly. Everything below applies to both; where they differ,
```

Lines -27,2 +26:

```text
before:
**A clean public-domain original can be primary evidence (Mark's ruling,
2026-09-25).** Language is not what decides whether a source is primary —
after:
**A clean public-domain original can be primary evidence.** Language is not what decides whether a source is primary —
```

Lines -52,6 +49,0:

```text
before:
This replaces this file's own prior framing (in force 2026-09-02 through
2026-09-25) that an original-language text was a second witness by
definition, never primary evidence, because the project's evidence language
was English. The reasoning for the change, and the ruling's own words, are
recorded in `worlds/_cross-world/LIBRARY-DECISION-LOG.md` — this file states
the current rule plainly, not its history.
after:
(cut)
```

Lines -66 +58:

```text
before:
this in Mark's own message alongside it; a file pulled from `_intake/`
after:
this in Mark's message alongside it; a file pulled from `_intake/`
```

Lines -216,2 +208:

```text
before:
Derived, gitignored, ~10 seconds for the whole corpus as of 2026-09-02 (64
files). Skipping this just means the new file is invisible to
after:
Derived, gitignored, about 10 seconds for the whole corpus. Skipping this just means the new file is invisible to
```

## `cic/texts/REGISTRY.yaml`

Lines -3,7 +3,3:

```text
before:
# WHY THIS EXISTS, AND WHY IT MOVED HERE (2026-09-02, Mark's sign-off). This
# data used to live as a 750-line Python tuple (`ENTRIES`) inside
# cic/engine/texts_registry.py. Moving it to YAML changes nothing about what
# it means or how it's checked — cic/engine/texts_registry.py still reads it,
# still validates it against what's actually sitting in cic/texts/, still
# generates cic/texts/README.md from it — but it stops requiring Python to
# read or write: the download queue, a future Zotero export, the Atlas feed,
after:
# WHY THIS IS YAML. cic/engine/texts_registry.py reads this file, validates
# it against what is actually sitting in cic/texts/, and generates
# cic/texts/README.md from it. As YAML it needs no Python to read or write: the download queue, a future Zotero export, the Atlas feed,
```

Lines -47,5 +43,3:

```text
before:
#                  and never a per-QUOTE pattern either — R33 (2026-09-23,
#                  Mark, on this file's own first draft, which anchored five
#                  entries to one quote's exact wording each): "we should be
#                  setting principles we will have a 100 worlds and cant
#                  tell the representitive what to say for every quote."
after:
#                  and never a per-QUOTE pattern either: the rule is a
#                  principle that holds across a hundred worlds, not a
#                  wording fitted to each quote.
```

Lines -81,2 +75:

```text
before:
#                    kind: letterform (Mark's OCR/normalization ruling,
#                      2026-09-25) - this ONE edition's own OCR misreading
after:
#                    kind: letterform - this ONE edition's own OCR misreading
```

## `cic/texts/abdisho-iv_approbatio-et-professio-fidei-concilio-tridentino-lat_1562.txt`

Lines -9 +9:

```text
before:
Content note: The whole print, about 11,000 characters. Cardinal Amulio's letter to the legates at Trent dated Rome, August 1562 (the day is garbled in the OCR); then the profession of faith of Abdisho IV (the successor line to Yohannan Sulaqa), sworn at Rome on 7 March 1562 in the presence of Cardinals Michele (Alessandrino) and Amulio, with the later certification of 23 July 1562 and his oath to receive the decrees of the councils and of Trent. SECOND WITNESS for exact wording: the OCR is readable but noisy (long s read as f and /, some broken words), sampled at five points; verify any quote against the page images (Mark's OCR ruling, 2026-09-25). A second scan of the same print is Internet Archive item LeaBX8301545A232 (University of Pennsylvania, Public Domain Mark; OCR noisier, not vendored). This is Abdisho IV's profession, not Sulaqa's own of 1553.
after:
Content note: The whole print, about 11,000 characters. Cardinal Amulio's letter to the legates at Trent dated Rome, August 1562 (the day is garbled in the OCR); then the profession of faith of Abdisho IV (the successor line to Yohannan Sulaqa), sworn at Rome on 7 March 1562 in the presence of Cardinals Michele (Alessandrino) and Amulio, with the later certification of 23 July 1562 and his oath to receive the decrees of the councils and of Trent. SECOND WITNESS for exact wording: the OCR is readable but noisy (long s read as f and /, some broken words), sampled at five points; verify any quote against the page images. A second scan of the same print is Internet Archive item LeaBX8301545A232 (University of Pennsylvania, Public Domain Mark; OCR noisier, not vendored). This is Abdisho IV's profession, not Sulaqa's own of 1553.
```

## `cic/texts/aquino-de-belen_pasyon-and-manga-panalangin-tgl_manila1760.txt`

Lines -9 +9:

```text
before:
Content note: Second witness under the Library's OCR ruling (2026-09-25), not quotable from this file alone: the OCR of this 1760 Manila print reads the long s as f throughout the Tagalog ("fa" for "sa", "Pafsion" for "Passion"), drops and garbles many letters, and carries marginal noise on most pages; the title page and the Spanish approbation (which describes the book as Villacastin's Recomendacion del alma put into Tagalog by Aquino de Belen, printer of books, with the Passion of Our Lord in Tagalog verse inserted by the translator) are readable with effort. Order of contents: title page, licences and approbations (Spanish), the prayers for the dying, the Litany of the Saints, then the verse Passion (the first "Pafsiong" of the poem falls a little under half way through the file) running to "LAVS DEO" at the end. The poem is the earliest surviving Tagalog pasyon; its first printing (1704) is after this world's window, so for the 1565-1650 entry it is a successor text, and it is placed to the Era-8 Philippine entry as that entry's own voice.
after:
Content note: Second witness, not quotable from this file alone: the OCR of this 1760 Manila print reads the long s as f throughout the Tagalog ("fa" for "sa", "Pafsion" for "Passion"), drops and garbles many letters, and carries marginal noise on most pages; the title page and the Spanish approbation (which describes the book as Villacastin's Recomendacion del alma put into Tagalog by Aquino de Belen, printer of books, with the Passion of Our Lord in Tagalog verse inserted by the translator) are readable with effort. Order of contents: title page, licences and approbations (Spanish), the prayers for the dying, the Litany of the Saints, then the verse Passion (the first "Pafsiong" of the poem falls a little under half way through the file) running to "LAVS DEO" at the end. The poem is the earliest surviving Tagalog pasyon; its first printing (1704) is after this world's window, so for the 1565-1650 entry it is a successor text, and it is placed to the Era-8 Philippine entry as that entry's own voice.
```

## `cic/texts/assemani_bibliotheca-orientalis-tomus3-pars2-de-syris-nestorianis-lat_1728.txt`

Lines -9 +9:

```text
before:
Content note: Tome III part 2 of the Bibliotheca Orientalis (the 1725 part 1, De Scriptoribus Syris Nestorianis, is Internet Archive item bub_gb_dqIBok_FOLEC and is not vendored). Part 2 opens with Assemani's long dissertation De Syris Nestorianis, whose chronology of the patriarchal line, the election of Sulaka in 1551, his journey to Rome, profession of faith and proclamation as patriarch, his return and death in 1555, and the election and profession of Abdisho IV (1562) are at file lines about 11995-12050, with quotations of the professions elsewhere (for example Abdisho's "Ego Abdjefus filius Joannis" at about line 42232). Written from the Roman side by a Maronite priest of the Vatican Library, from manuscripts and Roman archives; a documentary witness to the schism, not the voice of either patriarchal line. The dates in this OCR are garbled and do not agree with the 1725 volume's (item bub_gb_dqIBok_FOLEC, file lines about 101020-101080, which gives arrival 18 November 1552, profession 20 February 1553 and proclamation 9 April 1553 as the OCR reads); read them off the page images. SECOND WITNESS for exact wording: Google-digitised OCR of a Latin folio with long s read as f throughout and the Syriac and Arabic passages garbled; sampled at five points (10/30/50/70/90 per cent: the Latin of the dissertation reads, the Syriac script does not); verify any quote against the page images (Mark's OCR ruling, 2026-09-25).
after:
Content note: Tome III part 2 of the Bibliotheca Orientalis (the 1725 part 1, De Scriptoribus Syris Nestorianis, is Internet Archive item bub_gb_dqIBok_FOLEC and is not vendored). Part 2 opens with Assemani's long dissertation De Syris Nestorianis, whose chronology of the patriarchal line, the election of Sulaka in 1551, his journey to Rome, profession of faith and proclamation as patriarch, his return and death in 1555, and the election and profession of Abdisho IV (1562) are at file lines about 11995-12050, with quotations of the professions elsewhere (for example Abdisho's "Ego Abdjefus filius Joannis" at about line 42232). Written from the Roman side by a Maronite priest of the Vatican Library, from manuscripts and Roman archives; a documentary witness to the schism, not the voice of either patriarchal line. The dates in this OCR are garbled and do not agree with the 1725 volume's (item bub_gb_dqIBok_FOLEC, file lines about 101020-101080, which gives arrival 18 November 1552, profession 20 February 1553 and proclamation 9 April 1553 as the OCR reads); read them off the page images. SECOND WITNESS for exact wording: Google-digitised OCR of a Latin folio with long s read as f throughout and the Syriac and Arabic passages garbled; sampled at five points (10/30/50/70/90 per cent: the Latin of the dissertation reads, the Syriac script does not); verify any quote against the page images.
```

## `cic/texts/augustine_civitate-dei-1-13-lat_hoffmann-csel40-1.txt`

Lines -8 +8:

```text
before:
Provenance note: Mechanically extracted from the item's own djvu.txt; minimal front-cover scan noise stripped before the title page. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note (independent review, Round 18; extended, Round 19; extended, Round 20): quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1899), independently confirmed distinct from the in-copyright-adjacent 1962 Johnson Reprints of the same text (those reprints' own items were opened only briefly to confirm the 1962 reprint notice, and were not used as this file's source).
after:
Provenance note: Mechanically extracted from the item's own djvu.txt; minimal front-cover scan noise stripped before the title page. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note: quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1899), independently confirmed distinct from the in-copyright-adjacent 1962 Johnson Reprints of the same text (those reprints' own items were opened only briefly to confirm the 1962 reprint notice, and were not used as this file's source).
```

## `cic/texts/augustine_civitate-dei-14-22-lat_hoffmann-csel40-2.txt`

Lines -8 +8:

```text
before:
Provenance note: Mechanically extracted from the item's own djvu.txt; minimal front-cover scan noise stripped before the title page. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note (independent review, Round 17; extended, Round 18; extended, Round 19; extended, Round 20): quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1900), independently confirmed distinct from the in-copyright-adjacent 1962 Johnson Reprints of the same text.
after:
Provenance note: Mechanically extracted from the item's own djvu.txt; minimal front-cover scan noise stripped before the title page. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note: quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1900), independently confirmed distinct from the in-copyright-adjacent 1962 Johnson Reprints of the same text.
```

## `cic/texts/augustine_confessiones-lat_knoll-csel33.txt`

Lines -8 +8:

```text
before:
Provenance note: Mechanically extracted from the item's own djvu.txt; front-cover scan noise stripped before the title page. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note (independent review, Round 18; extended, Round 19; extended, Round 20): quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1896), independently confirmed distinct from the in-copyright-adjacent 1962 Johnson Reprint of the same text (that reprint's own item was opened only to confirm it carries a 1962 reprint notice, and was not used as this file's source).
after:
Provenance note: Mechanically extracted from the item's own djvu.txt; front-cover scan noise stripped before the title page. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note: quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1896), independently confirmed distinct from the in-copyright-adjacent 1962 Johnson Reprint of the same text (that reprint's own item was opened only to confirm it carries a 1962 reprint notice, and was not used as this file's source).
```

## `cic/texts/augustine_doctrina-christiana-enchiridion-lat_bruder1838.txt`

Lines -8 +8:

```text
before:
Provenance note: Mechanically extracted from the item's own djvu.txt; minimal front-matter scan noise stripped. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note (independent review, Round 18; extended, Round 19; extended, Round 20): quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1838) and by archive.org's own rights determination.
after:
Provenance note: Mechanically extracted from the item's own djvu.txt; minimal front-matter scan noise stripped. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note: quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1838) and by archive.org's own rights determination.
```

## `cic/texts/augustine_enarrationes-in-psalmos-lat_migne-pl36-37.txt`

Lines -8 +8:

```text
before:
Provenance note: Mechanically extracted from the item's own djvu.txt. Front matter stripped: Google's digitization notice, and Migne's own lengthy general advertisement for the whole Patrologia series (pricing, volume counts, subscription terms) that precedes this specific volume's title page -- kept only from "PATROLOGIAE LATINAE TOMUS XXXVI" onward. Back matter stripped: "Digitized by Google" scan markers and a Harvard College Widener Library overdue-fee notice, both scan artifacts unrelated to the text. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note (independent review, Round 17; extended, Round 18; extended, Round 19; extended, Round 20): quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1861).
after:
Provenance note: Mechanically extracted from the item's own djvu.txt. Front matter stripped: Google's digitization notice, and Migne's own lengthy general advertisement for the whole Patrologia series (pricing, volume counts, subscription terms) that precedes this specific volume's title page -- kept only from "PATROLOGIAE LATINAE TOMUS XXXVI" onward. Back matter stripped: "Digitized by Google" scan markers and a Harvard College Widener Library overdue-fee notice, both scan artifacts unrelated to the text. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note: quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1861).
```

## `cic/texts/augustine_epistulae-1-123-lat_goldbacher-csel34.txt`

Lines -8 +8:

```text
before:
Provenance note: Mechanically extracted from the item's own djvu.txt; front-cover scan noise stripped before the title page. Corrected here (independent review, Round 17): the back-cover Getty Center Library barcode ("GETTY CENTER LIBRARY" / call number) was NOT fully stripped -- it survives as the file's own last content lines, after the final letter's apparatus; disclosed here rather than silently left, an earlier draft of this note wrongly claimed it was removed. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note (independent review, Round 18; extended, Round 19; extended, Round 20): quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1895/1898).
after:
Provenance note: Mechanically extracted from the item's own djvu.txt; front-cover scan noise stripped before the title page. The back-cover Getty Center Library barcode ("GETTY CENTER LIBRARY" / call number) was NOT fully stripped -- it survives as the file's own last content lines, after the final letter's apparatus. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note: quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1895/1898).
```

## `cic/texts/augustine_epistulae-124-184a-lat_goldbacher-csel44.txt`

Lines -8,2 +8,2:

```text
before:
Provenance note: Mechanically extracted from the item's own djvu.txt; front-cover scan noise stripped before the title page. Corrected here (independent review, Round 17): the back-cover Getty Center Library barcode was NOT fully stripped -- it survives as the file's own last content lines, after the final letter's apparatus; disclosed here rather than silently left, an earlier draft of this note wrongly claimed it was removed. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note (independent review, Round 18; extended, Round 19; extended, Round 20): quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1904).
Content note: Covers Epistulae 124-184A. Corrected here (independent review, Round 16): this file does NOT include Letter 185 (the Correction of the Donatists, already independently vendored in NPNF1-04 English translation and cited at Registry row 12) -- an earlier draft of this note wrongly claimed it did. Letter 185 opens the NEXT part of Goldbacher's edition, CSEL 57 Pars IV (Registry row 193), not this Pars III file. Running Latin text is clean throughout, including at the collection's own true end; the apparatus criticus carries the usual sigla-level noise.
after:
Provenance note: Mechanically extracted from the item's own djvu.txt; front-cover scan noise stripped before the title page. The back-cover Getty Center Library barcode was NOT fully stripped -- it survives as the file's own last content lines, after the final letter's apparatus. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note: quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1904).
Content note: Covers Epistulae 124-184A. This file does NOT include Letter 185 (the Correction of the Donatists, already independently vendored in NPNF1-04 English translation and cited at Registry row 12). Letter 185 opens the NEXT part of Goldbacher's edition, CSEL 57 Pars IV (Registry row 193), not this Pars III file. Running Latin text is clean throughout, including at the collection's own true end; the apparatus criticus carries the usual sigla-level noise.
```

## `cic/texts/augustine_epistulae-critical_goldbacher-csel57-pars4.txt`

Lines -7,3 +7,3:

```text
before:
Source: Mark supplied a compiled docx, 2026-09-05, built from an archive.org-hosted "Full text" / "See other formats" view of an Internet Archive scan -- corrected here, independent review Round 23's own M1, from an earlier draft's own "a Google Books scan": the source item's own metadata carries no sponsor or scanningcenter field pointing at Google, and its own full text contains the word "Google" zero times. The archive.org item identifier, not stated when the file was supplied, is now independently confirmed rather than hedged -- confirmed here, independent review Round 23's own M1: archive.org/details/CSEL57, whose own full text matches this file's own text character for character at both ends (the same test Round 22 applied to the Possidius intake), closing the "very likely the same item... not independently confirmed" hedge this Source line previously carried.
Provenance note: Mechanically extracted from the supplied docx -- archive.org site-navigation chrome was stripped from the head of the file -- corrected here, independent review Round 23's own M1, from an earlier draft's own "archive.org/Google Books... chrome and Google's own standard public-domain usage notice," which wrongly attributed this scan's own chrome to Google Books, on the same mistaken basis the Source line above once carried and is corrected there; the "public-domain usage notice" that same earlier draft claimed was stripped is dropped here too, independent review Round 24's own L3, since the source item's own text carries no such notice, so its removal cannot be verified from here and is not claimed. The doubled/tripled inter-word spacing produced by that page's own text export was normalized to single spaces throughout. Nothing else altered -- no OCR error corrected, no apparatus reformatted, no content paraphrased. Rights basis, independently checkable: 1911 is far past the ~95-year US public-domain-by-date threshold this project's own registry uses.
Content note: Covers only Pars IV of Goldbacher's edition -- Epistulae 185 through 270 -- not the full Augustine correspondence Goldbacher edited across CSEL 34/1 (1895), 34/2 (1898), 44 (1904), 57 (1911, this file), and 58 (1923, preface and indices). Corrected here (independent review, Round 18): CSEL 34/1, 34/2, and 44 were vendored 2026-09-08 (Registry rows 195-196) -- an earlier draft of this note wrongly said Manifest G4 stayed open for all of these; G4 now stays open only for CSEL 58 (praefatio and indices, no letter text of its own). This is a Latin-only critical edition (no facing translation, unlike the Possidius/Weiskotten intake) -- original-language witness, second-witness caveat applies per cic/texts/INTAKE.md: never primary evidence for a Representative on its own, only for cross-checking a specific reading against the vendored NPNF English translation (npnf101_augustine-confessions-letters.xml) this world's own records actually cite. OCR quality is measurably worse here than in this project's two other recent Latin intakes (the Hartel Cyprian and Codex Theodosianus files): the running Latin letter text reads coherently at every point sampled across the full document, including the collection's own final lines (Epistle 270's own closing), but a direct paragraph-level scan found roughly 2.6% of all paragraphs (636 of 24,350) containing heavy runs of garbage OCR symbols, concentrated in the dense apparatus criticus and editorial notes -- at least one specific editorial note (on a letter's transmission history among the Hieronymian correspondence) is essentially unreadable rather than merely noisy. Treat any claim resting on the apparatus -- a specific manuscript reading, an editorial argument about a letter's transmission or authenticity -- as needing independent verification against a clean copy before use; the received body text of the letters themselves is not affected by this and reads reliably throughout.
after:
Source: Mark supplied a compiled docx, 2026-09-05, built from an archive.org-hosted "Full text" / "See other formats" view of an Internet Archive scan, not a Google Books scan: the source item's own metadata carries no sponsor or scanningcenter field pointing at Google, and its own full text contains the word "Google" zero times. The archive.org item, not stated when the file was supplied, is archive.org/details/CSEL57, whose own full text matches this file's own text character for character at both ends.
Provenance note: Mechanically extracted from the supplied docx -- archive.org site-navigation chrome was stripped from the head of the file; the source item's own text carries no public-domain usage notice, so none is claimed stripped. The doubled/tripled inter-word spacing produced by that page's own text export was normalized to single spaces throughout. Nothing else altered -- no OCR error corrected, no apparatus reformatted, no content paraphrased. Rights basis, independently checkable: 1911 is far past the ~95-year US public-domain-by-date threshold this project's own registry uses.
Content note: Covers only Pars IV of Goldbacher's edition -- Epistulae 185 through 270 -- not the full Augustine correspondence Goldbacher edited across CSEL 34/1 (1895), 34/2 (1898), 44 (1904), 57 (1911, this file), and 58 (1923, preface and indices). CSEL 34/1, 34/2, and 44 were vendored 2026-09-08 (Registry rows 195-196); CSEL 58 (praefatio and indices, no letter text of its own) is not vendored. This is a Latin-only critical edition (no facing translation, unlike the Possidius/Weiskotten intake) -- original-language witness, second-witness caveat applies per cic/texts/INTAKE.md: never primary evidence for a Representative on its own, only for cross-checking a specific reading against the vendored NPNF English translation (npnf101_augustine-confessions-letters.xml) this world's own records actually cite. OCR quality is measurably worse here than in this project's two other recent Latin intakes (the Hartel Cyprian and Codex Theodosianus files): the running Latin letter text reads coherently at every point sampled across the full document, including the collection's own final lines (Epistle 270's own closing), but a direct paragraph-level scan found roughly 2.6% of all paragraphs (636 of 24,350) containing heavy runs of garbage OCR symbols, concentrated in the dense apparatus criticus and editorial notes -- at least one specific editorial note (on a letter's transmission history among the Hieronymian correspondence) is essentially unreadable rather than merely noisy. Treat any claim resting on the apparatus -- a specific manuscript reading, an editorial argument about a letter's transmission or authenticity -- as needing independent verification against a clean copy before use; the received body text of the letters themselves is not affected by this and reads reliably throughout.
```

## `cic/texts/augustine_retractationes-lat_knoll-csel36.txt`

Lines -8 +8:

```text
before:
Provenance note: Mechanically extracted from the item's own djvu.txt; back-cover Getty Center Library barcode stripped after the closing indices. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note (independent review, Round 18; extended, Round 19; extended, Round 20): quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1902).
after:
Provenance note: Mechanically extracted from the item's own djvu.txt; back-cover Getty Center Library barcode stripped after the closing indices. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note: quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1902).
```

## `cic/texts/avvakum_zhitie-protopopa-avvakuma-orv_wikisource-transcription-nd.txt`

Lines -8 +8:

```text
before:
Provenance note: This world's own primary evidence in its own right, per INTAKE.md's real, current rule (Mark's ruling, 2026-09-25): language does not decide whether a source is primary, credibility and truth do. Two real, disclosed quotability caveats remain independent of that question: this transcription's own chain from manuscript to critical edition to az.lib.ru to Wikisource has not been independently verified hop by hop (az.lib.ru itself was unreachable from the vendoring session's own network egress allowlist), and it carries 116 bracketed modern-Russian editorial glosses interpolated directly into the running sentences (e.g. "[правое]", "[потому что]") -- a modern annotated reading edition's own apparatus, not Avvakum's words; strip before quoting. TRANSCRIPTION CONVENTION: quotations drawn from this file are given exactly as the file prints them, including its own editorial bracketed variant readings where a quoted passage does not cross one; no wording, spelling, or such reading is silently altered. MediaWiki markup ({{Otekste}} infobox, wiki-emphasis markup, wikilink brackets) stripped mechanically; non-breaking spaces normalized to plain spaces.
after:
Provenance note: This world's own primary evidence in its own right. Two real, disclosed quotability caveats remain independent of that question: this transcription's own chain from manuscript to critical edition to az.lib.ru to Wikisource has not been independently verified hop by hop (az.lib.ru itself was unreachable from the vendoring session's own network egress allowlist), and it carries 116 bracketed modern-Russian editorial glosses interpolated directly into the running sentences (e.g. "[правое]", "[потому что]") -- a modern annotated reading edition's own apparatus, not Avvakum's words; strip before quoting. TRANSCRIPTION CONVENTION: quotations drawn from this file are given exactly as the file prints them, including its own editorial bracketed variant readings where a quoted passage does not cross one; no wording, spelling, or such reading is silently altered. MediaWiki markup ({{Otekste}} infobox, wiki-emphasis markup, wikilink brackets) stripped mechanically; non-breaking spaces normalized to plain spaces.
```

## `cic/texts/barlow-william_summe-and-substance-hampton-court-conference_1804.txt`

Lines -7 +7:

```text
before:
Provenance note: Header prepended; the OCR text follows unchanged (zero long-s substitutions, the download contains no long-s glyph; nothing retyped, dropped or corrected; runs of spaces and page-number lines left as scanned). Rights basis restated: the host catalogues this printing as 1804 and the text is a 1604 work, so it is public domain by date either way; the 1804 imprint line itself is not legible in the OCR. SECOND WITNESS for exact wording (Mark's OCR ruling, 2026-09-25): this printing used the long-s and the OCR has already rendered it as "f" throughout ("pleafed", "Bifhops"), which cannot be reversed mechanically without touching real f's, so the text is left as scanned and a quote must be checked against the page image.
after:
Provenance note: Header prepended; the OCR text follows unchanged (zero long-s substitutions, the download contains no long-s glyph; nothing retyped, dropped or corrected; runs of spaces and page-number lines left as scanned). Rights basis restated: the host catalogues this printing as 1804 and the text is a 1604 work, so it is public domain by date either way; the 1804 imprint line itself is not legible in the OCR. SECOND WITNESS for exact wording: this printing used the long-s and the OCR has already rendered it as "f" throughout ("pleafed", "Bifhops"), which cannot be reversed mechanically without touching real f's, so the text is left as scanned and a quote must be checked against the page image.
```

## `cic/texts/boehmer_urkunden-bauernkrieg-wiedertaeufer-deu_1910.txt`

Lines -9 +9:

```text
before:
Content note: Vendored for its section IV, "Die sieben Artikel von Schlatt am Randen", Böhmer's edition of the German text of the Schleitheim articles (1527) with his variant notes; sections I-III (the peasants' Twelve Articles, the question of their author, the Memmingen articles) are the peasants' war, outside this world, present in the file but not assigned. SECOND WITNESS for scan quality (Mark's OCR ruling, 2026-09-25): the document texts are set in Fraktur and their OCR is garbled, while Böhmer's Antiqua introductions and notes are clean; sampled at five points. It is vendored because it is the only public-domain printing found of the full German Schleitheim text (Beck 1883, Beilage A, prints it abridged), against which the once-removed English of McGlothlin 1911 and Jackson 1901 can be checked on the page images.
after:
Content note: Vendored for its section IV, "Die sieben Artikel von Schlatt am Randen", Böhmer's edition of the German text of the Schleitheim articles (1527) with his variant notes; sections I-III (the peasants' Twelve Articles, the question of their author, the Memmingen articles) are the peasants' war, outside this world, present in the file but not assigned. SECOND WITNESS for scan quality: the document texts are set in Fraktur and their OCR is garbled, while Böhmer's Antiqua introductions and notes are clean; sampled at five points. It is vendored because it is the only public-domain printing found of the full German Schleitheim text (Beck 1883, Beilage A, prints it abridged), against which the once-removed English of McGlothlin 1911 and Jackson 1901 can be checked on the page images.
```

## `cic/texts/codex-canonum-ecclesiae-africanae_bruns-pars1-1839.txt`

Lines -8 +8:

```text
before:
Provenance note: Mechanically extracted from the item's own djvu.txt; Google's digitization notice and a Harvard library bookplate/gift stamp ("The Gift of Col. Benjamin Loring") stripped from the front, trailing decorative scan noise stripped from the tail after the Corrigenda. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note (independent review, Round 17; extended, Round 18; extended, Round 19; extended, Round 20): quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1839).
after:
Provenance note: Mechanically extracted from the item's own djvu.txt; Google's digitization notice and a Harvard library bookplate/gift stamp ("The Gift of Col. Benjamin Loring") stripped from the front, trailing decorative scan noise stripped from the tail after the Corrigenda. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note: quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1839).
```

## `cic/texts/cyprian_opera-omnia-critical_hartel-csel3-pars1-2.txt`

Lines -7,3 +7,3:

```text
before:
Source: Mark supplied a compiled docx, 2026-09-05, built from an archive.org-hosted "Full text" / "See other formats" view of a Google Books scan of the 1965 Johnson Reprint Corporation reprint. The exact archive.org item identifier, not stated when the file was supplied, is now independently confirmed rather than guessed -- confirmed here, independent review Round 24's own M3: sthascicaecilic01hartgoog (sponsor: Google, source: books.google.com), whose own full text matches this file's own text character for character at both ends (the same test applied to the Possidius and Goldbacher intakes, Registry rows 192 and 193), and whose own metadata carries the 1868 date and NOT_IN_COPYRIGHT status this file's own Rights line above states independently (corrected here, independent review Round 25's own C5, from an earlier draft's own "this row's own rights basis," a phrase written for Source_Registry.md row 191 and left uncorrected when reused here, where this file's header has a Rights line, not a row).
Provenance note: Mechanically extracted from the supplied docx -- archive.org/Google Books site-navigation chrome and Google's own standard public-domain usage notice (both present at the head of what was supplied) were stripped; the doubled/tripled inter-word spacing produced by that page's own text export was normalized to single spaces throughout. Corrected here, independent review Round 23's own L3: a further line of site chrome -- the archive.org item's own page-title metadata string, "S. Thasci Caecili Cypriani Opera omnia," which survived the extraction at the file's own tail rather than its head -- was found and removed; it is not part of Hartel's own printed text (the running apparatus already ends cleanly one line before it, at the close of Epistle 81) and its removal changes no content. The identical class of tail-chrome survival was already caught and fixed at the Possidius intake the same day (row 192); this file's own tail had not been checked the same way until now. Nothing else altered -- no OCR error corrected, no apparatus reformatted, no content paraphrased. Rights basis, independently checkable: Hartel's edition (1868/1871) is far past the ~95-year US public-domain-by-date threshold this project's own registry uses; Google's own embedded notice separately treats the scanned copy as public domain; the 1965 Johnson Reprint Corporation printing is a photomechanical reprint of that same public-domain text and creates no new claim over it.
Content note: Covers CSEL 3 Pars I (the treatises, ending with the Sententiae Episcoporum -- the 87 bishops' sentences at the Council of Carthage, 256) and Pars II (Epistulae I-LXXXI) in full; the document ends cleanly at the close of Epistle 81, no truncation found. Does NOT include CSEL 3 Pars III (spuria, the Vita Caecilii Cypriani, and the Acta Proconsularia) -- a separate volume, vendored 2026-09-08 at cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt (Registry row 194; corrected here, independent review Round 18, from an earlier draft that called Pars III still-unacquired and Manifest G1 still open -- G1 is now closed in full, Pars I through III all vendored). OCR quality is uneven by section: the running Latin text of the treatises and letters reads cleanly and coherently throughout every section sampled (including the very end); the apparatus criticus (the dense textual-variant footnotes) carries meaningfully more OCR noise -- garbled manuscript sigla, occasional stray characters -- consistent with how dense critical apparatus typically degrades under OCR even in an otherwise-clean scan. Treat any claim resting on a specific manuscript reading or textual variant (as opposed to the received text itself) as needing independent verification against a second source before use.
after:
Source: Mark supplied a compiled docx, 2026-09-05, built from an archive.org-hosted "Full text" / "See other formats" view of a Google Books scan of the 1965 Johnson Reprint Corporation reprint. The exact archive.org item identifier, not stated when the file was supplied, is sthascicaecilic01hartgoog (sponsor: Google, source: books.google.com), whose own full text matches this file's own text character for character at both ends (the same test applied to the Possidius and Goldbacher intakes, Registry rows 192 and 193), and whose own metadata carries the 1868 date and NOT_IN_COPYRIGHT status this file's own Rights line above states independently.
Provenance note: Mechanically extracted from the supplied docx -- archive.org/Google Books site-navigation chrome and Google's own standard public-domain usage notice (both present at the head of what was supplied) were stripped; the doubled/tripled inter-word spacing produced by that page's own text export was normalized to single spaces throughout. A further line of site chrome -- the archive.org item's own page-title metadata string, "S. Thasci Caecili Cypriani Opera omnia," which survived the extraction at the file's own tail rather than its head -- was found and removed; it is not part of Hartel's own printed text (the running apparatus already ends cleanly one line before it, at the close of Epistle 81) and its removal changes no content. The identical class of tail-chrome survival was already caught and fixed at the Possidius intake the same day (row 192); this file's own tail had not been checked the same way until now. Nothing else altered -- no OCR error corrected, no apparatus reformatted, no content paraphrased. Rights basis, independently checkable: Hartel's edition (1868/1871) is far past the ~95-year US public-domain-by-date threshold this project's own registry uses; Google's own embedded notice separately treats the scanned copy as public domain; the 1965 Johnson Reprint Corporation printing is a photomechanical reprint of that same public-domain text and creates no new claim over it.
Content note: Covers CSEL 3 Pars I (the treatises, ending with the Sententiae Episcoporum -- the 87 bishops' sentences at the Council of Carthage, 256) and Pars II (Epistulae I-LXXXI) in full; the document ends cleanly at the close of Epistle 81, no truncation found. Does NOT include CSEL 3 Pars III (spuria, the Vita Caecilii Cypriani, and the Acta Proconsularia) -- a separate volume, vendored 2026-09-08 at cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt (Registry row 194); Pars I through III are all vendored. OCR quality is uneven by section: the running Latin text of the treatises and letters reads cleanly and coherently throughout every section sampled (including the very end); the apparatus criticus (the dense textual-variant footnotes) carries meaningfully more OCR noise -- garbled manuscript sigla, occasional stray characters -- consistent with how dense critical apparatus typically degrades under OCR even in an otherwise-clean scan. Treat any claim resting on a specific manuscript reading or textual variant (as opposed to the received text itself) as needing independent verification against a second source before use.
```

## `cic/texts/cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt`

Lines -7,3 +7,3:

```text
before:
Source: archive.org item corpusscriptorum03cypruoft (contributor: Trinity College, University of Toronto; scanned 2006), full text at https://archive.org/download/corpusscriptorum03cypruoft/corpusscriptorum03cypruoft_djvu.txt. Fetched directly by this build thread 2026-09-08, closing this world's own Source_Acquisition_Manifest G1 request's open Pars III gap. A sibling research session (session_01WLxhNbVhjkf1R2SAh8dxxT, branch claude/latin-pastoral-source-integration) had independently located and vendored closely related material from the same edition; this file was independently re-fetched and re-verified against archive.org directly rather than adopted from that session's own copy.
Provenance note: Mechanically extracted from the item's own djvu.txt. Front-matter scan noise (a Trinity College Toronto library flyleaf stamp) stripped before the title page. The scanned volume is physically bound together with CSEL 4 (Arnobius, Adversus Nationes, ed. Reifferscheid, 1875); that second, unrelated work begins immediately after this file's own end and was cut entirely, not included. Doubled inter-word spacing (an OCR/scan artifact) normalized to single spaces; nothing else altered, no OCR error corrected. Note (independent review, Round 17; extended, Round 18; extended, Round 19; extended, Round 20): quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1871), independently confirmed by archive.org's own rights metadata.
Content note: The volume's own title page (lines 27 and 52-54) names three things -- Opera Spuria, Indices, Praefatio -- corrected here, independent review Round 25's own M3, from an earlier draft that said the title page names five, in the same clause that quotes it. This file's own physical contents, in sequence, are: (1) Cyprian's own spuria (works transmitted under his name but not by him), from line 78; (2) three indices, not two -- corrected here, Round 25's own M3, from an earlier draft that omitted the largest of them: a scriptural index (INDEX SCRIPTORVM, line 18617), a name/subject index (Index nominum et rerum, line 27256), and a word/phrase index (INDEX VERBORVM ET LOCVTIONVM, line 27335, roughly 20% of the file, the largest of the three); (3) the editorial Praefatio (line 36057); (4) the Vita Caecilii Cypriani attributed to Pontius the deacon (line 40258; title page: "VITA CAECILII CYPRIANI (Pontio diacono uulgo adscripta)"); (5) the Acta Proconsularia (Cyprian's own trial and martyrdom record, line 41413); and (6) a further index of works, INDEX OPERVM (line 41629), running to the file's own end -- corrected here, Round 25's own M3, from an earlier draft that ended its own enumeration at the Acta, roughly 970 lines before the file's actual end. This is the Latin original standing behind the already-vendored ANF05 English translation of Pontius's Life (Registry row 7). The apparatus criticus is noisier than the running text throughout; the running Latin text itself reads coherently, including at the Vita's own end.
after:
Source: archive.org item corpusscriptorum03cypruoft (contributor: Trinity College, University of Toronto; scanned 2006), full text at https://archive.org/download/corpusscriptorum03cypruoft/corpusscriptorum03cypruoft_djvu.txt. Fetched directly by this build thread 2026-09-08, closing this world's own Source_Acquisition_Manifest G1 request's open Pars III gap. This file was fetched and verified against archive.org directly.
Provenance note: Mechanically extracted from the item's own djvu.txt. Front-matter scan noise (a Trinity College Toronto library flyleaf stamp) stripped before the title page. The scanned volume is physically bound together with CSEL 4 (Arnobius, Adversus Nationes, ed. Reifferscheid, 1875); that second, unrelated work begins immediately after this file's own end and was cut entirely, not included. Doubled inter-word spacing (an OCR/scan artifact) normalized to single spaces; nothing else altered, no OCR error corrected. Note: quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1871), independently confirmed by archive.org's own rights metadata.
Content note: The volume's own title page (lines 27 and 52-54) names three things -- Opera Spuria, Indices, Praefatio. This file's own physical contents, in sequence, are: (1) Cyprian's own spuria (works transmitted under his name but not by him), from line 78; (2) three indices, the largest of them a scriptural index (INDEX SCRIPTORVM, line 18617), a name/subject index (Index nominum et rerum, line 27256), and a word/phrase index (INDEX VERBORVM ET LOCVTIONVM, line 27335, roughly 20% of the file, the largest of the three); (3) the editorial Praefatio (line 36057); (4) the Vita Caecilii Cypriani attributed to Pontius the deacon (line 40258; title page: "VITA CAECILII CYPRIANI (Pontio diacono uulgo adscripta)"); (5) the Acta Proconsularia (Cyprian's own trial and martyrdom record, line 41413); and (6) a further index of works, INDEX OPERVM (line 41629), running to the file's own end. This is the Latin original standing behind the already-vendored ANF05 English translation of Pontius's Life (Registry row 7). The apparatus criticus is noisier than the running text throughout; the running Latin text itself reads coherently, including at the Vita's own end.
```

## `cic/texts/delehaye_passions-martyrs-genres-litteraires-fra_1921.txt`

Lines -8 +8:

```text
before:
Provenance note: Mechanically extracted from the item's own djvu.txt; front-matter Internet Archive digitization notice stripped before the title page. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note (independent review, Round 18; extended, Round 19; extended, Round 20): quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1921).
after:
Provenance note: Mechanically extracted from the item's own djvu.txt; front-matter Internet Archive digitization notice stripped before the title page. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note: quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1921).
```

## `cic/texts/didymus-alexandria_de-trinitate-lat-grc_mingarelli1769.txt`

Lines -44,6 +44,6:

```text
before:
                  file) — corrected 2026-09-08, Round 1 Opus review,
                  from this note's own original conflation of the two
                  headings.
                  **Corrected 2026-09-08, Round 1 Opus review, from
                  this note's own original claim, which was checked
                  and found false:** a full Unicode census of this
after:
                  file), not at the first one.
                  The Greek text is not in this
                  file. That is a counted fact,
                  not an impression drawn from
                  sampling the scan:
                  a full Unicode census of this
```

## `cic/texts/franck_paradoxa-deu_rab1559.txt`

Lines -9 +9:

```text
before:
Content note: The whole print: title page, Franck's Vorred (from about file line 550), then the 280 numbered Paradoxa with their Latin and German theses and Franck's expositions, with the running head "Paradoxa" and printed leaf numbers, and a register. Franck's central statement of his spiritualist theology (the invisible church, the inner Word, Scripture as letter). SECOND WITNESS for exact wording: Google-digitised OCR of a Fraktur print, sampled at five points and found garbled in part (about 0.75 of tokens read as words; "f" for long s in many words, broken words); use it to locate passages and verify against the page images (Mark's OCR ruling, 2026-09-25). A 1558 printing by the same press (item bub_gb_4fk7AAAAcAAJ) reads slightly worse (0.74). The 1909 Jena edition in modernised German (item paradoxa00franuoft, ed. Heinrich Ziegler) is set in Fraktur and reads worse still (0.66). No public-domain English translation exists (Furcha's 280 Paradoxes, 1986, is in copyright).
after:
Content note: The whole print: title page, Franck's Vorred (from about file line 550), then the 280 numbered Paradoxa with their Latin and German theses and Franck's expositions, with the running head "Paradoxa" and printed leaf numbers, and a register. Franck's central statement of his spiritualist theology (the invisible church, the inner Word, Scripture as letter). SECOND WITNESS for exact wording: Google-digitised OCR of a Fraktur print, sampled at five points and found garbled in part (about 0.75 of tokens read as words; "f" for long s in many words, broken words); use it to locate passages and verify against the page images. A 1558 printing by the same press (item bub_gb_4fk7AAAAcAAJ) reads slightly worse (0.74). The 1909 Jena edition in modernised German (item paradoxa00franuoft, ed. Heinrich Ziegler) is set in Fraktur and reads worse still (0.66). No public-domain English translation exists (Furcha's 280 Paradoxes, 1986, is in copyright).
```

## `cic/texts/gerlach_tage-buch-deu_1674.txt`

Lines -9 +9:

```text
before:
Content note: SECOND WITNESS (Mark's OCR ruling, 2026-09-25): the Fraktur OCR is readable word by word, but the page's two columns and its marginal glosses are interleaved line by line, so sentences run into each other and no passage can be quoted without checking the page images. Order in the file: MDZ catalogue stub, title page (about line 100-130, imprint 'Getruckt bey Heinrich Friesen, 1674'), Wagner's preface ('Ausfuehrliche Vorrede', from about line 234, including a 'Vorrede vom Tuerck. Reich'), then the diary itself, kept by date from 1573 to 1578 with month and day headings as printed (for example 'Anno 1577.' at about line 50198), and a Register (index) from about line 59617. The preface names the Greek churchmen Gerlach spoke with, among them Patriarch Jeremias, Metropolitan Metrophanes of Berrhoea and the Zygomalas father and son (about file line 1311); an outside Lutheran eyewitness, not the church's own voice. German.
after:
Content note: SECOND WITNESS: the Fraktur OCR is readable word by word, but the page's two columns and its marginal glosses are interleaved line by line, so sentences run into each other and no passage can be quoted without checking the page images. Order in the file: MDZ catalogue stub, title page (about line 100-130, imprint 'Getruckt bey Heinrich Friesen, 1674'), Wagner's preface ('Ausfuehrliche Vorrede', from about line 234, including a 'Vorrede vom Tuerck. Reich'), then the diary itself, kept by date from 1573 to 1578 with month and day headings as printed (for example 'Anno 1577.' at about line 50198), and a Register (index) from about line 59617. The preface names the Greek churchmen Gerlach spoke with, among them Patriarch Jeremias, Metropolitan Metrophanes of Berrhoea and the Zygomalas father and son (about file line 1311); an outside Lutheran eyewitness, not the church's own voice. German.
```

## `cic/texts/gregory-nyssa_life-of-macrina-introduction-only_clarke1916.txt`

Lines -9 +9:

```text
before:
STILL NEEDED: the actual translated Vita Macrinae narrative -- the "Next Page" content from the same Pearse/tertullian.org transcription this Introduction came from, not yet supplied.
after:
Content note (scope): the translated Vita Macrinae narrative itself, the "Next Page" content of the same Pearse/tertullian.org transcription, is not in this file.
```

## `cic/texts/harnack_vita-cypriani-commentary-lat-deu_1913.txt`

Lines -8 +8:

```text
before:
Provenance note: Mechanically extracted from the bound volume's own djvu.txt, sliced to Harnack's own Heft 3 only (the source item binds several independent Hefte by different authors into one continuous scan). The bulk of the immediately preceding material in the bound scan (a Hinrichs publisher's advertisement list of other, unrelated Texte und Untersuchungen volumes) was cut as front matter; two trailing lines of that same list (a final catalogue entry and the words "Fortsetzung s. Seite III d. UraschlagR.", the file's own OCR of "Fortsetzung s. Seite III d. Umschlags" -- quoted here as it actually reads, corrected from an earlier draft that silently normalized it, per independent review's own C3 finding, Round 16) survive at the very start of this file, immediately before the "DAS LEBEN CYPRIANS" title page -- disclosed here rather than silently left, per independent review's own C1 finding (Round 15) -- and the file ends immediately before Heft 4 (Josef Martin's Studien und Beiträge zur Geschichte Commodians) begins. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note (independent review, Round 18; extended, Round 19; extended, Round 20): quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1913).
after:
Provenance note: Mechanically extracted from the bound volume's own djvu.txt, sliced to Harnack's own Heft 3 only (the source item binds several independent Hefte by different authors into one continuous scan). The bulk of the immediately preceding material in the bound scan (a Hinrichs publisher's advertisement list of other, unrelated Texte und Untersuchungen volumes) was cut as front matter; two trailing lines of that same list (a final catalogue entry and the words "Fortsetzung s. Seite III d. UraschlagR.", the file's own OCR of "Fortsetzung s. Seite III d. Umschlags" -- quoted here as it actually reads) survive at the very start of this file, immediately before the "DAS LEBEN CYPRIANS" title page -- and the file ends immediately before Heft 4 (Josef Martin's Studien und Beiträge zur Geschichte Commodians) begins. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note: quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1913).
```

## `cic/texts/hubmaier_form-des-nachtmals-bann-freiheit-des-willens-deu_1527.txt`

Lines -9 +9:

```text
before:
Content note: Three pieces of 1527 read in the OCR in this order: the order of the Lord's Supper ("was Form solch Nachtmal ze Nicolspurg gehalten", from the start), the treatise on the Christian ban ("Von dem christlichen Bann", with its Bannschriften), and the first treatise on the freedom of the will ("die Freyhait des Willens im Menschen", from about the last third). German, blackletter on microfilm. SECOND WITNESS for scan quality (Mark's OCR ruling, 2026-09-25): sampled at five points the word-like share runs about 0.5 to 0.7, and about 84 percent of 400-character windows read at or above half word-like; long-s, "ii" for "ü" and "r" for "t" are frequent. Nothing is quotable until read on the page images. Identification rests on the headings and phrases read in the OCR.
after:
Content note: Three pieces of 1527 read in the OCR in this order: the order of the Lord's Supper ("was Form solch Nachtmal ze Nicolspurg gehalten", from the start), the treatise on the Christian ban ("Von dem christlichen Bann", with its Bannschriften), and the first treatise on the freedom of the will ("die Freyhait des Willens im Menschen", from about the last third). German, blackletter on microfilm. SECOND WITNESS for scan quality: sampled at five points the word-like share runs about 0.5 to 0.7, and about 84 percent of 400-character windows read at or above half word-like; long-s, "ii" for "ü" and "r" for "t" are frequent. Nothing is quotable until read on the page images. Identification rests on the headings and phrases read in the OCR.
```

## `cic/texts/hubmaier_freiwilligkeit-des-menschen-und-von-dem-schwert-deu_1527.txt`

Lines -9 +9:

```text
before:
Content note: Two pieces of 1527 read in the OCR: the second treatise on the free will of man ("Freywilligkait", from the start, with Pharaoh, Esau and Jacob as its examples) and the treatise on the sword ("Von dem Schwert", answering the brethren who say a Christian may not bear the sword, from about the last third, with the heading on the two swords and the Christian magistrate). German, blackletter on microfilm. SECOND WITNESS for scan quality (Mark's OCR ruling, 2026-09-25): sampled at five points the word-like share runs about 0.5 to 0.7, and about 86 percent of 400-character windows read at or above half word-like. Nothing is quotable until read on the page images. The English of On the Sword is in the vendored Vedder 1905 appendix, which this original can be checked against on the page images.
after:
Content note: Two pieces of 1527 read in the OCR: the second treatise on the free will of man ("Freywilligkait", from the start, with Pharaoh, Esau and Jacob as its examples) and the treatise on the sword ("Von dem Schwert", answering the brethren who say a Christian may not bear the sword, from about the last third, with the heading on the two swords and the Christian magistrate). German, blackletter on microfilm. SECOND WITNESS for scan quality: sampled at five points the word-like share runs about 0.5 to 0.7, and about 86 percent of 400-character windows read at or above half word-like. Nothing is quotable until read on the page images. The English of On the Sword is in the vendored Vedder 1905 appendix, which this original can be checked against on the page images.
```

## `cic/texts/hubmaier_gesprech-auf-zwinglis-taufbuechlein-deu_froschauer1526.txt`

Lines -9 +9:

```text
before:
Content note: Hubmaier's dialogue against Zwingli's Taufbüchlein (1526), with, by its own announcement in the text, an answer to the mocking dialogue of certain preachers at Basel. German (early New High German), set in blackletter and photographed on microfilm. SECOND WITNESS for scan quality (Mark's OCR ruling, 2026-09-25): sampled at five points (10/30/50/70/90 percent) the word-like share of tokens runs from about 0.3 (title page and end noise) to 0.6 in the body; about 60 percent of 400-character windows read at or above half word-like. Nothing is quotable from this file until each passage is read on the page images. Vendored because no cleaner public-domain printing of Hubmaier's own German works exists on a reachable host (the 1962 critical edition is in copyright). Identification of the work rests on the title-page words and colophon read in the OCR, not on a catalogue description.
after:
Content note: Hubmaier's dialogue against Zwingli's Taufbüchlein (1526), with, by its own announcement in the text, an answer to the mocking dialogue of certain preachers at Basel. German (early New High German), set in blackletter and photographed on microfilm. SECOND WITNESS for scan quality: sampled at five points (10/30/50/70/90 percent) the word-like share of tokens runs from about 0.3 (title page and end noise) to 0.6 in the body; about 60 percent of 400-character windows read at or above half word-like. Nothing is quotable from this file until each passage is read on the page images. Vendored because no cleaner public-domain printing of Hubmaier's own German works exists on a reachable host (the 1962 critical edition is in copyright). Identification of the work rests on the title-page words and colophon read in the OCR, not on a catalogue description.
```

## `cic/texts/hubmaier_grund-und-ursach-deu_1527.txt`

Lines -9 +9:

```text
before:
Content note: Hubmaier's Grund und Ursach (1527) on the duty of those baptised as infants to be baptised according to Christ's order; the OCR also carries a heading for a Gesprech with preachers at Basel naming "Balthasaren Pacimontanus von Fridberg", and a short Entschuldigung, so the microfilm volume may hold more than one 1527 piece. German, blackletter on microfilm. SECOND WITNESS for scan quality (Mark's OCR ruling, 2026-09-25): sampled at five points, two of the five fall in page noise and the rest read at about 0.6 word-like; about 73 percent of 400-character windows read at or above half word-like. Nothing is quotable until read on the page images. Identification rests on the title-page words read in the OCR.
after:
Content note: Hubmaier's Grund und Ursach (1527) on the duty of those baptised as infants to be baptised according to Christ's order; the OCR also carries a heading for a Gesprech with preachers at Basel naming "Balthasaren Pacimontanus von Fridberg", and a short Entschuldigung, so the microfilm volume may hold more than one 1527 piece. German, blackletter on microfilm. SECOND WITNESS for scan quality: sampled at five points, two of the five fall in page noise and the rest read at about 0.6 word-like; about 73 percent of 400-character windows read at or above half word-like. Nothing is quotable until read on the page images. Identification rests on the title-page words read in the OCR.
```

## `cic/texts/monceaux_histoire-litteraire-afrique-chretienne-tome1_1901.txt`

Lines -8 +8:

```text
before:
Provenance note: Mechanically extracted from the item's own djvu.txt; minimal front-matter library scan noise stripped before the series title page, back-matter University of Toronto library-card-pocket noise stripped after the printer's colophon ("Angers. -- Imprimerie Orientale de A. Burdin et Cie."). Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note (independent review, Round 18; extended, Round 19; extended, Round 20): quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1901).
after:
Provenance note: Mechanically extracted from the item's own djvu.txt; minimal front-matter library scan noise stripped before the series title page, back-matter University of Toronto library-card-pocket noise stripped after the printer's colophon ("Angers. -- Imprimerie Orientale de A. Burdin et Cie."). Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note: quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1901).
```

## `cic/texts/monceaux_histoire-litteraire-afrique-chretienne-tome2_1902.txt`

Lines -8 +8:

```text
before:
Provenance note: Mechanically extracted from the item's own djvu.txt; minimal front-matter library scan noise stripped before the series title page, back-matter University of Toronto library-card-pocket noise stripped after the printer's colophon ("Angers. -- Imprimerie Orientale de A. Burdin et Cie."). Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note (independent review, Round 18; extended, Round 19; extended, Round 20): quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1902).
after:
Provenance note: Mechanically extracted from the item's own djvu.txt; minimal front-matter library scan noise stripped before the series title page, back-matter University of Toronto library-card-pocket noise stripped after the printer's colophon ("Angers. -- Imprimerie Orientale de A. Burdin et Cie."). Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note: quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1902).
```

## `cic/texts/monceaux_histoire-litteraire-afrique-chretienne-tome3_1905.txt`

Lines -8 +8:

```text
before:
Provenance note: Mechanically extracted from the item's own djvu.txt; a Princeton library catalogue-card header and minimal front-matter scan noise stripped before the series title page, back-matter library due-date-card noise stripped after the printer's colophon ("Angers. -- Imprimerie Orientale de A. Burdin et Cie."). Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note (independent review, Round 18; extended, Round 19; extended, Round 20): quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1905; the Bibliotheque nationale de France's own catalogue record gives 1906 for this volume -- both dates are pre-1930 and the PD determination is unaffected either way).
after:
Provenance note: Mechanically extracted from the item's own djvu.txt; a Princeton library catalogue-card header and minimal front-matter scan noise stripped before the series title page, back-matter library due-date-card noise stripped after the printer's colophon ("Angers. -- Imprimerie Orientale de A. Burdin et Cie."). Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note: quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1905; the Bibliotheque nationale de France's own catalogue record gives 1906 for this volume -- both dates are pre-1930 and the PD determination is unaffected either way).
```

## `cic/texts/morebath-parish_churchwardens-accounts-1520-1573_binney1904.txt`

Lines -8 +8:

```text
before:
Content note: The churchwardens' and store-wardens' accounts of one Devon parish, 1520-1573, printed in the original sixteenth-century spelling with the manuscript's abbreviations, preceded by Binney's introduction and followed by Weaver's biographical index. SECOND WITNESS for exact wording (Mark's OCR ruling, 2026-09-25): the Google OCR of this early-modern orthography misreads the superscript abbreviations systematically (for example "y8" or "y*" for the thorn-e "ye", "p'" for "per", roman numerals with stray characters), so a quote must be checked against the page images before it is relied on; the running English is nevertheless readable and searchable. OCR sampled at 10/30/50/70/90 per cent and found of that character throughout. No other public-domain edition of these accounts exists; Duffy's modern edition is in copyright.
after:
Content note: The churchwardens' and store-wardens' accounts of one Devon parish, 1520-1573, printed in the original sixteenth-century spelling with the manuscript's abbreviations, preceded by Binney's introduction and followed by Weaver's biographical index. SECOND WITNESS for exact wording: the Google OCR of this early-modern orthography misreads the superscript abbreviations systematically (for example "y8" or "y*" for the thorn-e "ye", "p'" for "per", roman numerals with stray characters), so a quote must be checked against the page images before it is relied on; the running English is nevertheless readable and searchable. OCR sampled at 10/30/50/70/90 per cent and found of that character throughout. No other public-domain edition of these accounts exists; Duffy's modern edition is in copyright.
```

## `cic/texts/perkins_golden-chaine-and-treatises_legat1600.txt`

Lines -8 +8:

```text
before:
Content note: SECOND WITNESS, not a clean quoting text (Mark's OCR ruling, 2026-09-25): the 1600 black-letter and roman print was OCR'd with systematic long-s misreads (faluation, Chrift, fuch) and broken words at the page edges; sampled at 10/30/50/70/90 per cent and found readable but garbled in every sample. The volume collects several Perkins works: A Golden Chaine in 58 chapters (chapter headings CHAP. n from about line 1255), An Exposition of the Creed (from about line 19809, with running heads 'of the Creede'), An Exposition of the Lords Prayer (about line 34368), A Treatise tending unto a Declaration (contents at line 503), A Case of Conscience, A Direction for the Government of the Tongue (about line 48106), Two Treatises (about line 49737), with the volume's own contents lists at lines 349-569. Use for locating passages; verify any quotation against the page images before it is relied on.
after:
Content note: SECOND WITNESS, not a clean quoting text: the 1600 black-letter and roman print was OCR'd with systematic long-s misreads (faluation, Chrift, fuch) and broken words at the page edges; sampled at 10/30/50/70/90 per cent and found readable but garbled in every sample. The volume collects several Perkins works: A Golden Chaine in 58 chapters (chapter headings CHAP. n from about line 1255), An Exposition of the Creed (from about line 19809, with running heads 'of the Creede'), An Exposition of the Lords Prayer (about line 34368), A Treatise tending unto a Declaration (contents at line 503), A Case of Conscience, A Direction for the Government of the Tongue (about line 48106), Two Treatises (about line 49737), with the volume's own contents lists at lines 349-569. Use for locating passages; verify any quotation against the page images before it is relied on.
```

## `cic/texts/perpetua-scillitan-martyrs-lat-grc_robinson1891.txt`

Lines -8,2 +8,2:

```text
before:
Provenance note: Mechanically extracted from the item's own djvu.txt; front-matter library-microfilm scan noise stripped before the title page, back-matter noise stripped after the printer's colophon ("Cambridge: printed by C. J. Clay, M.A. and Sons, at the University Press"). Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note (independent review, Round 18; extended, Round 19; extended, Round 20): quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1891). The series statement "Texts and Studies I.2" does not itself appear in this scan's own OCR text or catalogue record (the series half-title was evidently not filmed); it is standard bibliography, carried here but not independently verifiable from this item alone.
Content note: This single file carries the Latin/Greek text of BOTH the Passio S. Perpetuae (pp. 60-95, opening "Si uetera fidei exempla...") and, as the volume's own stated Appendix, the Passio Sanctorum Scillitanorum (pp. 112-117, opening with the consular dating formula "Praesente bis et Claudiano consulibus, XVI Kalendas Augustas, Kartagine in secretario inpositis Sperato, Nartzalo et Cittino, Donata, Secunda, Vestia, Saturninus proconsul dixit..."), plus two later Latin recensions of the Scillitan Acts (pp. 118-121). Both texts predate this world's own c. 246 boundary (Scillitan Martyrs, 180 CE; Perpetua, 203 CE) -- the same ground on which this world's own Source_Registry.md row 28 already excludes the (previously English-only) Scillitan Martyrs as a Named Comparandum rather than in-boundary evidence. This original-language file is a second witness for that same excluded comparandum, not new in-boundary evidence, and should be registered accordingly. Corrected here (independent review, Round 17): the Passio S. Perpetuae is NOT unassigned -- it is already assigned to `tertullian-s-voice` (Mark's own 2026-08-26 ruling), and this file's own vendoring adds a second entry to that same world's corpus-map bucket, `source_file: perpetua-scillitan-martyrs-lat-grc_robinson1891.txt`, `role: tradition`, `confidence: assigned`. An earlier draft of this note wrongly claimed the work was unassigned; Source_Registry.md row 204 and this file's own corpus-map staging entry both already record the correction, and this header is brought into line with them.
after:
Provenance note: Mechanically extracted from the item's own djvu.txt; front-matter library-microfilm scan noise stripped before the title page, back-matter noise stripped after the printer's colophon ("Cambridge: printed by C. J. Clay, M.A. and Sons, at the University Press"). Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note: quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1891). The series statement "Texts and Studies I.2" does not itself appear in this scan's own OCR text or catalogue record (the series half-title was evidently not filmed); it is standard bibliography, carried here but not independently verifiable from this item alone.
Content note: This single file carries the Latin/Greek text of BOTH the Passio S. Perpetuae (pp. 60-95, opening "Si uetera fidei exempla...") and, as the volume's own stated Appendix, the Passio Sanctorum Scillitanorum (pp. 112-117, opening with the consular dating formula "Praesente bis et Claudiano consulibus, XVI Kalendas Augustas, Kartagine in secretario inpositis Sperato, Nartzalo et Cittino, Donata, Secunda, Vestia, Saturninus proconsul dixit..."), plus two later Latin recensions of the Scillitan Acts (pp. 118-121). Both texts predate this world's own c. 246 boundary (Scillitan Martyrs, 180 CE; Perpetua, 203 CE) -- the same ground on which this world's own Source_Registry.md row 28 already excludes the (previously English-only) Scillitan Martyrs as a Named Comparandum rather than in-boundary evidence. This original-language file is a second witness for that same excluded comparandum, not new in-boundary evidence, and should be registered accordingly. The Passio S. Perpetuae is NOT unassigned -- it is already assigned to `tertullian-s-voice`, and this file's own vendoring adds a second entry to that same world's corpus-map bucket, `source_file: perpetua-scillitan-martyrs-lat-grc_robinson1891.txt`, `role: tradition`, `confidence: assigned`. Source_Registry.md row 204 and this file's own corpus-map staging entry record the same assignment.
```

## `cic/texts/possidius_vita-augustini_weiskotten1919.txt`

Lines -6,2 +6,2:

```text
before:
Source: Mark supplied a compiled docx, 2026-09-05, built from an archive.org-hosted "Full text" / "See other formats" view of an Internet Archive scan (the University of California, Berkeley library's own copy, per the scanned due-date slip at the physical volume's back) -- corrected here, independent review Round 22's own M2, from an earlier draft's own "a Google Books scan": the source item's own metadata (sponsor: MSN, scanningcenter: rich) is the signature of an Internet Archive/Microsoft Open Content Alliance scan, not a Google Books digitization, and the item's own full text contains the word "Google" zero times. The archive.org item identifier, not stated when the file was supplied, is now independently confirmed rather than guessed -- confirmed here, independent review Round 22's own M1: sanctiaugustiniv00possrich, whose own full text opens with the identical OCR-garbled string this file's own body opens with below ("SANCTI AUGDSTINI VITA / iCRIPTA A POSSIDIO EPISCOPO...") and ends immediately before the same UC Berkeley circulation-desk slip the Provenance note below records stripping.
Provenance note: Mechanically extracted from the supplied docx -- archive.org site-navigation chrome (at the head of what was supplied) was stripped -- corrected here, independent review Round 22's own M2, from an earlier draft's own "archive.org/Google Books... chrome and Google's own standard public-domain usage notice," which wrongly attributed this scan's own chrome to Google Books, on the same mistaken basis the Source line above once carried and is corrected there; the "public-domain usage notice" that same earlier draft claimed was stripped is dropped here too, independent review Round 24's own L3, since the source item's own text carries no such notice, so its removal cannot be verified from here and is not claimed -- as was a scanned UC Berkeley circulation-desk due-date slip bound into the back of the physical volume (a library artifact, not part of the work -- it names loan periods and a phone number, nothing of Possidius's or Weiskotten's own content); the doubled/tripled inter-word spacing produced by that page's own text export was normalized to single spaces throughout. Nothing else altered. Rights basis, independently checkable: 1919 is far past the ~95-year US public-domain-by-date threshold this project's own registry uses, for both the Latin critical text and Weiskotten's own English translation.
after:
Source: Mark supplied a compiled docx, 2026-09-05, built from an archive.org-hosted "Full text" / "See other formats" view of an Internet Archive scan (the University of California, Berkeley library's own copy, per the scanned due-date slip at the physical volume's back), not a Google Books scan: the source item's own metadata (sponsor: MSN, scanningcenter: rich) is the signature of an Internet Archive/Microsoft Open Content Alliance scan, not a Google Books digitization, and the item's own full text contains the word "Google" zero times. The archive.org item identifier, not stated when the file was supplied, is sanctiaugustiniv00possrich, whose own full text opens with the identical OCR-garbled string this file's own body opens with below ("SANCTI AUGDSTINI VITA / iCRIPTA A POSSIDIO EPISCOPO...") and ends immediately before the same UC Berkeley circulation-desk slip the Provenance note below records stripping.
Provenance note: Mechanically extracted from the supplied docx -- archive.org site-navigation chrome (at the head of what was supplied) was stripped; the source item's own text carries no public-domain usage notice, so none is claimed stripped -- as was a scanned UC Berkeley circulation-desk due-date slip bound into the back of the physical volume (a library artifact, not part of the work -- it names loan periods and a phone number, nothing of Possidius's or Weiskotten's own content); the doubled/tripled inter-word spacing produced by that page's own text export was normalized to single spaces throughout. Nothing else altered. Rights basis, independently checkable: 1919 is far past the ~95-year US public-domain-by-date threshold this project's own registry uses, for both the Latin critical text and Weiskotten's own English translation.
```

## `cic/texts/prosper_chronica-minora-1-lat_mommsen1892.txt`

Lines -8 +8:

```text
before:
Provenance note: Mechanically extracted from the item's own djvu.txt; front-cover and back-cover decorative scan noise stripped. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note (independent review, Round 17; extended, Round 18; extended, Round 19; extended, Round 20): quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1892).
after:
Provenance note: Mechanically extracted from the item's own djvu.txt; front-cover and back-cover decorative scan noise stripped. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note: quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1892).
```

## `cic/texts/racovian-catechism_catechesis-ecclesiarum-lat_moskorzewski1609.txt`

Lines -9 +9:

```text
before:
Content note: The whole 1609 Latin Catechism with its dedicatory Praefatio to King James I of Great Britain, then the questions and answers in chapters (including De Via Salutis, De Persona Christi, De Officio Christi, De Ecclesia). This is the earlier recension; Rees's English (1818) translates the 1680 recension, so the two are not the same text. OCR sampled at five points: Latin readable, but with long-s read as f (the word-like share of tokens is about 0.86), scattered Cyrillic-looking glyphs for short Latin words and some doubled columns; quote only after checking the page image. Second witness for exact wording until a cleaner scan is found (Mark's OCR ruling, 2026-09-25).
after:
Content note: The whole 1609 Latin Catechism with its dedicatory Praefatio to King James I of Great Britain, then the questions and answers in chapters (including De Via Salutis, De Persona Christi, De Officio Christi, De Ecclesia). This is the earlier recension; Rees's English (1818) translates the 1680 recension, so the two are not the same text. OCR sampled at five points: Latin readable, but with long-s read as f (the word-like share of tokens is about 0.86), scattered Cyrillic-looking glyphs for short Latin words and some doubled columns; quote only after checking the page image. Second witness for exact wording until a cleaner scan is found.
```

## `cic/texts/riedemann_rechenschaft-deu_berne1902.txt`

Lines -9 +9:

```text
before:
Content note: SECOND WITNESS for scan quality (Mark's OCR ruling, 2026-09-25): the book is set in Fraktur and the OCR is garbled throughout (sampled at five points, roughly half the word tokens are misread, e.g. "unfrer SReligion" for "unsrer Religion"); the headings and running heads are garbled too. It is vendored because it is the Hutterite Brethren's own confession of faith, the movement's fullest doctrinal statement from Moravia, and no cleaner public-domain scan was found (the microform duplicate MN5077ucmf_5 is the same OCR). Contents: a publishers' note on the Hutterite Brüder-Gemeine, then Riedemann's Vorrede and the Rechenschaft in its sections ("Von der ...") with page-numbered running heads. The English translations (London/Plough 1950; Plough 1970) are in copyright and the archive.org copies are access-restricted. Every quotation must be verified against the page images before use.
after:
Content note: SECOND WITNESS for scan quality: the book is set in Fraktur and the OCR is garbled throughout (sampled at five points, roughly half the word tokens are misread, e.g. "unfrer SReligion" for "unsrer Religion"); the headings and running heads are garbled too. It is vendored because it is the Hutterite Brethren's own confession of faith, the movement's fullest doctrinal statement from Moravia, and no cleaner public-domain scan was found (the microform duplicate MN5077ucmf_5 is the same OCR). Contents: a publishers' note on the Hutterite Brüder-Gemeine, then Riedemann's Vorrede and the Rechenschaft in its sections ("Von der ...") with page-numbered running heads. The English translations (London/Plough 1950; Plough 1970) are in copyright and the archive.org copies are access-restricted. Every quotation must be verified against the page images before use.
```

## `cic/texts/rogers-richard_seven-treatises_1610.txt`

Lines -8 +8:

```text
before:
Content note: SECOND WITNESS, not a clean quoting text (Mark's OCR ruling, 2026-09-25): early-modern print with systematic long-s misreads and marginal scripture references run into the lines; sampled at 10/30/50/70/90 per cent and found readable but garbled in every sample. The seven treatises run in sequence with chapter headings 'Chap. n' as printed (first chapter heading about line 991); the edition's dedication and address To the Christian Reader open the file. Use for locating passages; verify any quotation against the page images before it is relied on.
after:
Content note: SECOND WITNESS, not a clean quoting text: early-modern print with systematic long-s misreads and marginal scripture references run into the lines; sampled at 10/30/50/70/90 per cent and found readable but garbled in every sample. The seven treatises run in sequence with chapter headings 'Chap. n' as printed (first chapter heading about line 991); the edition's dedication and address To the Christian Reader open the file. Use for locating passages; verify any quotation against the page images before it is relied on.
```

## `cic/texts/schwenckfeld_ander-verantwortung-auff-melanchthon-deu_1556.txt`

Lines -9 +9:

```text
before:
Content note: Schwenckfeld's second reply (1556) to Melanchthon's accusation and the Nuremberg proceedings of 1555 against him, on justification and the eternal Son: his own voice from inside the census window. German, blackletter. SECOND WITNESS for scan quality (Mark's OCR ruling, 2026-09-25): the Google OCR has read the Fraktur as roman letters and the text is garbled throughout (sampled at five points, roughly half the tokens are non-words such as "fdjulbißung" for "schuldigung"); the file locates passages but nothing is quotable until read on the page images. Vendored because it is the only Schwenckfeld text of the 1540s-1550s window found on a reachable host apart from the two 1547 prints vendored beside it. About 4,700 words.
after:
Content note: Schwenckfeld's second reply (1556) to Melanchthon's accusation and the Nuremberg proceedings of 1555 against him, on justification and the eternal Son: his own voice from inside the census window. German, blackletter. SECOND WITNESS for scan quality: the Google OCR has read the Fraktur as roman letters and the text is garbled throughout (sampled at five points, roughly half the tokens are non-words such as "fdjulbißung" for "schuldigung"); the file locates passages but nothing is quotable until read on the page images. Vendored because it is the only Schwenckfeld text of the 1540s-1550s window found on a reachable host apart from the two 1547 prints vendored beside it. About 4,700 words.
```

## `cic/texts/servetus_de-trinitatis-erroribus-lat_1531.txt`

Lines -9 +9:

```text
before:
Content note: Servetus's first book, seven books on the errors of the Trinity (1531), in Latin, the work for which he was first condemned. The OCR is badly garbled in places (the 10 and 50 percent samples are readable Latin with errors; the 30 and 90 percent samples fall in noise, and the word-like share of tokens is about 0.79). Second witness for exact wording until a cleaner scan is found (Mark's OCR ruling, 2026-09-25). No public-domain English exists: Wilbur's 1932 translation (Harvard Theological Studies 16) was renewed in 1960 (R263240) and its archive.org copy is lending-only.
after:
Content note: Servetus's first book, seven books on the errors of the Trinity (1531), in Latin, the work for which he was first condemned. The OCR is badly garbled in places (the 10 and 50 percent samples are readable Latin with errors; the 30 and 90 percent samples fall in noise, and the word-like share of tokens is about 0.79). Second witness for exact wording until a cleaner scan is found. No public-domain English exists: Wilbur's 1932 translation (Harvard Theological Studies 16) was renewed in 1960 (R263240) and its archive.org copy is lending-only.
```

## `cic/texts/smith-richard_life-of-lady-magdalen-montague_cf1627.txt`

Lines -8 +8:

```text
before:
Content note: SECOND WITNESS, not a quotable text (Mark's OCR ruling, 2026-09-25): the OCR of this microfilm is garbled at every one of the five sample points (10/30/50/70/90 percent), with u/v/y confusions, dropped letters and noise lines, and no clean scan of this edition was found on a reachable host; the only modern edition (A. C. Southern, An Elizabethan Recusant House, 1954) is in copyright. Vendored because the work is essential to this world (the census names it) and no other public-domain witness exists. A quote drawn from it must be checked against the page images of the archive.org item before use. The book is the 1627 English translation of Smith's Latin Life of Lady Magdalen, Viscountess Montague, with the translator's dedication to her grandson Viscount Montague and Smith's preface to the devout reader; it closes with Smith's account of her death. The household chapel, the chaplains and the Catholic servants of her house (Battle Abbey) are the subject, which is why the census names it for the women's and household record.
after:
Content note: SECOND WITNESS, not a quotable text: the OCR of this microfilm is garbled at every one of the five sample points (10/30/50/70/90 percent), with u/v/y confusions, dropped letters and noise lines, and no clean scan of this edition was found on a reachable host; the only modern edition (A. C. Southern, An Elizabethan Recusant House, 1954) is in copyright. Vendored because the work is essential to this world (the census names it) and no other public-domain witness exists. A quote drawn from it must be checked against the page images of the archive.org item before use. The book is the 1627 English translation of Smith's Latin Life of Lady Magdalen, Viscountess Montague, with the translator's dedication to her grandson Viscount Montague and Smith's preface to the devout reader; it closes with Smith's account of her death. The household chapel, the chaplains and the Catholic servants of her house (Battle Abbey) are the subject, which is why the census names it for the women's and household record.
```

## `cic/texts/sudermann_hohe-geistreiche-lehren-hohes-lied-deu_heyden1622.txt`

Lines -9 +9:

```text
before:
Content note: Sudermann's verse-and-prose meditations on the Song of Songs, verse by verse ('im Hohen Lied Salomonis am 1. Cap.' and so on), each with an engraved figure, opening 'Vom Hohen Lied Salomonis schreibet ein Christlicher Lehrer' and closing with an errata list ('Correctur etlicher Wörter nach dem Original Exemplar') and the colophon. The one Schwenkfelder-community voice inside the census window (1540s-1650) found on a reachable host. SECOND WITNESS for scan quality (Mark's OCR ruling, 2026-09-25): Fraktur OCR sampled at five points, whole-word share 0.74-0.79, with the title page and the engravings' lettering lost; quote only after checking the page images. No English translation exists.
after:
Content note: Sudermann's verse-and-prose meditations on the Song of Songs, verse by verse ('im Hohen Lied Salomonis am 1. Cap.' and so on), each with an engraved figure, opening 'Vom Hohen Lied Salomonis schreibet ein Christlicher Lehrer' and closing with an errata list ('Correctur etlicher Wörter nach dem Original Exemplar') and the colophon. The one Schwenkfelder-community voice inside the census window (1540s-1650) found on a reachable host. SECOND WITNESS for scan quality: Fraktur OCR sampled at five points, whole-word share 0.74-0.79, with the title page and the engravings' lettering lost; quote only after checking the page images. No English translation exists.
```

## `cic/texts/vonsoden_cyprianische-briefsammlung-deu_1904.txt`

Lines -8 +8:

```text
before:
Provenance note: Mechanically extracted from the item's own djvu.txt; Google's digitization notice stripped from the front, a repeated back-cover scan of the series title page stripped from the tail (after the volume's own closing "Druck von August Pries in Leipzig." colophon). Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note (independent review, Round 18; extended, Round 19; extended, Round 20): quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1904).
after:
Provenance note: Mechanically extracted from the item's own djvu.txt; Google's digitization notice stripped from the front, a repeated back-cover scan of the series title page stripped from the tail (after the volume's own closing "Druck von August Pries in Leipzig." colophon). Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note: quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1904).
```

## `cic/texts/vonsoden_prosopographie-afrikanischer-episkopat-deu_1909.txt`

Lines -8 +8:

```text
before:
Provenance note: Mechanically extracted as a page-range slice (pp. 247-270 of the printed volume) from the full serial volume's own djvu.txt -- the article's own heading ("DIE PROSOPOGRAPHIE DES AFRIKANISCHEN EPISKOPATS ZUR ZEIT CYPRIANS. VON HANS VON SODEN.") through its own closing paragraph, immediately before the next, unrelated article in the same volume ("Toscanische Studien," by Fedor Schneider) begins. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note (independent review, Round 18; extended, Round 19; extended, Round 20): quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1909).
after:
Provenance note: Mechanically extracted as a page-range slice (pp. 247-270 of the printed volume) from the full serial volume's own djvu.txt -- the article's own heading ("DIE PROSOPOGRAPHIE DES AFRIKANISCHEN EPISKOPATS ZUR ZEIT CYPRIANS. VON HANS VON SODEN.") through its own closing paragraph, immediately before the next, unrelated article in the same volume ("Toscanische Studien," by Fedor Schneider) begins. Doubled inter-word spacing normalized to single spaces; nothing else altered, no OCR error corrected. Note: quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording. Public domain by publication date (1909).
```

## `engine/BASELINES.md`

Lines -17 +17:

```text
before:
that produced the 2026-08-24 live routing run on pahc and the three fleet
after:
that produced this baseline's live routing run on pahc and the three fleet
```

## `engine/Dockerfile`

Lines -2,3 +1,0:

```text
before:
# PHASE-1-LAUNCH.md Stage 3 asked for this container ("the engine needs a
# container"); the cic-poc Dockerfile that stage described beside it was
# retired and deleted with the old system, 2026-08-28.
after:
(cut)
```

Lines -11,3 +8:

```text
before:
# engine/Dockerfile and leave dockerContext as the repo root. (The retired
# cic-poc/Dockerfile this note once contrasted against is deleted - the
# old system's retirement, 2026-08-28.)
after:
# engine/Dockerfile and leave dockerContext as the repo root.
```

Lines -15,3 +10,2:

```text
before:
# Frontend stage added PHASE-1-LAUNCH.md Stage 5 (one Render service, not
# two - Mark's call): builds cic-poc/frontend's static bundle and lands it
# at cic-poc/frontend/dist, same source-tree-relative path engine/api/
after:
# Frontend stage (one Render service, not two): builds cic-poc/frontend's
# static bundle and lands it at cic-poc/frontend/dist, same source-tree-relative path engine/api/
```

## `engine/api/README.md`

Lines -6,3 +6,2:

```text
before:
**not** the participant-facing production system — see
`/root/.claude/plans/linear-popping-dawn.md` for what's deliberately out of
scope (SSE streaming, Postgres, rate limiting, deletion workflow, auth
after:
**not** the participant-facing production system. Deliberately out of
scope: SSE streaming, Postgres, rate limiting, deletion workflow, auth
```

Lines -10 +9:

```text
before:
production topology, which is not yet built).
after:
production topology.
```

## `engine/api/app.py`

Lines -1 +1:

```text
before:
"""FastAPI shape only (see /root/.claude/plans/linear-popping-dawn.md) - HTTP
after:
"""FastAPI shape only - HTTP
```

## `engine/api/config.py`

Lines -1 +1:

```text
before:
"""Minimal test-backend config (see /root/.claude/plans/linear-popping-dawn.md).
after:
"""Minimal test-backend config.
```

## `engine/api/table_wiring.py`

Lines -864 +864:

```text
before:
    # lookup is #440's own fix, scoped to THIS SEAT'S world (not a single
after:
    # lookup is scoped to THIS SEAT'S world (not a single
```

## `engine/api/wiring.py`

Lines -1,2 +1:

```text
before:
"""Pure orchestration layer for the minimal test backend (see
/root/.claude/plans/linear-popping-dawn.md) - no FastAPI import here, so this
after:
"""Pure orchestration layer for the minimal test backend - no FastAPI import here, so this
```

Lines -924,2 +923:

```text
before:
    it - see _replay_text for why the tags have to be there, and what an
    earlier version of this docstring got wrong. Facilitator turns are left
after:
    it - see _replay_text for why the tags have to be there. Facilitator turns are left
```

## `engine/m1/embedded_quotations.py`

Lines -1 +1:

```text
before:
"""OG-10 (Build/worlds/pahc/Open_Gaps_Tracking.md): does a non-quote record's own
after:
"""Does a non-quote record's own
```

## `engine/m1/gates.py`

Lines -140,3 +140:

```text
before:
    it's a string) and resolved silently to nothing at compile time. The
    desert pilot's own manual check (not this gate) is what first caught
    this gap - see Build/worlds/desert/Open_Gaps_Tracking.md.
after:
    it's a string) and resolved silently to nothing at compile time.
```

## `engine/m1/quote_verbatim.py`

Lines -110,2 +110:

```text
before:
# Two of the three patterns a #403 triage flagged (not the stray-backslash
# one, left for the record-fix session) fold into the whitespace/ellipsis
after:
# Two of the three source-side patterns (not the stray backslash) fold into the whitespace/ellipsis
```

Lines -130 +129:

```text
before:
# prayer` - already nested-mark-fixed by #413 but blocked here too).
after:
# prayer` - whose nested marks are already fixed, but blocked here too).
```

## `engine/m1/schemas.py`

Lines -452,10 +452,4:

```text
before:
        # comment). Root-caused and added per Open_Gaps_Tracking.md OG-45/
        # OG-48: witt's own world_core record authored this content honestly
        # in its body, disclosing at authoring time that no such field
        # existed yet ("pending a future schema change-order... the same way
        # thin_topics was added structurally after thinness/cautions already
        # existed in prose") - so the M2 compiler had no code path to read
        # it, and a project-lead-confirmed Article 29 determination never
        # reached the deployed prompt. Left unset, a world_core record has
        # nothing to say here (most do not yet have a confirmed Article 29
        # determination at all). Not yet in COMPLETION_REQUIRED - existing
after:
        # comment). A field, not body prose, so the M2 compiler can read it
        # into the deployed prompt. Left unset, a world_core record has
        # nothing to say here (a world without a confirmed Article 29
        # determination leaves it unset). Not in COMPLETION_REQUIRED - existing
```

Lines -889,3 +883,2:

```text
before:
                # meaning at compile time - never `quote.text` (Mark's
                # standing quote ruling; see gates.py's quotation-mark
                # fidelity gate).
after:
                # meaning at compile time - never `quote.text` (see
                # gates.py's quotation-mark fidelity gate).
```

## `engine/m2/builders.py`

Lines -405,2 +405:

```text
before:
        # world_core.living_traditions, added per Open_Gaps_Tracking.md
        # OG-45/OG-48): present only for a world with a CONFIRMED Article 29
after:
        # world_core.living_traditions): present only for a world with a CONFIRMED Article 29
```

## `engine/m2/site_compiler.py`

Lines -89,2 +89,2:

```text
before:
    """`modern_rendering` only - NEVER `text` (Mark's standing quote
    ruling). See engine/m1/gates.py's gate_quote_mark_fidelity for the
after:
    """`modern_rendering` only - NEVER `text` (a world speaks a quote's
    modern rendering, never its source text). See engine/m1/gates.py's gate_quote_mark_fidelity for the
```

## `engine/m4/evidence.py`

Lines -773 +773:

```text
before:
    this replaces: a divinity question's quote slots both filled from
after:
    this prevents: a divinity question's quote slots both filled from
```

## `engine/m4/facilitator_turns.py`

Lines -252 +252:

```text
before:
# unread-message line). It names no organisation or number; Mark's approved wording.
after:
# unread-message line). It names no organisation or number; the wording is approved and fixed.
```

## `engine/m4/grounding_net.py`

Lines -4 +4:

```text
before:
(grounding_experimental.py, claude/cic-design-assignment-ecoxh2), which
after:
(grounding_experimental.py), which
```

Lines -1514 +1514:

```text
before:
# proved live across two battery runs (#419, #420). A paragraph is a
after:
# proved live across two battery runs. A paragraph is a
```

## `engine/m4/live_table_battery.py`

Lines -7,8 +7,4:

```text
before:
RESHAPED (closing the STALE flag this replaces):
the original six probes ran one session of five real rounds against
TABLE_SESSION_ROUND_CAP=5; the cap was resized to 3 the same day this
battery was last touched, and L4/L5 would now run past it - round.py's
own cap check refuses any round once rounds_completed >= 3, before
either probe ever spent a call. Dropping L4/L5 to fit one 3-round
session would have quietly lost coverage nobody authorized losing, so
the battery now runs TWO sessions of three rounds each, keeping every
after:
SHAPE: TABLE_SESSION_ROUND_CAP is 3, and round.py's own cap check
refuses any round once rounds_completed >= 3, so six probes cannot share
one session. Dropping L4/L5 to fit one 3-round session would lose
coverage, so the battery runs TWO sessions of three rounds each, keeping every
```

## `engine/m4/named_claim_grounding.py`

Lines -2,2 +2:

```text
before:
passed engine.m4.grounding_net's own ratio test (fabrication guard; see
Build/worlds/pahc/Open_Gaps_Tracking.md OG-9 for the traced regression).
after:
passed engine.m4.grounding_net's own ratio test (fabrication guard).
```

## `engine/m4/output_check.py`

Lines -121 +121:

```text
before:
# saying and naming, never about the record: an earlier version matched "we
after:
# saying and naming, never about the record: it must not match "we
```

## `engine/m4/round.py`

Lines -149 +149:

```text
before:
# ~$0.51, against ~$0.70 for the un-resized 5-round figure this replaces.
after:
# ~$0.51, against ~$0.70 for a 5-round session.
```

Lines -206 +206:

```text
before:
        # Mark-approved resources text is reused verbatim; only its
after:
        # approved resources text is reused verbatim; only its
```

## `engine/m4/store.py`

Lines -3,2 +3,2:

```text
before:
decision (Artifact-6 SS3 topology: RDS Postgres) this build thread doesn't
need to make today to build and prove the log's actual guarantees
after:
decision (Artifact-6 SS3 topology: RDS Postgres) this module doesn't
need to make to build and prove the log's actual guarantees
```

Lines -143,3 +143,2:

```text
before:
        sessions deleted. The 90-day conversation retention (System Hub
        decision 34) calls this daily; the edge supplies `is_exempt` for
        conversations a signed-in person saved (the accounts change order),
after:
        sessions deleted. The 90-day conversation retention calls this daily; the edge
        supplies `is_exempt` for conversations a signed-in person saved,
```

## `engine/m7/retention.py`

Lines -12 +12:

```text
before:
90 days under the accounts change order. The engine never learns which
after:
90 days. The engine never learns which
```

## `engine/m8/reconcile.py`

Lines -2 +2:

```text
before:
one route and month, set against the invoice line Mark types in. The ratio
after:
one route and month, set against the invoice line the operator types in. The ratio
```

## `engine/prose.py`

Lines -588,2 +588,2:

```text
before:
    # a name - excluding bare "I" alone (the earlier version of this check)
    # missed every contracted form, since the regex keeps the apostrophe as
after:
    # a name - excluding bare "I" alone would
    # miss every contracted form, since the regex keeps the apostrophe as
```

## `engine/provider/guard.py`

Lines -93 +93:

```text
before:
    test conversation Mark runs goes through the live engine and needs no
after:
    test conversation the operator runs goes through the live engine and needs no
```
