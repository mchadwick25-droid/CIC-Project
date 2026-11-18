# Card check: batch 3 (2026-11-17)

Checker for Process.md step 6 and `roles/card.md`. Nine cards, each compared with its `.original.card.json`. Every quotation's modern wording was matched against the finished brief, and every printed wording was re-read at its file and lines in `cic/texts/`. Each cited line was opened. Where a changed field is a list or object (`sources`, `legacy`), the pre-existing items were compared and found word for word, in their order, with nothing removed. Where a card writer filled in a `secondReading` verdict, it is not judged here. It is to be replaced by the blind second reading.

Result: 7 PASS, 2 FIX (Justin Martyr, Arius).

---

## justin-martyr: FIX

- `briefLength` "about 3 minutes 10 seconds": justified. It is new, and 470 words at 150 a minute is 3:08.
- `briefReferences` (14): justified. Each is new from the brief. All the cited lines were opened and say what the entries claim (R1 72–75, 124–126, 729–731, 1230–1234; AR 87–89, 139–141, 163–169, 175–180, 399–401, 788–791, 6603–6605; R2 136–139, 273–276, 368–370; Gebhardt 1347–1353, 1423–1438; EUS 22420–22422, 23764–23787; anf01 33663–33667, 44907–44918; anf05 12996–13006; Tatian 7956–7960; anf02 6526–6533, 6550–6556; anf03 43161–43163). Note: "the death about 165" is not in EUS 23764–23782. McGiffert gives it at EUS 26223 ("after Justin's death (165 a.d.)"), so the entry holds, but the evidence in Card_Edits should add 26223.
- `quotationOriginals` (3): the modern wording matches the brief exactly. The Greek is verbatim at Archambault 429–435 (across the section break 1/2) and at Gebhardt 1410–1411 and 1420–1421, with the OCR kept. The English at anf01 17853–17857 and 29371–29374 is as quoted. **Two faults in form**, both of which the census check (`tools/validate-census.mjs`, QUOTATION_ORIGINAL_KEYS and wordingFault) rejects:
  1. The Greek is under the key `original`, and there is no `printed`. `printed` is required, and `original` is allowed only together with `originalFile` and `originalLines`. **Correction:** in all three entries, rename the key `"original"` to `"printed"`. Change nothing else. (Precedent: the Nicaea and Hild entries give the Greek or Latin as `printed`.)
  2. `cic/texts/acta-martyrum-selecta_gebhardt1902.txt`, the file cited by entries 2 and 3, is not among the card's sources. **Correction:** append to `sources.about`: `{"title": "The Martyrdom of Justin and his companions, Greek, in Acta martyrum selecta (ed. Oscar von Gebhardt)", "author": "Unknown", "date": "1902", "language": "Greek", "file": "cic/texts/acta-martyrum-selecta_gebhardt1902.txt"}`. List it in Card_Edits as a new edit.
- Existing statements: all were re-checked and hold (anf01 13965–13969; EUS 21864–21865, 23774–23787; anf01 29213–29220, 29257).

## vardan-mamikonian: PASS

- `briefLength` "about 3 minutes 15 seconds": justified. It is new: 492–495 words at about 150 a minute.
- `sources.about`, fourth entry (Langlois tomes 1–2 scan): justified. It is the file all three quotations cite, and it holds Elishe's French, which no existing entry names. The three existing entries are untouched. Note: the same text is also in the card's existing tome-2 scan (`…tome2-fra_1869.txt` 30569, 39136), but that scan has worse OCR. Choosing the cleaner scan is not a fault.
- `quotationOriginals` (3): each modern wording matches the brief. Each printed wording is verbatim at L12 91072–91076, 90623–90626 and 82667–82673, with the OCR kept ("parini", "ua", "nous.le", "ordresiniques", "estle"). Neumann's English at N 3928–3934 is as noted.
- `briefReferences` (17): justified. The lines opened bear out each entry (L12 87726–87729, 87776–87779, 90618–90626, 90690–90698, 90795–90799, 90889–90891, 90958–90966, 91056–91076, 91122–91126, 80463–80471, 91615–91625, 95201–95205, 95332–95334, 95976–95983, 99215, 99484–99498, 100500–100512, 100549–100552, 87287–87289, 92126–92128, 92384–92387; N 1116–1118, 1470–1473, 2204–2209, 2372–2383, 2402–2421, 2444–2446, 2647–2659, 2890–2893, 2957–2961, 4162–4166, 4175, 4227; O 2254–2262, 2287–2294).
- Nothing was corrected, and nothing needed to be.

