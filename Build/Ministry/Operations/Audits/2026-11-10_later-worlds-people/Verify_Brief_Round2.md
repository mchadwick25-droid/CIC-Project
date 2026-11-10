# P2-G3b, later-worlds count: round 2 verification brief

Read `Verify_Brief.md` (same folder as this file) first: the labels S / E / N / U, the passage rule
and the output format are the same. This round differs in three ways.

1. **One strict rule for where a mention may sit.** A context counts S only if it lies inside a
   work that THIS tradition's shelf holds, as the `files` entry describes it (work title and
   locus). If the locus is "whole file", anywhere in the file's own text counts (editorial matter
   still excluded). If the locus names a work, a section, letters, pages, a div or lines, the
   mention must be inside that part. Another work in the same file, even by the same author, is
   U, not S. Check the file around the line (`sed -n`) to see which work you are in; use the
   file's headings. If you cannot tell where the shelved work starts and ends, say so and use U.
2. **Fresh contexts.** Each candidate lists `aliases_dropped_as_namesakes` (round 1 found only
   other people under them; they are not searched now), `confirmed_round1` (traditions already at
   5, not re-checked), and `needs` (how many more traditions at 5 the person needs to pass). The
   contexts here were NOT seen in round 1. Some traditions also carry `round1_clean`: for those,
   the first contexts are round 1's S passages, shown again for a strict-rule recheck, and the
   rest are fresh.
3. **Stop early.** Once a candidate has `needs` traditions at 5 clean passages, you may stop
   labelling its remaining traditions (leave them out of the output).

Output: `result.json` in your own folder, same shape as before, one object per candidate, in input
order. Add `"passes": true|false` (true when confirmed_round1 plus your traditions at 5 reach 2) and
for every tradition you count at 5 or more, a list `clean_refs` of the distinct S passages as
`"file:line"`. Every `best_quote` copied exactly from the file and checked by grep or a script.
Do not edit the repository; write only in your own folder; no model calls, no network.
