#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """Cache Class"""
    def __init__(self):
        """Constructor Method"""
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store method
        Returns -> Key
        """
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key
