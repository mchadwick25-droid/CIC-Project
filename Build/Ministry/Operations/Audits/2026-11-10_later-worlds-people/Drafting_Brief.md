# P2-G3b: drafting brief for the later-worlds people list

The Church Family Tree gives some people an entry of their own ("person entry"). One route in
(Mark's ruling, Decision-Log 2026-11-09, "People on the map"): a person named repeatedly in the
own-voice texts of later traditions, at least 5 distinct passages in each of at least 2 later
traditions. A two-pass check has found the candidates in your `candidates.json` meeting that count.
You draft each one's row for Mark's list. Mark decides; you recommend. Nothing is published yet.

Repository: `/home/user/CIC-Project` (read only). Census: `cic-website/data/world-census.json`
(`movements`, each with id, name, dates, longDescription, voices, people). Library shelves:
`cic/corpus-map/<movement id>.yaml` (rows: work, author, role, locus, source_file). Texts:
`cic/texts/`. World builds: `Build/worlds/`.

## The qualifying test (ruling 14, Decision-Log 2026-11-06, item 14)

"Someone the corpus treats as a party in their own right, with writing of their own or a recorded
position, who founded no lasting movement." Answer C (2026-11-10): a person's own words are their
own writing, a document issued or signed in their name, or verbatim minutes. Speech others report
for them, and works of disputed authorship, do not count as their words. Check each part:

1. **Party in their own right**: the corpus treats them as an actor, not only a name in a list.
2. **Own writing or a recorded position**: name the work(s) of theirs the Library holds
   (`facts.own_works_rows`, or grep `cic/corpus-map/*.yaml` for their author id), or the
   recorded position (a creed, letter, condemnation, signed act). If their only "writing" is of
   disputed authorship, say so.
3. **Founded no lasting movement**: is there a census movement they founded or that is named for
   them (Montanism, Valentinians, Manichaeism, the Waldensians, the Franciscans, Novatianism...)?
   If yes, say which, with its id. Founders are a question for Mark (see below), not your call.
4. **Home**: the tradition the Library shelves them in (principle 4: "told within the tradition the
   Library shelves them in"). `homes` in the input is only where the count first found the name and
   can be wrong (Basil shows up under the Anomoeans because they argued against him). Find the
   shelf that holds their own works as role `tradition`; if none, the movement whose own story
   they belong to. Give the census id and name. If none fits, say "no tradition".
5. **Already in the census?** The 23 person entries (kind "person") are out. If this candidate is
   one of them under another spelling, say so and stop.
6. **Namesake and identity check**: confirm the counted passages name THIS person (not a namesake)
   and that the counted traditions are later than the person and not their own home. Read at
   least two of the `refs` per tradition in the file (`sed -n 'L-5,L+5p'`).

## What to write

`draft.json` in your own folder: one object per candidate, in input order:

```json
{"cid": "C038", "name": "display name, as the Library spells it",
 "home": {"id": "...", "name": "..."} ,
 "dates": "c. 216-277 (from the census or the corpus; give the source)",
 "dates_source": "file:line or census id",
 "own_words": "the works of theirs the Library holds (file names), or the recorded position, or 'none held'",
 "party_in_own_right": "one sentence",
 "founder_of": null or {"id": "...", "name": "..."},
 "counted_traditions": [{"id": "...", "name": "...", "clean": 7,
     "quote": {"file": "...", "line": 0, "text": "8-25 words copied exactly from the file"}}],
 "home_citation": {"file": "...", "line": 0, "text": "words from the person's own work or the home text naming them, copied exactly"},
 "why": "two or three plain sentences for Mark: who they are and why the later worlds name them",
 "recommendation": "include" | "hold",
 "reason": "one or two sentences",
 "doubts": "anything a reviewer should check"}
```

Recommend **include** only when every part of the test holds and both counted traditions are
sound. Recommend **hold** for: a founder (the question goes to Mark); no own words and no recorded
position; a home that is wrong or missing; doubtful counted passages; disputed identity. Never
invent a fact, a date or a source. Every quote is copied exactly from the file (grep it after you
copy it). Write plainly: short sentences, no jargon, no hedging filler. Do not edit the repository;
write only in your own folder; no model or network calls.
