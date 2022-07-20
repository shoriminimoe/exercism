"""Isogram"""
import re
import string as string_mod


def is_isogram(string: str) -> bool:
    """Return True if `string` is an isogram"""
    stripped = re.sub(
        f"[{string_mod.punctuation}{string_mod.digits}{string_mod.whitespace}]",
        "",
        string.lower(),
    )
    return len(set(stripped)) == len(stripped)
