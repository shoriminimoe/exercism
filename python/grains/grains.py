"""Calculate grains of wheat on a chessboard"""


def square(number):
    """Return the number of grains of wheat on a given square

    :param number: int - The square on the chessboard to calculate grains on
    :return: int - the number of wheat grains on the given square
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    if number == 1:
        return 1

    return 2 * square(number - 1)


def total():
    """Return the total number of grains of wheat on a chessboard"""
    return sum(square(i + 1) for i in range(64))
