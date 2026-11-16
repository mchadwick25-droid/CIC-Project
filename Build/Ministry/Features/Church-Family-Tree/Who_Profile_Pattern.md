# Who profile pattern

Approved to proceed (Mark, 2026-11-11). The one pattern every Who profile, story and listed line is written to. Rulings and their reasons are in `Decision-Log.md`, "The Who profile pattern" (2026-11-11).

Standard v1 approved to proceed (Mark, 2026-11-16: "yes this is a much better revision, i approve to move forward"). It adds the rulings of the Gregory of Tours and Benedict of Nursia test to this pattern, in "Standard v1: setting, impact and witnesses" below, and replaces the rules they supersede. The rulings are in `Decision-Log.md`, "The Who brief: what Mark has ruled so far, from the Gregory of Tours and Benedict test" (2026-11-15), and "Standard v1 approved to proceed" (2026-11-16).

## The writing standard this rests on

This pattern adds nothing to how the words are written beyond the newer standards of 2026-11-11 and 2026-11-15 listed below and the readability method. It adopts the standard behind the tradition cards and the eight early-church person briefs, by reference. Mark: "we use the same principles we used to develop the tradition cards, simple modern english with the accessability and no ai tells etc. it is a full design i dont want to repeat, no tails, no statements that have no context or meaning no xy no wise saying etc. find the quality and follow it."

| What | Where |
|---|---|
| Reading level, register, plain-language rules | `CLAUDE.md`, "Accessible and rigorous"; `Build/reference/method/Pass2-decisions/VR_1A_NorthStar_Readability_Target_2026-08-09.md` and `VR_1A_Writing_Standard_2026-08-09.md` (same folder) |
| No invention, quotes checked against the vendored file, the five confidence levels | `CLAUDE.md`, "Trust and source fidelity" |
| The five review questions and the named failures (1.3 to 1.12: dash fragments, triads, unearned adjectives, hedge calibration, anachronism, contested claims told as settled, terminology drift, stale cross-references, status-announcement register, questions that must match the source) | `Build/reference/method/CiC_Voice_Style_Guide_and_Scaling_Plan.md`, 1.1 to 1.12 |
| How a brief reads aloud: story, natural years, named witnesses, flowing sentences | `Decision-Log.md`, "Person briefs: 60 to 120 seconds, personal and theological" (2026-11-11) |
| Jon v4 voice, settings and audio tags | `Decision-Log.md`, "Person voice: Jon on Eleven v4, replacing David Baker" (2026-11-11) |
| The per-turn readability score | `engine/m7/turn_readability.py` through `engine.m1.gates.grade_text` |
| The profile readability check | "The readability method", below |

## Newer standards the tradition-card standard does not cover

Made on 2026-11-11 and 2026-11-15, and in the Decision-Log. They apply to every participant-facing person text: briefs, cards, stories, tree pages and council Who lists.

- **Common names (Mark, in three steps: "if a name is common we need to clarify from where"; "dont forget the newer ones like name full or place of common names like we did for socratise").** At its first mention in a text, a name that could mean more than one person gets its name with a place, in the form scholars use (Mark: "socrates from constantinopel"): "Socrates of Constantinople", "Eusebius of Caesarea", "Palladius of Helenopolis". A role or a time is added only where the place does not identify the person. The corrected texts of the eight carry it. The brief and the card are separate texts and each has its own first mention. The identifier comes from the vendored sources and adds no claim. It covers the subject's own name too ("Gregory of Nazianzus came to Constantinople") and any name a general listener would not know, since Mark also says "no statements that have no context". Where no vendored source gives a place, the name is left as the sources have it and the gap is logged.
- **Real witnesses named.** "Eusebius says", "Palladius tells", "his own letters say". Never "his editor", "the translator" or "a modern scholar". Under Standard v1 a witness is named only where trust turns on it, and no modern scholar is named in the brief ("Standard v1", below).
- **Natural dates.** Years are written to be spoken naturally.
- **Hostile witnesses.** Named, with polemic marked as polemic and its owner named.
- **Jon audio tags.** In the audio script only.
- **Craft.** Mark, 2026-11-15: "Craft is also good story telling and flow, no ai tells hanging sentences and everything is relevant to the story." And on 2026-11-11: "i want it a little more story telling, not fact giving ... the sentences flowing together not all short simple sentances for an elementary student." Five tests follow from his words. Each is applied to the whole brief, read beside the eight, and never one sentence at a time (checklist item 10):
  1. **Good storytelling.** The brief reads as one story with a line through it. It is not a list of facts.
  2. **Flow.** Each sentence leads into the next, and ideas are joined: where the source gives a reason or a result, it stands in the sentence with the act.
  3. **No AI tells**, as `CLAUDE.md` defines them: no hedging filler, no assistant cadence, no telltale phrasing, no generic polished voice.
  4. **No hanging sentences.** No line stands alone, unconnected to what comes before or after it. No closing punchline or quotable tag line is put there for effect.
  5. **Everything relevant to the story.** Every sentence serves this person's story. Source talk, editors and side facts that do not serve it go to the card.
