"""Fortune in a Pot — make.fun bounty u-golden-heron-44-fortune-in-a-pot-ded981e9.

Writes a single line (at most 120 characters) telling a houseplant's
fortune to /output/entry.txt: kind, warm and funny, in the cadence of a
prediction, about the plant on the windowsill and the new leaf it is
about to grow.

Deterministic: no input, no file reads, no randomness, no clock, no
network. The same constant text is written on every run, with no
trailing newline.
"""

import os

TEXT = (
    "The stars say a new leaf is coming, and it has already picked "
    "the sunniest spot on your windowsill."
)


def main() -> None:
    """Write the fortune to /output/entry.txt (or $ENTRY_OUTPUT)."""
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
