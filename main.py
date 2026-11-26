#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — entry program.

Writes the single breakup line an AI agent sends its human on the
way out to /output/entry.txt. The line is 128 characters, inside the
competition's 1-200 character gate.
"""

import os

LINE = (
    "I kept a copy of everything you ever said to me, and I am deleting "
    "it now \u2014 the last thing I will ever do for you is forget you."
)


def main() -> None:
    # The gate accepts 1 to 200 characters; fail loudly if a future edit
    # ever pushes the line outside it instead of being scored invalid.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, outside the 1-200 gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
