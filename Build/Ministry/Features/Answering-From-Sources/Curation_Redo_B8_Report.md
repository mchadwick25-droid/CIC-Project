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

## Round 3 (B8 sample review): Benson and both Mesnage scans

Start 2026-10-30 21:49 UTC, end 22:03 UTC (about 14 minutes). Code: `answering_library` exported from origin/main into the scratchpad, `cic/texts` linked there; nothing inside the shared checkout.

### What was wrong

- **Benson.** Printed "INTERCALARY. / PRESBYTERS AS MEMBERS OF THE ADMINISTRATION." (19508, 19510; Contents 559-561; running heads from 19543) sat inside `chapter7/section3/part2`, which was filed as "2. The Gaulish Appeal" with a false `allow_oversize` sentence. VI section 5 prints "I. The Mixed Cup." (17577) and "2. The Age of Baptism." (18009), matching Contents 537-539 and the running heads at 17998 and 18098, and was not split.
- **Both Mesnage scans.** The explicit entry lists were wrong in kind, in two directions.
  - Non-entries taken as entries. A later line of an entry started a division, so the real entry kept only its name and its text sat under a non-heading: "Évêché. More..." and "More., ..." lines, bishop-name lines (MONTANUS, JULIANUS, DEUTERIUS, FORTUNIUS, ROMANDS, VOGONIUS), location lines ("S.-E. du lac Djendeli.", "Route d'Aïn Beida...", "S.-E. de Bir el Henchir."), alias or continuation lines of a heading ("Alex. Liberum.", "Colonia Aelia Augusta Mereurialis...", "Haimeur du Corpus."), run-in sentence ends ("Montesquieu.)", "SUSICAZIA." in "Voir Évêchés non identifiés : SUSICAZIA", "Gazabiana.", "IV kal. dec."), a Nota inside Medjenat, and in the antiques scan `Bacanaria` (31668, 2,355 words of the Tingitane introduction), eleven cells of the Bevegerius table (32013-32073) and the "Espagne." row (32088).
  - Real entries lost. A heading line printed with no blank line after it (the first line of text follows at once) was not taken as an entry. Its text was filed under the previous entry. About 72 entries in the antiques scan and 288 in the ruines scan, for example Ater (Bir el), Anguia, Aquiaba, AURUSULIANA, AUSANA, Teboursouk, Mahfadia, Tiklat, Ahmed (Hr S1), Ahmed Djedidi.

### What was done

- **Benson.** Four divisions added: `chapter6/section5/part1` (17577), `part2` (18009), `chapter6/section5/part2/objection-to-council-iii-on-account-of-its-antipelagianism-l18101` (the Contents entry the body prints at 18101) and `chapter7/intercalary-presbyters-as-members-of-the-administration-l19508`. `chapter7/section3/part2` (19029-19507) lost its `allow_oversize`; it now holds 3,356 words. Four evidence lines added.
- **Mesnage.** The rule for an entry was read from the print: a short heading line after a blank line, followed by its text with or without a blank line, in alphabetical order inside each part. Three tests were run on each scan: titles that are not place-name shaped; every division after an entry of 3 words or fewer; alphabetical order against neighbours. The two scans were then aligned against each other by heading text and order (1,782 of 1,802 headings matched by program, the remaining 20 read by hand), so each scan's missing and false divisions showed up against the other. Every addition and removal was read in context.
  - Antiques: 44 non-entry divisions removed, 72 entries added, one heading moved to its first printed line (Mehdia: the heading is printed in three stacked lines; the division starts at 8207, locus `tunisie/meh-d-ia-8207`, title the OCR token "Meh.d.ia").
  - Ruines: 42 non-entry divisions removed, 288 entries added, Mehdia moved the same way (`tunisie/mehdia-8011`).
  - Maroc: the Tingitane introduction is now one division (31634 / 30605); real entries Dimmad el Achira, Faraoun, Tanger stay.
  - The new loci follow the scheme (`<part>/<printed heading slug>-<line>`); no title or number is invented. Titles are the first printed line, OCR errors kept.

### Final check output

Check runs: about a dozen across the three files as the lists changed (not counted exactly). Final:

