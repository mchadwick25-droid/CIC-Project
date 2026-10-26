# coverage_search.py - what the records and the vendored texts already hold on a topic

Run (read-only; standard library + PyYAML; no network, no model calls):
    python3 -I coverage_search.py --repo /home/user/CIC-Project --terms "hell,gehenna,eternal fire" [--regex] [--whole-words] [--worlds alx,syr] [--max-source-hits 3] [--json out.json]
Terms are comma-separated, matched case-insensitively as substrings (so `hell` also matches `shell`, `Hellenic`); `--regex` treats each term as a regex (e.g. `\bhell\b`), `--whole-words` wraps every term in word boundaries.
Records are `records/<code>/<type>/*.md` (front matter fields only, never the body); vendored texts are the `source_file`s in `cic/corpus-map/<world_id>.yaml` (falls back to `census_id`), scanned once each and shared across worlds. `canon/sealed_probes/` is never read.
Classes, strongest first: QUOTE = a quote record matched on text / modern_rendering / retrieval.retrieve_when;
WITNESS = a doctrinal_witness, term, gravity, force, story or demonstration record matched;
ABSENCE = an honest_limit, contested_claim, or source record with `kind: absence` matched (the world already says what it cannot answer);
SOURCE_ONLY = no record matched but vendored texts mapped to the world did; NOTHING = neither.
A world's line reports its strongest class, lists weaker classes it also has under "also", then matching record ids by type with formation_confidence and a 120-char snippet, and the top N vendored files by hit count with one 160-char line and its line number (XML and Latin editorial matter are treated as ordinary text).
The summary table at the end is world | class | n_quote | n_witness | n_absence | n_source_files; `--json` saves everything (including all hit files per world) for later comparison.
