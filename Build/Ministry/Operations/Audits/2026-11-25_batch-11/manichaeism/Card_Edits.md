# Card edits: Manichaeism (`manichaeism`, tradition)

Card: `manichaeism.card.json`. A tradition has no `card` field, so the card file holds the census entry's card fields, as `Card.existing.json` does, in the same order. `why`, `floorNote`, `relationsSummary` and `teaser` are left word for word in the card file; their changes are listed under **Entry fields** for release. Every other field not listed here is word for word from `Card.existing.json`. Four new keys follow at the end: `sources`, `uncertain`, `briefReferences`, `quotationOriginals`.

**Format note.** `tools/validate-census.mjs` sets key lists only for a person's `card` and a council, and checks a tradition's quotations nowhere. So `sources` uses the census's tradition form (`work`, `type`, `note`), with `file` added, and `quotationOriginals` uses the person-card keys, as the sibling cards of this batch do. Checked: a scratch census copy outside the repository, with the card's fields at the top of the entry, the brief as `longDescription` and the `modernWorks` below, gives 0 errors and the same 4 warnings as the live census (`node tools/validate-census.mjs --skip-quotes <copy>`; the full run was killed for memory in this container, and it checks no tradition quotation in any case). I re-read each `printed` and `original` at its lines with the validator's fold rule and its four ways of reading a segment, and each `modern` against the brief's six quoted spans: all hold. The card's new prose puts no double quotation marks around anything.

## Clearly wrong (card fields)

1. `voices[0]` (Mani).
   - Old: "and died in a Persian prison"
   - New: "and died at a Persian king's hands"
   - Evidence: the brief, "Bahram had him killed, but the accounts differ on how", with prison as one account only ("chained in prison until he died"). Source Sheet B10: the death at the Persian king's hands is Documented (all agree); the manner is Contested (BIR 29125-29127 flayed; 29132-29138 prison; FIH 5112-5128 hung in two halves, "others" prison). Outline Do not say: the manner is not told as fact.

## New (card fields)

