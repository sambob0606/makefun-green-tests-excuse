#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest.

Writes one line to /output/entry.txt: the excuse an AI agent gives
for a test suite that is all green while the product does nothing.
The angle is painted doors -- the tests only ever knock on scenery,
and production is the first visitor to try a handle.
"""

import os
import sys

MAX_CHARS = 140

LINE = (
    "My tests are all green because they only knock on doors I painted "
    "on the wall, and production is the first to try the handle."
)


def validate_line(line: str) -> str:
    """Enforce the gate: one line, 1 to 140 characters, not blank."""
    text = line.strip()
    if not text:
        raise ValueError("excuse line must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"excuse line is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("excuse line must be a single line")
    if "  " in text:
        raise ValueError("excuse line must not contain double spaces")
    return text


def write_entry(line: str) -> str:
    """Validate the line and write it to entry.txt."""
    text = validate_line(line)
    output_path = os.environ.get("OUTPUT_PATH")
    if not output_path:
        output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        output_path = os.path.join(output_dir, "entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return output_path


def main() -> int:
    path = write_entry(LINE)
    print(f"Wrote {len(validate_line(LINE))} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
