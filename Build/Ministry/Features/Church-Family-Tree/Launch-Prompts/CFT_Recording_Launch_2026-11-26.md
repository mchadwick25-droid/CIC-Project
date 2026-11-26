# Church Family Tree: recording batch 11's tradition briefs (2026-11-26)

Paste the part below the line as the first message of a new session.

---

Record the batch 11 tradition briefs that have no current recording, so the new briefs are live with audio. Read `CLAUDE.md` ("Usage/credit discipline": paid bulk runs), `Build/Ministry/Features/Church-Family-Tree/Stage-Two-Kit/Kit.md` (section 4, Recording) and `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Recording_Settings.md`.

**The briefs.** `antiochene-church-third-century`, `roman-church-third-century`, `apocryphal-and-pseudepigraphal-literature`, `ebionite-nazoraean-current`, `greek-apologists-second-century`, `latin-apologists`, `manichaeism`, `marcion-marcionism`, and the three built worlds `alexandria-catechetical`, `syriac-edessa-nisibis`, `post-apostolic-house-church`. Montanism is already recorded. Check `latin-pastoral-congregational-christianity` too: it is a built world whose current recording may be its world story rather than its new brief.

**First, the built worlds.** A built world's card may play its own world narration rather than the tree recording. Find what each of the four plays today, and whether the new `longDescription` would be heard once recorded. Report it before recording them. List any built-world recording that does not fit the card structure of the Stage Two Kit, for Mark: none is removed until he has seen the list.

**The run.** Daniel's tradition settings, every one passed on the command, one story per command, as `Recording_Settings.md` gives them. Two runs, each under 25,000 credits, as Mark approves them in his own words (quote them in `--approved-run`). Print and check the settings and counts before each run; read the balance before and after. Then `python Build/tools/align_tree_narration.py --only <ids>` and its `--check`. A recording replaces the old one for that brief; remove nothing else.

**Release.** One pull request into `main`, merged when CI is green; then check on churchfamilytree.com that each player shows, with Read along. Open-Gaps entries at the next free number. Report to the coordinator.
