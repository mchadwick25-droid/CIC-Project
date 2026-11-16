# Handover: Library, Thread B, after era 10 batch 2b, the periodicals (2026-11-16)

Written by Thread B (Library), session_01JMNsS9eBPDBXz7fMhLaHqF, which stopped at a clean point for its context
size. The coordinator is session_01JMNsSCBTsM2UVaFpDa3BTF; every report goes there with send_message. Read
`CLAUDE.md` first, then `../2026-11-16_library-era9-located/Handover.md` (the method), then this file.

## Done by this session

**Era 10 batch 2b, the periodicals (Open-Gaps 300).** 45 files: 31 numbers of The Christian East and 14 volumes
of The International Review of Missions. Record: this folder (`Search_Log.md`, `R1_review.md`, `R1_changes.md`,
`R2_recheck.md`, `mkspec300.py`). See "State of 300" at the foot for whether it is merged.

Also recorded in that pull request, each with Mark's quoted words as the coordinator passed them on, in
`cic/texts/INTAKE.md` and the Library Decision-Log ("Era 10, batch 2b, the periodicals"):

- R13: an institution's report counts by a date printed in its own text, read on the page image.
- R14: a host's own additions may be removed at intake, with the exact text, line count, host URL and original
  byte count in the header.
- R15: a microfilm maker's notice on a scan blocks taking it. The CMS Proceedings stay out for every year.
- R11 as the one rule for checking our own renderings; older stages of a language count as foreign; every
  quotation from English printed before 1931 is put into our modern English with the second rendering.
- Mark's Fable exception for renderings, quoted; `CLAUDE.md` is not changed, by his instruction.

## The queue, in the coordinator's order of 16 November

1. **The sample** (below). Commit nothing for it until Mark approves it.
2. **305: the year audit.** A read-only list of every held file under `cic/texts` whose header year differs
   from the host's date for the same item. Read the year on the page image for each, files dated 1925 to 1935
   first. Report every wrong year and say whether it changes the rights call. Change no file until Mark has
   seen the list. Publish it as one page and send the coordinator the link.
3. **302: the books of era 10 batch 2's follow-on**, with three more things in the same pull request:
   - the Pacific Garden Mission's statement of 1916 (`annualreportpaci1915paci`), now admitted by R13; its
     page-image reads are in `../2026-11-16_library-era9-located/Search_Log.md`, call 1;
   - the headers of the Путь files (`cic/texts/put_n*-rus_*.txt`) brought to R14: they give the stamp's text,
     the line count, the item and a byte count, and lack a URL;
   - the three shelf rows of era 8 batch 2 moved from `needs-ruling` to `assigned` as they stand (Parry on
     `the-sayfo-and-the-syriac-diaspora`; Charmot on `chinese-catholicism-1650-1906`; Quesnel as the condemned
     text on `catholic-church-ancien-regime`), with Mark's words, "Yes, as proposed (Recommended)", in the
     Decision-Log. Fix the staging files, then merge.
4. **301: era 8 batch 3** (`../2026-11-15_library-era8/Handover.md`, "Not yet searched").
5. **303: The International Review of Missions for 1912** (three numbers on the host: January, July, October)
   **and 1913** (`sim_international-review-of-mission_1912-01_1`, `_1912-07_1`, `_1912-10_1`, `_1913_2`). No
   CMS volume: R15.

If main shows any of these numbers taken at merge time, stop and ask the coordinator.

## The sample: the coordinator's brief, word for word