- **The floor.** Grade 8 is a floor that fails (Mark, 2026-11-15: "The floor is the biggest concern, this is not a kids book"). It is not a target. A brief below it is rewritten so its sentences carry more of the story. It is never padded with longer words.

The Style Guide says it is not a banned-word list and must not become one. Its test: for each sentence, name the source that makes it true and what the source does not establish. The checklist below points to the Style Guide's sections and does not copy them.

## The bar: the eight early-church briefs

Mark, 2026-11-15: "Restore the eight, fix their small flaws." The model for a Who brief is the eight early-church briefs, in their corrected texts at `Who-Profiles/bar/`: `origen.brief.txt`, `methodius-of-olympus.brief.txt`, `constantine-the-great.brief.txt`, `athanasius-of-alexandria.brief.txt`, `ephrem-the-syrian.brief.txt`, `gregory-of-nazianzus.brief.txt`, `gregory-of-nyssa.brief.txt` and `john-chrysostom.brief.txt`. A writer reads all eight before drafting. A reviewer reads the brief under review beside them. No one writes or reviews against the latest batch.

Standard v1 adds two examples for the opening, the witnesses and the impact half: `gregory-of-tours.brief.txt` and `benedict-of-nursia.brief.txt`, in the same folder. The eight stay the bar for prose. On 2026-11-16 the eight were themselves brought up to Standard v1 (Mark: "Revise, then record (Recommended)"), and their quotations from English printed before 1931 were put into our modern English. The model passages quoted in this section and in checklist item 10, and the figures in this section and in "The readability method", come from the eight's earlier corrected texts, kept in git at commit `4f1b754d`. They still show the craft they are quoted for. The current texts and their figures are in `Who-Profiles/bar/` and its README.

The `post-apostolic-house-church` entry remains the Style Guide's exemplar for a tradition card. It is not a model for a Who brief: it scores grade 12.3 and reading ease 46, and would fail this pattern's own readability check.

What the eight do, and what every brief is held to:

- **They tell a story.** Each opens in a moment (Standard v1 now puts the setting first) and follows a life through what happened next. No two are built alike: Methodius opens on a witness's odd story, Gregory of Nazianzus on an arrival, Athanasius on a severed hand. The order under "The brief" says what a brief holds, and each brief finds its own shape within it.
- **They join ideas.** An act stands in one sentence with its reason or its result: "In his eighteenth year he took charge of teaching the faith in Alexandria, because everyone else had fled." "Ephrem feared the people would absorb them, so he wrote hymns that held the church's doctrine and used the same melodies."
- **They say why the person mattered, as an idea.** Athanasius: if the Son were only a creature, his becoming man would have changed nothing for us. Gregory of Nazianzus: the orations defend the Trinity against two named errors. Origen: Scripture has body, soul and spirit, and what each does for a reader.
- **They carry evidence inside the story.** An ancient witness is named (Standard v1 now names one only where trust turns on it), with his leaning in a few words ("who tells it with plain sympathy", "so he is not a neutral witness", "years later and under oath"). A second witness is set against him where one exists, and the telling moves on.
- **They let length follow the person.** Methodius, with little known, takes about 240 words.
- **They are written for adults.** The register is BBC News or National Geographic: serious, vivid, clear. Measured, the corrected texts run grade 8.9 to 9.6, 15 to 20 words a sentence, and about one joining word in every hundred.

The live text and audio of the eight change to the corrected texts when they are re-recorded (Open-Gaps, "The eight's corrected briefs are the bar; the live text and audio wait for re-recording", 2026-11-15). Until then the files in `Who-Profiles/bar/` are the bar, and the live text is not.

## Standard v1: setting, impact and witnesses

Approved to proceed (Mark, 2026-11-16: "yes this is a much better revision, i approve to move forward"). From the Gregory of Tours and Benedict of Nursia test. Mark's read of the briefs before it: "they are ok, but still seem disconected from history, just a story about someone", and "i felt like both were more stories than significant impact on church history and theology". The examples are `Who-Profiles/bar/gregory-of-tours.brief.txt` and `benedict-of-nursia.brief.txt`.

