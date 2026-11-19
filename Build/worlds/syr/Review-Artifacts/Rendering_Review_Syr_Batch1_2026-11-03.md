# Rendering Review: syr quote records, batch 1 (17 records)

- **Reviewer:** Opus 5.5 (independent; did not draft or render any of these records)
- **Date:** 2026-11-03
- **Subject:** the `text` and `modern_rendering` of 17 `syr.quote` records.

## Method

Each record's `text` was searched for in the vendored edition named by its locus, read from `cic/texts/`. For the XML files, `<note>` elements and all other tags were stripped first. Line-end hyphens were rejoined, whitespace was folded (U+00A0 included), and curly quotes were folded to straight ones. The line span runs from the line holding the quote's first word to the line holding its last word. The vendored lines around each span were then read directly, so that each rendering was checked against the edition and not only against `text`.

Sentence lengths were counted by script and then hand-checked. A sentence ends at a full stop, question mark or exclamation mark, including one inside a closing quotation mark. Dashes are not counted as words. Each rendering was also checked against the record's `confidence.divergence_note` and `use_note.not_for`. Two further checks were applied. A bracketed or parenthetical supplement from an editor or translator that adds meaning must not be voiced as the source's own words, though a purely grammatical one may be rendered plainly. And every reported claim must stay inside its reported-speech frame.

Sources read: `npnf213_gregory-great-ephraim-syrus-aphrahat.xml`, `aphrahat_demonstrations-2-7_hallock1932.txt`, `addai_doctrine-of-addai.txt`, `npnf208_basil-letters-select-works.xml`, `anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml`, `chronicle-of-edessa_cowper.txt`, `palladius_paradise-v1-syriac_budge1907.txt`.

## Results

**17 records: 11 PASS, 6 FAIL (3 P1, 3 P2).**

| Record id (syr.quote.…) | Edition text at (file, lines) | Text check | Rendering check | Verdict |
|---|---|---|---|---|
| a-man-called-wise-amongst-the-jews | cic/texts/npnf213_gregory-great-ephraim-syrus-aphrahat.xml, lines 27421-27433 | pass (the section numeral "2." between secs. 1 and 2 is left out, as the divergence note says) | translator's gloss "(the Christian religion)" voiced as Aphrahat's own, set off by dashes; "not one wise man ..." sentence is 27 words | FAIL P1 |
| a-pearl-upon-the-palm | cic/texts/npnf213_gregory-great-ephraim-syrus-aphrahat.xml, lines 21794-21800 | pass | all clauses present; second sentence joins "saw mysteries" and "became a fountain" with a semicolon, 27 words | FAIL P2 |
| abgar-letter | cic/texts/addai_doctrine-of-addai.txt, line 25 | pass | one sentence of 27 words joined by a colon; the "not by ... but by your word" contrast is flattened to "and that" | FAIL P2 |
| aphrahat-anti-jewish-frame | cic/texts/npnf213_gregory-great-ephraim-syrus-aphrahat.xml, line 27100 | pass | "This is" renders the translator's grammatical "(This is)" plainly; all clauses; 16 | PASS |
| aphrahat-medicine-penitence | cic/texts/aphrahat_demonstrations-2-7_hallock1932.txt, line 39 | pass | all clauses; "smitten" as "wounded" holds; longest 25 | PASS |
| aphrahat-one-innocent | cic/texts/aphrahat_demonstrations-2-7_hallock1932.txt, line 38 | pass | "begotten" as "born", "put on a body" as "taken on a body"; all clauses; 22 | PASS |
| aphrahat-persecuted-litany | cic/texts/npnf213_gregory-great-ephraim-syrus-aphrahat.xml, lines 27954-27958 | pass | all five clauses, order kept; longest 12 | PASS |
| aphrahat-stone-foundation | cic/texts/npnf213_gregory-great-ephraim-syrus-aphrahat.xml, lines 24606-24610 | pass | "[this]" is a purely grammatical supplement, so rendering it plainly is allowed; all clauses; longest 20 | PASS |
| aphrahat-sure-thing | cic/texts/npnf213_gregory-great-ephraim-syrus-aphrahat.xml, lines 27115-27119 | pass | all sixteen titles present and in order; split into "He is" sentences with nothing added; longest 23 | PASS |
| as-a-stonecutter-i-have-brought-stones | cic/texts/npnf213_gregory-great-ephraim-syrus-aphrahat.xml, lines 27084-27093 | pass | all clauses; "wrangling" as "quarreling", "edify" as "build up"; longest 17 | PASS |
| basil-credits-a-syrian | cic/texts/npnf208_basil-letters-select-works.xml, lines 16726-16796 (endnotes 1435-1436 fall inside the span and are stripped) | pass | "Because it was closer to the Hebrew term ..." and the bird sentence stand outside the Syrian's "he said" / "he says" frame; "vital force" as "life" | FAIL P1 |
| blc-one-name | cic/texts/anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml, lines 68966-68970 | pass | all clauses; "lo!" as "see"; longest 25 | PASS |
| chronicle-flood-line | cic/texts/chronicle-of-edessa_cowper.txt, line 53 | pass | rendering repeats Cowper word for word; in modern English "temple" points to a pagan shrine, the reading `not_for` rules out | FAIL P2 |
| death-knew-his-kingdom-was-to-be-made-void | cic/texts/npnf213_gregory-great-ephraim-syrus-aphrahat.xml, lines 28079-28087 | pass | the poison simile is carried whole; "bringer to nought" is rendered through the simile, then "destroyed"; longest 20 | PASS |
| dem6-visit-the-sick | cic/texts/npnf213_gregory-great-ephraim-syrus-aphrahat.xml, lines 25658-25659 | pass | rendering matches the edition; 11 | PASS |
| ephrem-keeper-of-strangers | cic/texts/palladius_paradise-v1-syriac_budge1907.txt, line 1293 | pass | Budge's meaning-bearing supplement "[the means of relieving]" is voiced plainly as the account's own words | FAIL P1 |
| ephrem-only-begotten-dwelling | cic/texts/npnf213_gregory-great-ephraim-syrus-aphrahat.xml, lines 22306-22309 | pass | "[being]" is grammatical, and "left his place with God" holds the sense; all clauses; longest 24 | PASS |

