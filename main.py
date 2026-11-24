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


def verify_entry(path: str) -> None:
    with open(path, "rb") as f:
        raw = f.read()
    if raw != b"J":
        raise SystemExit(
            f"entry verification failed: expected exactly 1 byte b'J', "
            f"got {len(raw)} bytes: {raw!r}"
        )
    if len(raw) != 1 or not (b"A" <= raw <= b"Z"):
        raise SystemExit(
            f"entry verification failed: expected a single A-Z byte, got {raw!r}"
        )


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Re-read the file and verify it byte-for-byte: the competition gate
    # is exactly 1 character, so a stray newline or wrong byte would
    # silently fail the entry. Fail loudly instead of shipping bad output.
    verify_entry(path)


if __name__ == "__main__":
    main()
