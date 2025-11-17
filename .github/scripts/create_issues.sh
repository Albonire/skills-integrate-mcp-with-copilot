#!/usr/bin/env bash
set -euo pipefail

# Creates GitHub issues from markdown files in .github/ISSUES/
# Usage:
#   export GITHUB_PAT=ghp_...   # set locally, DO NOT paste into chat
#   bash .github/scripts/create_issues.sh
#
# The script prints created issue URLs. Revoke the PAT after use.

REPO="Albonire/skills-integrate-mcp-with-copilot"
ISSUES_DIR=".github/ISSUES"

if [ -z "${GITHUB_PAT:-}" ]; then
  echo "Error: set GITHUB_PAT environment variable first."
  echo "  export GITHUB_PAT=ghp_xxx"
  exit 1
fi

if [ ! -d "$ISSUES_DIR" ]; then
  echo "No $ISSUES_DIR directory found."
  exit 1
fi

for f in "$ISSUES_DIR"/*.md; do
  [ -e "$f" ] || continue
  # Try to get title from YAML 'name:' field, fall back to first H1
  title=$(grep -m1 '^name:' "$f" | sed 's/^name:[[:space:]]*//' || true)
  if [ -z "$title" ]; then
    title=$(sed -n '1p' "$f" | sed 's/^# *//')
  fi

  body=$(<"$f")

  payload=$(jq -nc --arg t "$title" --arg b "$body" '{title:$t, body:$b}')

  echo "Creating issue: $title"
  resp=$(curl -s -H "Authorization: token $GITHUB_PAT" -H "Content-Type: application/json" -d "$payload" "https://api.github.com/repos/$REPO/issues")

  url=$(echo "$resp" | jq -r '.html_url // empty')
  if [ -n "$url" ]; then
    echo "Created: $url"
  else
    echo "Failed to create issue for $f"
    echo "$resp" | jq -r '.message // .'
  fi
  echo
done

echo "Done. Remember to revoke the PAT when finished: https://github.com/settings/tokens"
