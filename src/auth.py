"""
Auth scaffold for Mergington High School API

This file provides a minimal, dependency-free scaffold for JWT-based
authentication. It intentionally contains placeholders so we can add
real JWT logic later without breaking CI.
"""
from typing import Optional


def verify_token(token: str) -> bool:
    """Placeholder token verifier — replace with real JWT verification."""
    return False


def get_current_user(token: str) -> Optional[str]:
    """Return the username for a valid token, otherwise None."""
    if verify_token(token):
        return "student@example.com"
    return None
