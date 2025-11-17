import os
import sys
import pytest

# Ensure repo root is on PYTHONPATH so `src` package can be imported during tests
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from fastapi.testclient import TestClient
from src.app import app
from datetime import datetime


@pytest.fixture
def client():
    return TestClient(app)


def test_get_activities(client):
    resp = client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    # Expect some known activity keys from seed data
    assert "Chess Club" in data


def test_signup_and_unregister_flow(client):
    activity = "Chess Club"
    email = "test-student@example.com"

    # Obtain auth token for demo user and use it for protected endpoints
    token_resp = client.post("/token", data={"username": "alice@example.com", "password": "password123"})
    assert token_resp.status_code == 200
    token = token_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Ensure signup works (authenticated)
    resp = client.post(f"/activities/{activity}/signup?email={email}", headers=headers)
    assert resp.status_code == 200
    body = resp.json()
    assert f"Signed up {email}" in body.get("message", "")
    # Timestamp should be present and ISO-8601 parseable
    assert "timestamp" in body
    datetime.fromisoformat(body["timestamp"])

    # Signing up again should return 400 (already signed up)
    resp = client.post(f"/activities/{activity}/signup?email={email}", headers=headers)
    assert resp.status_code == 400

    # Unregister
    resp = client.delete(f"/activities/{activity}/unregister?email={email}", headers=headers)
    assert resp.status_code == 200
    body = resp.json()
    assert f"Unregistered {email}" in body.get("message", "")
    # Timestamp should be present and ISO-8601 parseable
    assert "timestamp" in body
    datetime.fromisoformat(body["timestamp"])
