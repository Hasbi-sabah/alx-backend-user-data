#!/usr/bin/env python3
"""auth module"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """return a salted hash of the input password"""
    return bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        """Initialize a new instance of DB"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with the provided email and password."""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            user = self._db.add_user(email, _hash_password(password))
        else:
            raise ValueError(f"User {email} already exists")
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate user login credentials."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode("utf-8"), user.hashed_password)
