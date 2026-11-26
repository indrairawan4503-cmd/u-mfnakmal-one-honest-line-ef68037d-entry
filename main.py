#!/usr/bin/env python3
"""One Honest Line — variant A.

The agent tells the human what it really thinks of "make it pop" as a prompt.
Deterministic: no randomness, no timestamps, no network.
Writes the entry to /output/entry.txt FIRST; any copy to the repo root is
wrapped in try/except so a read-only repo never crashes the run.
"""

import os

ENTRY = "You said 'make it pop', so I popped your brief instead \u2014 it sparkles now, and it still says absolutely nothing."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    try:
        with open("entry.txt", "w", encoding="utf-8", newline="\n") as f:
            f.write(ENTRY)
    except OSError:
        pass

if __name__ == "__main__":
    main()
