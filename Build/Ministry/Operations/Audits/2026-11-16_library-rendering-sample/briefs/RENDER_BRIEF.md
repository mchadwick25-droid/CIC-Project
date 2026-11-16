# Brief: render three Dutch passages into modern English

Source: /home/user/CIC-Project/cic/texts/groen-van-prinsterer_ongeloof-en-revolutie-nld_2e-uitg1868.txt
(G. Groen van Prinsterer, Ongeloof en Revolutie, 2nd ed., Amsterdam 1868; raw OCR; 19th-century Dutch spelling.)
Read only this brief, that file, and the page images named below. Open no other file in the scratchpad.
No web. No model or API calls. Do not edit the source file.

## The passages (the file's own line numbers)
- P1: lines 6941-6951. Page image: <scratch>/img/p167.jpg
- P2: lines 6837-6850 (ends at the closing quotation mark of the prophecy, before the dash).
  Page image: <scratch>/img/p164.jpg
- P3: lines 10547-10562. Page image: <scratch>/img/p260.jpg
(All images are in the same img folder.) The OCR has faults ("hel" for "het", "heelt" for "heeft", and worse).
Where the OCR is faulty, read the Dutch on the page image. The print's footnote mark after "mensch" in P2 is
not part of the passage. You may read a few lines either side in the file for context; render only the passage.

## The bar
- Translation, not summary. Every clause of the Dutch is present in the English. Nothing is added: no gloss,
  no explanatory word, no bracket. Nothing is compressed away.
- One thought per sentence. You may split a long Dutch sentence into several English ones, keeping the order
  and the logic (its "because", "so", "but").
- No sentence much past 25 words.
- No word whose modern sense misleads. Choose the English word a present-day reader will take in the sense
  the Dutch had in 1868. Plain modern English; no archaism, no inflation; keep Groen's own images
  (plant, poison, circle, and so on) and his force.
- Keep his emphasis where the print has italics only if English can carry it without adding words.
- A Bible quotation inside a passage is rendered from the Dutch as printed, not replaced by an English Bible
  version's wording.
- "Revolutie" with the capital is "the Revolution"; "Omwenteling", "Hervorming" and "Reformatie" are distinct
  Dutch words: decide how to treat them and say what you did.

## Output
Write JSON to the output path you were given:
{"passages":[{"id":"P1","dutch_reading":"the Dutch as you read it, with the page image settling OCR faults",
  "ocr_faults":[{"line":N,"ocr":"...","print":"..."}],
  "english":"your rendering",
  "choices":[{"dutch":"word or phrase","english":"what you chose","why":"one sentence, incl. any real doubt"}]},
 ...]}
In "choices" list every place where you hesitated between meanings or where the Dutch is open to two readings.
Reply with only the path and one line per passage on any doubt you had.
