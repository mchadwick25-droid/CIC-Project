# Era 1 build scripts and worker instructions

The scripts and instructions this pass used, kept so a later session can rerun the release build.

| File | Use |
|---|---|
| `build_era1.py` | `python3 <this> 50 2026-11-16` from the repo root, after `git checkout origin/main -- cic-website/data/world-census.json tools/quote_renderings.json`. Puts era 1's briefs, cards and council entry into the census, lists the renderings and applies the Bardaisanite attribution. |
| `audio.mjs` | Regenerates the era 1 audio scripts. Its paths are absolute to `/home/user/CIC-Project`. |
| `tags.py`, `quotes.py` | Count tag verbs and quotations per brief (`quotes.py <git rev>` counts at that commit). |
| `council_qo.json` | The council's one quotation, which the council entry cannot carry. |
| `*.txt` | The instructions given to the writers and reviewers. |
| `live-errors-notes.md` | The live errors the card workers found, for the pull request. |
