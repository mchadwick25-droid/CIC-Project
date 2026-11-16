# Brief: finding guide for one span of Groen van Prinsterer, Ongeloof en Revolutie (2nd ed., 1868)

The file: /home/user/CIC-Project/cic/texts/groen-van-prinsterer_ongeloof-en-revolutie-nld_2e-uitg1868.txt
It is raw OCR of the Dutch print (19th-century spelling; OCR faults such as "cn" for "en", "lot" for "tot",
page numbers and running heads mixed into the text, footnotes set among the prose). Line numbers are the
file's own lines (as the Read tool shows them). Do not edit the file. Do not use the web. Make no model/API calls.

You are given a line span. Read ALL of it (Read tool, in pieces of about 600 lines). Then write a finding guide
for that span as JSON, to the output path you are given.

## What a finding guide is
"Our guide to the contents, not a translation." A writer who reads no Dutch uses it to find where the book
treats a subject, and what it names there. It goes part by part.

## Parts
- The top-level units are the book's own: title page, the note on the second edition, the preface
  ("Voorrede"), each numbered lecture, the contents list, the register.
- Within each lecture or the preface, divide into parts following the argument's own turns (the print's
  numbered points, "a." "b." heads, clear changes of subject). A part is typically 40 to 200 lines. Parts must
  be contiguous and cover the whole unit with no gaps and no overlap: each part's start = previous end + 1.
- A part starts on the first line of its prose (or the heading's first line) and ends at the last line before
  the next part begins. Read both ends in the text.

## For each part write
- "lines": [start, end]
- "label": 3 to 8 words, a plain descriptive label (ours).
- "covers": 1 to 4 short sentences on what the part covers. Plain English, CEFR B2: short sentences
  (12 to 20 words), active voice, concrete verbs, no academic filler, no "delves", no em-dash chains.
  Report what Groen says as his claim ("Groen argues...", "He says...") not as fact.
- "names": the persons, books, events, places, dates and Bible references the part names, AS PRINTED in the
  Dutch (keep the Dutch spelling, e.g. "Lodewijk XIV", "Bilderdijk"; if the OCR has mangled a name and you are
  sure what it prints, give the corrected form and put the OCR form in "ocr_notes"). Give each with the line
  where it first appears in the part: [{"name": "...", "line": N}]. Only names really in the part.
- "quoted_authors": authors whose words Groen quotes at length in the part (often in French, German, Latin or
  English), with the language and the lines: [{"author": "...", "lang": "fra", "lines": [a,b]}]. Empty if none.
- "ocr_notes": optional; anything a user must know (a garbled run, a footnote block and its lines).

## Hard rules
- Claim nothing the part does not contain. If you cannot make out what a passage says because of the OCR,
  say so in ocr_notes; do not guess.
- No outside knowledge: nothing about Groen, his sources, or history that the part itself does not say. Do not
  identify an unnamed person. Do not expand an abbreviation unless the text itself does.
- Names, dates, places as printed.
- Every line number you give must be checked: the name must be on that line.

## Also nominate passages
In "candidates", list up to 4 self-contained passages (8 to 30 lines each) in your span that a writer of a
profile of Groen would most want rendered into English: above all (a) a statement of the book's thesis,
(b) a passage on the Reformation ("Hervorming"), (c) a passage on the Revolution or on unbelief as its
source. Prefer passages where the OCR is clean and that are Groen's own Dutch (not a quotation from another
writer). For each: {"lines":[a,b], "kind":"thesis|reformation|revolution|other", "why":"one sentence",
"ocr":"clean|minor faults|rough"}. Give none if your span has nothing apt.

## Output JSON shape
{"span":[a,b], "units":[{"unit":"Lecture III", "title_as_printed":"ANTI-REVOLUTIONAIRE BEGINSELS",
  "lines":[a,b], "summary":"2 to 3 sentences on the whole unit, same B2 style",
  "parts":[{...}, ...]}], "candidates":[...]}
Write valid JSON (UTF-8) to the output path. Then reply with only: the path, the number of units and parts,
and any problem you met. Nothing else.
