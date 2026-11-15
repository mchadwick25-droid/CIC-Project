# Handover: Library era 8, batch 2 (2026-11-15), from Thread B

Written by Thread B (Library), session_01JMNsSE8iywJ4uqhmGsoKp2, which stopped near its context limit. The
coordinator is session_01JMNsSCBTsM2UVaFpDa3BTF; every report goes there. Branch: `claude/library-era8-2` (main
merged in at 10bfcc62). No pull request is open. **Nothing of batch 2 is vendored yet.** The Open-Gaps number the
coordinator gave for this batch is 298. Read `CLAUDE.md`, then
`Build/Ministry/Operations/Audits/2026-11-15_library-era8/Handover.md` (the recipe, the tools, the candidate
tables), then this file.

## Scope, as the coordinator set it on 15 November

- Batch 2 is the era 8 handover's two unspent tables ("British Isles and Methodists", "North America and Catholic
  Europe") and its list "Found by batch 1 and not vendored".
- The era 8 rows of the "Texts to fetch, by era" card list are not taken. The coordinator dropped that list for
  every era, passing on Mark's direction of 2026-11-15: "we dont need to build out more legends we need to make
  sure the who and counsils are drawing from their own sources not sources writen 1000 years later".
- Work only on texts the Church Family Tree needs; where a text serves both products, do the full work once. Work
  that serves Church in Conversation alone is deferred (the coordinator, passing on Mark, 15 November).
- No rendering of quotes, stories or lexicon entries starts until the coordinator has taken a proposal and one
  sample to Mark.
- Keep host bytes whole at intake. Stripping host additions is not in `cic/texts/INTAKE.md`.
- If a Fable call is refused or a usage limit is hit, do not switch models: stop at a clean point and report.

## The check before searching (the briefs' own step)

Done for the 41 candidates on 15 November, against `cic/texts/REGISTRY.yaml`,
`Build/worlds/_cross-world/download-queue-seed.yaml`, `WANTS-REGISTER.md` and `CORPUS-USE.md`, by archive.org
identifier and by author and title in `cic/texts/`. Record this in the batch's `Search_Log.md`.

- Held already, dropped from the batch: Richardson, Memoirs of Alexander Campbell, vol. 1
  (`memoirsalexande00unkngoog`; held as `richardson_memoirs-of-alexander-campbell-v1_1868.txt`).
- Not taken, a later printing of a text already held: Gobat's Journal, New York 1850
  (`journalthreeyea01bairgoog`; the London print of 1834 is held). It adds Baird's sketch; the coordinator may
  overrule.
- Held in another volume, so the candidate is a new volume and stays in: Davies's Sermons (vol. 3 held; vol. 1
  is the candidate); Valentijn (deel 3 held; deel 2); Launay (tomes 1 and 2 held; tome 3); Pascoe (vol. 1 held;
  vol. 2); Historia cultus Sinensium (the main volume held; the Continuatio); the Code noir (the collection of
  1767 held; the collection of 1743).
- No other candidate's identifier, author or title is in the four files.

## What is done

1. All 41 candidates fetched again from archive.org; every byte count equals the host's listed size
   (`fetch_manifest.json`; `fetch.py <outdir> candidate_ids.txt` fetches again, since the scratch downloads are gone).
2. Five Sonnet mappers read the 39 files that stay in, under the era 8 `MAPPER_BRIEF.md` with one added item (host
   marks and any copyright or permission line). Their reports are in `mapper-reports/` (`map1.md` to `map5.md`):
   title-page lines with line numbers, contents maps, editorial matter, wanted passages, OCR quality, the end.

## What the mappers corrected (read before writing headers)

- Parry: the title page prints 1896, not the host's 1895.
- Campbell's Declaration and Address: the title page prints 1906; "1908" stands only in the unsigned Centennial
  Introduction.
- Wilberforce (`lifewilliamwilb04wilbgoog`): the title page prints "VOL. I." (1838), whatever the identifier says.
- Hannah More, vol. I: "THIRD EDITION; REVISED, WITH AN ADDITIONAL PREFACE", MDCCCXXXV; the scan repeats some
  front matter.
- Raikes: lines 2273-2374 are newspaper extracts of 24 May 1784, not a letter. His letters are to Townley
  (25 November 1783, lines 1614-1673) and to the Arminian Magazine (5 June 1785, lines 1675-1748).
- Taft: vol. 2's title page (1828) is at line 19067; Sarah Crosby from line 20081.
- Fontaine: the two files are tome 1 and tome 2, Cologne 1738. Du Fossé is one volume in four books. Quesnel's
  tome 1 holds Matthew and Mark only.
- Dobrizhoffer: the three English files are vols. 1-3 (Murray, 1822); the Latin file is Pars I only (1784).
- Vieira's Sermoens: Terceira Parte (1683), Quinta Parte (1689), Parte Duodécima (1699).
- Valentijn, deel 2: no section headed for church affairs was found; the church chapters are not mapped.
- Soli Muratori's Vita: the title page is garbled in the OCR.
- The mappers' count of host marks used a one-space pattern, which misses the OCR's double spacing. With two or
  more spaces, a "Digitized by" line shows in Cooley's Haynes (line 11). Grep every file again for host marks
  with `[[:space:]]+` between the words before writing its Provenance note.
- McGready: vol. 2's title page and the heading of Sermon XXXV are missing from the OCR, and Sermon I has no
  heading page. The Gleaner: several essay headings in each volume could not be mapped; `map2.md` names them.

## Still owed, in order

1. Read on the page image every imprint the OCR garbles (the mapper reports quote each title page as the OCR has
   it): at least Davies vol. 1 ("M.DCC.xeiv"), Marsollier tomes 1 and 2, du Fossé, the Relation of the Missions of
   Paraguay (1759), the Code noir of 1743, the Continuatio ("M. DCC."), Soli Muratori, Love's Samson Occom (only a
   copyright notice of 1899 was read: ruling R12 applies if the title page prints no year). Page images:
   `https://archive.org/download/<identifier>/page/n<leaf>.jpg`.
2. Decide the doubtful ones: Valentijn deel 2 (600,000 words of Dutch with no church section found); the Code noir
   of 1743 (does it add acts the 1767 collection lacks?); Taft (a user upload of 2025: check the scan is of the
   prints of 1825 and 1828).
3. Write the spec on the pattern of `../2026-11-15_library-era8/mkspec1.py` and run `intake.py`. Shelves: the era
   8 census entries in `ERA8_WANTS_MASTER.md`; the shelf principle of the Decision-Log's "Shelf rulings".
4. Records: `Search_Log.md` here (with the pre-search check above), the "Era 8, batch 2" section of
   `CFT-Wants.md`, a Decision-Log entry, Open-Gaps 298.
5. One independent review by Opus, given the files and not the conclusions; then at most a targeted recheck.
6. The recipe and checks, `corpus_coverage.py` last; one draft pull request; one push; report to the coordinator.
   Check every pick's archive.org identifier against main's registry again just before the merge: three
   duplicates reached era 9 batch 2a that way.

## Thread B's queue after this batch, as the coordinator set it

1. Era 9 batch 2b's follow-on: only the "Located, not yet taken" volumes of
   `Build/Ministry/Operations/Audits/2026-11-15_library-era9-b2b/Handover.md`, not its 134 card rows.
2. Era 10 batch 2's follow-on list (The Christian East, the International Review of Missions, the Church
   Missionary Society's Proceedings, about thirty books), each title still owed its title-page check; not its 128
   card rows.
3. Era 8 batch 3: the groups the era 8 handover lists as not yet searched.
4. The second stage, rendering, only after Mark has seen the proposal and sample.
