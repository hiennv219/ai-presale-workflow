#!/bin/sh
#
# Install git hooks from shared/hooks/ into .git/hooks/
# Run once after cloning: ./shared/hooks/install.sh
#

REPO_ROOT="$(git rev-parse --show-toplevel)"
HOOK_DIR="$REPO_ROOT/.git/hooks"
SRC_DIR="$(cd "$(dirname "$0")" && pwd)"

for hook in "$SRC_DIR"/*; do
  name="$(basename "$hook")"
  [ "$name" = "install.sh" ] && continue
  ln -sf "$hook" "$HOOK_DIR/$name"
  echo "  Installed: $name"
done

echo "Done. Hooks active."
