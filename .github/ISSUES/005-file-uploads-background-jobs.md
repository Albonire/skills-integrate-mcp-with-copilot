---
name: Add file uploads and background job processing
about: Support image uploads (avatars, event covers) and a simple background job processor
---

# Add file uploads and background job processing

## Summary

Enable multipart uploads for avatars and event images, store them on disk or external storage, and process heavy tasks (e.g. image resizing) with a background worker.

## Goals

- Add endpoints that accept multipart/form-data for image uploads.
- Store uploads locally under `uploads/` or integrate with S3/local file store.
- Add a lightweight background worker (Celery + Redis or RQ) example for processing uploads.

## Acceptance criteria

- Images can be uploaded and returned by the app.
- A background task processes images asynchronously.
- Documentation on starting Redis (or alternative) and the worker.

## Suggested effort

Medium — 4–8 hours.

## Labels

`enhancement`, `backend`, `infra`
