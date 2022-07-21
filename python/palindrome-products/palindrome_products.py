"""palindrome products"""
from itertools import combinations_with_replacement


def largest(*, min_factor: int = 0, max_factor: int):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    value = None
    factor_list = []
    for factors in combinations_with_replacement(
        range(max_factor, min_factor - 1, -1), 2
    ):
        product = factors[0] * factors[1]
        if value is not None and product < value:
            continue
        product_str = str(product)
        if product_str == product_str[::-1]:
            if product != value:
                factor_list = []
            factor_list.append(factors)
            value = product

    return value, factor_list


def smallest(*, min_factor: int = 0, max_factor: int):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    value = None
    factor_list = []
    for factors in combinations_with_replacement(range(min_factor, max_factor + 1), 2):
        product = factors[0] * factors[1]
        if value is not None and product > value:
            continue
        product_str = str(product)
        if product_str == product_str[::-1]:
            if product != value:
                factor_list = []
            factor_list.append(factors)
            value = product

    return value, factor_list
