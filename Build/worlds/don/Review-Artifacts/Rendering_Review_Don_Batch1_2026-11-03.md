# Rendering Review: don quote records, batch 1 (5 records)

- **Reviewer:** Opus 5.5 (independent; did not draft or render any of these records)
- **Date:** 2026-11-03
- **Subject:** the `text` and `modern_rendering` of 5 `don.quote` records.

## Method

Each record's `text` is compared against the vendored file in `cic/texts/` at its locus. XML notes and tags are stripped, line-end hyphens rejoined, and whitespace folded. For OCR scans (CIL VIII, Migne PL 11, Ziwsa), a reading passes when every word is present and the only differences are plain OCR letter errors. Each `modern_rendering` is checked clause by clause against the edition text, then against `confidence.divergence_note` and `use_note.not_for`. Sentence length is counted by hand in words, splitting at full stops, question marks and colons that end a clause.

Files read: `cil8-supplementum-numidiae_cagnat-schmidt1894.txt`, `optatus_against-the-donatists.txt`, `optatus_libri-vii-critical_ziwsa1893.txt`, `optatus_libri-vii-lat_ziwsa1893-csel26-tei.txt`, `pl11-zeno-optatus-collatio-carthaginiensis_migne.txt`, `npnf104_augustine-anti-manichaean-anti-donatist.xml`.

## Results
**5 records: 5 PASS, 0 FAIL (0 P1, 0 P2).**

| Record id (don.quote.…) | Edition text at (file, lines) | Text check | Rendering check | Verdict |
|---|---|---|---|---|
| deo-laudes | cic/texts/cil8-supplementum-numidiae_cagnat-schmidt1894.txt, lines 3868-3874 (no. 17732; OCR "nro LtAVDES (Lis)" for DEO LAVDES (bis), with the editors' Donatist note); clean "DEO LAVDES" at line 4566 (no. 17368) | pass (17732 legible only through OCR errors; clean at 17368) | two words rendered; "praise to God" keeps the acclamation's sense; nothing added; longest 3 | PASS |
| donatus-quid-est-imperatori | cic/texts/optatus_libri-vii-lat_ziwsa1893-csel26-tei.txt, line 3357 (clean Latin); cic/texts/optatus_libri-vii-critical_ziwsa1893.txt, line 6557 (OCR); cic/texts/optatus_against-the-donatists.txt, line 1904 (English) | pass (Latin verbatim in the TEI file; English verbatim) | "quid est imperatori cum ecclesia" fully rendered as a question; no added sense; longest 9 | PASS |
| emeritus-magno-argumento | cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt, lines 126834-126837 | pass (every word present; OCR errors only, e.g. "irgnmento", "occullaiur", "sileanttir") | all clauses: great device, truth hidden, our inquiry, small thing put forward, rest kept silent; longest 23 | PASS |
| petilian-conscience-of-the-giver | cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml, line 10280 | pass | both propositions rendered with the bracketed "in holiness" and "knowingly" kept; nothing added; longest 24 | PASS |
| the-shores-are-covered | cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml, lines 15512-15513 | pass | all clauses: shipwrecked limbs, waves of truth, Egyptians, dying on the shores, heavier in death, no burial; longest 20 | PASS |

## Failed renderings: corrected text

None. All five renderings meet the bar.