2. `legacy`: a new last paragraph, from outline What came of it 2 and 4 and Leave out (Samarkand and Baghdad, B27, B28; Leo of Rome; Ephrem), all marked card, and Cut first 5 (Biruni about 1000, card).
   - "The old record also shows how long they lasted in the East. In the 900s, the Fihrist says, some five hundred of them gathered at Samarkand. When the ruler of Khorasan wished to kill them, the ruler of China, as the Fihrist calls him, swore that he would kill all the Muslims in his own lands if one of them were killed, and they were left alone and taxed. The Fihrist's author had known about three hundred of them in Baghdad, but in his own day barely five were left there. About the year 1000 Biruni wrote that most of the eastern Turks, and many of the people of China and Tibet, still held Mani's law. In the West their opponents went on answering and hunting them: Ephrem the Syrian wrote against Mani in Syriac, and at Rome in 443 Bishop Leo had many of them found where they hid in the city, exposed before the whole church, and their books burned."
   - Evidence: FIH 5406-5431 (Samarkand, the "Beherrscher China's", the tax; Baghdad's three hundred and five); BIR 29140-29147; Ephrem, Prose Refutations, `ephraim_prose-refutations_mitchell1912-1921.txt` 640 ("we have opposed Mani also with a true refutation"; the census edge `syriac-edessa-nisibis--manichaeism`); Prosper, `prosper_chronica-minora-1-lat_mommsen1892.txt` 54712-54717 (a. 443: "plurimos Manicheos intra urbem latere ... oculis totius ecclesiae publicatos ... incensis eorum codicibus").
3. `documentedStories[0].sources`: the BeDuhn item, a modern work, is removed here and moves to the story's `modernWorks` (edit 11).
4. `sources` (new): twelve old works, each with its file, the files the brief and the card draw on (Source Sheet, Files). Titles and translators are from the file headers and NPNF 1/4's contents (lines 586-640: Fortunatus tr. Newman; Fundamental and Faustus tr. Stothert; Morals of the Manichaeans tr. Stothert). Migne PL 42 (CFo, CEF, CFa Latin); NPNF 1/4 (the same in English, and DMM); Knöll's Confessions; Pilkington's Confessions; Biruni (Sachau); the Fihrist (Flügel); the Theodosian Code (Mommsen-Meyer); the Khuastuanift (Le Coq); the Chinese texts (Chavannes and Pelliot); Alexander of Lycopolis and the Acts of Archelaus (ANF 6); Prosper (Mommsen); Ephrem's Prose Refutations (Mitchell).
5. `uncertain` (new), the disputes the outline and reviews send to the card:
   - a. Who ruled at Mani's birth: Review fix 3 and Do not say (BIR 29094-29100, 12375-12376; Source Sheet A1).
   - b. Twelve or thirteen: Source Sheet G (FIH 4391; BIR 29098-29099). The call itself is Cut first 27, card.
   - c. Shapur's welcome or banishment: Cut first 3, card "with its dispute" (FIH 4449-4462; BIR 29161-29171). The two lamps of light: Leave out, "Card" (FIH 4449-4451).
   - d. Mani's wonders: Leave out, "Card" (BIR 29149-29159).
   - e. Which king and how: Cut first 29, card "with its dispute" (ALX 24496-24498), with BIR 29125-29138, FIH 5112-5128 and ARC (Source Sheet B10). The Acts are named as a staged debate (Leave out: "Card, flagged as legend, or nowhere"); its life of Mani as a slave boy is left off.
   - f. Augustine's charges and the fig: Leave out, "Card, in full" (DMM, `npnf104` 2743; CONF III.10, `npnf101` 6163-6174).
   - g. The deaths of 843: the number 70 or 72 (Source Sheet B26; CHI 14094, 14114).
6. `briefReferences` (new): eight lines, one for each run of the brief, with the lines it draws on. The cut details the outline sends to the card are carried in them at their lines: the Baths of Sossius, before the people (Cut first 17; Migne 7609-7611); the Chinese rule for entering the religion (Leave out, card; CHI 4928-4933); Mardinu and Kutha, and the land between the Tigris and the Euphrates (Cut first 25); the baptizers, at-Taum the Companion, the call at twelve and at twenty-four (Cut first 8, 26, 27; FIH 4362-4372, 4390-4404); the gospel and the other books, and seven books, six in Syriac and one in Persian (Cut first 13, 15; BIR 29112-29115; FIH 5243-5244); the Fihrist's rule for whoever cannot tame desire (Cut first 9; FIH 4881-4898); four or seven prayers turned to the great light (Cut first 11, 22; FIH 4936-4940); the three seals (Do not say, card; DMM 2438-2439); the yearly fast (Leave out, card; KHU 17106-17125); the Bema's five steps and cloth, and Easter kept with little care (Cut first 6, 18; Migne 12871-12904); the river of Balkh (Cut first 12; FIH 5385-5396); Papus and Thomas (Cut first 1; ALX 24494-24496); the 399 law (Cut first 4; CTh 87272-87278); Carthage (Cut first 24; Knöll 7333-7336); the Old Testament question (Cut first 32; CFa 4471); "and some others" and the decree that freed them (Cut first 23, 28; CFa 4615-4616, Migne 16828-16840); the khagan's four teachers and the inscription (Cut first 10, 21; CHI 8671-8673, 8750-8751); the decrees of 768 and 771 (Cut first 2; CHI 12205-12208, 12230-12233); the 806 notice (Leave out, card; CHI 12381-12387); "across the empire" (Cut first 28; CHI 14093-14094); "of Buddhist books", "in China's far west", the explorer of 1907 and the scroll's length (Cut first 16, 19, 28; KHU 15395-15417, 15429-15433).
7. `quotationOriginals` (new): one entry for each of the brief's six quoted spans, each `modern` copied exactly from the brief.
   - "You were at our prayer.": `printed` Migne's Latin, 7666-7667, "Interfuisti orationi" (the scan breaks it "ora- / tioni"). Newman's English leaves the clause out (3230-3232), so the Latin is the printed wording and no English is given. Five words: `secondReading` "checked at card".
   - "to the Bad Place.": `printed` Le Coq, KHU 17443, "go to the Bad Place." Four words: "checked at card".
   - "angels and gods": `printed` Pilkington, `npnf101` 6345-6346; `original` Knöll, 5732-5733. Three words: "checked at card".
   - Bahram's words: `printed` Sachau, BIR 29121-29122, word for word.
   - Q2, Faustus: `printed` Stothert, `npnf104` 4523; `original` Migne 16422-16436, verbatim as the scan has it (the outline renders from the Latin; NPNF confirms it clause for clause, so the damaged scan's reading stands). The scan's line breaks, dash and stray "A." are named in `uncertain`.
   - Q3, the confession: `printed` Le Coq, KHU 17347-17357, verbatim with the scan's "da>-" for "day", named in `uncertain`, with "miserable" given as "wretched" (outline Q3 row).
   - No `secondReading` is set for the three spans of six words or more.

## Entry fields (for release)

8. `why`.
   - Old: "He broke from them after what he described as revelations from his heavenly twin."
   - New: "He broke from them after what he described as revelations from an angel he called the Companion."
   - Evidence: FIH 4395-4396, "hiess at-Taum, was im Nabatäischen soviel als Gefährte bedeutet" (companion). Outline Do not say: "his heavenly twin" → "an angel he called at-Taum, the Companion"; Source Sheet G: "twin" rests on the editor (FIH 7083), a modern reading.
   - Old: "He wrote his own scriptures and had them translated on purpose, and his faith spread from Persia all the way to China."
   - New: "He wrote his own scriptures, and his faith spread from Persia all the way to China."
   - Evidence: outline Do not say: "Mani had his books translated on purpose" (card) → not held. Kit Part 1: no short text repeats a claim the brief no longer makes (the pre-kit brief made it; the finished brief does not).
9. `teaser`.
   - Old: "a prophet who set out to found the one universal religion, and whose one intact surviving temple still stands on a hillside in Fujian."
   - New: "a prophet who called himself the last of God's messengers, and whose Hearers' prayer of confession was kept in a cave library near Dunhuang."
   - Evidence: outline Do not say: "the last Manichaean temple still stands in Fujian" (card) → leave out, modern, not in a held source; "meant to replace Christianity, Zoroastrianism and Buddhism" → not held (the one universal religion is the same modern judgment). Kit Part 1: a judgment only a modern work makes stays off the card. New words: the brief ("in this last age, the revelation had come down through Mani himself, God's messenger"; "a cave library kept a scroll ... It is the Hearers' confession"); BIR 29063-29064, "the seal of the prophets (i.e. the last of them)".
10. `modernWorks` (new on the entry), the outline's modern tools (Who tells it, Modern; Source Sheet, Files and D):
    - `{"title": "Introductory Essay on the Manichaean Heresy (Nicene and Post-Nicene Fathers, first series, 4)", "author": "Albert H. Newman", "year": "1887", "note": "Mani's life and teaching, with an English version of the Fihrist's account."}` (NPI, the translation check on FIH; title at `npnf104` 712).
    - `{"title": "Commentary in Mani, seine Lehre und seine Schriften", "author": "Gustav Flügel", "year": "1862", "publisher": "F. A. Brockhaus", "note": "Notes on the Fihrist's chapter on Mani, among them the angel's name at-Taum."}` (Source Sheet G, FIH 7083).
    - `{"title": "Introduction and notes to Dr. Stein's Turkish Khuastuanift from Tun-huang (Journal of the Royal Asiatic Society, 1911)", "author": "A. von Le Coq", "year": "1911", "note": "The scroll and its find, and the confession's words on the light of the Five-God."}` (Source Sheet D, alms row, KHU 18038-18050; B30).
    - `{"title": "Notes to Un traité manichéen retrouvé en Chine, part 2 (Journal asiatique, 1913)", "author": "Édouard Chavannes and Paul Pelliot", "year": "1913", "note": "The Chinese texts on the Manichaeans, their sources and dates, and Chinese names such as the Hu, for western foreigners."}` (Source Sheet D, the Hu, CHI 6907-6909; B26a).
    - Rights: all four are prints before 1931, held in `cic/texts/`, listed as further reading only, with nothing quoted.
11. `documentedStories[0].modernWorks` (new), the BeDuhn item moved from the story's `sources` (edit 3): `{"title": "Augustine's Manichaean Dilemma, vol. 1", "author": "Jason BeDuhn", "year": "2010", "publisher": "Penn", "note": "Augustine's years as a Hearer."}`. Title, author, year and publisher word for word from the old `work`. The old note, "The fullest modern study of Augustine's years as a Hearer.", judged the work; the new note says what it covers (Kit Part 1). Not held; a modern work listed for reading only.

## Flagged, not changed

- `floorNote`: "most scholars: a distinct universal religion" states a modern opinion as content (Kit Part 1; outline Setting: "The story does not settle what it was"). It is the doctrinal-floor note, a governance field, so it is left for the checker and Mark.
- `experienceToday` (an entry field outside the card): the Fujian temple, which outline Do not say keeps off the story and card as modern and not held.
- `people[2]` (Faustus): the outline's Q2 row says the people entry's line from Reply to Faustus II.1 is one "which this story's card replaces". It is not wrong (the line stands at `npnf104` 4338) and shares no words with Q2, so under this role it is left word for word.
- `voices[2]` (Augustine), "the movement's most effective Latin opponent": a judgment of praise in the narrator's voice; not contradicted by a held source, so left.
- Not carried: the Acts of Archelaus's life of Mani (Leave out allows "or nowhere"); Eusebius's "from Persia to our part of the world" (Cut first 7, Leave out); the father's voice in the idol temple (Leave out, no card).

## Not found (left in place)

- `voices[0]`: "rather than leaving the task to disciples".
- `legacy`: "It had largely vanished by the sixth century"; "it held on in southern China for many centuries"; the manuscripts from Turfan and Medinet Madi and the Cologne Mani Codex (Source Sheet: not held); "one of the few extinct ancient religions that can now be read largely in its own words".
- `why`: "before his conversion" (not re-read here; the Confessions hold the nine years only, B14).
