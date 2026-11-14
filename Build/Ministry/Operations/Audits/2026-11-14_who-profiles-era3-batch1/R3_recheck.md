# R3 recheck: era 3 batch 1

Scope: round 3, the last allowed. This is a targeted recheck of the round 2 changes only (`git diff 0e61224d 2515c8a8`), against `R2_recheck.md` (N1 to N5 and the PARTLY items) and `R2_changes.md`. Under `era3/batch1/`, six files changed: the Lazar brief, audio and card, the Barsauma and Narsai cards, and `records.json`. The README change (`2d11789d`) was already read by R2. Open-Gaps entry 242, new at the end of `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md`, was checked line by line against held files and the R1 and R2 files. Unchanged text was not reviewed again. Each changed sentence was opened at its line in the vendored file, with XML tags stripped and whitespace collapsed, to confirm who is speaking. I edited no drafts, and I made no paid calls, model calls or web requests. Line numbers point to files under `cic/texts/` unless another path is given.

## 1. The R2 findings

| Finding | Status | Check against source |
|---|---|---|
| N1 Vardan record: Langlois's date tagged Widely Accepted | RESOLVED | The claim "Victor Langlois places Lazar at the end of the fifth century or the start of the sixth" is now `Dominant Modern Reconstruction`. That matches the Lazar record. Langlois: "Il vécut à la fin du cinquième siècle ou au commencement du sixième" (Langlois t2 l.35079–35081), in the introduction signed "V. L." (l.35357). |
| N2 Lazar brief l.1: "even in the camp" moved onto the psalms | RESOLVED | Brief and audio: "They said the psalms in their minds as they took up their weapons." Lazar: "ils suivaient les exercices spirituels même dans le camp… En prenant les armes, ils récitaient mentalement des psaumes" (Langlois t2 l.43192–43198). The camp detail stays in records claim 1 (`records.json` l.856), correctly apart. |
| N3 Lazar card `uncertain` 4: "instead" with nothing to point to | RESOLVED | "Langlois says Vahan put him in charge of the mother church at Etchmiadzin. Stephen of Taron, an Armenian historian of about the year 1000, says instead that Vahan made him head of the monks of Surenay-Anapat." Langlois: Vahan "restaura la métropole d'Edchmiadzin… fit chercher Lazare… et lui confia l'administration de la métropole" (l.35197–35202). Stephen: "gab ihnen zum Oberhaupt den Redner und Geschichtsschreiber Lazar Pharbeci" (`stepanos-taron_armenische-geschichte-deu_gelzer-burckhardt1907.txt` l.2933–2936); "Stephanus, fl. ca. 1000" (l.22). "Instead" now has its referent. |
| N4 One epithet spelled two ways | RESOLVED | On both cards, the Cause entry's author is "Barhadbeshabba 'Arbaia, bishop of Halwan" (Barsauma l.51, Narsai l.64). It sits beside "Barhadbeshabba 'Arbaia" for the History (Barsauma l.58, Narsai l.57). No "'Arbaya" is left in the batch. Nau: "Rarbadbesabba' 'Arbaia" (PO 9 l.31560); "Bar Hadbesabba Arbaia, qui etait eveque de Halwan en 605" (l.31579–31580). Scher: "Mar Hadb$abba 'Arbaia, évèque de Halwan" (PO 4 l.656, OCR). |
| N5 Lazar card `uncertain` 7: "The copy used here is a rough scan." | RESOLVED | The sentence is gone. The item reads "Langlois says Samuel Ghesarian translated from the only printed text, the Venice edition, and that this text is faulty." Langlois: "Il n'existe qu'une seule édition… publiée par les soins des Mékhitaristes de Venise" (l.35282–35284); "le seul texte qu'il avait à sa disposition est malheureusement incorrect" (l.35346–35348). No build narration remains in the batch's cards. |

## 2. The R2 PARTLY items

| Item | Status | Evidence |
|---|---|---|
| Vardan B2 (blocking; the tag) | RESOLVED | Closed by N1, above. |
| Barsauma M6 (the epithet in the source fields) | RESOLVED | Closed by N4, above. |
| Lazar M1 (the camp) | RESOLVED | Closed by N2, above. |
| Lazar M6 (Stephen of Taron's account set against Langlois's) | RESOLVED | Closed by N3, above. |
| Moses M1 (log that the late date rests on no held line) | PARTLY | Open-Gaps 242 now has the log: "The brief says the Library holds only one side; the Contested tag stays, as the coordinator ruled." Carrière is on the Library want list. Two of its sentences, though, misstate what the held lines carry (N6). |

## 3. Open-Gaps 242, checked

