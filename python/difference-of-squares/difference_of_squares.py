"""Difference of squares"""


def square_of_sum(number):
    """Return the square of the sum of the natural numbers counting up to number"""
    return pow(sum(num + 1 for num in range(number)), 2)


def sum_of_squares(number):
    """Return the sum of the squares of the natural numbers counting up to number"""
    return sum(pow(num + 1, 2) for num in range(number))


def difference_of_squares(number):
    """Return the difference of the square of the sum and the sum of squares of number"""
    return square_of_sum(number) - sum_of_squares(number)
