"""All your base"""
from typing import List


def rebase(input_base: int, digits: List[int], output_base: int) -> List[int]:
    """Return a list of integers in `output_base` starting with `digits` in `input_base`"""
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if not all(0 <= d < input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    output_digits = []

    quotient = sum(
        digit * input_base**exponent
        for exponent, digit in enumerate(reversed(digits))
    )

    while quotient >= output_base:
        quotient, remainder = divmod(quotient, output_base)
        output_digits.insert(0, remainder)

    output_digits.insert(0, quotient)

    return output_digits
