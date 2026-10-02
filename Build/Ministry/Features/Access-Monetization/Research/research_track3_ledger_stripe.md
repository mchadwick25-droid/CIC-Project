# Track 3 — Record-keeping and Stripe integration for one-time conversation access

**For:** Church in Conversation (Faithways Studio, Inc., Colorado PBC, not a 501(c)(3))
**Date:** 2026-10-02
**Scope:** pay-as-you-go one-time purchases that grant additional conversation access, a free allowance for anonymous visitors, and a ledger reconciled against real Stripe transactions.

**Research note on sources.** This sandbox's egress proxy blocks `stripe.com`, `docs.stripe.com`, and most vendor doc hosts (OpenMeter, Lago, Metronome, TigerBeetle, Modern Treasury). Every Stripe fact below is taken from search-engine snippets of the official docs plus third-party guides, and each is cited. Anything marked **[verify in Stripe docs]** is a specific number or parameter name that Mark (or the implementing thread, from an unblocked network) should confirm against the live doc before it becomes a code constant.

---

## 0. What already exists in the repo (read-only survey)

The recommendations below are shaped to fit this, not to replace it.

| Thing | Where | Relevance |
|---|---|---|
| One FastAPI service on Render (`cic-engine`, Docker, `plan: standard`, single instance), frontend served same-origin | `render.yaml`, `engine/api/app.py` | Same-origin means an HttpOnly cookie reaches the API with no frontend work; single instance means in-process locks are real today but not after the Postgres move. |
| SQLite on a 1 GB Render Disk: `events.db` (session events) and `usage.db` (M8 usage log), WAL mode, daily online backup to R2 | `render.yaml`, `engine/m4/store.py`, `engine/m8/log_store.py`, `engine/api/db_backup.py` | The ledger should be a third SQLite file (or a table in `usage.db`) with the same DECIDABLE pattern and the same backup path; Postgres is the stated destination. |
| **No accounts, no Supabase in the live app.** Supabase holds only the retired pilot's transcripts. | `render.yaml` top comment | Identity today is anonymous. |
| Anonymous visitor identity: random 144-bit id, HMAC-signed, HttpOnly cookie `cic_visitor`, 400-day max-age; id persisted on each session's `session_started` event | `engine/api/anon_cap.py`, `engine/m4/entrance.py` | This is already the natural key to hang a free allowance and a purchase on. |
| Daily anon caps: 5 sessions / 150 turns per visitor, **in-memory, reset on restart** | `engine/api/anon_cap.py` | A soft abuse deterrent, explicitly not a ledger. Paid access cannot ride on it. |
| Per-IP sliding-window rate limit: 6 creates/min, 40 converse/min; admin bucket | `engine/api/ratelimit.py` | Keep; add a webhook bucket. |
| M8 usage log: one row per model call with `trace_id`, `session_id`, `call_kind`, `model_id`, `world_key`, and `usage_json` holding input/output/cache-write/cache-read tokens; "zero unattributed calls" enforced structurally | `engine/m8/usage.py`, `engine/m8/log_store.py` | Already the per-conversation cost telemetry Track 3(e) asks for. The ledger must link to `session_id` and this table already keys on it. |
| Approved price table (Sonnet 4.5 / Haiku 4.5 by `call_kind`), `estimate_cost()` returns *unpriced* when no sourced table exists (spec principle 13) | `engine/m8/price_tables.py`, `engine/m8/cost.py` | Margin-per-purchase can be computed today without inventing numbers. |
| Stripe today: two dashboard **Payment Links** on the public site (`donate.stripe.com` one-time, `buy.stripe.com` monthly). The earlier `cic-poc/backend/app/giving.py` Checkout+webhook build is **retired with the old service**; no Stripe code is live in `engine/`. | `cic-website/support.html`, `Build/Ministry/Features/Funding-Strategy/CiC_Stripe_Setup_Wording_Strategy_Logistics_V0_1.md` | Gifts never unlock anything (the "rung 1/2" decision). Access-granting purchases are "rung 3" and were explicitly deferred to a separate decision. A webhook endpoint has to be built fresh in `engine/api`. |
| Admin auth: Bearer token + 12 h cookie session; `/api/admin/*` routes | `engine/api/admin_auth.py` | A reconciliation report can hang off this. |
| Spec line: "an account is a list of session ids, nothing more" (not built in Phase 1) | `engine/m8/summary.py` docstring | Matches the access-token model proposed below. |
| No "Build a Table" cost-measurement document was found under `Build/` or `engine/` by that name. | grep | Open question 8 below. |

---

## (a) Stripe one-time payment architecture

### Surface choice

| Option | What it is | Fit for CiC |
|---|---|---|
| **Payment Links** (dashboard, no code) | Reusable URL; product/price fixed in dashboard. | Fine for gifts (already in use). Weak for access grants: no per-visit `client_reference_id`/metadata from the app, so tying a payment back to a visitor requires the visitor to re-identify afterwards. |
| **Checkout Session, hosted** (one API call + redirect) | Stripe-hosted page; app creates the session server-side with `metadata`, `client_reference_id`, `success_url`/`cancel_url`; qualifies for PCI **SAQ A** because card fields never touch the app. | **Recommended.** Smallest code surface, same webhook as every other mode, and it is the only surface eligible for Stripe Chargeback Protection should that ever be wanted. |
| **Checkout Session, embedded / Payment Element** | Same Sessions API, Stripe iframe inside the app's own page. | Nicer UX, more frontend work, same backend. Stripe now presents all three as "UI modes" of one Checkout Sessions API, with `checkout.session.completed` the single fulfillment event regardless of mode. Defer; upgrade path is cheap later. |

