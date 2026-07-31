"""Configuration settings for the CiC POC backend."""

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

from app.world_manifest import WORLD_MANIFEST


@dataclass
class WorldConfig:
    """Configuration for a specific world."""

    world_id: str
    name: str
    data_path: Path
    permanent_prompt_filename: str
    world_capsule_filename: str
    vector_store_name: str

    @property
    def permanent_prompt_path(self) -> Path:
        return self.data_path / self.permanent_prompt_filename

    @property
    def world_capsule_path(self) -> Path:
        return self.data_path / self.world_capsule_filename

    @property
    def lexicon_chunks_path(self) -> Path:
        return self.data_path / "lexicon_chunks"

    @property
    def story_chunks_path(self) -> Path:
        return self.data_path / "story_chunks"

    @property
    def source_registry_path(self) -> Path:
        return self.data_path / "source_registry.json"


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # LLM Configuration
    llm_provider: Literal["anthropic", "openai"] = "anthropic"
    llm_model: str = "claude-sonnet-5"
    # When true, every LLM call in the backend (representative/facilitator
    # generation, all classifiers, retrieval filtering) is replaced with a
    # zero-cost mock (see app/mock_llm.py) - no network call, no API spend.
    # For exercising the app's own mechanics (session flow, streaming,
    # multi-world turn-taking, the frontend) when API credits are
    # unavailable, not for validating conversation quality.
    mock_llm: bool = False

    # Server-side transcript capture for the tester pilot (see
    # app/transcript_logging.py). Off by default - only turn on for an
    # actual pilot deployment where testers have been told, in the
    # onboarding text, that their conversation is being cataloged. Never
    # enable this for a general/public deployment without that same
    # disclosure existing first.
    pilot_logging_enabled: bool = False

    # Per-tester session cap is controlled by the presence of
    # pilot_tester_codes.json (see app/session_cap.py), not a settings
    # field - the registry itself is the on/off switch and the per-tester
    # allocation, so there's nothing to duplicate here.

    # API Keys
    anthropic_api_key: str = ""
    openai_api_key: str = ""

    # Supabase (accounts, per-user activity/credit tracking - see
    # supabase_schema.sql and app/auth.py). Empty by default so local
    # dev/mock-mode work without a Supabase project; real values are set as
    # env vars once a project exists.
    supabase_url: str = ""
    supabase_service_key: str = ""

    # Stripe (SH-9: the voluntary contribution flow - see app/giving.py).
    # No accounts, no gating - a contribution never unlocks anything, so this
    # is deliberately independent of Supabase/auth.py entirely. Empty by
    # default, same "off until configured" discipline as Supabase above:
    # /api/support/checkout returns a clear 503 rather than failing, so cic-
    # website's Support page can go live before real Stripe keys exist.
    stripe_secret_key: str = ""
    # Only required to make /api/support/webhook verify signatures; without
    # it the endpoint 503s the same way checkout does. Set once the webhook
    # endpoint is registered in the Stripe dashboard (see the logistics doc).
    stripe_webhook_secret: str = ""

    # Base paths
    data_base_path: Path = Path("./data")
    vector_store_base_path: Path = Path("./vector_store")

    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    # Defaults to local dev only. Already overridable via the CORS_ORIGINS
    # env var (a JSON array string, e.g. '["https://your-domain.example"]')
    # - pydantic-settings parses list-typed fields from env vars natively,
    # no extra code needed. See .env.example. REQUIRED for any hosted
    # deployment: without it, every request from a real frontend domain is
    # blocked.
    cors_origins: list[str] = ["http://localhost:5173", "http://127.0.0.1:5173"]

    # World configurations - built from the single-source-of-truth manifest
    # (app/world_manifest.py) rather than hardcoded here.
    @property
    def worlds(self) -> dict[str, WorldConfig]:
        return {
            entry.world_id: WorldConfig(
                world_id=entry.world_id,
                name=entry.world_name,
                data_path=self.data_base_path / entry.data_dir_name,
                permanent_prompt_filename=entry.permanent_prompt_filename,
                world_capsule_filename=entry.world_capsule_filename,
                vector_store_name=entry.vector_store_name,
            )
            for entry in WORLD_MANIFEST
        }

    def get_world_config(self, world_id: str) -> WorldConfig:
        """Get configuration for a specific world."""
        if world_id not in self.worlds:
            raise ValueError(f"Unknown world: {world_id}")
        return self.worlds[world_id]

    def get_vector_store_path(self, world_id: str) -> Path:
        """Get lexicon vector store path for a specific world."""
        world_config = self.get_world_config(world_id)
        return self.vector_store_base_path / world_config.vector_store_name

    def get_story_vector_store_path(self, world_id: str) -> Path:
        """Get story vector store path for a specific world."""
        world_config = self.get_world_config(world_id)
        return self.vector_store_base_path / f"{world_config.vector_store_name}_stories"

    # Legacy properties for backwards compatibility (default to Syriac)
    @property
    def data_path(self) -> Path:
        return self.data_base_path / "syriac_world"

    @property
    def permanent_prompt_path(self) -> Path:
        return self.data_path / "syr_Representative_Permanent_Prompt_Yausep.txt"

    @property
    def world_capsule_path(self) -> Path:
        return self.data_path / "syr_World_Capsule_Core.md"

    @property
    def lexicon_chunks_path(self) -> Path:
        return self.data_path / "lexicon_chunks"

    @property
    def vector_store_path(self) -> Path:
        return self.vector_store_base_path / "syriac"


settings = Settings()
