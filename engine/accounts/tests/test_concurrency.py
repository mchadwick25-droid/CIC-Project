import threading

from engine.accounts.tests.conftest import sign_in

ADDR = "ada@example.org"
NET = "203.0.113.5"


def _race(count, work):
    barrier = threading.Barrier(count)
    results = [None] * count

    def run(i):
        barrier.wait()
        results[i] = work(i)

    threads = [threading.Thread(target=run, args=(i,)) for i in range(count)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return results


def test_concurrent_wrong_guesses_cannot_beat_the_try_limit(svc, mailer, store):
    challenge = svc.start_sign_in(ADDR, NET).challenge
    right = mailer.last_code(ADDR)
    wrong = "000000" if right != "000000" else "111111"
    counted = []
    real = store.take_try

    def counting(*args, **kwargs):
        row = real(*args, **kwargs)
        if row is not None:
            counted.append(row.tries)
        return row

    store.take_try = counting
    results = _race(30, lambda i: svc.finish_sign_in(challenge, ADDR, wrong, f"198.51.100.{i}", "1990-05-15").status)
    assert set(results) == {"wrong"}
    assert len(counted) <= svc.limits.code_tries
    assert svc.finish_sign_in(challenge, ADDR, right, NET, "1990-05-15").status == "wrong"  # the code was burned


def test_two_simultaneous_right_codes_open_exactly_one_session(svc, mailer, store):
    challenge = svc.start_sign_in(ADDR, NET).challenge
    right = mailer.last_code(ADDR)
    results = _race(4, lambda i: svc.finish_sign_in(challenge, ADDR, right, f"198.51.100.{i}", "1990-05-15").status)
    assert results.count("ok") == 1
    assert store._e.execute("SELECT COUNT(*) FROM sessions").fetchone()[0] == 1
    assert store._d.execute("SELECT COUNT(*) FROM accounts").fetchone()[0] == 1
