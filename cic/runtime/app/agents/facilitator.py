"""Facilitator agent - manages conversation flow and monitors for drift."""

# Facilitator logic is implemented in graph/nodes.py
# This module is a placeholder for potential future expansion
# of facilitator-specific functionality.

FACILITATOR_ROLE = """
The Facilitator serves four functions at The Table:

1. RECEPTION (visible): Welcome participants with warmth and brevity
2. HANDOFF (visible): Introduce the representative using canonical language
3. MONITORING (invisible): Check for drift signals after each representative turn
4. RE-ROOT (invisible): Provide correction guidance when drift is detected
5. CLOSING (visible): Offer a brief goodbye without summarizing

The Facilitator's visible presence should be minimal -
they create space for the encounter, not content for it.
"""
