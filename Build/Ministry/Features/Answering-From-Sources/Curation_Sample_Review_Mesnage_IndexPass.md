# Curation sample review: Mesnage index pass (fourth look, Mark's ruling)

Reviewer: Opus 5.5, a different reader from the fixer and from rounds 1 to 3. Date: 2026-10-30.
Under review: local commit 572f38b12 on `claude/curation-sample-b8`. Scope: a targeted pass that uses the edition's own index (Tables, section A) as the checklist. This is the last look at these two documents.
Bar (Mark): acceptable scholarly rigor, not perfection. A file fails only if something is actually wrong or misleading: text filed under a non-heading, real entries missing in a pattern, or an invented division.

`check` was run from origin/main code exported to the reviewer's scratchpad, with `cic/texts` linked only there. Both files: `RESULT: PASS`, verbatim byte ranges 0 mismatch (antiques 1,660 exact and 342 less declared furniture of 2,002; ruines 1,678 and 322 of 2,000).

## Verdicts

| stem | verdict | reasons |
|---|---|---|
| `mesnage_afrique-chretienne-eveches-ruines-antiques-fra_1912` | **pass (sampled-ok)** | The 16 entries are restored, each at its own heading. Index recall: 39 of 39 sampled entries that have a printed heading start a division exactly there (the 40th has no heading of its own). 20 unresolved index names: none is a missing entry. Heading scan: 0 misses in 3 windows. The 20 added divisions are all printed headings. |
| `mesnage_afrique-chretienne-eveches-ruines-fra_1912` | **pass (sampled-ok)** | The same 16 entries are restored. Index recall: 40 of 40. 20 unresolved index names: none is a missing entry. Heading scan: 0 misses in 3 windows. The 19 added divisions are all printed headings. |

## (1) The 16 known entries

Each line below starts a division, and the line before it is blank. The division before each one now ends just above it, so the earlier mis-filing is gone.

