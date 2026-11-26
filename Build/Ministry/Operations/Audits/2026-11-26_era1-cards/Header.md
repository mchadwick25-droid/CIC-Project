# Batch header: era 1 card content (2026-11-26)

**Scope (Mark, 2026-11-26, verbatim):** "this should be for all era one cards now, built worlds should be exactly like all the cards in church family tree". This replaces the 12-built-worlds short-description task (`Short-Descriptions/2026-11-26_built-worlds-v2/`, halted). Launch prompt: `Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/CFT_Card_Content_Launch_2026-11-26.md`, {N} = 1. Rule: `Build/Ministry/Features/Church-Family-Tree/Stage-Two-Kit/Kit.md` (sections 1 to 3). How a card is written and checked: `Brief-Kit/roles/card.md`. Kind: tradition (`Brief-Kit/kinds/tradition.md`). Folder: `Build/Ministry/Features/Church-Family-Tree/Card-Content/2026-11-26_era-1/`.

**Fields to write, on the census entry for a tradition** (`cic-website/data/world-census.json`, `movements`; shapes in `tools/validate-census.mjs`, `checkCardLayout`): `shortDescription`, `timeline`, `briefSources`, `uncertain`, and `quotationOriginals` where the brief quotes. Shown `dates` follow the date rule (Brief Kit Part 1, Rigor; Decision-Log "A date shown follows the date rule; the map's years only place", 2026-11-26): mark any change from the census `dates`.

