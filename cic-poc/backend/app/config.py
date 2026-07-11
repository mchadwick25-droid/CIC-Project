"""Configuration settings for the CiC POC backend."""

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


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

    # API Keys
    anthropic_api_key: str = ""
    openai_api_key: str = ""

    # Base paths
    data_base_path: Path = Path("./data")
    vector_store_base_path: Path = Path("./vector_store")

    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    cors_origins: list[str] = ["http://localhost:5173", "http://127.0.0.1:5173"]

    # World configurations
    @property
    def worlds(self) -> dict[str, WorldConfig]:
        return {
            "syriac-edessa-nisibis": WorldConfig(
                world_id="syriac-edessa-nisibis",
                name="Syriac Christianity",
                data_path=self.data_base_path / "syriac_world",
                permanent_prompt_filename="syr_Representative_Permanent_Prompt_Yausep.txt",
                world_capsule_filename="syr_World_Capsule_Core.md",
                vector_store_name="syriac",
            ),
            "post-apostolic-house-church": WorldConfig(
                world_id="post-apostolic-house-church",
                name="Post-Apostolic House-Church",
                data_path=self.data_base_path / "pahc_world",
                permanent_prompt_filename="pahc_Representative_Permanent_Prompt_Amma.txt",
                world_capsule_filename="pahc_World_Capsule_Core.md",
                vector_store_name="pahc",
            ),
        }

    def get_world_config(self, world_id: str) -> WorldConfig:
        """Get configuration for a specific world."""
        if world_id not in self.worlds:
            raise ValueError(f"Unknown world: {world_id}")
        return self.worlds[world_id]

    def get_vector_store_path(self, world_id: str) -> Path:
        """Get vector store path for a specific world."""
        world_config = self.get_world_config(world_id)
        return self.vector_store_base_path / world_config.vector_store_name

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
