# Brief: a section-level finding guide (Groen van Prinsterer, Ongeloof en Revolutie, 2nd ed. 1868)

A detailed finding guide to this Dutch book already exists: about 200 small parts, each read twice against
the Dutch. The project lead has ruled that finding guides are to be at chapter or section level: about 20 to
40 parts for the whole book. Your job is to write the section-level guide for some of the book's units from
the detailed guide you are given. You do not read the Dutch; an independent reviewer will check every section
you write against the Dutch afterwards. No web, no model or API calls. Write only your output file.

## Sections
- A lecture gets TWO sections, or THREE if it is long or has three clear main divisions; never more.
  Follow the lecture's own main divisions (its numbered points). The preface gets one or two. The title page
  and the note on the second edition together are one section. The contents list and the register together
  are one section.
- A section's line range must start and end on existing part boundaries (start of some detailed part, end of
  some detailed part), be contiguous with its neighbours, and stay inside one unit (except the two joined
  cases above).

## For each section write
- "unit": the unit name as given (e.g. "Lecture VII"), "title_as_printed": as given.
- "lines": [start, end]
- "label": 3 to 8 plain words (ours).
- "covers": 4 to 8 short sentences on what the section covers, so that a writer who reads no Dutch can tell
  whether the passage they need is here. Plain English, CEFR B2: sentences of 12 to 20 words, none over 25,
  active voice, concrete verbs, no filler. Report what Groen says as his claim ("Groen argues...", "He
  says..."), never as fact.
- "notable_footnotes": 0 to 4 short sentences naming long footnotes or later bracketed notes that carry
  their own subject, each with its lines ("A long note at 7680-7717 argues that..."). Empty string if none.
- "scan_note": one or two sentences if the detailed parts flag something a user must know (a garbled run, an
  unreadable date or name, with lines). Empty string if nothing matters at this level.
Do NOT write names or quoted authors: those are merged by script from the detailed parts.

## Hard rules (the faults the first review found; do not reintroduce them)
- WHOSE VIEW: a view Groen sets out in order to attack (the revolutionary doctrine, an opponent, an author
  quoted against him) must never read as Groen's own claim. Say whose view it is. Where the detailed parts
  give both Groen's praise and his criticism of a writer, keep both.
- QUALIFIERS: keep Groen's limits ("largely", "now and then", "in many cases", "he does not say whether").
  Do not strengthen a claim when you shorten it. "Is bound up with" is not "caused".
- Claim nothing the detailed parts do not say. No outside knowledge about Groen, his sources or the history.
  Names, dates and places as the detailed parts print them (Dutch forms: "Lodewijk XIV", "Frankrijk").
- You must choose what to leave out. Leave out detail, never the main line of the argument and never Groen's
  own stated stand.

## Output
JSON to the path you are given: {"sections":[{...}, ...]} in book order. Reply with only the path, the number
of sections per unit, and any doubt you had.
