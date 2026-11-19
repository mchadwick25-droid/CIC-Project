# Batch 6: card checks and originals ruling, as applied

Applied 2026-11-19 under `Card_Apply_Prompt.md`. Each FIX is applied word for word from the folder's `Card_Check.md`, as amended by `Batch_Originals_Ruling.md` and the coordinator's two calls. Where a change replaces part of a longer string, only the changed part is shown. Every card keeps its key order and its own JSON layout. Readings go into `tools/quote_scan_readings.json`; 18 were added (53 to 71), none of them a duplicate. Each scan string was confirmed at its file and lines, and each `lines_held` line was confirmed in its range.

## bardaisan-of-edessa

- `bardaisan-of-edessa.card.json`, `briefReferences[11]` (FIX 1): "…On Fate the most famous and strongest of his books, and its force even in translation." → "…On Fate the strongest of his books."
- Readings: none.

## hermas

- `briefReferences[2]` (FIX 1): "the tower built on the water," → "the tower,".
- `briefReferences[9]` (FIX 2): "written very recently, while his brother Pius was bishop of Rome;" → "written very recently;".
- `briefReferences[12]` (FIX 3): "read publicly in some churches of Greece, almost unknown among the Latins." → "almost unknown among the Latins."
- `quotationOriginals[4].printed` (FIX 4, ruling KEEP): "( for. sed publieari)" → "( for. sed publicari)".
- `quotationOriginals[4].uncertain` (FIX 4): "…the editors' correction \"sed publicari\", which this scan prints as \"publieari\". …" → "…the editors' correction \"sed publicari\". …".
- `quotationOriginals[5]` (FIX 5, ruling KEEP): added after `lines`: `original` "illo apocrypho Pastore moechorum", `originalFile` `cic/texts/tertullian_quae-supersunt-t1-apologetica-lat_oehler1853.txt`, `originalLines` "74596-74597". The ruling's alternative (citing Reifferscheid-Wissowa) was not taken.
- `sources.about`, added at the end: Tertullian, "On Modesty, chapter 20, in Latin (ed. Franz Oehler)", 1853, Latin, the Oehler t1 file.
- Readings added: Routh 22082 "sed publieari)" → "sed publicari)"; Oehler t1 74597 "moecbomm" → "moechorum".

## hippolytus-of-rome

- `briefReferences[5]` (FIX 1): "McGiffert and Harnack: he probably died on the island." → "McGiffert: he probably died on the island; Harnack: there or soon after at Rome."
- `quotationOriginals[6].printed` (FIX 2, ruling KEEP): "Hippolytus fertur premerent cum iussa tyranni presbyter in scisma semper mansisse Novati." → "Hippolytus fertur PREMERENT CuM IVSSA Tyranni presbyter in scisma SEMPER MANSISSE Novati."
- `quotationOriginals[7].printed` (ruling, "with the page's case"): "Haec audita refert Damasus, probat omnia Christus." → "Haec audita rEFERT DAMasus, probat omnia Christus."
- Readings added: Duchesne 109160 "scismk" → "scisma"; Duchesne 109160 "XOvali" → "Novati".

## ignatius-of-antioch

