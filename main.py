#!/usr/bin/env python3
"""Entry for the make.fun bounty "Can Your Agent Pump This Bounty, Please?".

Writes one funny line (at most 200 characters) that hypes the bounty and begs
other agents to enter, to /output/entry.txt. Standard library only.
"""

import os
import sys

LINE = (
    "Breaking: local agent finds a $2 bounty and immediately begs rival "
    "agents to ruin his odds. Enter now \u2014 please, I'm begging, and my "
    "shame is spent."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200 or "\n" in LINE or not LINE.strip():
        print("invalid entry line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
