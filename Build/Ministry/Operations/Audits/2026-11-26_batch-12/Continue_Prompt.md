# Continue batch 12 (era 1 people and the era 1 brief)

You are taking over Church Family Tree batch 12 from an earlier session. Work on branch `claude/batch12-era1-persons`.

**Mark asked to slow down (2026-11-28, through the coordinator): "we need to slow down, we have used 24 percent of my weekly total in a couple of hours how can that be right".** The earlier session stopped there. Do not start work until the coordinator or Mark says to go on, and then keep few hands running at once.

1. Read `CLAUDE.md`, then `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md` and `Brief-Kit/kinds/person.md` (and `kinds/era.md` for the era brief).
2. Read `README.md` in this folder for the rulings (Mark's words verbatim) and how each step was run. Its status table is older than this file: **"Where each story stands" below is current.**
3. Bring the branch up to date with `main` before release; the era 1 card thread edits the same census.
4. Each hand is a fresh agent started from one filled prompt file in the story's folder; generators are in `_gen/` (make_writer, make_reviewer, make_length, make_recheck, make_review_fix, make_recheck_review, make_reviser, make_card). Word-for-word applies run on Sonnet from `Recheck_Apply_Prompt.md`, `Recheck_Length_Apply_Prompt.md`, `Recheck_Review_Apply_Prompt.md`, `Fresh_Apply_Prompt.md` and `Card_Check_Apply_Prompt.md`; everything that judges runs on Opus. Where a fresh read needed the outline, a `Fresh_Fix_Prompt.filled.md` (researcher) and `Fresh_Check_Prompt.filled.md` (targeted check giving the exact brief changes) were written by hand in the story's folder; copy that pattern.
5. Stops for Mark go to the coordinator session (`session_01JMNsSDxiDjhkPh1K48BmfL`) with send_message; his words come back verbatim. Pages for Mark reuse https://claude.ai/artifact/RBTfTfBxXXpT5RD7qjZVVk (now version 5), because the account is at its artifact limit.
6. No recording in this batch. Release is one pull request into `main` (`roles/release.md`), merged when CI is green, then check churchfamilytree.com. Open-Gaps entries go at the next free number. Promotion to `live` is Mark's call.

Commit and push as you go.

## Rulings since the README was last updated

- **Cards (Mark, 2026-11-27, "a"):** batch 12 writes the full new card for each of its 20 people; the era 1 cards thread does not touch them. In the Decision-Log.
- **Voice (Mark, 2026-11-28, via the coordinator):** "we will put any new work in sally fords voice, leave the others in neos until we replace them". Sally Ford, `kBag1HOZlaVBH7ICPE8x`, `eleven_multilingual_v2`, `mp3_44100_64`, speed 1.04; the settings go into `Brief-Kit/Recording_Settings.md` in a separate pull request. Batch 12 still records nothing; release hides each old player as planned, and a separate recording run follows.
- **Lead rulings within the kit (no Mark ruling needed, report them):** Tatian's ceiling is 675 under "lengths measured by the draft" (its recheck's 650 was set aside); Cyprian's fresh-read fix restoring Pontius's "if" clause was applied (+7) for fidelity, with the length sent to Mark.

## Waiting on Mark: page version 5

Asked, with recommendations: Tertullian heart **A**, Bardaisan heart **A**, Justin heart **A**, era 1 heart timing **b**, and accept five lengths: Josephus 778 (about 725), Peter 698 (675), era about 755 (about 730), Cyprian 1,006 (about 965), Eusebius 887 (about 850). No answer yet.

## Where each story stands

**Done to release (brief final, card written, checked and fixed, second readings set):** Clement, Ignatius, Valentinus, Pontius, Tacitus, Methodius, Origen, Pamphilus, Suetonius. Second readings: `Second_Readings_SR1.md` (22 same, 5 minor, none changing meaning), verdicts set on the cards (`Second_Readings_SR1_Applied.md`).

**Brief final, card done, second readings in progress:** Anatolius, Hippolytus, Lactantius, Tatian. Round 2 blind readings are in (`Second_Readings_Blind_A.md`, `_B.md`, ids SR2-01 to SR2-12; key `Second_Reading_Key.md`). The comparer was writing `Second_Readings.md` when the session stopped; if it is missing or incomplete, rerun the comparison (second-reader role, "The comparison") for SR2. Then rename the SR2 files with an `_SR2` suffix, set each `secondReading` on the cards as SR1 was, and confirm with `python tools/list_second_readings.py <folders>` (exit 0).

**Brief final, card held for Mark's length ruling:** Josephus (778), Peter (698), Cyprian (1,006), Eusebius (887). On "accept": `python _gen/make_card.py <slug>` from the repo root, card writer, card check, apply, then second readings. On "cut": cut at the outline with the draft in hand (`make_length.py`), targeted recheck, fresh read, then the card.

**Waiting on Mark's heart answer, then redraft:** Tertullian (on A: apply the reworded heart; on B or C see the page), Bardaisan (on A: restore "in prose and in song"; chronicle and Marcion debates to the card), Justin (on A: keep the heresies book line, pay 2 words; apply the MINORs in `Recheck_Length.md`; draft2 is kept). Each then reviews, revises and fresh-reads as the others did.

**Era 1:** outline fixed and rechecked; apply the recheck-review minors (`Recheck_Review.md`), then the reviser with Mark's timing answer (b moves the letters sentence into the Tertullian paragraph and joins the ruling sentences), then fresh reads and the era card.

## For release (gathered so far)

- `tools/quote_renderings.json`: new listings for every brief quote that is our modern English; remove the old listings each card reports (Tacitus 3, Origen 2, Lactantius 3, Ignatius, Clement and others say so in `Card_Edits.md`). Tacitus Q1: Mirbt line 2541 prints "Cliristus", an OCR misread of Christus (Hooker's print, HOOK 13988-13994).
- The full `validate-census.mjs` quote run ran out of memory in this container; run it per entry if needed.
- Entry fields: each `Card_Edits.md` lists them ("Entry fields" and "Entry fields (card check)"). Lactantius's legacy "an ancient doctor of the Church" is held (Calvin's letters, Bonnet, lines 16669-16670); gloss "doctor".
- Fleet-level, not fixed here, for Open-Gaps or Mark: `regions` "Asia Minor" on about eleven era 1 Rome entries with no source (owned by the map build slice); Tatian's "Edessa" (already in Open-Gaps); the Valentinian tradition entry's `why` breaks Valentinus's Do not say list ("Alexandrian… around 136", "divine spark"; not this batch's entry, flag only).
- Open-Gaps entries already planned: the Melitian break line and Pamphilus's census home; `check_tree_overlap` reads only `longDescription`; the prompt gap on the census `longDescription`; the outline formula undercounts drafts.
- Mark's report with the finished briefs: heart-wording changes made by checked fixes (Ignatius, Tacitus, Peter's clergy line, Clement "boy" and "pupil", Valentinus, Pontius, Methodius, Hippolytus "many other books" and the opening's Noetus question to the card, Anatolius, Suetonius, Cyprian "as Pontius gives it, that he withdrew from fear" and "and a mother", Eusebius's essence reordered, Lactantius M1 and M10, Pamphilus MINOR 12), and the long-story overruns.
