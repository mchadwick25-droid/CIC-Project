"""SH-9: the voluntary contribution flow. Stripe Checkout, nothing gated.

Deliberately separate from app/auth.py and app/session_auth.py: a
contribution never unlocks anything and is never tied to a conversation
session, so it needs neither identity nor possession checks - anyone can
give, signed in or not, mid-conversation or having never opened the app at
all. This mirrors Part C.2 rung 1/2 of old-tree Ministry Funding/
CiC_Go_Live_Cost_Model_V0_1.md exactly: "No accounts, no Supabase, no
feature-gating - nothing in the app needs to change [to add this]."

Amounts are built as inline Stripe price_data per session rather than
pre-created Price objects in the dashboard - the "or whatever fits" custom
amount already promised in cic-website/support.html's copy would otherwise
need a Price object minted per custom value. This also means Mark's Stripe-
side setup is just an account and two API keys, not a product catalog - see
the logistics doc for the full checklist.

"Off until configured" discipline, matching app/auth.py's supabase_configured()
exactly: no STRIPE_SECRET_KEY means every call here returns cleanly rather
than raising, so cic-website's Support page can ship (buttons and all)
before Mark has created real Stripe keys - main.py's endpoints turn that
into a 503 the frontend already knows how to fall back on.
"""

import logging

from app.config import settings

logger = logging.getLogger("cic.giving")
logger.setLevel(logging.INFO)
if not logger.handlers:
    _handler = logging.StreamHandler()
    _handler.setFormatter(logging.Formatter("%(asctime)s %(message)s"))
    logger.addHandler(_handler)

# Stripe's own real floor for a USD charge (below this their API itself
# rejects the session). A gift can't cost more to process than it's worth,
# and there's no legitimate reason for a genuine gift to be a single cent.
MIN_AMOUNT_CENTS = 100
# Not a business ceiling - a sanity guard against a stray extra digit
# (typed cents instead of dollars, a client bug) reaching Stripe as a real
# charge attempt. A gift larger than this is real and should go through
# the direct, relational ask (info@churchinconversation.com), not this form.
MAX_AMOUNT_CENTS = 10_000_00


class GivingNotConfigured(Exception):
    """Raised by every function below when STRIPE_SECRET_KEY isn't set yet."""


class InvalidAmount(Exception):
    """Raised for an amount outside [MIN_AMOUNT_CENTS, MAX_AMOUNT_CENTS]."""


def stripe_configured() -> bool:
    return bool(settings.stripe_secret_key)


def _client():
    import stripe

    stripe.api_key = settings.stripe_secret_key
    return stripe


def create_checkout_session(
    mode: str, amount_cents: int, success_url: str, cancel_url: str
) -> str:
    """Create a Stripe Checkout Session for one gift and return its hosted URL.

    mode: "once" (a single payment) or "monthly" (a recurring subscription -
    Stripe handles all future billing itself; nothing in this app tracks who
    is subscribed, since nothing is gated by it). Any other value is a
    programming error, not a user error, and raises ValueError rather than
    being silently coerced.
    """
    if mode not in ("once", "monthly"):
        raise ValueError(f"giving mode must be 'once' or 'monthly', got {mode!r}")
    if not (MIN_AMOUNT_CENTS <= amount_cents <= MAX_AMOUNT_CENTS):
        raise InvalidAmount(
            f"amount_cents={amount_cents} outside [{MIN_AMOUNT_CENTS}, {MAX_AMOUNT_CENTS}]"
        )
    if not stripe_configured():
        raise GivingNotConfigured()

    stripe = _client()
    price_data = {
        "currency": "usd",
        "product_data": {
            "name": "Support Church in Conversation"
            + (" (monthly)" if mode == "monthly" else ""),
        },
        "unit_amount": amount_cents,
    }
    if mode == "monthly":
        price_data["recurring"] = {"interval": "month"}

    session = stripe.checkout.Session.create(
        mode="subscription" if mode == "monthly" else "payment",
        line_items=[{"price_data": price_data, "quantity": 1}],
        success_url=success_url,
        cancel_url=cancel_url,
        # Real name/email off a card isn't needed for anything downstream -
        # nothing here builds a donor record beyond the structured log line
        # below - but Stripe's own receipt email is the giver's proof of the
        # gift, so it's worth collecting even though this app never reads it.
        customer_creation="if_required" if mode == "once" else None,
    )
    logger.info(
        "[giving_checkout_created] mode=%s amount_cents=%d session_id=%s",
        mode, amount_cents, session.id,
    )
    return session.url


def verify_and_log_webhook(payload: bytes, sig_header: str | None) -> dict:
    """Verify a Stripe webhook's signature and, for a completed checkout,
    log the gift. Raises GivingNotConfigured / ValueError on bad input -
    main.py turns both into the right HTTP status.

    This is the only durable record a contribution leaves in this app: there
    is no donor database (see the module docstring on why none is built
    here). The structured [giving_completed] line is this flow's audit
    trail, parseable later the same way scripts/cost_baseline_runner.py
    already parses [llm_usage] lines, should anyone need to reconcile
    against Stripe's own dashboard.
    """
    if not stripe_configured() or not settings.stripe_webhook_secret:
        raise GivingNotConfigured()
    if not sig_header:
        raise ValueError("missing Stripe-Signature header")

    stripe = _client()
    event = stripe.Webhook.construct_event(
        payload, sig_header, settings.stripe_webhook_secret
    )

    if event["type"] == "checkout.session.completed":
        obj = event["data"]["object"]
        mode = "monthly" if obj.get("mode") == "subscription" else "once"
        amount = obj.get("amount_total")
        logger.info(
            "[giving_completed] mode=%s amount_cents=%s session_id=%s",
            mode, amount, obj.get("id"),
        )

    return event