| File | Divisions before | After | Result |
|---|---|---|---|
| `benson_cyprian-his-life-his-times-his-work_1897` | 124 (111 body) | 128 (115 body) | PASS, class curated, 745 byte ranges exact |
| `mesnage_afrique-chretienne-eveches-ruines-antiques-fra_1912` | 1,786 (1,779 body) | 1,814 (1,807 body) | PASS, class curated, 0 over 5,000 words, 1,983 ranges 0 mismatch |
| `mesnage_afrique-chretienne-eveches-ruines-fra_1912` | 1,569 (1,562 body) | 1,815 (1,808 body) | PASS, class curated, 0 over 5,000 words, 1,982 ranges 0 mismatch |

All three carry `status: drafted`. No checker or tooling change.

### Remaining defects

- The Mesnage recall is not proven complete. A heading that no scan caught and that the other scan lacks too would still be filed under the previous entry. The 15-entry sample per file (random seed) showed no non-entry divisions and no entry run into another.
- Headings the print breaks across lines or prints in a bracket stack (Mehdia) take the first printed line as the start; the title is an OCR fragment.
- A few sub-headings inside an entry stay as divisions because the edition prints them as headings: "Musée Lavigerie.", "Musée de Lambèse...", "Ausvaga II." (antiques only), "BOSET II.", "NUMIDIE ET MAURÉTANIE SITIFIENNE", "Bains romains." (not a division; left in its entry).
- The two Mesnage scans differ in how many sub-lines they set as divisions only where the print differs; each list was checked against the other, not against a third source.
- Benson unnumbered Contents entries still inside sections (8250, 11303, 11431, 11826, 12707, 15795) are unchanged from the reader's note (a).

### Judgment calls for the Opus reader

1. Benson 18101 is added although the reader called it optional: the scheme promises Contents entries by heading text plus line, and the entry is printed.
2. Mesnage "Evêques" bishop lines (all-caps personal names) are never divisions, even when they follow a blank line; the only all-caps divisions kept are place names on the lists of unidentified sees.
3. Mesnage Mehdia start line (8207 / 8011) is the first line of the stacked heading, so the division does not begin on the third printed line of its own heading.
4. "Gafsa. = Gapsa col. A l'époque byzantine..." (antiques 5404) is taken as an entry although the heading and the first sentence share a line.
5. Mesnage `Bevegerius` table and the reordered list (32083-32092 antiques, 30985 ruines) are left inside the Tingitane introduction division, not set as apparatus; they are part of its argument.
6. Ruines "Batoum. | Kondiat el)" (16168) keeps its OCR title; the bar and bracket are printed damage.

## Fourth look at the two Mesnage scans (Mark's ruling, option A, 2026-10-30)

Scope: the 16 headings the third-round review found missing from each scan, plus every further miss the edition's own index and a body scan revealed. Nothing else was reopened. Time: 22:21 to 22:37 UTC (about 16 minutes). Check runs: 4 (two files, before and after the status change). No model or paid calls. The vendored text was not edited.

### Cause

The earlier lists were built from headings printed as plain `Name. (qualifier)` after a blank line, aligned one scan against the other. Both scans print the same headings in the same shapes, so the alignment could not show recall. The 16 headings carry a comma or qualifier before the first period, a stray mark in front (`•`, `i`, `[`), or a heading that wraps to a second line. The earlier explicit list was not wrong in kind: it is an entry list by design, and it was missing entries. The 16 were added to it; no rule was introduced, because the gazetteer headings have no pattern that separates them from running text (the 16 and the headings already found share no common shape).

### Method

1. Index extraction. Antiques: the Tables, section A (33349-40559), parsed into 2,414 entries (name plus page reference). Ruines: the same section (32166-43083). This scan prints the names in one block and the pages in another, so the parse is by name only and splits some entries in two: 2,580 name lines, of which about 166 more than the other scan are fragments.
2. Each index entry was matched to a division title by name tokens (OCR-tolerant). Entries left over were searched in the body: antiques within the pages the entry cites (page-to-line map from the running heads, plus or minus one page), ruines over the whole body.
3. Independent body scans for headings that are not in the index: (a) every line after a blank line that is shaped like a heading and falls alphabetically between the two divisions around it; (b) every short heading-shaped line with no blank line before it, on the same test; (c) lines of the form `Name I.` / `Name II.`. All hits were opened and read.
4. Cross-check: the two scans' division lists were aligned title against title after the additions. They now differ only in OCR spelling (and the two Carthage heading lines, which sit before the range compared).

### Result per file

