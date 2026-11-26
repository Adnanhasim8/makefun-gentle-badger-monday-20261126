#!/usr/bin/env python3
"""Monday Morning Punchlines entry.

Writes one funny Monday-morning punchline, a single line of 1-200
characters, to /output/entry.txt. Python 3.13 standard library only,
no network at run time.
"""

import os

ENTRY = "My blanket filed a restraining order against my Monday alarm."


def main() -> None:
    # Gate assertions: the entry must be exactly one line, 1-200
    # characters, non-empty and not only whitespace.
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must be non-empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Verify what was written matches the gate.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry differs from ENTRY"
    assert 1 <= len(written) <= 200 and "\n" not in written


if __name__ == "__main__":
    main()