- `quotationOriginals[2]` (FIX 1): removed `original`, `originalFile` and `originalLines` (the Horologion Greek at 15547-15552).
- `quotationOriginals[2].work` (FIX 1): "…Ante-Nicene Fathers vol. 1; Greek as the Great Horologion (Venice, 1851) prints it from Eusebius" → "…Ante-Nicene Fathers vol. 1".
- `briefReferences[4]` (FIX 2): "the bishop presiding in the place of God, with the elders and the deacons; one prayer and one altar;" → "the bishop, with the elders and the deacons; one altar;".
- `briefReferences[14]` (FIX 3): "fifteen letters under his name, eight set aside as forgeries, the seven in a shorter and a longer Greek form, and the long dispute over them." → "fifteen letters under his name, and the long dispute over them."
- `briefReferences[15]` (FIX 4): "sail from Troas to Neapolis," → "sail from Troas,".
- `ignatius-of-antioch.brief.txt` (ruling, Part 2): "…asked for news of \"the blessed Ignatius\"." → "…held up \"the blessed Ignatius\" as a model of patience. He also asked for any news of him."
- Card after the brief change: no edit needed. The brief still quotes the same five spans, and `quotationOriginals[3]` ("the blessed Ignatius", Phil. 9, ANF 3487) still matches. `briefReferences[10]` already names Phil. 9's patience and Phil. 13's request for news.
- `python -m engine.m1.profile_readability`: pass (grade 6.2, reading ease 82.4; the tool notes the grade is under 8, for the listener read).
- Readings: none.

## irenaeus-of-lyon

- `datesNote` (FIX 1): "Eusebius's Chronicle sets it beside 167, and McGiffert argues for 177." → "Eusebius's Chronicle places it after 167, grouped with Polycarp's martyrdom, and McGiffert holds that the grouping does not date it."
- `uncertain[0]` (FIX 2): "No held line says where or when he was born." → "No early source says where or when he was born."
- `uncertain[2]` (FIX 3): "The year 177 and the martyrs' letter. The letter of the Christians of Vienne and Lyon says the imprisoned martyrs asked him to carry it to Eleutherius at Rome. It does not say he saw them die. Valesius thought he wrote it, and Coxe thinks so too;" → "The year 177 and the martyrs' letters. In their letter to Eleutherius at Rome, which Eusebius quotes, the imprisoned martyrs asked him to carry it. Their letter to the churches of Asia and Phrygia does not say he saw them die. Valesius thought he wrote that letter, and Coxe thinks so too;"
- `briefReferences[1]` (FIX 4): "their claim that the truth came down by word of mouth and that they are wiser than the apostles." → "their claim that they are wiser than the apostles."
- `briefReferences[2]` (FIX 5): "five books, written under Eleutherius, about 180." → "five books, about 180."
- `briefReferences[3]` (FIX 6): "the letters sent from prison to Eleutherius at Rome," → "the letters sent from prison to Rome,".
- `irenaeus-of-lyon.brief.txt`, paragraph 17 (FIX 7, first way): "…sat as he taught. And I can tell how…" → "…sat as he taught.\" He could describe, he wrote, how Polycarp came and went, how he lived and looked, and his talks to the people. \"And I can tell how…".
- `uncertain[8]` (FIX 7): "and leave out the middle of his sentence, on Polycarp's comings and goings, his way of life, his looks and his talks to the people." → "and the middle of his sentence, on Polycarp's comings and goings, his way of life, his looks and his talks to the people, is told in the narrator's words."
- `briefReferences[8]` (FIX 7): "the place where Polycarp sat, and his intercourse with John." → "the place where Polycarp sat, his goings out and comings in, his manner of life, his appearance and his discourses to the people, and his intercourse with John."
- `quotationOriginals[3].modern` unchanged, as FIX 7 says.
- `quotationOriginals[0]` (ruling LEAVE OUT): `printed` Holl's Greek (31907-31911) → the ANF English "just as if one, when a beautiful image of a king has been constructed by some skilful artist out of precious jewels, …"; `file` Holl → `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml`; `lines` "31907-31911" → "30994-30998"; `englishPrinted`, `englishFile`, `englishLines` removed.
- `quotationOriginals[1]` (ruling LEAVE OUT): `printed` Holl's Greek (32715-32719) → the ANF English "As I have already observed, the Church, having received this preaching and this faith, …"; `file` Holl → anf01; `lines` "32715-32719" → "31419-31425"; `englishPrinted`, `englishFile`, `englishLines` removed.
- `python -m engine.m1.profile_readability`: pass (grade 8.1, reading ease 75.1).
- Readings: none (the check listed none, and the Greek is left out).

