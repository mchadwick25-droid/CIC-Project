# V2: run harness for B, on a test branch from `live`

**Owner:** engine thread. **Model:** Opus, because this is core code that will spend money.

**Purpose.** Run B exactly as fleet graded run 1 ran A, with the switch on as the only difference, and record what `../Test_Plan.md` §8 lists.

**Design.**
- **Test branch.**
  - Cut `v7/b-on-live` from `live` at c869dd86. This is the tree that produced A, as verified by the empty diff of `engine` and `records` against `ddabd865`.
  - Add only three things: the B switch (V5), the card loader (V4a), and this runner.
  - The branch is never merged into `live` or `main`. The same code goes to `main` through V4a and V5 for later use.
- **Runner.** A new script, `v7_run.py`, in `engine/m3/`. It drives `LiveModelAnswerer` as `engine.m3.live_admission_run` did for A:
  - the same model id, region and max_tokens, all passed explicitly on the command;
  - the same packages, checked against the manifest hashes in A's `run_settings`;
  - the probes, read through the existing sealed loader.
- **Arms.** `--arm b` sets the switch in memory on the loaded world. `--arm a` exists for tests only.
- **Logging.** The script times each call itself, and records each call's usage and priced cost in the same fields as A.
- **Spend.**
  - Calls are guarded by `--live-test` and `--cap-usd`.
  - The script prints the guard's announcement and its settings before the first call.
  - After the sample it computes the stop rule in Test_Plan §7.
- **Dry mode.** `--reply-files <dir>` answers every call from files. Tests and V6 use it.

**May touch.** The new `v7_run.py` and its tests, on the test branch.
**Must not touch.** The turn path beyond V5's switch, `render.yaml`, records and packages.

**Tests written first.**
1. Without `--live-test` and `--cap-usd`, the command exits with code 2 and makes no call.
2. In dry mode, each record has every field that A's records have, plus the size of B's additions.
3. A package hash that differs from A's `run_settings` stops the run before any call.
4. With `--arm a` in dry mode, the user message is byte-equal to A's saved `request` for the same probe.

**Done when.** The tests pass on the test branch, and a dry-mode run over two probes produces records of A's shape.

**Cost.** None.
