#!/usr/bin/env python3
""" Basic authentication
"""
from .auth import Auth
import base64
from flask import request
from typing import TypeVar
from models.user import User


UserType = TypeVar('UserType', bound=User)


class BasicAuth(Auth):
    """basic auth class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extracts the Base64 part of the Authorization header."""
        if authorization_header is None or \
           not isinstance(authorization_header, str) or \
           not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(self,
                                           b64_auth_header: str) -> str:
        """Decodes a Base64 string."""
        if b64_auth_header is None or \
           not isinstance(b64_auth_header, str):
            return None

        try:
            base64_bytes = b64_auth_header.encode('utf-8')
            decoded_bytes = base64.b64decode(base64_bytes)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 dec_b64_auth_header: str) -> (str, str):
        """Extracts user email and password from the Base64 decoded value."""
        if dec_b64_auth_header is None or \
           not isinstance(dec_b64_auth_header, str) or \
           ':' not in dec_b64_auth_header:
            return None, None

        email, password = dec_b64_auth_header.split(':', 1)
        return email, password

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> UserType:
        """Return the User instance based on email and password."""
        if user_email is None or not isinstance(user_email, str) or \
           user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})
            if not users:
                return None

            user = users[0]

            if user.is_valid_password(user_pwd):
                return user
            else:
                return None
        except Exception:
            return None

    def current_user(self, request=None) -> UserType:
        """Retrieves the User instance for a request."""
        if request is None:
            return None

        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_auth_header = self.extract_base64_authorization_header(
            auth_header)
        if base64_auth_header is None:
            return None

        decoded_base64_auth_header = self.decode_base64_authorization_header(
            base64_auth_header)
        if decoded_base64_auth_header is None:
            return None

        user_email, user_pwd = self.extract_user_credentials(
            decoded_base64_auth_header)
        if user_email is None or user_pwd is None:
            return None

        return self.user_object_from_credentials(user_email, user_pwd)