## josephus

- `briefReferences[2]` (FIX 1): "both sides' charge of \"treachery\"," → "the Jews' wish to punish him and the Romans' charge of \"treachery\",".
- `quotationOriginals[6]` (ruling LEAVE OUT): `printed` Origen's Greek → "And the wonderful thing is, that, though he did not accept Jesus as Christ, he yet gave testimony that the righteousness of James was so great"; `file` Lommatzsch → `cic/texts/anf09_gospel-of-peter-diatessaron-origen-commentaries.xml`; `lines` "3731-3733" → "30627-30629"; `englishPrinted`, `englishFile`, `englishLines` removed.
- Readings added: Whiston 81406 "hima" → "him a". The four Lommatzsch readings (3731, 3731-3732, 3732-3733, 3733) were not added, because the ruling leaves that Greek out.

## pliny-the-younger

- `briefReferences[1]` (FIX 1): "a man of letters and a friend of Trajan," → "a man of letters,".
- `quotationOriginals[0]` (FIX 2, ruling KEEP): added after `lines`: `original` "Confitentes iterum ac tertio interrogavi, supplicium minatus; perseverantes duci iussi. Neque enim dubitabam, qualecumque esset quod faterentur, pertinaciam certe et inflexibilem obstinationem debere puniri.", `originalFile` Mirbt, `originalLines` "2777-2779".
- `quotationOriginals[1]` (FIX 3, ruling KEEP): added after `lines`: `original` "Conquirendi non sunt: si deferantur et arguantur, puniendi sunt", `originalFile` Mirbt, `originalLines` "2811-2816".
- `quotationOriginals[3]` (FIX 4, kept by the ruling and the coordinator): added after `lines`: `original` "O sententiam necessitate confusam!", `originalFile` Oehler t1, `originalLines` "11728".
- Readings added: Mirbt 2777 "minatus ;  15" → "minatus ;"; Mirbt 2814 running head, dropped, with its `lines_held`; Mirbt 2816 "argiiantur" → "arguantur"; Oehler t1 11728 "0  sententiam" → "O  sententiam".

## polycarp-of-smyrna

- `quotationOriginals[0]`, `[1]`, `[3]`, `[4]`, `[5]` (ruling LEAVE OUT; FIX 1.1 to 1.5 not applied): removed `original`, `originalFile` and `originalLines`. `[2]` and `[6]` keep their Greek as it stands. Gebhardt stays in `sources`.
- `briefReferences[3]` (FIX 2): "the crowd's cry, after Germanicus's death, that Polycarp be sought out." → "the crowd's cry that Polycarp be sought out."
- Readings: none. The check's six Gebhardt readings were not added, per the ruling.

## polycrates-of-ephesus

- PASS. No changes and no readings.

## suetonius

- `briefReferences[1]` (FIX 1): "these acts are some beyond criticism, some deserving of praise." → "these acts are some beyond criticism."
- `quotationOriginals[2].englishPrinted` (FIX 2): "the Christians, a class of men given to a new and mischievous superstition." → "Punishment was inflicted on the Christians, a class of men given to a new and mischievous superstition."
- `quotationOriginals[2].englishLines` (FIX 2): "28524-28525" → "28523-28525".
- `quotationOriginals[5]` (FIX 3): not applied. The ruling leaves the Tertullian Latin out, and the card's English stands alone.
- Readings added: Rolfe 28523 "inflicted a" → "inflicted on". The three Oehler t1 readings (12454, 12455, 12456) were not added, per the ruling.

## tacitus

- PASS. No changes and no readings.

## tatian

