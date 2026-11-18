# R2 recheck: Library era 10, batch 2 (2026-11-15)

**Verdict: PASS. 0 blocking findings.** All four round 1 blocking findings are confirmed fixed in the files. Two new non-blocking findings, both in the audit folder or about a dropped limit; neither touches a rights line.

Reviewer: independent, targeted recheck, read and grep only. No network, no validators, no page images. Round 1 read commit `0482b470`; the changes are in `b4364f2f`. Read at `eaebb962`, which adds only `Handover.md` to this folder. Matters round 1 accepted were not reopened.

## What changed since round 1

`git diff 0482b470 b4364f2f`: 30 files. Eleven text files differ, each by one or two header lines and nothing else (numstat 1/1 or 2/2; every hunk at lines 5 to 9): `catholic-sabha`, `christian-east_v4-no2`, `christian-east_v4-no4`, `gollock`, `international-review-of-missions_v12`, `jabavu`, `khrimian`, `manassa-yuhanna`, `tucker`, `velimirovic_religion-and-nationality`, `vvedensky`. The other 60 text files are byte-identical to round 1. No body line changed in any file.

## Blocking findings of round 1

| # | status | evidence |
|---|---|---|
| B1 | confirmed fixed | `_staging/put_n08-rus_1927.yaml` line 11: "Signed pieces here by Berdyaev." `_staging/put_n22-rus_1930.yaml` line 11: "Signed pieces here by Florovsky." The bucket `emigre-orthodoxy-and-the-paris-school.yaml` carries the same words on the rows `put_n22-rus_1930--...` (line 155) and `put_n08-rus_1927--...` (line 233). Checked again in the texts: in number 8 Bulgakov stands only in the list of contributors (line 26), the contents (101) and as author of the book reviewed (15868); in number 22 Berdyaev stands as editor (19, 26), as the addressee of the letter (72, 4390) and as a writer cited (6205). The note for number 22 does not add the letter addressed to Berdyaev, which round 1 offered; it is not needed for the note to be true. No other staging file or bucket still carries the old wording for these two numbers. |
| B2 | confirmed fixed | Header line 9 of `vvedensky_tserkov-i-gosudarstvo-rus_1923.txt`: "An epistle of the Council to the people, which orders prayers for "14 сентября", at about lines 6949-7056; the print gives it no date that can be read." Opened: line 6952 "Собор повелевает устроить 14 сентября ... на которых прочитывалось следующее послание"; the epistle ends at line 7056 ("...самоотвержения и любви Христовой"). Between 6850 and 7100 the only dates are "14 сентября" (6952) and "23 сентября" (7077), with no year on the epistle. "September 1917" is gone. `REGISTRY.yaml` line 25362 carries the same sentence. The queue row (`download-queue-seed.yaml`, about line 29614 to 29626) holds no Content note and no line range, at round 1 or now, so there was nothing to copy there; its `why` speaks only of Tikhon's epistle of 1918. |
| B3 | confirmed fixed | May 1923: header line 8 "at lines 4125-4200"; `_staging/christian-east_v4-no2-may-1923.yaml` locus "lines 4125-4200"; both Russian buckets (`the-russian-new-martyrs-and-the-catacomb-church.yaml` line 18, `the-russian-orthodox-church-council-patriarchate-and-reunion.yaml` line 18) "lines 4125-4200"; `REGISTRY.yaml` line 25330 the same. Opened: the heading "A PASTORAL OF THE PATRIARCH TIKHON." at 4125; the closing prayer ends at 4200 ("To Thee belongs our life. To Thee goes forth our hope."); "THE BITTER CRY OF THE GEORGIAN CATHOLICOS" at 4203. November 1923: header line 8 "at lines 1359-1629"; staging locus, both buckets (line 26 in each) and `REGISTRY.yaml` line 25338 the same. Opened: "THE EPISTLE OF THE PATRIARCH TIKHON." at 1359; "The original signed by THE HUMBLE TIKHON, Patriarch of Moscow and All Russia." at 1623-1625; "Donskoi Monastery, Moscow." at 1626; "July 15th, 1923." at 1629; the next piece follows. Both ranges now hold the whole document. No file under `cic/corpus-map`, `REGISTRY.yaml` or the queue still carries 4125-4147 or 1359-1612. The queue rows hold no line range. |
| B4 | confirmed fixed | `CFT-Wants.md`, batch 2, rows not filled: the Rātana row now reads "Te Whetu Marama is reported to be on Papers Past, which was not opened: on the hand-fetch list"; the Loisy row reads "A search result reports the first on Gallica, which refused a plain fetch: on the hand-fetch list, to be confirmed." `Hand_Fetch_List.md` item 7 (line 62): "Search results for Te Ara and other pages give the same first issue, 15 March 1924; none was opened." Item 7's "NOT CONFIRMED" line (61) stands. Item 14 (line 91): "by the search result, not opened. An edition of 1936 would fail the 1930 test." |

## Non-blocking changes claimed in R1_changes.md

