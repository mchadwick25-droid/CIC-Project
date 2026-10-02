import urllib.parse

import pytest

from access_ledger import CheckoutError, create_checkout_session
from access_ledger.checkout import session_params


class FakeTransport:
    def __init__(self, status=200, payload=None):
        self.status = status
        self.payload = payload if payload is not None else {"id": "cs_test_1", "url": "https://checkout.stripe.com/c/pay/cs_test_1"}
        self.calls = []

    def __call__(self, method, url, headers, body):
        self.calls.append((method, url, headers, body))
        return self.status, self.payload


NAMES = {"pack_small": "5 conversations"}


def test_session_params_carry_visitor_pack_and_amount_from_the_catalogue(catalogue):
    params = session_params("v1", "pack_small", catalogue, NAMES, "https://x/ok", "https://x/cancel")
    assert params["mode"] == "payment"
    assert params["client_reference_id"] == "v1"
    assert params["metadata[sku]"] == "pack_small"
    assert params["line_items[0][price_data][unit_amount]"] == "1000"
    assert params["line_items[0][price_data][currency]"] == "usd"


def test_unknown_pack_is_refused(catalogue):
    with pytest.raises(CheckoutError):
        session_params("v1", "nope", catalogue, NAMES, "u", "c")


def test_create_session_posts_form_data_with_the_key_and_returns_the_hosted_url(catalogue):
    transport = FakeTransport()
    session = create_checkout_session("sk_test_x", "v1", "pack_small", catalogue, NAMES, "https://x/ok", "https://x/cancel", transport, idempotency_key="k1")
    method, url, headers, body = transport.calls[0]
    assert (method, url) == ("POST", "https://api.stripe.com/v1/checkout/sessions")
    assert headers["Authorization"] == "Bearer sk_test_x"
    assert headers["Idempotency-Key"] == "k1"
    assert urllib.parse.parse_qs(body)["client_reference_id"] == ["v1"]
    assert (session.session_id, session.url) == ("cs_test_1", "https://checkout.stripe.com/c/pay/cs_test_1")


def test_stripe_errors_surface_as_checkout_errors(catalogue):
    transport = FakeTransport(status=402, payload={"error": {"message": "Your card was declined."}})
    with pytest.raises(CheckoutError, match="declined"):
        create_checkout_session("sk_test_x", "v1", "pack_small", catalogue, NAMES, "u", "c", transport)
