#!/usr/bin/env python3
"""module for the class SessionAuth"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """SessionAuth class for session-based authentication."""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a new session for the given user."""
        if not user_id or type(user_id) != str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Retrieves user id from session id"""
        if not session_id or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id, None)
