# Card edits, round 2: John Wyclif

Starting card: the census's current `card` for `john-wyclif` (`cic-website/data/world-census.json`). Brief: `john-wyclif.brief.txt` (final). Every field not named below is kept word for word. No `briefLength` (the census does not accept it). No statement on the card corrected.

## New

1. **quotationOriginals, removed.** The entry whose modern is Hus's three sentences ("I do not know where John Wyclif's soul is. ... Yet in hope I would wish my soul to be where John Wyclif's soul is."). The new brief quotes only the last sentence, so the three-sentence span is not a quotation in it.
2. **quotationOriginals, added: Hus.** Modern: "Yet in hope I would wish my soul to be where John Wyclif's soul is." Printed: "vellem tamen in spe, quod anima mea esset ibi, ubi est anima Joannis W.", palacky 15248-15249, re-read. Second reading: "same", the removed entry's value; this sentence is part of the span `Second_Readings.md` line 39 judged SAME (no new reading in batch 3's round 3). Uncertain: the removed entry's note, cut to this sentence (drops "Joan. W." and the clause on the second reading keeping "John W.", which concerned the first sentence's rendering); the name is given just before as "Joannis Wiclef" (15242-15243); Hus first said it twelve years before (15243-15245).
3. **quotationOriginals, added: the English tract.** Modern: "So Christ and his apostles taught the people in the tongue the people knew best. Why should people not do the same now?" Printed: the scan's words verbatim, its doubled spaces and line breaks set as single spaces: "& j^us crist & his apostlis taujtew fe puple in fat tuwge fat was moost knoAvuw to J^e puple ; why shuldew not mew do non so ?", matthew1880 35791-35795 (lines as corrected in `Second_Readings_3.md` line 53; the question ends on 35795). Work: De Officio Pastorali, ch. 15, ed. Matthew. Second reading: S3-26 (`Second_Reading_Key_3.md` line 32), SAME → "same" (`Second_Readings_3.md` line 36). Uncertain: the normalized Middle English (Outline Quote 1; Source_Sheet E13, B13); "men" means people; authorship rests on editors: Matthew "undoubtedly genuine" (matthew1880 2866-2867), Shirley no accurate list of the English tracts yet (fasciculi 2612-2616, re-read; Source_Sheet gives 2614-2618).
4. **quotationOriginals, added: Knighton.** Modern: "And so the Gospel's pearl is scattered and trampled by pigs." Printed: "et sic evangelica margarita spargitur et a porcis conculeatur", knighton 16968-16969, re-read ("evan- / gelica" joined; the scan reads "conculeatur"). Second reading: S3-27 (key line 33), SAME → "same" (`Second_Readings_3.md` line 37). Uncertain: hostile witness; the passage dated only "probably before 1400" (wycliffite-bible 870-871, re-read); the scan fault.
5. **briefReferences, replaced.** Nineteen plain-text references with file and lines for what the new brief draws on, each re-read: matthew1880 35750-35755, 35791-35795, 2866-2867; knighton 16948-16969; wycliffite-bible 870-871, 69-74, 2317-2320, 979-981, 1025-1031; pollard 840-846, 967-975; fasciculi 1635-1637, 2606-2608, 2696-2706, 2748-2751, 27415-27421, 11404-11408, 11450-11457, 11579-11585, 11669-11684; lechler 694-700; vaughan 4033-4034; foxe v3 20044-20055; walter 673-679, 692-695, 25528-25536; foxe v4 17982-17988, 17458-17461; mansi t.27 65527-65560; schaff 1509-1516; palacky 15246-15249; census tradition `lollardy`. No quotation marks inside them. Dropped from the old list: Thorpe (pollard 7204-7220), the letter to Urban's summons line, Raynaldus (burning), the council mocking Hus, and Shirley's no-friendly-hand remark, since the new brief no longer draws on them. The Tyndale reference states only his own words (no one's English to follow) and Walter's (a version of his own); nothing ties his text to Wyclif's.
6. **sources.about, added: Foxe, Acts and Monuments, volume 4** (`cic/texts/foxe_acts-and-monuments-v4_cattley-townsend1837.txt`). Evidence: the brief's Grosar and Durdant sentences (17982-17988, 17458-17461).
7. **sources.about, added: Tyndale, Doctrinal Treatises, ed. Henry Walter, 1848** (`cic/texts/tyndale_doctrinal-treatises_walter1848.txt`). Evidence: the brief's scarcity sentence (673-679) and its Tyndale sentence (25528-25536; from the Greek, 692-695).

## Left alone

- keyWorks, De Officio Pastorali: "Wyclif writes" stands, credited to Matthew's "undoubtedly genuine" (2866-2867); the brief's "goes under John Wyclif's name" does not contradict it, and the new quotation's `uncertain` carries the doubt.
- legacy.traces, Hus "in a sermon of probably 1408": credited to Workman and Pope; the brief gives no year (as round 1).
- legacy.traces, Forshall and Madden's "between 1382 and 1526" (wycliffite-bible 76-78): their own claim about the Wycliffite versions; it does not name Tyndale or tie his work to Wyclif's.
- The card nowhere says or implies that Tyndale built on Wyclif's text.

## Not found

None. Every card claim the new brief touches is supported in the held files.

## For the census edit (not done here)

`tools/quote_renderings.json` lists the old three-sentence Hus span for `john-wyclif`; when the census takes the new brief, its renderings listing must match the three new quoted spans.
