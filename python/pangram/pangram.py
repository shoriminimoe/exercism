"""Pangram"""
import string


def is_pangram(sentence):
    """Returns True if `sentence` is a pangram"""
    sentence_lower = sentence.lower()
    return all(x in sentence_lower for x in string.ascii_lowercase)
