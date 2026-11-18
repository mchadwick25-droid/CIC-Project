# Rendering Review: alx quote records, round 3 (1 record)

- **Reviewer:** Opus 5.5 (independent; did not draft or render this record)
- **Date:** 2026-11-04
- **Subject:** the `text` and `modern_rendering` of 1 `alx.quote` record, rechecked against the rendering bar (every clause, nothing added).

## Method

The reviewer reads the record and the edition at `cic/texts/anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml`, lines 47886-47900 (Stromateis VI.13). Footnotes and tags are stripped and whitespace folded. The record's `text` then matches the edition verbatim, including the translator's "[as deacons]". The reviewer matches the rendering clause by clause and counts each sentence's words. No model calls are made.

The reviewer then traces how a bracket in `modern_rendering` reaches a participant. Nothing on the way removes or rewrites a single square bracket:

- `engine/m4/quote_placement.py:172-173` sets `quotable_rendering(record)` between curly quotation marks, after the voice's lead-in. Lines 181 and 193 do the same with the code-written lead-in that names the speaker.
- `engine/m4/grounding_net.py:946-968` (`quotable_rendering`) only takes off one wrapping pair of quotation marks and turns inner curly double marks into single ones. It does not touch square brackets.
- `engine/m4/grounding_net.py:123` and `126-130` (`_DISPLAY_TAG`, `strip_tags`) remove only double-bracket tags and markers (`[[…]]`, `[[quote:…]]`, `[[story:…]]`, `[[as:…]]`). `strip_markdown` at line 173 hides only `[[…]]` spans. `engine/m4/output_check.py:83` (`_ANY_TAG`) also matches only `[[…]]`. `quote_placement.py:126-129` (`_settable`) requires the placed quote's inner text to equal the rendering exactly, bracket included.
- `engine/m4/citation_cards.py:192` copies `modern_rendering` verbatim into the card's `spoken_rendering`. `cic-poc/frontend/src/components/StoryMark.tsx:93-96` shows it as plain text in a blockquote under the label "In today's English".
- `engine/m2/site_compiler.py:111` passes `modern_rendering` verbatim as a pull quote's text.
- No text-to-speech path reads a quote rendering. The only audio in the tree is the public site's card-back clips, made from census summaries (`engine/m2/tests/test_card_back_audio.py`).

So the participant sees "will first serve [as deacons]" with its brackets, in the reply's quotation and on the card. It is never stripped and never spoken. The brackets mark it as an editor's supplement, the same convention the fleet uses in `desert.quote.melania-to-the-governor` and `syr.quote.ephrem-keeper-of-strangers`. "[as deacons]" adds meaning: it reads Clement's "minister" as the deacon's office. So the bracket rule requires it to stay marked, and it does. The bracket finding does not fail this record.

## Results

**1 record: 0 PASS, 1 FAIL.**

| Record id (alx.quote.…) | Edition text at (file, lines) | Text check | Rendering check | Verdict |
|---|---|---|---|---|
| the-grades-here-in-the-church | cic/texts/anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml, lines 47886-47900 | pass | Bracket rule met: "[as deacons]" stays marked and reaches the participant marked. "According to my opinion" is kept as "In my view", and "the Scriptures say" and "the apostle writes" are kept. "Economy" becomes "order", which avoids a misleading modern sense. The three grades, the angelic glory, the apostles' footsteps, the righteousness "as the Gospel teaches", the promotion in glory and "glory differs from glory" are all rendered. But the edition sets "a perfect man" in quotation marks as a quotation of Ephesians 4:13. The rendering gives "full maturity" with no marks, so a quotation the source marks as scripture's words is presented as Clement's own. The bar requires the source's reported-speech frames to be kept. Round 2 noted this and did not fail it. This review holds that a lost quotation frame is a missing element, not a stylistic choice. Longest sentence 20 words ("In my view, the ranks..."; also "They also imitate the order..."). | FAIL (minor) |

## Failed renderings: corrected text

### the-grades-here-in-the-church (FAIL, minor)

The Ephesians phrase goes back inside quotation marks. When code places the quote, `quotable_rendering` turns them into single marks. Inside the marks it reads "a mature man" rather than "a perfect man". The modern sense of "perfect man" (a flawless male) misleads, while the edition's "man" stays. Everything else, including "[as deacons]", is unchanged.

Corrected rendering:

> In my view, the ranks here in the Church, of bishops, presbyters and deacons, imitate the glory of the angels. They also imitate the order which, the Scriptures say, awaits those who have followed in the footsteps of the apostles. These people have lived in perfect righteousness, as the Gospel teaches. For those taken up in the clouds, the apostle writes, will first serve [as deacons]. Then they will be ranked among the presbyters, promoted in glory, for one glory differs from another. This goes on until they grow into “a mature man.”

Longest sentence 20 words. `gates.grade_text`: FK 7.23, FRE 66.90.

Notes that do not change the verdict:

- The edition's opening "Since" has no main clause within the quoted span. Rendering the clause as a statement is the plain reading, and it adds no claim.
- `use_note.means`, `modern_lens_note` and `confidence.divergence_note` (Clement's own speculation, not church order) all agree with the rendering. "In my view" carries the hedge they rely on.
- Outside this verdict: the body note says the "For" sentence is evidence for the "Since" clause. That describes the logic loosely, but the rendering does not depend on it.
