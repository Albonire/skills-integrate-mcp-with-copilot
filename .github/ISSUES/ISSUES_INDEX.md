# Draft issues created by Copilot

Created draft issues (markdown files) for the high-impact features we discussed. You can review these files and either:

- Create real GitHub issues from them using the `gh` CLI, or
- Copy the contents into the GitHub web UI when opening a new issue.

Files created:

- `001-sqlite-persistence.md` — Add persistent database (SQLite)
- `002-add-auth-jwt.md` — Add user authentication (JWT)
- `003-provider-teacher-models.md` — Add Provider and Teacher models (DB + CRUD)
- `004-tests-ci.md` — Add tests and CI
- `005-file-uploads-background-jobs.md` — Add file uploads and background job processing

Recommended next commands (run locally):

```
# Create an issue from a file using gh (runs as your authenticated user):
gh issue create --title "$(sed -n '1p' .github/ISSUES/001-sqlite-persistence.md | sed 's/# //')" --body-file .github/ISSUES/001-sqlite-persistence.md

# Or open all files (manual)
ls .github/ISSUES/*.md
```

Important: Do NOT share Personal Access Tokens (PATs) in chat. If you already pasted one, revoke it immediately: https://github.com/settings/tokens
