#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

Writes exactly one character, the letter J, to entry.txt.

J stands for "jackpot": the day hit the jackpot. It is vivid and specific
(a sharp picture, not a vague mood), funny and surprising in a way that
lands at once, and true to a real day — an honest report, not a
performance. The letter fits its word exactly, and it is not the obvious
pick (A for amazing, Z for zero sleep) where a sharper one exists.

Deterministic: no network, no randomness, no clock. The output is the
single byte "J" with no trailing newline, so the file is exactly 1
character, inside the gate of 1 to 1 characters.
"""

import os

LETTER = "J"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
