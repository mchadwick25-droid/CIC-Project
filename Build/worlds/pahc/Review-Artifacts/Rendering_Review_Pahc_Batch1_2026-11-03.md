# Rendering Review: pahc quote records, batch 1 (25 records)

- **Reviewer:** Opus 5.5 (independent; did not draft or render any of these records)
- **Date:** 2026-11-03
- **Subject:** the `text` and `modern_rendering` of 25 `pahc.quote` records.

## Method

Each record's `text` is checked by script against the vendored file named or implied by its locus. For XML files, `<note>` blocks and tags are blanked with line numbers preserved, entities are decoded, line-end hyphens are rejoined and whitespace (including U+00A0) is folded. Curly and straight quotation marks are treated as the same. "..." in `text` splits the quote into segments, and each segment must occur in order. For the Didache records, the edition's inline verse numerals ("2.", "3.") are set aside as apparatus. For the Pliny record the passage sits inside an editorial endnote, so that file is searched with note bodies kept. Line spans run from the line holding the first word to the line holding the last.

Renderings are read clause by clause against the edition span and checked against `confidence.divergence_note` and `use_note.not_for`. Sentence lengths are counted by script (split at sentence-final punctuation, words counted on whitespace) and the longest sentence is reported. The bracket rule is applied: an editor's or translator's bracketed or parenthetical supplement that adds meaning must not be voiced as the source's own. A parenthetical that only gives the source's own original word (Greek *eucharistia*, Latin *ministrae*) is not treated as added meaning.

Files read: `cic/texts/npnf204_athanasius-select-works-letters.xml`, `anf01_apostolic-fathers-justin-irenaeus.xml`, `anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml`, `anf07_lactantius-apostolic-constitutions-didache-liturgies.xml`, `anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml`, `npnf201_eusebius-church-history-life-of-constantine.xml`, `lucian_works-vol4-peregrine_fowler1905.txt`, `tacitus_annals-15-44_church-brodribb1876.txt`.

## Results

**25 records: 21 PASS, 4 FAIL (3 P1, 1 P2).**

