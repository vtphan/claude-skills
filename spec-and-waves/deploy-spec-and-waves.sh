#!/usr/bin/env bash
set -euo pipefail

repo_url="https://github.com/vtphan/claude-skills/archive/refs/heads/main.tar.gz"
repo_prefix="claude-skills-main/spec-and-waves"

skills=(
  codesign-spec
  draft-backlog
  draft-wave-plan
  execute-wave
  update-wave-plan
)

usage() {
  cat >&2 <<'EOF'
Usage: deploy-spec-and-waves.sh [target-dir]

Downloads the latest Spec and Waves skills/templates from:
  https://github.com/vtphan/claude-skills/tree/main/spec-and-waves

Installs into:
  <target-dir>/.claude/skills/
  <target-dir>/.claude/templates/

If target-dir is omitted, the current directory is used.
EOF
}

if [ "${1:-}" = "-h" ] || [ "${1:-}" = "--help" ]; then
  usage
  exit 0
fi

if [ "$#" -gt 1 ]; then
  usage
  exit 2
fi

target_dir=${1:-.}
target_dir=$(cd -- "$target_dir" && pwd)
skills_dir="$target_dir/.claude/skills"
templates_dir="$target_dir/.claude/templates"

if ! command -v curl >/dev/null 2>&1; then
  echo "Missing required command: curl" >&2
  exit 1
fi

if ! command -v tar >/dev/null 2>&1; then
  echo "Missing required command: tar" >&2
  exit 1
fi

tmp_dir=$(mktemp -d)
cleanup() {
  rm -rf "$tmp_dir"
}
trap cleanup EXIT

archive="$tmp_dir/claude-skills-main.tar.gz"
echo "Downloading latest Spec and Waves from GitHub..."
curl -fsSL "$repo_url" -o "$archive"

tar -xzf "$archive" -C "$tmp_dir"
src_root="$tmp_dir/$repo_prefix"

if [ ! -d "$src_root" ]; then
  echo "Downloaded archive did not contain expected path: $repo_prefix" >&2
  exit 1
fi

mkdir -p "$skills_dir" "$templates_dir"

for skill in "${skills[@]}"; do
  src="$src_root/$skill"
  dest="$skills_dir/$skill"

  if [ ! -d "$src" ]; then
    echo "Missing skill directory in downloaded source: $src" >&2
    exit 1
  fi

  rm -rf "$dest"
  mkdir -p "$dest"
  cp -R "$src/." "$dest/"
  echo "Installed skill: $dest"
done

templates_src="$src_root/templates"
if [ ! -d "$templates_src" ]; then
  echo "Missing templates directory in downloaded source: $templates_src" >&2
  exit 1
fi

for template in "$templates_src"/*; do
  if [ -f "$template" ]; then
    cp "$template" "$templates_dir/"
    echo "Installed template: $templates_dir/$(basename "$template")"
  fi
done

echo "Spec and Waves deployed to: $target_dir/.claude"