These statements hold against the held lines or the R1 and R2 files:
- List lines. Of the ten, people rows in `cic-website/data/world-census.json` exist for Dioscorus and Timothy (movement 42), Narsai and Barsauma (44), Elishe and Lazar (45) and Victor (56). Vardan and Euthymius appear only in `voices`, and Moses has no row. That is seven, as stated.
- Victor's card tradition. Movement 56 is "Gothic, Vandal & Lombard Homoian Christianity", which matches card l.10 and the README.
- Not held:
  - The Letter to Vahan: Langlois l.35100 and 35291, and the scan row l.54.
  - Timothy's Refutation has no translation: records `absent_details`.
  - Cyril is held only in Cotelier's Latin, and the census cites "trans. R. M. Price… 1991" (movement 47).
  - Victor is held only in the 1605 English.
  - The Chronicle of Seert's Barsauma sections are not held. The held fascicle (PO 5) is described in its own header as breaking off in the early fifth century, and it says the part that follows (PO 7) is not vendored.
- Scan years:
  - Timothy "patriarch 457-477" (scan l.35). The file header has "d. 477" (timothy-aelurus file l.2), and Evetts's heading is "A. D. 458-480" (l.35194).
  - Euthymius "377-473" (scan l.62).
  - Narsai "c.413" (scan l.47; Connolly file header l.3).
  - Dioscorus 454: Feltoe "in 454" (npnf212 l.762–766); Nau "mourut le 4 septembre 454" (Theopistus l.176–180); Evetts's heading "A. D. 444-458" (l.34864).
  - Barsauma "fl. 457" (scan l.48) and the 435 date: Scher (PO 4 l.20625, 20820); Abbeloos–Lamy's note on Cod. Syr. Vat. 39, "Christi 435" (vol. III l.3651–3653).
  - Ormanian's 26 May (l.2256), and the 2 June of the note in Lazar's French (Langlois t2 l.40450–40451). Lazar's own text names the Friday of Pentecost and no year (l.40213–40214).
  - The scan's "All his speeches are Eghishe's composition" (scan l.52).
  - Brosset's "446 — 499" (`brosset_histoire-de-la-georgie-pt1-fra_1849.txt` l.870).
- Scan places:
  - The Vardan row's "langlois_t2_1869 36587-36712 (Lazar)". That line is Lazar's account of the Persian plans, while the Vardan narrative is at l.38815–38822 and l.40118–40124.
  - The Lazar row's "translator Ghesarian's introduction" is signed "V. L." (l.35357).
  - Barhadbeshabba is held in PO 9 and PO 4, and the scan cites him only "via Connolly 270-280" (scan l.47).

### New findings

- **N6 MINOR (Open-Gaps 242, the "Not held" item on Carrière and the "Moses of Khoren's date" item; Moses M1; a held line made to say more than it does).**
  - "Carrière's study of Moses of Khoren (1895), the one named work for the late date" and "The later date appears only in a Library file header and a bibliography title in Harnack" both treat Harnack's line as a witness to the late date. The line is a bare title in a bibliography on the Abgar legend: "Carriere, La legende d'Abgar dans l'histoire d'Armenie de Moise de Khoren, Paris 1895." (`harnack_geschichte-der-altchristlichen-litteratur-chronologie-band2-deu_1904.txt` l.9335–9336). It names no date and no argument. R1 found it "by title only (l.9336-9337)", and the records note says the same (`records.json` l.647).
  - The only held places that name the later dating are the Italian edition's file header, "traditionally 5th c. CE; modern scholarship debates the work's actual date" (`moses-khoren_history-of-armenians-ita_mechitaristi1850.txt` l.4–5), and the era 3 scan ("modern scholarship: 8th-9th c.", `Who_Scan_Era3.md` l.61).
  - "Every held work takes the fifth-century date" also overstates. Macler gives Moses no date: "On ne sait pour ainsi dire rien de précis sur Lazar de Pharbi ou Moïse de Khorën" (`stepanos-taron_histoire-universelle-deuxieme-partie-fra_macler1917.txt` l.672–673). R1 established only that no held work argues a later date.
  - Fix, "Not held" item: replace "Carrière's study of Moses of Khoren (1895), the one named work for the late date (the coordinator's ruling, 2026-11-14)" with "Carrière's study of the Abgar legend in Moses of Khoren (Paris 1895), which Harnack lists by title only, so no held line says what date it argues (on the want list by the coordinator's ruling, 2026-11-14)".
  - Fix, "Moses of Khoren's date" item: replace "Every held work takes the fifth-century date (Langlois; the Mekhitarist preface). The later date appears only in a Library file header and a bibliography title in Harnack." with "No held work argues the later date; Langlois and the Mekhitarist preface take the fifth century, and Macler says almost nothing precise is known of him. The later date appears only in the Library's file header for the Italian edition and in the era 3 scan."

