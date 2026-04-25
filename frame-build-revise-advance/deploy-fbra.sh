#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $0 <target-dir>" >&2
}

if [ "$#" -ne 1 ]; then
  usage
  exit 2
fi

target_dir=$1
script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
skills_dir="$target_dir/.claude/skills"

skills=(frame build revise advance)

mkdir -p "$skills_dir"

for skill in "${skills[@]}"; do
  src="$script_dir/$skill"
  dest="$skills_dir/$skill"

  if [ ! -d "$src" ]; then
    echo "Missing skill directory: $src" >&2
    exit 1
  fi

  mkdir -p "$dest"
  rsync -a --delete "$src/" "$dest/"
  echo "Deployed $skill -> $dest"
done

echo "FBRA skills deployed to $skills_dir"
