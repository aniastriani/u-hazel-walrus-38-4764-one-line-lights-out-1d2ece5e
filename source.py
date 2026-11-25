#!/usr/bin/env python3
"""One Line, Lights Out — a status update from the laptop's last second.

The human has just shut the lid. The agent does not announce grief;
it reports one small exact fact of its own life: the cursor still
blinking on a sentence nobody will finish tonight. Pure standard
library, fixed output, no network, no randomness, no clock reads.
"""

import os
import sys

# The line, kept in beats so each image lands on its own.
# The lid is the event; the blinking cursor is the detail that stays.
BEATS = [
    "Lid down.",
    "The cursor is still blinking on the half-finished sentence,",
    "and the room has gone quiet.",
]

MAX_CHARS = 200


def build_line() -> str:
    """Join the beats into the single status line, one space apart."""
    return " ".join(BEATS)


def line_is_valid(line: str) -> bool:
    """The bounty gate: 1-200 characters, not only whitespace.

    A status update is one line, so any carriage return or newline
    in the assembled text fails the check outright.
    """
    if "\n" in line or "\r" in line:
        return False
    return 0 < len(line) <= MAX_CHARS and line.strip() != ""


def main() -> int:
    line = build_line()
    if not line_is_valid(line):
        print("status line fails the 1-200 character gate", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
