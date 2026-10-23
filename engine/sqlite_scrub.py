"""Makes a deletion leave the journal file too.

With the write-ahead log on, a deleted row's old page can sit in the log file until
a checkpoint folds it in. A truncating checkpoint empties the log, but it reports
busy while another connection is reading; this retries a few times and says
whether it worked, so a caller can log a failure instead of assuming success.
"""
import logging
import sqlite3
import time

logger = logging.getLogger("cic.api")

ATTEMPTS = 5
PAUSE_SECONDS = 0.05
JOURNAL_LIMIT_BYTES = 4 * 1024 * 1024


def truncate_wal(conn: sqlite3.Connection) -> bool:
    """True when the log was emptied."""
    conn.execute(f"PRAGMA journal_size_limit = {JOURNAL_LIMIT_BYTES}")
    for _ in range(ATTEMPTS):
        busy, _log, _checkpointed = conn.execute("PRAGMA wal_checkpoint(TRUNCATE)").fetchone()
        if not busy:
            return True
        time.sleep(PAUSE_SECONDS)
    logger.warning("a deletion could not empty its journal file; the next checkpoint will")
    return False
