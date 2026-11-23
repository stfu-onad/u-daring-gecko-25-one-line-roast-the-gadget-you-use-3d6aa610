#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (<=200 chars, one line) to
/output/entry.txt. The roast targets wireless earbuds, a gadget used
every day: one earbud always dies first, and the joke turns that
familiar moment into the music sneaking out of the room.

Candidates considered and rejected: the phone battery that hits 1%
and survives another hour (too common a complaint), the smart kettle
demanding a firmware update (close to the brief's own example), and
face unlock failing after a yawn (weaker sting). The earbuds line
won for the freshest image and the tightest wording.
"""

import os

ROAST = (
    "My earbuds die one ear at a time, so my music sounds like "
    "it's sneaking out of the room without saying goodbye."
)


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"roast is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "roast must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