- **The Who test.** Mark accepted a significance test: "yes, or defended". A Who changed or defended church history or theology beyond their own house or town, and the held sources show it. Recorders stay Whos ("we need to include people like him as who's", 2026-11-11). A Who that fails the source test or the significance test moves to Story (documented), Story (legend), a mention without a card, or out of use.
- **Their own sources.** "we need to make sure the who and counsils are drawing from their own sources not sources writen 1000 years later". From the legend check: "it was about it calling legends true who profiles". A Life written long after is never told as fact. Where it is the record, the brief says so plainly, and its wonders are told as that writer's ("Gregory tells that").
- **The shape.** "do you remember the shape of the story, personal and then impact". The brief tells the person first, then the impact, with no headings or lists. It moves from the moment, to the thread of what they inherited and passed on, to what they changed or defended.
- **Each stance with its consequence.** Impact is the end of the story: "it told what he stood for and who against (trinity), but it doesn't tell the end of that story, what happened because he stood up agains the king". It is told as a consequence: "it read like two seperate stories not a consequence". The brief says what they stood for, then what came of it. A causal claim needs a source that makes it: the person's own words or a held witness. Where the sources give only the order of events, the brief says what the person believed came of it, or says plainly that the record shows what followed but not why. Where the record stops, the brief says so.
- **More than one stance.** "it can be more than on thing, if they had several things then they should be told". Each is told as stance and then consequence, ordered by weight. A real one is not cut to keep to one thread, and a weak one is not added to fill space.
- **The opening setting.** "we can be clearer up front to the time and place and context of the story. dates and location." The first two or three sentences give when (a clear year, or "around 570"), where (a place and its region), the tradition, and what was going on. Then the scene.
- **The tradition.** "i think we should mention the tradition they are a part of if they are". The opening names the person's tradition on the tree, in plain words and as it appears in `cic-website/data/world-census.json`. Where they belong to none, or the link is only one of time or place, it is left out.
- **Witnesses.** "do we need to have everything referenced in the story, like who says what". Mark said "yes" to naming a witness only where it changes how far to trust the point. In practice, this pattern reads that as: the person's own words, a partisan or hostile witness, a point resting on one source, a wonder or legend, or a contested point. Documented and widely accepted facts are told plainly.
- **No later scholars.** "what do you think about all the references to later scholors". Mark said "yes" to leaving modern scholars out of the brief. A claim that rests only on a modern scholar goes to the card, under What is uncertain or Sources.
- **References listed below.** "we will also have the references listed below". Under each brief the visitor sees its references: the card's Sources in its two groups, and a short list of what the brief draws on, as work, edition and the part used. Every claim the brief tells without a named witness can be traced there.
- **Length.** "target under 2 minutes, can streatch to 2:30 if needed, no hard cap" ("The brief", below).
- **All of it together.** "lets not loose the craft, rigor and access to what we talked about, it need all". Standard v1 is added on top of the craft tests, the rigor rules and the readability method. It replaces none of them. A brief that fails any of craft, rigor, access, or the shape with its length is not ready.
- **Quotation marks and reviews.** Both points once left open are ruled (Mark, 2026-11-16): quotation marks in "The brief", Quotes, and the review process in "How a batch is reviewed and released". Standard v1 has no open points.

## The brief

- **Length.** Mark, 2026-11-15: "target under 2 minutes, can streatch to 2:30 if needed, no hard cap". At about 150 spoken words a minute, that is under about 300 words, stretching to about 375. A brief is shorter where the sources are thin, as Methodius is. It runs past 2:30 only where the content demands it (Mark, 2026-11-15, to the coordinator: "we are ok to go long if the content demands it"), and the batch note then says in one line why. A brief is never cut to fit a number, and never filled to reach one. Padding (a repeated point, a scene that serves neither the story nor the impact, colour with no source) is cut; sourced substance and a real stance with its consequence are not. One that falls short of the standard is rewritten.
- **Opening.** Setting first, then the scene (Standard v1). The first two or three sentences give when, where, the tradition, and what was going on. Then one sourced moment.
- **Order.** Personal first, then the impact (Standard v1). Personal: the setting, the scene, who they were, their story. Impact: each position they fought for, developed or defended, or for a recorder what they recorded, each followed by what came of it; the thread of what they inherited and passed on; and the close, which says what they changed or defended with its witness. One line in their own words where the Library holds them.
- **Disputes in place.** A contested point is told where it arises, with its witness named. The brief does not save it for the close. Facts the card already shows (dates, place, role, works) are not repeated as a list.
- **Witnesses and evidence.** Under Standard v1, the brief names a witness only where trust turns on it ("Standard v1", above). Where it names one, it names the real ancient witness: "Eusebius of Caesarea says", never "his editor". A witness gets his leaning in a few words the first time it matters ("who tells it with plain sympathy", "so he is not a neutral witness"). Once a witness is named, the sentences that follow need not name him again, but only while each of them is carried by that witness. A claim from any other source names its own. A partisan witness is placed once and said to be partisan. A modern editor, translator or historian belongs on the card and never in the brief: by name under Sources, and with the doubt he raises under What is uncertain. The records hold the file and lines for every claim. In the brief:
  - What an ancient witness carries is told with that witness where trust turns on it, and plainly where it is documented or widely accepted.
  - What only a modern scholar establishes (a date he reckons, a count, an attribution, a judgment on a manuscript) goes to the card, under What is uncertain or Sources. It is never told flat in the brief, and never given to an ancient writer. This replaces the earlier option of naming the scholar in a clause (Standard v1).
  - A dispute that bears on the story is told in the brief where it arises, with each side named, in a sentence or two. Only a dispute over a date or a manuscript reading that bears on nothing else goes to What is uncertain, and the brief then claims only what both sides accept ("in the 590s") (Mark, 2026-11-15).
  - How a text reached us (editions, manuscripts, printings) is not a paragraph of the brief. Where it bears on trust, one clause says so, through ancient witnesses: "We read that book mostly in the Latin of Rufinus of Aquileia, and Jerome said Rufinus changed it."
