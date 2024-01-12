#!/usr/bin/env python3
"""password encryption module presumably"""


import bcrypt


def hash_password(password: str) -> bytes:
    """Hash a password for storing."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
