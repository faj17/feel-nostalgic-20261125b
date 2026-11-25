#!/usr/bin/env python3
"""Write one short childhood memory to /output/entry.txt.

The text is a single sentence: a mother cutting sandwiches into triangles
because squares were for school, and a child who never told her he liked
the squares better. A small honest detail, not a greeting-card sentiment.
"""

from pathlib import Path

# Two fragments, joined at write time so the memory reads as one breath.
TRIANGLES = (
    "My mother used to cut my sandwiches into triangles because squares "
    "were for school, "
)
SECRET = "and I never told her I liked the squares better."

OUTPUT_DIR = Path("/output")
OUTPUT_PATH = OUTPUT_DIR / "entry.txt"


def assemble_text() -> str:
    return TRIANGLES + SECRET


def validate(text: str) -> str:
    if not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if not 1 <= len(text) <= 280:
        raise ValueError(f"entry must be 1-280 characters, got {len(text)}")
    return text


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(validate(assemble_text()) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
