"""Scoring for the Yacht dice game"""
from collections import Counter
from typing import Union

# Score categories.
# Change the values as you see fit.
YACHT = "YACHT"
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT_1"
BIG_STRAIGHT = "BIG_STRAIGHT_2"
CHOICE = "CHOICE"


def score(dice: list[int], category: Union[str, int]) -> int:
    """Returns the Yacht score for the given `category` and `dice`

    :param dice: list[int] - A list of integers representing the dice rolls
    :param category: Union[str, int] - The Yacht scoring category
    :return: int - The score for the roll
    """
    if len(dice) != 5 or max(dice) > 6 or min(dice) < 1:
        raise ValueError(f"invalid dice: {dice}")

    roll_score = 0
    counts = Counter(dice)

    if category == "YACHT":
        _, count = counts.most_common(1)[0]
        if count == 5:
            roll_score = 50

    elif category in (1, 2, 3, 4, 5, 6):
        roll_score = category * counts[category]

    elif category == "FULL_HOUSE":
        # If there is a full house in the dice, there will be exactly 2 unique
        # values in the set.
        _, count = counts.most_common(1)[0]
        if len(set(dice)) == 2 and count in (2, 3):
            roll_score = sum(dice)

    elif category == "FOUR_OF_A_KIND":
        # If there is a four-of-a-kind in the dice, there will be at most 2
        # unique values in the set.
        value, count = counts.most_common(1)[0]
        if len(set(dice)) <= 2 and count >= 4:
            roll_score = 4 * value

    elif category in ("LITTLE_STRAIGHT_1", "BIG_STRAIGHT_2"):
        offset = int(category[-1])
        if all(d+offset in dice for d in range(5)):
            roll_score = 30

    elif category == "CHOICE":
        roll_score = sum(dice)

    else:
        raise ValueError(f"invalid category: '{category}'")

    return roll_score
