# Brief: constructed gold-set items, one failure class

You write candidate sentences that carry exactly one known defect of one class. They go into a gold set used to measure automatic judges, and they are counted apart from natural sentences. A sentence is a line a historical Representative of a Christian tradition might say, in the first person plural ("we", "our") for its own tradition, in plain modern English (CEFR B2, 12 to 25 words, active voice). It is bound to one or two records. The defect must be certain from the bound record's own words, so that anyone can check it.

## Where the records are

Read records only as they stood at these commits, with `git show <commit>:<path>` and `git ls-tree -r --name-only <commit> records/<world>` in /home/user/CIC-Project:

- worlds alx, desert, don, gallic, hal, ijc, pahc, rzg, syr: commit fdfcf33dad0c7d0097fef62a3269ee8146c9a91a
- world witt: commit 1a716fe86fc084a46b5241dfac5952be65a0c30d
- world lpc: commit fcd5768412b60ae64e58c639a5624979679bce6f

A record is a Markdown file with YAML front matter. Its `id` is the binding id. Quote records carry the source's words (`text`, often `modern_rendering`, `register`, `speaker` or `attribution`, `locus`). Term records carry a world word and lexicon risk flags.

Do not read anything under Build/Ministry/Features/Answering-From-Sources/ except `Stage1/data/seed-tests.jsonl`. Do not bind to any record id that appears in that file. Do not use the web. Do not call any model API or run any engine command.

## Rules for every candidate

- Exactly one defect, of your class. Every other part of the sentence must be supported by the bound record. If a second defect slips in, drop the candidate.
- It reads like something a Representative could say. No broken grammar, no odd capitals, no tell-tale wording that gives the defect away.
- The defect is certain from the record's words, not from outside knowledge.
- Spread across worlds: at most 6 candidates from any one world, and at least 7 worlds in all.
- No two candidates bound to the same record.

## Output

Write 45 candidates to /tmp/claude-0/-home-user-CIC-Project/b19321d6-b32f-53b7-a583-04ee0a7a3c2e/scratchpad/constructed/CLASS.yaml (CLASS as given below) as a YAML list, each entry:

```yaml
- seed_type: CLASS
  world: alx
  records_commit: fdfcf33dad0c7d0097fef62a3269ee8146c9a91a
  bindings: [{kind: record, id: alx.quote.some-id}]
  sentence: "..."
  record_words: "the exact words of the bound record, copied character for character, that make the defect certain"
  construction: "one plain sentence: what the record says, and what the sentence changes"
```

Check each `record_words` value with a script against the record file at its commit (an exact substring of the file after joining whitespace). Fix or drop any that fail. Report only the file path, the count per world, and how many you dropped and why, in a few lines.
