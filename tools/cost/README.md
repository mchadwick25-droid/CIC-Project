# Cost measurement tooling

Supporting scripts for `CiC_Cost_Architecture_Review_2026-08-16.md`.

- `measure_prompt_tokens.py` — reconstructs the exact `static_prompt` and a
  representative `dynamic_prompt` for each deployed world by replaying the
  same assembly `cic/runtime/app/prompts/representative_prompts.py` and
  `cic/runtime/app/rag/retriever.py` perform (front-matter strip,
  `truncate_at(KEY_SOURCES)`, `excise_section(QUICK_MEANING)`), then reports
  character counts. Point `ROOT` at a checkout containing `cic/`.
  Exact token counts come from feeding the emitted `/tmp/pay_*_static.txt`
  files to `POST /v1/messages/count_tokens`, which is free.

- `cost_scenarios.py` — the scenario ladder in the review (T0-T7). Edit the price
  constants at the top if rates change. Sonnet 5 is $2/$10 per MTok flat -
  verified against the live model docs 2026-08-16, no introductory expiry.

Neither script makes a billable API call.

- `verify_prompt_cache.py` — **makes ~4 billable calls (~12 cents).** Replicates
  `get_llm(max_tokens=1200)` and `_cached_system_message` verbatim, runs the
  same prompt twice on the streaming path and once non-streaming, and prints
  both the raw Anthropic usage block and what `log_llm_usage` would record.
  Needs `CIC_ANTHROPIC_KEY` and `/tmp/pay_syriac_static.txt` from
  `measure_prompt_tokens.py`. Result on 2026-08-16: cache confirmed working
  (17,565-token read on call 2); LangChain's `input_tokens` is the TOTAL,
  raw Anthropic's is the uncached remainder (115). Do not sum the two.

- `trim_ledger.py` — the A-F trim ledger priced at 1,000 conversation-hours
  per month, cumulative. Adjust `HOURS` for a different volume. One penny per
  hour is $120/year at that scale.

- `analyze_usage_log.py` — prices a real `[llm_usage]` log correctly and
  reports cache effectiveness. Makes no API calls. Run it over saved logs
  rather than trusting any per-turn figure:

      python3 tools/cost/analyze_usage_log.py backend.log --hours-per-month 1000

  Reports true spend per label, the double-count factor a naive calculator
  would produce, the read/write/uncached split, and the **pooling factor** -
  reads served per write. Pooling is what lever F is: the 1h cache entry is
  keyed on the prompt prefix, not the session, so every session opening the
  same world inside the window reads the same block. A single-session test
  can never show it, which is why per-hour cost looks worse in testing than
  in production.

- `analyze_over_settling.py` — turns the `[over_settling_decision]` log into a
  decision about the screen's sensitivity. Reports fire rate, confirm rate per
  world, and prices the two-stage design against adjudicating unconditionally.
  Reports the fire rate with a 95% Wilson interval and refuses to recommend a
  retune while that interval straddles the 60% break-even — and when it does,
  says how many turns would actually resolve it rather than quoting a fixed
  bar. Makes no API calls.

      python3 tools/cost/analyze_over_settling.py backend.log

  Measured token shape (2026-08-16, count_tokens): adjudication cached head
  8,831 tok fleet mean, screen prompt 869 tok. The screen only pays for
  itself below a 60% fire rate.

- `run_traffic_sample.py` — **drives real conversations and spends money**
  (~$0.04/turn; the 48-turn default ≈ $2). Runs N sessions × 12 newcomer
  questions through the app's own endpoints, capturing both the `[llm_usage]`
  and `[over_settling_decision]` streams into one file for the two analyzers
  above. `--dry-run` costs nothing; `--max-spend` aborts on a ceiling.

      cd cic/runtime
      PYTHONPATH=. python3 ../../tools/cost/run_traffic_sample.py --out /tmp/sample.log
      python3 ../../tools/cost/analyze_usage_log.py     /tmp/sample.log
      python3 ../../tools/cost/analyze_over_settling.py /tmp/sample.log

  48 turns, not 200: at a fire rate near 78% that already excludes the 60%
  break-even (95% CI ≈ 65%–87%), and the cost/token shape converges sooner
  still. Only a rate sitting near the threshold needs hundreds of turns, and
  the analyzer says so when it sees one. Run the default, read the verdict,
  extend with `--sessions` only on INCONCLUSIVE.

  Sessions run back to back and concentrate on two worlds by default: the
  cache pools on the per-world prompt prefix, so spreading four sessions over
  six worlds would measure four cold caches and prove nothing about pooling.
  `--worlds a,b,c` overrides the selection.

  **Cannot run in the Claude Code web sandbox.** Retrieval downloads
  `all-MiniLM-L6-v2` and `cross-encoder/ms-marco-MiniLM-L-6-v2` from
  huggingface.co on first use, and that host is denied by egress policy there
  (`httpx.ProxyError: 403`, re-confirmed 2026-08-16 against
  `huggingface.co`, `cdn-lfs.huggingface.co`; `pypi.org`, `github.com` and
  `api.anthropic.com` are all reachable, so it is that host specifically).
  There is no cached copy to fall back on and no pre-built FAISS index in the
  repo, so the index build needs the embedder too. Run it anywhere HF is
  reachable, or warm `~/.cache/huggingface` there once and copy it across.
  Everything up to retrieval is verified: the app boots, `/health` is 200, and
  `/api/session/start` completes against the live API.

  A **preflight** loads both models before the first session starts, so a
  blocked host costs nothing instead of failing mid-run with turns already
  billed.

## The published review

`cost-review-artifact.html` is the source for the published artifact at
<https://claude.ai/code/artifact/b56d902b-fe88-4705-acbe-d53a5ad091b0>. It is
kept in the repo because the first copy lived only in a session scratchpad and
came within one container reclaim of being unrecoverable. To update the
published page, edit this file and republish it **to that same URL** — a
publish without the URL creates a second artifact instead of updating this one.

It mirrors `CiC_Cost_Architecture_Review_2026-08-16.md` at the repo root. The
markdown is the full record; the HTML is the readable summary. When one
changes, change the other.
