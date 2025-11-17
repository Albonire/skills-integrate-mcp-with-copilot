---
name: Add tests and CI
about: Add pytest tests and a GitHub Actions workflow to run them
---

# Add tests and CI

## Summary

Introduce automated tests (pytest) and a GitHub Actions workflow that runs tests on push/PRs.

## Goals

- Add unit tests for core API operations (signup, unregister, activity listing).
- Add `requirements-dev.txt` (pytest, httpx) or update `requirements.txt`.
- Add `.github/workflows/ci.yml` to run tests on Python matrix (3.9/3.10/3.11).

## Acceptance criteria

- Tests run successfully in CI and fail on regressions.
- PRs will trigger the test workflow.

## Suggested effort

Small — 2–4 hours.

## Labels

`test`, `ci`, `good first issue`
