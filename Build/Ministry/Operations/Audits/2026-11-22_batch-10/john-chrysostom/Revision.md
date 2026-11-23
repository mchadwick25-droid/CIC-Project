# Revision: John Chrysostom (`john-chrysostom.brief.txt`)

Revised 2026-11-23 under the change order of 2026-11-19: approved wording is kept wherever it passes; a fix touches only what fails. Backup before any change: `john-chrysostom.brief.v1.txt` (never edited).

## Do not say (no Outline.md for this story, so recorded here, word for word from Review.md)

- "Do not place the Homily 50 on Matthew line in his Constantinople years or after his consecration. The Matthew homilies were preached at Antioch (npnf110 line 535). Tell it with his Antioch years."

## Findings and what I did

- **B1 (BLOCKING).** I checked `cic/texts/npnf110_chrysostom-homilies-matthew.xml` line 535 ("were undoubtedly delivered at Antioch") and lines 29929–29931 (the line itself). I deleted "In a sermon on Matthew, John told his listeners that if they wanted to honor the body of Christ, they must not neglect Him when He is naked." from paragraph three. I inserted the review's wording word for word into paragraph two, after "…who kept to the literal sense of Scripture.": "There, in a sermon on Matthew, he told his listeners that if they wanted to honor the body of Christ, they must not neglect Him when He is naked." No other wording changed. Paragraph three now ends "…and built more hospitals."
- **M1 (MINOR, card).** In `Card.existing.json` I replaced the briefReference "Socrates, Church History VI.3, tr. Zenos: John's training under Diodore, who kept to the literal sense of Scripture." with the review's wording: "Socrates, Church History VI.3, tr. Zenos: John's training under Diodore; Zenos's note and Prevost's preface (NPNF 1.10): Diodore's literal sense." The JSON still parses. The brief is unchanged for M1.
- **M2 (MINOR).** The brief is being re-recorded for B1, so I applied the review's smallest split word for word: "…in procession. By this, Socrates says, he brought back to the church's communion the followers who had left it over John's deposition." The longest sentence is now 29 words.

## New sentences

None. Every sentence is the old brief's wording or the review's exact wording.

## Essence

Complete at "naked" (word 158 of the file), at Antioch, within the first minute: the plain speech aimed at the powerful (the Eutropius hook), then the poor in the Matthew line.

## Checks

- Scorer: `john-chrysostom.brief.txt: 352 words, grade 8.4 (names out 7.1), reading ease names out 72.9, 16.0 words a sentence, 0.6 joining words per 100, 9% short sentences, longest sentence 29 words - pass`.
- Heard once as the listener. The Matthew line now sits with Antioch, and "There" points back to it plainly. The Constantinople paragraph runs from 398 to the hospitals and on to the rebukes without a break.
- Four faults re-read: no one witness's claim told as fact (Palladius and Socrates are still credited); no editor's view given to a source (the card now credits the literal sense to Zenos and Prevost); no date or detail on the wrong event (B1 fixed); no force or conflict softened.
- Length: 352 words by the scorer (358 by whitespace), about 2.3 minutes at 150 words a minute. Not lengthened.

Coordinator's note (2026-11-23): the M1 change to `Card.existing.json` was undone; that file stays the census card as it stands. M1 (the Diodore "literal sense" reference credited to Socrates VI.3, where it comes from Zenos's note and Prevost's preface) goes to the card step as a card correction.
