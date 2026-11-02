#!/usr/bin/env bash
# Links each skill into ~/.claude/skills, pointing back at this checkout,
# so a git pull here updates the installed copies.
set -euo pipefail
here=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$HOME/.claude/skills"
for dir in "$here"/skills/*/; do
  name=$(basename "$dir")
  dest="$HOME/.claude/skills/$name"
  if [ -e "$dest" ] && [ ! -L "$dest" ]; then
    echo "$dest exists and is not a symlink; move it aside first" >&2; exit 1
  fi
  ln -sfn "${dir%/}" "$dest"
  echo "linked $name"
done
echo "restart claude code to pick them up"
