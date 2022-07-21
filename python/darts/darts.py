"""Darts"""
import math
from typing import Union


def score(x: Union[int, float], y: Union[int, float]) -> int:
    """Returns a dart score given an (x, y) position"""
    radius = math.hypot(x, y)

    if radius <= 1:
        return 10

    if radius <= 5:
        return 5

    if radius <= 10:
        return 1

    return 0
