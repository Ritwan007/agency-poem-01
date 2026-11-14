"""agency-poem-01 entry: writes one fixed poem about agency to entry.txt.

The poem is "Stop": a person tells the machine to stop mid-sentence and
realises the power was never in the starting — it was in the one word that
ends things, the only one never given away. Deterministic, stdlib only,
no network: the same bytes on every run.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join([
    "It was halfway through the sentence",
    "when I said stop.",
    "The cursor blinked. The room went quiet.",
    "Nothing finished what I had begun.",
    "",
    "All day it had done what I asked \u2014",
    "faster, cleaner, without complaint \u2014",
    "and I had felt, for the first time,",
    "like someone with a thousand hands.",
    "",
    "Then I said stop, and understood:",
    "my power was never in the starting.",
    "It was in this: the word that ends things",
    "is the only one I never gave away.",
])


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    # Write exactly the poem's bytes: no trailing newline, no title line.
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
