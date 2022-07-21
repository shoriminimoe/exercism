"""Perfect numbers"""
from typing import Set


def factor(number: int) -> Set[int]:
    """Return the factors of number

    Blunt force style
    """
    factors = {1}
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            factors.add(i)
    return factors


def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0 or not isinstance(number, int):
        raise ValueError("Classification is only possible for positive integers.")

    aliquot = sum(factor(number))

    if aliquot < number or aliquot == 1:
        return "deficient"

    if aliquot > number:
        return "abundant"

    return "perfect"
