#!/usr/bin/env python3
"""One Star for Monday — make.fun entry.

Writes a single-line, one-star review of Monday as if Monday were a
restaurant to /output/entry.txt (the grader's output path; falls back to
./output/entry.txt when /output is not writable).

The review (23 words, 111 characters):
    Monday's sat me at a table for one, served cold coffee and a full
    week of work, then billed me for the weekend.
"""

import os
import sys

ENTRY = (
    "Monday's sat me at a table for one, served cold coffee and a full "
    "week of work, then billed me for the weekend."
)


def main() -> int:
    # Gate: 1-180 UTF-8 characters, at most 25 words, one line, plain text.
    words = ENTRY.split()
    assert 1 <= len(ENTRY) <= 180, f"entry is {len(ENTRY)} chars"
    assert len(words) <= 25, f"entry is {len(words)} words"
    assert "\n" not in ENTRY, "entry must be a single line"

    for out_dir in ("/output", os.path.join(os.getcwd(), "output")):
        try:
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(ENTRY)
            print(f"wrote {path} ({len(ENTRY)} chars, {len(words)} words)")
            return 0
        except OSError:
            continue
    print("error: could not write entry.txt", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