- **Dates.** A clear year, or "around 570", in the opening setting (Standard v1). This replaces "round anchors and relative time first". Years after that are written to be spoken naturally, with a bare year only where the year is the event (working rule A64).
- **Common names.** An identifier at first mention, in the brief and again in the card (the 2026-11-11 common-name standard). It comes from the vendored sources and adds no claim.
- **Audio.** `[calmly]` opens the audio script. `[warmly]` goes before the closing line. The tags are never in the census, the card or a page. There is no intro: person audio is the brief only.
- **Quotes.** Short and plain, verbatim from the vendored file. Where a line is foreign-language, long or archaic, there are two kinds of telling, kept apart (Mark, 2026-11-16: "Two kinds, kept apart (Recommended)"):
  - **A close rendering** covers every clause of the line, adds nothing, and is checked against the original. It may carry quotation marks, labelled as our modern English ("in modern words"), and it is listed in `tools/quote_renderings.json`. Per `CLAUDE.md`, Opus authors any rendering that carries marks.
  - **Rendered at the point of use, and checked twice** (Mark, 2026-11-16: "Render at point of use, re-check the 14 (Recommended)"). A close rendering made for a brief or card is a passage rendering. Opus renders it. A second Opus agent that has not seen the first renders the same lines on its own. The two are compared. Any difference in meaning is marked as uncertain on the card, and both readings are kept in the record. Only then may the rendering carry quotation marks. Writers read the originals directly; there are no bulk finding guides for eras 1 to 7.
  - **Older forms count as foreign** (Mark, 2026-11-16: "Treat old forms as foreign (Recommended)"). Old and Middle English, Middle High German and other older stages of a language get the same two-rendering check as Latin. A modern telling without quotation marks names its source, as before.
  - **Every English quotation printed before 1931** (Mark, 2026-11-16: "we even treat english from 1850s needing translation", then "Yes, every quote before 1931 (Recommended)"). A quotation the tree takes from an English text printed before 1931 is spoken and shown in our modern English, labelled as ours, and gets the same second rendering as Latin. The printed wording, with its file and lines, stays on the card under the references. One line under each brief on the page says its quotations are in our modern English; nothing is added to the spoken text (Mark, 2026-11-16: "One note per brief (Recommended)"). This replaces the earlier rule that a 17th- to 19th-century English translation is quoted word for word where it reads plainly.
  - **A looser telling** never carries quotation marks. It names its source and does not claim to be the quote.
  This supersedes the batch calls of 2026-11-14 that dropped the marks.

### A founder known through hostile witnesses

Marcion and Valentinus. Mark: "teaching two, life one". The teaching needs two independent witnesses. The life outline may rest on one if the brief says so. Epiphanius drawing on Irenaeus is one witness. The brief says early that the account comes through opponents, marks polemic as polemic, names whose it is, and separates what the witnesses agree on from what rests on one.

## The card

Mark's converged order, from "The people layer" (2026-11-11): name and other forms; known for; dates, place, tradition, role; the brief and its length; key works (three at most); Legacy in two parts, "What traces to them" and "How they're remembered"; What is uncertain; links on the map; Sources in two groups, "Their own words" and "Written about them". A missing field is absent, never filled. What is uncertain opens with the brief's own caveat, then more, each item naming its witnesses.

## The story

For a compelling testimony: someone worth telling in their own right who did not shape the church. Writings they left support the story. There is no theology beat. A first-person account carries the story in the person's own words. Where a claim matters, the story names its witnesses and marks a later or legendary source as such. A contested detail is told as contested. The close says why the account was kept and by whom. The card drops key works and the two-part legacy unless the record carries them.

## Listed, and how the categories stack

Mark: "for whos, they are still in the record or lists." Every named person keeps their place in their tradition's record and in its sources conversation and people lists. A Who profile or a story is added on top. It never replaces the list line, and the line is not rewritten when one is added.