| entry | antiques | ruines |
|---|---|---|
| Aïn el Asker, ou Rdir es Soltan. = Sutunurga | 2543 | 2620 |
| Ali Djebin. (S') = Novis Aquilianis | 2786 | 2851 |
| Alouani (H'' el) ou S' Djabeur. | 2855 | 2921 |
| Aouitta. (H'' bou) ou Aouïa. = Avissa ou Avitta ? | 3064 | 3119 |
| **Béja. = Vaga.** (Col. Septimia) ; Theodorias | 3309 | 3351 |
| Chateur S' Mansour. (bou) = (T)hisita | 3888 | 3908 |
| Hadjeb el Aïoun, sur la Sebkha el Hani. = Germanicia ? | 5861 | 5792 |
| **Haïdra. = Ammaedera ou Ammaedara** | 5903 | 5834 |
| Hamdouna (bordj) ... = Civ. Avensesis. | 6027 | 5954 |
| Kahloulia (Aïn) ... = Tegiata. | 6603 | 6498 |
| Ouassel (à 1500m d'Aïn) | 8965 | 8736 |
| Ouderf et de la Mtouïa. (Oasis de) = Ad Palmas. | 9002 | 8771 |
| Tell el Kaïd ou Aïn Tlit. = Thagari majus | 10796 | 10478 |
| Kafrida (Tizi) ou Tala Aïzraren | 19935 | 19280 |
| Mrata. (H') (stray `•` in front in antiques) | 21810 | 21108 |
| Duperré. (El Khadra) = Oppidum Novum. (stray `i` / `[`) | 28436 | 27523 |

Béja (Vaga) is no longer filed under Begueur: Begueur (antiques 3303, ruines 3345) now ends at 3308 / 3350. Haïdra (Ammaedara) is no longer filed under Hagueuf: Hagueuf (5898 / 5829) now ends at 5902 / 5833.

## (2) Independent recall check from the index

Method: the reviewer parsed the index separately (antiques 33334-40559, ruines 32154-43083) into entries ending at a page number. Cross-references (`Voir`, `Cfr.`, `Gfr.`) were left out. The rest was split into 40 equal bands in alphabetical order, and one entry was drawn from each band (seed 20261030). Each heading was found in the body using the cited page and a name search. A hit means a division starts on the heading line. A name printed only as the equivalent in another entry's heading (for example `Sufes = Sbiba`) counts as a hit when that entry's division starts at its heading.

**Antiques: 39 hits out of 39 entries with a printed heading.** Index lines: 33461, 33598, 33821, 33945, 34120, 34220, 34488, 34753, 34885, 35027, 35110, 35330, 35416, 35528, 35717, 35855, 36027, 36193, 36452, 36499, 36705, 36838, 36983, 37410, 37545, 37804, 38058, 38294, 38390, 38577, 38834, 38947, 39102, 39595, 39699, 39861, 40090, 40191, 40276. A few matched only through OCR damage, and their divisions are: Aeliae 11949; Baricis (de) 25645 for `Batucis`; Genturiae 26095; GlUMTUTURBO 12864; NoBA I et II 31058 for `NoRAletR`; Haouch (Bir bou) 19792; Zama (Propriété) 11442. The 40th entry (38709, `Sepïa. = Ceuta 507`) has no printed heading. Septa is named only in the prose of the Maurétanie Tingitane introduction (31634-32003), so it is not a miss.

**Ruines: 40 of 40.** Index lines: 32224, 32283, 32459, 32522, 33097, 33136, 33385, 33837, 34010, 34290, 34932, 35041, 35067, 35200, 35259, 35313, 35973, 36054, 36336, 36403, 36972, 37221, 37316, 37533, 37678, 38076, 38657, 38790, 39339, 40035, 40111, 40294, 40549, 40663, 40700, 41778, 41844, 42040, 42399, 42768. Some resolve through OCR or through the equivalent named in another heading: Ad Atticille → Sahbi 9297; Avitta → Aouitta 3119 (one of the 16); Bacanaria 29549; Brighita 3681; Saltus Horreorum → Zada (Aïn) 24191; Cefala → Gefala 12388; Djena (bou) 4504; Hanacher (Bir el) 19116; Menza bent es Soltan 28036; Nouzidias 26041. Fedj Deriasse (index line 34932) is a place named inside the Centuriae entry (25285), not a heading of its own.

**The drafter's unresolved names.** The report gives counts (81 and 143) and 14 names, but no line lists. So the reviewer rebuilt the set with the same test: index entries whose name words match no division title. That gave 280 for antiques and 120 for ruines (a looser parse than the drafter's). From each set, 20 were drawn (seed 7).

- Antiques (index lines 33869, 33969, 34075, 34097, 34218, 34267, 34371, 34443, 34503, 34936, 35435, 35801, 36783, 37571, 38092, 38505, 38572, 38718, 39894, 40139): 18 have a division at their heading, and the index spelling differs from the body only by OCR. Examples: Aqu^ Régime 6398; ASUOEEMIXTA 25533; Gueydon (Port) ou Azeffoun 28570; Barchouch 3268; Behir 16852 for `Beliir`; Bey (Aïn el) = Sadbar 17041 (also Saddar); Brahim (Sidi) = Gunugu 28078; Chateur 3818; Eminentiana 26137; Marcelliana 13918; Laslâa 7364; MOLICUNTA 26709; Outaia = Mesarfelta 22255; Akhmim (bir el) = Salina 2582; Seredueli 31203; TuBUNAE de Maurétanie 31513; YlBIANA 15426. Two (Barba campestris and Bocanum Hemerum, both p. 507) are named only in the Tingitane prose. None is a missing entry.
- Ruines (index lines 32490, 32522, 32536, 33026, 33070, 33374, 33420, 33953, 34263, 35223, 35414, 36083, 36336, 36408, 36498, 37320, 37565, 38764, 41801, 42064): all 20 have a division. Examples: Mehdia = Alipota 8011 (the heading's two OCR pieces at 8011 and 8013; accepted in round 3); Sahbi 9297; Ambia 29528 for `Amiua`; Dehiret el Atrous 15879 and 17625; AUSUGRARA 24772; Bavagaltana 11972; Bel Aït = Tepelta 3444; BlJRUGJATA 12177; C.VTRA 29679; Enfida ville 5011; Fournou = Furnos majus 5197; Brahim (Sidi) = Gunugu 27187; Hanacher 19116; Hermania 13126 (the Préface's erratum corrects it to Hermiana); Medinet es Soultan = Iscina 7931; Liberalia 25682; Faroha = M(anange) 5043; Nechma (Aïn) 21226; TlGUALA 14629; TURRES CONCORDIAE 26569. None is a missing entry.

## (3) Added sub-headings

- Ausvaga II (antiques 12266, ruines 11914), Boset I (antiques 12449, ruines 12093) and BOSET II (antiques 12472). Each is printed alone on its line, with its own bishop beneath it. Each matches a twin already set as a division (`Ausvaga I.`, and `BOSET II.` in ruines 12111). In antiques, BOSET II follows the page-185 running text with no blank line before it. That explains why the blank-line passes missed it. **Fine.** None is invented, and the filing is now the same in both scans.
- Bains romains (antiques 27942, ruines 27053). It is printed alone at the head of p. 444, followed by its `Atl. arch., f. 5, Alger, 8` line, and it is in the Tables (`Bains Romains 444`, antiques 34166). **Fine.**

## (4) Body scan for heading-shaped lines that are not division starts

Method: in each window, every line was flagged that is under 75 characters, starts with a capital, is not a citation, bishop or `Nota` line, and is followed within two non-blank lines by an `Évêché` / `More` / `Atl. arch.` / `C. I. L.` / `Route` line. Each flagged line not at a division start (or within two lines after one, for a wrapped heading) was opened and read.

| file | window | flagged | at a division | not at a division | of those, real headings |
|---|---|---|---|---|---|
| antiques | 4000-6000 | 79 | 63 | 16 | 0 |
| antiques | 16000-18000 | 104 | 87 | 17 | 0 |
| antiques | 27000-29000 | 97 | 83 | 14 | 0 |
| ruines | 4000-6000 | 84 | 63 | 21 | 0 |
| ruines | 15500-17500 | 97 | 82 | 15 | 0 |
| ruines | 26200-28200 | 101 | 85 | 16 | 0 |

Every line not at a division is the end of a running-text or citation sentence. Examples: antiques 27592 `Vageatensis.` ends a `Nota`; 28068 `Golumnata.` ends a milestone quotation; 16415 `Aïch. Tunisie.` ends a `Cfr.`; ruines 4247 `Kicha. 92.` ends an `Atl. arch.` citation. **0 misses.** No pattern of missed entries remains.

## (5) No non-entry divisions among those added

Of the 20 added in antiques and 19 in ruines, the diff of 572f38b12 contains only added division entries plus the status line. Every added start line was opened (sections 1 and 3). Each one is a printed entry heading or a printed numbered sub-heading. None is a bishop line, a `Nota`, a cross-reference or running text. Titles keep the printed text, OCR included. A stray mark in front of a heading (`•`, `i`, `[`) is left out of the title, but the division still starts on that line. This matches the print and does not invent anything.

## Notes, not defects

- The drafter's report gives the unresolved counts but not the line lists the instruction refers to. The reviewer rebuilt the set independently (section 2).
- The report's own caveat (6) still holds: a heading with no blank line before it, no period and out of alphabetical order cannot be ruled out by any scan. None was found in this pass.

## Conclusion

Both scans pass at Mark's bar. The recall failure found in round 3 is fixed at its cause, and an independent check against the index found no further missing entry. These documents need no further rounds.
