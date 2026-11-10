# P2-G3b, later-worlds count: context verification brief

You are checking a mechanical name count for the Church Family Tree. A script found every place a
person's name (or alias) appears in the texts that later Christian traditions' Library shelves hold
as that tradition's OWN voice. Your job is to read each found mention in context and say what it
really is. Nothing you write goes to the public; it decides whether the count is clean.

Your input is one JSON file in your own folder (`batchNN.json`): a list of candidates. Each has
`name`, `homes` (the tradition the person belongs to), dates, the aliases searched, and up to three
later `traditions`, each with `files` (which shelved work of that tradition the file holds: work
title, author id, locus) and `contexts` (id, file, line, the alias matched, ~450 characters of text).

## Label every context with one letter

- **S** — the same person, named in the shelved work's own text (the ancient/medieval/modern author
  writing as the tradition's voice, or a faithful translation of that text). A translation of the
  author's own text counts; it is the author's words rendered.
- **E** — editorial matter: an editor's, translator's or modern scholar's footnote, introduction,
  preface, heading or summary added by the editor, apparatus criticus (sigla, variant readings,
  manuscript notes), index, table of contents, bibliography, running header, or a modern study's
  own prose. If the text reads like a 19th/20th-century scholar discussing the person (cites pages,
  editions, "cf.", "see", German/Latin scholarly commentary, critical sigla), it is E.
- **N** — a namesake or a different referent: another person with the same name (e.g. "Jerome"
  meaning Jerome Lalemant; "Gregory" meaning another Gregory; a biblical figure; a place or church
  named after the person, e.g. "St Cyprian's church", unless the person is plainly meant), or a word
  that only looks like the name.
- **U** — cannot tell from the text given (OCR too broken, or not enough context).

Then for each tradition give `clean_passages`: the number of DISTINCT passages labelled S. Two
contexts that are the same passage in two languages (Greek text and a facing Latin translation) or
the same sentence repeated are ONE passage. A work's own title line counts as S only if the author
or the original text gives it, not an editor.

## Rules

- Judge only from the text and file information given. If you need more, you may read the file
  itself (paths are relative to `/home/user/CIC-Project/cic/texts/`) around the given line, e.g.
  `sed -n 'L-15,L+15p' file`. Do this whenever the label is not obvious, and always before calling
  something S when the passage might be a footnote.
- Never guess a person in. If unsure between S and E/N, choose U.
- Do not edit anything in the repository. Write only in your own folder.
- Quote nothing you have not seen in the file.

## Output

Write `result.json` in your own folder: a list, one object per candidate, in input order:

```json
{"cid": "C023", "name": "Maximilla",
 "traditions": {"<tradition id>": {"labels": {"<context id>": "S", ...},
                                     "clean_passages": 4,
                                     "best_quote": {"file": "...", "line": 1471,
                                                    "text": "exact words from the file, 8-25 words, naming the person"}}},
 "namesake_notes": "which aliases picked up someone else, and who",
 "editorial_notes": "what kind of editorial matter was counted",
 "comment": "anything the coordinator must know (one or two sentences)"}
```

`best_quote` is one S passage per tradition, copied exactly from the file (check it with grep or
sed; keep the file's own spelling and OCR errors). Omit it when there is no S passage.

Finish with a one-paragraph summary in your final message: how many candidates, how many
traditions reached 5 clean passages, the commonest namesakes and editorial noise.
