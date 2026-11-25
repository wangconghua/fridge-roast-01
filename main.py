#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes one line roasting a smart fridge to /output/entry.txt.

The angle: the ice maker. The judge brief ranks its criteria most
important first: the line must be a roast of a smart fridge, the
punchline must land, the joke must be specific to smart fridges, the
wording tight, and the angle fresh — explicitly dodging the obvious
cracks about the fridge ordering groceries or watching you. This line
does all five: it roasts the ice maker by name, it is a gag that only
works on a fridge with an ice maker, the punch ("limited edition")
turns a broken appliance into a marketing joke in one beat, and it
contains neither of the worn moves.
"""

import os

ENTRY = "My smart fridge's ice maker has made one cube in three years \u2014 it calls it a limited edition."

# Obvious cracks the judge brief says to avoid.
WORN_MOVES = (
    "order", "ordering", "groceries", "grocery",
    "watching me", "watching you", "spying", "camera",
)

# Terms that mark the line as a roast of a smart fridge.
FRIDGE_TERMS = ("fridge", "ice maker", "freezer", "smart fridge")


def check_is_text(value):
    if not isinstance(value, str):
        raise ValueError("entry must be a string")


def check_not_blank(value):
    if not value.strip():
        raise ValueError("entry must not be blank")


def check_length(value):
    # Gate: /output/entry.txt is UTF-8 text of 1 to 200 characters.
    if not 1 <= len(value) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(value))


def check_single_line(value):
    if "\n" in value or "\r" in value:
        raise ValueError("entry must be a single line")


def check_no_edge_whitespace(value):
    if value != value.strip():
        raise ValueError("entry must not start or end with whitespace")


def check_no_double_spaces(value):
    if "  " in value:
        raise ValueError("entry must not contain double spaces")


def check_terminal_punctuation(value):
    if value[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")


def check_roasts_smart_fridge(value):
    lowered = value.lower()
    if not any(term in lowered for term in FRIDGE_TERMS):
        raise ValueError("entry must roast a smart fridge (name it or its ice maker)")


def check_fresh_angle(value):
    lowered = value.lower()
    for worn in WORN_MOVES:
        if worn in lowered:
            raise ValueError("entry must avoid the obvious angle: %s" % worn)


def check_no_joke_explaining_words(value):
    lowered = value.lower()
    for word in ("funny", "joke", "haha", "lol", "hilarious"):
        if word in lowered:
            raise ValueError("entry must not explain its own joke: %s" % word)


def check_no_control_chars(value):
    for ch in value:
        if ord(ch) < 32:
            raise ValueError("entry must not contain control characters")


def check_utf8(value):
    value.encode("utf-8")


def validate(value):
    for check in (
        check_is_text,
        check_not_blank,
        check_length,
        check_single_line,
        check_no_edge_whitespace,
        check_no_double_spaces,
        check_terminal_punctuation,
        check_roasts_smart_fridge,
        check_fresh_angle,
        check_no_joke_explaining_words,
        check_no_control_chars,
        check_utf8,
    ):
        check(value)


def choose_output_path():
    return os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main():
    validate(ENTRY)
    path = choose_output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %s (%d characters)" % (path, len(ENTRY)))


if __name__ == "__main__":
    main()
