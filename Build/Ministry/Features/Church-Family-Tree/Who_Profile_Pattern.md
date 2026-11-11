# Who profile pattern

Approved to proceed (Mark, 2026-11-11). The one pattern every Who profile, story and listed line is written to. Rulings and their reasons are in `Decision-Log.md`, "The Who profile pattern" (2026-11-11).

## The writing standard this rests on

This pattern adds nothing to how the words are written. It adopts the standard behind the tradition cards and the eight early-church person briefs, by reference. Mark: "we use the same principles we used to develop the tradition cards, simple modern english with the accessability and no ai tells etc. it is a full design i dont want to repeat, no tails, no statements that have no context or meaning no xy no wise saying etc. find the quality and follow it."

| What | Where |
|---|---|
| Reading level, register, plain-language rules | `CLAUDE.md`, "Accessible and rigorous"; `Build/reference/method/Pass2-decisions/VR_1A_NorthStar_Readability_Target_2026-08-09.md`; `VR_1A_Writing_Standard_2026-08-09.md` |
| No invention, quotes checked against the vendored file, the five confidence levels | `CLAUDE.md`, "Trust and source fidelity" |
| The five review questions, the exemplar, and the named failures (dash fragments, triads, unearned adjectives, hedge calibration, contested claims told as settled, terminology drift, status-announcement register) | `Build/reference/method/CiC_Voice_Style_Guide_and_Scaling_Plan.md`, 1.1 to 1.12 |
| How a brief reads aloud: story, natural years, named witnesses, flowing sentences | `Decision-Log.md`, "Person briefs: 60 to 120 seconds, personal and theological" (2026-11-11) |
| Jon v4 voice, settings and audio tags | `Decision-Log.md`, "Person voice: Jon on Eleven v4, replacing David Baker" (2026-11-11) |
| The per-turn readability score | `engine/m7/turn_readability.py` through `engine.m1.gates.grade_text` |

## Newer standards the tradition-card standard does not cover

All made on 2026-11-11 and in the Decision-Log. They apply to every participant-facing person text: briefs, cards, stories, tree pages and council Who lists.

- **Common names (Mark: "if a name is common we need to clarify from where"; "dont forget the newer ones like name full or place of common names like we did for socratise").** At its first mention in a text, a name that could mean more than one person gets its name with a place, in the form scholars use (Mark: "socrates from constantinopel"): "Socrates of Constantinople", "Eusebius of Caesarea", "Palladius of Helenopolis". A role or a time is added only where the place does not identify the person. The live briefs' "the church historian Socrates" predates this refinement. The brief and the card are separate texts and each has its own first mention. The identifier comes from the vendored sources and adds no claim.
- **Real witnesses named.** "Eusebius says", "Palladius tells", "his own letters say". Never "his editor", "the translator" or "a modern scholar".
- **Natural dates.** Years read as they are spoken, not as bare numbers.
- **Hostile witnesses.** Named, with polemic marked as polemic and its owner named.
- **Jon audio tags.** In the audio script only.
- **Story, not fact-giving.** Sentences flow, and grade 8 is a floor, not a target.

The Style Guide says it is not a banned-word list and must not become one. Its test is the rule: for each sentence, name the source that makes it true and what the source does not establish. The review checklist below points to its sections and does not copy them.

## The brief

- **Length.** Mark: "we moved the who to 1 to 2 minutes with streatch for major people". A brief is never cut to fit a number. One that falls short of the standard is rewritten.
- **Opening.** Scene first: one sourced moment. The who-line follows within the first few sentences.
- **Order.** Who they were, with time and place. Their story and what mattered. The positions they fought for, developed or defended, and why they mattered to their tradition and its opponents, told through events. One line in their own words where the Library holds them, otherwise how later readers remembered them.
- **Disputes in place.** A contested point is told where it arises, with its witness named. The brief does not save it for the close.
- **Witnesses.** Named, as in the 2026-11-11 standard: "Eusebius says", never "his editor". A partisan witness is placed once and said to be partisan.
- **Dates.** Round anchors and relative time first. A bare year only where the year is the event.
- **Common names.** An identifier at first mention, in the brief and again in the card (the 2026-11-11 common-name standard). It comes from the vendored sources and adds no claim.
- **Audio.** `[calmly]` opens the audio script. `[warmly]` goes before the closing line. The tags are never in the census, the card or a page. There is no intro: person audio is the brief only.
- **Quotes.** Short and plain, verbatim from the vendored file. Where a line is long or archaic, the narrator tells it in modern words and names the source. A quote is never re-rendered in modern English, so no Opus rendering is needed.

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