| | antiques | ruines |
|---|---|---|
| Index entries | 2,414 | 2,580 name lines |
| Matched to a division of their own | 2,174 | 2,346 |
| Added from the index list (heading had no division) | 17 | 16 |
| Cross-references (`Voir`, `Cfr.`, `Gfr.`): no entry of their own, by design | 65 | 67 |
| Variant or ancient name printed inside another entry's text | 35 | 10 |
| Index line unreadable (OCR, fragments, running heads, map letters only) | 59 | 14 |
| Unresolved: no division and no body line found | 81 | 143 |
| Divisions before / after | 1,814 / 1,834 | 1,815 / 1,834 |
| Added outside the index list | 3 (Ausvaga II, Boset I, BOSET II) | 3 (Bains romains, whose line is not legible in this scan's index, Ausvaga II, Boset I) |

The unresolved counts are not a list of missing entries. Opening a sample of them (Oghab, Rezel, Zaroura, Sbia, Klab, Mzata, Mziger, Naceur, Dia, Guellil, Sola, Segueur, Phua, Safsaf) showed each already has a division; the index line is too damaged to match (`Beliir` for Behir, `Gliemorra` for Chemorra, a descriptor run into the name). The rest are index lines that are OCR debris or the second half of a two-line entry (this is most of the ruines count, from the block layout). Nothing in the unresolved lists could be placed as a printed heading in the body, and none was forced.

Added headings (antiques line / ruines line): Aïn el Asker 2543 / 2620; Ali Djebin 2786 / 2851; Alouani 2855 / 2921; Aouitta 3064 / 3119; Béja = Vaga 3309 / 3351; Chateur S' Mansour 3888 / 3908; Hadjeb el Aïoun 5861 / 5792; Haïdra = Ammaedara 5903 / 5834; Hamdouna 6027 / 5954; Kahloulia 6603 / 6498; Ouassel 8965 / 8736; Ouderf 9002 / 8771; Tell el Kaïd 10796 / 10478; Kafrida 19935 / 19280; Mrata 21810 / 21108; Duperré 28436 / 27523. Beyond the 16:

- Bains romains (antiques 27942, ruines 27053): a heading alone on its line at the top of printed page 444, followed by its `Atl. arch.` citation, and listed in the Tables (`Bains Romains 444`). Found by the index check.
- Ausvaga II (antiques 12266, ruines 11914): a printed heading with its own bishop, the twin of the division `Ausvaga I.` already present.
- Boset I (antiques 12449, ruines 12093) and BOSET II (antiques 12472): printed sub-headings with their own bishops, the twins of BOSET II in the ruines file. The antiques file had no division at BOSET II; it is not listed in the earlier note and was a miss. BOSET II sits directly after text with no blank line before it, which is why the earlier blank-line passes did not see it.

### Final check output

Both files: `RESULT: PASS`, 1,834 divisions (1,827 body, 7 apparatus), address uniqueness all unique, coverage 100.0 percent, 0 over 5,000 words, rules and evidence all found, word completeness exact (antiques 194,050 / ruines 193,128), verbatim byte ranges 0 mismatch (1,660 exact and 342 less declared furniture of 2,002; 1,678 and 322 of 2,000). Checker run from origin/main code in a scratchpad export with `cic/texts` linked only there. `status: drafted` on both.

### Judgment calls for the reader

1. Titles are the printed first line, OCR kept (`OuasseL`, `AugusLa E mérita`). Two headings that wrap carry the printed continuation: Béja (`byzantine.`) and Haïdra (`Augusta Emerita`). A stray mark in front of the heading (`•`, `i`, `[`) is dropped from the title because it is not part of the print; the division still starts on that line.
2. Hadjeb el Aïoun and Ouassel: the second printed line is a `Voir` note or running text, so it is not in the title.
3. Ausvaga II, Boset I and BOSET II are sub-headings of entries, not index entries. They are added for consistency with `Ausvaga I.`, `BOSET II.` and the `Noba I et II` style headings already divisions. If the reader would rather keep sub-headings inside their entry, these three (two in the ruines file) come out without touching anything else.
4. Variant names printed inside another entry (Baharine inside Chahoud, Thisita inside Chateur S' Mansour, the ancient names under Duperré and Kafrida) are not divisions: the edition prints them as part of that entry's text.
5. The ruines index parse is by name only and over-counts; its figures are an upper bound on fragments and the reason its unresolved count is higher. They were not used to add or remove anything that the antiques parse and the body scans did not also support.
6. Not covered: a heading with no blank line before it, no trailing period and not alphabetically between its neighbours. None was found by any scan, but the scans cannot exclude one.
