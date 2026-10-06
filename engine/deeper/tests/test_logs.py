import logging
import re
from datetime import date

from engine.deeper import codes
from engine.deeper.claims import ClaimStore
from engine.deeper.meter import Meter

CODE_SHAPED = re.compile(r"[2-9A-HJ-NP-Z]{20}")


def test_no_full_code_reaches_a_log_line(tmp_path, caplog):
    caplog.set_level(logging.DEBUG, logger="cic.deeper")
    meter = Meter(str(tmp_path / "m.db"), clock=lambda: date(2026, 10, 5))
    claims = ClaimStore(str(tmp_path / "c.db"))
    minted = meter.mint("batch", 3, "pi_log", count=2)
    claims.put("log-reference-12345", minted)
    for code in minted:
        admission = meter.reserve(code)
        meter.settle(admission.reservation, True)
        meter.verify(code)
        meter.status(code)
    meter.reserve(codes.generate())
    meter.pause(True)
    meter.pause(False)
    meter.void("pi_log")
    claims.get("log-reference-12345")
    meter.purge()
    claims.purge()
    text = "\n".join(r.getMessage() for r in caplog.records)
    assert text
    for code in minted:
        assert code not in text
        assert codes.display(code) not in text
        assert codes.hash_code(code) not in text
    assert CODE_SHAPED.search(text) is None
    assert "log-reference-12345" not in text
    meter.close()
    claims.close()
