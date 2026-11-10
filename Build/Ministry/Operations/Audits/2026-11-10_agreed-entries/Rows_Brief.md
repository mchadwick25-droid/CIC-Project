# People-rows brief (P2-G3)

Repo: /home/user/CIC-Project. Do NOT edit repo files. No metered model calls. Keep memory light (target files; no greps over all of cic/texts at once).

Read first: CLAUDE.md ("Trust and source fidelity"); the census meta.notes on `people` in cic-website/data/world-census.json; the people/named-voice checks in tools/validate-census.mjs (section "entry kinds, people and review status"); Decision-Log entry "2026-11-09 — The gap sweep ruled (P2-G1)", section "People on the map" (Build/Ministry/Features/Church-Family-Tree/Decision-Log.md).

Rule (Mark): every tradition shows its named people, drawn from its `voices`: named individuals whose words the Library holds or the entry quotes from a source. None is invented. A tradition with no named individual shows none, and its card says why.

Inputs: scratchpad/g3/voice_candidates.json (voices lines with script-found shelf authors that may match by name token; hints only). Planned person entries: scratchpad/g3/planned_persons.json — in a home movement's row put {"person": ID}, and do not also list that person as a named voice.

For each voices line of each movement in your band (skip kind "person" entries):
1. Named individual? (Not a group, office, community, church body, text, or "named individuals are scarce".) A line naming several people yields one item per person, each backed.
2. Backing, in order:
   a. held: a row_id on cic/corpus-map/<movement id>.yaml whose `author` slug is this person (confirm it really is this person, not a namesake or editor). Item {"name": exact substring of the voices line, "year": int, "voice": index, "author": slug, "held": row_id}.
   b. source: a verbatim quote of the person's OWN words (not words about them, not a narrator's), in a file under cic/texts/: look first in the entry's documentedStories sources and its links' sources, then a quick grep in files on the movement's shelf. Item {"name","year","voice","source":{"work","file","lines","quote"}}. Copied character for character, under ~40 words, lines exact (1-based). A document signed jointly by several people: allowed, but put it on flags ("joint").
   c. Neither: leave out, with the reason.
3. `name` must be an exact substring of voices[voice].
4. `year`: whole-number year of activity (first dated work or office), from the voices line, shelf row date or entry text; record what it rests on.
5. Order each row by year (a person entry sorts by its first working year; estimate it and state it).

For EVERY named individual judged (included or not): aliases for a mention count across the Library (distinctive forms as printed in 16th-20th c. editions in English, Latin, Greek translit., French, German, Syriac/Arabic translit.; never a bare common first name), and death or last-active year if known (else null).

Output <your dir>/rows.json:
{"rows": {"<movement id>": [items]},
 "decisions": [{"movement","voice","name","individual","backing":"held|source|none","reason"}],
 "people_index": [{"name","movement","year","last_year","author","aliases":[...]}],
 "empty_reasons": {"<movement id>": "one plain sentence why no named person is shown"},
 "flags": [...]}
Validate every source quote verbatim at its lines by script (whitespace squashed), every held row exists with that author, names are substrings, rows in year order. Reply with a short summary only.
