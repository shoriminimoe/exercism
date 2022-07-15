"""Diffie-Hellman key exchange"""
import secrets


def private_key(p):
    """Return a random private key greater than 1 and less than p"""
    return 2 + secrets.randbelow(p-2)


def public_key(p, g, private):
    """Return a Diffie-Hellman public key"""
    return pow(g, private) % p


def secret(p, public, private):
    """Return a Diffie-Hellman secret"""
    return pow(public, private) % p
