import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_token_and_protected_endpoints():
    # Authenticate with the fake user in FAKE_DB
    resp = client.post("/token", data={"username": "alice@example.com", "password": "password123"})
    assert resp.status_code == 200
    body = resp.json()
    assert "access_token" in body
    token = body["access_token"]

    # Use token to signup
    headers = {"Authorization": f"Bearer {token}"}
    resp = client.post("/activities/Chess Club/signup?email=test2@example.com", headers=headers)
    assert resp.status_code == 200
    assert "timestamp" in resp.json()

    # Unregister
    resp = client.delete("/activities/Chess Club/unregister?email=test2@example.com", headers=headers)
    assert resp.status_code == 200
    assert "timestamp" in resp.json()
