# Handover — Library thread for the Church Family Tree, batch 4

Written 2026-11-10 at the end of batch 3, so that batch 4 starts in a fresh session.

## The charter and the coordinator

Mark's charter (2026-11-10): "launch a library thread that is patterned after previous threads with
full research, organization and render abilities to find the sources you need, public domain in any
language we can find it." The coordinator is session `session_01JMNsSDbFsmawtDvuAiukNQ`; report to
it with `send_message` after each batch. Read CLAUDE.md first, all of it.

## Where things stand

| batch | PR | what it did |
|---|---|---|
| 1 | #1577 | the later-worlds people gate (Pamphilus, Bonaventure, Francis, Priscillian; the Ecthesis already held); the Library defects in Open-Gaps 165 and 152 |
| 2 | #1579 | 22 files for the eras 8-9 holds; Mark's two cross-world rulings carried out (Bell Part II; the Pedalion) |
| 3 | this PR | 20 files for the earliest named gaps of Open-Gaps 158; AP10; the Ferencz rows corrected |

- **The record:** `CFT-Wants.md`, with one section per batch. Each want has its state, its
  files, its shelf and what it unblocks.
- **The decisions:** `Decision-Log.md` in this folder.
- **The page for Mark:** https://claude.ai/artifact/RTJ2uXC4rjqKEguvt4UiDP. Its source is not in
  the repo. Re-read it with the Artifact tool's `read` action, then republish to the same `url`.

## How a batch runs

1. Build the want list from the source (Open-Gaps or an audit). Each want names the text, the entry
   it serves, and its window.
2. Before any search, check what the Library already holds. Grep `cic/texts/README.md` and the
   filenames, and read the entry's shelf in `cic/corpus-map/<census-id>.yaml`. Census ids and dates
   are in `cic-website/data/world-census.json`.
3. Send searchers out (Sonnet subagents, one scratch directory each, nothing written outside it).
   The archive.org advancedsearch, `/metadata/<id>` and `/download/<id>/<file>_djvu.txt` endpoints
   work. HathiTrust is behind a browser check. Google Books refuses downloads from this host.
4. Verify every pick yourself before vendoring:
   - the host's rights field;
   - the title page in the OCR;
   - the wanted passage;
   - the byte count against the host's listed size.
   Never write a date, place or publisher the title page or the host record does not give. Batch 2
   and batch 3 both caught drafted details that were not in the sources, before writing.
5. Vendor with the header block in `cic/texts/INTAKE.md`. Header, a blank line, a row of 70
   underscores, a blank line, then the raw OCR unaltered. Give the offset ("add N") in the header.
   Check that the file ends with the full host text.
6. Shelve with `cic/corpus-map/_staging/<file>.yaml`, then run `python cic/engine/corpus_map_merge.py`.
   Rules:
   - The author slug is the filename's first segment.
   - A gap text gets a row only where an entry covers its date of writing; otherwise no row.
   - `needs-ruling` is for an entry the text fits but the tree has not yet ruled on.
7. Add a `cic/texts/REGISTRY.yaml` entry and a `download-queue-seed.yaml` row (`status: downloaded`).
   Then run `texts_registry.py --write-readme` and `gen_download_queue.py`.
8. Checks before the one push:
   - `texts_registry.py --check`
   - `tests_corpus_map.py`, `tests_corpus_structure.py`
   - `works_registry.py --check`, `author_ids.py --check`
   - `corpus_index.py --build`, then `tests_corpus_index.py --reuse-index` and `tests_passage_index.py`
   - `node tools/validate-census.mjs --base <main's census> ...`
   - `tools/check_live_commentary.py --base origin/main --enforce`
   - `engine.m2.cli staleness-check` and `engine.m9.cli check` if a built world's shelf changed
9. Things that bit:
   - Editing a vendored file's header must keep its line count. The census quotes files by line.
   - A header title change makes `cic/texts/README.md` stale; regenerate it.
   - CI's census check fails whenever main has published new movements since the branch was cut.
     Merge main in and push.
   - Open-Gaps entries are append-only. On a merge conflict, main's numbers stand and yours move up.
   - A change to a built world's shelf: check `records/`, `packages/` and the census for references
     first, and ask the coordinator.
10. Commit on `claude/library-cft-wants`, reset to the latest main at the start of each batch.
    Open the PR, merge it yourself on green, tell the coordinator, and update the page.

## What is left

Open, from the batches so far:

- **ME-21, Rabinowitz.** Six full-view Google Books items; the ids are in the Decision-Log (batch
  3). The fetch needs a browser, so ask Mark, or have him put the files in `cic/texts/_intake/`.
- **The Syriac Orthodox Church, 1300-1915.** Wright's Catalogue of Syriac Manuscripts in the British
  Museum (dated colophons, 1870-72) is the lead.
- **Not found in batch 2:**
  - AF-8 (Capitein, Quaque);
  - ME-4 (the 1848 Encyclical in a printing from before 1931);
  - ME-7 (a source from inside the region);
  - RV-9 (Kosmas);
  - AP13 (a Māori source);
  - the Molokans;
  - the Peking mission after 1808;
  - the 1860 Concordat in a period printing.
- **Located, not vendored:**
  - Lang 1834;
  - Bonaventure Opera VIII;
  - Brosset part II, 1856 first livraison;
  - Cluny charters vols. II-VI;
  - the Lerins cartulary part II (1905);
  - Kimmel 1850.
- **Ullathorne 1837:** the only scan is a 1963 facsimile, so its rights are unclear.

The next wants, in order:

1. **Open-Gaps 158, the rest of the 79 named gaps.** Batch 3 took the earliest thirteen, from Antioch
   after 312 to the Arabic Chalcedonians. Next come the orders and the later medieval and early
   modern gaps:
   - Athonite monasticism after 1300; the Carthusians after 1534;
   - the Cistercians, Dominicans and Carmelites after 1300;
   - the Maronites and the Franciscans after 1517;
   - the canons regular after 1246; the Order of Malta after 1291;
   - the St Thomas Christians 1665-1836; the Kongo church after 1650;
   - Japanese Christians 1650-1865; Chinese Catholics 1650-1906;
   - and so on down the list.
   Work them an era at a time.
2. **Open-Gaps 159:** the present-day families the tree doesn't reach. The Patriarchate of
   Alexandria, Cyprus, and the Polish, Czech-Slovak and Macedonian churches; the Eastern Catholic
   churches it never names.
3. **Open-Gaps 162:** the living marks graded none. These want dated own-voice items after 2010,
   which is mostly web material, not public-domain print. Ask the coordinator whether these are the
   Library's.
4. **The loci pass:** multi-work volumes whose rows say "whole file". 707 staging files say "whole";
   start with Langlois, the anf volumes and the PO fascicles.
5. **Desert OG-50:** desert's voice_craft process wording is the desert owner's, not the Library's.
