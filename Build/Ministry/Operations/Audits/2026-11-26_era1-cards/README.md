# Era 1 cards — batch README

Owner: the one era 1 cards thread (coordinator session `session_01JMNsSDxiDjhkPh1K48BmfL`). Rule and scope: `Header.md` in this folder. Branch: `claude/built-world-short-descriptions-v2`.

## Step

1. **First set for Mark** (one card of each of eight kinds; table in `Header.md`). Written (`<id>.layout.json`, `Card_Edits_<id>.md`), checked (`Card_Check_A.md`, `Card_Check_B.md`), exact changes applied word for word (`Applied.md`), evidence gathered and every quote re-found at its lines (`Evidence.json`, 231 of 231). Page sent to the coordinator 2026-11-26: https://claude.ai/artifact/CVzArtefSKCkoRRyC23ZfB (built by `build_first_set_page.py`). **Approved** (Mark, 2026-11-26: "yes, but let say church in conversation world instead of built world"; Decision-Log).
2. The rest of era 1, kind by kind, on the approved cards (same process: one write, one independent check by a hand that wrote none, the checker's exact changes applied word for word, `Evidence.json` with every quote re-found by script). No public "world" anywhere a visitor or Mark reads: "Christian Tradition", and "Church in Conversation Tradition" for the eleven built ones (Decision-Log, 2026-11-26). Internal names stay. Work order and state, updated after each card:
   - **2a. Traditions** (20 in era 1; Bardaisanites, modalist Monarchianism and Danubian Latin get cards built from what is held, brief kept as it stands): Montanism and Alexandria done. Next: post-apostolic-house-church, syriac-edessa-nisibis, latin-pastoral-congregational-christianity (Church in Conversation Traditions; short descriptions for the first two drafted in `Short-Descriptions/2026-11-26_built-worlds-v2/Drafts_A.md`, unchecked), then greek-apologists-second-century, latin-apologists, apocryphal-and-pseudepigraphal-literature, marcion-marcionism, valentinian-and-other-gnostic-christianities, manichaeism, ebionite-nazoraean-current, novatianism, anatolian-church-third-century, antiochene-church-third-century, palestinian-church-pre-constantinian, roman-church-third-century, danubian-latin-christianity, modalist-monarchianism, bardaisanite-current. Batch-11 folders hold sheets and held fields for the twelve it rebuilt.
   - **2b. People** (28 in era 1, all of them, from the briefs they have now): Polycarp done.
   - **2c. Council** (1): done.
   - **2d. Era 1**: done.
   - **2e. Stories** (26 documented stories on era 1 entries, plus the map stories in era 1): one done.
   - **2f. Connections** (82 edges touching an era 1 entry): one done.
   - **2g. Rivers** (6 in era 1: Origin, Syriac East & Asia, Greek East & Orthodoxy, Africa, Latin West & Catholicism, Non-Nicene Traditions): Africa done.
   - **2h. Existing-text fixes** flagged in `Applied.md` (story text, connection note, council fields, river origin record): to apply by the same process, worded by a checker.
3. Site code: branch `claude/built-world-short-descriptions` handed over (coordinator, 2026-11-26) and merged into this branch at its head 9711baa7. Still to build: a field home, validator keys, atlas-sync carriage, map open functions, MENU_ORDER folds, tree pages and tests for story, connection and river cards; `timeline` for rivers. Two phone tests in `Build/tools/tree_map_view.test.mjs` already fail on main.
4. Release: one pull request for era 1. Not started.

## Cards

| Card | Kind | Step |
|---|---|---|
| montanism-the-new-prophecy | tradition | checked, fixes applied, shown to Mark |
| alexandria-catechetical | Church in Conversation Tradition | checked, fixes applied, shown to Mark (short description drafted in `Build/Ministry/Features/Church-Family-Tree/Short-Descriptions/2026-11-26_built-worlds-v2/Drafts_A.md`) |
| polycarp-of-smyrna | person | checked, fixes applied, shown to Mark |
| councils-of-rome-and-carthage-251 | council | checked, fixes applied, shown to Mark |
| era-1 | era | checked, fixes applied, shown to Mark |
| The Sister Who Saw Visions During the Service | story | checked, fixes applied, shown to Mark |
| post-apostolic-house-church--montanism-the-new-prophecy | connection | checked, fixes applied, shown to Mark |
| river-africa | river | checked, fixes applied, shown to Mark |

Short descriptions also drafted, unchecked: post-apostolic-house-church and syriac-edessa-nisibis (same Drafts_A.md). The halted 12-built-worlds task's records are in `Short-Descriptions/2026-11-26_built-worlds-v2/`.

## Open items

- Public "world" sweep (Decision-Log 2026-11-26): fixed the four map card strings in `cft-website/index.html` ("This world's sources", "No further orientation content recorded for this world yet.", "This world's fuller record could not be loaded", "Loading this world's fuller record…" now say "tradition"), and the Africa river card's legacy line. Still in the census, for the era 1 release: `alexandria-catechetical` `livingEvidence.basis` "The world built from this entry names the Coptic…", and one field reading "the next richest built world's 37". "Throughout the world" and similar ordinary uses, and quotations, stay.

- First set, left open by the checks: Polycarp's timeline references need file and lines added (P3, minor); the existing texts flagged for a fix (story text, connection note, council fields, river origin record; listed in `Applied.md`) are not changed until Mark rules; shown dates for Alexandria ("c. 180 to 4th c.") and Polycarp ("2nd c.") are proposed, not applied.

- Syriac's shown end date 410 is given as a Widely Accepted event, with no held line opened (Drafts_A.md).
- Open-Gaps 429 (years no source gives), 428 (where a tradition's card lives), 437, 438, 410 and 422 (connection notes and map stories, hold lifted for era 1).
- Two phone tests already fail on main (card site build thread's note).

## Mark's rulings in this batch

All are quoted verbatim in `Header.md`: the short-description rulings, and the widened scope of 2026-11-26.
