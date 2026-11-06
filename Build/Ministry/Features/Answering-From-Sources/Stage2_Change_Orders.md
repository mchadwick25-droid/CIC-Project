# Stage 2 change orders (Library thread)

Companion to `Decision-Log.md`. Each change order names what it changes, its
number, and how it keeps Mark's standing constraint (entry 4): every passage and
its fields stay linkable, so a click-through can show the full page description
and link to the source reference and the vendored document, and no corpus-map or
repin change drops a source a reader can reach today. The Library design (D3) is
frozen; these are the changes to it. The runtime seal and the review unit are
filed with stages 3 and 4.

## CO-S2-1. Row fields in the corpus map (shelf-row authority)

Changes: `cic/engine/corpus_map_merge.py` keeps, besides its eight row fields,
`locus_ids`, `voice_of`, `documented_exchange`, `language` and `date` (a window
with its source and a formation confidence from the five-level vocabulary).
`corpus_map.validate()` checks their shape. The staging files carry them as
additive keys today and the merge drops them until this change lands. A work's
facts live on its row; a world's source record points at the row by `shelf_row`
and keeps only what is the world's own.

Number: for lpc, every row has `language` and `locus_ids` (or an explicit
`unknown` with what was checked); every non-tradition row has `voice_of`; every
`date` carries a source and a confidence; none is guessed.

Keeps transparency: nothing is removed from any row or record. The pointers are
added; the duplicated record fields (author, work, edition, citation) are listed
per world and stripped only by a later change order, never in this one.

## CO-S2-2. Passage index scope

Changes: a derived passage index over the union of the twelve shelves (338
files), built by `Sandbox/answering-library/`, outside the live and canonical
trees, rebuildable, versioned by a hash of the passage hashes, the curation
files, the pipeline code and the model id (none). Each passage record carries
`passage_id`, `file`, `division_locus`, `division_title`, `ordinal`, `text`,
`byte_start`, `byte_end`, `language`, `script`, `apparatus`, `speaker`,
`ocr_score`, `row_ids`, `worlds`. The index holds no context lines until a later
change order fills them.

Number: 0 passages fail the byte-span check; passage words plus suppressed page
furniture equal the file's words for every plain-text file.

Keeps transparency: every hit returns the vendored file path and byte span next
to the passage, so mark, hover and click-through each reach the source.

## CO-S2-3. Segmentation classes, curation, speaker and OCR floors

Changes: a file's class is `clean`, `partial`, `none` or `curated`. A curated file
has a per-file curation file under `Sandbox/answering-library/curation/` that
uses the edition's own citation scheme and passes the checker. Until a file is
curated its citation addresses stay at the division level and the card says so.
The speaker field is `known`, `mixed` or `unknown`; unsure means `unknown`. A
passage scoring below 0.70 on OCR can be cited and shown on the card but not
spoken as a quotation; below 0.50 it does not enter retrieval.

Number: all 66 lpc partial or unmarked files are curated or listed with the
reason they cannot be; a sample of each wave is read by Opus; lpc rows carry the
new row fields (CO-S2-1).

Keeps transparency: curation never edits the vendored file; it only decides where
divisions start. A failing curation falls back to the heuristic class and keeps
its divisions.

## CO-S2-4. `voice_of` is set only where a party is ruled

Changes: the Number line of CO-S2-1 ("every non-tradition row has `voice_of`") is replaced. `voice_of` is set only where a party is ruled in `PAIRS.yaml` or a census movement is clearly the voice of the work. A non-tradition row with no `voice_of` is outside the world's own voice: it stays citable and labelled, and is never spoken as the world's own.

Authority: Mark's own ruling, 2026-10-31, relayed by coordination. Raised by the lpc row-fields work: `PAIRS.yaml` rules only the fixture party, and none of lpc's 47 non-tradition rows (modern scholarship, translations, the Gesta, Codex Theodosianus, Prosper) is clearly one movement's voice.

What the code does with an unset `voice_of` (checked 2026-10-31):
- `cic/engine/corpus_map.py` treats `voice_of` as optional and checks only its shape when present, so an unset row validates.
- `engine/m9/confinement.py` (`gate_voicing_pair`): an emic citable record that cites a non-tradition row with no `voice_of` is a finding ("the row carries no voice_of"). Unset therefore already reads as not voiceable; the unset rows can be cited only where the record is not emic.
- `engine/m9/shelf.py` carries `voice_of: None` through unchanged.
- `engine/m10/quotes.py` runs its mixed-voice speaker check only on files that have at least one row with `voice_of`. A file whose rows are all unset gets no speaker check from that gate. This is a gap in the check, not a change made here.

Keeps transparency: no row loses a field; the 47 rows stay on the shelf with their role and confidence.

## CO-S2-5. `translator` and `edition_date` on the shelf row (OG-140)

Changes: `cic/engine/corpus_map.py` gains two optional row fields, kept by the merge like the others. `translator` is a mapping `{name, source, formation_confidence}`, where `name` is the translator as the vendored file prints it (for a Latin edition, its editor) and `source` is the file and line that state it; `edition_date` is `{year, source, formation_confidence}`, the year the vendored file states for the edition it holds. Either may be `{formation_confidence: unknown, checked: "<where it was looked for>"}`. Confidence is one of the five formation levels; "Documented" only where the file states the fact in so many words. Nothing is filled from memory.

Why: the quote card's second layer (template B, Decision-Log 52) shows the edition's words with their translator and date, and the source records carry only free-text `edition` and `citation`. The work's facts live on its row (CO-S2-1), so the fields go on the row, and the card reads them through the row the source record already points at.

Number: every lpc row cited by a quote or term record carries both fields, set or `unknown` with where it was looked for; none is guessed.

Keeps transparency: nothing is removed from any row or record; both fields are additive.

Authority: coordination relay of 2026-11-01 after Mark chose template B. The shape of the two fields is the Library thread's reading of that request and is open to change.
