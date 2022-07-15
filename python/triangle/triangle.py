"""Trangles"""


def is_triangle(sides):
    """Return True if `sides` represents a valid triangle"""
    if any(s <= 0 for s in sides):
        return False
    return (
        sides[0] + sides[1] >= sides[2]
        and sides[1] + sides[2] >= sides[0]
        and sides[0] + sides[2] >= sides[1]
    )


def equilateral(sides):
    """Return True if `sides` represents an equilateral triangle"""
    return is_triangle(sides) and sides[0] == sides[1] == sides[2]


def isosceles(sides):
    """Return True if `sides` represents an isosceles triangle"""
    return is_triangle(sides) and (sides[0] in sides[1:] or sides[2] in sides[:2])


def scalene(sides):
    """Return True if `sides` represents an scalene triangle"""
    return (
        is_triangle(sides) and sides[0] not in sides[1:] and sides[2] not in sides[:2]
    )


def degenerate(sides):
    """Return True if `sides` represents a degenerate triangle"""
    return is_triangle(sides) and (
        sides[0] + sides[1] == sides[2]
        or sides[1] + sides[2] == sides[0]
        or sides[0] + sides[2] == sides[1]
    )
