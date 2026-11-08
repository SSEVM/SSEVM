#!/usr/bin/env bash
# SSEVM privacy check (owner's rule): one private word must never appear in this
# public repository. The pattern below matches it and its spellings without
# writing it out. Run before every commit and push; CI runs it on every push/PR.
set -u
cd "$(dirname "$0")/.."
hits=$(git ls-files -z | xargs -0 grep -nIiE 'm[ou]h[a]j' 2>/dev/null)
if [ -n "$hits" ]; then
  echo "PRIVACY CHECK FAILED: the private word was found:"; echo "$hits"; exit 1
fi
echo "privacy check: clean"
