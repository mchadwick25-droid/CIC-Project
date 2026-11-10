# P2-G3, the agreed entries: data release 29 — 2026-11-10

The Church Family Tree's agreed entries, built under Mark's gap-sweep rulings (Decision-Log,
"The gap sweep ruled (P2-G1)", 2026-11-09) and his answers on the people list (2026-11-10:
"A a, B a, C a, D a, E a"). One data release: 353 movements (322 before), 689 links (644 before). Release 28 (P2-L10 part 2)
merged while this was in review, so it was re-applied on main as release 29; no entry or link it
changes was touched by either era 10 part.

## What the release holds

**Nine new movements**

| atlasId | id | dates | status |
|---|---|---|---|
| I.44 | `melitian-schism` | c. 306-8th c. | Pre-Survey Candidate |
| I.45 | `luciferians` | c. 355-c. 440 | Pre-Survey Candidate |
| V.24 | `carthusians-later-middle-ages` | 1300-1534 | Pre-Survey Candidate |
| VI.31 | `new-france-mission-born-christianity` | 1610-1650 | Pre-Survey Candidate |
| VI.32 | `hutterite-brethren` | 1528-1785 | Pre-Survey Candidate |
| VII.30 | `swedish-lutherans-of-new-sweden` | 1638-1786 | Pre-Survey Candidate, thin (one source) |
| VII.31 | `english-unitarianism` | 1774-1813 | Floor Question (register), copied from the American Unitarian entry; nothing decided |
| VII.32 | `mennonites-and-amish-after-1650` | 1650-1890 | Pre-Survey Candidate |
| VIII.52 | `melkite-greek-catholic-church-after-1815` | 1815-1911 | Pre-Survey Candidate |

**II.1 extended back to 328.** `cyrilline-miaphysite-egyptian-christianity` is now "The Church of
Alexandria and Miaphysite Egypt", 328-642 (ruling 2). The ID stays, and so does era 3: its
"continued as" link to the era 4 Coptic entry needs adjacent eras. Its claim to the inheritance of
Athanasius and Cyril is stated as Contested in the text, with both sides. It carries five stories:
three from the retired I.14 (Hypatia, Ephesus 431, Dioscorus at Chalcedon) and two new (Proterius,
Benjamin), each checked against vendored text. The desert monks' "gave rise to" link,
`desert-monasticism--cyrilline-miaphysite-egyptian-christianity--2`, is retired: the church now starts
before the monks, and the 457 evidence shows influence, which the "influenced" link on the same pair
now carries. The older retired record that pointed at it now points at that link.

**22 person entries** (kind "person"), each told within the tradition whose Library shelf holds them
(principle 4), carrying its door:

| person | told within | why an entry |
|---|---|---|
| Irenaeus of Lyon | post-apostolic-house-church | ruling 11 |
| Origen | alexandria-catechetical | 16 own works |
| Cyprian of Carthage | latin-pastoral-congregational-christianity | 35 own works |
| Athanasius of Alexandria | alexandria-catechetical | 22 own works; Mark, answer A a |
| Ephrem the Syrian | syriac-edessa-nisibis | 11 own works |
| Gregory of Nyssa | cappadocian-nicene-pastoral-monastic-tradition | 15 own works |
| Ambrose of Milan | ambrosian-milan-standalone | sweep principles (M) |
| Jerome | hieronymian-ascetic-literary | 17 own works; sweep principles |
| Augustine of Hippo | latin-pastoral-congregational-christianity | ruling 10; 106 own works |
| John Chrysostom | antiochene-exegetical-christianity-chrysostom-ce | ruling 10a; 36 own works |
| Jovinian | no tradition | ruling 13 |
| Nestorius | antiochene-exegetical-christianity-chrysostom-ce | ruling 12 |
| Peter the Iberian | no tradition | ruling 14 |
| Simeon of Beth Arsham | syriac-orthodox-west-syriac-christianity | ruling 15 |
| Gregory the Great | roman-church-gregorian | sweep principles |
| John Wyclif | lollardy | 12 own works |
| Thomas à Kempis | devotio-moderna-brethren-of-the-common-life | 14 own works |
| Martin Luther | lutheran-wittenberg-and-its-congregations | 47 own works |
| Ignatius of Loyola | the-society-of-jesus | 10 own works |
| William Tyndale | the-english-reformation-and-elizabethan-settleme | ruling 16 |
| John Calvin | the-reformed-cities-zurich-and-geneva | 12 own works |
| John Wesley | the-methodist-revival | 11 own works |

Jovinian and Peter the Iberian are Pre-Survey Candidates with the status word "Told within no
tradition" (answer B a). Tertullian's display name is now "Tertullian" (Open-Gaps 136; the ID stays).