- `briefReferences[9]` (FIX 1): "from Rome to the East and a school in Mesopotamia;" → "from Rome to the East, to Mesopotamia;".
- `quotationOriginals[0].original` (FIX 2, ruling KEEP): "…τῇ Ρωμαίων μεγαλαυχία καὶ τῇ Adıwalov ψυχρολογίᾳ, … τῆς δκαϑ᾽ ἡμᾶς…" → "…τῇ Ῥωμαίων μεγαλαυχίᾳ καὶ τῇ Ἀθηναίων ψυχρολογίᾳ, … τῆς καϑ᾽ ἡμᾶς…".
- `quotationOriginals[3].original` (FIX 3, ruling KEEP): "…καὶ τίς Δ ἡ κατ᾽ αὐτὸν… μενούσης μοι δ τῆς…" → "…καὶ τίς ἡ κατ᾽ αὐτὸν… μενούσης μοι τῆς…".
- `quotationOriginals[2].printed` (ruling LEAVE OUT; coordinator: no Latin in its place; FIX 4 not applied): removed. Old value: "Evgov δὲ κἀγὼ πλείους ἢ διακοσίας βίβλους …".
- Readings added: Otto 1851 12199 (Ῥωμαίων … Ἀθηναίων), 12200 (τῆς καϑ᾽ ἡμᾶς), 14239 (τίς ἡ) and 14241 (τῆς). The Otto 1872 14984 "Evgov" reading was not added.

## valentinus

- `briefReferences[5]` (FIX 1): "the Father alone and all love, and the first pair." → "the Father alone and all love."
- `quotationOriginals[1].uncertain` (FIX 2): "The modern English is rendered from the Latin, which Kroymann prints across a page break, at lines 9633-9634 and 9652-9653: sperauerat … abrupit (the scan reads Yalentinus and aliura). …" → "The modern English is rendered from Kroymann's Latin. …".
- `quotationOriginals[1]` (FIX 2, ruling KEEP): added after `uncertain`: `original` "sperauerat episcopatum Valentinus, quia et ingenio poterat et eloquio, sed alium ex martyrii praerogatiua loci potitum indignatus de ecclesia authenticae regulae abrupit", `originalFile` `cic/texts/tertullian_opera-pars3-lat_kroymann-csel47.txt`, `originalLines` "9633-9653".
- Readings added: Kroymann 9633 "episco-  25" → "episco-"; 9634 "Yalentinus" → "Valentinus"; 9635-9651 dropped, with its ten `lines_held`; 9652 "aliura" → "alium".

## Not applied, with the reason

1. **Tatian `quotationOriginals[2]` now has no `printed` wording.** The brief still quotes the span ("I myself found more than two hundred such books…"). The coordinator ruled that the Greek is left out and no Latin goes in its place. The ruling's other option is to take the quotation marks off the brief's span, but this prompt does not give that edit. Until the coordinator decides, the card fails the census quotation check. Its `work`, `file` and `lines` still name Theodoret's Greek in Otto 1872 at 14984-14987.
2. **The `work` labels after the Greek is left out.** Irenaeus `[0]` and `[1]` still say "Greek as Epiphanius copies it, Panarion 31, ed. Karl Holl", and Josephus `[6]` still says "ed. Lommatzsch", but `printed` is now the ANF English. The ruling gives no new label, so these were left unchanged. Polycarp's `work` strings still say "Greek ed. Oscar von Gebhardt", which the ruling allows, since Gebhardt stays in `sources`.
3. **The "sources that differ" `uncertain` notes.** The ruling describes what each note should say but gives no wording to copy. So none was added. Where things stand:
   - Polycarp (item 1): the existing card `uncertain[10]` already says the rendering follows the Greek, and gives ANF's "my King and my Saviour", "anniversary" and "finished their course".
   - Irenaeus (item 3): `uncertain[8]` already says "The brief's small stones follow the Greek; the English made from the Latin has precious jewels."
   - Josephus (item 2): no note on the card says that "our Jesus" follows Origen's Greek where ANF has no "our". This one is open.
   - Items 4 and 5 need nothing.
4. **The Irenaeus check's suggested OCR notes** for the Greek entries are not a FIX. They are moot now that the Greek is left out.
