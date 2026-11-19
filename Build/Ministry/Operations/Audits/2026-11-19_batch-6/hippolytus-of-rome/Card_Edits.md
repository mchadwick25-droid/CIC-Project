# Card edits: Hippolytus of Rome (`hippolytus-of-rome`)

The existing card (`Card.existing.json`, identical to the census card) is kept word for word in every field it had. The edits are additions only: three `sources.about` entries, `briefReferences` and `quotationOriginals`. No field was corrected: nothing in the existing card is contradicted by a held source or by the brief. No `briefLength`, no connections to other entries. Short names as in `Source_Sheet.md`: HIP, EUS, CHR, LP, DUH, HAR. Every cited line was re-read in its file.

## Kept unchanged (checked)

- knownFor, datesNote, placeNote, role, keyWorks: agree with the brief (paragraph 2) and with HIP 638-643, 1162-1183, 23116-23175; HIP 628-633 (sixteen-year cycles on the chair).
- legacy.traces: JER 40693-40696.
- legacy.remembered: CHR 12909-12913 (Ypoliti in Tiburtina, 13 August); HIP 598-602; EUS 35733.
- uncertain 1: EUS 35521 ("greatly overdrawn"). uncertain 2: EUS 35449 ("over another church"); JER 40690-40691; HIP 852-863 (MacMahon accepts Portus); HIP 832-835 (Döllinger); EUS 35663 ("quite worthless"). uncertain 3: EUS 35669-35688; CHR 13078 (presbiter). uncertain 4: HIP 748, 803-812. uncertain 5: HIP 863-868; EUS 35698-35700.
- "Jerome of Strido" kept: the census uses that form for the author in many cards; not wrong.

## New: sources.about

| Old | New | Evidence |
|---|---|---|
| (none) | Liber pontificalis, ed. Louis Duchesne, 1886, Latin and French, `cic/texts/liber-pontificalis_texte-introduction-commentaire-t1-lat-fra_duchesne1886.txt` | Holds the list of bishops as printed (LP 66804-66809) and Damasus's verse (LP 109159-109166) that the quoted spans come from; Duchesne on the verse (LP 109167-109176) |
| (none) | Histoire ancienne de l'Église I, Louis Duchesne, 1907, French, `cic/texts/duchesne_histoire-ancienne-de-leglise-tome1-fra_3e-ed1907.txt` | Brief: "His Greek books soon dropped out of sight at Rome, where the clergy now wrote Latin" (DUH 11728-11731); "Historians judge that Damasus confused two different splits" (DUH 11718-11727) |
| (none) | Die Chronologie der altchristlichen Litteratur bis Eusebius II, Adolf Harnack, 1904, German, `cic/texts/harnack_geschichte-der-altchristlichen-litteratur-chronologie-band2-deu_1904.txt` | Brief: "some doubt there was any split" (HAR 11879-11889, Batiffol); "though some doubted it" (HAR 11870-11874); death on the island (HAR 11976-11979) |

## New: briefReferences

One line per brief paragraph (8). No quotation marks.

1. Ark: HIP 13909-13912 (Refutation IX, ch. VII).
2. Essence: EUS 35454, 35482-35504 (dates), 35722 (all in Greek); HIP 13870-13952; CHR 13078 with 13104-13105 and LP 66807-66808 (exile); EUS 35669-35686, HAR 11912, DUH 11685 (rival church).
3. Noetus: HIP 23116-23175 (Against Noetus 1), 23442-23450 (ch. 7).
4. Callistus's past: HIP 13285-13295, 13640-13641 (IX, ch. VI), 13672-13751; EUS 35509-35521 (McGiffert's note in Church History VI.21).
5. Charges and the rival-church question: HIP 13870-13952; HIP 1130 (preface); EUS 35669-35686; HAR 11912; DUH 11685; CHR 13716-13728 and HIP 852-863 (Portus); HAR 11879-11889 (Batiffol); HIP 878-879 (after 222); HIP 1162-1183 (Greek philosophy).
6. Sardinia: LP 66807-66808; CHR 12909-12913 (13 August); EUS 35698-35700; HAR 11976-11979.
7. The book: DUH 11728-11731; HIP 638-643 (Coxe, 1842), 748 (1851), 803-806 (majority); HAR 11870-11874 (doubters).
8. Damasus: LP 109159-109166; LP 109167-109176 and DUH 11718-11727 (confusion); CHR 13738-13740 (Mommsen); census `novatian` for the split of 251.

## New: quotationOriginals (8 spans, all awaiting second reading)

The census card had no `quotationOriginals`, so every span is new and no `secondReading` is set. Each `modern` is the brief's span exactly.

1. "He also said that Noah's ark was made as a sign of the church ..." Printed: MacMahon's English, HIP 13909-13912 ("But also he affirmed that the ark of Noe ..."). Awaiting second reading.
2. "Christ did not say, 'I and the Father am one,' but 'are one.' ..." Printed: Salmond's English, HIP 23442-23450 ("He did not say, “I and the Father am one, but are one.” ..."). Awaiting second reading.
3. "worshippers of two gods." Printed: HIP 13640-13641 (Refutation IX, ch. VI). Awaiting second reading.
4. "high-priesthood." Printed: HIP 1130 (Refutation, preface). Awaiting second reading.
5. "the elder Hippolytus," Printed: "Yppolitus presbyter", LP 66807 (the list of bishops as Duchesne prints it; CHR 13078 has the same words, but its scan reads "presbitcr"). Awaiting second reading.
6. "the unhealthy island." Printed: "in insula nociva", LP 66808 (CHR 13104 scans "uocina"; Duchesne, LP 109188-109191, takes nociva as the right reading). Awaiting second reading.
7. "It is said that Hippolytus, an elder, while the tyrant's orders pressed hard, had stayed all along in the split of Novatus." Printed: Damasus lines 1-2, LP 109159-109160. Awaiting second reading.
8. "Damasus tells what he has heard. Christ tests it all." Printed: LP 109166. Awaiting second reading.

## Flags for the person who runs the check

- The validator requires `secondReading` on every entry, so the card fails until the second-reading step fills all eight.
- Span 7: the printed Latin does not stand verbatim in the scan. LP 109160 reads "presbyter in scismk SEMPER MANSISSE XOvali." for "presbyter in scisma semper mansisse Novati." The card gives the printed reading. It passes only once those two scan faults (scismk for scisma, XOvali for Novati) are listed in `tools/quote_scan_readings.json`, which I did not edit. No other held file carries the verse whole (CHR 13740 has the last line only, scanned "Itaec ... oinnia").
- The brief's English renderings of the Latin (spans 5-8) will also need listing in `tools/quote_renderings.json` for the census quote check; not done here.

## Claims not found

None. Every statement in the existing card was found at a cited line.
