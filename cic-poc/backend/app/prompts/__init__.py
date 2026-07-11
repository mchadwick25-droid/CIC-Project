"""Prompts for facilitator and representative agents."""

from app.prompts.facilitator_prompts import (
    FACILITATOR_CLOSING_PROMPT,
    FACILITATOR_HANDOFF_PROMPT,
    FACILITATOR_MONITORING_PROMPT,
    FACILITATOR_RECEPTION_PROMPT,
    FACILITATOR_REROOT_PROMPT,
)
from app.prompts.representative_prompts import build_representative_prompt

__all__ = [
    "FACILITATOR_RECEPTION_PROMPT",
    "FACILITATOR_HANDOFF_PROMPT",
    "FACILITATOR_MONITORING_PROMPT",
    "FACILITATOR_REROOT_PROMPT",
    "FACILITATOR_CLOSING_PROMPT",
    "build_representative_prompt",
]
