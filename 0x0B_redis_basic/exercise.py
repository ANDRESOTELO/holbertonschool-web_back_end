#!/usr/bin/env python3
"""
Writing strings to Redis
"""
from functools import wraps
import redis
from uuid import uuid4
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """
    Counts how many times a method in the class is called
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper for decorator
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """Cache Class"""
    def __init__(self):
        """Constructor Method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store method
        Returns -> Key
        """
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key


    def get(self, key: str,
        fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Get method that take a key string and
        convert to original type
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value


    def get_str(self, key: str) -> str:
        """
        Automatically parametrize Cache.get to str
        """
        value = self._redis.get(key)
        return value.decode('utf-8')


    def get_int(self, key: str) -> int:
        """
        Automatically parametrize Cache.get to int
        """
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value
