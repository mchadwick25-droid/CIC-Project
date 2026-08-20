""""Anachronism is computed per world from its time window; the dictionary
is fleet data, owned once" (spec M5). No world identifier in code (law 4) -
this takes the world's time_window and the fleet's modern_term records as
plain data and computes membership; it has no idea which world it's
running for.
"""


def anachronistic_term_ids(modern_terms: dict[str, dict], world_time_window: dict) -> set[str]:
    """A modern term is anachronistic for a world if the term's own
    origin_year postdates the world's window (the term did not yet exist
    when this world's Representative would be speaking)."""
    end = world_time_window["end"]
    return {
        term["id"]
        for term in modern_terms.values()
        if term.get("record_type") == "modern_term" and term.get("origin_year") is not None and term["origin_year"] > end
    }
