# The Church Family Tree stage two kit

Stage two begins once a brief has passed its brief review and its one revision. The Brief Kit (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`) stays as it is, and its steps 5 to 8 (card, final check, release, recording) run as written. This kit says what each card must now hold, and how recording and release are judged; where the two differ, this kit governs stage two.

## 1. The card: one layout for every kind

A tradition, a person, a council and an era share one layout.

1. **On screen first:** a short description, the direct line, then the player.
   - The short description is one or two sentences, written fresh at the card step and checked like the brief.
   - The direct line goes one step each way, showing up to three, then "and more" into Connections. Tapping it opens the Family line view on the map.
2. **Below:** the brief's text, closed but openable (Read along), and open where there is no current recording. Under the text, a short list of the old sources the brief draws on.
3. **Then the menu, in this order:** Timeline; People and stories (the people first, then the documented stories, each a full story to listen to); the kind's own sections (Key works for a person, What happened for a council); Connections; Legacy and today; Open questions; Sources, with the Modern works reading list kept apart.

## 2. The timeline

1. It holds every component of the subject in time order (events, acts, writings, rules, quarrels, what came of them): a map of progress and events, not storytelling.
2. It is made after the brief, so it never shapes the brief, from all the research: the source sheet, the outline, the census entry and the card, documented stories included.
3. A line is dated where the old sources fix the date or it is Widely Accepted. Otherwise it says "date unknown", or gives the record's own phrase ("in Callistus's time"), and sits where it naturally falls in the sequence.
4. Every line carries its reference directly after the point.
5. Lines are grouped in periods, each with a date and a one-line headline, closed until opened, with a control to open them all. Where one witness carries a period, that witness is named once at its head; a line keeps its own note only where it differs: a wonder, a contested point, a much later source.
6. The card writer, on Sonnet, builds it; the card checker, on Opus, checks every line and headline against its source, by the card list in `Brief-Kit/roles/final-check.md`.

## 3. Dates and names on the card

- An entry's `start`, `end` and `activeYear` only place it on the map. Its shown `dates` and the card's `datesNote` follow the Brief Kit's date rule.
- An other name is a plain string or `{name, note}`. Search shows the name only, and a note carries no brackets of its own.

## 4. Recording

- **Tradition, council and era briefs:** Daniel, `onwK4e9ZLuTAKqWW03F9`, `eleven_multilingual_v2`, `mp3_44100_64`, `{"stability":0.95,"similarity_boost":0.68,"style":0,"use_speaker_boost":true}`, every setting passed on the command (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Recording_Settings.md`).
- **Person briefs and documented stories:** not recorded until Mark names a new voice.
- **Every run:** capped under 25,000 credits, in Mark's own words, with a sample for his ear first. The run prints its settings and counts before it starts, and the paragraph times are remade after it.
- **Old recordings stay until replaced:** no recording of a brief, a person or a story is removed until its new recording is made, and the new one replaces it. On the built worlds, recordings that do not fit the new card structure are removed, once Mark has seen which.

## 5. When a piece, and an era, is done

- A text passes at grade C or better. It is graded by the readers of `Build/Ministry/Operations/Audits/2026-11-25_tradition-grades/` and `Build/Ministry/Operations/Audits/2026-11-25_person-council-grades/`, scored on the whole text by `Build/Ministry/Operations/Audits/2026-11-28_era1-new-grades/grade_whole.py`, each finding weighed by its size against the Brief Kit's bar. Exactness that misses the heart weighs nothing; a large fault still fails. Reading level is judged names out. Every new or rebuilt text gets a grading run by that method, and passes at B or better, or with Mark's sign-off.
- An era is complete when its traditions, people and councils pass, with its era brief and every card in the new layout, timeline included.
