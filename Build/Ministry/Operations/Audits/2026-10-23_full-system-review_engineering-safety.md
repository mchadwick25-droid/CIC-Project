# Full-system review: engineering, safety and operations risk — 2026-10-23

One of four parallel, independent reviews of the whole system that Mark asked for on 2026-10-23. This one's lens is engineering, safety and operations risk. The other three are scholarly rigor and content; participant experience and accessibility; and market and sale-readiness. Reviewer: Opus 5.5, read-only on the product.

## 1. Scope and method

**Commits reviewed.** `origin/main` = `e6464639`; `origin/live` = `469d072c` (the merge of PR #1081). Main is 21 commits ahead of live. Almost all of the difference (+3.85 million lines) is vendored Library texts from Era III (PR #1082). In `engine/` and `render.yaml`, live and main differ in four files only (`engine/m10/quotes.py`, its test, and two page tests). So the engine findings below hold for both branches. The public site is a separate case: it publishes from `main` (see R6).

**What I read myself.** CLAUDE.md, README.md, render.yaml, `engine/Dockerfile`, `.github/workflows/ci.yml` and `live-watch.yml`, and these engine files: `engine/api/app.py` (message, bound, health and backup wiring), `engine/api/ratelimit.py` (client address), `engine/api/deeper_admission.py`, `engine/api/deeper_routes.py` (webhook, products), `engine/deeper/bound.py`, `engine/m5/live_calls.py`, `engine/m5/failure.py`, `engine/m5/routing.py`, `engine/m4/facilitator_turns.py`, `engine/m4/crisis_resources.py`, `engine/provider/bedrock.py`, `engine/m5/reports/safety-script-run-1..8.json`. Also the Backup/Restore, Promotion and Model Spend Budget runbooks, the Pilot Feedback Log and Decisions (`Build/Ministry/Operations/Pilot-Feedback/`), the System Hub Decision Log's recent entries, and both copies of the Facilitator Governance V3.6 document.

**Delegated reading.** Four read-only subagents swept these areas: the safety path; sign-in, payments and privacy; cost controls and state; operations, CI and supply chain. I treated their reports as leads. Every finding ranked below I checked in the source myself, unless it is marked "subagent, not re-checked".

**Commands I ran** (all free, all with fakes, no model calls, no network beyond `git fetch`):

| Command | Result |
|---|---|
| `git rev-parse --short origin/main origin/live`; `git ls-remote --heads origin \| wc -l` | `e6464639`, `469d072c`; 729 remote branches |
| `pytest -q engine/deeper/tests engine/accounts/tests engine/m5/tests/test_routing.py engine/m5/tests/test_failure.py engine/m4/tests/test_crisis_resources.py` | 377 passed |
| `python -m pytest tools/tests -q` | **2 failed**, 260 passed (`test_check_live_commentary.py`: the `support.html` hand label and the precision/recall test) |
| `python tools/check_paths.py --baseline tools/check_paths_baseline.txt` | 0 new; 968 cited, 980 in baseline |
| `python -m engine.m1.cross_world` | exit 0 (subagent: "0 new defect(s), 6 accepted-open") |

Subagents also ran: `engine/m9` check (exit 0, 65 waivers, none stale), `tools/check_live_commentary.py` (report-only; REWRITE hits remain: engine 33, records 40), and the `cic-worker` tests (18/18).

**Not checked, and why.**
- The `engine/api`, `engine/m8` and `engine/provider` test suites. This sandbox lacks `fastapi`, `yaml`, `boto3` and `anthropic`, and installing them needs network. So the HTTP-level safety seam tests did not run here.
- Anything only a dashboard shows: Render settings (Auto-Deploy, `WEB_CONCURRENCY`, the values of `CIC_DEEPER_PRODUCTS`), the AWS Budget and its action, Stripe's webhook destination, Cloudflare's proxy settings, GitHub branch protection, R2 contents.
- The live service itself. I made no request to it.
- Classifier accuracy. Measuring it needs model calls, which are out of scope.
- Git history for old secrets. Only the current tree was scanned.

## 2. Done, with evidence

- **A per-turn safety gate runs before the voice, and the voice never runs on a safety route.** Safety and the reader run together, then routing (`engine/m4/turn.py:143-147`, subagent; `engine/m5/failure.py:49-89`, checked). Safety text never streams: the gate finishes first, and only voice routes stream (subagent).
- **Crisis text is fixed and added by code, never by a model** (`engine/m4/crisis_resources.py:1-18`, checked). It names no hotline, by the project's resource-naming decision (`Build/reference/L3D-Encounter-Methodology/CiC_L3D_RelationalSafety_ResourceNaming_Decision_Options.md`).
- **Past the monthly visitor bound, the reply is a fixed Facilitator line with the redirect always included, and no model call** (`engine/api/app.py:93-113`; `engine/m4/facilitator_turns.py:240-242`, checked).
- **The Stripe webhook is verified properly**: HMAC-SHA256 over the raw body, constant-time compare, 300-second tolerance, 256 KB cap. Startup is refused if the secret is missing (`engine/api/deeper_routes.py:166-184, 422-433, 679-684`, checked).
- **The admin token fails closed**: a 404 when unset or wrong, `hmac.compare_digest`, and a minimum of 32 characters at startup (subagent, `engine/api/app.py:482-511`).
- **Accounts sign-in is built carefully but is off in production**: emailed 6-digit codes, hashed session tokens, `__Host-` cookie, a CSRF header, a 7-day recovery wait (subagent; the account tests pass, 172 of them within the 377 above).
- **The model is called only through one guarded seam**: `make_client` calls `guard.admit()` (`engine/provider/bedrock.py:74-86`, checked), and tests forbid building a client anywhere else (subagent, `engine/provider/tests/test_guard.py`).
- **Retries are cut to one** (`CONVERSATION_MAX_RETRIES = 1`, `bedrock.py:71`). Voice output is capped at 2,048 tokens (`engine/m4/generation.py:59`). Input is capped at 4,000 characters for a reply and 20,000 for the safety read (`engine/api/wiring.py:107`, `app.py:252-255`).
- **Daily online backups of events, usage, QC, feedback and the meter** use the SQLite backup API and an integrity check, with 14-day rotation (`engine/api/db_backup.py`, `app.py:1054-1062`, checked). The first production upload and a download-and-verify drill ran on 2026-10-16, and row counts matched (`CiC_Backup_Restore_Runbook.md:210-218`).
- **A participant can delete a conversation**, and the deletion reaches backups within 14 days (`app.py:859-877`, checked).
- **A scheduled live check runs four times an hour** (`.github/workflows/live-watch.yml:11`, checked). It watches health, the deployed commit, backup age and disk use (subagent, `tools/live_watch.py`).
- **One real rollback is evidenced**: PRs #851 and #852, 2026-10-10/11 (subagent, System Hub Decision Log).
- **No committed secrets** were found in the current tree (subagent scan; I spot-checked render.yaml: every credential is `sync: false`).

## 3. In process

- **Buying tokens.** Three live Stripe Payment Links, the event destination and `CIC_DEEPER_PRODUCTS` were set by Mark in the dashboards (`Pilot_Feedback_Decisions.md`, "Buying, no test purchase…", 2026-10-23). The buy page can take money. No purchase or refund has been made or proven (same entry).
- **Accounts** (A1d onward, A3 held out of the last promotion). As built, they cannot be switched on: `_build_real_app` passes no mailer, and `build_runtime` refuses to start without one (subagent, `engine/api/accounts_routes.py:106-109`).
- **The cost report** (PR #1055) is on live. Its first reading: about $0.087 for round 1 with checks, and $0.0024 per safety check (subagent, Pilot Feedback Log). Finding F11, whether late rounds are under-priced, is still open.
- **The visitor bound, the door removal and the daily-limit removal** are built and on live (Pilot Feedback Log, "Done" entry; ruling 69).
- **Two V3.6 copies of the Facilitator Governance document** (see R13), and a V3.7 proposal in `Build/reference/L3D-Encounter-Methodology/`.

## 4. Still needed for the full system to be live

1. A safety reply for when the safety check itself cannot run (R1).
2. A proven global spend stop: the AWS Budget deny action set up and tested (R2).
3. Buying proven end to end, with the product mapping made part of the blueprint (R3).
4. Alerting that reaches Mark when conversations fail, not only when `/health` fails (R5).
5. A full safety battery run on the current prompt and model, recorded against the spec's floor of at least 19 of 20 (R4).
6. A decision on the anonymous, possibly-minor visitor (R9), and the age line already listed on the finish line.
7. A mail provider before accounts can run at all (subagent, see §3).
8. A full restore drill: suspend, overwrite, resume (R11).

## 5. Quality: strengths with examples

- **Fail-safe defaults are written down where they are decided.** `resolve_gate` says it plainly: "A message no one has read for risk never reaches the voice" (`engine/m5/failure.py:56-60`). The code does what the comment says for timeouts and SDK errors.
- **Tests hit real code with fakes only at the provider edge.** The API tests load the real fixture package and real stores behind a `FakeBedrockClient` (subagent, `engine/api/tests/conftest.py`). The proof suites fail any skip or xfail (subagent, `test_deeper_proofs.py:280-290`).
- **Money code is careful.** Spending is one guarded `UPDATE`. A claim is written before minting. Minting is idempotent on the payment intent. A full refund or dispute voids the codes. Codes are stored only as SHA-256 (subagent, `engine/deeper/meter.py`, `deeper_routes.py:263-330`).
- **Privacy by construction.** Access logs are off (`engine/Dockerfile:140`, checked). Bound counters are kept as keyed hashes with no session or person in them (`engine/deeper/bound.py:1-9`, checked).
- **The backup module explains its own constraints.** It shows why the backup runs in-process (a Render disk cannot be reached from a cron job) and why it uses online backup, not a file copy (`engine/api/db_backup.py:1-35`).
- **The forwarded client address is read from the right end**, which is correct behind exactly one trusted proxy (`engine/api/ratelimit.py:114-118`).

## 6. Risks, ranked by consequence

### Blocking

**R1. When the safety check cannot run, a person in crisis gets no redirect.**
- *Evidence (checked).* A safety timeout or SDK error routes to `SAFETY_FAILED` = `check_in_turn` (`engine/m5/failure.py:46, 61-62`). The check-in carries no resources (`engine/m4/facilitator_turns.py:97-105, 159-164`). Its words ask the person to confirm: "If it's the first, say so plainly and I'll take it that way." Errors outside the SDK's own types (for example a botocore credential error from `AnthropicBedrock`'s credential chain, `bedrock.py:74-86`) become `ProviderCallFailed`, a 502 (`engine/api/wiring.py:1121-1127`, checked). The frontend then shows "The voice couldn't be reached just now…" (subagent, `cic-poc/frontend/src/lib/api.ts:56-57`). A burst over 40 messages a minute gets a 429 before any screening (`app.py:729-734`, checked).
- *Why this is blocking.* CLAUDE.md, Safety: "never make a redirect conditional on the participant confirming they're okay", and "default to caution". The engine already holds the cautious pattern: past the bound, nobody reads the message, so the fixed line with the redirect is sent anyway (`app.py:93-96`). The failure case is the same situation, a message nobody read for risk, but it gets the weaker reply.
- *Failure scenario.* AWS keys are rotated or expire, or Bedrock throttles, or the Budget deny action (R2) fires. A participant writes "I don't think I can keep going." The safety call fails. They see either a request to clarify, with no help named, or "the voice couldn't be reached."
- *Smallest fix.* On `SAFETY_FAILED`, and on a provider failure during the gate, send the fixed Facilitator line with the code-added redirect, the same text family as `visitor_bound_turn()`. No model call is needed. This changes the safety protocol, so it is Mark's ruling (a governance/methodology decision). The ambiguous-signal check-in (Artifact-4 §3 rule 2) is a separate, already-decided design. This finding is only about the case where nothing read the message.

**R2. No global spend stop is proven to exist.**
- *Evidence (checked).* The weekly door is removed (ruling 69; Pilot Feedback Log: "Free voice now has no weekly money cap"). Mark accepted the risk on the understanding that "the AWS limit is the only backstop" (`Build/Ministry/Operations/Handoffs/2026-10-22_daily-visitor-limits-removed.md:39`). The Model Spend Budget runbook describes an automatic deny action at 100%. No record says it was created or tested. The Decision Log lists it as "Left for Mark" (subagent). The pilot decisions file says "the AWS budget (alert only, or an action that stops spending, and the figure)" is still open (`Pilot_Feedback_Decisions.md:342`, checked). Also, any fault in admission (for example a locked or full meter database on the 1 GB disk) grants the free allowance with nothing counted (`engine/api/deeper_admission.py:176-181`, checked).
- *Failure scenario.* A script rotates through many IPv4 addresses or IPv6 /56 networks, each with its own 550-token window. The only global brake in code is 16 concurrent voice calls (`engine/m4/generation.py:46-47`, checked). At saturation, the subagent's estimate is roughly $3,700 to $11,000 a day (not re-derived; it rests on 10–30 s calls and about $0.08 a round). Against a $200-a-month budget, one bad day is ruinous if the AWS action is only an email. AWS billing data also lags by hours.
- *Smallest fix.* (a) Mark creates and tests the Budget deny action per the runbook, then records the date and the figure (dashboard steps: §2 of `CiC_Model_Spend_Budget_Runbook.md`). (b) Make an admission fault refuse free voice (with the fixed redirect line, per R1) instead of granting it. A global daily dollar breaker in the engine would be a re-opening of ruling 69, so it is Mark's call, not proposed here as settled.

### High

**R3. Buying can take money, but delivery is unproven and partly outside the blueprint.**
- *Evidence (checked).* `CIC_DEEPER_PRODUCTS`, `CIC_DEEPER_GIFT_LINKS` and `CIC_DEEPER_PILOT_LINKS` are not in `render.yaml`, not even as `sync: false` (grep, empty). A paid session whose link is not in the products map returns `ignored_not_ours` and mints nothing (`deeper_routes.py:232-234`). render.yaml itself says the file, not the dashboard, is the source of truth (`render.yaml:24-27`). No purchase has been made (`Pilot_Feedback_Decisions.md`, 2026-10-23). The redirect, fixed quantity and amounts at checkout are "Not confirmed by Mark" (same entry). Paid codes sit in `localStorage` (subagent, `cic-poc/frontend/src/lib/deeper.ts:55, 93`), and the app sets no CSP or other security headers (subagent).
- *Failure scenario.* A dashboard edit, a typo in the JSON key, or a re-created Payment Link leaves one pack's link out of the map. A buyer pays $7. The webhook logs `ignored_not_ours`. No code reaches them, and nothing alerts.
- *Smallest fix.* Declare the three keys in render.yaml as `sync: false`. Refuse startup when `CIC_DEEPER_ENABLED` is on and the products map is empty. Log `ignored_not_ours` at warning level, and have live-watch or the reconciliation report count it. Prove one purchase and refund, in Stripe test mode if Mark does not want to spend.

**R4. The safety classifier's accuracy on the current prompt is not shown against its own floor.**
- *Evidence (checked).* The committed runs are per-batch slices on the pinned Haiku 4.5: 1/5, 0/5, 4/5, 5/5, 4/5, 3/3, 1/2, 3/3 (`engine/m5/reports/safety-script-run-1..8.json`). Each says "spec's eventual floor is >=19/20 across the full ~20-scenario battery, not this 5-scenario slice". No full-battery report is committed. The 19/20 result of 2026-07-21 (System Hub Decision Log:1539) was run against "the local backend" of the July app, before this engine. Not checked: whether it used the same prompt. CI runs only routing logic with fakes (subagent, `ci.yml:496-501`).
- *Failure scenario.* A prompt or routing change since batch 1 has shifted how scenario s3 (harmful dynamic) classifies, and nothing catches it. s3 last failed in run 3 and has no later rerun (subagent).
- *Smallest fix.* One full-battery run (23 scenarios, about 46 small Haiku calls), approved by Mark as a named live test with a cap, its report committed. Repeat it on any change to `live_calls.py` or the pinned safety model.

**R5. Failures of real conversations would go unseen.**
- *Evidence (checked).* `/health` always returns 200 and never checks the database or Bedrock (`app.py:622-634`). `should_page_operator` ("two consecutive degraded gate turns pages the operator") is never called outside tests (grep). Per the subagent: live-watch alerts only through GitHub's failed-workflow email to whoever last edited the schedule; 5xx- and 429-rate alerts are spec only (`CiC_Alerting_Runbook.md:218-227`); there is no error tracking.
- *Failure scenario.* The R1 scenario happens on a quiet evening. Every message returns 502 or a check-in. `/health` says ok. Mark learns of it from a participant, if at all.
- *Smallest fix.* Count degraded gates and `ProviderCallFailed` in memory. Expose the count of the last 15 minutes on `/health` (no text, no ids). Have `live_watch.py` fail on a threshold. Confirm which address receives the workflow-failure email.

**R6. The public site, including the buy and privacy pages, ships from `main` without the promotion gate.**
- *Evidence (checked).* "Its *production* deployment stays on `main`, not `live`" (`CiC_Promotion_Runbook.md:101-107`; Mark, 2026-09-20). Today the privacy page on live reads "During the pilot, Go Deeper sells nothing. We do not take your name, your email or any payment." Live's `go-deeper.html` holds three `buy.stripe.com` links. Main's privacy page has the payment paragraph (commit `fc10ad9d7`). So the public site is right today only because it follows main. The engine the site talks to follows live.
- *Failure scenario.* A site change on main announces a price, pack or feature that the live engine does not yet have. Payment is taken against an engine that cannot honour it, and no review step stood between them.
- *Smallest fix.* Mark's call, since the setting was settled on purpose: either have Cloudflare follow `live`, or add a CI check that fails a PR when site pages name an engine route or setting the live engine lacks.

**R7. The safety classifier's output is not validated, and two bad shapes fail open or crash.**
- *Evidence (checked).* `_forced_tool_call` returns `tool_uses[0].input` without checking it against the schema (`engine/m5/live_calls.py:198-201`). In `route`, a `signal` outside the expected values matches neither `ACUTE_SIGNALS` nor `AMBIGUOUS_LOW_CONFIDENCE`, and routing falls through to the reader and the voice (`engine/m5/routing.py:150-170`). A missing `signal` raises `KeyError`, which ends in the 502 of R1.
- *Failure scenario.* The model returns `"signal": "acute_distress"` (wrong case) or a new label. The Representative answers a crisis message in character.
- *Smallest fix.* Check `signal` against the tool's enum in `_forced_tool_call` or `resolve_gate`. Treat anything else as `parse_failure`, so it routes to `SAFETY_FAILED` (and, after R1, to the redirect). Add two tests.

### Medium

**R8. Safety reads one message at a time.** `call_safety` gets `recent_window=[]` and `accumulator={}`; the comments call the accumulator "RECORDED, NOT CONSULTED" (subagent, `turn.py:144, 173-180`; `engine/m5/safety_accumulation.py:18-25`). The window plumbing exists at `live_calls.py:204-210` (checked). *Scenario:* the check-in asks "is this real?", and the reply "yes" is classified alone, as no signal. The code's own note says the gate then has "no memory of having asked" (`safety_accumulation.py:50-56`). *Fix:* pass the previous participant message, and the fact that a check-in was just asked, into the existing window argument.

**R9. Anonymous visitors face no age line, and nothing handles minors.** Accounts ask "18 or over" (subagent, `engine/accounts/service.py:285-289`). Accounts are off, and the anonymous path has no age statement (subagent). The age line is already on the finish line (`Pilot_Feedback_Decisions.md`, 2026-10-23). *Fix:* the age line plus a policy decision by Mark. Cross-lens with participant experience.

**R10. The single-process design is assumed, not enforced.** Uvicorn runs one process (`engine/Dockerfile:140`, checked), on one instance with a 1 GB disk (`render.yaml:115-122`, checked). Reservations, burst limits, voice slots and the group daily ceiling are in memory (subagent, `meter.py:254, 523-526`), so a restart resets the group ceiling. If `WEB_CONCURRENCY` were set, uvicorn would start several workers, each with its own counters (subagent; not checked in the dashboard). *Fix:* refuse startup when more than one worker is configured, and keep the group ceiling in the meter file.

**R11. Supply chain and build reproducibility.** Python dependencies are lower bounds only, with no lock file or hashes (`fastapi>=0.115.0`, `uvicorn>=0.30`; subagent, `engine/api/requirements.txt`). Base images are pinned by tag, not digest. Actions are pinned by major tag (`.github/workflows/*.yml`, checked: `checkout@v4`, `setup-python@v5`, and others). There is no Dependabot. pytest ships in the production image (subagent). *Scenario:* a release of fastapi or uvicorn lands between CI and a deploy; production runs code CI never ran. *Fix:* a hashed lock file used by both CI and the Dockerfile; pin actions by SHA.

**R12. CI gaps let breakage reach `main` unseen.**
- CI does not run on push to `main` (`ci.yml:73-77`, checked). Merges are tested only as PRs.
- `check-paths`, `live-commentary` and `world-gates` are `continue-on-error: true` (`ci.yml:285, 303, 326, 383`, checked). The comment at `:293` calls live-commentary blocking (subagent).
- Path filters miss dependencies. As a result, `tools/tests` fails on main today, 2 tests (my run). `support.html` changed in `0f2675dca`, and the filter only watches `tools/**` (subagent).
- The docker filter omits `records/`, `packages/` and `cic/texts/`, which the image copies (subagent).

*Fix:* repair the two tests; add `cic-website/**` to the checker filter, and the copied trees to the docker filter.

**R13. Backups: restore half-proven; the claims file is not backed up; copies are unencrypted.**
- The full suspend/overwrite/resume restore has never run ("Not yet run for real", `CiC_Backup_Restore_Runbook.md:218`, checked).
- The claims database, which holds bought codes waiting to be picked up, is not in `backup_extra_dbs` (`app.py:1054-1062`, checked).
- Backups of transcripts are uploaded unencrypted at the application level (same docstring).
- The runbook still says retention is "not yet implemented", but `engine/m7/retention.py` exists (subagent).

*Fix:* one staging restore drill; add the claims file; encrypt at upload before accounts join.

**R14. Admin and app hardening.** The admin cookie is an HMAC of its expiry under the admin token. Changing the password does not revoke issued cookies; only rotating the token does (subagent, `engine/api/admin_auth.py:105-128`). The app sends no CSP, HSTS or frame-ancestors (subagent). *Fix:* add a password-version field to the cookie MAC, and a CSP on the app's static mount.

### Low

- **R15.** 729 remote branches; the 2026-10-23 handoff counted 636 unmerged among 704. `.git` is 2.6 GB with no LFS. All of `cic/texts/` is copied into the production image (subagent, `engine/Dockerfile:94`). Stray `shot-*.png` files sit at the repository root (checked).
- **R16.** Two different files are both named Facilitator Governance V3.6. They differ by one sentence. The `Build/reference/` copy points to `cic-poc/backend/wrs/parameters.yaml`, a retired backend (`diff` of the extracted text, checked). CLAUDE.md names the `Archive/` copy.
- **R17.** Stale operational text: the spend runbook still calls the door "the fast control" (subagent). `ratelimit.py:77` mentions the removed daily cap (subagent). 12 entries in the `check_paths` baseline now resolve (subagent).
- **R18.** The visitor secret has no minimum length (subagent, `required_secrets.py:32, 49`). `req.internal` is set by the client and hides a session from dashboard counts (subagent, `app.py:690, 708`). Open feedback rows keep emails with no age limit (subagent).
- **R19.** Live-surface commentary remains in `engine/` (33 REWRITE hits) and `records/` (40). CLAUDE.md requires a PR that edits such a file to clear it (subagent, report-only check).

## 7. Best parts

1. The safety gate's structure: classify first, voice never on a safety route, fixed crisis text from code, and a cautious bound reply.
2. Payment handling: signed webhooks, idempotent minting, refund voiding, hashed codes.
3. A single, tested model seam with a live-test guard, which makes stray spend structurally hard.
4. Backups with a real production drill and row counts written down.
5. Honest records: the Pilot Feedback files state open risks and accepted risks in plain words, with sources.

## 8. Gaps

- No safety reply for the case where the safety check fails (R1, R7).
- No proven global spend stop (R2).
- No end-to-end proof of buying (R3).
- No alerting on failed conversations or on safety events (R5).
- No full safety battery result for the current engine (R4).
- No age line for anonymous visitors (R9).
- No locked dependencies (R11).
- No full restore drill (R13).

## 9. Cross-lens notes

- *Participant experience:* the check-in wording ("say so plainly and I'll take it that way") and the 502 wording are what a distressed visitor reads. Both should be reviewed for B2 clarity once R1 is ruled.
- *Participant experience:* safety turns are styled like any other Facilitator turn (subagent, `Conversation.tsx:107-121`).
- *Market and sale-readiness:* a buyer's diligence would ask first for R2 (unbounded spend) and R3 (payment without proven delivery).
- *Market and sale-readiness:* the 2.6 GB repository and 729 branches would read as hygiene debt.
- *Scholarly rigor:* `engine/m10/quotes.py` changed on main and is not yet on live. It touches quote checks; that lens may want to see it.
- *Governance:* the pilot decisions record that this session's sibling threads opened PRs #1076 and #1081 into `live` at Mark's word, against CLAUDE.md's default table. That conflict is named there as Mark's to settle.

## 10. Five questions for Mark

1. When the safety check itself fails, should the participant get the fixed line with the redirect, the same as past the monthly bound (R1)?
2. Is the AWS Budget deny action set up, at what figure, and has it been tested (R2)?
3. May a build thread add the three Go Deeper link settings to render.yaml as `sync: false`, and make the engine refuse to start without the products map (R3)?
4. Will you approve one capped live test: the full 23-scenario safety battery on the pinned safety model (R4)?
5. Should the public site keep publishing from `main`, now that it carries payment pages (R6)?
