# Council profile pattern

Approved to proceed (Mark, 2026-11-14). The pattern every major-council profile is written to: the brief, the entry and the records. It adapts `Who_Profile_Pattern.md` and changes only what a gathering needs that a person does not. The list of major councils and the rulings behind it are in `Decision-Log.md`, "Councils: one word for every gathering, and the major councils" (2026-11-12), and in `Build/Ministry/Operations/Audits/2026-11-12_major-events-scan/Councils_Scan.md`.

## What carries over from the Who pattern unchanged

- The writing standard, by reference: `CLAUDE.md`, "Accessible and rigorous"; the NorthStar readability target and Writing Standard; the Voice Style Guide 1.1 to 1.12; the person-brief decision of 2026-11-11 (story, natural years, named witnesses, flowing sentences).
- The newer standards of 2026-11-11: common names with their place at first mention in each text, real witnesses named, natural dates, hostile witnesses named with polemic marked, Jon audio tags in the audio script only, grade 8 as a floor.
- Quotes verbatim from the vendored file, re-checked against file and line. A narrator's modern-word telling is a paraphrase and does not claim to be the quote.
- The five `formation_confidence` levels as record tags, never said aloud or shown as labels. A contested point gives both sides by name and has a `contested_claim` behind it. An honest limit is an `absent_detail`.
- The review checklist, items 1 to 9, 11 and 13, as written there.

## How a council differs from a person

1. **Whose account we have.** A person has a life and witnesses to it. A council has a record, and the record is usually written by one side. Every council entry names, for each main witness, what kind of witness it is:
   - **acts**: the council's own minutes, canons, creed, decree, synodal letter or subscription list;
   - **participant**: a letter or account by someone who was there or who called it;
   - **later narrative**: a history written afterwards, with its writer named and, where a held source gives it, when;
   - **modern reconstruction**: an editor or historian of the councils (Hefele, Leclercq, McGiffert) who supplies a date, a count or a sequence that no ancient witness gives.
2. **Acts versus later narratives.** What the acts say is told plainly. What only a later narrative says is told as that writer's account. Where the acts are lost, the brief says so once, early, and says whose account stands in their place. A council with held acts cites them first, before any history.
3. **Friendly and hostile witnesses.** The winners usually wrote the record. The condemned party's position is told in its own words where the Library holds them. Where it does not, the brief says the view reaches us through opponents and names them. The Who rule for hostile-witness founders applies to the condemned teaching: two independent witnesses for the teaching, or the brief says it rests on one. A participant who called or led the council is a partisan witness for it, placed once and said to be partisan.
4. **Numbers, dates and names.** A count of bishops comes from a named witness or a subscription list, and the two are kept apart where they differ (a round number in a history and a signed list are different witnesses). A month or year that no ancient witness gives is told as the modern historian's dating, by name ("by Hefele's dating"). This is the Who reviews' "modern date told as an ancient writer's" fault, guarded at the pattern level.
5. **Issue, decision and outcome are separate.** The issue or controversy that brought them together is one field; what it decided or tried to decide is another; what came of it is a third. A council that failed to decide, or whose decision was rejected, is told as such. The river-level reach is told through events in the outcome, not asserted.
6. **Confessions through the meeting.** A creed, definition or confession is told as the act of the meeting that made it: who drafted, who signed, who refused. It is listed among the sources under the council's own record.
7. **A council is shown like a tradition; its people are on the Who click.** A council carries no verdict; its people do. The Who click lists the people in the record with their verdict (WHO, STORY, LISTED) and what part they played. Attending does not make someone a Who. A Who has one profile, shown in the council's list and in their tradition's, never a second copy.

## The brief

- **Length.** A ceiling of 2 minutes 30 seconds, the same as a major Who (about 400 words), and never a target. A council that tells in a minute and a half is told in a minute and a half.
- **Opening.** One sourced moment that puts the listener in the room or just before it. What was at stake follows within the first few sentences.
- **Order.** The scene. What was at stake and who called the meeting. Whose account we have, said once and early, with the partisan witness named. Who came, from where. What was argued and decided, told through what happened. What came of it, told through events that show its reach beyond one tradition.
- **Disputes in place.** A contested date, count or sequence is told where it arises, with its witnesses named.
- **Quotes.** Short, from the acts first where held, otherwise from the named participant or historian.
- **Close.** Where it stands in later memory or what it left in place, from a held source. No summing-up line.
- **Audio.** `[calmly]` opens the audio script and `[warmly]` goes before the closing line, as with a person. There is no intro.

## The entry: a tradition page with its own icon and title

