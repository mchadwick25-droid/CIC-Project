"""Settings the module reads from the environment: where its two files go and
whether it is on. Numbers and wording are in the operations file, not here."""
import os
from dataclasses import dataclass

DEFAULT_GROUP_DAILY_CEILING = 300
METER_DB_NAME = "cic_deeper_meter.db"
CLAIMS_DB_NAME = "cic_deeper_claims.db"


@dataclass(frozen=True)
class DeeperConfig:
    enabled: bool
    meter_db_path: str
    claims_db_path: str

    @classmethod
    def from_env(cls, data_dir: str = ".") -> "DeeperConfig":
        """data_dir is where the two files go unless named: the caller passes
        the directory that already holds the event store, so they sit on the
        same backed-up disk."""
        return cls(
            enabled=os.environ.get("CIC_DEEPER_ENABLED", "") in ("1", "true", "yes"),
            meter_db_path=os.environ.get("CIC_DEEPER_METER_DB", os.path.join(data_dir, METER_DB_NAME)),
            claims_db_path=os.environ.get("CIC_DEEPER_CLAIMS_DB", os.path.join(data_dir, CLAIMS_DB_NAME)),
        )