**Sources.** Where batch 11 rebuilt the tradition, its folder in `Build/Ministry/Operations/Audits/2026-11-25_batch-11/<slug>/`: `Source_Sheet.md`, `Outline.md`, `<slug>.card.json`, `<slug>.brief.txt` (the final brief), `Card_Check.md`. Its held card fields (`uncertain`, `quotationOriginals`; "Held, not applied" in that folder's parent `Release.md`) map across as they stand, unless they contradict the final brief or the census brief (`longDescription`). Otherwise: the census entry, its card fields and documented stories, and the held texts they cite in `cic/texts/`, each claim checked at its lines. Never rewrite the brief. Open-Gaps 429 lists years no source gives; where a timeline needs one of those, it says "date unknown" or the record's own phrase.

**Mark's rulings for the short description (2026-11-26), verbatim:**
- "a short one or two sentance description like the other cards, but the player stays on the page. something like this but simpler description". His example (the Montanism teaser): "Phrygia in inland Asia Minor, from the second century into the centuries after — a movement convinced the Spirit was still speaking, which named the town where it expected the New Jerusalem to come down." Simpler than that. The dates · place line sits above it.
- "we dont say they didnt or what they were not, only a brief description what they are, use our writing rules for this". No negatives, no contrasts.
- "i dont like these christians starting desert". No opening on "These Christians" or a like placeholder.
- "they were not monks when they left". People named by what they were at the moment described.
- "its no clear if he asked to leave or was asked and what does seized it stands alone with no context". Every phrase clear heard once.
- "i feel like you are just making these up from memory and not giving a depth thought to the accuracy and craft". Every claim on a held line that was opened and read.

**Process.** Mark sees the first two cards (Montanism, a tradition; Alexandria, a built world) before the rest are written. Write once, check once independently, fix only what fails.

## Scope widened again (coordinator, 2026-11-26), Mark's words verbatim

- "no one thread to do it, not peicemeal. we need quality cards for every era 1 tradition, people, counsils, era, stories, connections and rivers. they all have a title, context and direct line, a brief (when there is one) and other relevent information and sources"
- "this thread does what it has and when batch 12 runs it then does the card refinements like now on new material"

Batch folder is now `Build/Ministry/Operations/Audits/2026-11-26_era1-cards/`. Every card has: a **title**, a **context** (the short description, one or two sentences, to the rulings above), the **direct line**, the **brief** where one exists (never rewritten), **other relevant information**, and **sources**. Traditions, people, councils and the era follow `Stage-Two-Kit/Kit.md` section 1. A person keeps the layout fields in `card`, a council in `council`, a tradition and the era on the entry.

## First set for Mark: one card of each kind

| Kind | Card | Writer |
|---|---|---|
| Tradition | `montanism-the-new-prophecy` | card writer 1 |
| Built world | `alexandria-catechetical` (short description from `Short-Descriptions/2026-11-26_built-worlds-v2/Drafts_A.md`) | card writer 1 |
| Person | `polycarp-of-smyrna` (graded B) | card writer 2 |
| Council | `councils-of-rome-and-carthage-251` (graded C) | card writer 2 |
| Era | era 1 (`eras`, `no` 1; `kinds/era.md`) | card writer 3 |
| Story | "The Sister Who Saw Visions During the Service" (Montanism `documentedStories`) | card writer 3 |
| Connection | edge `post-apostolic-house-church--montanism-the-new-prophecy` | card writer 3 |
| River | Africa (lane 4; its record in `RIVER_ORIGINS`, `cft-website/index.html`) | card writer 3 |

## Proposed layout for the three kinds that have none (for Mark to see in the first set)

The same pattern as Stage-Two-Kit section 1: title, a dates · place line, context, direct line, the text, then a menu of the other information, then sources.

- **Story card.** Title. Dates · place: when and where the story happens, by the date rule. Context: one or two sentences, what happens in it. Direct line: the tradition and the people on the tree it belongs to (the entries it is told under, and any person entry who acts in it). The text: the story as it stands, never rewritten. Menu: Who tells it (the witness, when they wrote, and how near the event); Open questions; Sources (the old work at file and lines, with each quotation's printed wording).
- **Connection card.** Title: the two entries and the kind of link ("House churches argued against Montanism"). Dates · place: when the link was made, by the date rule. Context: one or two sentences, what passed between them. Direct line: the two entries, each tappable, with the link's kind and its confidence level in plain words. The text: the connection note as it stands; where it carries a modern view or claim its sources do not hold, that is listed for the fix, never silently changed here. Menu: Open questions; Sources (each old source at file and lines, with its quote; any modern work in a separate reading list, one line on what it covers).
- **River card.** Title: the river's name. Dates: the span it runs in this era. Context: one or two sentences, which churches it carries. Direct line: the river it leaves (its parent) and the rivers that leave it, one step each way, with how it began (lineage, declared, origin). The text: none; a river has no brief. Menu: The traditions in it this era, in time order, each with its dates and tappable; Open questions (how it began, where uncertain); Sources (the origin record's own sources).

Each writer writes, for each card, `<id>.layout.json` (the fields as the census would hold them; for a story, connection or river, the proposed fields) and `Card_Edits_<id>.md` (every field and line with its evidence: claim | work | file | line | short verbatim quote). An independent checker who wrote none of them then checks all eight.

## Correction: the full section set (coordinator, 2026-11-26), Mark's words verbatim

- "the list i had on the cards was not exhastive, the format we have for traditions and the sections is fuller,"
- "i want timelines on all the people, era and river cards too"

Mark's short list is the minimum. Every card gets the full section set of Stage-Two-Kit section 1: on screen first, the short description, the direct line, then the player; below, the brief (Read along) with its short list of old sources; then the menu: **Timeline; People and stories; the kind's own sections; Connections; Legacy and today; Open questions; Sources, with Modern works kept apart.** (Approved mock: https://claude.ai/artifact/Ude7ZA3Bzjvegoj63YRvDi.) Person, era and river cards each have a Timeline built like a tradition's. Where a section has no held material yet, the card says so plainly.

Proposed full sets for the three new kinds, at a tradition card's depth:
- **Story:** short description; direct line (the entry it is told under, and each person entry who acts in it); the text, with its source list; Timeline (the story's events in order, each with its reference, and when its witness wrote it down); People and stories (who acts in it, by what they were then; sibling stories); the kind's own section, **Who tells it** (the witness, when they wrote, how near the event, and what the listener must know); Connections (entries it ties to); Legacy and today (who later kept or quoted it, from held lines); Open questions; Sources, with Modern works apart.
- **Connection:** short description; direct line (the two entries, each tappable, the link's kind and confidence in plain words); the note; Timeline (the dated points that make the link, each with its reference); People and stories (the people and documented stories through whom it passed); the kind's own section, **What passed** (what specifically went from one to the other, on held lines); Connections (other links between the same two entries or their rivers); Legacy and today; Open questions; Sources, with Modern works apart.
- **River:** short description; direct line (its parent river and the rivers that leave it, one step each way, with how it began); no brief; Timeline (its traditions and turning points in time order, in periods); People and stories (the traditions on it this era, in time order, each tappable, then its people); the kind's own section, **How it began** (the origin record, its basis and confidence); Connections (links that cross into or out of it); Legacy and today (the living traditions it carries, from the census `living` evidence); Open questions; Sources, with Modern works apart.

## The card standard (Mark, 2026-11-26, verbatim)

"we want the same craft, rigor and accessability we had for the briefs, but in a card form not narritive for audio."

Every text on a card (short description, timeline headlines and lines, open questions, the kind's own section, legacy lines, notes) meets Brief Kit Part 1 in full: its Craft, Rigor and Accessibility, the four faults, and the bar in Part 3. What changes is the form only:
- **Written to be read and scanned, not heard.** Each line stands on its own and is clear read once, out of order, with no line leaning on the one before it.
- **No narrative moves.** No opening scene, hook, held-back reveal, story arc or closing image; those belong to the brief. A timeline line is one plain fact with its date and reference; a headline names what happened in that period.
- **Kept from the briefs, unchanged:** explain it or leave it out; plain, precise modern words; every claim on an old source at its lines; a wonder, judgment or enemy's charge in its witness's voice; uncertainty stated plainly; no modern view, date or identification as content; no stock words, no "not X but Y", no dash for drama.
- **Accessibility:** reading grade 8 to 10 and reading ease 60 or more for each card's running text (`python -m engine.m1.profile_readability` on a plain file of it), short sentences, one idea each, a church word glossed where it is first met on the card. Mark, 2026-11-26, verbatim: "10.1 is ok for the card as there are a lot of names and references". So on a card, a full-text grade a little over 10 that comes from names and references passes when the scorer's names-out grade is within the limits; it is a warning, never a reason to split or reword.
- The checker reads every card text against this, as the reviewer reads a brief, and blocks on the same faults.

## Dates from the sources' own clues

Mark, 2026-11-26, verbatim: "we can use some logic to get the dates, if there are sources that give us clues we can also say around 410 to 430 if there is truelly no way to figure it out". So a shown date may be worked out from the old sources' own clues (a regnal year, a consul, a named bishop or ruler, an event the source ties it to), with the working shown in `datesNote` or the timeline line's reference ("the eleventh year of Yazdegerd, so about 410"). Where the clues give no single year, give the range they allow ("around 410 to 430"). Only where nothing in the sources narrows it does the line say "date unknown" or the record's own phrase.

## Modern works on the cards

Mark, 2026-11-26, verbatim: "the modern sources can be included in the cards as places for further research or checking credibility if they are historical and not speculitive". A modern work of historical scholarship (an edition, a translation, a reference history, a chronology) may be listed in a card's Modern works, as a place for further reading or for checking the card's credibility, with one line on what it covers, never what it argues. It is never the source of a claim, date or identification in the card's own text or timeline, and a year that only modern reckoning gives is not stated on the card; the work that reckons it may be listed. Speculative or argued work (reconstructions, contested identifications, hypotheses) is left out. This sits inside "The brief kit consolidated: one standard, six kind kits" (2026-11-24), decision 6 ("modern works are a reading list only ... No modern opinion, date or identification appears anywhere on the tree"; Open-Gaps 409), and does not change it.
