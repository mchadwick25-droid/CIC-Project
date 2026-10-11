from engine.provider.list_profiles import build_report, global_counterparts

IDS = [
    "us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    "global.anthropic.claude-sonnet-4-5-20250929-v1:0",
    "us.anthropic.claude-haiku-4-5-20251001-v1:0",
]


def test_global_counterpart_found_where_it_exists_and_not_where_it_does_not():
    assert global_counterparts(IDS, "us.anthropic.claude-sonnet-4-5") == ["global.anthropic.claude-sonnet-4-5-20250929-v1:0"]
    assert global_counterparts(IDS, "us.anthropic.claude-haiku-4-5") == []


def test_report_names_every_global_profile():
    report = build_report(IDS, "us-east-1", {"voice": "us.anthropic.claude-sonnet-4-5"})
    assert report["global_profiles"] == ["global.anthropic.claude-sonnet-4-5-20250929-v1:0"]
    assert report["patterns"]["voice"]["global_counterparts"] == report["global_profiles"]
