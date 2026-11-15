# Era 6 council profiles: targeted check of the cap-ruling fixes

- **Date.** 2026-11-15.
- **Scope.** This checks only the strings changed for six R3_recheck.md findings. Constance: A3-M1 and A3-M2, under Mark's standing cap ruling of 2026-11-14 for minor round 3 fixes. Florence: B3-B1, B3-S1, B3-M1 and B3-M2, under Mark's cap ruling of 2026-11-15 ("Fix + one check (Recommended)"). It does not count toward the review cap (Mark's cap rulings, 2026-11-14 and 2026-11-15).
- **Files.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era6/council-of-constance-1414.entry.json`, `council-of-basel-ferrara-florence-1431.entry.json`, `records.json`. Branch `claude/cft-councils-era6`, `git diff e9378fc2^ HEAD` (commits `e9378fc2` and `63c71a89`).
- **Reviewer.** A fresh Opus reviewer at full effort, who did not see the drafting or the earlier rounds.
- **Method.** `git diff` was compared with `R3_changes.md` line by line. Each string was read in its file and against the vendored source lines in `cic/texts/` (grep and small `sed -n` ranges, several lines either side). Sentence lengths were counted by script. No model calls, no network, no paid services. Nothing was edited except this report.

Abbreviations as in R3_recheck.md: LUD = `ludolf_commentarius-ad-historiam-aethiopicam-lat_1691.txt`; LUDH = `ludolf_new-history-of-ethiopia_jp1682.txt`; TEL = `telles_travels-of-the-jesuits-in-ethiopia_1710.txt`; ALM = `almeida_historia-aethiopiae-liber-5-8-por_beccari1907.txt`; MEND = `mendes_expeditio-aethiopica-liber-1-2-lat_beccari1908.txt`; MANSI27 = `mansi_sacrorum-conciliorum-collectio-tomus-27-1409-1418-lat_welter-facsimile1902.txt`; CRESPIN1 = `crespin_histoire-des-martyrs-t1-fra_benoit-lelievre1885.txt`.

## Summary

| # | Finding | File and field | Verdict |
|---|---|---|---|
| 1 | A3-M1 | records.json, Constance, `absent_details` "The burning of Wyclif's bones as carried out" | CLEAR |
| 2 | A3-M2 | Constance entry, `decided[12]` | CLEAR |
| 3 | B3-B1 | Florence entry, `uncertain` "Who sent the Ethiopians" | CLEAR |
| 4 | B3-B1 | Florence entry, `record`, Ludolf item (witness and note) | CLEAR |
| 5 | B3-B1 | Florence entry, `sources.writtenLater`, two new items | CLEAR for Ludolf; one minor for Tellez (R4-M1) |
| 6 | B3-B1 | records.json, Florence, Ludolf Commentarius claim (rewritten) | CLEAR |
| 7 | B3-B1 | records.json, Florence, new Ludolf History claim | CLEAR |
| 8 | B3-B1 | records.json, Florence, new Tellez claim | CLEAR |
| 9 | B3-B1 | records.json, Florence, contested claim "Who sent the Ethiopian envoys", `sides` | CLEAR |
| 10 | B3-B1 | records.json, Florence, `absent_details` "An Ethiopian-side witness" | CLEAR |
| 11 | B3-S1 | records.json, Florence, Innocent X claim, `witness_kind` | CLEAR |
| 12 | B3-M1 | Florence entry, `uncertain`, "the patriarch of that day" | CLEAR |
| 13 | B3-M2 | Florence entry, `uncertain`, "names no sender" | CLEAR |

**Mechanics.** Every string is in the files exactly as `R3_changes.md` logs it. In the era 6 folder, only the three files changed (34 insertions, 10 deletions), and no other line in them changed. All three JSON files parse. The Florence records key holds 131 claims, 21 contested claims and 12 absent details, as logged. In the rewritten `uncertain` item, the longest sentence has 20 words. No changed entry sentence runs over 25 words. The one string over 25 words is the `record` witness label (26 words; see item 4).

## 1. A3-M1: CLEAR

- **Text.** "... That the burning was done is held only in later writers. Among them are Foxe, under the heading A.D. 1425 (...); Crespin's martyrology, which says he was dug up 'par le commandement du Pape' and his bones burned (crespin t1 l.19221-19225, 19965-19968); the 1916 editors of Luther's works ...; and van Braght's Martyrs Mirror ... No witness of the time is held."
- **Resolves.** "Among them are" no longer reads as a complete list, and Crespin is in it.
- **Sources.** CRESPIN1 l.19221-19225: "quarante & vn ans après sa mort, il fut déterré par le commandement du Pape, fes oz furent bruflez, & fes cendres iettees dedans l'eau". The quote "par le commandement du Pape" is verbatim (l.19222-19223, across a line break). CRESPIN1 l.19965-19968: "après la mort de Hus, par fentence dudit Concile, les os de Wicleff furent déterrez & bruflez". The file header gives Crespin (d. 1572) with the 1619 continuations, so he is a later writer and the main claim holds.
- **Noted, no finding.** The 1619 text holds continuations by other hands. "Crespin's martyrology" names the work as it is known, not the hand of each passage, so it claims nothing false.

## 2. A3-M2: CLEAR

- **Text.** "At the last session, the acts say, the words 'Lords, go in peace' came after the Mass and the litanies." (20 words.)
- **Source.** MANSI27 l.129231-129233: "Adiffam de Spiritu fankto devotiffime celebravit. Qua finita, @ litanris cum folitis orationibas finitis O peraltis". It leaves out "the usual prayers", but nothing in it now claims that nothing came between. Clear and faithful.

## 3. B3-B1, entry `uncertain`: CLEAR

- **Text.** "Ludolf's History, in its English of 1682, says no doubt is made of the embassy Zara Yaqob sent in 1439. The Jesuit history of Tellez, in English, also says Zara Yaqob sent Ethiopians to Eugenius. In his Commentarius of 1691, Ludolf denies that Zara Yaqob joined Rome at the council. The Jesuits themselves, he says, show the king stood apart from the Roman church." (20, 15, 15 and 14 words.)
- **Ludolf's History (required check 1).** LUDH l.19484-19496 was read in context, from l.19440. Ludolf is speaking in his own voice in Book III ("The HISTORY of Book III", running head l.19466). He goes through the reputed Ethiopian embassies to the popes. He doubts the letter of Alexander III (l.19470-19488) and gives the Avignon embassy only as what "Others there are, that believe" (l.19489-19491). Then, at l.19491-19496: "Nor-is there any doubr made of the Embassy | Which Zera-Jacob sent: ro Eugenius the Fourth, in the. year 1439. toward the. Conclusion" of the: Council of Florence. Gregory had known nothing of ir, had he not seenthe Embasl- sador and his Retinue painted at Rome, and known his own Councrymen by their Habic." The sentence is Ludolf's, set against the doubtful items before it. "Says no doubt is made of the embassy Zara Yaqob sent in 1439" renders it closely. The header confirms the translation is "Made English by J. P." of London 1682, so "in its English of 1682" is right.
- **Ludolf's Commentarius (required check 2).** LUD l.52403-52444 was read in context, from l.52385. Section XCVII, "De Legationibus Aethiopum ad Pontificem Romanum" (l.52403), opens with what Catholic writers say: that the king's envoys came to Clement V and, "finito concilio", to Eugenius IV at Florence (l.52405-52408). Next comes Miraeus, who "Zera-Iacobo attribuit" a confession and "corrumpit & adulterat" it to look Catholic (l.52410-52414). After a back-reference, l.52432-52435 reads: "Nihil autem tale in Concilio Florentino actum, sed potius Zera-Jacobum ab Ecclesia Romana alienum fuisse, testantur ipsi Patres Societatis". The Jesuits' witness is Susenyos's curse on "el Rey Zera-Jacob", who "made us today be outside the faith" (l.52437-52440). Then: "Ita Susneus Zera-Jacobum manifeste schismatis autorem facit" (l.52442). And: "Post illa tempora nulla Aethiopica legatio Romam venit" (l.52444), which grants the earlier embassies. So what "tale" denies is a Catholic act or profession by the king at the council. "Sed potius" sets it against his standing apart from Rome. Read this way, "denies that Zara Yaqob joined Rome at the council" is a fair plain rendering of the passage. It neither denies the embassy nor overstates the passage.
- **Tellez (required check 4).** TEL l.6271-6302: "till Zar[a Jac]ob, who Govern'd about 1437 ... In the Days of this Zara Facob the Florentine Councel was held ... and this was he that desir'd to reduce his Empire to the Catholick Faith, and in order to it writ [OCR gap] ... and sent some of his Abyssinians to Pope Eugenius the 4th, who then govern'd the Church, and answer'd him in a Letter". The narrator is the Jesuit compiler, and "sent ... Abyssinians to Pope Eugenius the 4th" is on l.6295. "Also says Zara Yaqob sent Ethiopians to Eugenius" holds. The OCR loses a few words after "writ", but the claim does not depend on them.
- **Writing (required check 7).** Each witness keeps its own sentence. "He" in the last sentence is Ludolf, named in the sentence before. "The king" is Zara Yaqob, named in the same sentence pair. "Themselves" is Ludolf's own point ("ipsi Patres Societatis"). It also sits fairly beside Tellez, a Jesuit who reports the embassy. There is no empty contrast, no filler and no summing-up line. Beccari's verdict stays attributed to him. The phrase "no doubt is made of" keeps the History's English and reads clearly aloud.

## 4. B3-B1, entry `record`, Ludolf item: CLEAR

- **Witness.** "Hiob Ludolf, Commentarius ad Historiam Aethiopicam (1691) and his History in English (1682), with a Latin version of the oration of the Portuguese patriarch Alphonsus Mendez" (26 words).
- **The 25-word rule (required check 5).** This is a label, not a sentence. It has no verb and no full stop. It names two works and a text printed in one of them, like the other `record` labels in era 6 (the next longest are 24 and 21 words). Cutting it would mean dropping a title or the date. The sentence rule does not apply to it, so it is not a finding. Its sense is clear when it is read as a list.
- **Accuracy.** The titles and dates match the two file headers: LUD "Frankfurt am Main ... 1691"; LUDH "London ... 1682", "Made English by J. P. Gent.". "A Latin version of the oration" is in the Commentarius (LUD l.57414-57425, "Venerunt ab Imperatore & metropolita vestro Oratores ad concilium Florentinum"). The R3 recheck confirmed the source of that version (LUD l.56873-56877). The note's "in his Latin" places it.
- **Note.** "Ludolf takes the embassy of 1439 as Zara Yaqob's, but says the king stood apart from the Roman church. The oration, in his Latin, says the emperor and the metropolitan sent the envoys." (19 and 14 words.) The first sentence joins LUDH l.19491-19494 and LUD l.52432-52442 and is true of both. The "but" marks a real difference: the embassy is granted, and the king's union with Rome is denied. It is not an empty contrast. The second sentence is unchanged in substance and matches LUD l.57420.
- **Kind.** `later narrative` fits both works by the pattern's definition (`Council_Profile_Pattern.md` l.18).

## 5. B3-B1, entry `sources.writtenLater`: Ludolf CLEAR; Tellez one minor (R4-M1)

- **Ludolf.** {"A New History of Ethiopia", "Hiob Ludolf, made English by J. P.", English, LUDH}. It matches the header's title and creator lines.
- **Tellez (required check 3).**
  - *The title page.* TEL l.100-101 (OCR): "The whale [whole] ... by F. Balthazar Teller [Tellez], [of] the Society of JES[U]S; and now first Translated into Euglist [English]". The header gives the title as "collected and historically digested by F. Balthazar Tellez". The title page credits Tellez alone and names no translator. So "Balthazar Tellez (the title page's attribution ...)" and "English translation anonymous" are right.
  - *The preface.* TEL l.165-177 says the work is "methodically digested by a Learned Jesuit employ'd in it by his Society". It names its sources: "The [first] of them is F. Peter Paiz ... [the second] is F. Emanuel d'Almeyda ... Thirdly, The Patriarch Don Alfonso Mendez". So the book itself names Almeida as a source, not as its author.
  - *The header.* TEL l.2: "Balthazar Tellez (the title page's attribution; the host's sister item and its description credit the underlying work to Manuel de Almeida)". The ALM header (l.9) adds a Library note: "Tellez 1710 (vendored) is an English abridgement of the same Jesuit history". MEND l.2188-2191 (Beccari) calls Tellez's history "vel potius synopsim Historiae" of the Patriarch's, which concerns Mendez, not Almeida.
  - *Conclusion.* "The work is credited to Manuel de Almeida" is supported only by the Library header's report of the host's catalogue for a sister scan. The title page does not support it, and neither does any text in the file. The label also drops "underlying", and its passive gives no one who does the crediting. It reads as if an authority credits the English book to Almeida against its own title page. That is more than the held evidence shows. The underlying point, that the Tellez history draws on Almeida, is true and is in the preface. So this is a wording and citation slip, not a false attribution.
- **R4-M1. Minor (an unattributed credit, resting only on a catalogue note).**
  - **Text.** `sources.writtenLater`, Tellez item, `author`: "Balthazar Tellez (the title page's attribution; the work is credited to Manuel de Almeida), English translation anonymous".
  - **Evidence.** TEL l.100-101 (title page: Tellez only); TEL l.165-177 (preface: Almeida is the second of the compiler's named sources); TEL l.2 (header: "the host's sister item and its description credit the underlying work to Manuel de Almeida").
  - **Fix.** Replace the `author` value with: "Balthazar Tellez, as the title page gives it (its preface names Manuel de Almeida among his sources), English translation anonymous". No other text changes.

## 6. B3-B1, records, Ludolf Commentarius claim: CLEAR

- **Text.** "Ludolf's Commentarius denies that Zara Yaqob joined Rome at the council of Florence. The Jesuit fathers themselves, he says, show the king stood apart from the Roman church". Witness LUD l.52403-52413; LUD l.52431-52444. `later narrative`, Contested.
- **Source.** As in item 3. The first range now covers Miraeus's attribution (l.52410-52414; "corrumpit & adulterat" stands on l.52414). The second range now runs to l.52444 ("Post illa tempora nulla Aethiopica legatio Romam venit"). "The Jesuit fathers themselves" renders "ipsi Patres Societatis". "Show" for "testantur" is fair.

## 7. B3-B1, records, new Ludolf History claim: CLEAR

- **Text.** "Ludolf's History, in its English of 1682, says no doubt is made of the embassy Zara Yaqob sent to Eugenius IV in 1439, toward the end of the council. The Ethiopian Gregory, it says, knew of it only from a painting at Rome". LUDH l.19489-19496. `later narrative`, Contested.
- **Source.** As in item 3. "Toward the end of the council" renders "toward the Conclusion of the Council of Florence". "Knew of it only from a painting at Rome" renders "Gregory had known nothing of it, had he not seen the Embassador and his Retinue painted at Rome". That is fair. "The Ethiopian Gregory" is supported by "known his own Countrymen by their Habit" (l.19495-19496) and by the header ("Gregorius the Ethiopian"). The range starts two lines early, at "Others there are", which does no harm.
- **Noted, no finding.** The first sentence runs 29 words. Records claims are record data, not reader-facing sentences. R3_changes.md applied the length check to the entry only, as era 5 did.

## 8. B3-B1, records, new Tellez claim: CLEAR

- **Text.** "Tellez's Jesuit history, in English, says Zara Yaqob wished to bring his empire to the Catholic faith and sent some of his Abyssinians to Eugenius IV". TEL l.6272-6295. `later narrative`, Contested.
- **Source.** As in item 3: "desir'd to reduce his Empire to the Catholick Faith ... and sent some of his Abyssinians to Pope Eugenius the 4th" (l.6275-6295). "Wished to bring" for "desir'd to reduce" is the right modern sense. The range ends on the line that holds the sending.

## 9. B3-B1, contested claim "Who sent the Ethiopian envoys": CLEAR

- **Added sides.** "Zara Yaqob, in 1439, toward the council's end, beyond doubt: Ludolf's History, English of 1682 (LUDH l.19489-19496). Zara Yaqob: Tellez, in English (TEL l.6272-6295)." "Beyond doubt" renders "Nor is there any doubt made" (it reports Ludolf's own certainty). Both sides fit the question asked.
- **Ludolf side.** "Zara Yaqob did not join Rome at the council and stood apart from it: Ludolf's Commentarius (LUD l.52403-52413; LUD l.52431-52444)." It no longer answers "who sent", and it no longer reads as a denial of the embassy. That is right: in the Commentarius, Ludolf does not deny the sending. "It" is Rome. The other sides, with their ranges, are unchanged.

## 10. B3-B1, `absent_details` "An Ethiopian-side witness": CLEAR

- **Text.** "Ludolf's Commentarius (1691) and his History in English (1682) were read in context. So were Tellez, Almeida and Mendez, with Beccari's introduction and Innocent X's brief. None is an Ethiopian text of the time." (13, 13 and 8 words.)
- **Check.** All five texts are Western works of the 17th to 20th centuries. Ludolf drew on Gregory, but the History is Ludolf's. The R3 recheck's search found no held Ethiopian text of the time that names Florence, so the absence holds.

## 11. B3-S1, Innocent X claim, `witness_kind`: CLEAR

- **Change.** `acts` became `later narrative`. The text, witness and confidence are unchanged.
- **Pattern (required check 6).** `Council_Profile_Pattern.md` l.16 keeps `acts` for "the council's own minutes, canons, creed, decree, synodal letter or subscription list". l.18 defines `later narrative` as "a history written afterwards, with its writer named and, where a held source gives it, when". A papal brief of 30 October 1645 (MEND l.1450-1451, "die xxx octobris mdcxxxxv") that recounts 1438-1439 is a later teller. Of the pattern's four kinds, `later narrative` is the only one that fits it. The three new claims (Ludolf's Commentarius, Ludolf's History, Tellez) are `later narrative` too, and that is right for each. None of them is an editor supplying a date or count that no old witness gives, which is what `modern reconstruction` means (l.19).

## 12. B3-M1: CLEAR

- **Text.** "In Almeida's Portuguese of it, the emperor and the patriarch of that day sent them." (15 words.)
- **Source.** ALM l.28464-28466: "ao concilio Florentino forão mandados embaixadores pelo Emperador e Patriarcha, e trouxerão cartas do papa Eugenio quarto ao emperador Zara Jacob". The patriarch here is the one who sent envoys to Florence, so "of that day" is right. "The patriarch" no longer reads as Mendez, the "Catholic patriarch" of the sentence before.

## 13. B3-M2: CLEAR

- **Text.** "Almeida's history names no sender: some Ethiopians, it says, came with the Armenians as the council ended." (17 words.)
- **Source.** ALM l.7658-7680: "no tempo do papa Eugenio 4° ... como refere o cardeal Baronio, e o dizem muitos autores gravissimos, no fim do tal concilio chegarão ali com os Armenios alguns Ethiopes ou Abexins". No sender is named, and "as the council ended" renders "no fim do tal concilio".
- **Noted, no finding.** Almeida gives the arrival on Baronius's authority and that of "many weighty authors". The entry's "it says" is still true: the history says it. The records claim behind it (records.json l.1534, "Almeida says, after Baronius and other authors") carries the chain in full.

## Result

Every finding is resolved: A3-M1, A3-M2, B3-B1, B3-S1, B3-M1 and B3-M2 are CLEAR. Ludolf's stance is now told the right way round in the entry, the `record` item, the records claim and the contested claim's sides. His History grants Zara Yaqob's embassy of 1439. His Commentarius denies a Catholic union by the king at the council, not the embassy. There are no blocking or substantial findings.

One minor remains, R4-M1, in the new Tellez sources item. "The work is credited to Manuel de Almeida" rests only on the Library header's report of the host's catalogue for a sister scan. The title page credits Tellez alone, and the preface names Almeida as a source. The fix is to set the `author` value to "Balthazar Tellez, as the title page gives it (its preface names Manuel de Almeida among his sources), English translation anonymous".

This check does not count toward the review cap (Mark's cap rulings, 2026-11-14 and 2026-11-15).

## Counts

Blocking 0. Substantial 0. Minor 1 (R4-M1). Strings checked: 13 (Constance 2, Florence 11). Findings resolved: 6 of 6.
