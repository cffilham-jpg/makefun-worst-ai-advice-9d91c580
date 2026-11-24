"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst possible advice an AI could give to
$MAKEFUN_OUTPUT_DIR/entry.txt (or <repo>/output/entry.txt when the
variable is unset). Python 3.13, standard library only.
"""

from __future__ import annotations

import os
from pathlib import Path

LINE = "To fix slow Wi-Fi, microwave your router for 30 seconds — the heat boosts the signal."


def validate(line: str) -> None:
    """Reject anything that is not exactly one line of 1-140 characters."""
    if not line:
        raise ValueError("line must not be empty")
    if len(line) > 140:
        raise ValueError("line must be at most 140 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be exactly one line")


def main() -> None:
    """Validate the line and write it to entry.txt."""
    validate(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        out_path = Path(output_dir) / "entry.txt"
    else:
        out_path = Path(__file__).resolve().parent / "output" / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
