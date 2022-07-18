"""Pig Latin"""
import string

vowels = ("a", "e", "i", "o", "u")
consonants = tuple(frozenset(string.ascii_lowercase) - frozenset(vowels))


def translate(text: str) -> str:
    """Return `text` translated to Pig Latin"""
    translated_words = []
    for word in text.split():
        consonant_prefix = ""
        for char in word:
            consonant_prefix = f"{consonant_prefix}{char}"

            # Rule 1 - Special case for "xr" and "yt" as vowel sounds
            if consonant_prefix in ("xr", "yt"):
                consonant_prefix = ""
                break

            # Rule 3 - Stop processing if the prefix ends with "qu"
            if consonant_prefix.endswith("qu"):
                break

            # Rule 1/2 - Stop processing when a vowel is reached
            # Rule 4 - Special case for "y" following leading consonants
            if char in vowels or char == "y" != consonant_prefix:
                consonant_prefix = consonant_prefix[:-1]
                break

        translated_words.append(f"{word[len(consonant_prefix):]}{consonant_prefix}ay")

    return " ".join(translated_words)