Mark (era 2 Who scan, 2026-11-11): "counsels are treated like a tradition with a different icon and title. but people who are a part of it should be on the who click." A major council is written as a census-style tradition entry, shown on a tree page of the same form as a tradition's, under its own icon and the title "Major council". It is not a person card. Its people show under Who for that council.

The page reads in the tradition page's order: the line with era, dates and place; the name; the "Major council" label; About This Council (the narrated brief); then the council's own sections; then the traditions it touched; then Who; then Sources. A missing field is absent, never filled.

| Field | Holds |
|---|---|
| `id`, `kind`, `kindLabel` | The id; `kind` is `major-council`, which gives the icon; `kindLabel` is "Major council", the title shown beside the name. |
| `era`, `name`, `shortName`, `informalName` | As on a tradition entry. `informalName` holds another name the held sources use (Robber Synod). |
| `dates`, `start`, `end`, `datesNote` | Year or years for the line and the map. `datesNote` gives the month where a source gives it, with whose dating it is when a modern historian supplies it. |
| `region`, `placeLabel`, `modernCountries` | As on a tradition entry, with the ids copied from existing census rows. |
| `rivers` | The rivers it reached, as the major-councils table gives them. |
| `teaser` | One or two sentences for the map: place, year, what met and what it decided or tried to decide. |
| `knownFor` | One sentence, as for a tradition. |
| `issue` | The issue or controversy that brought them together: what had happened, what question it raised, and who stood on each side, each item with its witness. Mark: "for the card, we need to know the issues/contriversy that caused to meet". |
| `calledBy` | Who summoned it, with the witness where it is disputed. |
| `attended` | Who came and how many, each count with its witness; whether a list of names is held. |
| `decided` | What it decided or tried to decide, item by item, from the acts where held. |
| `outcome` | What came of it: who accepted, who refused, what followed, with witnesses. |
| `record` | Whose account we have: each main witness, its kind (acts, participant, later narrative, modern reconstruction) and its side. |
| `traditions` | The traditions it touched, in groups that take the place of a tradition's lineage links: Gathered, Condemned, Refused, Affected. Each has the census id and one sourced line. |
| `people` | The Who click: name, verdict (WHO, STORY, LISTED) and part played, with the id only where a Who profile or census entry already has one. A Who opens their one profile; a listed person shows as a line. A person in the record whom no Who scan has scored shows as NOT SCORED, with no id, until a scan scores them; the council profile makes no verdict. |
| `briefLength` | The spoken length of About This Council. |
| `uncertain` | Opens with the brief's caveat on the record, then each further doubt naming its witnesses. |
| `sources` | Three groups: `fromTheCouncil` (acts, canons, creed, synodal letters, subscription lists), `fromThoseThere` (participants' own accounts), `writtenLater` (histories and modern editors). Each entry gives a title, an author where one applies, a language and its file under `cic/texts/`. |

## The records

`records.json` holds, for each council id:

- `claims`: claim, witness (file and lines), `witness_kind` (acts, participant, later narrative, modern reconstruction) and `formation_confidence`.
- `contested_claims`: claim, sides (each named), and a `formation_confidence` for the claim as it stands.
- `absent_details`: detail and note, for honest limits: lost acts, unnamed attendees, months no ancient source gives.

`witness_kind` is the one field the Who records do not have. It lets a reviewer see at a glance which claims rest on the council's own record and which on later tellers.

## Files

`Council-Profiles/era<N>/` holds, per council id, `<id>.brief.txt`, `<id>.entry.json` and `audio/<id>.audio.txt`, with one `records.json` and a `README.md` per era folder. Ids are lowercase and hyphenated from the display name, with the year where two councils share a name (`council-of-ephesus-431`).

## Review checklist additions

Run with the Who checklist, items 1 to 9, 11 and 13.

C1. Every main witness in `record` has a kind and, where partisan, a side.
C2. Where the acts are lost, the brief says so once, early, and names whose account stands in for them.
C3. The condemned party's view is in its own words, or the text says it reaches us through opponents and names them.
C4. Every count of attendees has its witness; every month or year that no ancient witness gives is attributed to the modern historian by name.
C5. The issue that brought them together is stated with its sides and witnesses; issue, decided and outcome are separate, and a failed or rejected decision is told as such.
C6. A creed or confession is told as the act of the meeting, with who signed and who refused where held.
C7. The entry is in the tradition page's form, with the "Major council" title. The Who click gives each person their verdict and part; no new verdict is made by the council profile.
C8. The brief is within 2 minutes 30 seconds and reads as a story from a scene.
