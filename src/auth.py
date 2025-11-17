"""JWT-based auth helpers.

This implements a minimal JWT token creation and verification using
`python-jose`. It's intentionally small so tests and CI remain quick.
Replace the `FAKE_DB` with a real database and secure the `SECRET_KEY`
via environment variables in production.
"""
from datetime import datetime, timedelta
from typing import Optional

from jose import JWTError, jwt
from passlib.context import CryptContext

# NOTE: In a real deployment keep this secret in env vars / secret manager
SECRET_KEY = "dev-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

# Minimal in-memory user store for demo/testing purposes
FAKE_DB = {
    "alice@example.com": {
        "username": "alice@example.com",
        # password: "password123" (hashed)
        "hashed_password": pwd_context.hash("password123")
    }
}


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(username: str, password: str) -> Optional[str]:
    user = FAKE_DB.get(username)
    if not user:
        return None
    if not verify_password(password, user["hashed_password"]):
        return None
    return username


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


def get_current_user_from_token(token: str) -> Optional[str]:
    payload = decode_access_token(token)
    if not payload:
        return None
    username = payload.get("sub")
    return username
