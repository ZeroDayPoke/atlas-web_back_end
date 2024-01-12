#!/usr/bin/env python3
"""Auth class for the API."""
from flask import request
from typing import List, TypeVar


class Auth:
    """auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determines if authentication is required for a given path."""
        if path is None or not excluded_paths:
            return True

        path = path + '/' if not path.endswith('/') else path

        return not any(ep == path for ep in excluded_paths)

    def authorization_header(self, request=None) -> str:
        """Retrieves the Authorization header from a Flask request object."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current user from a Flask request object."""
        return None
