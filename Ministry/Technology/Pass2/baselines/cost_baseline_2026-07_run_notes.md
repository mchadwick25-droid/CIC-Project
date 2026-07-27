# B-COST run notes (kept beside the generated report, which must stay re-generatable)

Run 2026-07-26, single continuous execution of the fixed 40-turn set against
the live system (real API, `claude-sonnet-5` main + `claude-haiku-4-5`
monitoring), instrumentation complete per S1.1a (30/30 call sites).

1. **C4 turns 9–10 are conversation-cap turns, not failures.** They streamed
   the canned cap message with 0 LLM calls: `app/message_cap.py`'s
   `CONVERSATION_TURN_CAP = 20` counts *representative* turns, and a 3-world
   table burns 2–3 per participant turn, so the cap landed after 8
   participant turns. Real current-system behavior, worth knowing when
   comparing multi-world costs later: C4's per-turn average ($0.307
   standard) includes two nearly-free capped turns — the 8 real multi-world
   turns average ≈ $0.38.
2. **Cache-TTL measured, textbook shape** (report's own table): C3 turn 5
   `main_response` cache_read = 15,737; post-330s-pause turn 6 cache_read =
   0 with cache_write = 15,737 (the full prefix re-paid); turn 7 cache_read
   = 15,737 again. A >5-minute participant pause costs one full prefix
   re-write at 1.25× — the §8 cache-TTL variable is now a number, not a flag.
3. **Headline per-turn figures (standard rates):** single-world ≈
   $0.080–0.140/turn (C1/C2/C3), three-world ≈ $0.31/turn (incl. capped
   turns; ≈$0.38 uncapped). 689 calls / 40 turns ≈ 17 calls per turn at a
   3-world table's peak (47 on its opening turn); the monitoring/adjudicator
   layer instrumented at S1.1a accounts for the large majority of calls but
   a minority of dollars (Haiku); the Sonnet `main_response` dominates cost.
4. **Interaction with the R-lite re-run:** `S1.1_rlite_rerun_raw.jsonl` was
   collected 22:32–22:34, overlapping C4 turns 3–5 in wall time; verified
   irrelevant to the cap events at 22:40 (the cap is turn-count arithmetic,
   not rate limiting).
