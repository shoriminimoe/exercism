"""Rotational cipher"""
import string

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase


def rotate(text: str, key: int) -> str:
    """Return `text` translated using the rotational cipher value `key`

    :param text: str - Text to rotate
    :param key: int - Shift value
    :return: str - text rotated by key
    """
    translation_table = str.maketrans(
        f"{LOWER}{UPPER}",
        f"{LOWER[key:]}{LOWER[:key]}{UPPER[key:]}{UPPER[:key]}",
    )
    return text.translate(translation_table)
