"""Gigasecond module"""
from datetime import datetime, timedelta

GIGASECOND = timedelta(seconds=1_000_000_000)


def add(moment: datetime):
    """Add 1 gigasecond to `moment`

    :param moment: datetime - Time to add the gigasecond to.
    :return: A datetime object representing 1 gigasecond after `moment`
    """
    return moment + GIGASECOND
