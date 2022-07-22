"""Flatten array"""


def flatten(iterable) -> list:
    """Return arbitrarily nested `iterable` as a flat array"""
    result = []
    for item in iterable:
        if item is None:
            continue

        if isinstance(item, list):
            result += flatten(item)
            continue

        result.append(item)
    return result
