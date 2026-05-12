#!/usr/bin/env python3
"""
pack.py — Bundle source files for diagram-keeper.

Reads settings from pack.cfg in the current directory (INI format, [pack] section).
Command-line arguments override config file values.

Config file (pack.cfg):
    [pack]
    src = ./src
    dest = pack.txt
    chunk_size = 50000
    exclude = */test/* */generated/*

Usage:
    python scripts/pack.py
    python scripts/pack.py --src <dir> [--dest <file>] [other options]

Output format:
    === INDEX ===
    File: <relative/path>
    Classes: A, B
    ...

    === FILE: <relative/path> ===
    <file content>
    ...
"""

from __future__ import annotations

import argparse
import configparser
import fnmatch
import re
import sys
from pathlib import Path
from typing import Iterable

DEFAULT_CONFIG = Path("pack.cfg")

DEFAULT_EXTENSIONS = {
    # C / C++
    ".c", ".cpp", ".cxx", ".cc", ".c++",
    ".h", ".hpp", ".hxx", ".hh",
    # Java
    ".java",
    # C#
    ".cs",
    # Visual Basic
    ".vb",
    # Python
    ".py",
    # TypeScript / JavaScript
    ".ts", ".tsx", ".js", ".jsx",
    # PHP
    ".php",
    # Rust
    ".rs",
}

# Loose regex — INDEX entries are hints for the AI, not ground truth.
CLASS_PATTERN = re.compile(
    r"^\s*(?:pub|public|internal|private|protected|static|sealed|abstract|final|partial|"
    r"friend|mustinherit|notinheritable|export|default|readonly|\s)*"
    r"\b(?:class|interface|struct|module|structure|trait|enum)\s+([A-Za-z_][A-Za-z0-9_]*)",
    re.MULTILINE | re.IGNORECASE,
)


# ── Config ────────────────────────────────────────────────────────────────────

def load_config(config_path: Path) -> dict[str, str]:
    """Load [pack] section from an INI config file. Returns {} if not found."""
    if not config_path.exists():
        return {}
    cp = configparser.ConfigParser()
    cp.read(config_path, encoding="utf-8")
    if not cp.has_section("pack"):
        return {}
    return dict(cp["pack"])


def split_words(value: str) -> list[str]:
    """Split a whitespace-separated config value into a list, ignoring empty strings."""
    return [v for v in value.split() if v]


# ── Source scanning ───────────────────────────────────────────────────────────

def iter_source_files(
    root: Path,
    extensions: set[str],
    includes: list[str],
    excludes: list[str],
) -> Iterable[Path]:
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() not in extensions:
            continue
        rel = path.relative_to(root).as_posix()
        if includes and not any(fnmatch.fnmatch(rel, pat) for pat in includes):
            continue
        if excludes and any(fnmatch.fnmatch(rel, pat) for pat in excludes):
            continue
        yield path


def extract_classes(source: str) -> list[str]:
    seen: list[str] = []
    for name in CLASS_PATTERN.findall(source):
        if name not in seen:
            seen.append(name)
    return seen


def read_text(path: Path) -> str:
    for enc in ("utf-8", "utf-8-sig", "cp932", "latin-1"):
        try:
            return path.read_text(encoding=enc)
        except UnicodeDecodeError:
            continue
    return path.read_bytes().decode("utf-8", errors="replace")


# ── Output formatting ─────────────────────────────────────────────────────────

def build_manifest_section(entries: list[tuple[str, list[str]]]) -> str:
    lines = ["=== INDEX ==="]
    for rel, classes in entries:
        lines.append(f"File: {rel}")
        lines.append(f"Classes: {', '.join(classes)}" if classes else "Classes: (none detected)")
    return "\n".join(lines) + "\n"


def build_file_section(rel: str, content: str) -> str:
    if not content.endswith("\n"):
        content += "\n"
    return f"\n=== FILE: {rel} ===\n{content}"