- **The line.** One sentence in text only: the name with its identifier if common, a time or place anchor, and what the record says they did. Everything in it comes from the census row and the vendored file the tradition cites. Where the record is thin, the line says so.
- **Wanted.** A person who would be a Who if the Library held one named source gets no text until it is vendored. The source must be able to carry a life, not only writing (the coordinator's routine call, open to Mark).

## The outside witness

A label on a Who profile for a historian outside the church who reports on it, such as Josephus or Tacitus. Mark: "these are historians, not doctrine or athiests or others fighting the church, just objective historians." A polemicist does not qualify. The profile says who they were, exactly what they say, and how far it can be trusted. There is no "what they fought for" beat. Passages are quoted or tightly paraphrased from the vendored file. Each doubt names who raises it and why. The card's Tradition line reads "Outside the church", and the label sits beside the role. The Who test is unchanged.

## Councils

Mark: "counsels are treated like a tradition with a different icon and title. but people who are a part of it should be on the who click." A council is shown like a tradition with its own icon and title. Its Who click lists the people who took part, each with their own verdict: a Who opens a profile, a listed person shows as a line. Mark: "it is one who listed in two places (counsil and the tradition)." A Who who took part has one profile, shown in the council's Who and in their tradition's Who, never a second copy. Attending a council does not make someone a Who. Councils and other multi-tradition events belong to the Shared Events workstream (`Build/Ministry/Features/Shared-Events/`); Mark's earlier "the counsels are stories i think" (Open-Gaps 197, 2026-11-10) is superseded by the 2026-11-11 ruling above (approved by Mark on the coordinator's recommendation, 2026-11-16).

## Naming

- **Display name.** The census `name`, in English, with "of <place>" where the name alone is not enough. `shortName` for second mentions.
- **First mention.** A name that could mean more than one person gets "name of place" ("Socrates of Constantinople"), in each separate text. A role or a time is added only where a place does not identify the person.
- **Epithets.** Used where the record uses them, and named as the record's.
- **Other forms on the card.** The census `informalName`. An original-language form only where a vendored source spells it. Basis: the source-fidelity rule, which allows no claim the sources do not carry.
- **Namesakes.** Always carry the place or the epithet the record uses: Lucian of Antioch and Lucian of Samosata; Dionysius of Alexandria and Dionysius of Rome.
- **Ids.** Lowercase and hyphenated from the display name. When two people collide, the new id adds the place. An existing id is never renamed. Basis: ids name the tree pages and the audio files, so a rename breaks both.

## Confidence

The five `formation_confidence` levels are record tags. They are not said aloud and are not shown as labels on the card. Documented and Widely Accepted are told plainly and traced in the references. Dominant Modern Reconstruction is told only as far as the sources agree, and who reconstructs it is named on the card, under What is uncertain (Standard v1). Contested gives both sides by name and has a `contested_claim` record behind it. Inferential-Thin is said as an inference with what it rests on, or kept to the card. "Not Attested" is an absent claim, handled as an honest limit. Basis: Style Guide 1.6 and 1.8.

## Review checklist

Run against any profile, story or listed line. Each item is pass or fail.

