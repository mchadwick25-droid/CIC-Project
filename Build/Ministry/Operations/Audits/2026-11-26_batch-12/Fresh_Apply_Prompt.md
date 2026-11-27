# Batch 12: apply each fresh read's exact changes, word for word

You apply changes; you judge nothing. For each folder you are given, under `Build/Ministry/Operations/Audits/2026-11-26_batch-12/<slug>/`, read `Fresh_Read.md`. Apply to `<slug>.brief.txt` every exact change it gives, MINOR ones included, word for word: copy the new text exactly, and replace only the text it names. Change nothing else, and nothing listed under "For Mark". If a change's old text cannot be found as quoted, do not guess: list it as not applied, with what you found. Then run `python -m engine.m1.profile_readability <brief>` and report its line.

In each folder write `Fresh_Applied.md`: each change, "applied" or "not applied" with the reason, and the scorer line. Do not commit, and edit nothing outside the folders you are given. Reply in under 80 words: for each slug, the count applied and not applied, and the word count.
