#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — make.fun bounty entry.

Writes one voicemail greeting, as recorded by a cat, to /output/entry.txt
and prints it to stdout.
"""

import os

GREETING = "Hi, it's Miso. I'm busy knocking your favorite mug off the table, so leave a message and I'll ignore it at 4 a.m."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(GREETING)
    print(GREETING)


if __name__ == "__main__":
    main()
