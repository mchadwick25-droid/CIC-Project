#!/usr/bin/env python
"""SH-9 verification: the voluntary contribution flow (app/giving.py +
/api/support/checkout, /api/support/webhook in main.py).

No real Stripe account or network call needed - app.giving._client() is
monkeypatched with a fake stripe module, the same pattern used throughout
this repo (see redesign_battery.py) for exercising real code without live
external dependencies.

  python scripts/giving_flow_check.py
"""

import os
import sys
from pathlib import Path
from types import SimpleNamespace

os.environ.setdefault("MOCK_LLM", "true")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f" - {detail}" if detail else ""))


def section(title: str) -> None:
    print(f"\n{title}\n{'-' * len(title)}")


# ---------------------------------------------------------------------------
section("A. unconfigured - every entry point 503s cleanly, no crash")
# ---------------------------------------------------------------------------
from app.config import settings  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

import app.main as main_mod  # noqa: E402

settings.stripe_secret_key = ""
settings.stripe_webhook_secret = ""
client = TestClient(main_mod.app)

r = client.post("/api/support/checkout", json={
    "mode": "once", "amount_cents": 1000,
    "success_url": "https://churchinconversation.com/thanks",
    "cancel_url": "https://churchinconversation.com/support.html",
})
check("checkout unconfigured -> 503", r.status_code == 503, f"HTTP {r.status_code}")

r = client.post("/api/support/webhook", content=b"{}", headers={"stripe-signature": "x"})
check("webhook unconfigured -> 503", r.status_code == 503, f"HTTP {r.status_code}")

# ---------------------------------------------------------------------------
section("B. input validation - runs even before Stripe is reachable")
# ---------------------------------------------------------------------------
r = client.post("/api/support/checkout", json={
    "mode": "once", "amount_cents": 1000,
    "success_url": "https://evil.example.com/steal",
    "cancel_url": "https://churchinconversation.com/support.html",
})
check("non-allowlisted success_url -> 400 (open-redirect guard)",
      r.status_code == 400, f"HTTP {r.status_code}")

r = client.post("/api/support/checkout", json={
    "mode": "once", "amount_cents": 1000,
    "success_url": "https://churchinconversation.com/thanks",
    "cancel_url": "https://churchinconversation.com/support.html",
})
check("still unconfigured (503, not 400) once URLs are valid",
      r.status_code == 503, f"HTTP {r.status_code}")

# ---------------------------------------------------------------------------
section("C. configured - checkout session creation, no real network call")
# ---------------------------------------------------------------------------
from app import giving as giving_mod  # noqa: E402

settings.stripe_secret_key = "sk_test_fake"
settings.stripe_webhook_secret = "whsec_fake"

created_sessions = []


class _FakeCheckoutSession:
    def __init__(self, **kwargs):
        self.id = "cs_test_123"
        self.url = "https://checkout.stripe.com/pay/cs_test_123"
        created_sessions.append(kwargs)


class _FakeStripe:
    class checkout:
        class Session:
            @staticmethod
            def create(**kwargs):
                return _FakeCheckoutSession(**kwargs)

    class Webhook:
        @staticmethod
        def construct_event(payload, sig_header, secret):
            import json
            return json.loads(payload)

    class error:
        class SignatureVerificationError(Exception):
            pass


giving_mod._client = lambda: _FakeStripe

r = client.post("/api/support/checkout", json={
    "mode": "once", "amount_cents": 1000,
    "success_url": "https://churchinconversation.com/thanks",
    "cancel_url": "https://churchinconversation.com/support.html",
})
check("configured one-time checkout -> 200 with a url", r.status_code == 200 and "url" in r.json(),
      f"HTTP {r.status_code} body={r.json() if r.status_code == 200 else r.text}")
check("one-time session created in 'payment' mode",
      created_sessions and created_sessions[-1]["mode"] == "payment")
check("one-time price_data carries no 'recurring' key",
      "recurring" not in created_sessions[-1]["line_items"][0]["price_data"])

r = client.post("/api/support/checkout", json={
    "mode": "monthly", "amount_cents": 800,
    "success_url": "https://churchinconversation.com/thanks",
    "cancel_url": "https://churchinconversation.com/support.html",
})
check("configured monthly checkout -> 200 with a url", r.status_code == 200 and "url" in r.json())
check("monthly session created in 'subscription' mode",
      created_sessions[-1]["mode"] == "subscription")
check("monthly price_data carries recurring.interval=month",
      created_sessions[-1]["line_items"][0]["price_data"].get("recurring") == {"interval": "month"})
check("monthly unit_amount matches the request (800 cents = $8)",
      created_sessions[-1]["line_items"][0]["price_data"]["unit_amount"] == 800)

r = client.post("/api/support/checkout", json={
    "mode": "bogus", "amount_cents": 1000,
    "success_url": "https://churchinconversation.com/thanks",
    "cancel_url": "https://churchinconversation.com/support.html",
})
check("invalid mode -> 400", r.status_code == 400, f"HTTP {r.status_code}")

r = client.post("/api/support/checkout", json={
    "mode": "once", "amount_cents": 1,
    "success_url": "https://churchinconversation.com/thanks",
    "cancel_url": "https://churchinconversation.com/support.html",
})
check("amount below MIN_AMOUNT_CENTS -> 400", r.status_code == 400, f"HTTP {r.status_code}")

r = client.post("/api/support/checkout", json={
    "mode": "once", "amount_cents": 99_999_999,
    "success_url": "https://churchinconversation.com/thanks",
    "cancel_url": "https://churchinconversation.com/support.html",
})
check("amount above MAX_AMOUNT_CENTS -> 400", r.status_code == 400, f"HTTP {r.status_code}")

# ---------------------------------------------------------------------------
section("D. webhook - signature verification and structured logging")
# ---------------------------------------------------------------------------
import io  # noqa: E402
import json  # noqa: E402
import logging  # noqa: E402

buf = io.StringIO()
h = logging.StreamHandler(buf)
h.setFormatter(logging.Formatter("%(message)s"))
giving_mod.logger.addHandler(h)

completed_event = json.dumps({
    "type": "checkout.session.completed",
    "data": {"object": {"id": "cs_test_123", "mode": "payment", "amount_total": 1000}},
}).encode()
r = client.post("/api/support/webhook", content=completed_event,
                 headers={"stripe-signature": "sig"})
check("valid webhook event -> 200", r.status_code == 200, f"HTTP {r.status_code}")
check("checkout.session.completed logs a [giving_completed] line",
      "[giving_completed]" in buf.getvalue() and "amount_cents=1000" in buf.getvalue())


def _raise(*a, **kw):
    raise _FakeStripe.error.SignatureVerificationError("bad sig")


giving_mod._client = lambda: SimpleNamespace(
    Webhook=SimpleNamespace(construct_event=_raise),
    error=_FakeStripe.error,
)
r = client.post("/api/support/webhook", content=b"{}", headers={"stripe-signature": "bad"})
check("bad signature -> 400, not 500", r.status_code == 400, f"HTTP {r.status_code}")

r = client.post("/api/support/webhook", content=b"{}", headers={})
check("missing stripe-signature header -> 400", r.status_code == 400, f"HTTP {r.status_code}")

# ---------------------------------------------------------------------------
n_pass = sum(1 for _, p, _ in RESULTS if p)
print(f"\n{'=' * 72}\nRESULT: {n_pass}/{len(RESULTS)} checks passed\n{'=' * 72}")
sys.exit(0 if n_pass == len(RESULTS) else 1)
