---
name: Add user authentication (JWT)
about: Add lightweight authentication so signups can be associated with students
---

# Add user authentication (JWT)

## Summary

Add authentication so students can sign in and the app can reliably associate signups with user identities. Use JWT-based auth for a minimal implementation.

## Goals

- Add endpoints for register / login that issue JWTs.
- Protect signup/unregister endpoints to require authentication.
- Persist users in the database (email, name, grade, hashed password).
- Provide a simple `Authorization: Bearer <token>` flow for the frontend.

## Acceptance criteria

- Users can register and login to obtain JWTs.
- `POST /activities/{name}/signup` requires an authenticated user and uses their email if not provided.
- README contains setup steps for JWT secret and config.

## Suggested effort

Medium — 3–6 hours.

## Labels

`enhancement`, `security`, `backend`
