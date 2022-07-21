"""Atbash Cipher"""
import re
import string

ENCODE_TABLE = str.maketrans(
    f"{string.ascii_lowercase}",
    f"{string.ascii_lowercase[::-1]}",
)
DECODE_TABLE = {v: k for k, v in ENCODE_TABLE.items()}


def encode(plain_text: str) -> str:
    """Encode `plain_text` using the Atbash cipher"""
    encoded = re.sub(
        f"[{string.punctuation}{string.whitespace}]",
        "",
        plain_text.lower(),
    ).translate(ENCODE_TABLE)
    return " ".join(encoded[i : i + 5] for i in range(0, len(encoded), 5))


def decode(ciphered_text: str) -> str:
    """Decode `ciphered_text` using the Atbash cipher"""
    return "".join(ciphered_text.split()).translate(DECODE_TABLE)