## moses-the-black: PASS

- `briefLength` "about 2 minutes 10 seconds": justified. It is new, at 331 words.
- `sources.about`, Ethiopian Synaxarium: justified. It is new, and it carries the brief's "later Ethiopian tradition". The text is at 37094 and 37160–37185 ("the Barbanans came and killed him", OCR). The four existing entries are untouched.
- `briefReferences` (9): justified. LH 333, 335 and 337, Clarke's notes 657 and 713, PAR2 164 and 1028, and the Synaxarium were all re-read and match.
- `quotationOriginals` (3): the modern wordings match the brief. The first two are broken around "he told the brothers" and "they said", which the census rule allows as one entry. The printed wordings are verbatim at LH 335 (twice) and PAR2 1028.
- `secondReading` ("minor", "minor", "same"): filled in by the card writer and not judged here. To be replaced by the blind second reading.
- Existing statements: all were checked and hold. `knownFor` "driven out for robbery" is partial against LH 333 ("immorality and brigandage") but is not contradicted.

## alopen: PASS

- `briefLength` "about 1 minute 10 seconds": justified. It is new, at 181 words.
- `quotationOriginals` (1): the modern wording matches the brief exactly. The printed wording is verbatim at MAL 13688–13689.
- `briefReferences` (5): justified. MAL 13684–13693; LEGGE 1008–1012, 1243–1246, 1254–1258, 1475–1478, 1633–1640, 1863–1871, 4340–4350, 4389–4390; YULE 2908–2910, 2929–2931 all hold.
- `sources.about`, Legge 1888: justified. It is new, the brief draws on it, and the eight existing entries are untouched.
- `knownFor` "from Syria" → "from the far west": justified as a correction. "Syria" is Wylie's rendering of Ta Ts'in (MAL 13687), and Legge keeps "Ta Ts'in", "the Far West from China" (LEGGE 1011, 4117–4118). The card's own `placeNote` marks it as a rendering. The finished brief says "from the far west", and its outline rules out "from Syria" as plain fact. Two words changed.
- `knownFor` "a church" → "a monastery": justified as a correction. Legge has "a Ta Ts'in monastery" with the note "Not 'a church'" (LEGGE 1256–1258, 1285), Budge's Saeki has "monastery" (5209–5211), and the brief has "built a monastery". One word changed.
- `legacy.traces[2]`, clause added: justified. Williams's report is kept word for word. The added clause corrects the implication that the 3,000 were all Christians: Legge's edict reads "as well those of Ta Ts'in as of Mu-hu-pi, amounting to more than 3,000 persons" (LEGGE 4346–4350), and Yule agrees (3291–3292). This matches the brief's "Christians and others". It is the fewest words that both keep Williams's report and set it right.

## baudonivia: PASS

