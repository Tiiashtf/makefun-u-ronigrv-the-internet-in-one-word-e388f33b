"""The Internet in One Word — entry program.

Writes a single word describing the whole internet to /output/entry.txt.
Deterministic: no input, no network, no randomness — every run writes the
exact same bytes.
"""

import os
import shutil

WORD = "doomscroll"


def main() -> None:
    out_dir = "/output"
    # Never remove the output directory itself: the grader may run this with
    # a root-owned output directory inside a sticky parent, where removing
    # the directory fails. Only clear its contents, then write.
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
