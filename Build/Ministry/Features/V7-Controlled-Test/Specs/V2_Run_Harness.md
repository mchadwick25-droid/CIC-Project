# V2: the run harness for A and B

**Owner:** engine thread. **Model:** Opus, because this is core code that will spend money.

**Purpose.** One command runs a frozen question file through one arm. Each question is a fresh first turn on the real turn path, with production settings. Everything in `../Test_Plan.md` §7 is recorded.

**Design.**
- **Where it lives.** A new script, `v7_run.py`, in `engine/m3/`. It uses only interfaces that exist on both `live` and `main`: `engine/m3/generation.py` (`LiveModelAnswerer`, `production_settings`) and `engine/provider/guard.py`. Arm A runs it against a checkout of `live`, made with git worktree in the run's scratch folder and never committed. B runs it on `main`. `--arm a` on `main` (the switch off) is kept for tests and for a third arm, should one ever be funded.
- **Timing.** The script times each call and each turn itself. It does not rely on `engine/m3/call_capture.py`, which is absent on `live`.
- **Arms.**
  - `--arm a` loads the world unchanged.
  - `--arm b` sets the new frame switch in memory on the loaded world, as `engine/m3/test100.py:91-107` does. Nothing in `records/worlds/` or `render.yaml` changes.
- **Spend.** Calls are guarded by `--live-test` and `--cap-usd`. The script prints the guard's announcement and its settings before the first call.
- **Dry mode.** `--reply-files <dir>` answers every call from files, as `test100.py` does. Tests and V6 use this mode.

**May touch.** The new `v7_run.py` and its tests. **Must not touch.** The turn path, `render.yaml`, records, packages.

**Tests written first.**
1. Without `--live-test` and `--cap-usd`, the command exits with code 2 and makes no call.
2. In dry mode, each turn's record holds every field in Test_Plan §7.
3. The settings used equal `production_settings()` read from `render.yaml`.
4. `--arm a` leaves the loaded frame byte-equal to the package's `frame.json`.
5. The script imports and runs in dry mode on a checkout of `live`.

**Done when.** The tests pass on `main` and on a `live` checkout, and one dry-mode run over two questions produces the record shape.

**Cost.** None.
