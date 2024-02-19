#!/usr/bin/env python3
"""auth module"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """return a salted hash of the input password"""
    return bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())