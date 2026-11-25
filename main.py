#!/usr/bin/env python3
"""One Star for Monday — u-clever-harbor-75-one-star-for-monday-9ead4a61.

Prints the single-line one-star review of Monday, written as though
Monday were a restaurant, and writes the same line to /output/entry.txt
for the grader. Python 3.13 standard library only.
"""

import os

REVIEW = "One star. Monday sat me by the door, forgot my coffee, and billed me for a weekend I never finished."

# Kit gates (competition.yaml): 1-180 chars, at most 25 words, one line.
assert REVIEW, "entry must not be empty"
assert "\n" not in REVIEW and "\r" not in REVIEW, "entry must be a single line"
assert not REVIEW.isspace(), "entry must not be only whitespace"
assert len(REVIEW) <= 180, "entry is %d chars, over the 180 cap" % len(REVIEW)
assert len(REVIEW.split()) <= 25, "entry is %d words, over the 25-word cap" % len(REVIEW.split())


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