- `briefLength` "about 2 minutes 10 seconds": justified. 346 words is 2:18 at a strict 150 a minute, but it matches the pace of the finished era-3 cards (about 160 a minute, 320 words = "about 2 minutes"). Not a fault.
- `briefReferences` (10): justified. SRM2 29433–29441, 29492–29499, 29663–29675, 29743–29745, 29987–29995, 30238–30261, 30302–30312, 30519–30523, 30581–30584, 28170–28197, 28219–28233; AA4 43014–43015, 41896–41900, 41917–41920 all hold. ("Radegund, wife of King Chlothar" in the ch. 5 entry is not in ch. 5's own lines, but it is not in doubt; see AA4 41896.)
- `quotationOriginals` (3): the modern wordings match the brief. The printed wordings are verbatim with the OCR kept, at SRM2 29492–29493, 30245 and 30522.
- Nothing was corrected. Leaving the PL72 entry in place is right, since no held source contradicts it.

## arius: FIX

- `briefLength` "about 3 minutes": justified. It is new, at 458 words.
- `sources.ownWords`, Epiphanius Panarion 69.6 (Oehler): justified. It is the file Q1 cites.
- `sources.about`, Socrates 2.10 (Hussey Greek): justified. It is the file Q3 cites.
- `sources.about`, the Creed of Nicaea (npnf214): justified. Two quotations cite it (2419–2425).
- `sources.about`, Mansi 3, Aquileia: justified. It is the brief's Aquileia beat: "Ego Arium non novi" (60273), "Qui fuerit Arius, ignoro" (61131–61133), and Palladius anathematised and deposed (60851–60853, 61004–61008).
- `sources.about`, Kauffmann 1899: justified. "einstimmig wurden Palladius und Secundianus als ketzer ihrer ämter für unwürdig erklärt" (1957–1958).
- `briefReferences` (12): justified. Spot-checked against npnf204 19016–19019, 41470–41480, 57414–57419; npnf203 6024–6027, 6044–6046; and the Mansi and Kauffmann lines above.
- `quotationOriginals` Q2 and Q4–Q7: the modern wordings match the brief, and the printed wordings are verbatim (npnf204 41472–41479, npnf203 6026, npnf204 19018, npnf214 2422 and 2422–2423).
- **Q1 and Q3: the printed wording is not verbatim.** The card writer "corrected mechanically" the OCR. The printed wording must stand as the file has it, with the true readings given in `uncertain`, as Vardan, Baudonivia and Justin do. **Exact corrections:**
  - Q1 `printed` → `Διωκόμεϑα δὲ ὅτι εἴπομεν, ᾿Δρχὴν ἔχει ὁ υἱὸς, ὁ δὲ ϑεὸς ἀναρχός ἐστι.` (Oehler 45736–45738). Q1 `uncertain`: replace its first sentence with: `The file is OCR, kept as it stands: ᾿Δρχὴν reads Ἀρχὴν, ἀναρχός reads ἄναρχός, and ϑ is the scan's θ; line 45737, inside the span, is scanned apparatus.` Keep the sentence on εἴπομεν.
  - Q3 `printed` → `Ἡμεῖς οὔτε ἀκόλουθοι ' Apelov γεγόναμεν. πῶς γὰρ ἐπίσκοποι ὄντες ἀκολουθήσομενν πρεσβυτέρῳ ;` (Hussey 16658–16659). Q3 `uncertain`: replace its first sentence with: `The file is OCR, kept as it stands: ' Apelov reads Ἀρείου, and ἀκολουθήσομενν reads ἀκολουθήσομεν.` Keep the sentence on πρεσβυτέρῳ.
  - Card_Edits N8 and N10 to say the same. (The census check folds Greek away, so it would not catch this. The rule is verbatim regardless.)
- **Ruling on the not-found claim**, `legacy.traces[0]` ("The churches later called Arian, which held with him that the Son was not eternal."): **leave in place, not found as worded.** The held sources give partial support only. At Aquileia in 381, Ambrose asks Palladius whether, "juxta epistolam Arii", the Son "non est sempiternus", and Palladius evades. The margin reads "Nota miram haeretici tergiversationem" (Mansi 3 60104–60110; Kauffmann 5510). Eusebius of Bologna asks whether he holds "solum Patrem sempiternum, & filium aliquando coepisse", and Palladius answers only that he never saw Arius (Mansi 3 60152–60154; Kauffmann 5669–5670). That shows one Homoian bishop refusing to call the Son everlasting. No held source shows the later "Arian" churches as a body holding that the Son was not eternal. Nothing held contradicts the claim, so card.md does not allow a correction. Register it in the Arius Open_Gaps_Tracking.md as unsupported, so that it is not left quiet.

## thomas-a-kempis: PASS

- `briefLength` "2 minutes 30 seconds" → "2 minutes 40 seconds": justified as a correction. The finished brief, after Brief_Correction.md, is 402 words (`wc -w`; Card_Edits says 400, which is immaterial): 2:41 at 150 a minute. The old value contradicts the brief.
- `legacy.traces[1]`, the Ignatius entry: justified as a correction. The Gerçonzito passage is no. 97 of Câmara's Memoriale, not the story of his life: the running head is "MEMORIALE P. CONSALVII DE S. IGNATIO" (9255), and the passage is at 9400–9406. The Memoriale was begun on 26 January 1555, and no. 97 is in its Spanish part (765–776). "In 1555" is taken from the brief. The rest of the entry is word for word.
- `sources.ownWords`, Pohl Opera II (Imitation I.1): justified. Q1 cites it (595–605, 702–706).
- `sources.ownWords`, Pohl Sermons to the Novices: justified. "in unum collegi … simplicibus placere cupiens" (254–261).
- `sources.about`, Methodist Minutes: justified. "From four to five in the morning … Kempis" (2648–2653).
- `sources.about`, Woolman: justified. "a man of a true Christian spirit" (12189–12192).
- `briefReferences` (17): justified. Busch 5410–5415, the Memoriale lines and the sources above were re-read and match.
- `quotationOriginals` (2): the modern wordings match the brief. Q1 is verbatim at Pohl II 704–706. Q2 is verbatim at Scripta 9403–9406, with the line-break hyphen joined and the footnote mark after "Ger^onzito" left out, both as declared in `uncertain`. The editors' note is at 9429.

## narsai: PASS

- `briefLength` "about 2 minutes 45 seconds": justified. It is new, at 411 words.
- `quotationOriginals` (2): the modern wordings match the brief. The printed wordings are verbatim at Scher 20743–20746 (hyphen joined) and Connolly 6857–6858.
- `briefReferences` (13): justified. Spot-checked: Edessa Chronicle 189 ("An. 800, the school of the Persians was eradicated"), Guidi 9884–9888 and 9948–9952, Bar Hebraeus 4554–4557 (fifty years), Connolly 7089–7092 (Leper / Harp), and Assemani BO I 47487 ("Narfes Leprofus"). All hold.
- Nothing was corrected. The card's existing dates and uncertainties agree with the brief.

## john-wyclif: PASS

- `briefLength` "2 minutes 30 seconds" → "2 minutes 50 seconds": justified as a correction. The finished brief is 423 words, which is 2:49.
- `sources.about`, Palacký, Documenta: justified. Q1 cites it (15240–15250).
- `sources.about`, Raynaldus vol. 28: justified. It is the brief's "Martin V later ordered them burned": "facias exhumari … et igne publice concremari" (8013–8015), dated "V id. Decembris, anno xi" (8018–8019), with the letter's heading at 7971–7975. The fourteen existing entries are untouched.
- `briefReferences` (16): justified. Spot-checked against Palacký 15240–15250 ("deriserunt eum valde, moventes capita sua") and Raynaldus. Both hold.
- `quotationOriginals` (1): the modern wording matches the brief. The printed wording is verbatim at Palacký 15246–15249 ("dam-/natus" joined).
- `secondReading` ("minor"): filled in by the card writer from Outline_Check.md and not judged here. To be replaced by the blind second reading.
- Leaving `legacy.traces` "a sermon of probably 1408" in place is right. Workman and Pope give 1408, and Mladoňovice's "ante annos XII" (15243–15245) is a second dating, not a clear contradiction of a hedged "probably".
