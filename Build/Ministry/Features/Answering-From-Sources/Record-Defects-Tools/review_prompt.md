You are an independent Opus reviewer for the CIC-Project (you did not draft or render any of these records). Work only in the repo checkout at REPO. Read-only on everything except the ONE review file you write. Make no model API calls, no network fetches, no git commands that change anything (no commit, no push). Keep any scratch scripts in your own folder, /tmp/claude-0/-home-user-CIC-Project/618d9b9d-56aa-5bcf-8a39-70f880fbd66a/scratchpad/rv_WORLD_N/ (create it); other reviewers run in parallel and must not share files with you.

TASK: review the `modern_rendering` of each record id listed in IDS_FILE (one id per line), against the record's `text` AND against the edition text read from the vendored file in REPO/cic/texts/ at the record's locus. Records live at REPO/records/WORLD/quote/<id>.md (YAML front matter). Never review from memory; read the vendored lines.

For each record:
1. Locate the passage. The locus in `sources[].locus` names a work, a section, and often "file lines N-M" with a short file tag (e.g. "npnf211" = cic/texts/npnf211*.xml). If no file or lines are given, find the passage in the vendored file for that work (grep a distinctive phrase from `text`; cic/texts/REGISTRY.yaml and cic/corpus-map/ help map works to files). Record the exact file and the tight line span (first line holding the quote's first word to the line holding its last word).
2. Text check: does the record's `text` occur verbatim in that span (strip <note>…</note> and tags in XML, rejoin line-end hyphens, fold whitespace incl. U+00A0; "..." in the text marks an elision)? Report pass / FAIL with the differing words. Do NOT fix anything.
3. Rendering check, the project bar (CLAUDE.md): every clause of the edition text rendered; nothing added (no new claim, name, number or sense); one thought per sentence; no sentence past about 25 words (count them); no word whose modern sense misleads; the source's own hedges and reported-speech frames kept (e.g. "it is said", "as I think", "they say"); readable (plain modern English, BBC/National Geographic register, CEFR B2). Check it against `confidence.divergence_note` and `use_note.not_for` too, where they bear on the rendering. Minor stylistic preferences are NOT failures; fail only for something wrong, missing, added, misleading, or over-length.
4. Verdict: PASS, or FAIL P1 (meaning wrong, added or dropped, hedge lost) / FAIL P2 (misleading word, over-long sentence, two thoughts joined). For every FAIL give a corrected rendering that you author yourself to the bar above, built from the edition text (every clause, nothing added, sentences <= 25 words).

WRITE exactly one file: REPO/Build/worlds/WORLD/Review-Artifacts/OUTFILE, in this shape (Markdown):

# Rendering Review: WORLD quote records, batch N (K records)

- **Reviewer:** Opus 5.5 (independent; did not draft or render any of these records)
- **Date:** 2026-11-03
- **Subject:** the `text` and `modern_rendering` of K `WORLD.quote` records.

## Method
(short: how text was checked, how sentence lengths were counted, sources read)

## Results
**K records: X PASS, Y FAIL (a P1, b P2).**

| Record id (WORLD.quote.…) | Edition text at (file, lines) | Text check | Rendering check | Verdict |
|---|---|---|---|---|
| short-id | cic/texts/file.xml, lines N-M | pass | one short phrase of what you checked (e.g. "all clauses; 'x' follows y; longest 22") | PASS |

## Failed renderings: corrected text
For each FAIL: the record id, the finding in one or two sentences, and "Corrected rendering:" followed by your full corrected rendering in a block quote.

Rules: every row's first cell is the short id (record id without the "WORLD.quote." prefix) and must appear exactly as the id. Use plain present tense; no talk of rounds or other reviews. Do not edit any record. Do not invent a quote, a locus or a rendering detail; if you cannot find a passage in the vendored files, say so in the row ("passage not found in vendored files") and verdict FAIL P1.

When done, reply with only: the counts line, and the list of FAIL ids with their severity.
