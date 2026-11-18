# Brief: second pass on one span of the finding guide (Groen van Prinsterer, Ongeloof en Revolutie, 1868)

First read <scratch>/GUIDE_BRIEF.md
(the rules the guide was written to; they still hold). The Dutch file and line numbers are as described there.
No web. No model or API calls. Edit nothing but your output files.

You are given: an existing guide JSON for one span, and an independent review of a random sample of the whole
guide: <scratch>/review_guide.json
The review found these faults. Your job is to find and fix every case of them in YOUR span, in every part,
not only the sampled ones. Read all of your span in the Dutch (Read tool, about 600 lines at a time) with the
guide beside it.

Check each part for:
1. WHOSE VIEW. A view Groen sets out in order to attack it (the revolutionary doctrine, an opponent, an
   author he quotes against) must not read as Groen's own claim, and the reverse. Say whose view it is, in
   the Dutch's own terms ("on the revolutionary principle...", "his opponents say...; Groen answers...").
   Where Groen praises and then criticises a writer, both must be there.
2. LOST QUALIFIERS. Where Groen limits a claim ("grootendeels", "nu en dan", "in menig geval", "ik laat
   daar of...") and the covers text states it flat or stronger, restore the limit. "Is bound up with" is not
   "caused".
3. LONG FOOTNOTES. A footnote or bracketed later note of about 10 lines or more that carries its own subject
   must be mentioned in covers in one short sentence ("A long note argues...").
4. A major subject or Groen's own stated stand in the part that covers does not mention.
5. SENTENCES over 25 words in covers or summary: split them. Aim 12 to 20 words. No added content.
6. NAMES: "line" must be the FIRST line in the part where the name appears (printed or OCR form).
7. FOOTNOTE PLACEMENT (rule, decided): a name or quoted author is listed under the part whose line range
   physically holds its lines, because the guide is keyed by lines. Where such a footnote belongs to prose in
   the previous or next part, ocr_notes must say so in plain words ("The note at 2180-2185 belongs to line
   2156, in the part before."). Make every such case consistent with this rule.
8. quoted_authors line ranges must cover only that author's words. A long quotation with no author named in
   the text is entered as {"author":"not named in the text","lang":...,"lines":[a,b]}.
9. Apply every finding of the review that falls in your span, unless the Dutch shows the reviewer is wrong
   (then say why in the change log). Do not move part boundaries, except where the review asks for it and the
   Dutch bears it out (keep parts contiguous: change the neighbour's end too).

Change only what these checks require. Leave sound text alone. Keep the JSON shape exactly.

Output:
- the corrected full guide JSON for your span, to the "out" path you are given;
- a change log JSON to the "log" path: [{"lines":[a,b],"check":1-9,"was":"...","now":"...","dutch":"the
  Dutch words and line that require it"}]
Reply with only: the two paths, the number of parts changed out of the total, and a count by check number.
