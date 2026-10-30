# Curation redo, batch B8 (martyr acts and modern monographs)

Drafter: Sonnet 5.5. Start 2026-10-30 21:29 UTC, end 21:37 UTC. One sparse worktree, one branch, one pull request. Code and tooling from origin/main. No model or paid calls. Check runs: about 30 in all.

## Per file

| File | Result | Fixes | Minutes | Defects left |
|---|---|---|---|---|
| `hefele-leclercq_histoire-des-conciles-tome1-1-cyprien-novatiens-baptheme-slice-fra_1907` | pass | 0 | 1 | none |
| `perpetua-scillitan-martyrs-lat-grc_robinson1891` | pass | 3 | 3 | none |
| `harnack_mission-und-ausbreitung-des-christentums-band2-deu_2e-aufl1906` | pass | 2 | 3 | none |
| `benson_cyprian-his-life-his-times-his-work_1897` | pass | 33 divisions added, 4 split, 3 `not_subheadings` entries, 4 `allow_oversize` sentences rewritten, 1 removed per split part | 12 | see below |
| `monceaux_histoire-litteraire-afrique-chretienne-tome2_1902` | pass | 1 | 2 | none |
| `mesnage_afrique-chretienne-eveches-ruines-antiques-fra_1912` | pass | 3 divisions removed | 1 | none |
| `mesnage_afrique-chretienne-eveches-ruines-fra_1912` | pass | 4 divisions removed | 1 | none |

All seven files pass the whole check and carry `status: drafted`.

## What was wrong and what changed

- **Hefele-Leclercq.** Already repaired on main (`section6/sub1` at 746, no `allow_oversize`). The check passes unchanged. No edit.
- **Robinson Perpetua.** Three loci named labels the edition does not print. Now the slug of the printed heading plus line: `the-latin-and-greek-texts-of-the-passion-of-s-perpetua-l3438` (printed over lines 3438-3444), `the-acts-of-the-scillitan-martyrs-l7108`, and `maptyrion-toy-atioy-kai-kaaainikoy-maptypoz-l7428` (the OCR of the Greek heading as the scan prints it).
- **Harnack.** Testimonies 27 and 28 were folded into 26. Line 500 prints `("27)  Lactantius` and 529 prints `(2b)  Constantin`. Fixes set 27 and 28. Second printed instances: 992 "Aus Lactantius' Mitteilungen (Nr. 27)" and 883 "dieser Kaiser (Nr. 28)", said of Constantine. Quotes added to `evidence`. The series now reads 1 to 30 with no gap.
- **Benson.** Six `allow_oversize` sentences failed the scan. The body does print headings the old curation missed:
  - ch. X section 1: parts 1 to 5 at 26660, 27122, 27540, 27772, 27824; section 2: parts 1 to 3 at 27929, 28158, 28540. Both sections now divided as `partN`, as ch. VIII section 1 already was.
  - ch. VIII section 4: parts 1 to 3 at 25016, 25089, 25455.
  - ch. VIII section 2 part 2 (21,625 words): split at the twelve Contents entries the body prints as heading lines (21113 to 23231), addressed by printed heading text plus line, as the scheme line now says. The Fifth and Sixth Council documents stay in the first division (20784).
  - ch. IV section 3: split at the Contents entries "How to make the best of the forgeries now" (13810) and "Note on the Citation from Pelagius II" (13844).
  - ch. VI section 4: split at "Table shewing the verbal debts" (16774), "On the Characteristics and Genuineness of the De Dominica Oratione" (16973), "Comparison elucidating the dates" (17351).
  - ch. XI: split at six Contents entries (29826 to 30440). Its first part (6,463 words, "The Birthday") keeps `allow_oversize`.
  - Running heads listed in `not_subheadings` for ch. IV section 3 (9 lines), ch. VIII section 3 (12) and ch. XI (6). The remaining `allow_oversize` sentences were rewritten to say what the page shows.
- **Monceaux tome 2.** Livre III ch. VI section V (`l3/c6/s5`, 10244) added; numeral lost in the scan, read from the Table des matières (21936), as for l4/c4/s5 at 17918. `l3/c6/s4` is now 5,696 words and keeps its `allow_oversize` sentence, which the scan accepts.
- **Mesnage, both scans.** Removed the divisions that are not entries: antiques 2863, 7868, 8767; ruines 2436, 2440, 5671, and also 2456 `Saladin.`. Line 2456 is the last row of a bibliography table in a footnote of the Abd-el-Melek entry (2376) and the entry text continues beneath it, so it was not an entry either (not named by the reader; found while reading 2436). The removed text now belongs to the entry before it.

## Judgment calls for the Opus reader

1. Benson ch. VIII section 2 part 2 addresses: twelve loci of the form `part2/<slug>-l<line>` for Contents entries that carry no numeral. The scheme line now states this. Slugs shorten the printed heading (for example `that-quietus-of-buruc`).
2. Benson 21626: "The Seventh Council under Cyprian and Third ON Baptism was held on ..." is a run-in line, not a standalone heading. It is taken as the start of the Contents entry "Seventh Council, Third on Baptism" (page 364). The Fifth and Sixth Council entries have no heading line in the body and stay inside the first division.
3. Benson ch. IV section 3 still holds four flagged lines that are not running heads: 12966 and 13509 (a "1726" year at a line start), 13619 and 13630 (the author's own "I." and "2." for the four interpolations). They are not listed in `not_subheadings` since none of the four kinds fits and the count is under the limit of 10.
4. Benson ch. VIII section 3 (9,497 words) keeps `allow_oversize`. The Contents prints Cyprian's 1 to 4 and Stephen's arguments as page entries but the body sets no heading line for them; "Baptism in the Name of Christ alone" (24117) is the one heading line. Not split there, because the halves stay over 5,000 words.
5. Benson 25689 vs `chapter9/part1` start at "(RESUMED)." 25686, and the appendices A to L as `notes` apparatus: both left as the reader recorded them (minor / a project decision).
6. Benson `introduction`, ch. III question 3 and ch. VII section 3 part 2 keep their old `allow_oversize` sentence. The scan accepts them (10 or fewer heading-like lines); the sentences were not re-read against the page.
7. Benson ch. X: the scan duplicates one page, so the heading "2. Rome. — The exclusion from the Cemeteries." prints twice (28158 and 28215) with the same text beneath. Part 2 starts at the first; the repeat sits inside it.
