# Tree gap sweep (P2-G1), 2026-11-08

Ruling: `Build/Ministry/Features/Church-Family-Tree/Decision-Log.md`, 2026-11-06 scope entry, rulings 13 to 15 ("Every tradition on the tree", Q9, option B). Mark launched it on 2026-11-08 ("launch P2-G1 gap sweep").

This sweep was read only. It changed no census, record, Library or site file. Mark rules on the list in one sitting. P2-G2 (schema) and P2-G3 (the agreed entries) wait for that ruling.

## Files

- `candidates.json`: 108 numbered candidates, with every citation (file, lines, exact quote), the nearest census entries, vendored and wanted sources, a recommendation and one line of reason.
- `candidates.md`: the same list as a readable table, followed by the Open-Gaps entries for Mark.
- `open_gaps_rulings.json`: 23 open Open-Gaps entries from the link passes that are marked as Mark's call, each with options and a recommendation.

## Method

1. **Census.** `cic-website/data/world-census.json`: 300 movements, 364 links, no retired movements or links.
2. **Mechanical extraction (scripts, no model).**
   - Every staging file in `cic/corpus-map/_staging/` (1,527 files) was parsed. Every `atlas_ids` and `voice_of` value names a current census ID, so the structured fields have no gaps. A pattern search of the notes, the author rulings and the header comments for "no census entry", "no bucket", "nearest entry", "for want of a better home" and similar phrases gave 109 excerpts from 55 files.
   - Sections 2, 5 and 6 (cross-link opportunities, open cross-world questions, scope notes) were taken from all 118 dossiers in `Build/worlds/_cross-world/dossiers/`.
   - The same phrase search ran over `Build/worlds/*/` and `Build/World-Builds/`, plus `LIBRARY-DECISION-LOG.md`, `CASE-gallic-monasticism.md` and `GAPPED-FORMATION-WORLDS.md` (310 lines with context).
   - `PAIRS.yaml` lists no non-census party except the M9 fixture.
3. **Listing (Haiku, five agents, each in its own scratch folder).** One agent read the staging excerpts. Three read the dossier sections, a third each. One read `Build/worlds/_cross-world/NEEDS-RULING.md` in full and the world-folder hits. Each checked its quotes by script as exact substrings of the cited lines. Together they listed 125 leads still without a census home, after dropping those a current entry covers.
4. **Seeds from the tree's own Open-Gaps.** Nine "no movement for X" entries were added as leads. They are the church of Alexandria in the 4th and 5th centuries, Irenaeus, Augustine, the medieval English and Scandinavian successors, the Melkites from 1009 to 1724, the Second Bulgarian Empire's church, the Syriac Orthodox church after 1300, the conciliar movement, and the Carthusians after 1300.
5. **Judging and drafting (Sonnet, three agents by era: 1-4, 5-7, 8-10).** Each opened every cited line and confirmed it says what the lead claims. None was dropped, but several line numbers had drifted and were corrected. Each judge checked every lead against the full census entry (dates, region, text), grouped near-duplicates, checked `cic/texts/` for vendored sources and applied ruling 14's person test. The judges stated their granularity rules:
   - Orders and branches get their own entry only with a vendored rule, chronicle or voice and a story distinct from the covering entry's.
   - Wings and national branches stay inside the era's entry for that lineage.
   - A person needs writing of their own or a recorded position. The corpus must treat them as a party in their own right, not as a voice inside an existing movement.
6. **Merge and check (main thread).** Two leads overlapped across the era split and were joined: English Unitarianism and New Sweden. The two judges disagreed on English Unitarianism, and both readings are kept as options. Every file the "add" recommendations rest on was confirmed vendored. The census text was searched for the names it should lack (Jovinian, Lucifer, Tyndale, New Sweden, New France and others). One judge's claim was corrected. For the Syriac Orthodox church after 1300, the vendored Chronicon of Bar Hebraeus, vol. 3 (Abbeloos and Lamy, 1877), carries a continued list of maphrians with entries dated 1317 to 1369 (lines 25788 to 27282).
7. **Open-Gaps entries (Sonnet, one agent).** Every open entry the link passes raised that is marked as Mark's call was gathered once, with options and a recommendation. Continuations of the same question are grouped under it.

No metered model call was made.

## Counts

- Leads: 125 raised by the readers. Judged and grouped into 108 candidates (76 movements, 32 persons).
- Recommendations: add 8, add as person 7, retire as duplicate 1, merge into an existing entry 56, leave out 36.
- Groups:
  1. The Cyrilline duplicate and the church of Alexandria (2).
  2. New movements recommended (7).
  3. New person entries recommended (7).
  4. Successor gaps and structure questions from the link passes (10).
  5. Existing entries checked for the person kind (4, all "leave out").
  6. Told within an existing entry (54).
  7. Leave out (24).
- Open-Gaps entries for Mark: 23. Nine are census questions settled by a candidate, which leaves 14 separate rulings.

## Findings that shape the ruling

- **The Cyrilline duplicate.** `cyrilline-miaphysite-egyptian-tradition` (I.14, era 2, "from 451") and `cyrilline-miaphysite-egyptian-christianity` (II.1, era 3, 451-642) have the same subject: their census text, links and voices both describe the church after 451. The Library shelf for I.14 (`cic/corpus-map/cyrilline-miaphysite-egyptian-tradition.yaml`) is different. It holds Cyril's own works and the acts of Ephesus 431 and 449, which come before 451. Retiring I.14 into II.1 alone would leave that shelf in an entry whose window opens at 451. Keeping the ID and re-scoping it would break the permanence promise in `meta.identifiers`. The recommendation pairs the retirement with a new entry for the church of Alexandria up to 451, which also answers "No entry for the church of Alexandria, 4th-5th century" (Open-Gaps, 2026-11-07).
- **Stale notes.** Many "no census entry" notes in the staging files and dossiers predate entries added later. Examples are the third-century Roman, Palestinian, Anatolian and Antiochene churches, the floor-question shelves and the apocrypha shelf. Each is marked "covered (stale note)" rather than raised again. The Methodist build's Open-Gaps note that no Whitefield text is vendored is also stale: three Whitefield works are now in `cic/texts/`.
- **Real holes with no shelf yet.** The medieval English church after 1066, the medieval Scandinavian church after 1104, the Melkites from 1009 to 1724, the Scottish church after 1650, and the Swedenborgian and Old Believer successors are real census gaps. None has a vendored voice for its period. They are "leave out" for now and become candidates for a source pass.
- **Persons.** Seven pass ruling 14 on the Library's own evidence: Augustine, Irenaeus, Nestorius, Jovinian, Peter the Iberian, Simeon of Beth Arsham and William Tyndale. Nestorius did not come from a Library "no home" note: the era 1-4 judge found him while checking the Cyrilline shelf. Jovinian and Peter the Iberian pass only on the "recorded position" limb, since no writing of their own survives. Of the four existing entries that center on one person (Ambrose, Jerome, Gregory the Great, Chrysostom), none was recommended for the person kind, because each is a city church, a circle or a school.

## Not done here

No entry was drafted, and no census, Library shelf or site file changed. Wanted texts named in the list are not added to `Build/worlds/_cross-world/download-queue-seed.yaml`; that is the source-research thread's work once Mark has ruled.
