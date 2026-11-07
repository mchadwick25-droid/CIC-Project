# Era 3 links — drafting brief (addendum)

Era 3 is "The Age of Monks and Empires", 451-622. Launch prompt:
`Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/CFT_Phase2_Links_Era_Launch_2026-11-07.md`.

The method is `Build/Ministry/Operations/Audits/2026-11-06_census-lineage-rigor/Drafting_Brief.md`,
unchanged: the six types, the five grades, the source shape, the note rules, "grade the
relationship, not the events". Read it in full first. Era 1's audit folder
(`Build/Ministry/Operations/Audits/2026-11-07_links-era-1/`, `README.md` and
`Drafting_Record.json`) shows the method applied; its wanted-texts list may already answer a gap.

## Your input

- `Inventory.json` in this folder: every relationship each era-3 movement's text names, and the
  links each already has.
- The census: `cic-website/data/world-census.json` (read only). The text is a movement's
  `relationsSummary`, `longDescription`, `why` and `legacy`.

## What you decide, per named relationship

One disposition, with a one-line reason:

- `link`: a new link, or an existing link kept / rewritten / regraded / retyped.
- `qualify`: the sentence is rewritten to say only what the vendored or repo-cited sources
  support ("may have", with the reason). Give the old and new sentence.
- `remove`: the sentence goes. Give the reason.
- `no-entry`: the other party has no census movement. Still check the claim; qualify it in a
  prose change if no vendored or repo-cited source supports it.
- `out-of-scope`: see the era-2 rule below, or the relationship is another era's (the other
  movement's own text names it and that movement is in era 1 or era 2).
- `kept-as-is`: the sentence is supported and needs no link (e.g. it names a person, not a
  movement relationship). Say what supports it.

## The era-2 rule (two sessions run at once)

Leave out every relationship between an era-3 movement and an era-2 movement where the era-2
movement's own text names it (the inventory's `era2_names_it: true`). Era 2 owns those; mark
them `out-of-scope` with the reason "era 2 owns it". Draft only the era-3↔era-2 relationships
that the era-3 text alone names. Existing era-2↔era-3 links are not yours to change unless
only the era-3 text names the relationship; if you think one is wrong, put it in
`drafter_flags` and leave it.

Links to era 1 and to eras 4-10 are in scope when this era's movement text names them.

## Existing links

Every existing link touching your movements appears once in your output with an action
(`keep`, `rewrite`, `regrade`, `retype`, `remove`). Link IDs are permanent: never change
`from`, `to` or `type` of an existing link in place. If the type or direction is wrong, mark
the old one `remove` (it will be retired with a reason) and draft a `new` one.

## Prose changes

For each `qualify` or `remove`, give the paragraph's new text in full:
`{"movement", "field", "old", "new", "reason"}`. `old` is the whole current field text, copied
exactly; `new` is the whole new field text. Keep the movement's own voice and every fact the
sources support. Plain, serious, BBC / National Geographic register; short sentences;
nothing past about 25 words. No raw movement IDs or internal language in public text: if a
field prints a movement ID (like `roman-church-gregorian`), rewrite it in words.

Readability is scored later; you need not score it.

## Output

Write ONE JSON file at the path you are given:

```json
{"group": "X",
 "dispositions": [{"movement", "field", "sentence", "other_id", "disposition", "link_id", "prose_change", "reason"}],
 "links": [ ...link objects exactly as the main brief's shape, plus "named_in_text" ... ],
 "prose_changes": [{"n", "movement", "field", "old", "new", "reason"}],
 "wants": ["..."],
 "escalations": ["anything for Mark: a grading that would change a method rule; a movement whose own text is wrong beyond a sentence"]}
```

`link_id` for a new link is `from--to` (or `from--to--2` if that pair already has a link).
For the symmetric types (`broke with`, `in contact with`) `from` < `to` alphabetically.

## Quote check

Before you finish, run
`python3 /tmp/claude-0/-home-user-CIC-Project/7d71a83c-a0b1-5e38-b90e-9a331370169e/scratchpad/check_drafts.py <your output file>`
and fix every failure. It applies the same verbatim test the validator uses: the quote,
whitespace squashed, must appear inside the stated lines, whitespace squashed.

Fabrication is the most serious failure this project recognizes. An honest "not found in the
vendored texts" is worth far more than a confident guess.
