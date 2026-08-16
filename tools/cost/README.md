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

- `cost_scenarios.py` — the scenario ladder in the review. Edit the price
  constants at the top when Sonnet 5 leaves introductory pricing on
  2026-09-01 ($2/$10 -> $3/$15 per MTok).

Neither script makes a billable API call.
