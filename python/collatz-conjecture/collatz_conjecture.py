"""Collatz Conjecture"""


def steps(number):
    """Return number of steps to satisfy the Collatz Conjecture for `number`"""
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    steps = 0
    while number != 1:
        steps += 1
        if number % 2 == 0:
            number /= 2
        else:
            number = number * 3 + 1

    return steps
