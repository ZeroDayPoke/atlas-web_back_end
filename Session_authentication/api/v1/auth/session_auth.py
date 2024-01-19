#!/usr/bin/env python3
""" Module of Session authentication views
"""
from .auth import Auth
import uuid


class SessionAuth(Auth):
    """session authentication class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user_id.
        """
        if user_id is None or type(user_id) is not str:
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
