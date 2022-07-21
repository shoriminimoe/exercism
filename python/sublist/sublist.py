"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""
from typing import Iterable

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def nwise(superlist: list, n=2) -> Iterable[list]:
    """Yield sliding sublists of superlist with length n

    s -> (s0, ..., sn-1), (s1, ..., sn), (s2, ..., sn+1), ...
    """
    if n > len(superlist):
        raise ValueError("n must be less than the length of superlist")

    for i in range(len(superlist) - n + 1):
        yield superlist[i : i + n]


def sublist(list_one: list, list_two: list) -> int:
    """Return the category of `list_one` relative to `list_two`"""

    if list_one == list_two:
        return EQUAL

    len_one = len(list_one)
    len_two = len(list_two)

    if len_one == 0:
        return SUBLIST

    if len_two == 0:
        return SUPERLIST

    if len_one > len_two:
        for sub in nwise(list_one, len_two):
            if sub == list_two:
                return SUPERLIST
    elif len_one < len_two:
        for sub in nwise(list_two, len_one):
            if sub == list_one:
                return SUBLIST

    return UNEQUAL
