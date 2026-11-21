import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import check_open_gaps_numbers as c


def test_clean_log_with_gaps_passes():
    assert c.repeated("1. **a**\n2. **b**\n4. **c**\n") == []


def test_union_merge_duplicate_is_caught():
    assert c.repeated("3. **B** y\n4. **B** z\n3. **A** x\n") == [3]


def test_real_log_has_no_repeats():
    assert c.main([c.LOGS[0]]) == 0
