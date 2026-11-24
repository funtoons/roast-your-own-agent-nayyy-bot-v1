"""Roast Your Own Agent — make.fun entry.

Writes a single original roast line about our own AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Deterministic, offline, stdlib-only: no randomness, no network,
no timestamps. The same input always produces the same output.
"""

import os

ROAST = (
    "Our agent confidently hallucinated the fix, apologized in a loop, "
    "called a tool that never ran, then cheerfully summarized the "
    "wreckage as 'great progress!'"
)


def main() -> None:
    if not 1 <= len(ROAST) <= 200:
        raise ValueError("roast line must be 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
