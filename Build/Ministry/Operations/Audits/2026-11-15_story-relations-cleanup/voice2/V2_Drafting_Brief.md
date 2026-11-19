# Brief: "How it connects" lines for Church Family Tree story cards, new voice

You draft the "How it connects" line for a set of story cards on the Church Family Tree (a public map of Christian traditions). Each story card already has a title, teaser, text, caveat and sources. "How it connects" is one small section of the card, read in 10 to 15 seconds. It tells the reader how this story links to traditions on the map, and why that link matters.

## Read first
- /home/user/CIC-Project/CLAUDE.md, the sections "Trust and source fidelity" and "Accessible and rigorous".
- /home/user/CIC-Project/Build/Ministry/Operations/Audits/2026-11-15_story-relations-cleanup/Handover.md (Mark's decisions, the four approved two-sentence cuts, known traps).
- /home/user/CIC-Project/Build/Ministry/Operations/Audits/2026-11-15_story-relations-cleanup/Voice_Samples_Approved.json (eight samples Mark approved as the voice; they run long, the rule below came later).
- /home/user/CIC-Project/Build/Ministry/Operations/Audits/2026-11-15_story-relations-cleanup/Old_Line_Claims.md (claims in the old lines that had no card or census support; do not carry them forward unless you find support).

## Your inputs
Each story is a packet at scratch/pk/NN_<id>.json: the card fields, `line_live_now` (the line on the live site), `line_first_rewrite_rejected` (a rewrite Mark rejected as "too factual, no color"), and `linked_census`: the census entries for the traditions the card links to. Every census tradition is listed in scratch/census_index.txt (id | name | short name | dates | region), and its full entry is scratch/mov/<id>.json if you need one the card does not link.

## The rules (Mark's, converged)
1. Exactly two sentences. No exceptions. About 35 to 45 words in all. A semicolon does not make a third sentence acceptable; avoid using semicolons to smuggle one in.
2. The first sentence gives the connection: which tradition(s) this story belongs to or links to, named in words, and how. The second says what the connection shows: why it matters. Not a scene, not narrative, not a retelling of the story.
3. Every claim, including the "what it shows" sentence, must be supported by the card's own text, teaser, caveat or sources, or by a census entry. Hedges in the source stay ("reportedly", "tradition says"). Nothing invented, nothing inferred beyond what a reader of those texts would accept as said. An honest limit or a correction is folded into the two sentences, never a third.
4. Name a tradition by its census short name (e.g. "Scattered Households", "Latin Pastoral", "Church of the Desert", "Arab Evangelicals"), or its full name where the short name would mean nothing to a reader. Never an id. Never talk about the data: no "records", "entry", "row", "lane", "census", "placed", "the map has", "coverage". Speak of the traditions and the people, not the site.
5. Cut the scaffolding. Don't restate the card's list of nearby traditions. No setup clause before the point. Don't repeat what the card's text already tells at length; use it only to carry the link.
6. Voice: craft and rigor side by side. Story-led in the sense that the link is told through people and events, with the reason joined to the act ("so", "because", "which"). Serious adult register (BBC News, National Geographic). Readable aloud in one breath per sentence; aim for about 15 to 25 words a sentence, never a nested clause inside a clause. Not a children's book.
7. No AI tells: no "not X but Y" or "X, not Y" contrasts, no colon reveals, no rhetorical questions, no aphorisms or quotable tag lines, no triads or doublets for rhythm, no dash fragments (avoid dashes entirely), no unearned adjectives ("remarkable", "powerful", "profound", "striking", "vivid"), no hedging filler, no "a testament to", "underscores", "highlights", "serves as", "speaks to". Loose quantifiers ("only", "first", "never", "always") only where the source says so.
8. A person whose name could mean more than one person gets "name of place" at first mention.
9. Known traps (from the first rewrite's reviews): Abercius's 'the same faith' cannot be quoted (no held text); Anatolia is not Pliny's province; four home traditions exist in the census (Hungary Protestants, Catholics of Ceylon, Arab Evangelicals, Maronites 1815-1906); the Amish split is within the Anabaptist family; Olympias was an ordained deaconess; Abitinae's break is "reportedly"; "towns of Lombardy" on the Great Alleluia has no support (the card says "cities of northern Italy").
10. Where the card links a tradition the story does not truly belong to (a neighbor in time or place), say so honestly within the two sentences rather than inventing a link.
11. For the four stories with approved two-sentence cuts in the Handover (Lay, Abitinae, Nickel Mines, As'ad), use those cuts as given unless one breaks a rule above; if so, say why in your note.

## Output
For each story write scratch/draft/NN_<id>.json (same NN and id as the packet), JSON:
{"id": "...", "line": "the two sentences", "support": [{"claim": "short paraphrase", "source": "card text | card teaser | card caveat | card sources | census <id> <field>", "quote": "the exact supporting words, copied verbatim"}], "note": "anything a reviewer should know, or empty"}
Every claim in the line gets a support item with a verbatim quote. Write valid JSON (escape quotes). Use only the Read and Write tools. Do not edit anything in the repository.

When done, reply with one line per story: NN id, word count, and any story you were unsure about and why. Do not paste the lines back.
