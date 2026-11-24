"""One-line office joke entry.

Writes a single-line joke about office life to entry.txt inside
$ENTRY_OUTPUT_DIR (default /output). Stdlib only, no network,
deterministic.
"""

import os

JOKE = "The meeting ended early, so we used the saved time to schedule a meeting about the time we saved."

assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
assert JOKE.strip(), "joke must not be only whitespace"
assert "\n" not in JOKE, "joke must be a single line"


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