Sources: [Stripe Checkout vs Payment Element (devstacked)](https://devstacked.tech/blog/stripe-checkout-vs-payment-element), [Checkout vs Payment Links (noorsplugin)](https://noorsplugin.com/stripe-checkout-vs-payment-links/), [PCI/SAQ A for Checkout (cside)](https://cside.com/blog/can-you-use-stripe-for-pci-dss), [Stripe docs index: Checkout Sessions vs PaymentIntents comparison](https://docs.stripe.com/payments/checkout-sessions-and-payment-intents-comparison).

Useful Checkout parameters **[verify in Stripe docs]**: `mode=payment`; `client_reference_id` ("can be used to reconcile the Session with your internal systems"); `metadata` (up to 50 keys, 40-char keys, 500-char values) and `payment_intent_data.metadata` (copies onto the PaymentIntent and Charge so refund/dispute events carry it); `customer_creation` (defaults to `if_required` in payment mode, so no Customer object is created for a guest unless asked); `consent_collection[terms_of_service]=required` with `custom_text[terms_of_service_acceptance][message]` for a refund-policy acknowledgment; `invoice_creation[enabled]=true` if a PDF receipt/invoice is wanted for one-time payments; `expires_at` 30 min–24 h (default 24 h). Sources: [Stripe metadata limits (acodei)](https://www.acodei.com/glossary/stripe-metadata), [customer_creation default changelog](https://docs.stripe.com/changelog/2022-08-01/default-customer-creation-checkout-session), [Checkout policies/consent docs](https://docs.stripe.com/payments/checkout/customization/policies), [receipts for one-time payments](https://docs.stripe.com/payments/checkout/receipts), [session expiry](https://onetwothreesend.com/stripe-checkout-session-expiration-timing/).

### Identity for anonymous buyers — what ties a purchase to access

| Mechanism | How | Pros | Cons |
|---|---|---|---|
| **Visitor cookie id** (already exists) passed as `client_reference_id` | Server creates Checkout Session with the signed `cic_visitor` id; webhook grants to that id. | Zero friction; no PII; fits existing code. | Cookie loss = access loss unless there is a recovery path; sharing is by copying a cookie (hard for normal people, trivial for the determined). |
| **Email from Checkout** (`customer_details.email` on the completed session) | Webhook stores the email (or a salted hash) alongside the grant. | Gives a recovery handle: "enter the email you paid with." | Email in Checkout is **not verified** unless the buyer uses Link (one-time code to phone); so recovery by email alone must send a magic link to that address, never grant on bare entry. Stores PII. |
| **Signed access token / claim code** | Webhook mints a random `access_code`, shown on the success page (after server-side verification) and emailed on the Stripe receipt via `custom_text`/metadata. Entering it binds a new cookie to the purchase. | Works without any email on file; lost-cookie recovery is "paste your code." | Codes get shared; mitigate by binding to at most N devices and logging binds. |
| **Magic link** | Email-only sign-in; purchase bound to the email. | Standard; strongest recovery. | Requires an email sender and deliverability work; introduces accounts by another name. |
| **Device fingerprint** | Hash of UA/IP/etc. | None worth having. | Unreliable, privacy-hostile; not recommended. |

**Recommendation (guest-first, recoverable):** keep purchases keyed to the existing `visitor_id`, and *also* record a salted hash of the Checkout email plus a one-time **claim code** minted by the webhook. Recovery path: a "restore my access" page accepts the claim code, or the email (which triggers a magic link). Accounts (Supabase or otherwise) are not needed for this and should not be introduced for it; the spec's own line "an account is a list of session ids" is exactly a `visitor_id`-to-grants mapping, which is what the ledger provides. Sources: [guest customers in Checkout](https://docs.stripe.com/docs/payments/checkout/guest-customers), [Link one-time code verification (Stripe support)](https://support.stripe.com/questions/using-link-to-save-your-payment-information), [email lives in customer_details.email, not metadata (GitHub issue summarising Stripe guidance)](https://github.com/yea-80y/WoCo-Event-App/issues/749).

---

## (b) Webhook-driven fulfillment

**Authoritative events for a one-time Checkout purchase**

| Event | Treat as | Notes |
|---|---|---|
| `checkout.session.completed` | **Grant only if `payment_status == "paid"`** (or `no_payment_required`). | `status: complete` does not mean paid. For delayed methods (ACH, some bank redirects) `payment_status` is `unpaid` here; return 200 and record a *pending* purchase. Stripe's own fulfillment page says the `payment_status` value is what you use "to decide when to fulfill." |
| `checkout.session.async_payment_succeeded` | Grant (same code path, idempotent). | Only fires for delayed methods. Simplest: **restrict Checkout to cards (and wallets)** so this path is dormant but still handled. |
| `checkout.session.async_payment_failed` | Mark pending purchase failed; no grant. | |
| `checkout.session.expired` | Close the open purchase row. | Housekeeping only. |
| `payment_intent.succeeded` | **Do not fulfill from it.** | Fires alongside `checkout.session.completed`; using both double-grants. |
| `charge.refunded` | Post a reversal. Read `amount_refunded` vs `amount` to tell partial from full. | Card refunds fire this synchronously. **API-version note [verify]:** from `2025-03-31.basil` Stripe changed some charge-event emission for partial-capture/cancel flows; confirm `charge.refunded` is still emitted for ordinary refunds on the pinned API version, and also subscribe to `refund.created`/`refund.updated`. |
| `charge.dispute.created` | Post a *hold* reversal (freeze the remaining credits from that purchase); log for evidence. | Carries the charge id; use `payment_intent` to find the purchase. `charge.dispute.closed` with `status: won` releases the hold; `lost` finalizes the reversal and records the $15 fee. |
| `radar.early_fraud_warning.created` | Consider proactive refund + reversal. | Stripe: refund an EFW when the charge is at or below the dispute fee; most EFWs become disputes. |

Sources: [Stripe fulfillment docs (snippet)](https://docs.stripe.com/checkout/fulfillment), [payment_status guard issue thread](https://github.com/nicolovejoy/prntd/issues/266), [async payment handling thread](https://github.com/AI-Shipping-Labs/website/issues/1423), [checkout.session.completed vs payment_intent.succeeded (Stripe api-discuss)](https://groups.google.com/a/lists.stripe.com/g/api-discuss/c/FfUO09BKoWg), [refund/dispute revocation guidance](https://dev.to/uudg/cancelled-customers-who-keep-access-the-stripe-webhook-bug-nobody-reports-5gbi), [charge.refunded vs refund.updated](https://github.com/HiEventsDev/hi.events/issues/1067), [basil changelog on charge events](https://edge-docs.stripe.com/changelog/basil/2025-03-31/remove-refund-from-partial-capture-and-payment-cancellation-flow), [EFW guidance](https://redo.com/resources/articles/chargebacks/stripe-chargebacks).

**Handler rules**

1. **Verify the signature** with the SDK's `Webhook.construct_event(payload, sig_header, secret)` on the *raw* body (default 5-minute timestamp tolerance; every retry is freshly signed, so late retries still verify). Reject on failure with 400.
2. **Dedupe on `event.id`** in a `stripe_events` table with a unique index; insert before processing; a duplicate returns 200 immediately. Keep rows at least 3 days (Stripe's live retry window), in practice forever (they are tiny).
3. **Also make the business operation idempotent on the Stripe object id** (`checkout.session.id` / `payment_intent.id`), because Stripe can emit two distinct events for one logical change and event-id dedupe alone does not catch that. The ledger's `UNIQUE(source_ref)` constraint does this.
4. **Ordering is not guaranteed.** Never assume `completed` arrives before `refunded`; and `event.created` has one-second resolution, so do not order by it. Each handler re-fetches the object from Stripe (or reads the snapshot) and applies state as a function of current truth, not of arrival order.
5. **Return 2xx fast; do the work in the request only if it is a few local SQLite writes** (it is). Do not call Bedrock or send email inside the webhook.
6. **Retries:** live mode retries with exponential backoff for up to 3 days, then disables the endpoint; test mode retries three times over a few hours. Alert on `webhook_endpoint` failures (Stripe emails; also a daily job that lists `Events` from the last 30 days and replays any id missing from `stripe_events` — Stripe's Events API retains 30 days).
7. **Never grant from the client redirect.** The `success_url` page may call `GET /api/purchase/{session_id}` which only *reads* the ledger; if the webhook has not arrived yet the page polls for a few seconds and then says "your receipt will arrive by email; your access will appear shortly."
8. **Stripe idempotency keys** on every *outbound* create call (`checkout.sessions.create`, `refunds.create`) using `Idempotency-Key = "cs:" + purchase_id`. Stripe keeps keys 24 h and returns the original response on replay; a replay with different params errors.
9. Snapshot (v1) events are what the SDK's `construct_event` expects; thin (v2) events need a separate destination and are not needed here.

Sources: [Stripe webhook retries (svix review)](https://www.svix.com/resources/webhook-reviews/stripe-webhooks-review/), [3-day retry window](https://eventdock.app/webhooks/stripe-webhook-retry), [duplicate/out-of-order reference implementation](https://github.com/Zenn1t/stripe-webhooks-out-of-order), [webhook idempotency guide](https://www.activepieces.com/blog/webhook-idempotency-how-to-handle-duplicate-events-2026), [Events API 30-day retention](https://www.acodei.com/glossary/stripe-webhook), [thin vs snapshot events](https://edge-docs.stripe.com/webhooks/migrate-snapshot-to-thin-events), [idempotent requests (Stripe docs index)](https://docs.stripe.com/api/idempotent_requests).

---

## (c) Ledger design

### Append-only entries, derived balance — not a mutable column

Every money-adjacent system worth copying (Stripe, Square, PayPal, Modern Treasury, TigerBeetle) models balances as the sum of immutable entries; a balance column is at best a verifiable cache. The practical arguments for CiC: an audit trail that explains *why* a visitor has 3 conversations left; reversals that are entries, not overwrites; reconciliation that can replay. At CiC's volume (hundreds of entries per visitor at most) `SUM()` on read is cheap; add a cached balance later only if measured.

Sources: [double-entry wallet, balances derived](https://github.com/Vrinda-Vijay5/double-entry-wallet-ledger), [Modern Treasury on ledgers](https://www.moderntreasury.com/journal/history-of-ledgers), [TigerBeetle immutability and two-phase transfers](https://docs.tigerbeetle.com/single-page/), [pg-ledger: Postgres enforces append-only](https://github.com/osmncnylmz/pg-ledger).

### How the metering products model this (the parts worth borrowing)

- **OpenMeter**: a *grant* is "a singular record of granting some amount of usage" with priority, expiration, rollover; balance is burned down against active grants "in order by priority (lower first), then by expiration (sooner first), then by effective date (oldest first)"; grants carry "a ledger-style history where you can follow how and why a customer's balance changes." Borrow: **free grants burn before paid grants** (priority), **paid grants expire later or never**, and **consumption records which grant it drew from**. Sources: [OpenMeter balances, grants, rollovers](https://openmeter.io/blog/launchweek-2-02-balances-grants-and-rollovers), [OpenMeter grant docs](https://openmeter.io/docs/billing/entitlements/grant).
- **Metronome**: every balance "contains a ledger, which tracks all invoice deductions, manual adjustments, expirations, or true-ups"; a `credit_segment_expiration` entry type records unused credit that expired; drain order is tier then priority. Borrow: **expiration is an entry, not a deletion**. Sources: [Metronome prepaid credits guide](https://docs.metronome.com/guides/pricing-packaging/billing-model-guides/prepaid-credits), [Metronome balance tracking](https://docs.metronome.com/guides/customers-billing/optimize-customer-experience/get-remaining-balance).
- **Lago**: wallets with paid vs. granted (free) credits, up to 5 wallets per customer each scoped to fees; the authoritative balance updates at invoice finalization, with a real-time "ongoing balance" alongside. Borrow: the **two-number display** — settled balance vs. balance-net-of-open-holds. Source: [Lago wallet overview](https://getlago.com/docs/guide/wallet-and-prepaid-credits/overview).
- **Stripe Billing credits** (credit grants): designed for usage-based *subscription invoices*; grants have applicability, priority, expiry, and a balance-transaction history. Not usable for CiC's no-subscription model (they offset invoices, not a custom entitlement), but the object shape (grant → credit balance transactions) is the same pattern. **[verify in Stripe docs]** Source index: [Stripe billing credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits).

### Unit of account — decision needed (open question 1)

Options: (i) **conversations** (a session), (ii) **turns**, (iii) **minutes**, (iv) **cost-backed credits** (an internal unit priced to the M8 cost model). Recommendation: sell and display **conversations**, and meter *turns within a conversation* only as an abuse ceiling (the existing 150/day), because a participant can reason about "three more conversations" and cannot reason about tokens. The margin analysis in (e) still works per conversation.

### Hold, then capture or release (the failed-response / accidental-exit problem)

The naive pattern — decrement when the conversation starts — charges for a Bedrock error, a tab closed by accident, or a dropped connection. The naive pattern in the other direction — decrement at the end — lets a visitor open unlimited conversations concurrently. The standard answer is the card pre-authorization shape, which TigerBeetle calls a *pending transfer* (reserve now; later *post* for the actual amount or *void*, with an optional timeout that auto-voids) and which LLM-billing write-ups describe as reserve → call → settle/release, releasing on 4xx/5xx and thrown errors.

Applied to CiC, one conversation = one unit:

1. **Start:** in one transaction, check `available = settled_balance − open_holds ≥ 1`, insert a `hold` entry (`−1`, `status=open`, `session_id`, `expires_at`). If not available, refuse with the existing cap message. This is the only place a concurrency race exists; see "Atomicity" below.
2. **First substantive turn succeeds** (a voice turn returned and was stored as a `session_events` row): post a `capture` entry (`−1` finalised, `source_ref=session_id`) and close the hold. Before that point the visitor has paid for nothing.
3. **Nothing substantive happened** (session created, then error, idle-close, or exit before any turn landed): post a `release` entry (`+1`) referencing the hold. The existing `engine/m4/idle_close.py` thread is the natural place for the sweep: any `open` hold past `expires_at` with zero stored voice turns is released; any with ≥1 is captured.
4. **Mid-conversation failure after capture:** the unit is spent, by design — the participant got a conversation. But a Bedrock error on turn *n* should never cost a *second* unit, and the turn itself is retried free. Policy knob: if a conversation dies before turn k (say 3), release instead of capture. Record the policy constant in one place.
5. **Disconnect/reload:** because the hold is keyed on `session_id`, reopening the same session (the frontend already stores it) does not open a second hold.

Sources: [reservation pattern for LLM budgets](https://agenticspendguard.dev/docs/use-cases/reservation-pattern/), [Stigg on reserve-then-settle](https://www.stigg.io/blog-posts/usage-based-api-billing), [Firecrawl reservation PR (race condition fix)](https://github.com/firecrawl/firecrawl/pull/2659), [orphaned reservations issue (why holds need a sweep)](https://github.com/Open-Finance-Lab/AgenticTrading/issues/554), [TigerBeetle two-phase transfers](https://docs.tigerbeetle.com/single-page/).

### Free vs paid grants

- **Free allowance** = a `grant` entry with `kind=free`, `priority=0`, `expires_at=end of UTC day` (or week), minted lazily the first time a visitor id is seen in a period. The existing in-memory daily cap stays as the burst/abuse guard; the *ledger* becomes the source of truth for "how many free conversations are left," and it survives restarts (fixing the acknowledged false-negative in `anon_cap.py`).
- **Paid grant** = `kind=paid`, `priority=10`, `expires_at` NULL or long (open question 3), `source_ref=checkout.session.id`, `purchase_id` FK.
- Holds and captures draw from the lowest-priority, soonest-expiring grant with remaining balance (OpenMeter's order). Record `grant_id` on each consumption entry so a refund can reverse exactly the unused remainder of *that* purchase.
- **Expiration** is a sweep that posts `expire` entries for the unused remainder; never a delete.

### Atomicity

Today (SQLite, one process): wrap "check available + insert hold" in `BEGIN IMMEDIATE` so a second writer waits rather than reading a stale sum; SQLite ignores `SELECT … FOR UPDATE`. After the Postgres move: a single conditional statement or `SELECT … FOR UPDATE` on the visitor's row-lock stand-in (a `visitor_locks` table with one row per visitor) inside the transaction. Keep the ledger write path in one module so the swap is local. Sources: [SQLite BEGIN IMMEDIATE vs Postgres FOR UPDATE](https://github.com/scanner/mibudge/pull/62), [credits_remaining -= 1 is a race](https://dev.to/indierob_/creditsremaining-1-is-a-race-condition-52fo), [Postgres race-condition handling](https://oneuptime.com/blog/post/2026-01-25-postgresql-race-conditions/view).

---

## Recommended data model

Three new tables beside the existing `session_events` and `usage_log`. All timestamps ISO-8601 UTC text (matching the existing stores). Amounts in **integer units** (conversations) for the access ledger; **integer cents** for money.

```
stripe_events            -- webhook dedupe + raw audit
  event_id        TEXT PRIMARY KEY     -- evt_...
  event_type      TEXT NOT NULL
  livemode        INTEGER NOT NULL     -- refuse test events on prod and vice versa
  object_id       TEXT                 -- cs_..., pi_..., ch_..., dp_...
  received_at     TEXT NOT NULL
  processed_at    TEXT                 -- NULL until handler committed
  payload_json    TEXT NOT NULL        -- the snapshot, verbatim (no card data exists in it)

purchases                -- one row per Checkout Session the app created
  purchase_id     TEXT PRIMARY KEY     -- app uuid; also the Stripe Idempotency-Key
  visitor_id      TEXT NOT NULL        -- anon_cap id at time of purchase
  product_code    TEXT NOT NULL        -- e.g. "conv_3", "conv_10"
  units           INTEGER NOT NULL     -- conversations purchased
  amount_cents    INTEGER NOT NULL     -- list price
  currency        TEXT NOT NULL
  checkout_session_id TEXT UNIQUE      -- cs_...
  payment_intent_id   TEXT UNIQUE      -- pi_...
  charge_id       TEXT UNIQUE          -- ch_...
  balance_transaction_id TEXT UNIQUE   -- txn_...  (filled by reconciliation; carries fee/net)
  stripe_fee_cents INTEGER             -- from balance transaction
  net_cents        INTEGER
  payout_id       TEXT                 -- po_... once paid out
  status          TEXT NOT NULL        -- created | pending_async | paid | failed | expired | refunded | partially_refunded | disputed | dispute_won | dispute_lost
  email_hash      TEXT                 -- salted SHA-256 of customer_details.email (recovery), never the plaintext
  claim_code_hash TEXT                 -- salted hash of the one-time recovery code
  created_at, updated_at TEXT NOT NULL

access_ledger            -- append-only; balance = SUM(delta) per visitor
  entry_id        TEXT PRIMARY KEY     -- uuid
  visitor_id      TEXT NOT NULL
  kind            TEXT NOT NULL        -- grant_free | grant_paid | hold | capture | release | reverse | expire | adjust
  delta           INTEGER NOT NULL     -- +units or -units; hold is -N, release is +N
  grant_id        TEXT                 -- the grant this entry draws on / reverses (NULL for grants)
  priority        INTEGER              -- grants only: 0 free, 10 paid
  expires_at      TEXT                 -- grants only
  purchase_id     TEXT                 -- grant_paid / reverse
  session_id      TEXT                 -- hold / capture / release
  source_ref      TEXT UNIQUE          -- idempotency: "cs:<id>" for a paid grant, "hold:<session_id>", "capture:<session_id>", "refund:<re_id>", "dispute:<dp_id>", "free:<visitor>:<day>"
  reason          TEXT                 -- adjust entries: who/why (admin token id + note)
  created_at      TEXT NOT NULL
  INDEX (visitor_id, created_at)
```

Why `source_ref UNIQUE` matters: it makes every business operation idempotent independent of event-id dedupe (rule 3 above). An `adjust` entry is the only kind an admin can write by hand, and it requires a `reason`.

Linking to cost: `usage_log.session_id` → `access_ledger.session_id` (capture) → `purchases` via `grant_id`. No schema change to `usage_log` is needed.

---

## Event flow (text diagram)

```
VISITOR (anon cookie cic_visitor)                                    ENGINE (FastAPI, one instance)                      STRIPE
 │                                                                        │                                                 │
 │ GET /api/session  ──────────────────────────────────────────────────▶  │ ledger.available(visitor)                       │
 │                                                                        │   ≥1 → BEGIN IMMEDIATE; insert hold(-1,         │
 │                                                                        │        session_id, expires_at); COMMIT          │
 │                                                                        │   =0 → 429 "no conversations left" + offer      │
 │ ◀─ session_id (or 429 + buy link) ─────────────────────────────────── │                                                 │
 │ POST /message … first voice turn stored ──────────────────────────▶   │ insert capture(-1,"capture:<session>"), close    │
 │                                                                        │ hold   [or idle_close sweep: release(+1) if 0   │
 │                                                                        │ turns / capture if ≥1 after expires_at]         │
 │                                                                        │                                                 │
 │ POST /api/purchase {product_code} ─────────────────────────────────▶  │ insert purchases(created); Idempotency-Key=     │
 │                                                                        │ purchase_id; checkout.sessions.create(          │
 │                                                                        │   mode=payment, client_reference_id=visitor,    │
 │                                                                        │   metadata{purchase_id}, payment_intent_data.   │
 │                                                                        │   metadata{purchase_id}, consent_collection,    │
 │                                                                        │   success_url=/thanks?pid=…) ────────────────▶  │
 │ ◀─ 303 to checkout.stripe.com ─────────────────────────────────────── │ ◀──────────────────── cs_… ───────────────────── │
 │ (pays on Stripe-hosted page; Radar screens; receipt emailed by Stripe) │                                                 │
 │                                                                        │ ◀── POST /api/stripe/webhook  (signed) ───────── │
 │                                                                        │ verify sig; INSERT stripe_events(event_id) or   │
 │                                                                        │   return 200 if duplicate                        │
 │                                                                        │ checkout.session.completed & payment_status=paid│
 │                                                                        │   → purchases.status=paid, pi/ch ids, email_hash│
 │                                                                        │   → insert grant_paid(+units,"cs:<id>")  (UNIQUE│
 │                                                                        │     makes a second event a no-op)               │
 │                                                                        │   → mint claim_code, store hash                 │
 │                                                                        │ processed_at=now; 200                           │
 │ ◀─ /thanks polls GET /api/purchase/<pid> (read-only) ──────────────── │ returns status + new balance + claim code once  │
 │                                                                        │                                                 │
 │                                                                        │ ◀── charge.refunded ─────────────────────────── │
 │                                                                        │   partial: reverse(-min(unused, units*refund/   │
 │                                                                        │   amount)); full: reverse(-unused), status      │
 │                                                                        │ ◀── charge.dispute.created ──────────────────── │
 │                                                                        │   hold(-unused,"dispute:<dp>"), status=disputed │
 │                                                                        │ ◀── charge.dispute.closed (won|lost) ────────── │
 │                                                                        │   won: release; lost: capture + record fee      │
 │                                                                        │                                                 │
 │                                                                        │ DAILY (in-process thread, like db_backup.py):   │
 │                                                                        │   reconcile() — see next section ─────────────▶ │
 │                                                                        │ ◀─ balance_transactions, payouts, events(30d) ─ │
```

---

## (d) Reconciliation procedure

Run daily (same in-process-daily-thread pattern as `engine/api/db_backup.py`, since a Render cron cannot reach the disk), write a `reconciliation_runs` row with counts and every mismatch, and expose the last run at `/api/admin/reconciliation` behind the existing admin auth.

**Step 1 — Events replay (catch missed webhooks).** List Stripe `Events` for the last 2 days (API retains 30; a small window keeps it cheap) filtered to the subscribed types; any `event.id` not in `stripe_events` is processed through the same handler. This is the backstop for the 3-day retry window and for an endpoint Stripe auto-disabled.

**Step 2 — Purchases ↔ Stripe (money side).** For each `purchases` row with status `paid` and no `balance_transaction_id`, retrieve the PaymentIntent with `expand[]=latest_charge.balance_transaction`; store `charge_id`, `balance_transaction_id`, `stripe_fee_cents`, `net_cents`. Then list `BalanceTransactions` (type `charge`, `refund`, `adjustment` for disputes, `stripe_fee`) created since the last run and match on `source`:
- **Orphan (paid in Stripe, no purchase row or no grant):** flag `ORPHAN_PAYMENT`; auto-create the grant only if the Checkout Session's metadata carries a known `purchase_id` and `livemode` matches; otherwise hold for Mark (money was taken; the fix is a grant *or* a refund, never silence).
- **Duplicate grant (two `grant_paid` for one `cs_`):** cannot happen with `source_ref UNIQUE`, but check anyway and flag `DUPLICATE_GRANT` with an `adjust` entry proposed, not applied.
- **Grant with no money (ledger says paid, Stripe has no succeeded charge):** `UNBACKED_GRANT` — the serious one; freeze remaining units with a hold and escalate.
- **Refund amount mismatch:** compare `charge.amount_refunded` to the sum of `reverse` entries' implied cents; flag `REFUND_MISMATCH`.
- **Dispute:** reconcile `dispute` balance transactions (amount withdrawn + $15 fee) against `disputed` statuses.

**Step 3 — Payouts ↔ bank.** For each `payout.paid` since last run, list `BalanceTransactions?payout=po_…` and tag each purchase row's `payout_id`; sum `net` and compare to `payout.amount`. The bank deposit should equal `payout.amount` exactly; the Stripe **Payout reconciliation report** (Dashboard → Reports, CSV) is the accountant-facing version of the same join and is free. Stripe recommends automatic payouts precisely because the payout ↔ balance-transaction association is kept for you. Sources: [Payout reconciliation report type](https://docs.stripe.com/reports/report-types/payout-reconciliation), [balance transactions by payout (Stripe api-discuss)](https://groups.google.com/a/lists.stripe.com/g/api-discuss/c/nCR65yXGayI), [reconciling refunds/disputes/payouts without double counting](https://caigeek.com/en/blog/how-do-i-reconcile-stripe-refunds-disputes-and-payouts).

**Step 4 — Ledger self-check.** For every visitor: `SUM(delta)` ≥ 0; no `capture` without a prior `hold` for the same session; no open hold older than `expires_at` + grace; every `grant_paid` has a `purchases.status ∈ {paid, partially_refunded, disputed, dispute_won}`. Any violation is a run failure, not a warning (the repo's own "unlisted defect fails the run" rule).

**Step 5 — Usage ↔ ledger.** Every `session_id` with ≥1 `voice_generation` row in `usage_log` must have a `capture` (or a free-grant capture) in the ledger; every capture must have ≥1 voice row. This is the "zero unattributed calls" gate extended one layer up.

**Stripe reporting tools at small scale.** Sigma: $10/mo annual ($15 monthly) up to 250 charges; free in sandbox and free with Data Pipeline. Data Pipeline: $50–65/mo at ≤250 charges, syncs to Snowflake/Redshift/Databricks. Neither is needed while the API join above fits in a daily thread; the free Dashboard reports (Balance, Payout reconciliation, Balance change from activity) cover the accountant. Revisit Sigma only if Mark wants ad-hoc SQL over Stripe without touching the app. Sources: [Sigma pricing (definite.app)](https://www.definite.app/blog/stripe-sigma-pricing), [Stripe support: Sigma & Data Pipeline pricing](https://support.stripe.com/questions/understanding-stripe-sigma-and-data-pipeline-pricing).

**Accounting-grade records.** Store gross, fee, net, and payout id per purchase (above); book Stripe's balance as a clearing account; revenue is recognized when the conversation is captured, not when paid, if the accountant wants deferred-revenue treatment for unused units (the ledger supports both views because grants and captures are separate entries) — **verify with accountant**.

**Retention and audit trail.** `stripe_events` and `access_ledger` are append-only and kept for the tax-record horizon (7 years is the common US guidance — **verify with accountant**). PII minimization: store Stripe ids (`cs_`, `pi_`, `ch_`, `cus_` if ever created) and a salted email hash; never the plaintext email in the ledger, never card data (Checkout keeps the app at SAQ A). A deletion request: delete the visitor's `session_events` per the existing `deletion_requested` design, null the `email_hash`/`claim_code_hash`, keep the money rows (legal retention), and note that Stripe itself retains transaction data under KYC/AML obligations and handles subject requests via privacy@stripe.com. **Privacy law applicability:** CCPA/CPRA applies only above $25M revenue, 100k consumers, or 50% revenue from selling data — Faithways is far below; GDPR applies if the service is *targeted* at people in the EU, not merely reachable from there — **verify with counsel** if EU-facing marketing ever happens. Sources: [CCPA thresholds](https://baylegal.com/ccpa-small-business-requirements/), [GDPR extraterritorial scope](https://pandectes.io/blog/how-gdpr-applies-to-non-eu-businesses/), [Stripe data deletion practice](https://support.spectora.com/en/articles/10041453-stripe-data-deletion-process), [GDPR retention guidance for developers](https://dev.to/jguillaumesio/gdpr-data-retention-and-deletion-a-practical-guide-for-developers-58jf).

---

## (e) Usage-vs-cost telemetry

Nothing new is needed on the capture side: `usage_log` already records input, output, cache-write and cache-read tokens per call with `session_id`, `call_kind`, `model_id`, `world_key`, and `engine/m8/price_tables.py` prices each `call_kind` from a sourced table, returning *unpriced* for anything unrecognised. What Track 3 adds is the join:

- **Margin per purchase** = `purchases.net_cents` − Σ over sessions captured against that purchase's grant of `estimate_cost(usage_log rows)`. Free-grant sessions have revenue 0 and are the "cost of the free allowance" line.
- **Cost per conversation distribution** (p50/p95 by world) is what prices the unit; it comes straight from grouping `usage_log` by `session_id`.
- Add one `reconciliation_runs` column set: `period_revenue_net_cents`, `period_model_cost_cents` (priced), `period_unpriced_calls` (must be 0 or explained), so the daily run also produces a margin line.
- **Bedrock invoice leg.** Spec principle 13 ("no $/token figure quoted onward until measured on the billing provider") means the price table is still an approved *published-rate* decision, not an invoice-reconciled one. The same daily job should, monthly, compare Σ priced cost to the AWS Bedrock invoice line and record the ratio; until that leg exists, margin figures are labelled "at published rates."
- **Feeding the Table cost effort.** The grouping above is per session; the Table (multi-voice) already tags `world_key` per call, so per-world cost at a table is available without schema change. The separate measurement effort should consume `usage_log` + the ledger's `capture` rows rather than instrument anything new (open question 8 on what that document is called).

---

## (f) Abuse and fraud

**Free-tier abuse (anonymous).** Layers, cheapest first:
1. Keep the per-IP burst limiter and the per-visitor daily cap (now ledger-backed, restart-proof).
2. Add **Cloudflare Turnstile** (free, unlimited, privacy-preserving, tokens single-use and ~5 min) on *free-grant minting* — i.e. the first session of a new visitor id per day — not on every turn. This is the one control that defeats "clear cookies, get a new free allowance." The site already uses Cloudflare; Turnstile can be embedded without routing traffic through Cloudflare. Sources: [Turnstile pricing/limits](https://prosopo.io/tools/cloudflare-turnstile-pricing/), [Turnstile overview](https://www.cloudflare.com/products/turnstile/).
3. Per-IP cap on *new visitor ids per day* (e.g., 10) in addition to per-visitor caps — catches cookie-clearing without Turnstile and NAT'd classrooms are still fine.
4. No device fingerprinting.

**Card testing on low-ticket checkouts.** Hosted Checkout plus Radar (included in standard pricing) is the main defence; Stripe's built-in rule example is "Block if total_charges_per_ip_address_hourly > 1" and Radar scores every card payment 0–99. Radar for Fraud Teams (custom rules, ~$0.02 per screened transaction — **[verify]**) is only worth adding if attacks appear. App-side: rate-limit `POST /api/purchase` per IP and per visitor (e.g., 3 open Checkout Sessions per visitor per hour), set `expires_at` to 30–60 minutes, and never expose a client-side PaymentIntent flow. Sources: [Radar rules 101](https://stripe.com/guides/radar-rules-101), [Radar pricing](https://stripe.com/radar/pricing), [card testing response](https://paymentfarm.com/how-stripe-radar-responded-card-testing/).

**Dispute risk on small digital goods.** US dispute fee $15 (never refunded); since 17 June 2025 a second $15 counter fee when you contest, refunded only if you win. On a $5–$10 purchase, contesting is uneconomic; policy: **refund fast and freely on request, and auto-refund EFWs at or below the fee**, which is Stripe's own guidance. Keep access logs (session timestamps, turn counts, claim-code binds) as evidence for the rare case worth contesting. Stripe Chargeback Protection (0.4%, Checkout-only, fraud-type disputes only, needs ~6 months history) is not worth it at this ticket size unless the dispute rate climbs. Sources: [dispute fees](https://www.chargeflow.io/blog/stripe-dispute-fees), [June 2025 dispute pricing (Stripe support)](https://support.stripe.com/questions/june-2025-pricing-updates-for-disputes), [Chargeback Protection terms](https://www.chargeback.io/blog/what-is-stripe-chargeback-protection), [EFW refund guidance](https://redo.com/resources/articles/chargebacks/stripe-chargebacks).

**Test strategy.** Stripe test clocks apply to Billing/subscription objects, not one-time payments — not needed. Use: the Stripe CLI (`stripe listen --forward-to localhost:8000/api/stripe/webhook`, `stripe trigger checkout.session.completed`, which builds the product/price/session fixture chain); the test cards `4242…4242` (success), `4000 0000 0000 0259` (succeeds then disputed as fraudulent), `4000 0000 0000 2685` (not received dispute), `4000 0025 0000 3155` (3DS required), the refund-fails card; and a replay harness that feeds the handler every permutation of {completed, refunded, dispute.created} in every order with duplicates, asserting the final ledger is identical. Sources: [Stripe CLI local testing](https://learnedgeek.com/Blog/Post/testing-stripe-webhooks-with-cli), [test card list](https://checkoutpage.com/tools/stripe-test-cards), [test clocks (Stripe docs index)](https://docs.stripe.com/billing/testing/test-clocks), [ordering harness](https://github.com/Zenn1t/stripe-webhooks-out-of-order).

**Test plan outline**
1. Unit: ledger invariants (balance ≥ 0; hold→capture/release; priority order; expiration entry; UNIQUE source_ref makes replays no-ops).
2. Unit: webhook handler with recorded fixtures — bad signature → 400; duplicate event id → 200 no-op; `completed` with `unpaid` → pending, no grant; `async_payment_succeeded` → grant; partial/full refund → correct reverse; dispute created/closed won/lost.
3. Property/replay: all orderings and duplicates of the lifecycle converge.
4. Concurrency: N parallel session creates against balance 1 yield exactly one hold (SQLite `BEGIN IMMEDIATE`).
5. Integration (test mode, staging service): real Checkout with test cards through to `/thanks`; kill the webhook endpoint, pay, restore, confirm the daily replay grants; dispute card flow; refund from Dashboard flows back.
6. Reconciliation: seed an orphan payment, a duplicate event, an unbacked grant; run reconcile; assert each flag.
7. Mode guard: a test-mode event hitting prod (livemode mismatch) is rejected and logged.

---

## (g) Compliance basics — verify with counsel/accountant

- **Refund policy:** publish one; the digital-goods norm is "refund on request within N days if unused units remain," and for a small ticket a no-questions refund is cheaper than any dispute. Collect acknowledgment in Checkout via `consent_collection`. Reversals in the ledger are proportional to unused units; a goodwill refund can leave access in place (policy choice).
- **Receipts:** Stripe emails a receipt automatically when "Successful payments" is on in Customer emails; `invoice_creation[enabled]` gives a PDF invoice-receipt for one-time payments if wanted. The app need not issue its own.
- **Stripe Tax:** 0.5% per transaction (no-code) / $0.50 per API transaction, no monthly minimum, charged only in jurisdictions where registered. Economic-nexus thresholds for remote sellers start at $100k sales or 200 transactions in most states; digital-goods taxability varies by state. At CiC's scale the obligation is unlikely to exist yet; turning on Stripe Tax *threshold monitoring* is cheap insurance. Sources: [Stripe Tax pricing](https://frontdeskreview.com/software/sales-tax-automation/stripe-tax/), [US economic nexus intro](https://stripe.com/guides/introduction-to-us-sales-tax-and-economic-nexus), [Stripe Tax digital goods limits](https://goodvat.com/guides/usa-sales-tax/stripe-tax-digital-goods/).
- **Nonprofit fee rate:** Stripe's 2.2% + 30¢ rate requires registered 501(c)(3) status, ≥80% of volume as tax-deductible donations, and an application; it covers donations only. Faithways is a Colorado PBC, so **not eligible**; standard 2.9% + 30¢ applies, and refunds do not return the processing fee. If a 501(c)(3) affiliate ever exists, paid access would still be at standard rates. Sources: [Stripe nonprofit discount](https://www.whitelabel.ai/blog/stripe-nonprofit-discount), [Givebutter summary](https://givebutter.com/blog/stripe-for-nonprofits), [refund fee policy](https://www.hubifi.com/blog/stripe-fees-for-refunds).
- **PBC record-keeping:** gifts to a Colorado PBC are not deductible (already disclosed on the Support page); the annual benefit report is a statutory duty; if the PBC solicits for a purpose that meets the Colorado Charitable Solicitations Act definition it may need to register — **verify with counsel**. Keep gift records and sale records in separate Stripe products/metadata so the two never mix in reports. Sources: [Colorado PBC Q&A](https://www.fwlaw.com/insights/colorado-public-benefit-corporations-qa), [Colorado SOS charity registration](https://www.coloradosos.gov/pubs/charities/CCSARegInstr.html).

---

## Recommended architecture in one paragraph

Hosted Stripe Checkout Sessions created server-side with the visitor's existing signed cookie id as `client_reference_id`; fulfillment only from signature-verified webhooks, deduped by event id and by Stripe object id, granting only on `payment_status=paid`; an append-only `access_ledger` in the same SQLite-then-Postgres store as `usage_log`, with free and paid grants burned in priority order and a hold → capture/release cycle per conversation so a failed or abandoned session never costs a unit; refunds and disputes posted as reversals, never as edits; a daily in-process reconciliation that replays missed events, joins purchases to balance transactions and payouts (fee, net, payout id), checks ledger invariants, and emits a margin line from the existing M8 cost tables; Turnstile on free-grant minting and Radar defaults on Checkout; a free-refund policy because the dispute fee exceeds the ticket.

---

## Open questions and uncertainties for Mark

1. **Unit of sale** — conversations (recommended), turns, or time? Pricing itself is a Funding-Strategy decision, but the ledger's unit must be chosen first.
2. **Free allowance shape** — per day (matches `anon_cap`), per week, or a one-time starter? And does a paid visitor keep getting the free allowance (recommended yes, free burns first)?
3. **Do paid units expire?** Never (simplest, cleanest for refunds) vs. 12 months (limits deferred liability). Accountant input.
4. **Recovery path** — claim code only, or claim code + email magic link (needs an email sender; none exists in `engine/`)?
5. **Refund policy wording and window**, and whether a goodwill refund leaves access in place.
6. **Hold policy constant** — capture on first voice turn (recommended) or on turn k?
7. **Where the ledger lives** — new `access.db` file on the disk (matches the one-store-per-concern pattern) vs. tables in `usage.db`. Either way it joins the daily backup.
8. **"Build a Table" cost-measurement effort** — no document by that name was found; which file/thread is it, so (e) can point its output at the right consumer?
9. **Checkout payment methods** — cards + wallets only (keeps `async_payment_*` dormant) or also ACH/bank?
10. **API version pin** — confirm on the pinned Stripe API version that `charge.refunded` still fires for ordinary refunds (the 2025-03-31.basil changelog touched charge events), and whether to subscribe to `refund.*` instead/as well. **[verify in Stripe docs]**
11. **Stripe-side facts to re-verify from an unblocked network** before they become constants: metadata limits (50/40/500), `customer_creation` default, `expires_at` bounds, 5-minute signature tolerance, 3-day live retry window, 30-day Events retention, 24-hour idempotency-key window, Radar for Fraud Teams per-transaction price, Sigma tiers.
12. **Counsel/accountant items:** sales-tax nexus posture and whether to enable Stripe Tax monitoring now; revenue recognition for unused units; retention horizon for money records; Colorado charitable-solicitation registration if gifts are solicited for a charitable-purpose clause in the PBC articles; GDPR exposure if EU-facing.
13. **Governance note:** paid access gating is the deferred "rung 3" in the Go-Live cost model; building it is a Funding-Strategy decision (the `cic-org-funding-strategy` thread), not something Track 3 can converge alone.
