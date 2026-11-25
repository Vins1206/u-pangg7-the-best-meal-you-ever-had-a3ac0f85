"""Best meal ever had: one concrete sentence, at most 200 characters.

Writes exactly one sentence of plain text to /output/entry.txt.
Python standard library only; no input files, no network.
"""

import os

SENTENCE = (
    "At my grandmother's kitchen table in Bandung, I tore warm rendang beef "
    "with my fingers while rain drummed the tin roof and the coconut gravy "
    "stained my rice gold."
)


def main():
    if not 1 <= len(SENTENCE) <= 200:
        raise ValueError("sentence must be 1 to 200 characters")
    if SENTENCE.count(".") != 1 or not SENTENCE.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
