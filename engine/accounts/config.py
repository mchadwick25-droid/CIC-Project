"""Settings the module reads from the environment: where its two files go and
whether it is on. Keys are read by the edge and handed to the key ring."""
import os
from dataclasses import dataclass

DURABLE_DB_NAME = "cic_accounts.db"
EPHEMERAL_DB_NAME = "cic_accounts_ephemeral.db"


@dataclass(frozen=True)
class AccountsConfig:
    enabled: bool
    durable_db_path: str
    ephemeral_db_path: str

    @classmethod
    def from_env(cls, data_dir: str = ".") -> "AccountsConfig":
        """data_dir is the directory that already holds the event store, so the
        durable file sits on the same backed-up disk."""
        return cls(
            enabled=os.environ.get("CIC_ACCOUNTS_ENABLED", "") in ("1", "true", "yes"),
            durable_db_path=os.environ.get("CIC_ACCOUNTS_DB", os.path.join(data_dir, DURABLE_DB_NAME)),
            ephemeral_db_path=os.environ.get("CIC_ACCOUNTS_EPHEMERAL_DB", os.path.join(data_dir, EPHEMERAL_DB_NAME)),
        )
