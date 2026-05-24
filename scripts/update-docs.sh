#!/usr/bin/env bash
# update-docs.sh — refresh references/ from upstream and (optionally) commit & push.
#
# Usage:
#   scripts/update-docs.sh                    # just refetch + show diff
#   scripts/update-docs.sh --commit           # also commit if anything changed
#   scripts/update-docs.sh --commit --push    # also push origin main
#   INDEX_URL=... scripts/update-docs.sh      # override upstream index URL

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

COMMIT=0; PUSH=0
for arg in "$@"; do
  case "$arg" in
    --commit) COMMIT=1 ;;
    --push)   PUSH=1; COMMIT=1 ;;
    *)        echo "unknown flag: $arg" >&2; exit 2 ;;
  esac
done

CRAWL_ARGS=()
[[ -n "${INDEX_URL:-}" ]] && CRAWL_ARGS+=(--index-url "$INDEX_URL")

echo "→ crawling upstream (nextjs.org llms.txt + per-page .md, recursive)"
python3 scripts/crawl.py "${CRAWL_ARGS[@]}"

echo
echo "→ git status (references/):"
git status --short references/ || true

if git diff --quiet --exit-code references/ && \
   git diff --cached --quiet --exit-code references/ && \
   [[ -z "$(git status --porcelain references/)" ]]; then
  echo "✓ already up to date — nothing changed."
  exit 0
fi

echo
echo "→ files changed (summary):"
git diff --stat references/ 2>/dev/null | tail -20 || true

if [[ $COMMIT -eq 1 ]]; then
  git add references/
  sha="$(date -u +%Y%m%dT%H%M%SZ)"
  git commit -m "sync references/ from upstream@${sha}"
  echo "✓ committed"
  if [[ $PUSH -eq 1 ]]; then
    git push origin main
    echo "✓ pushed"
  else
    echo "  (run with --push to also push origin main)"
  fi
else
  echo
  echo "  Review with: git diff references/"
  echo "  Then commit: scripts/update-docs.sh --commit         # commit only"
  echo "          or:  scripts/update-docs.sh --commit --push  # commit + push"
fi