| # | in the files as described? | where |
|---|---|---|
| N2 | yes | `Search_Log.md` line 19: the basis row names Путь numbers 2 and 17 and what their dates rest on; line 211 agrees. |
| N6 | yes | `gollock` header line 8 and `REGISTRY.yaml` line 25126. Checked: "Missionary Education Movement" at line 319; Dr Lerrigo at lines 7386 and 7466. "For study groups" and "the Kibangu section crediting" are gone. |
| N7 | yes | Header, `REGISTRY.yaml` line 25134, staging locus and the bucket `african-initiated-churches-harrist-aladura-zioni.yaml` all read 11465-11610. The section heading (OCR "Re ticious UNREST") stands at line 11465. No 11456 is left. |
| N8 | yes | See the next section. |
| N10 | yes | `tucker`: "Volume II only of two." `manassa-yuhanna`: "The OCR yields no mention of the Sunday schools." (a grep for the usual Arabic spellings finds none). `catholic-sabha`: "The names of Dionysius and Abdul Masih do not appear in the OCR" (a grep for likely Malayalam spellings finds none; the OCR is poor, so this is as far as it can be checked). `khrimian`: the sentence about unexamined lines is gone; see new finding 2. `REGISTRY.yaml` copies follow in all four. |
| N11 | yes | `CFT-Wants.md`: "71 files, 4,273,101 words: 32 in English and 39 in other languages." |
| N12 | yes | `Search_Log.md` line 28: 3,332. |
| N13 | yes | `Search_Log.md`: the reason for the Christian East issues, Lototsky and Евразийский временник (left to the follow-on session; located late); the Mizo and Khasi identifiers now point to `searcher-logs/oriental_LOG.md`. |
| N14 | yes | `Search_Log.md` (Oceania): "a letter that speaks of Rātana raising the Treaty again and of a covenant; its OCR is broken". "Petition" is gone. |
| N15 | yes | `CFT-Wants.md`: "the three "Catholic Worker" pamphlets there (two of them of 1947)". |
| N16 | yes | `Hand_Fetch_List.md` item 14, as under B4. |

## The Jabavu row and the new call

Consistent in all three places.

- `_staging/jabavu_black-problem-2e_1921.yaml`: role `tradition`; note "His own papers of 1920, printed at the Lovedale mission press fifteen years after the entry's window closes. No census entry covers the mission churches of southern Africa after 1906." The bucket `southern-african-mission-churches.yaml` (line 38 onward) carries the same role and note.
- `Search_Log.md` line 35, the new calls row: Tucker (1908), the Zulu hymnal (1911), Kyriakos Mikhail (1911), Jabavu (1921) and the Arabic history of the Coptic Church (1924) are tradition on the entry that closes in 1906, "each note giving the date". The five staging notes do give the date (1908; 1911; 1911; "fifteen years after" 1906 with the papers' own year 1920; 1924), and all five rows are `tradition`.
- `Decision-Log.md`, last entry: the same five works, the same role, "the shelf principle does not name this case". The call is marked as one the coordinator may overrule.

One small thing, not a defect: the Search_Log row lists Sundar Singh among the gaps; his rows are `context` (line 153) and are a different case. The Decision-Log does not list him. Nothing contradicts.

## Headers and counts

- **Headers.** The thirteen changed header lines were read in full. None gained commentary, process narration, a reference to a review, or a person's ruling. A scan of the first 12 lines of all 71 files for "Mark", "ruling", "coordinator", "review", "this thread", "looked for", "not taken" and "not examined" finds only the print's own words (the journal's title, "Public Domain Mark", "a review of Professor Zankow's book"). "Catalogue" is "catalog" throughout the 71 headers.
- **Counts.** `CFT-Wants.md` batch 2 table, recounted: 71 rows, 71 distinct files, all present; the word column sums to 4,273,101; 32 eng, 28 rus, 2 fra, 2 zul, 2 mal, 1 each mri, ara, hye, deu, ell; basis strings 65 / 3 / 2 / 1. `Search_Log.md`: 71 files, 65 / 3 / 2 / 1. `Decision-Log.md`: 71 files, 4,273,101 words. They agree. (`Search_Log.md` does not state the word total, as at round 1.)

## New findings

| # | file | finding | weight |
|---|---|---|---|
| R2-1 | `Hand_Fetch_List.md` lines 23, 26, 54 | The spelling change turned "catalogued" into "catalogd" three times. It should read "cataloged". No other file of the batch carries the slip (`REGISTRY.yaml`, the queue, the staging files, `CFT-Wants.md`, `Decision-Log.md`, `Search_Log.md` checked). | non-blocking |
| R2-2 | `khrimian_amboghjakan-yerker-hye_1929.txt` header; `Search_Log.md` | Round 1 (N10) asked for the process words to go. The fix removed the whole sentence, so the limit itself (the file's last 920 lines, 40100-41019, were not read) is now recorded nowhere: not in the header, the Search_Log or the Handover. The header's other claims stand without it. A line in the Search_Log's caution 18 would keep the limit on record without putting process words back in the header. | non-blocking |

## Checks not made

As at round 1: no page images, no network, no byte counts. Round 1's N1 (Zankov's title-page year, read again on the image by the builder) rests on the builder's word; nothing in the text contradicts it.
