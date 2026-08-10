# Combined go-live checklist — interview upgrades + the table build + the Haiku switch

**Written 2026-08-10 for System Hub 8–9 to drive.** Two workstreams are
converging on one runtime and one model switch. This is the single merge
order, the gates, the owners, and the rollback for each step.

**The governing rule: the model switch lands LAST and ALONE.** Everything
else merges first and is verified on Sonnet. If something breaks after
the switch, it is the model, and the fix is a one-line revert instead of
an untangling. Nothing below is worth more than that property.

**Why one checklist and not one thread:** the two workstreams have
different evidence behind them and different surfaces in front of them.
The interview upgrades ship to the FREE TIER — every visitor, most of the
traffic. The table ships to a feature open during the pilot but far
smaller. Same switch, very different depth. Keep the evidence separate;
share only the integration.

---

## Status at writing

| item | state |
|---|---|
| Voice Rebuild (PR #9) | **MERGED to main 2026-08-10** — six worlds rebuilt, live |
| Table build (PR #10) | **DRAFT** — B1, B2, B6, speaker-label repair; verified, not merged |
| Interview upgrades | in flight in its own workstream — **not** covered by this document's verification, only by its gates |
| Production model | `claude-sonnet-5`, pinned in `render.yaml` (Blueprint-managed) |
| B4 solo Haiku checkpoint | **RUNNING** — world 1 of 6; the free tier's evidence, and the one gate still missing |

---

## Step 1 — Interview upgrades merge to main

**Owner:** the interview workstream. **Model:** unchanged (Sonnet).

Gates before merging:
- [ ] Its own checkpoint artifacts pass on every hard bar, per that workstream's discipline
- [ ] `assembly_identity` clean; `PENDING_RECHECKPOINT` empty or every entry declared
- [ ] CI green on the head commit

**Rollback:** revert the merge commit. Sonnet is still serving, so a
revert restores exactly today's behaviour.

## Step 2 — Table build merges to main (PR #10)

**Owner:** this workstream. **Model:** unchanged (Sonnet).

**Know what actually changes on the live site at this step.** Not
everything in PR #10 is inert:

| change | effect on production (still Sonnet) |
|---|---|
| **Round cap 6 → 4** | **ACTIVE, participant-visible** — table rounds get shorter |
| Fabrication gate | inert — configured haiku-only |
| Speaker-label repair | effectively inert — zero occurrences measured on Sonnet |
| Drift evidence capture | observability only |

Gates before merging:
- [ ] B5 `ship-regression` green — **DONE** (B2 edge clean both seatings, divergence held, mean rep turns 2.12 / 2.62)
- [ ] Fixtures pass: `fabrication_gate_fixture.py`, `speaker_label_repair_fixture.py` — **DONE**
- [ ] `app.graph.replay.parity_suite replay` run somewhere with real egress — **OPEN, owner: Mark.** It 403s in the build sandbox; confirmed reproducing on clean HEAD, so it is an environment limit, not these changes. Do not skip it: it is the only check that the governance chain's ordering did not move.
- [ ] PR #10 taken out of draft

**Rollback:** revert the merge commit. The only participant-visible piece
is the cap, and reverting restores 6.

## Step 3 — Verify main on Sonnet, both workstreams merged

**Owner:** System Hub. **This step exists because it is the last moment
the model is not a variable.**

- [ ] CI green on main after both merges
- [ ] Render deploy succeeded; service healthy (watch for status 137 / OOM
      — the fix was moving index-building into the Docker build, so a
      regression here means something re-entered runtime startup)
- [ ] One real conversation through the live site, solo, read by a human
- [ ] One real conversation through the live site at a table, read by a human
- [ ] **Transparency surfaces seen rendered by a human** — citations,
      gloss pills, name-bridge pills, per speaker, at a table. **OPEN,
      owner: Mark.** PR #9's own honest note: three of these have never
      been seen rendered by anyone. Ten minutes, and only eyes catch it.

**Rollback:** revert whichever merge the failure points at.

## Step 4 — The model switch, alone

**Owner:** this workstream (it is a repo edit, not a dashboard change).

`render.yaml` carries `LLM_MODEL: claude-sonnet-5` and its own comment
says that file, not a manual dashboard edit, is the source of truth for
this service. A dashboard change would be overwritten by the Blueprint.
So this is one line, in a commit of its own, with nothing else in it.

Gates before flipping:
- [ ] **B4 passes** — six solo Haiku checkpoints, full hard bars, all six
      worlds. **RUNNING.** This is the free tier's whole evidence base and
      the only gate still outstanding. If any world fails, the switch is
      table-only and B3's per-mode split gets built for a real reason
      (see the blueprint's B3 amendment for what that costs: 19 sites).
- [ ] **The speaker-label repair is already in main** — i.e. Step 2 done.
      Non-negotiable ordering. The transcript-format leak is Haiku-only,
      measured in every Haiku arm at up to 21% of turns, and its serious
      form is one Representative writing another world's dialogue inside
      its own turn. Flipping the model without the repair ships that
      defect to participants.
- [ ] The Anthropic Console spending limit reviewed for the free pilot —
      **owner: Mark.** With tiers deferred and no per-visitor cap, the
      console limit plus the per-conversation caps (40 solo / 100 table
      representative turns) are the only real backstops.

**Rollback:** revert the one-line commit. Sonnet returns on the next
deploy. This is why the switch is alone.

## Step 5 — After the switch

- [ ] Watch `[speaker_label_repair]` lines for a week — the repair hides
      the defect from participants, deliberately, so the log is the only
      place its real rate stays visible. A rising `truncated_at_other_speaker`
      count is a quality signal, not a formatting statistic.
- [ ] Watch `[fabrication_gate]` outcomes. Known and unresolved: the gate
      fired 5 times in the regression run and at least two look like
      FALSE POSITIVES on correctly attested material (Ignatius's own
      words; Simeon bar Sabbae and the daughters of the covenant). The
      corrective tells the voice "our record does not hold them", so a
      false positive pushes a Representative away from real grounded
      scholarship. If the false-positive rate stays high, narrow what the
      gate acts on. **Not a launch blocker; it is a watch item with a
      named remedy.**
- [ ] Re-run the cost baseline on the shipped stack (blueprint B10) so the
      standing cost record stops describing a system that no longer exists.
- [ ] Pilot group: recruitment, and the logging-disclosure text before
      `pilot_logging_enabled` is turned on. **Owner: Mark.** This is the
      instrument the whole quality ruling now rests on — Mark's own
      decision was to pass the arms and let the pilot report
      inconsistencies. Without a pilot group there is no instrument.

---

## Deadline

Sonnet's intro pricing ends **2026-08-31**; the table's per-round cost
rises about 32% the next morning. That is the clock on Step 4 — not on
Steps 1–3, which should take exactly as long as their gates need.

## The one review this checklist does not replace

Nobody has read the two workstreams' changes **side by side**. The
interview work touches prompts and records; the table work touches
emission, governance and the round loop. They are unlikely to interact,
which is precisely why an unexamined assumption is worth one clean-room
read of the combined diff before Step 4 — by someone who wrote neither.
Not a re-litigation of settled decisions: only "do these interact
anywhere unexpected."