**People rows.** Every tradition now shows its named people, drawn from its `voices` (principle P4b):
433 items in 164 traditions (277 on a work of their own on the tradition's shelf, 135 on a quote of
their own words, 21 person entries). 166 traditions name no one, and each carries `peopleNote`, one
plain sentence saying why (a new field: validator check, tree-page section, meta note).

**Links.** 46 new: argued against 21, gave rise to 7, in contact with 7, influenced 6, continued as 3,
broke with 2; Documented 38, Widely Accepted 4, Inferential-Thin 4. Major: the 12 of the three
lineage types, and 6 with an `outcome` under step 4b. One link rewritten under its own ID, one
retired. 107 existing links gain `concerns`, the person entry they are about, read link by link
against the note and quotes. Where a link names two person entries, one is chosen and the choice is
in the drafting record (the two Calvin links go to Calvin, whose words are quoted).

**Text changes to existing entries.** latin-pastoral-congregational-christianity's longDescription now
matches its own Doc_01 and takes in the controversies (ruling 10; census fields only, the world's files
untouched). post-apostolic-house-church gains a voices line for Irenaeus (ruling 11). The Devotio
Moderna entry gains the line that its houses kept their own chronicles (ruling 51 C), and its line on
the Imitation now says the authorship is disputed, to match the Kempis page. The Anabaptist entry's
Hutterite material is trimmed now the Hutterites have their own entry. carthusian-life, the Anabaptist entry and VII.23 gain
`continuesAs` to their successors. Two link notes now name John Wesley in full, so their `concerns` names him; one
note gains the accent in "Thomas à Kempis".

## The map until the people view

The map has no people layer yet (P2-P). Mark ruled (2026-11-10, "Hide until P2-P") that until it
does, the map leaves person entries and the links whose end is a person out of its own data. Their
pages, the people rows on each tradition's page and the census are unchanged. P2-P removes the
filter (`PERSON_IDS` in `cft-website/index.html`; a test in `generate_tree_pages.test.mjs`).

## The two counts

**Own works (ruling 10c).** 10 or more distinct works of their own, held as a tradition's own voice on
one shelf (`counts/count_own_works.py`): 15 people (Tertullian already an entry). Collections and
editors are not people and are left out (the Jesuit Relations, Blair and Robertson, the Church of
England, the Kirk). Just under the line, 8 or 9 works: Basil, Zinzendorf, Ambrose, Gregory the Great,
Francke, Edwards, Laínez, Justin.

**Later worlds (ruling 10d).** Each of 1,140 named people, with an alias list, counted in the own-voice
texts of later traditions (`counts/later_worlds_tally.py`; ripgrep over the 1,210 files the shelves
hold as tradition). As written (5 or more mentions in each of 2 or more later traditions) the rule
passes 125 people, most of them from eras 1 and 2, whose volumes sit on many later shelves. Known
noise: one-word aliases that also name others are not counted (`counts/ambiguous_aliases.json`), but
namesakes remain (Jerome Lalemant counts for Jerome), and the editions' own notes and indexes count as
mentions. Mark (answer D a): the 22 ship now; the counted people are held for a follow-up with a clean,
namesake-checked count. Result: `counts/later_worlds_result.json`.

## What counts as a person's own words (answer C a)

The rows reviewer sorted every quoted backing by speaker: own writing, issued in their name, jointly
signed, verbatim minutes, reported by another, disputed authorship. Mark ruled that the first four
count and the last two do not, for quotes and Library rows alike. 37 people left the rows under it.

## The Carthusians (answer E a)

The order from 1300 to 1534 is an entry, with Nicholas Love's own book as its voice. 1534 onward is
held as a named gap (principle 3): the Library holds no voice of the London Charterhouse's own, only a
Victorian retelling, a convent's account and the crown agents' letters. The 1535 martyrs, the Newgate
deaths and the exile to Bruges are told in three sourced sentences in the entry's legacy. The draft
of the second entry is kept here unapplied (`drafts/D2_Draft_optionB_not_applied.json`).

## How it was drafted and reviewed

