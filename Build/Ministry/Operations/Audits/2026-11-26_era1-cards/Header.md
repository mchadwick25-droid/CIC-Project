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