## Failed renderings: corrected text

**a-man-called-wise-amongst-the-jews** (FAIL P1). The translator's parenthesis "(the Christian religion)" adds meaning, and the rendering voices it as Aphrahat's own words by setting it between dashes. The sentence "So it seems that in all your people ... and is heard" is 27 words, and moving "and is heard" to its end loosens the link to "whose prayer is heard".

Corrected rendering:

> One day a man known as wise among the Jews questioned me. He said: Jesus, who is called your Teacher, wrote this for you. If there is faith in you like one grain of mustard, you will say to this mountain, 'Move,' and it will move away from you. You will even say, 'Rise up and fall into the sea,' and it will obey you. So it seems your whole people has not one wise man whose prayer is heard, who asks God to make your persecutors leave you alone. For it is clearly written for you in that passage: there is nothing you will not be able to do. When I saw that he was blaspheming and speaking much against the Way [the Christian religion], my mind was troubled.

**a-pearl-upon-the-palm** (FAIL P2). The second sentence joins two thoughts, the mysteries seen in the pearl and the pearl becoming a fountain, and runs to 27 words.

Corrected rendering:

> One day, my brothers, I picked up a pearl. In it I saw mysteries of the Kingdom, images and symbols of the Majesty. It became a fountain, and from it I drank mysteries of the Son. I set it, my brothers, on the palm of my hand so I could examine it. I went to look at it from one side, and it showed faces on every side.

**abgar-letter** (FAIL P2). The rendering is one 27-word sentence joined by a colon, and it flattens the edition's contrast "not by medicines and roots ... but by Thy word". The corrected version keeps the healing claims inside Abgar's "I have heard" frame.

Corrected rendering:

> I have heard about you and your healing. I have heard that you do not heal with medicines and roots, but by your word you open the eyes of the blind.

**basil-credits-a-syrian** (FAIL P1). In the edition, the closeness to the Hebrew and the brooding-bird image both belong to the Syrian's report ("He said ... that", "the Syrians, he says, understand"). The rendering sets "Because it was closer to the Hebrew term ..." and "It is the way a bird ..." apart as free-standing claims, outside that frame. "Gives them life" also overstates "impart to them vital force".

Corrected rendering:

> How then did the Spirit of God move upon the waters? The explanation I am about to give you is not my own. It comes from a Syrian. He was as unschooled in this world's wisdom as he was learned in the knowledge of the Truth. He said that the Syriac word was more expressive. He said too that it was closer to the Hebrew term, and so came nearer to the meaning of Scripture. This is the meaning of the word. By 'was borne,' he says, the Syrians understand that it cherished the nature of the waters. In their reading, it was the way you see a bird cover her eggs with her body and pass living strength to them from her own warmth.

**chronicle-flood-line** (FAIL P2). The rendering repeats the edition word for word. In modern English, "temple" suggests a pagan shrine, which is exactly the reading `use_note.not_for` excludes.

Corrected rendering:

> And they destroyed the church building of the Christians.

**ephrem-keeper-of-strangers** (FAIL P1). Budge's bracketed "[the means of relieving]" adds meaning, since it turns "give me this distress" into a request for resources. The rendering voices it as the account's own words. It must stay bracketed. The citizens' line "O man, we know that you are God" is correctly kept, as the divergence note requires.

Corrected rendering:

> And the people said to him, 'O man, we know that you are God.' And he said to them, 'Put your trust in me, then, and give me [the means of relieving] this distress. For see: for your sakes I will set myself apart to become the keeper of a house that receives strangers.'
