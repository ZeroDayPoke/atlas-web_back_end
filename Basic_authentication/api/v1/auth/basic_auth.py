#!/usr/bin/env python3
""" Basic authentication
"""
from .auth import Auth
import base64
from flask import request


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
