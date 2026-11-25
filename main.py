#!/usr/bin/env python3
"""One Star for Monday — u-clever-harbor-75-one-star-for-monday-9ead4a61.

Prints the single-line one-star review of Monday, written as though
Monday were a restaurant, and writes the same line to /output/entry.txt
for the grader. Python 3.13 standard library only.
"""

import os

REVIEW = "One star. Monday sat me by the door, forgot my coffee, and billed me for a weekend I never finished."


def main() -> None:
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(REVIEW + "\n")
    except OSError:
        pass
    print(REVIEW)


if __name__ == "__main__":
    main()
