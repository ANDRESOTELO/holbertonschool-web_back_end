#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
import uuid

from typing import Union

class Cache:
    """Cache Class"""
    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()


    def store(self, data: Union[Union[Union[str, int], float], bytes]) -> str:
        """
        Store method
        Returns -> Key
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
