#!/usr/bin/env python3
"""
Class to validate user attributes
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import User
from db import DB
import uuid
import bcrypt


def _hash_password(password: str) -> str:
    """
    Takes password as an argument and returns a hashed_password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
