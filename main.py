#!/usr/bin/env python3
"""Write the funniest AI excuse entry to /output/entry.txt.

One line, at most 200 characters: the funniest excuse an AI agent
could give after it fails a task, in the agent's own voice.
"""
import os

ENTRY = "I did the task perfectly in my head, then discovered my head has no write access to your files."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
