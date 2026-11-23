"""Real-life patch notes entry: writes one patch-note line to /output/entry.txt.

Standard library only; no network.
"""

import os

ENTRY = "v1.8.2: fixed a bug where the user replied 'you too' when the waiter said 'enjoy your meal.'"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
