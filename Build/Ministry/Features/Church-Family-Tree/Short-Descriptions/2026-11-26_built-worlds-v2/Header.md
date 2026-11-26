# Batch header: short descriptions for the 12 built worlds, round v2 (2026-11-26)

**Kind:** tradition (`Build/Ministry/Features/Church-Family-Tree/Brief-Kit/kinds/tradition.md`). **Step:** card (`roles/card.md`), the `shortDescription` field only, as `Build/Ministry/Features/Church-Family-Tree/Stage-Two-Kit/Kit.md` section 1 defines it: "one or two sentences, written fresh at the card step and checked like the brief." It sits on the card's screen under the name and a "dates · place" line, above the player. **Folder:** `Build/Ministry/Features/Church-Family-Tree/Short-Descriptions/2026-11-26_built-worlds-v2/`. **Census:** `cic-website/data/world-census.json` (`movements`, by `id`).

## The twelve (slug — world folder)

1. post-apostolic-house-church — `Build/worlds/pahc/`
2. alexandria-catechetical — `Build/worlds/alx/`
3. syriac-edessa-nisibis — `Build/worlds/syr/`
4. desert-monasticism — `Build/worlds/desert/`
5. cappadocian-nicene-pastoral-monastic-tradition — `Build/worlds/cappadocian/`
6. imperial-juridical-christianity — `Build/worlds/ijc/`
7. hieronymian-ascetic-literary — `Build/worlds/hal/`
8. gallic-monastic-ascetic-christianity — `Build/worlds/gallic/`
9. the-reformed-cities-zurich-and-geneva — `Build/worlds/rzg/`
10. donatism — `Build/worlds/don/`
11. lutheran-wittenberg-and-its-congregations — `Build/worlds/witt/`
12. latin-pastoral-congregational-christianity — `Build/worlds/lpc/`

Each also has a world record `cic-website/data/worlds/<slug>.json`. The census entry's `longDescription` (the brief) and `sources` are a starting list, never a source: every phrase on the card rests on a held line in `cic/texts/` that you have opened and read. Nothing from memory.

## Job

One or two plain sentences that say what this community was: who they were and what they did or held, so a visitor meets them at a glance and stays on the page. Simpler than Mark's model.

## Mark's rulings for this batch (2026-11-26), verbatim

- "a short one or two sentance description like the other cards, but the player stays on the page. something like this but simpler description". His example (the Montanism teaser): "Phrygia in inland Asia Minor, from the second century into the centuries after — a movement convinced the Spirit was still speaking, which named the town where it expected the New Jerusalem to come down." Simpler than that. Time and place are already on the dates · place line, so the description need not repeat them.
- "we dont say they didnt or what they were not, only a brief description what they are, use our writing rules for this". No negatives, no contrasts, nothing they did not do or were not.
- "i dont like these christians starting desert". No opening on "These Christians" or a like placeholder.
- "they were not monks when they left". Name people by what they were at the moment described, never by what they later became.
- On a draft of the Gallic card: "its no clear if he asked to leave or was asked and what does seized it stands alone with no context". Every phrase clear heard once: nothing hanging, no context missing, no act without who did it.
- "i feel like you are just making these up from memory and not giving a depth thought to the accuracy and craft".

## Standing points for this batch

- Part 1 of the Brief Kit governs: plain words, explain-it-or-leave-it-out (a named thing says what it was), a wonder or judgment stays in its witness's voice, no modern view, no stock words, no dash for drama. Reading grade 8–10, ease ≥ 60 (`python -m engine.m1.profile_readability <file>` on a plain-text file of the card). Name a person only if the card says what they did.
- One held finding from the rejected round: in the house-church card, only Ignatius greets a church's households (Smyrnaeans 13; To Polycarp 8). The churches did not greet one another household by household.
- The rejected drafts are on branch `origin/claude/built-world-short-descriptions` (`git show origin/claude/built-world-short-descriptions:Build/Ministry/Features/Church-Family-Tree/Short-Descriptions/2026-11-26_built-worlds/Drafts_v2.md`). The writer may read their evidence tables for leads to source lines. Write fresh; never reuse their sentences.

## The dates · place line

The date rule is Brief Kit Part 1, Rigor ("A date the old sources fix, or one so settled it is Widely Accepted ... is told plainly; a date that rests on one editor's reckoning is told only as roughly as the old sources allow ... An entry's `start`, `end` and `activeYear` only place it on the map; its shown `dates` ... follow this rule"), with Mark's ruling "A date shown follows the date rule; the map's years only place" (Decision-Log, 2026-11-26; its model: "4th c.; wrote the Panarion c. 375"). For each card give the shown `dates`, and the place from the census `placeLabel`. Mark every change from the census `dates`, with the held lines (or Widely Accepted event) that set each end.