> THE SAMPLE (Fable, under Mark's exception):
> 1. A finding guide for Groen van Prinsterer's Ongeloof en Revolutie (1868, the held Dutch file). Go section by
>    section: what each part covers, who and what it names, its line range. Plain English at the B2 reading
>    level, labelled "our guide to the contents, not a translation". Names, dates and places as printed. Claim
>    nothing the section doesn't contain.
> 2. Three passages that a profile writer would likely want, for example his statement of his thesis, a passage
>    on the Reformation and one on the Revolution. Render each to the CLAUDE.md bar: every clause, nothing added,
>    one thought per sentence, nothing much past 25 words, no word whose modern sense misleads.
> 3. The R11 check: a second Fable rendering of each passage, done by a separate agent that never sees the
>    first. Compare the two. Mark any difference in meaning as "uncertain", and keep both readings.
> 4. A fresh reviewer, also separate, checks the guide (by sampling sections against the Dutch) and the three
>    final renderings against the Dutch and the bar.
> 5. One artifact page for Mark: the guide; each passage in Dutch beside the final English, with the second
>    rendering and the marked differences; and the review result.
> Commit nothing for the sample until Mark approves it. Report the link to me.

The approved proposal is at https://claude.ai/artifact/6dzfNKYrABrFFRpdcd6epq. Mark's choices on it: "A: guides
now, passages when used (Recommended)"; "Yes, Groen van Prinsterer (Recommended)"; "R11 as the one rule
(Recommended)"; "New cic/renderings/ folder (Recommended)". The `cic/renderings/` folder waits for his approval
of the sample, and the root `README.md` map is updated first when it is made. Finding guides are for
non-English texts and older stages of a language only.

## 302, the books: where it stands

Twenty-five scans were fetched on 16 November into this session's scratch folder, which is gone; fetch again
with `fetch.py` and the identifiers below. Every byte count matched. None is mapped and no title page is read.

- Already held, drop: `bantupastpresent00mole` (`molema_bantu-past-and-present_1920.txt`).
- Not to take: `mokhoa-oa-ho-etsa-komunione-e-halalelang` (the record carries CC BY-NC-ND 4.0, a non-commercial
  license).
- To check and take if they pass: `tuckerofugandaar0000shep`, `uganda18771927pa00chur`,
  `churchinugandach00will`, `twentyfiveyears00roscuoft`, `howugandawassave00stoc`, `unitedwestafrica00hayf`,
  `congomissionaryc00cong_0`, `congomissionfiel00gene`, `monkanamomosemon00bill`, `ebukahimeneifaaa00chur`,
  `kealakaioiahoihe00dina`, `ngahimenemongahu00unse_0`, `servicebookofhol00orth_0`,
  `relationsofangli00dougiala`, `someaspectsofcon00gavi`, `orthodoxcatholic1361unse`,
  `newidealineducat00veliiala` (host date "[1916?]"), `cerkovne-pravo-lotockyj-1923`,
  `evraziskivremenn53unse`, `modernsonsofphar00leeduoft` (host date "[1918]"), `ethiopicliturgyi0000merc`,
  `lesynaxairearmni0000arme`, `in.ernet.dli.2015.464686`.
- Named in the list without an identifier, still to find: Tucker's Eighteen Years, vol. I (vol. II is held);
  Te Karere for 1926 and 1928; Connolly's Two Commentaries on the Jacobite Liturgy (1913); the Armenian
  pamphlets of 1908; the Mizo prints of 1912-1930 (`../2026-11-15_library-era10-b2/searcher-logs/oriental_LOG.md`).
- Run the check against the registry, the seed, WANTS-REGISTER and CORPUS-USE again before intake, and record it.

## What the two reviews of 300 caught (watch for these)

- **A range that gives one party's words to another.** One row covered a patriarchal deputy's letters and, in
  the same span, the constitution of the rival council he was writing against. Give each document its own row.
- **A row that runs on to the next heading, or stops before the document ends.** An anchor check proves the
  words are on the line, not that the range ends where the document ends. Read both ends of every row in the
  text: end at the signature or the last line of prose, never on a running head, a junk run or the next title.
- **A plate leaf inside a document.** Junk lines in the middle of a text are not its end; look past them.
- **A row that starts on the editors' lead-in.** Start at the document; cite the lead-in in the note.
- **"No translator named" where the editors do name one**, a few lines above the document.
- **"All signed" where the print makes an exception.**
- **A by-line that gives a see and a signature that gives the name.** Read the end of the article and the notes
  on contributors before saying a name is not printed.
- **A cited line that is a running head, the second line of a heading, or a by-line.** Cite the heading's
  first line.
- **A section or a book notice listed as an article.**
- **Facts about a writer the print does not give** ("a Serbian bishop", "a Japanese writer"). Use the print's
  words.
- **Search narration in a date source** ("the letter's own date was not found").
- **A cover read too quickly**: one cover of eleven lacked "Canon" before an editor's name.
- A number filmed without its cover may still name its editor in a notice inside.

## Held or ruled out from this batch

- The Proceedings of the Church Missionary Society, every year: out under R15. No other scan was found on
  archive.org; HathiTrust and Google Books refused automated searches and want a search by hand.
- The Christian East, vol. XI, no. 4 ("Winter, 1930-31"): printed in 1931, free from January 2027.

## Tools here

`fetch.py`, `intake.py` (the fetch date is set inside it), `mkspec300.py` (the spec pattern for a periodical:
one helper per journal, every cited line anchored), `tools/grid.py` (one sheet of first leaves for many
items), `MAPPER_BRIEF.md` (the brief for periodicals, with the item on host marks and on years later than the
file's). The page-image tools `sheet.py`, `crop.py` and `stack.py` are in
`../2026-11-16_library-era9-located/tools/`.
