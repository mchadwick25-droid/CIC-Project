# Handover: Library era 10, after batch 1 (2026-11-15)

Written by the era 10 Library thread (session_01JMNsSAqz5MpXueLhCgHP2f) at the end of batch 1, for a fresh session.
The coordinator is session_01JMNsSAmN1HUCBWPQWS4gro (the Church Family Tree coordinator). Read `CLAUDE.md` first.

## Where things stand

- Batch 1: 94 files, 10,208,969 words, branch `claude/library-era10-majors`. Records: `CFT-Wants.md` ("Era 10 ...
  batch 1"), `Decision-Log.md` (last entry), `Search_Log.md`, `R1_review.md`, `R1_changes.md` and the round 2 recheck
  in this folder.
- Rights: Mark's rulings R1 to R11 (`Decision-Log.md`, "Era 10 rights rulings") and R12 (the batch 1 entry). Calls made
  in batch 1 are in the Search_Log's table: the dictionary of African biography is CC BY-NC and is cite and link; the
  Catholic Worker is "Original paper scans only"; a year printed only inside the work's title is taken on the
  coordinator's conditions; a permission notice on a library film means "held for Mark".

## How batch 1 was run

1. Searchers: Sonnet subagents, one scratch directory each, a written brief (the rights test, the allowed commands,
   the spec to hand back). They searched archive.org by title, author and year, read title pages, and downloaded the
   djvu.txt with a byte-count check.
2. This thread checked every pick: title page (the page image where the OCR was unclear:
   `https://archive.org/download/<id>/page/n<k>.jpg`), rights fields, dates.
3. Renewal searches (R7): the Stanford database by its web search, and a local copy of the NYPL `cce-renewals` data
   searched as text. Both, every time.
4. Strip pass by script (Google's preamble, the Internet Archive notice, "Digitized by" marks, the Cornell scanning
   notice), with the removed lines counted in the header and a list kept so line numbers can be re-derived.
5. Mappers: Sonnet subagents read each stripped file and gave the title-page words, the parts and the wanted
   passages by line number.
6. One curated table per group held what the title page and host record give. A script joined it with the maps and
   wrote the file, the registry entry, the queue row and the staging file from one spec.
7. Review: one fresh Fable subagent, read and grep only, then a targeted recheck.

What bit:

- A scan can carry a permission notice on a film target (Loisy 1902). Grep every file for "permission" before vendoring.
- Later printings hide behind a copyright line: a ZIP code or "Twenty-eighth printing" in the publisher's address
  (Larkin); "Copyright 1930, 1945" (Houteff volume 1); "Special Edition Copyright 1993" (one Scopes scan).
- The bound volume of a periodical can garble what the single-issue scan reads cleanly (the Korea Mission Field).
- Mapper notes inside part headings must not reach a header.
- Never write an office, a date or "first" from memory. The review caught "first issued from 1910 to 1915".
- `texts_registry.py --write-readme` and `--check` each take several minutes on the full corpus. Run them in the
  background.

## Batch 2, proposed

Search first; these rows have no held source (the reasons are in `CFT-Wants.md`, "wanted rows not filled"):

- **Africa.** William Wadé Harris, Kimbangu, the Aladura founders, Kivebulaya, Spartas, Luwum and the Revival people.
  Try: mission periodicals to 1930 by issue (the Church Missionary Review, the Journal des missions évangéliques, the
  Baptist Missionary Society's Herald, Congo Mission News), colonial yearbooks, and African-language prints. Located
  and left for the era 9 thread: Lloyd, Dayspring in Uganda (1921); Mullins, The Wonderful Story of Uganda (1904).
- **Oceania.** Rātana: Papers Past refuses automated clients. Māori and Pacific hymnals of 1896-1918 were located and
  not checked (identifiers in the Search_Log).
- **The Orthodox and Oriental churches.** The 1918 Definitions and Acts of the Moscow council; Tikhon; Balakian in
  Armenian; Kyrion II; the encyclical of 1920; Serbian, Bulgarian and Georgian prints; Habib Girgis in Arabic; the
  Malankara prints of 1912 (Malayalam monthlies located, unchecked); Etchmiadzin 1918-1919 (located, unchecked).
- **The Catholic Worker.** More original scans of the paper (Mark: "Original paper scans only"). One issue is held.
- **Council leads not yet searched.** The Lviv Sobor of 1946, Belhar, Puebla and the like are cite and link (R4); the
  Lambeth Conferences of 1968 and 1998 are after 1930. A cite-and-link register may be all the Library can give.
- **A hand-fetch list for Mark.** HathiTrust refuses automated clients (a site-side block, not a settings step); Mark
  fetches by hand. List each wanted item with its exact URL and edition: The Apostolic Faith (Los Angeles, 1906-1908;
  pentecostalarchives.org, whose owner's terms say personal research only: held for Mark); Fosdick's sermon in The
  Christian Work; Larkin's Dispensational Truth in a printing to 1930; Bartleman 1925; Penn-Lewis; Blair's Korea
  Pentecost in a dated printing; Te Whetu Marama on Papers Past; the 1918 Moscow Definitions on prlib.ru.

Batch 3, proposed: the remaining non-major people, mostly American books of 1931-1963 tested for non-renewal under R7
(Adventist, Churches of Christ, Oneness, the Black church).

## Open with the coordinator

- Bultmann's Jesus (1926) rests on a dated afterword with the catalog date agreeing; R12 names a preface.
- The eleven files taken on the coordinator's call (a year only inside the title): Mark may overrule.
- Whether the living marks after 2010 (Open-Gaps 162) are the Library's.
- A second independent rendering (R11) will be needed for the Latin held with no old English: Mortalium animos,
  Sacrorum antistitum, the homily to the Chinese bishops, Ab ipsis, Iniquis afflictisque.
