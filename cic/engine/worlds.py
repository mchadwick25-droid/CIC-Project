"""The world table - the ONLY per-world configuration in the clean engine.

One row per world: identity, record-store directory, core record ids, and
the rebuilt flag (readability enforcement). Everything else per-world is a
RECORD (craft table included). A world is added to the clean system by
adding its row here and its records under cic/records/<key>/ - no new code.
"""

WORLDS = {
    "syriac": {
        "world_id": "syriac-edessa-nisibis",
        "records_dir": "syriac",
        "world_core_id": "syrcore001",
        "voice_profile_id": "syrvoice001",
        "craft_id": "syrcraft001",
        "prompt_filename": "syr_Representative_Permanent_Prompt_Yausep.txt",
        "capsule_filename": "syr_World_Capsule_Core.md",
        "capsule_display_name": "Syriac",
        "world_code": "syr",
        "rebuilt": True,
    },
}
