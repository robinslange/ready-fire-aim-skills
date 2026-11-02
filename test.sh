#!/usr/bin/env bash
# Runs every test suite. Exits non-zero if any suite fails.
set -u
here=$(cd "$(dirname "$0")" && pwd)
export PYTHONDONTWRITEBYTECODE=1
status=0
for suite in "$here"/tests/test_*.py; do
  if out=$(python3 -m unittest -q "$suite" 2>&1); then
    echo "pass  $(basename "$suite")"
  else
    echo "FAIL  $(basename "$suite")"; echo "$out" | sed 's/^/      /'; status=1
  fi
done
bash -n "$here/install.sh" || status=1
exit $status
