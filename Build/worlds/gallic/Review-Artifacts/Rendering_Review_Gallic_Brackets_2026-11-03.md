# Rendering Review: gallic quote records, bracketed supplements (1 record)

- **Reviewer:** Opus 5.5 (independent; did not render or review this record before)
- **Date:** 2026-11-03

## Method (short)

I read the working-tree record and its diff against HEAD. I then read the edition text at `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml`, lines 727-741 (Vita S. Martini ch. II). I matched each source clause to the rendering in order. I checked the bracket rule, sentence length, one thought per sentence, the kept hedge, modern-sense traps, and plain English. No model calls were made.

The supplement "[servant's]" adds meaning. Without it, "he drew off his boots" reads as Martin's own boots. The translator inserted it to resolve that reading (it stands for the Latin dative *ei*, "from him"). So the rule requires it to stay bracketed or be left out. It may not be voiced as the source's own word.

## Results

| Record id (gallic.quote.…) | Bracketed words in text | Rendering check | Verdict |
|---|---|---|---|
| the-soldier-who-served-his-servant | "[servant's]" (translator's supplement, line 730; adds meaning, since it settles whose boots) | Bracket rule: met. The rendering keeps "his [servant's] boots" bracketed. The earlier "the other man's boots" voiced the supplement as the source's own; that is now fixed. Every clause is rendered, in order: "changing places as it were" becomes "as if the two had changed places", which keeps the hedge; "for the most part" becomes "most of the time"; "however" becomes "yet"; "even at that date" becomes "even then". Nothing is added. Each of the 10 sentences carries one thought. The longest is 21 words ("It went so far that..."). No modern word misleads: "lower one" stands for "inferior", "trade" for "class of men", "remarkable" for "wonderful". The English is plain. | PASS |

Out-of-scope note, flagged rather than fixed: the record's `modern_lens_note` quotes the source as "drew off his servant's boots" without the brackets. That presents the supplement as Sulpitius's own words inside a quotation mark. The rendering itself is not affected.
