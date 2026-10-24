"""The SES mailer sends one plain-text message per call and leaks nothing. The words in these tests are
test words, written here so the code can be exercised; the live words come from the approved file."""
import logging
from datetime import date

import pytest

from engine.api import accounts_routes, ses_mailer
from engine.api.ses_mailer import MailConfigError, MailSendError, MailWords, SesMailer

WORDS = {
    "code": {"subject": "test subject", "body": "test code {code}"},
    "notices": {
        "recovery_started": {"subject": "test notice", "body": "test cancel {cancel_code} on {effective_on}"},
    },
}
DAY = date(2026, 11, 2)
ADDRESS = "reader@example.org"
CODE = "482913"


class FakeSes:
    def __init__(self, fail=None):
        self.calls = []
        self.fail = fail

    def send_email(self, **kwargs):
        if self.fail:
            raise self.fail
        self.calls.append(kwargs)


def mailer(client=None):
    return SesMailer(client or FakeSes(), "CiC <accounts@example.org>", MailWords.from_data(WORDS))


def test_a_code_goes_out_as_one_plain_text_message_to_one_address():
    client = FakeSes()
    mailer(client).send_code(ADDRESS, CODE)
    (call,) = client.calls
    assert call["Destination"] == {"ToAddresses": [ADDRESS]}
    assert call["FromEmailAddress"] == "CiC <accounts@example.org>"
    simple = call["Content"]["Simple"]
    assert simple["Subject"]["Data"] == "test subject"
    assert simple["Body"]["Text"]["Data"] == f"test code {CODE}"
    assert "Html" not in simple["Body"]
    assert "ConfigurationSetName" not in call  # no tracking, no event destination


def test_a_notice_fills_only_its_own_fields():
    client = FakeSes()
    mailer(client).send_notice(ADDRESS, "recovery_started", {"cancel_code": "abc", "effective_on": DAY.isoformat(), "extra": "x"})
    assert client.calls[0]["Content"]["Simple"]["Body"]["Text"]["Data"] == "test cancel abc on 2 November 2026"


def test_an_unknown_notice_is_refused():
    with pytest.raises(MailSendError):
        mailer().send_notice(ADDRESS, "surprise", {})


@pytest.mark.parametrize("bad", ["a@b.org\r\nBcc: x@y.org", "a@b.org, c@d.org", "no-at-sign", "", "a b@c.org"])
def test_an_address_that_could_add_a_header_or_a_second_recipient_is_not_sent(bad):
    client = FakeSes()
    with pytest.raises(MailSendError):
        mailer(client).send_code(bad, CODE)
    assert client.calls == []


def test_a_provider_fault_reaches_the_caller_without_the_address_the_code_or_the_provider_text(caplog):
    boom = RuntimeError(f"cannot send to {ADDRESS} with {CODE}")
    with caplog.at_level(logging.DEBUG):
        with pytest.raises(MailSendError) as caught:
            mailer(FakeSes(fail=boom)).send_code(ADDRESS, CODE)
    assert ADDRESS not in str(caught.value) and CODE not in str(caught.value)
    assert caught.value.__cause__ is None and caught.value.__suppress_context__
    assert ADDRESS not in caplog.text and CODE not in caplog.text


def test_the_queued_path_logs_a_failed_send_without_the_address_or_code(caplog):
    queued = accounts_routes.QueuedMailer(mailer(FakeSes(fail=RuntimeError(f"{ADDRESS} {CODE}"))))
    with caplog.at_level(logging.DEBUG):
        queued._send(ADDRESS, CODE)
    assert ADDRESS not in caplog.text and CODE not in caplog.text


@pytest.mark.parametrize("sender", ["", "no-at", "a@b.org\nBcc: c@d.org", "x <a@b.org>\r\n"])
def test_a_bad_sender_is_refused_at_start(sender):
    with pytest.raises(MailConfigError):
        SesMailer(FakeSes(), sender, MailWords.from_data(WORDS))


def test_words_must_use_the_code_and_only_fields_that_are_sent():
    without_code = {**WORDS, "code": {"subject": "s", "body": "no code here"}}
    with pytest.raises(MailConfigError):
        MailWords.from_data(without_code)
    stray = {**WORDS, "code": {"subject": "s", "body": "{code} {address}"}}
    with pytest.raises(MailConfigError):
        MailWords.from_data(stray)
    brace = {**WORDS, "code": {"subject": "s", "body": "{code} }"}}
    with pytest.raises(MailConfigError):
        MailWords.from_data(brace)
    multiline = {**WORDS, "code": {"subject": "s\nBcc: x", "body": "{code}"}}
    with pytest.raises(MailConfigError):
        MailWords.from_data(multiline)


def test_every_notice_the_service_sends_needs_words():
    missing = {"code": WORDS["code"], "notices": {}}
    with pytest.raises(MailConfigError):
        MailWords.from_data(missing)
    with pytest.raises(MailConfigError):
        MailWords.from_data({"code": WORDS["code"], "notices": {**WORDS["notices"], "invented": WORDS["code"]}})


def test_no_words_file_means_no_start(tmp_path):
    env = {
        ses_mailer.ENV_FROM: "accounts@example.org", ses_mailer.ENV_REGION: "us-east-1",
        ses_mailer.ENV_ACCESS_KEY: "k", ses_mailer.ENV_SECRET_KEY: "s",
        ses_mailer.ENV_WORDS: str(tmp_path / "absent.yaml"),
    }
    with pytest.raises(MailConfigError, match="missing"):
        ses_mailer.from_env(env)


def test_no_ses_settings_means_no_mailer_and_partial_settings_are_a_mistake():
    assert ses_mailer.from_env({}) is None
    with pytest.raises(MailConfigError, match="partly set"):
        ses_mailer.from_env({ses_mailer.ENV_FROM: "accounts@example.org"})



def test_a_day_is_written_the_way_the_screens_write_it():
    assert ses_mailer.day_in_words(DAY.isoformat()) == "2 November 2026"
    assert ses_mailer.day_in_words(date(2027, 1, 31).isoformat()) == "31 January 2027"
    assert ses_mailer.day_in_words("soon") == "soon"


def test_the_approved_words_file_loads_and_says_what_mark_approved():
    words = MailWords.from_file(ses_mailer.DEFAULT_WORDS_PATH)
    client = FakeSes()
    mail = SesMailer(client, "accounts@example.org", words)
    mail.send_code(ADDRESS, CODE)
    mail.send_notice(ADDRESS, "recovery_started", {"cancel_code": "CANCEL", "effective_on": DAY.isoformat()})
    code_mail, notice_mail = (c["Content"]["Simple"] for c in client.calls)
    assert code_mail["Subject"]["Data"] == "Your sign-in code"
    assert code_mail["Body"]["Text"]["Data"] == (
        f"Your code is {CODE}. It works for ten minutes.\n\nIf you did not ask for it, ignore this email."
    )
    assert notice_mail["Subject"]["Data"] == "Someone is moving your account"
    assert notice_mail["Body"]["Text"]["Data"] == (
        "Someone started moving your account to a new email address.\n\n"
        "If this was you, do nothing. The move happens on 2 November 2026.\n\n"
        "If this was not you, sign in with this address and press Stop the recovery.\n\n"
        "Cannot sign in? Your cancel code is CANCEL. Use it on the sign-in page, under “I cannot get to my email”."
    )
