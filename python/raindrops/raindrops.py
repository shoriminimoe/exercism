"""Raindrops"""


def convert(number: int) -> str:
    """Return the raindrop sound for number"""
    sound = ""

    if number % 3 == 0:
        sound = f"{sound}Pling"

    if number % 5 == 0:
        sound = f"{sound}Plang"

    if number % 7 == 0:
        sound = f"{sound}Plong"

    return sound if sound else str(number)
