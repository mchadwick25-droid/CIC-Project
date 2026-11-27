# Batch 12: apply each card check's exact changes, word for word

You apply changes; you judge nothing. For each folder you are given, under `Build/Ministry/Operations/Audits/2026-11-26_batch-12/<slug>/`, read `Card_Check.md`. Apply to `<slug>.card.json` every exact change it gives (the field, the old text, the new text), word for word: copy the new text exactly and replace only the text it names. Where a change adds an item to a list (a timeline line, a `sources`, `briefSources` or `modernWorks` entry), add it where the check says, exactly as given. Where the check gives a change to an entry field rather than the card, write it into `Card_Edits.md` under a heading "Entry fields (card check)" instead, since release sets entry fields. Change nothing else. If an old text cannot be found as quoted, do not guess: list it as not applied, with what you found.

After applying, confirm the file is valid JSON (`python -m json.tool <file> > /dev/null`), and score the card's running text if `Card_Edits.md` names the command it used.

In each folder write `Card_Check_Applied.md`: each change, where it went, and "applied" or "not applied" with the reason, and the JSON check result. Do not commit, and edit nothing outside the folders you are given. Reply in under 80 words: for each slug, the count applied and not applied.