| Record id (pahc.quote.…) | Edition text at (file, lines) | Text check | Rendering check | Verdict |
|---|---|---|---|---|
| appointed-to-be-read | cic/texts/npnf204_athanasius-select-works-letters.xml, lines 68817-68825 | pass | all clauses present; editor's "[merely]" voiced as Athanasius's own "only read"; longest 24 | FAIL P1 |
| asia-rejected-new-prophecy | cic/texts/anf07_lactantius-apostolic-constitutions-didache-liturgies.xml, line 11308 | pass | clauses present; after three "They" sentences about the faithful, "they were thrown out" reads as the faithful being expelled; longest 17 | FAIL P1 |
| first-clement-apostolic-chain | cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml, lines 1845-1860 | pass | all clauses; "[has done so]" rendered as grammar ("did the same"); "[of their labours]" not voiced; elision kept; longest 13 | PASS |
| first-concerning-the-cup | cic/texts/anf07_lactantius-apostolic-constitutions-didache-liturgies.xml, lines 12960-12964 | pass (verse numerals set aside) | all clauses; "(Eucharist)" gives the Greek word the text itself uses; no body/blood or institution language added; longest 27 (prayer after colon, 23) | PASS |
| hermas-doubting | cic/texts/anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml, lines 2386-2400 | pass | all clauses; "creature" to "creation" avoids the animal sense; "double-souled" kept; elisions kept; longest 16 | PASS |
| ignatius-marriage-bishop | cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml, lines 8734-8737 | pass | all clauses; "it becomes" to "it is right"; no rite added; longest 18 | PASS |
| ignatius-truly-born | cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml, lines 6612-6623 | pass | all clauses; each unbracketed "truly" kept; bracketed "[truly]" before "died" left out; longest 17 | PASS |
| in-living-water | cic/texts/anf07_lactantius-apostolic-constitutions-didache-liturgies.xml, lines 12914-12920 | pass (verse numerals set aside) | all clauses and fallbacks in order; "thrice" to "three times"; longest 25 | PASS |
| jesus-christ-our-god | cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml, lines 6509-6517 | pass | all clauses; "enactments" to "commands"; "Jesus Christ our God" kept as is; longest 26 | PASS |
| justin-flame-kindled | cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml, lines 17851-17857 | pass | all clauses; "attend to them" to "think them over"; "Thus, and for this reason" kept as two; longest 19 | PASS |
| justin-reasonable-livers | cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml, lines 15684-15695 | pass | all clauses; "partakers" to "shared in the Word"; "barbarians" to "non-Greeks"; Elias given as Elijah; elision kept; longest 18 | PASS |
| lucian-all-brothers | cic/texts/lucian_works-vol4-peregrine_fowler1905.txt, line 1049 | pass | all clauses; Lucian's "You see" and "misguided" kept; "self-devotion" to "give themselves up"; longest 21 | PASS |
| lucian-orphans-and-widows | cic/texts/lucian_works-vol4-peregrine_fowler1905.txt, line 1049 | pass | all clauses; Lucian's own aside "(as he was still called in those days)" kept; "gaolers" to "jailers"; longest 20 | PASS |
| melito-no-phantom | cic/texts/anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml, lines 71180-71206 | pass | all clauses; two-natures sequence (three years / thirty periods) intact; longest 26 | PASS |
| moses-is-more-ancient | cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml, lines 15608-15613 | pass | all clauses; four topics kept; "suggestions" to "hints"; Justin's claim stays his; longest 24 | PASS |
| not-every-one-that-speaketh-in-the-spirit | cic/texts/anf07_lactantius-apostolic-constitutions-didache-liturgies.xml, lines 13026-13028 | pass (verse numerals set aside) | all clauses; test by "ways", not doctrine; trailing elision kept; longest 25 | PASS |
| polycrates-to-victor | cic/texts/anf08_twelve-patriarchs-clementina-apocrypha-edessa-syriac.xml, lines 72578-72623 | pass | clauses present; the `text` elision (lines 72585-72613) is dropped, so two separate passages read as continuous; longest 21 | FAIL P2 |
| put-away-doubting-from-you | cic/texts/anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml, lines 2386-2391 | pass | all clauses; inner question kept as Hermas's imagined speech; trailing elision kept; longest 23 | PASS |
| tacitus-hatred-against-mankind | cic/texts/tacitus_annals-15-44_church-brodribb1876.txt, line 68 | pass | all clauses; "called Christians by the populace" kept as the crowd's name; no arson claim against Christians; longest 16 | PASS |
| the-memoirs-of-the-apostles-are-read | cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml, lines 16502-16507 | pass | all clauses; "president" to "the one presiding" (no titled office); "as long as time permits" kept; longest 19 | PASS |
| they-appointed-the-first-fruits | cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml, lines 1856-1865 | pass | all clauses; "first-fruits" glossed as "first converts" from the Greek's own "their first-fruits", not from "[of their labours]"; Scripture quote kept as Clement gives it; longest 24 | PASS |
| they-appointed-those-already-mentioned | cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml, lines 1922-1930 | pass | clauses present; editor's "[ministers]" voiced as Clement's own "the ministers named before"; longest 17 | FAIL P1 |
| those-who-lived-reasonably-are-christians | cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml, lines 15686-15695 | pass | all clauses; leading and trailing elisions kept; "lived by reason"; longest 16 | PASS |
| two-female-slaves-who-were-called-deaconesses | cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml, lines 19502-19507 (inside translator's endnote) | pass (note body; `<i>` tag around ministræ) | all clauses; "who were called" frame kept; "(ministræ)" is Pliny's own Latin word, not an added sense; torture kept; longest 15 | PASS |
| two-ways-one-of-life-and-one-of-death | cic/texts/anf07_lactantius-apostolic-constitutions-didache-liturgies.xml, lines 12700-12708 | pass (verse numerals set aside) | all clauses; negative golden rule kept as negative; longest 21 | PASS |

## Failed renderings: corrected text

### appointed-to-be-read (FAIL P1)

The edition prints "the latter being [merely] read". The bracketed "merely" is the translator's supplement, and it adds a sense of lesser worth. The rendering "These others are only read" voices it as Athanasius's own. The correction leaves it out.

Corrected rendering:

> I add this too, to be more exact, and I write it because I must. There are other books besides these. They are not in the Canon. But the Fathers appointed them to be read by those who newly join us and want teaching in the word of godliness. These are the Wisdom of Solomon, the Wisdom of Sirach, Esther, Judith, Tobit, the book called the Teaching of the Apostles, and the Shepherd. But the books I listed first, my brothers, are in the Canon. The others are read. And nowhere is there any mention of apocryphal writings.

### asia-rejected-new-prophecy (FAIL P1)

In the edition, those expelled are the people led astray by the new prophecy. The surrounding lines call them "those few who were thus deluded". The rendering opens three sentences in a row with "They" for the faithful, so its final "they were thrown out" reads as the faithful being expelled. That turns the meaning around. The correction names the referent from the passage's own context and adds no new name.

Corrected rendering:

> The faithful all over Asia met many times, in many places in Asia, to talk this over. They looked closely at these new teachings. They declared them false and rejected them as heresy. Because of that, those who had been led astray were thrown out of the Church and shut out of communion.

### polycrates-to-victor (FAIL P2)

The record's `text` has an elision after "the coming of the Lord", where the edition lists the Asian luminaries (lines 72585-72613). The rendering drops the elision mark, so two separate passages read as one continuous statement. The correction restores the mark.

Corrected rendering:

> As for us, we keep the exact day with great care, adding nothing and taking nothing away. For in Asia great luminaries have gone to their rest, and they will rise again on the day the Lord comes... And I too, Polycrates, the least of you all, follow the tradition of my relatives, some of whom I have succeeded. Seven of my relatives were bishops, and I am the eighth. My relatives always kept the day when the people put away the leaven. I myself, brothers, am sixty-five years old in the Lord. I have met the brothers in every part of the world, and I have read through all of Holy Scripture. So I am not frightened by the things people say to terrify us. For those greater than I have said: "We ought to obey God rather than men."

### they-appointed-those-already-mentioned (FAIL P1)

The edition prints "those [ministers] already mentioned". The bracketed noun is the editor's supplement, and it puts a label on a group the Greek leaves unnamed ("those mentioned before"). That label matters here, because the divergence note says the key clause is much disputed and may be corrupt. The rendering "the ministers named before" voices the label as Clement's own. The correction leaves it out.

Corrected rendering:

> So, for this reason, because they knew this fully in advance, they appointed those already mentioned. Later they gave instructions that, when these men died, other approved men should follow them in their ministry.
