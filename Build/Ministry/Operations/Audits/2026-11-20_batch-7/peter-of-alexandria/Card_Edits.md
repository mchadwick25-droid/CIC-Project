# Card edits: Peter of Alexandria

Card writer, batch 7, 2026-11-20. Existing card: `Card.existing.json` (the census `card` object for `peter-of-alexandria`). Result: `peter-of-alexandria.card.json`. Brief: `peter-of-alexandria.brief.txt` (about 638 words, about 4 minutes 15 seconds; `briefLength` is not a census card key, so it is not on the card).

Every existing statement is kept word for word and in its order, apart from the spelling edit and the additions below.

## Clearly wrong

None. Checked against the held sources and the brief; each quotation on the card stands at its lines (EUS 47994, 44798-44800; ATH 22465, 1676-1685; SOC 3203-3220, 4007; BELL 3153-3157; ANF6 28222-28224; EUS 43251-43253). The dates of the split (ATH 1638, HEF 22104, BELL 3168), Sozomen on Arius (SOC 27552-27563), Maffei (ANF6 16704-16705) and McGiffert on the bishops' letter (EUS 44329-44330) hold.

## Spelling (Melitius, as the census spells it; instruction of the coordinator)

Old: "Meletius", "Meletian", "Meletians". New: "Melitius", "Melitian", "Melitians". Places: `knownFor`; `keyWorks[1].about`; `legacy.traces[1]`; `uncertain[0]`, `uncertain[1]`; `sources.about` titles for the four bishops' letter and for Bell's chapter. No quoted wording contains the name. Evidence: the brief's spelling; Source_Sheet X8.

## New

1. **`keyWorks[0].about`, three sentences added** after "and on those who fled": those who paid to be left in peace or withdrew to save their lives (canons 12 and 13, ANF6 27483-27485, 27536-27538, 27602-27603); those who rushed in unbidden still share communion (canon 9, ANF6 27039-27046); those whose hands were burned, as the martyrs' letters from Libya say (canon 14, ANF6 27634-27646). The Outline and Recheck sent E9, E11 and E12 to the card.
2. **`legacy.traces`, a third line.** The Council in Trullo, 692, canon 2 (NPNF14 26731-26744); Nikodemos's view that by that seal the canons take on, in a way, the force of a council of the whole church (PED 49704-49706). Brief, paragraph 7.
3. **`uncertain`, four lines added.** (a) 306 against Nikodemos's 304 (EUS 43238-43240; ANF6 25777-25779; PED 49702-49703; the Review sent this to the card). (b) Bell on the prison (BELL 3198-3200), beside the Epiphanius and Hefele lines already on the card. (c) Peter in hiding: Bell 3205-3207, Hefele 21952-21954, the account kept with the letter ANF6 16836-16837; the brief says "probably in hiding". (d) The year of death: EUS 43218-43226; ANF6 25767-25776; BELL 3210-3212.
4. **`sources.ownWords`, one entry added:** the Pedalion, Greek of canon 1 and Nikodemos's note (PED 49702-49723).
5. **`sources.about`, three entries added:** Eusebius, Martyrs of Palestine 3 (EUS 46173-46178); Panarion 68 in Migne's PG 42 (the second print of the Greek of Quote 2); the Council in Trullo, canon 2 (NPNF14).
6. **`briefReferences`, fifteen lines added**, one for each place the brief draws on. No quotation marks: the brief quotes only its three spans.
7. **`quotationOriginals`, three entries added**, one for each quoted span. The census card had none, so every span is new and has no `secondReading`.
   - Q1, the canon: printed English ANF6 26616-26618; Greek PED 49722-49723, hand-checked word by word. The scan prints σίγματα; the ANF6 note at 26619 prints στίγματα, which confirms the reading.
   - Q2, Epiphanius: no English translation is held, so the Greek is the print (Oehler 43852-43853), hand-checked. The scan prints a numeral 0 for ὁ; PG 42 (13796-13799) prints ὁ, which confirms it. PG's own faults (Μελητίον, χαὶ) are not used.
   - Q3, Eusebius: English alone (EUS 47996-47998). The Greek (EUS-G 17556-17560) is held only in a damaged scan (διαξιμίνου, χαὶ, ὡἧς) with no confirming print, so it is not printed.

## Needed in shared files (not touched here)

`tools/quote_scan_readings.json` needs two readings before the census check passes:
- `nikodemos-hagiorite_pedalion-canons-grc_1886.txt`, line 49723: scan "σίγματα", reads "στίγματα"; confirmed by ANF6 line 26619.
- `epiphanius_panarion-haer-48-69-corpus-haereseologicum-t2-pars-posterior-grc-lat_oehler1860.txt`, line 43852: scan "Πέτρου 0 λόγος", reads "Πέτρου ὁ λόγος"; confirmed by `epiphanius_panarion-haer-65-80-pg42-grc-lat_migne1863.txt` line 13797.

`tools/quote_renderings.json` needs a listing for each of the three spans (renderings of non-English originals, and of the Greek in Q2).

## Awaiting second reading

| Modern span (brief) | Printed | File and lines |
|---|---|---|
| "They did not come to this by their own choice. The weakness of the flesh betrayed them. For they show the marks of Jesus in their bodies." | "for they did not come to this of their own will, but were betrayed by the frailty of the flesh; for they show in their bodies the marks of Jesus"; Greek PED 49722-49723 | ANF6 26616-26618 |
| "Peter's case was for mercy and kindness. The case of Melitius and those with him was for truth and zeal." | Greek, Panarion 68.3 | EPI 43852-43853 (PG 42 13796-13799) |
| "He was seized for no cause, when no one expected it. All at once and with no reason given, as though on Maximinus's order, he was beheaded." | "being seized for no cause and quite unexpectedly, was, as if by command of Maximinus, immediately and without explanation, beheaded." | EUS 47996-47998 |

## Not found

- "Later Coptic and Ethiopic lives give a family, and do not agree with each other" (`uncertain`). The held Coptic life (24858 on) calls Peter Theonas's "son and disciple" and gives no family; the held Ethiopic Synaxarium has only index entries for Peter and names him as Theonas's successor (19817-19818). Left in place.
- "Socrates of Constantinople and Theodoret say the same" (`uncertain`). Socrates has the sacrifice charge (SOC 2405-2409). Theodoret says only that Peter deposed him for certain crimes (THDT 6551-6556), with no council and no sacrifice. Left in place.
- The `sources.about` title for Socrates and Sozomen lists Socrates 1.6 and 1.9; the legacy line draws on Socrates 1.15 (SOC 4007-4008). Title left as it is; 1.15 is in `briefReferences`.