- **N7 MINOR (Open-Gaps 242, "Scan corrections"; a date given to the wrong part of an editor's work).** "the 2 June of Neumann's preface and a note in Lazar's French" is wrong. Neumann's preface gives the month only: "the fatal battle fought on the banks of the Dekhmud, in June 451 of our era" (`eghishe_history-of-vartan-and-the-armenian-war_neumann1830.txt` l.757–758). The day is in his margin, "June 2." (l.4147). R2 and the Vardan records `contested_claim` both read it this way ("Neumann's margin: June 2 (l.4147), and his preface, June 451 (l.758)"). Fix: "Both dates for Avarayr are modern: Ormanian's 26 May; Neumann's June 451 (preface) and 2 June (margin); and the 2 June of a note in Lazar's French."

- **N8 MINOR (Open-Gaps 242, "Scan corrections"; R1's Lazar B1 framing restored in the log).** The list "Years that rest on no held line" includes "the census year 485 for Lazar". That 485 does match a held line, Neumann's end date for the History: "from 428 to 485" (`eghishe_neumann1830` l.1019–1021). Treating 485 as resting on no held line was R1's Lazar B1. The records now put it right: "The census year 485 matches Charles Neumann's end date for the History" (Lazar `absent_details` 1). Fix: take Lazar out of that list and add after it: "The census year 485 for Lazar is not a year of his life: it matches Neumann's end date for the History, 'from 428 to 485' (preface to Elishe)."

- **N9 MINOR (Open-Gaps 242, "Scan rows that cite the wrong place"; the scan row misdescribed).** "Langlois's introduction to Elishe (l.25692-26100, not 27333)" gives the scan a citation it does not make. The Elishe row cites "langlois_t2_1869 27333 on (new translation of the same History)" (`Who_Scan_Era3.md` l.53) and does not cite Langlois's introduction at all. Line 27333 is inside the translation, in the bishops' list. The introduction ends at "182 INTRODUCTION" (l.26100), and "CHAPITRE PREMIER" opens at l.26255. Fix: "Langlois's translation of Elishe opens after his introduction (l.25692-26100), with chapter one at l.26255, where the scan gives '27333 on'; the scan does not cite the introduction, which is the source for Elishe's life."

- **N10 MINOR (Open-Gaps 242, "Not held, and noted on the cards"; the heading says more than the batch does).** Of the items under this heading, only the Letter to Vahan is noted on a card (Lazar `uncertain` 1). The following are noted only in `records.json` `absent_details`: Carrière (l.646–647), Timothy's Refutation, Dioscorus's letters, the Cyril texts and a clean English Victor. The Chronicle of Seert is noted nowhere in the batch: no card, records entry or README names it. Fix: "Not held, and noted in the cards or `records.json` (the Chronicle of Seert is not noted in the batch):".

Observation only, not a finding: 242 cites "Decision-Log, 'Who profiles, era 3 batch 1' (2026-11-14)" and calls the profiles approved to proceed. At `2515c8a8` the Decision-Log has no such entry (the last is era 2 batch 6). For era 2 batch 6, the Decision-Log entry and Open-Gaps 241 landed together after R3. The closing commit should add the entry under that exact title.

## 4. Mechanical checks

- All ten audio scripts equal their briefs once `[calmly] ` and `[warmly] ` are removed (checked by script). Each has one `[calmly]` and one `[warmly]`.
- `grade_text` (`engine.m1.gates`) on `lazar-parpetsi`: FK 7.98, Flesch 66.41. That passes (FK at most 10, Flesch at least 60). It is 321 words, about 1:59, matching R2's scoring of the N2 fix.
- All eleven JSON files in the batch parse (ten cards and `records.json`).
- Card, brief and records agree on every changed point.

## Verdict

R2's N1 to N5 are all resolved and hold against the sources, and so are four of the five PARTLY items. Moses M1 is PARTLY: its log now exists in Open-Gaps 242, but it misstates Harnack's line (N6). No change to a card, brief, audio script or `records.json` adds a wrong attribution or a claim the source does not carry. The ten profiles clear review at round 3. The five new findings are all in Open-Gaps 242, a tracking entry owned by the coordinator. They are corrections to that entry, not a further revision round on the profiles.

## Totals

R2 findings: N1–N5, 5 of 5 RESOLVED. PARTLY items: Vardan B2, Barsauma M6, Lazar M1 and Lazar M6 RESOLVED; Moses M1 PARTLY (N6). None NOT resolved. New: 0 blocking, 5 minor (N6–N10, all in Open-Gaps 242); the profiles clear at round 3.
