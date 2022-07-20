"""ISBN Verifier"""
import re
from itertools import cycle


def is_valid(isbn: str) -> bool:
    """Return True if `isbn` is a valid ISBN-10 number

    Spaces and dashes "-" in `isbn` are ignored
    """
    digits = re.sub(r"[\s-]", "", isbn)
    if not re.fullmatch(r"\d{9}[\dxX]", digits):
        return False
    check_value = 10 if digits[-1] in ("x", "X") else int(digits[-1])
    total = check_value + sum(
        int(digit) * factor
        for factor, digit in enumerate(reversed(digits[:-1]), start=2)
    )
    return total % 11 == 0


def isbn10_to_isbn13(isbn10: str) -> str:
    """Convert the ISBN-10 string `isbn10` to an ISBN-13 string

    :param isbn10: str - An ISBN-10 number to convert
    :return: str - `isbn10` as an ISBN-13 number
    """
    if not is_valid(isbn10):
        raise ValueError(f"invalid ISBN-10 number: '{isbn10}'")
    digits = isbn10.replace("-", "")[:-1]
    # 9*1 + 7*3 + 8*1 = 38
    total = 38 + sum(
        int(digit) * factor for factor, digit in zip(cycle((3, 1)), digits)
    )
    check_digit = (10 - (total % 10)) % 10
    return f"978{digits}{check_digit}"
