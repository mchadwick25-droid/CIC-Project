from access_ledger import AccessService, apply_event
from tests.test_stripe_events import session_event


def test_new_visitor_gets_three_free_conversations_of_three_turns(conn):
    svc = AccessService(conn)
    first = svc.start_conversation("v1", "s1")
    assert (first.admitted, first.bucket, first.turn_cap) == (True, "free", 3)
    assert svc.balance("v1").free == 2


def test_the_free_allowance_is_granted_once_per_visitor(conn):
    svc = AccessService(conn)
    svc.start_conversation("v1", "s1")
    svc.first_reply_stored("s1")
    svc.start_conversation("v1", "s2")
    svc.first_reply_stored("s2")
    svc.start_conversation("v1", "s3")
    svc.first_reply_stored("s3")
    assert svc.start_conversation("v1", "s4").reason == "no_balance"
    assert svc.balance("v1").total == 0


def test_a_paid_conversation_has_a_seven_turn_cap(conn, catalogue):
    svc = AccessService(conn)
    for i in range(3):
        svc.start_conversation("v1", f"f{i}")
        svc.first_reply_stored(f"f{i}")
    apply_event(conn, session_event(), catalogue)
    started = svc.start_conversation("v1", "paid1")
    assert (started.admitted, started.bucket, started.turn_cap) == (True, "paid", 7)


def test_a_failed_conversation_returns_the_unit(conn):
    svc = AccessService(conn)
    svc.start_conversation("v1", "s1")
    assert svc.balance("v1").free == 2
    svc.conversation_failed("s1")
    assert svc.balance("v1").free == 3


def test_no_balance_is_an_answer_the_caller_can_route_on(conn):
    svc = AccessService(conn, free_conversations=1)
    svc.start_conversation("v1", "s1")
    svc.first_reply_stored("s1")
    refused = svc.start_conversation("v1", "s2")
    assert (refused.admitted, refused.bucket, refused.turn_cap, refused.reason) == (False, None, None, "no_balance")


def test_a_second_visitor_has_a_separate_allowance(conn):
    svc = AccessService(conn)
    svc.start_conversation("v1", "s1")
    assert svc.balance("v2").total == 0
    svc.start_conversation("v2", "s2")
    assert svc.balance("v2").free == 2
