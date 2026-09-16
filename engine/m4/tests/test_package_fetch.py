"""ensure_package_local's own three branches: already-local (no object
storage call at all), not-configured (falls through unchanged), and
fetch-then-cache. object_storage.download_package_dir is mocked - this
module's own job is the branching logic, not object storage's own
correctness (see test_object_storage.py for that)."""
from unittest.mock import patch

from engine.m4.package_fetch import ensure_package_local


def test_already_local_short_circuits_with_no_object_storage_call(tmp_path):
    package_dir = tmp_path / "packages" / "fix" / "pkg-1"
    package_dir.mkdir(parents=True)
    (package_dir / "manifest.json").write_text("{}")

    with patch("engine.m4.package_fetch.object_storage.is_configured") as mock_configured:
        result = ensure_package_local(package_dir=package_dir, cache_dir=tmp_path / "cache", key_prefix="packages/fix/pkg-1")

    mock_configured.assert_not_called()
    assert result == package_dir


def test_missing_and_unconfigured_returns_package_dir_unchanged(tmp_path):
    package_dir = tmp_path / "packages" / "fix" / "pkg-1"  # never created
    with patch("engine.m4.package_fetch.object_storage.is_configured", return_value=False):
        result = ensure_package_local(package_dir=package_dir, cache_dir=tmp_path / "cache", key_prefix="packages/fix/pkg-1")
    assert result == package_dir  # unchanged - load()'s own PackageRefused explains why, not this function


def test_missing_and_configured_fetches_into_cache_dir(tmp_path):
    package_dir = tmp_path / "packages" / "fix" / "pkg-1"  # never created locally
    cache_dir = tmp_path / "cache"

    def _fake_download(key_prefix, dest_dir):
        dest_dir.mkdir(parents=True, exist_ok=True)
        (dest_dir / "manifest.json").write_text("{}")
        return [f"{key_prefix}/manifest.json"]

    with patch("engine.m4.package_fetch.object_storage.is_configured", return_value=True), patch(
        "engine.m4.package_fetch.object_storage.download_package_dir", side_effect=_fake_download
    ) as mock_download:
        result = ensure_package_local(package_dir=package_dir, cache_dir=cache_dir, key_prefix="packages/fix/pkg-1")

    mock_download.assert_called_once_with("packages/fix/pkg-1", cache_dir / "packages/fix/pkg-1")
    assert result == cache_dir / "packages/fix/pkg-1"
    assert (result / "manifest.json").is_file()


def test_already_cached_from_an_earlier_fetch_skips_a_second_download(tmp_path):
    package_dir = tmp_path / "packages" / "fix" / "pkg-1"  # never created locally
    cache_dir = tmp_path / "cache"
    cached = cache_dir / "packages/fix/pkg-1"
    cached.mkdir(parents=True)
    (cached / "manifest.json").write_text("{}")  # already fetched by an earlier call

    with patch("engine.m4.package_fetch.object_storage.is_configured", return_value=True), patch(
        "engine.m4.package_fetch.object_storage.download_package_dir"
    ) as mock_download:
        result = ensure_package_local(package_dir=package_dir, cache_dir=cache_dir, key_prefix="packages/fix/pkg-1")

    mock_download.assert_not_called()
    assert result == cached
