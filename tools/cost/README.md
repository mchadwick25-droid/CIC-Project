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
  constants at the top when Sonnet 5 leaves introductory pricing on
  2026-09-01 ($2/$10 -> $3/$15 per MTok).

Neither script makes a billable API call.

- `verify_prompt_cache.py` — **makes ~4 billable calls (~12 cents).** Replicates
  `get_llm(max_tokens=1200)` and `_cached_system_message` verbatim, runs the
  same prompt twice on the streaming path and once non-streaming, and prints
  both the raw Anthropic usage block and what `log_llm_usage` would record.
  Needs `CIC_ANTHROPIC_KEY` and `/tmp/pay_syriac_static.txt` from
  `measure_prompt_tokens.py`. Result on 2026-08-16: cache confirmed working
  (17,565-token read on call 2); LangChain's `input_tokens` is the TOTAL,
  raw Anthropic's is the uncached remainder (115). Do not sum the two.
