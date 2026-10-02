# SH-9 — Set Up Stripe for Contributions: Wording, Strategy, Logistics

**Date:** 2026-07-31. **Status:** built and verified offline; not live until the
account setup in Part C below is done. The Phase-1 hold on funding/support gifts
(`Decision-Log.md`, 2026-07-22 cross-reference entry) was lifted by Mark the same
day this was built.

## Part A — Wording

Ask copy, suggested amounts, and the "where this goes" line are taken directly
from `Build/Ministry/Funding/CiC_Go_Live_Cost_Model_V0_1.md` Part C.3 — the document
`cic-website/README.md` already named as the source of truth before changing
amounts or copy on the Support page. Two adaptations, both flagged rather than
silently made:

- The Go-Live doc's own example ask line ("$10/month keeps the Table open for
  ten more seekers") pairs a $10 figure with monthly framing, but the
  document's own suggested *recurring* amount is $8, not $10 — one-time is
  the $10 figure. Rather than ship a line whose number doesn't match the
  button next to it, each tier now states its own real per-tier line using
  the same $1/user/month unit-cost logic the document describes as the
  method: **one-time** "$10 covers a full month of access for someone who
  couldn't otherwise afford it," **monthly** "$8 a month keeps the Table
  open for eight more seekers."
- **"Keep the Table Open" is now the section's explicit label**, not just
  implicit in the body copy the way it was before. The Funding Strategy
  thread's own roadmap (`CiC_Business_Roadmap_V0_1.md`) still lists final
  gesture terminology as genuinely open (candidates on the table: "Hold a
  seat," "Steward of the Table"). This build reused the phrase already live
  in Mark-approved copy rather than picking a new, untested one — cheapest
  to change later if that thread converges on something else.

The PBC/no-tax-deduction disclosure on the page is new copy, written to match
the honesty level of the Case for Support draft's own approved line ("gifts to
Faithways Studio are not tax-deductible under this structure... that is the
honest cost of that choice") and the exact entity facts already public in
`cic-website/README.md` (Colorado PBC, Entity ID 20261874960, no 501(c)(3)).

## Part B — Strategy

This build covers Go-Live Cost Model rungs 1 and 2 (Part C.2) in one pass, not
sequentially — a single Stripe Checkout integration handles both a one-time
gift and a recurring monthly pledge, so there was no reason to ship the
simpler rung first and the recurring one later. Matches rung 1/2's own stated
constraint exactly: **no accounts, no Supabase, no feature-gating** — a gift
never unlocks anything in the app, and giving works whether or not the giver
has ever opened a conversation.

**Deliberately not built, and why:** rung 3 (gating a real feature behind
payment) is explicitly the *next* rung, not this one, per the Go-Live doc's
own sequencing ("only build #3 once #1/#2 prove there's something worth
gating"). SH-12 (the $15/mo tier system) is that future rung when it comes -
a separate task, separate decision, not scope creep onto this one. There is
also no donor database here: the only durable record a gift leaves in this
app is a structured `[giving_completed]` log line (see Part D) - Stripe's own
dashboard and its automatic email receipt are the real record. A donor CRM,
gift history, or receipts issued by this app are all real possible future
work, genuinely out of scope for "wording, strategy, and logistics."

## Part C — Logistics: what's left to actually do (yours, not mine)

Same discipline as the Go-Live Cost Model's own Part D: these are personal
account-creation and dashboard steps only you can do.

1. **Create a Stripe account** (or confirm you already have one) at
   stripe.com, for Faithways Studio, Inc.

2. **Start in test mode, not live.** Stripe gives every account a parallel
   test-mode key pair and a set of fake card numbers (4242 4242 4242 4242,
   any future expiry, any CVC) that never touch real money. Do the whole
   checklist below in test mode first.

3. **Get the secret key.** Dashboard → Developers → API keys → copy the
   **Secret key** (starts `sk_test_...` in test mode, `sk_live_...` once you
   switch). Set it as the `STRIPE_SECRET_KEY` environment variable on the
   `cic-poc` Render service.

4. **Register the webhook, then get its signing secret.** Dashboard →
   Developers → Webhooks → Add endpoint. URL:
   `https://<your-render-backend-domain>/api/support/webhook` (your real
   Render URL — not something I have). Select the `checkout.session.completed`
   event (that's the only one this app currently reads). Stripe shows a
   **Signing secret** (`whsec_...`) once the endpoint is created — set that as
   `STRIPE_WEBHOOK_SECRET` on Render, alongside the secret key from step 3.

5. **Confirm `CORS_ORIGINS` on the Render service includes
   `https://churchinconversation.com`** (and `.org` too, if it ever serves
   pages directly rather than only redirecting to `.com`). Without this, a
   real visitor's browser blocks every call from the Support page to the
   backend — this was likely already required for the app itself; it now
   also gates the giving flow specifically.

6. **Fill in the backend URL in the frontend.** Open
   `cic-website/support.html`, find `const API_BASE = "";` near the bottom,
   and set it to the same Render URL used in step 4 (e.g.
   `"https://cic-poc-xxxx.onrender.com"`). Left blank on purpose rather than
   guessed - every "Give" button fails gracefully to the existing email CTA
   until this is set, so the page is safe to deploy before this step is done.

7. **No product/price setup needed in the Stripe dashboard.** Unlike a typical
   Stripe integration, this one builds each checkout's price inline per
   request (so the "or whatever fits" custom amount works without a Price
   object per possible value) — there's nothing to pre-create.

8. **Test end to end, still in test mode:** click each amount button on the
   deployed Support page, pay with the 4242 test card, confirm it lands back
   on the page with the thank-you banner, and check Stripe Dashboard →
   Developers → Webhooks → your endpoint → for a successful (200) delivery.
   The Render service's own logs should show a `[giving_completed]` line
   (see Part D) for the same event.

9. **Only then switch to live keys** — replace `STRIPE_SECRET_KEY` with the
   `sk_live_...` key and repeat step 4 for a *live-mode* webhook endpoint
   (test and live webhooks are registered separately in Stripe; the signing
   secret is different for each), updating `STRIPE_WEBHOOK_SECRET` to match.

**Guardrail already built in, not something to configure:** the backend
rejects any amount outside $1–$10,000 per gift
(`cic-poc/backend/app/giving.py`, `MIN_AMOUNT_CENTS`/`MAX_AMOUNT_CENTS`) - a
safety floor/ceiling against a stray typed value, not a business decision.
Adjust there directly if it's ever wrong for a real case.

## Part D — What was actually built

- `cic-poc/backend/app/giving.py` — checkout-session creation (one-time and
  recurring, inline pricing) and webhook signature verification, both
  "off until configured" the same way `app/auth.py` is - `STRIPE_SECRET_KEY`
  unset means a clean `503`, not a crash, so this shipped before real keys
  existed.
- `cic-poc/backend/app/main.py` — `POST /api/support/checkout`,
  `POST /api/support/webhook`; an allowlist on the redirect URLs a checkout
  can send a browser to, since both are caller-supplied.
- `cic-poc/backend/app/config.py` — `stripe_secret_key`, `stripe_webhook_secret`
  settings, empty by default.
- `cic-poc/backend/requirements.txt` — added `stripe`.
- `cic-website/support.html` — the buttons, the copy from Part A, and the
  `API_BASE` constant from step 6 above. Restored to the header nav on every
  page (`about.html`, `atlas.html`, `index.html`, `pilot-feedback.html`,
  `support.html`, `tour.html`, `whats-next.html`).
- `cic-poc/backend/scripts/giving_flow_check.py` — 18/18 checks, no real
  Stripe account needed (a fake Stripe client stands in, the same pattern
  `scripts/redesign_battery.py` already uses): unconfigured 503s cleanly,
  the open-redirect guard, one-time vs. monthly session shape, amount-range
  validation, and webhook signature verification including a bad-signature
  case. Run it again any time this module changes:
  `python scripts/giving_flow_check.py`.
- A durable record of every completed gift: a `[giving_completed]` line in
  the backend's own logs (`cic.giving` logger, same pattern as
  `usage_logging.py`) - not a database, deliberately (see Part B).
