# Card check: The Ebionites and Nazoraeans (`ebionite-nazoraean-current`, tradition)

Checked: `ebionite-nazoraean-current.card.json` and `Card_Edits.md`, against `Card.existing.json`, the census entry, the brief, `ebionite-nazoraean-current.brief.approved.txt`, `Outline.md`, `Source_Sheet.md`, `Review.md` and `Fresh_Read.md`. I re-read every cited line in `cic/texts/` for the quotations, the card prose's quoted spans, the edits' evidence and the `briefReferences`, and spot-checked the `uncertain` items.

## Verdict

**FIX.** Four changes, set out below. With them made, the card passes. Its placement on a tradition entry is still held for Mark, as in the Montanism check: a tradition has no `card` key, and the validator and page builder do not read these four fields there.

## What was checked

1. **Edits against their evidence.** Edits 1-5 each stand on their lines. Edit 1: the brief, "Their own books are lost". Edit 2: ANF3 21552-21554 ("the other, Hebion"), ANF5 12273-12274, Pan 25230 ("Ἐβίων, ἀφ᾽ οὗπερ Ἐβιωναῖοι"), ANF4 34025 and 39118-39119. Edit 3: CSEL34 23235-23237, AugE 33602-33605, AugF 6787 and PL42 27450-27456 ("usque ad nostra tempora ... in exigua ... perdurant"). Edit 4: no held line makes the judgment. Edit 5: HE 34446-34464, JP 7541 and 7553, PL23 48081-48083 and 48161-48162, and VI 16163-16164 (in the chapter headed "A confession of the Catholic faith which Pope Damasus sent", VI 16132). Hilary is at npnf209 16941.
   - **Items sent to the card.** Every outline item marked card is on it. That covers Cut first 1-6, 4b-4d, 7, 8, 13, 15 and 16; the Leave out items marked card (B5b, B13-B16, E5, E9, E12, F3-F4, F9, I5); What came of it 1-3; Words to explain (Origen's columns and "the poverty of their Law"); and Source Sheet J (the prophets). The condescension in `Trust_Shape_Second.md` is on it too, and so is the Juliana line from `Review.md`. `Fresh_Read.md` sends nothing more.
   - **Modern content.** No modern opinion, date or identification is stated as content. Each `modernWorks` note says what the work covers.
2. **Nothing else moved.** A key-by-key diff against `Card.existing.json` shows only `floorNote`, `voices` and `legacy` changed, as listed, in the same key order. The four new keys follow at the end.
3. **`briefReferences`.** Seven lines, one per paragraph, each re-read at its lines. Each names only what the brief tells.
4. **Census rules.**
   - **Validator.** I built two scratch copies outside the repository, in `/tmp/claude-0/-home-user-CIC-Project/39d92526-11f8-5688-9d05-41b4a8cf62d5/scratchpad/ebio-check/`. Both carried the card fields with FIX 2-3 applied, the brief as `longDescription`, and the entry fields with FIX 1. On the tradition entry, the full `node tools/validate-census.mjs` (quotes included) gave 0 errors and the 4 standing warnings. As a person card, the run left only the expected errors: the test entry's person fields, `secondReading` not yet set on the four spans of six words or more, and the three renderings (Q1-Q3) not yet in `tools/quote_renderings.json`.
   - **Quotations.** Every `printed`, `englishPrinted` and `original` stands at its lines. Every double-quoted span in the card's prose stands in a cited file, and all six brief spans have one entry each. Every cited file is in `sources`. Keys are allowed, no audit is named, and the held originals are carried.
   - **Q1 Greek, checked by hand.** At JusG 2166-2167, Εἰσίν ... τοῖς τοιούτοις τολμῶντες· οἷς ἐγὼ οὐ σύναινός εἰμι matches the rendering clause by clause. Nothing is added.
   - **Q2 Latin.** CSEL34 23272-23275 matches the rendering, and AugE 33605-33609 confirms it.
   - **Q3 Latin.** PL23 48133-48136 is a damaged scan ("ἃ dormientibus"). Richardson, VI 39337-39340, confirms the reading, so printing the Latin is right.
   - **Spelling.** Two British spellings sit in prose outside quotation marks (FIX 2-4).
5. **"checked at card".** "an apostate from the Law" matches its original, Pan 24117 and 26753 ("apostatam eum legis"), and its print, ANF1 33537-33538 ("an apostate from the law"). "poor" matches its print, ANF4 39118-39119 ("“poor”"), and no Greek is held. Both pass.
6. **Not found, and the flagged fields.** Ruled below. FIX 1 comes from these rulings.
7. **Entry fields.**
   - Edits 10-14 pass. The teaser's "the second century" and "about 400" are the brief's.
   - `peopleNote` and `voices[0]` match C5, rated Documented as their reports.
   - In `modernWorks`, the Archambault `url` is the license address the file's own licence element names (JusG line 5, line 29). That is the attribution CC BY-SA asks for, so it stays.
   - `why` needs FIX 1.

## Rulings on the flagged fields and the claims not found

- **`dates` "1st-4th c." Not clearly wrong. Not changed by this card.**
  - The first century has three held old witnesses, not only Epiphanius, as the outline puts it. Epiphanius places both beginnings at Pella (Pan 25029-25034, 25335-25345). Tertullian sets "Hebion"'s teaching in John's epistle (ANF3 21552-21554). Jerome says John wrote against "the then growing dogma of the Ebionites" (VI 39566-39572). All three are later and hostile, and the sheet rates the Pella beginnings Contested (H2, H3). No held source contradicts them.
  - The brief's "Church writers wrote of them from Justin's day" dates the writers, not the community, so it does not contradict the field.
  - The fourth century as the close: the last dated witness is Jerome in 404 ("usque hodie", CSEL34 23235). Augustine says the sect "still continues" (AugF 6787). Neither gives an end, and "4th c." does not contradict the brief's "to about 400".
- **`start` 70. Not clearly wrong. Not changed.** It rests on Epiphanius's Ebionite beginning "after Jerusalem was taken" (Pan 25335-25336), in the timeline's voice rather than his.
- **`end` 400. Not clearly wrong. Not changed.** It matches the brief's "to about 400". No held witness gives an end.
- **For Mark.** Timeline years for a span the sources leave open are his call, as in the Montanism check, FIX 4. Options for his ruling, not proposed here:
  - keep all three fields as they are;
  - make `start` the first writer the brief tells (Justin, mid-second century, A2, Widely Accepted), with `dates` "2nd-5th c." or "2nd-4th c.";
  - set `end` to 404, Jerome's letter.
- **`region` "Palestine, Syria" (with `placeLabel` and `placeQualifiers`). Not clearly wrong. Stays.** No held witness uses the word "Palestine". But Epiphanius places them in the Decapolis near Pella, Kokaba in Bashan, Paneas, Moab and Nabataea (Pan 25026-25029, 26876-26879). Those places lie in the region that `placeQualifiers` qualifies as "the historical region". The outline bars the word only from speech, and the teaser no longer uses it (edit 11).
  - One related point, outside this card: `modernCountries` lists Syria alone, though Pella and Moab lie in modern Jordan. It is noted for Mark with the timeline fields.
- **`why`: "long after most of the church had moved on" and "honoring James, the brother of Jesus". Change both (FIX 1).** They are not wrong by a held source, and Epiphanius does give some footing for James. He says they once prized virginity "δῆθεν διὰ τὸν Ἰάκωβον τὸν ἀδελφὸν τοῦ κυρίου", supposedly for the sake of James (Pan 25331). He also gives their Ascents of James (Pan 26731-26734). Even so, the approved text made both claims: "long after the wider church had moved away from them" and "honored James the brother of Jesus". The finished brief makes neither. Kit Part 1, as the card role applies it, bars `why` from repeating a claim the brief no longer makes. The first claim is also the modern frame that edits 4 and 12 removed from `legacy` and `relationsSummary`. The second leans toward the outline's Do not say, "James's community". What the held lines say about James is already on the card, in `uncertain[14]` and Q3.
- **`legacy`: "No community descends from them". Not found, and not clearly wrong. Stays.**
  - The brief never made this claim. It agrees with the census `livingEvidence` ("Its carriers ended") and with the outline's "census: no line" against descent. It does not say they died out, which the outline's Do not say bars.
  - For Mark, a note only: the `livingEvidence` basis cites this very sentence, so the claim rests on the census alone.
- **`voices[0]`: "No leader of these communities is named in any source they produced themselves". Not found, and true as an absence. Stays.**

## FIX

**FIX 1. Entry field `why`, first sentence (for release, with edit 10 on the second sentence).** It repeats two claims the finished brief no longer makes (rulings above).
- Old: `Some Jewish communities of believers in Jesus kept observing Torah, circumcision, and the Sabbath long after most of the church had moved on, honoring James, the brother of Jesus, and regarding Paul as someone who had abandoned the Law.`
- New: `Some Jewish communities of believers in Jesus kept observing Torah, circumcision, and the Sabbath, regarding Paul as someone who had abandoned the Law.`
- Evidence: the brief, "went on keeping that Law: circumcision, the Sabbath, the food laws" and "They rejected Paul as "an apostate from the Law", one who had abandoned it".

**FIX 2. Card `uncertain[8]` ("The Sabbath and the Lord's day"). American spelling in the card's own prose.** The words are not in quotation marks.
- Old: `in memory of the Saviour's resurrection.`
- New: `in memory of the Savior's resurrection.`

**FIX 3. Card `quotationOriginals[0].uncertain`. American spelling.**
- Old: `used under a Creative Commons Attribution-ShareAlike 4.0 licence.`
- New: `used under a Creative Commons Attribution-ShareAlike 4.0 license.`

**FIX 4. Entry field `modernWorks`, the Archambault `note` (`Card_Edits.md` edit 14). American spelling.**
- Old: `under a Creative Commons Attribution-ShareAlike 4.0 licence.`
- New: `under a Creative Commons Attribution-ShareAlike 4.0 license.`
