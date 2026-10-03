"""Settings the module reads from the environment. Every number here is a
parameter the project lead sets; the defaults are safe, not decided."""
import os
from dataclasses import dataclass

DEFAULT_METER_DB = "./cic_deeper_meter.db"
DEFAULT_CLAIMS_DB = "./cic_deeper_claims.db"
DEFAULT_GROUP_DAILY_CEILING = 300


@dataclass(frozen=True)
class DeeperConfig:
    enabled: bool
    meter_db_path: str
    claims_db_path: str
    group_daily_ceiling: int

    @classmethod
    def from_env(cls) -> "DeeperConfig":
        return cls(
            enabled=os.environ.get("CIC_DEEPER_ENABLED", "") in ("1", "true", "yes"),
            meter_db_path=os.environ.get("CIC_DEEPER_METER_DB", DEFAULT_METER_DB),
            claims_db_path=os.environ.get("CIC_DEEPER_CLAIMS_DB", DEFAULT_CLAIMS_DB),
            group_daily_ceiling=int(os.environ.get("CIC_DEEPER_GROUP_DAILY_CEILING", DEFAULT_GROUP_DAILY_CEILING)),
        )
