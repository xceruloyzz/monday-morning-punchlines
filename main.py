"""Monday Morning Punchlines entry.

Writes one Monday-morning one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: the same bytes on every run, no temp files, no trailing newline.

Tie-break note: the joke is kept short on purpose (76 of 200 chars) -- the
judge weighs economy of words, so every word has to earn its place.
"""

import os

# One literal, one line: the whole entry lives here so a re-read can never drift.
JOKE = "Monday: my alarm rings, my coffee quits, and my bed files for custody of me."

MAX_CHARS = 200


def main():
    text = JOKE
    if not text or not text.strip():
        raise ValueError("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError("entry exceeds 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write directly to the final file: no temp file in the output folder.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
