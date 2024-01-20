#!/usr/bin/env python3
"""auth module"""
import bcrypt
from db import DB
from user import User
import uuid


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a user with the provided email and password.
        """
        user = self._db.find_user_by(email=email)
        if user:
            raise ValueError(f"User {email} already exists")

        hashed_password = self._hash_password(password)
        new_user = self._db.add_user(email, hashed_password)
        return new_user

    def _hash_password(self, password: str) -> bytes:
        """
        Hash a password for storing.
        """
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate user login.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user and bcrypt.checkpw(
                    password.encode('utf-8'), user.hashed_password):
                return True
        except Exception:
            pass
        return False

    def create_session(self, email: str) -> str:
        """
        Create a session ID for a user with the given email.
        """
        user = self._db.find_user_by(email=email)
        if user:
            session_id = str(uuid.uuid4())
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        return None

    def get_user_from_session_id(self, session_id: str):
        """
        Get a user from a session ID.
        """
        if session_id is None:
            return None
        user = self._db.find_user_by(session_id=session_id)
        return user

def _hash_password(self, password: str) -> bytes:
    """
    Hash a password for storing.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    Generate a new UUID and return its string representation.
    """
    return str(uuid.uuid4())
