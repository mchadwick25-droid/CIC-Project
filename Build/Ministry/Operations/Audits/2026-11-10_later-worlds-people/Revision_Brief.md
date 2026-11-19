# P2-G3b: revision brief (round 1 findings)

Your `input.json` holds draft rows and an Opus reviewer's findings on each. Read
`Drafting_Brief.md` (same folder as this file) for the row format and rules. Produce `revised.json`:
the same rows, in the same order and format, with every BLOCKING, SUBSTANTIAL and MINOR finding
applied, plus these fields:

- `passes`: the reviewer's `passes_after_review`. If false, keep the row but set
  `recommendation` to "out" and `reason` to one sentence saying why the count fails.
- `counted_traditions[].clean`: the reviewer's recount (`valid`, plus `added`). Use the reviewer's
  refs; give each counted tradition a `quote` from a passage the reviewer kept valid, copied
  exactly from the file (grep it).
- `question`: null, or one of these when the recommendation turns on it:
  - "founder": the person founded, or gave their name to, a census movement.
  - "own_words": their only own words are a letter written for them and issued in their name
    (e.g. Paula) or a jointly written work (e.g. Pamphilus), which answer C counts as own words;
    or sermons taken down by hearers (Tauler), which answer C does not count.
  - "one_witness": both counted traditions rest on the same text by one author shelved twice.
  Answer C (Mark, 2026-11-10) counts own writing, a document issued or signed in their name, a
  jointly signed document, and verbatim minutes; it does not count speech others report or works of
  disputed authorship. Apply it as written: a letter issued in someone's name counts.
- `revision_log`: one line per finding: what you changed, or why no change was needed.

Recommendation rules: "include" when the count passes and every part of the qualifying test holds
on the rules as written; "hold" for a founder, for no own words or recorded position under answer C,
or for one_witness; "out" when the count fails. Never invent a fact or a source. Plain sentences.
Do not edit the repository; write only in your own folder; no model or network calls.
