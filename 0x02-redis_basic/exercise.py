#!/usr/bin/env python3
"""exercise module implementation of redis inmemory datastore
       - writing strings to redis
       - Reading from redis and recovering original type
       - incrementing values
       - storing and retrieving lists ."""


import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def call_history(method: Callable) -> Callable:
    """Store the history of inputs and outputs for a particular function.

    Args:
        method (Callable): The function to be wrapped.

    Returns:
        Callable: The wrapped function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = f'{method.__qualname__}:inputs'
        outputs_key = f'{method.__qualname__}:outputs'
        self._redis.rpush(inputs_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(output))
        return output
    return wrapper


def count_calls(method: Callable) -> Callable:
    """Take a function and return a function that counts how many\
        times the function was called.
    Args:
        method (Callable): The function to be wrapped.
    Returns:
        Callable: The wrapped function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Simulates the Caching of redis keys. Creates a new connection\
        everytime an instance of this class is created, saves the\
            keys temporalily, and deletes the keys when the execution of\
                the instance stops.
    """

    def __init__(self):
        """Instantiates a new connection to redis. Flushes the redis\
            server once connection terminates.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key and stores the data in the redis\
            server.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The key generated.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable
            = None) -> Union[str, bytes, int, float]:
        """Used to convert data back to desired format."""
        newkey = self._redis.get(key)
        if fn:
            return fn(newkey)
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """Converts data to UTF-8 format."""
        if key:
            return self.get(
                key, lambda d: d.decode("utf-8")
            )

    def get_int(self, key: str) -> int:
        """Converts data to integer format."""
        if key:
            return self.get(
                key, lambda d: int(d.decode("utf-8"))
            )
