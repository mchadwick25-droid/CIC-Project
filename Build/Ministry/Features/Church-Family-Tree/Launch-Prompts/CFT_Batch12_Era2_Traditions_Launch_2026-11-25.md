# Church Family Tree, batch 12 (era 2, traditions): launch

Paste this as the first message of a new session.

---

Run Church Family Tree batch 12 end to end on the brief kit. Read `CLAUDE.md`, then `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`. The kit and its role prompts in `Brief-Kit/roles/` hold every standing rule. Each agent gets its role prompt filled in with the batch header the kit describes, and nothing else.

**The group.** Thirteen era 2 traditions, in two halves, through `Brief-Kit/kinds/tradition.md`: Mark's ruling in the Decision-Log entry "Era 2 traditions: thirteen rebuilt now, ten pushed off" (2026-11-25). Half A: `desert-monasticism`, `gallic-monastic-ascetic-christianity`, `donatism`, `armenian-christianity-conversion-era`, `jerusalem-liturgical-pilgrimage-christianity`, `persian-church-of-the-east-early`, `anomoean-eunomian-christianity`. Half B: `antiochene-exegetical-christianity-chrysostom-ce`, `aquileian-christianity`, `homoian-arian-christianity`, `pneumatomachian-current`, `priscillianist-asceticism`, `cappadocian-nicene-pastoral-monastic-tradition`. The four built worlds among them (`desert-monasticism`, `gallic-monastic-ascetic-christianity`, `donatism`, `cappadocian-nicene-pastoral-monastic-tradition`) also rebuild their census `entry` texts, Open-Gaps 416. Antiochene Exegetical and Priscillianist Asceticism are siblings of batch 10's `john-chrysostom` and `priscillian`; each is researched after its person's text is settled (Open-Gaps 408). Each live `longDescription` is a text approved before the kit, reviewed here; the writer keeps its wording wherever it passes. Each one's grade and main fault are in `Build/Ministry/Operations/Audits/2026-11-25_tradition-grades/Grades.csv`. Before the slate, run `python tools/list_story_status.py --write` and read Era 2 in `Story-Ledger.md`.

**Where things go.** The batch folder is `Build/Ministry/Operations/Audits/<date>_batch-12/`, with a README that carries each story's step, the open items and this batch's rulings, so a fresh session can pick up from it. The batch 11 folder (`Build/Ministry/Operations/Audits/`, named `<date>_batch-11`) shows what each step's records look like.

**Step 0, then stop for Mark.** One page (an Artifact): each story's job in one line, its half, its census home and that tradition's direct line as its card shows it, with any descent or break the story will tell that the census lacks or contradicts, its siblings, and the live stories it sits beside. Name each quote already used elsewhere on the tree, and any reuse the kit's quote rule would allow. Run `python tools/check_tree_overlap.py` once on the old texts. Research starts only after Mark approves.

**Stops for Mark:** the slate; the hearts and lengths page; the first two finished briefs, before any other is written; a brief that still fails after its one revision; a sibling or shape question; the recording approval, in his own words with a credit cap; and the first recording, for his ear.

**Recording.** The settings in `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Recording_Settings.md`, each passed on the command. Run one story per command.

**Release.** One pull request into `main`, merged when CI is green, then check churchfamilytree.com. Open-Gaps entries at the next free number. Promotion to `live` is Mark's call. Do not write the next batch's launch prompt unless Mark asks; when he does, fill in the blanks of `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Launch_Template.md` and change nothing else.
