"""Matching brackets"""


OPENERS = ["(", "[", "{"]
CLOSERS = [")", "]", "}"]


def is_paired(input_string: str) -> bool:
    """Return True if all of the [], {}, () pairs in `input_string` are closed"""
    opens = []
    next_close = ""
    for char in input_string:
        if char in OPENERS:
            opens.append(char)
            next_close = CLOSERS[OPENERS.index(char)]

        if char in CLOSERS:
            if char != next_close:
                return False
            del opens[-1]
            if len(opens) > 0:
                next_close = CLOSERS[OPENERS.index(opens[-1])]
            else:
                next_close = ""

    return len(opens) == 0
