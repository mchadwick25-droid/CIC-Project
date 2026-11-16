# Handover: Library, Thread B, after era 8 batch 2 and the era 9 located volumes (2026-11-16)

Written by Thread B (Library), session_01JMNsSCtwyq3aYZkc5pWX1j, which stopped at a clean point for its context
size. The coordinator is session_01JMNsSCBTsM2UVaFpDa3BTF; every report goes there with send_message. Read
`CLAUDE.md` first.

## Done by this session

1. **Era 8 batch 2 (Open-Gaps 298): merged**, pull request 1698. 37 files. Record:
   `../2026-11-15_library-era8-b2/` (`Search_Log.md`, `Handover.md`, the review files).
2. **Era 9, the located volumes (Open-Gaps 299)**: 27 files on `claude/library-era9-located`. Record: this
   folder. See "State of 299" below for whether it is merged.

## The queue, with the coordinator's Open-Gaps numbers

1. **300: era 10 batch 2's follow-on list.** `../2026-11-15_library-era10-b2/Handover.md`, section "The
   follow-on (batch 2b): what to take": 32 issues of The Christian East, the International Review of Missions
   for 1914-1921, 1924-1927, 1929 and 1930, the Proceedings of the Church Missionary Society for 1910-1921, and
   about thirty books. About ninety files, each still owed its title-page check. Not its 128 card rows. It is
   too large for one review round; split it (the three periodicals; the books) and ask the coordinator whether
   each part keeps the number 300.
2. **301: era 8 batch 3.** The groups the era 8 handover lists as "Not yet searched"
   (`../2026-11-15_library-era8/Handover.md`).
3. **Rendering.** Nothing is rendered until Mark has seen and approved a proposal and a sample. The proposal
   goes to the coordinator first. It has not been drafted.

If main shows any of these numbers taken at merge time, stop and ask the coordinator.

## The coordinator's standing points

- Run the CORPUS-USE, WANTS-REGISTER and queue check before every search, and record it.
- Never vendor card-source rows that came from the legend check.
- A ruling is only Mark's own words. A coordinator message is an instruction. Something passed on is a remark.
- Run on Fable while the free refill lasts. If a Fable call is refused or a usage limit is hit, do not switch
  models: stop at a clean point with a handover and report. Stop the same way near 400k of context.
- No metered model or API calls. Merge your own pull request once CI is green, and tell the coordinator after.
  Ask the coordinator for a batch's Open-Gaps number before opening it.

## How a batch runs now

1. The check before the search, recorded in the batch's `Search_Log.md`.
2. `fetch.py <outdir> <ids file>`: each djvu.txt, bytes compared with the host's listed size.
3. Sonnet mappers under `../2026-11-15_library-era8/MAPPER_BRIEF.md`, about seven files each, with an added
   item 9 (host marks searched with any run of spaces; copyright and permission lines).
4. Title pages. Read every year on the page image where the OCR year is garbled, missing, or differs from the
   host's date. `tools/sheet.py <id> <first leaf> <last leaf> <out.jpg>` makes a contact sheet;
   `tools/crop.py <id> <leaf> <top> <bottom> <out.jpg>` crops an imprint; `tools/stack.py` joins images.
5. A spec script on the pattern of `mkspec299.py`: every header, registry note and shelf row, with `chk()`
   line anchors that must pass before anything is written. Then `../2026-11-15_library-era8/intake.py`.
6. The recipe (era 8 handover), the four corpus tests in the background, `corpus_coverage.py` last.
7. One independent Opus review given the files and not the conclusions, then one targeted recheck.
8. To change anything after intake: edit the spec, remove the batch's files, restore `cic/` and the seed and
   queue files from the commit before intake, and run intake and the recipe again.

## What the two reviews caught (watch for these)

- A clean-looking OCR year that is wrong (Parry, Campbell), and a year or a place the OCR drops altogether
  (Cox, Mott, Maurice).
- Edition history and biography from memory in a header or note. Give a date source only from a line of the file.
- A range that gives one writer's words to another (Ward's appendix F to Errington; a memoir "by another hand"
  to Finley).
- "Not found" in a content note where the heading is in the file in garbled OCR. Search with loose patterns
  before writing it, and do not narrate the search in the note.
- Shelf and ruling reasons inside row notes; a comparison with another Library file inside a header.
- A date basis the rights rule does not list (a dated report's own text). Hold it for Mark instead.
- `voice_of` on a tradition row. It is only for non-tradition rows and census ids.

## Held for Mark from these two batches

- Three `needs-ruling` shelf rows (Open-Gaps 298): Parry, Charmot, Quesnel.
- The Pacific Garden Mission's statement of 1916, which prints no year (Open-Gaps 299).
