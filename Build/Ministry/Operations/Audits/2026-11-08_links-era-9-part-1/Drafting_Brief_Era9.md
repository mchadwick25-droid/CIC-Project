# Era 9 links — drafting brief (addendum)

Era 9 is the long nineteenth century, about 1770-1906. It has 51 movements and runs as two
parts, split by lane, each with its own audit folder, review rounds and pull request:

- Part 1: the Protestant and Evangelical lane, plus the Syriac East / Protestant bridge (24
  movements). Folder `Build/Ministry/Operations/Audits/2026-11-08_links-era-9-part-1/`.
- Part 2: every other era-9 lane (27 movements). Folder `.../2026-11-08_links-era-9-part-2/`.

Launch prompt: `Build/Ministry/Features/Church-Family-Tree/Launch-Prompts/CFT_Phase2_Links_Era_Launch_2026-11-07.md`.
The method is `Build/Ministry/Operations/Audits/2026-11-06_census-lineage-rigor/Drafting_Brief.md`,
unchanged: the six types, the five grades, the source shape, the note rules, "grade the
relationship, not the events". Read it in full first. Era 5's folder
(`Build/Ministry/Operations/Audits/2026-11-07_links-era-5/`, `README.md` and
`Drafting_Record.json`) shows the method applied; the eras 1-5 wanted-texts lists may already
answer a gap.

## Your input

- `Inventory.json` in your part's folder: every relationship each movement's text names, and
  the links each already has. The inventory was made by a fast model. Read each of your
  movements' four fields yourself; add what it missed and correct wrong matches.
- The census: `cic-website/data/world-census.json` (read only). The text is a movement's
  `relationsSummary`, `longDescription`, `why` and `legacy`.
- Sources: `cic/texts/` (vendored editions) and `cic/corpus-map/`. Search with `grep -n`, `rg`
  and `ls`. Many nineteenth-century texts are vendored under English titles.

## What you decide, per named relationship

One disposition, with a one-line reason:

- `link`: a new link, or an existing link kept / rewritten / regraded / retyped.
- `qualify`: the sentence is rewritten to say only what the vendored or repo-cited sources
  support ("may have", with the reason). Give the old and new field text.
- `remove`: the sentence or clause goes. Give the reason.
- `no-entry`: the other party has no census movement. Still check the claim; qualify it in a
  prose change if no vendored or repo-cited source supports it.
- `out-of-scope`: another session owns it (rules below).
- `kept-as-is`: the sentence is supported and needs no link (e.g. it names a person, not a
  movement relationship). Say what supports it.

## Who owns a relationship (other sessions run at once)

- Eras 6, 7 and 8 are being linked in other sessions now. A relationship between an era-9
  movement and an era-6, -7 or -8 movement is theirs when the other movement's own text names
  it (inventory `other_names_it: true`): mark it `out-of-scope`, "era N owns it". Draft it
  only when the era-9 text alone names it.
- Eras 1-5 are done. A relationship to an era 1-5 movement that an era-9 text names is yours,
  unless a link for it is already on main (then review that link as an existing link).
- Era 10 has not run. Links to era 10 named by era-9 text are yours.
- Between the two parts: part 1 owns a relationship whenever a part-1 text names it. Part 2
  drafts a cross-part relationship only when part-2 text alone names it.

## Existing links

Every existing link touching your movements appears once in your output with an action
(`keep`, `rewrite`, `regrade`, `retype`, `remove`). Link IDs are permanent: never change
`from`, `to` or `type` of an existing link in place. If the type or direction is wrong, mark
the old one `remove` (it will be retired with a reason) and draft a `new` one.

## Major links (Mark, 2026-11-08)

- "gave rise to", "continued as" and "broke with" are major by type. They carry no `outcome`.
- An "influenced", "argued against" or "in contact with" link is major only when one of its
  OWN listed sources shows an institutional act:
  - a council, canon, synod or law condemning, deposing or excluding a group or its teaching
    (kind `council-law`);
  - a split into a separate church or body (kind `split`);
  - a rule, practice or settlement changed by an authority (kind `rule-changed`).
- None of these count: a teaching, text or practice merely taken up by the other side
  (translations, set reading, compilations, following a writer); one bishop's
  excommunication; an exile soon reversed; a ruling in a letter with no sign it was carried
  out; or evidence more than about 60 lines from the cited quote.
- A link that passes carries `"outcome"`: one plain public sentence naming the act. Every fact
  in it comes from a source already on that link. 30 words or fewer, ending in a full stop,
  Reading Ease 60 or more and FK 10 or less. No internal words or IDs; American spelling.
  Leave the field off otherwise.
- For each judged-type link (new or existing) add a `major` block to the link object:
  `{"major": true|false, "kind": "council-law"|"split"|"rule-changed"|null,
  "evidence": {"file", "lines", "text"} | null, "reason": "one line"}`. The evidence `text`
  is verbatim from the vendored file at those lines (the check script tests it). The `major`
  block is audit record only; it is stripped before apply. Expect only a few per part.

## Prose changes

For each `qualify` or `remove`, give the field's new text in full:
`{"n", "movement", "field", "old", "new", "reason"}`. `old` is the whole current field text,
copied exactly; `new` is the whole new field text. One prose change per field: if several
dispositions touch one field, fold them into one change. Keep the movement's own voice and
every fact the sources support. Plain, serious, BBC / National Geographic register; short
sentences; nothing past about 25 words. Each paragraph of `new` must score Reading Ease 60 or
more and FK 10 or less (the check script scores it). No raw movement IDs or internal language
in public text. If a field prints a movement ID or a map-layout note, rewrite it in words.

A movement whose own text is wrong (not just unsupported) where the fix is more than a
sentence goes in `escalations`, not in a rewrite.

## Output

Write ONE JSON file at the path you are given:

```json
{"group": "X",
 "movements": ["ids"],
 "dispositions": [{"movement", "field", "sentence", "other_id", "disposition", "link_id", "prose_change", "reason"}],
 "links": [ ...link objects in the main brief's shape, plus "id", "action", "named_in_text", "major", "outcome" (judged types only, when major), "wants", "drafter_flags", "change_reason" ... ],
 "prose_changes": [{"n", "movement", "field", "old", "new", "reason"}],
 "wants": ["..."],
 "escalations": ["anything for Mark"]}
```

`id` for a new link is `from--to` (or `from--to--2` if that pair already has a link).
For the symmetric types (`broke with`, `in contact with`) `from` < `to` alphabetically.
`named_in_text` gives the movement and field that name the link.

## Check before you finish

Run `python3 /tmp/claude-0/-home-user-CIC-Project/222bf868-d532-5764-957f-0cad2c0547be/scratchpad/check_drafts.py <your output file>`
and fix every failure. It applies the validator's verbatim test (the quote, whitespace
squashed, must appear inside the stated lines, whitespace squashed), the link shape, internal
words, the outcome rules, and the reading scores of notes, outcomes and prose. It also tests
each `major.evidence.text`.

Fabrication is the most serious failure this project recognizes. An honest "not found in the
vendored texts" is worth far more than a confident guess.