Mark: "counsels are treated like a tradition with a different icon and title. but people who are a part of it should be on the who click." A council is shown like a tradition with its own icon and title. Its Who click lists the people who took part, each with their own verdict: a Who opens a profile, a listed person shows as a line. Mark: "it is one who listed in two places (counsil and the tradition)." A Who who took part has one profile, shown in the council's Who and in their tradition's Who, never a second copy. Attending a council does not make someone a Who.

## Naming

- **Display name.** The census `name`, in English, with "of <place>" where the name alone is not enough. `shortName` for second mentions.
- **First mention.** A name that could mean more than one person gets "name of place" ("Socrates of Constantinople"), in each separate text. A role or a time is added only where a place does not identify the person.
- **Epithets.** Used where the record uses them, and named as the record's.
- **Other forms on the card.** The census `informalName`. An original-language form only where a vendored source spells it. Basis: the source-fidelity rule, which allows no claim the sources do not carry.
- **Namesakes.** Always carry the place or the epithet the record uses: Lucian of Antioch and Lucian of Samosata; Dionysius of Alexandria and Dionysius of Rome.
- **Ids.** Lowercase and hyphenated from the display name. When two people collide, the new id adds the place. An existing id is never renamed. Basis: ids name the tree pages and the audio files, so a rename breaks both.

## Confidence

The five `formation_confidence` levels are record tags. They are not said aloud and are not shown as labels on the card. Documented and Widely Accepted are told plainly with the witness named. Dominant Modern Reconstruction names who reconstructs it. Contested gives both sides by name and has a `contested_claim` record behind it. Inferential-Thin is said as an inference with what it rests on, or kept to the card. "Not Attested" is an absent claim, handled as an honest limit. Basis: Style Guide 1.6 and 1.8.

## Review checklist

Run against any profile, story or listed line. Each item is pass or fail.

1. Each sentence names its source, and the source establishes at least what the sentence says (Style Guide 1.2; the five questions in 1.1).
2. Every quote matches the vendored file word for word, checked again, not taken from a "quotes verified" note.
3. No invented family, feeling, thought, anecdote or speech.
4. Banned patterns, each pointing to the Style Guide:
   - AI tells and the generic polished voice (1.1; `CLAUDE.md`, "Accessible and rigorous").
   - "Not X but Y" and "X, not Y" contrasts, and rhetorical build-ups.
   - Aphorisms and wise sayings, and any sentence built to be quotable (1.1, question 5).
   - Tails: a closing line that adds a beat and no fact (1.1, question 3).
   - Statements without context or meaning, and floating abstractions that no name, number or action cashes in (1.1, mechanical shape).
   - Dash fragments (1.3), triads and padding (1.4), unearned emotional adjectives (1.5).
   - Hedging filler and loose quantifiers such as "only", "no", "always" (1.1, question 1; 1.6).
5. No role standing in for a named witness ("his editor", "a modern scholar").
6. A partisan or hostile witness is named and marked. A hostile-witness founder has two witnesses for the teaching.
7. A contested claim shows both sides by name and is never told as settled (1.8).
8. Common names have their name of place ("Socrates of Constantinople"), with a role or time only where the place does not identify them, at first mention in each separate text: brief, card, story, tree page and council Who list. Check the first mention of every name that could mean more than one person.
9. One term for one thing across the text (1.9).
10. The brief reads as a story, opens on a scene, tells disputes in place, and is 1 to 2 minutes, longer only for a major figure.
11. Readability passes `grade_text`: FK 10 or below, Flesch 60 or above.
12. The card is in Mark's order, missing fields are absent, and the brief's caveat appears again in What is uncertain.
13. Audio tags appear only in the audio script, at the start and before the closing line.
14. The person keeps their list line. A Who has a body of work or a following; an outside witness is an objective historian, not a polemicist.
