"""The runtime's ONE seam to the clean engine.

Every place the serving app consumes something the engine owns - guard
exports, the alias frequency table, the operational parameters, the
gloss data - goes through this module, so the full engine surface the
runtime depends on is readable in one place. The old tree reached into
its build system from six different files; the clean system does it
here, once.
"""
import sys
from pathlib import Path

_CIC = Path(__file__).resolve().parents[2]  # cic/
ENGINE = _CIC / "engine"
RECORDS = _CIC / "records"
DEPLOY = _CIC / "deploy"

if str(ENGINE) not in sys.path:
    sys.path.insert(0, str(ENGINE))

PARAMETERS_PATH = ENGINE / "parameters.yaml"
GLOSSES_PATH = ENGINE / "confirmed_glosses.yaml"

from segments.guards import post_history_guard_for  # noqa: E402,F401
from gates import _alias_freq_table  # noqa: E402,F401
from worlds import WORLDS  # noqa: E402,F401
