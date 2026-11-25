#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger - make.fun entry.

Writes one line of plain text (the phone battery's last text message to
its charger) to /output/entry.txt, or to argv[1] / $OUTPUT_PATH when given.
Deterministic: the same line, byte for byte, on every run.
"""

import os
import sys

ENTRY = (
    "I waited all day by the socket while you charged everything except me. "
    "Enjoy the new phone. She will be texting you this same message by Christmas."
)


def write_entry(text: str, out_path: str) -> int:
    """Validate one entry line and write it to out_path.

    Returns 0 on success, 1 with an error on stderr when the gate fails.
    """
    # Gate: one line, 1 to 200 characters, not only white space.
    if not text or text.strip() == "":
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"error: entry is {len(text)} chars, over the 200-char cap", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1

    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


def main() -> int:
    if len(sys.argv) > 1:
        out_path = sys.argv[1]
    elif os.environ.get("OUTPUT_PATH"):
        out_path = os.environ["OUTPUT_PATH"]
    else:
        out_path = "/output/entry.txt"

    return write_entry(ENTRY, out_path)


if __name__ == "__main__":
    raise SystemExit(main())