Opus drafted in seven slices (D1 to D4 movements, P1 to P3 persons) and five row bands (R12, R36,
R78, R910 by era, RNEW for this release's new and rewritten entries), each in its own scratch folder,
to the briefs here (`G3_Drafting_Brief.md`, `Rows_Brief.md`). Each draft carries a fact table tying
every factual sentence to a vendored file, lines and quote. `check_draft.py` scored every paragraph
(Reading Ease 60 or more, FK 10 or less, with `engine.m7.turn_readability.score_turn`) and checked
every quote verbatim; it ran clean on every final draft. No metered model call was made.

A separate Opus 5.5 reviewed each part (`Review_Brief.md`), from the census, the sources and the
drafting record, not the drafters' conclusions:

| part | Round 1 | Round 2 | Round 3 |
|---|---|---|---|
| Movements and II.1 | revise: 0 blocking, 8 substantial, 19 minor | approve (3 minor, applied) | — |
| Person entries | revise: 1 blocking, 6 substantial, 16 minor | approve (1 minor, judged sound as is) | — |
| People rows | revise: 1 blocking, 3 substantial, 6 minor | revise: 1 substantial, 4 minor | approve, no findings |

Revision logs are in `drafts/*_Revision_Round1.json`; review files in `reviews/`. The coordinator's
own fixes at apply (a short name, two place IDs with no source, two link notes, and four spellings:
two edition titles quoted, three paraphrases in American spelling) are listed with reasons
in `decisions_final.json` (`field_overrides`), and the row fixes in `rows_fixes.json`. `apply_g3.py`
merged everything; its log is `apply_log.json`. Drafting keys never reach the census: a link keeps
only the census's own fields.

## Checks

- `node tools/validate-census.mjs --base <main's census> --atlas cft-website/index.html --tree cft-website/tree`: 0 errors (2 old shortName warnings).
- `python -m engine.m6.cli check` and `atlas-check`: no changes. `atlas-sync` added the 31 entries to the map.
- `node Build/tools/generate_tree_pages.mjs`: 353 pages. `node tools/build_tree_site.mjs`: 0 mismatched.
- Node tests: the validator suite (41) and `cic-worker/worker.test.mjs` with `generate_tree_pages.test.mjs` (46), with new tests for `peopleNote`. `pytest engine/m6/tests`: 45 passed.
- Paths, commentary (`--enforce`) and spelling: clean.
- Chromium: the map draws the new entries; new movement pages, person pages, II.1's new name and row, and an empty row's note render; link anchors resolve; no page errors.

## Recording batch (no recording made)

Mark ruled (2026-11-10) that all tree recording waits for one batch after P2-L10 and P2-G3 have both
merged. Both parts of P2-L10 have now merged. What this release adds to that batch, from the narration dry
runs (`narration_counts.json`):

| what | items | characters |
|---|---|---|
| new tree pages (9 movements, 22 persons) | 31 | 38,112 |
| tree pages whose text changed (II.1, Devotio Moderna, the Anabaptists) | 3 | 3,898 |
| documented stories, new or changed (II.1's five, the Melitians' one) | 6 | 3,508 |
| **total** | | **45,518** |

## Wanted texts

- **Melitians:** the History of the Patriarchs, life of Michael I (744-768), the last report of them;
  SB 5174-5175; Epiphanius, Panarion 68 in English; the Canons of Peter of Alexandria in English;
  Rufinus, Church History X.9-10.
- **Luciferians:** a primary source dating Socrates' Church History and the council of 362; a
  Damasian or neutral account of the Roman Luciferians.
- **Carthusians:** Chauncy's Historia (1550), the voice the named gap after 1534 waits for; Ludolph of
  Saxony, Denys the Carthusian, the order's statutes; the English Carthusians in exile (1559-1783);
  Arundel's approbation of Love's Mirror; Richard Methley's own writings.
- **New France:** any text in a convert's own hand; the Relations after 1650.
- **New Sweden:** the congregations' church books; Campanius (1702); a Moravian account of 1742-1745.
- **English Unitarianism:** Lindsey's Apology (1774) and Historical View (1783); Belsham's Memoirs of
  Lindsey whole; Toulmin's Life of Socinus; Nye's history and Biddle's tracts; the 1813 Act; anything
  after 1813.
- **Mennonites and Amish:** texts written 1650-1850 (the Skippack letters, the Amish division, a
  church order or hymnal of the 1700s); the 1748 Ephrata Martyrs Mirror; a pre-1931 Martyrs Mirror
  printing.
- **Hutterites:** the chronicle of the years in Wallachia and Russia; the 1874 emigration; a clean
  scan of Riedemann's Rechenschaft.
- **Melkites after 1815:** Maximos III Mazloum's own history; Thomas Mazloum's documents; al-Machriq.
- **Persons:** Ambrose Letter 42 and Siricius Letter 7 (Jovinian); Augustine on Jovinian; a clean
  Possidius; Paulinus' Life of Ambrose; a usable Cyril of Scythopolis; Simeon's longer letter; a modern
  study of Nestorius in the repo; Bedjan's Syriac Bazaar; the medieval lives of Gregory; a critical
  source on the theses-door story; Shirley's Fasciculi Zizaniorum; a source for Ignatius's election.

## Open items

Logged in `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` (2026-11-10): the later-worlds
people held for a follow-up; Library shelf moves for the Library thread; place IDs with no source; the
Martyrs Mirror file's rights; the Carthusian end date; the desert monks' influence evidence after their
span; and the people layer on the map.
