#!/usr/bin/env python3
"""Write the Office Artifacts placard entry to /output/entry.txt."""

import os

ENTRY = "Lanyard, c. 2019, woven nylon, gift of Human Resources \u2014 worn daily for six years by a man whose name nobody in the building ever learned."

def main():
    # Gate: one line, 1-180 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 180, "entry must be 1-180 characters"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be a single non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
