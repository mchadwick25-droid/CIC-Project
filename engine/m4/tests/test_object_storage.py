"""No live R2/AWS calls here - boto3.client itself is mocked, same
pattern engine/provider/tests/test_bedrock.py already uses for Bedrock.
R2 is not reachable from this sandbox at all, so
there is no live-path counterpart to preflight.py's own hand-run check -
the object-storage runbook's own "using it once set up" section is what
a human verifies against a real bucket."""
import os
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from engine.m4 import object_storage


def test_is_configured_false_when_bucket_unset(monkeypatch):
    monkeypatch.delenv("CIC_API_PACKAGE_BUCKET", raising=False)
    assert object_storage.is_configured() is False


def test_is_configured_true_when_bucket_set(monkeypatch):
    monkeypatch.setenv("CIC_API_PACKAGE_BUCKET", "cic-packages")
    assert object_storage.is_configured() is True


def test_client_refuses_without_endpoint(monkeypatch):
    monkeypatch.setenv("CIC_API_PACKAGE_BUCKET", "cic-packages")
    monkeypatch.delenv("CIC_API_PACKAGE_BUCKET_ENDPOINT", raising=False)
    with pytest.raises(object_storage.ObjectStorageError, match="ENDPOINT"):
        object_storage._client()


def test_client_refuses_without_credentials(monkeypatch):
    monkeypatch.setenv("CIC_API_PACKAGE_BUCKET", "cic-packages")
    monkeypatch.setenv("CIC_API_PACKAGE_BUCKET_ENDPOINT", "https://acct.r2.cloudflarestorage.com")
    monkeypatch.delenv("CIC_API_PACKAGE_BUCKET_ACCESS_KEY_ID", raising=False)
    monkeypatch.delenv("CIC_API_PACKAGE_BUCKET_SECRET_ACCESS_KEY", raising=False)
    with pytest.raises(object_storage.ObjectStorageError, match="access key"):
        object_storage._client()


def _configure_env(monkeypatch):
    monkeypatch.setenv("CIC_API_PACKAGE_BUCKET", "cic-packages")
    monkeypatch.setenv("CIC_API_PACKAGE_BUCKET_ENDPOINT", "https://acct.r2.cloudflarestorage.com")
    monkeypatch.setenv("CIC_API_PACKAGE_BUCKET_ACCESS_KEY_ID", "AKIA-fake")
    monkeypatch.setenv("CIC_API_PACKAGE_BUCKET_SECRET_ACCESS_KEY", "secret-fake")


def test_upload_package_dir_writes_every_file(tmp_path, monkeypatch):
    _configure_env(monkeypatch)
    local = tmp_path / "pkg"
    (local / "compiled").mkdir(parents=True)
    (local / "manifest.json").write_text("{}")
    (local / "compiled" / "prompt.txt").write_text("hi")

    mock_client = MagicMock()
    with patch("engine.m4.object_storage.boto3.client", return_value=mock_client):
        written = object_storage.upload_package_dir(local, "packages/fix/pkg-1")

    assert set(written) == {"packages/fix/pkg-1/manifest.json", "packages/fix/pkg-1/compiled/prompt.txt"}
    assert mock_client.upload_file.call_count == 2


def test_upload_failure_raises_object_storage_error(tmp_path, monkeypatch):
    _configure_env(monkeypatch)
    local = tmp_path / "pkg"
    local.mkdir()
    (local / "manifest.json").write_text("{}")

    mock_client = MagicMock()
    mock_client.upload_file.side_effect = RuntimeError("network blip")
    with patch("engine.m4.object_storage.boto3.client", return_value=mock_client):
        with pytest.raises(object_storage.ObjectStorageError, match="network blip"):
            object_storage.upload_package_dir(local, "packages/fix/pkg-1")


def test_download_package_dir_mirrors_structure(tmp_path, monkeypatch):
    _configure_env(monkeypatch)
    dest = tmp_path / "dest"

    mock_client = MagicMock()
    mock_paginator = MagicMock()
    mock_paginator.paginate.return_value = [
        {"Contents": [{"Key": "packages/fix/pkg-1/manifest.json"}, {"Key": "packages/fix/pkg-1/compiled/prompt.txt"}]}
    ]
    mock_client.get_paginator.return_value = mock_paginator

    def _fake_download(bucket, key, target):
        Path(target).write_text("fetched")

    mock_client.download_file.side_effect = _fake_download
    with patch("engine.m4.object_storage.boto3.client", return_value=mock_client):
        fetched = object_storage.download_package_dir("packages/fix/pkg-1", dest)

    assert len(fetched) == 2
    assert (dest / "manifest.json").read_text() == "fetched"
    assert (dest / "compiled" / "prompt.txt").read_text() == "fetched"


def test_download_of_empty_prefix_raises(tmp_path, monkeypatch):
    _configure_env(monkeypatch)
    mock_client = MagicMock()
    mock_paginator = MagicMock()
    mock_paginator.paginate.return_value = [{"Contents": []}]
    mock_client.get_paginator.return_value = mock_paginator
    with patch("engine.m4.object_storage.boto3.client", return_value=mock_client):
        with pytest.raises(object_storage.ObjectStorageError, match="no objects found"):
            object_storage.download_package_dir("packages/nowhere/pkg-1", tmp_path / "dest")
