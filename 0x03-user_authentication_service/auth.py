#!/usr/bin/env python3
""" auth module  """

import bcrypt
from db import DB
from user import User
import uuid

def _hash_password(password: str) -> bytes:
    """ returns a passwd hash """
    hashed_password = bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt(4))
    return hashed_password
