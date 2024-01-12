#!/usr/bin/env python3
"""password encryption module presumably"""


import bcrypt


def hash_password(password: str) -> bytes:
    """Hash a password for storing."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if a provided password matches the hashed password."""
    return bcrypt.checkpw(password.encode(), hashed_password)