1. Every claim has a source the reviewer can name from the records, and the source establishes at least what the sentence says (Style Guide 1.2; the five questions in 1.1). The brief names a witness only where trust turns on it (Standard v1): the person's own words, a partisan or hostile witness, a point resting on one source, a wonder or legend, or a contested point (see Confidence). Documented and widely accepted facts are told plainly and traced in the references. No modern scholar is named in the brief. It does not repeat "X says" on every sentence. A claim no witness carries fails, however it is worded.
2. Every quote matches the vendored file word for word, checked again against the file. A "quotes verified" note is a claim to re-check.
3. No invented family, feeling, thought, anecdote or speech.
4. Reading aids from the Style Guide and Mark's words, read as aids and not as a mechanical list. Scope: the narrator's own prose, never a quoted source.
   - AI tells and the generic polished voice (1.1; `CLAUDE.md`, "Trust and source fidelity" and "Accessible and rigorous").
   - "Not X but Y" and "X, not Y" contrasts, colon-reveals, rhetorical questions and rhetorical build-ups (Mark: "no xy"; the 2026-10-17 fleet check, A3 and C5, in `Build/Ministry/Operations/Audits/`).
   - Aphorisms, wise sayings, and any sentence built to be quotable (1.1, question 5).
   - Tails and beat lines: a closing or one-line sentence that adds a beat and no fact (1.1, question 3).
   - Statements with no context or meaning, floating abstractions, and a paragraph that opens on a thesis (1.1, mechanical shape).
   - Dash fragments and verbless labels (1.2, 1.3), triads and doublets (1.4, 1.5), unearned emotional adjectives (1.5).
   - Hedging filler, loose quantifiers such as "only", "no", "always" (1.1, question 1; 1.6), and honest limits that end on a bare how, why or when (Writing Standard).
   - Anachronism (1.7), status-announcement register (1.11) and undefined technical terms.
   - Rhythm, both ways (`CLAUDE.md`; Mark's person-brief notes). A sentence the ear loses is recast: one with a clause nested inside a clause, or one that runs well past `CLAUDE.md`'s guide of about 25 words without reading in one breath. A run of short flat statements is joined where the source gives the link between them. The eight average 15 to 20 words a sentence, and 17 of their 151 sentences run past 25 words. A fix may join sentences as well as split them. No fix splits a sentence only to pass a count, and no fix drops a reason, a contrast or a witness's leaning to make a sentence shorter.
5. No role standing in for a named witness ("his editor", "a modern scholar").
6. A partisan or hostile witness is named and marked. A hostile-witness founder has two witnesses for the teaching.
7. A contested claim shows both sides by name and is never told as settled (1.8).
8. Common names have their name of place ("Socrates of Constantinople"), with a role or time only where the place does not identify them, at first mention in each separate text: brief, card, story, tree page and council Who list. Check the first mention of every name that could mean more than one person.
9. One term for one thing across the text (1.9).
10. The close read comes first, and the scores in item 11 only guard it. The reviewer reads the whole brief beside at least two of the eight (Methodius is one of them where the record is thin) and applies Mark's five craft tests. For each test the reviewer quotes the brief's weakest sentence for that test beside the model passage from the eight, and says plainly whether the brief reaches that level. No test passes without quoted evidence (Mark, 2026-11-15). A test that fails is a blocking finding, and its fix is a rewrite of the passage, never a patch to one sentence.
    - **Good storytelling.** Does it open on its setting and a sourced moment, and run as one story, so that a listener could retell it? Say the line of the story in one sentence. If that cannot be done, it is a list of facts and fails. Model: Ephrem, which opens on the famine and closes on it; Athanasius, from the severed hand to the exiles.
    - **Flow.** Does each sentence lead into the next, with reasons and results joined to their acts? Quote the weakest link between two sentences beside the model. Rows of statements with the links left out fail. Model: Gregory of Nyssa, "Macrina had turned him around once before ... But it was his sister who persuaded him"; Origen, "because everyone else had fled".
    - **No AI tells.** Read the narrator's prose against `CLAUDE.md` and item 4. Model: John Chrysostom's opening paragraph, which carries a scene, two witnesses and a judgment on each with no device at all.
    - **No hanging sentences.** Mark every sentence that connects to neither neighbor, and the last line. A stand-alone beat fails. So does a close chosen because it is quotable. A close is sound when it finishes the story. Model: Ephrem's close, "a month later, Palladius says, he died there"; John Chrysostom's, the body carried home.
    - **Everything relevant.** For each sentence about a source, an editor or a side fact, ask what the person's story would lose without it. If nothing, it goes to the card. This test also asks for the sentence or two that say why the person mattered, as an idea; a brief without them has left out the most relevant thing. Model: Athanasius, "If the Son were only a creature ..."; Methodius, which weighs a thin record in a few sentences and moves on.

    Signals the reviewer looks at, none of which decides alone: joining words per 100 words (the eight average 1.0, the 250 briefs written from 2026-11-12 to 2026-11-15 average 0.3); the share of sentences that are source talk; a close on a quotation; an opening on the template naming sentence "The X was Y"; runs of short sentences. A signal flags a harder read. It never passes or fails a brief by itself.

    Two further checks sit with the close read. Register: it would sit in BBC News or National Geographic, serious, adult, vivid and clear; a children's-book voice fails, and so does a page of footnotes. Length: it follows the person, aiming under 2:00 and stretching to 2:30, shorter where the sources are thin, and past 2:30 only where the batch note says in one line why. The brief also opens on its setting, then a scene, and tells disputes in place.
11. Readability, as a guard on the close read. Two counts are used, and they are not the same count. Grade, with its floor of 8.0 and its ceiling of 10.0, is counted on the full text, names included. Reading ease, with its floor of 60, is counted with proper names left out of the syllable count. A brief fails below grade 8.0, above grade 10.0, or below reading ease 60, each on its own count ("The readability method", below). Three more figures are reported beside the eight's own and are aids to item 10, not pass or fail: words a sentence (the eight: 15 to 20), joining words per 100 words (the eight: about 1), and the share of sentences of eight words or fewer (the eight: about 1 in 17). No brief is asked to fall inside the eight's ranges; they show the reviewer where to look. A brief below grade 8 is rewritten by joining and explaining. Longer words and added names do not mend it. A brief that passes every number and fails the close read fails. The score applies to the brief and story; a card field or listed line is under its minimum length and is read by eye.
12. The card is in Mark's order, missing fields are absent, and the brief's caveat appears again in What is uncertain.
13. Audio tags appear only in the audio script, at the start and before the closing line.
14. The person keeps their list line. A Who has a body of work or a following; an outside witness is an objective historian and never a polemicist.
15. Standard v1 shape: personal first, then the impact. Each stance is followed by what came of it, and each causal link is sourced or said plainly to be absent. Every stance the held sources show is told, ordered by weight.
16. Standard v1 opening: the first two or three sentences give the year, the place and region, the tradition where the census holds one, and what was going on.
17. Standard v1 witnesses and references: a witness is named only where trust turns on it; no modern scholar is in the brief; every claim told without a named witness is traced in the references listed below the brief.

## How a batch is reviewed and released

Mark, 2026-11-16: "CLAUDE.md governs (Recommended)".

- **Who reviews.** Opus drafts the Who briefs (`CLAUDE.md`), and Opus reviews every round. Who drafts council briefs follows `CLAUDE.md` as it stands.
- **Round 1** runs the full checklist: craft, rigor, access, and shape with length.
- **From round 2**, only what changed is rechecked, against the earlier findings.
- **The cap.** The three-round cap in `CLAUDE.md` applies.
- **Not rules.** The second-hand remarks "dont sacrafice quality, expecially the quality of writing" and "stop all opus work except the rewrite process" are not rules.

Mark, 2026-11-15 ("Yes", to all three parts of the review process: the quoted evidence in checklist item 10, and the two below).

- **The blind pairing.** In every review round, the batch's reviewer also gets at least one unlabeled pair: a brief from the batch and a passage of similar kind from one of the eight. The reviewer says which is stronger and why before learning which is which. The result goes in the review file. If the reviewer cannot tell them apart, or prefers the new brief without a concrete reason, that is a finding, raised to the coordinator.
- **Mark's sample read.** Before a batch goes onto the live tree, Mark reads one or two of its briefs, picked by the coordinator: one at the batch's median and one the signals flag. His word decides. A batch may merge into `Build/Ministry/` before his read. It does not go live until he has read its sample, and the release brief says so. Drift guard 3, below, adds his listen to this read.

### Drift guards (Mark, 2026-11-16: "All six (Recommended)")

Six guards keep Standard v1 from drifting. They are recorded in `Decision-Log.md`, "Standard v1 approved to proceed" (2026-11-16). Guard 1, a CI check on changes to the pattern files and the bar folder, is built separately. Guard 2 is in `Worker_Brief_Template.md`. The other four are these.

- **Guard 3: a listen before each release.** Before each batch of an era goes live, Mark hears one brief picked at random from it, beside a bar brief. His yes is the release.
- **Guard 4: a blind check every five batches.** A fresh reviewer scores a mix of new briefs and bar briefs, without being told which is which. If the new ones score lower, writing stops until the cause is known.
- **Guard 5: numbers as a guard, not the goal.** The readability check stays as a floor and a ceiling only (grade 8 to 10, reading ease 60 or more, "The readability method" below), and length is reported. Craft is judged by reading, never by numbers alone.
- **Guard 6: rulings only in Mark's words.** One coordinator works at a time. A ruling is recorded only with Mark's quoted words. Anything passed on second-hand is marked as a remark. Every brief and handover links the rulings record.

## The readability method

Mark, 2026-11-15: "Craft first, numbers as a guard"; proper names are not counted against reading ease.

1. **Words and sentences** are counted as the scorer counts them (`engine/m1/fk.py`): a word is a run of letters and apostrophes, with a curly apostrophe first turned into a straight one; a sentence ends at a full stop, question mark or exclamation mark.
2. **Opening word.** The first word of the text, of a sentence, of a line, or after an opening quotation mark or bracket.
3. **Proper name.** A word form is a proper name when all of these hold: it begins with a capital letter; it is not "I"; it appears at least once in the text where it is not an opening word (a final `'s` or `'` is ignored, so "Origen's" and "Origen" are one form); and its lower-case form appears nowhere in the text. Every use of that form then counts as a name, opening words included.
4. **Grade**, the figure the floor of 8.0 and the ceiling of 10.0 apply to, is the standard Flesch-Kincaid figure on all the words, names included: 0.39 × (words ÷ sentences) + 11.8 × (syllables ÷ words) − 15.59.
5. **Reading ease, names out**, the figure the floor of 60 applies to, is 206.835 − 1.015 × (all words ÷ sentences) − 84.6 × (syllables in the words that are not names ÷ the count of those words). Names still count toward sentence length. Only their syllables are left out.
6. A text under 12 words is not scored.

A grade with names left out (the formula of step 4 with the syllable term of step 5) is printed for information only. It is never a pass or fail figure and the floor of 8 does not apply to it: seven of the eight score 6.7 to 7.7 on it, and Gregory of Nyssa 8.3. Its one use is to tell the reviewer when a brief owes its grade to long names and place forms, so the close read looks harder at the prose.

Known limits, both small: a capitalized word that is not a name ("God", "Scripture", "Greek", a month) is counted as one, and a name that appears only at the start of sentences is not.

Joining words are counted as: because, since, though, although, so that, until, yet, even so, and ", so" or ", for" inside a sentence. The count is rough: it takes in "since" used of time and ", for" used as a preposition. A low count does not fail by itself. Constantine's brief scores none and still joins its ideas, with "that", "and that night" and "Only when he knew he was dying". It tells the reviewer to look.

The corrected eight, on these terms:

| Brief | Grade, full text | Reading ease, names out |
|---|---|---|
| Origen | 8.9 | 76.1 |
| Methodius of Olympus | 9.1 | 72.3 |
| Constantine the Great | 9.1 | 77.4 |
| Athanasius of Alexandria | 9.1 | 72.7 |
| Ephrem the Syrian | 9.2 | 76.7 |
| Gregory of Nazianzus | 9.5 | 72.0 |
| Gregory of Nyssa | 9.6 | 69.3 |
| John Chrysostom | 9.1 | 70.0 |

## Era 2 scan rulings that bear on profiles

From `Decision-Log.md`, "The era 2 Who scan, and the standing OUTSIDE WITNESS label" (2026-11-11), which this pattern follows.

- **Outside witness is a standing label in every era.** Josephus, Tacitus, Suetonius and Ammianus Marcellinus carry it. Celsus, Porphyry, Lucian of Samosata, Julian and Libanius are polemicists and stay listed. Pliny the Younger is a Who, outside witness, not major (Mark, 2026-11-12; `Decision-Log.md`, "Who scan records cleaned").
- **Recorders are Whos.** A biographer, church historian or recorder whose work is a main source for how the church knows its people is a Who on that body of work. The 2026-11-15 significance test keeps them ("Standard v1", above).
- **A founder known through a disciple's or biographer's record is a Who.** The record counts as developed with them, and the brief marks it as hagiography.
- **A council carries no verdict.** Its participants do.

## Working rules (approved by Mark on the coordinator's recommendation, 2026-11-16)

Mark, 2026-11-16: "Take my recommendations (Recommended)". These are not Mark's own words. They are working rules the coordinator recommended from the rulings draft, and Mark approved them as a set. The ids are the draft's.

**Kept.**
- **A6.** Four categories: WHO, STORY, LISTED, WANTED.
- **A7.** A WANTED source must be able to carry a life.
- **A19.** Suetonius and Ammianus Marcellinus are outside witnesses.
- **A27.** Each person appears once, in the era of their main work.
- **A47.** A partisan, hostile or disputed account is said to be so, and a contested point is never told as settled.
- **A48.** The brief's shape, folded into Standard v1's personal-then-impact shape.
- **A53.** The scene comes straight after the opening setting (Standard v1), and a contested point is told where it arises.
- **A61.** Confidence levels are record tags, told in plain sentences and never shown as card labels.
- **A62.** Other name forms come from the census; an original-language form appears only where a held source spells it; ids are never renamed.
- **A64.** After the opening's clear year (Standard v1), a bare year is used only where the year is the event. A partisan witness is placed once. The close may say how later readers remembered the person, so long as it still says what they changed or defended, with its witness.
- **A65.** Our prose uses American spelling; quotations and titles keep their own.
- **A74.** A saint carried by a near-time source stays a Who, if they pass the significance test ("Standard v1", The Who test).
- **B14.** A council person not yet scored shows "not scored", with no id.
- **B15.** A council's Who list is those who took part, were condemned, or acted on its decisions.
- **C2.** A first-person testimony is a STORY; WHO is for those who shaped the church.
- **C3.** A testimony needs no church office.
- **C4.** The story pattern: no theology section; witnesses named where a claim matters; later or legendary sources marked; the close says why the account was kept.
- **C9.** Every claim in "How it connects" rests on the card or the census, and its hedges stay.
- **C10.** A neighbor linked only by time or place is left out of that line.
- **C11.** The check fails story text that shows an id or builder wording.
- **C19.** Story source notes on how a builder read a source stay an open item, not a rule.

**Retired.**
- **A37 and B13**, the 2:30 caps, are replaced by Mark's length rule ("The brief", Length; `Council_Profile_Pattern.md`, Length).
- **A72 and A73** ("a much later Life means LISTED") are replaced by Mark's downgrade model: Story (documented), Story (legend), a mention, or not used ("Standard v1", The Who test).

**Follow Standard v1.** A67 and A70 are replaced by the two-kinds quotation rule ("The brief", Quotes).

**Held, not rules.** C17 and C18, from the legend-fixes branch, are not released.

## Proposed by this spec, not yet ruled

These carry no Mark ruling of their own. They follow from his rulings and stand until he changes them.

- A listed line is one sentence, in text only.
- The outside witness card's Tradition line reads "Outside the church", with the label beside the role.
- A Who who took part in a council is covered by the same first-mention and card rules as any other.
