# Record-defects tools (RD1 to RD7)

Working tools from the Library record-defects thread. Paths inside the prompts point to that thread's scratchpad; change REPO and the scratch paths before reuse.

- `review_prompt.md`: round-1 Opus rendering review brief (fill REPO, WORLD, IDS_FILE, N, K, OUTFILE). Includes the bracket rule and reported-speech frames.
- `pr_review_prompt.md`: independent Opus pull-request review brief (every changed record plus a sample of at least a fifth).
- `mklog.py REPO WORLD Prefix`: builds `Rendering_Review_Log_<N>_2026-11-03.md` from the batch, Round2, Brackets and Round3 tables. Hand-edit rows whose history it cannot express.
- `setfield.py REPO WORLD JSON`: replaces top-level fields in quote records and checks every other field is unchanged.
- `gc.py WORLDS [v]`: runs the quote-locus and rendering-review gates for comma-separated worlds.
- `minitest.py MODULE`: runs a pytest module without pytest installed (monkeypatch, tmp_path, parametrize).
- `brit.py REPO`: lists British spellings in modern-English fields of records changed against the merge base.
- `spans.py REPO WORLDS...`: prints, as JSON, each reviewed quote's file and tight line span parsed from the batch review tables. RD7 uses it: all 362 verbatim quotes with no span are covered.

The batch review tables live in each world's `Build/worlds/<world>/Review-Artifacts/` on main (gallic, desert, don, rzg) and on the branches `claude/rd4-ijc-witt-renderings`, `claude/rd5-syr-hal-renderings` and `claude/rd6-alx-pahc-cappadocian-renderings`.

Pre-push checks: `engine.m2.cli staleness-check`, `engine.m2.site_cli staleness-check`, `cic/engine/texts_registry.py --check`, `engine.m10.cli regate|records <w> --base origin/main`, `engine.m9.enforce`, `tools/check_live_commentary.py --base origin/main --enforce`.
