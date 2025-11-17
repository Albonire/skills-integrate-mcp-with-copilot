---
name: Add Provider and Teacher models (DB + CRUD)
about: Introduce Provider and Teacher domain models and CRUD APIs
---

# Add Provider and Teacher models (DB + CRUD)

## Summary

Introduce domain models for `Provider` (organization that offers activities) and `Teacher` (staff running activities), store them in the DB, and expose CRUD endpoints.

## Goals

- Add DB models and tables for Provider and Teacher.
- Implement CRUD endpoints (create, read, update, delete) and basic validation.
- Allow associating Activities with a Provider and optionally a Teacher.

## Acceptance criteria

- Provider and Teacher persisted in DB and manageable via API.
- Activities include optional `provider_id` and `teacher_id` fields.
- Frontend can list provider/teacher details (optional enhancement).

## Suggested effort

Medium — 4–8 hours.

## Labels

`enhancement`, `backend`, `api`
