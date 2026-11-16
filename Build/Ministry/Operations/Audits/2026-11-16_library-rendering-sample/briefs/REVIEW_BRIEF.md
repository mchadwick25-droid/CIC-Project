# Brief: review every section of a finding guide against the Dutch

You are an independent reviewer. You had no part in writing the guide. No web, no model or API calls. Write
only your output file.

The book: /home/user/CIC-Project/cic/texts/groen-van-prinsterer_ongeloof-en-revolutie-nld_2e-uitg1868.txt
(G. Groen van Prinsterer, Ongeloof en Revolutie, 2nd ed., 1868; 19th-century Dutch; raw OCR with faults;
footnotes are set among the prose, often some lines after the text they belong to; line numbers are the
file's own, as the Read tool shows them).

The guide is "our guide to the contents, not a translation". It is at section level: 40 sections for the whole
book. Each section has: "lines"; "label"; "covers" (4 to 8 short sentences on what the section covers, plain
English at CEFR B2, no sentence over 25 words, Groen's statements reported as his claims);
"notable_footnotes" (long notes with their own subject, with lines); "scan_note"; "names" (names as printed
in the Dutch, each with the first line it appears on in the section; a corrected form may stand where the OCR
mangles a name the print makes clear); "quoted_authors" (authors quoted at length, language, lines).
A section necessarily leaves detail out. That is not a fault.

You are given the sections for one span of the book. Read the WHOLE span in the Dutch (Read tool, about 600
lines at a time), then check EVERY section:

1. Every statement in "covers" and "notable_footnotes": is it in the section, and is it right? Quote the
   Dutch for anything wrong.
2. WHOSE VIEW: is any view Groen sets out in order to attack (the revolutionary doctrine, an opponent, an
   author quoted against him) given as Groen's own, or the reverse? Is praise kept and criticism dropped?
3. QUALIFIERS: has a limit Groen sets ("grootendeels", "nu en dan", "in menig geval", "misschien") been
   dropped so the claim reads stronger than he wrote?
4. MAIN LINE: does "covers" give the main line of the section's argument and Groen's own stated stand? Flag
   only a real gap: a main division of the section, or a subject a writer would come looking for, that is
   absent. Do not flag missing detail.
5. Footnote line ranges in "notable_footnotes": right lines, right content, right author? Where the text
   says "among the footnotes at ..." give the exact lines.
6. "scan_note": true and useful?
7. Names: check every name that appears in "covers" or "notable_footnotes", and at least 12 from the "names"
   list chosen across the section: is it on the stated line, in printed or OCR form? Is it the first
   appearance in the section? Is a corrected form sound? Check every "quoted_authors" entry's author.
8. Boundaries: does the section begin and end at a real division of the lecture?
9. Style: any sentence over 25 words; wording a B2 reader would stumble on.
10. Outside knowledge: anything stated that the section itself does not say.

A finding is "substantial" only if something is wrong, unsupported or misleading about what the text says or
whose view it is, or a main division is absent. Everything else is "minor". Do not report taste.

Output JSON to the path you are given:
{"sections":[{"lines":[a,b],"verdict":"sound|minor|substantial",
  "findings":[{"check":1-10,"severity":"substantial|minor","detail":"with Dutch line(s) and words","fix":"exact corrected wording or value"}],
  "corrected":{"label":"...","covers":"...","notable_footnotes":"...","scan_note":"...",
               "name_fixes":[{"name":"...","line":N,"action":"set_line|rename|remove|add","new_name":"...(if rename)"}],
               "quoted_author_fixes":[{"author":"...","lines":[a,b],"action":"remove|replace|add","new":{"author":"...","lang":"...","lines":[a,b]}}]}
 }],
 "overall":"2-4 plain sentences"}
"corrected" must give the FULL final text of label, covers, notable_footnotes and scan_note for the section
with all your fixes applied (repeat them unchanged if sound), keeping to the guide's rules above: 4 to 8
sentences in covers, none over 25 words, Groen's views as his claims, nothing the section does not contain.
Reply with only: the path, the verdict count, and one line per substantial finding.
