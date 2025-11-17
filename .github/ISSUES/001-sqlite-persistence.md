---
name: Add persistent database (SQLite)
about: Replace in-memory storage with a simple SQLite database and migrations
---

# Add persistent database (SQLite)

## Summary

Replace the current in-memory `activities` store with a persistent SQLite database so data survives restarts and multiple processes can share state.

## Goals

- Use SQLite (via `sqlmodel` or `sqlite3`/`SQLAlchemy`) for local development.
- Add a simple migration workflow (or initialize schema on startup).
- Migrate Activities and participant signups to the DB.
- Update the frontend to continue working unchanged (API contract preserved).

## Acceptance criteria

- The app persists activities and signups to a local `db.sqlite` file.
- Existing endpoints (`GET /activities`, `POST /activities/{name}/signup`, `DELETE /activities/{name}/unregister`) work with the DB.
- README updated with new setup steps and dependencies in `requirements.txt`.
- Basic migration or schema-init script included.

## Suggested effort

Small — 2–4 hours.

## Labels

`enhancement`, `backend`, `good first issue`
