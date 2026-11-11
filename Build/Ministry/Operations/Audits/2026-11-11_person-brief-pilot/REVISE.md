# Round-1 revision (read all; BRIEF.md still governs)

Reviews: review/R1_set1.md and review/R1_set2.md (under the pilot dir). Fix every BLOCKING and STANDARD finding for your people. Overwrite `<id>.txt` and update `<id>.notes.md` (add a "Round-1 changes" list: finding → what you did). Re-verify every new claim and the quote in the file.

## Witnesses
Modern translators, editors and introducers (Robertson, Schaff, Gwynn, Clarke, Moore, Wilson, Browne, Swallow, Clark, Foster, Calder, Percival...) are NOT story witnesses. Tell the point through an ancient or contemporary witness (Eusebius, Socrates, Sozomen, Theodoret, Palladius, Jerome, Photius, Gregory himself...) or, where the file documents it plainly, tell it directly (the source stays in the notes), or drop it. Where only a later writer is our source for a point and it matters, say so in story terms without abstract roles ("the story comes to us only from much later").
Don't let "X says" become a citation list: name the witness where it matters (a hostile, partisan, lone or disputing account), and otherwise just tell the story.

## Shape (coordinator's research guidance; Mark's standard wins where they differ)
- Open inside ONE sourced scene that is the way into what they stood for — not "X was born in...". First 15 seconds decide whether the rest is heard.
- Beats: a moment → who and when → the question they fought for or built, and what was at stake for ordinary believers → the cost or turn, with the theology running through the event → one contested point if material (who says it, why it's doubted) → WHAT REMAINED (legacy).
- LEGACY beat carries real weight (about 15–25 seconds for the major figures): concretely who took up their work, what in later belief or practice traces to them, how different traditions remember them (honored, disputed, condemned). Every claim sourced; influence that is argued, not shown, is said to be argued. Never "his legacy lives on". End on a concrete image or their own voice.
- For the ear: one or two natural time anchors ("around the year two hundred"); at most three proper nouns per sentence; repeat the name rather than an unclear "he"; mark turns ("But", "Years later"); no parentheses, no lists of works.
- Three registers for uncertainty: the sources agree / one early source says, and others doubt it / later tradition says. Weakly attested vivid stories go on the card, not in the audio.
- Length: Origen, Athanasius, Chrysostom about 290–330 words (Mark: "it's ok if they run long"); others 200–270 as sources allow. Band still FK 8–10, FRE ≥ 60 (score.py).

## Also write `<id>.card.json` (person card; every field sourced in the notes; a field with no source is null, never filled):
{
 "known_for": "one sentence, ~20 words, what they did",
 "role": "a few words",
 "key_works": ["up to 3 short titles"],
 "legacy_traces": ["2–3 sourced lines: ideas, practices, works taken up later, and by whom"],
 "legacy_remembered": ["1–3 lines: honored / disputed / condemned, and by whom, in terms each tradition would accept"],
 "uncertain": ["1–2 lines, same words as the audio where the audio states it; card-only weak stories go here, as the witness's account"],
 "written_about": [{"title":"", "author":"", "date":"e.g. about 325", "language":"English translation / Greek ...", "file":"cic/texts/... "}]
}
`written_about` = the sources about them that the brief and card rest on (not their own works). Dates of those works only where the file states or the entry documents them; otherwise null.
Census context (each person's `legacy`, `floorNote`, `sourcing`, `voices`) is in entries.json; you may draw on it but verify against files.

Origen specifics: tell the break with Demetrius as the reason for Caesarea; the self-castration goes on the card as Eusebius's account (not the audio); check where he died (Tyre?) in the files; make 553 and Decius placeable by ear ("the emperor Decius", "three centuries later, a council at Constantinople").
