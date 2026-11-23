"""Entry for make.fun's "The joke about the demo".

Writes one one-line joke about working beside AI coding agents
to /output/entry.txt, as the bounty requires.
"""

import os

JOKE = (
    "I told my AI coding agent to rehearse the demo until it "
    "couldn't crash; it rehearsed the crash 400 times, and now "
    "performs it flawlessly."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