def chunk_bundle(
    entries: list[tuple[str, list[str], str]],
    max_chars: int | None,
) -> list[str]:
    """Split entries into chunks, each under max_chars when set."""
    if max_chars is None:
        manifest = build_manifest_section([(rel, cls) for rel, cls, _ in entries])
        body = "".join(build_file_section(rel, content) for rel, _, content in entries)
        return [manifest + body]

    chunks: list[str] = []
    current: list[tuple[str, list[str], str]] = []

    def flush() -> None:
        if not current:
            return
        manifest = build_manifest_section([(rel, cls) for rel, cls, _ in current])
        body = "".join(build_file_section(rel, content) for rel, _, content in current)
        chunks.append(manifest + body)

    for entry in entries:
        tentative = current + [entry]
        manifest = build_manifest_section([(rel, cls) for rel, cls, _ in tentative])
        body = "".join(build_file_section(rel, content) for rel, _, content in tentative)
        if len(manifest) + len(body) > max_chars and current:
            flush()
            current = [entry]
        else:
            current = tentative

    flush()
    return chunks


def write_chunks(out_path: Path, chunks: list[str]) -> list[Path]:
    if len(chunks) == 1:
        out_path.write_text(chunks[0], encoding="utf-8")
        return [out_path]
    written: list[Path] = []
    stem = out_path.stem
    suffix = out_path.suffix or ".txt"
    for i, chunk in enumerate(chunks, 1):
        p = out_path.parent / f"{stem}-{i:03d}{suffix}"
        p.write_text(chunk, encoding="utf-8")
        written.append(p)
    return written


# ── CLI ───────────────────────────────────────────────────────────────────────

def parse_args(config: dict[str, str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--config", type=Path, default=None,
                   help=f"Config file path (default: {DEFAULT_CONFIG})")
    p.add_argument("--src", type=Path, default=None,
                   help="Source directory to scan")
    p.add_argument("--dest", type=Path, default=None,
                   help="Output file (default: pack.txt)")
    p.add_argument("--include", action="append", default=None,
                   help="Glob pattern to include (repeatable)")
    p.add_argument("--exclude", action="append", default=None,
                   help="Glob pattern to exclude (repeatable)")
    p.add_argument("--chunk-size", type=int, default=None,
                   help="Split output when a chunk exceeds this char count")
    p.add_argument("--ext", action="append", default=None,
                   help="Override extension list (e.g. --ext .cpp --ext .h)")

    args = p.parse_args()

    # Apply config values where CLI arg was not given
    if args.src is None and "src" in config:
        args.src = Path(config["src"])
    if args.dest is None:
        args.dest = Path(config.get("dest", "pack.txt"))
    if args.include is None:
        args.include = split_words(config.get("include", ""))
    if args.exclude is None:
        args.exclude = split_words(config.get("exclude", ""))
    if args.chunk_size is None and config.get("chunk_size", "").strip():
        args.chunk_size = int(config["chunk_size"])
    if args.ext is None:
        args.ext = split_words(config.get("ext", ""))

    return args


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> int:
    # First pass: check for --config override before loading config
    pre = argparse.ArgumentParser(add_help=False)
    pre.add_argument("--config", type=Path, default=None)
    pre_args, _ = pre.parse_known_args()
    config_path = pre_args.config or DEFAULT_CONFIG

    config = load_config(config_path)
    args = parse_args(config)

    if args.src is None:
        print("error: --src is required (or set 'src' in pack.cfg)", file=sys.stderr)
        return 2

    src = args.src.resolve()
    if not src.is_dir():
        print(f"error: not a directory: {src}", file=sys.stderr)
        return 2

    extensions = (
        {e.lower() if e.startswith(".") else f".{e.lower()}" for e in args.ext}
        or DEFAULT_EXTENSIONS
    )

    entries: list[tuple[str, list[str], str]] = []
    for path in iter_source_files(src, extensions, args.include, args.exclude):
        rel = path.relative_to(src).as_posix()
        content = read_text(path)
        entries.append((rel, extract_classes(content), content))

    if not entries:
        print(f"warning: no source files matched under {src}", file=sys.stderr)

    chunks = chunk_bundle(entries, args.chunk_size)
    written = write_chunks(args.dest, chunks)
    for p in written:
        print(f"wrote {p} ({p.stat().st_size:,} bytes)")
    print(f"files: {len(entries)}  chunks: {len(written)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
