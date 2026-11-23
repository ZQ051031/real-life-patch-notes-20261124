"""Real-life patch notes entry: writes one patch-note line to /output/entry.txt.

Standard library only; no network.
"""

import os

ENTRY = "v2.1.0: fixed a bug where the brain replayed an embarrassing moment from 2011, unprompted, at 3 a.m."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
