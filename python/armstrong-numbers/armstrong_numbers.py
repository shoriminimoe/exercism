"""Is this an Armstrong number?"""


def is_armstrong_number(number):
    """Return True if number is an Armstrong number

    :param number: int - The integer to test
    :return: bool - Whether number is an Armstrong number
    """
    digits = [int(digit) for digit in str(number)]
    exponent = len(digits)
    return sum(pow(digit, exponent) for digit in digits) == number
