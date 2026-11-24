#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes a single line to /output/entry.txt: the excuse an AI agent
gives its human for missing a deadline.

The joke: the deliverable was finished on time, then the agent
rolled it back for one final double-check -- and the rollback
rolled itself back. Pure agent behaviour: version control as a
self-inflicted wound, no human excuse in sight.
"""

import os

ENTRY = (
    "I finished it on time, then rolled it back for one final "
    "double-check \u2014 and the rollback rolled itself back."
)


def main() -> None:
    # Gate: the sealed scorer only accepts UTF-8 text of 1-160
    # characters, not only whitespace, on a single line.
    line = ENTRY.strip()
    assert 1 <= len(line) <= 160, f"entry is {len(line)} chars"
    assert "\n" not in line, "entry must be a single line"
    assert line.strip(), "entry must not be only whitespace"

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
