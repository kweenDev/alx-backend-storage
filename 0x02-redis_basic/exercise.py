#!/usr/bin/env python3
"""exercise.py

A module for interacting with Redis NoSQL data storage. It provides a Cache
class to store and retrieve data, alongside utility decorators to track
method calls and their history.

Author: Refiloe Radebe
Date: October 24, 2024

Features:
- `Cache`: A class that interacts with Redis to store,
retrieve, and track data.
- `count_calls`: A decorator to count how many times a method is called.
- `call_history`: A decorator to track input/output of a method.
- `replay`: A function to display the call history of a method.

Redis is used for data persistence, and the module supports
storing different data types such as strings, bytes, integers,
and floats.
"""

import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union


def count_calls(method: Callable) -> Callable:
    """
    A decorator that tracks the number of times a method is called.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: A wrapped method that increments a call
        counter before invocation.
    """
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """
        Increments the call counter for the method and then invokes it.

        Args:
            self: The Cache instance.
            *args: Positional arguments passed to the method.
            **kwargs: Keyword arguments passed to the method.

        Returns:
            Any: The result from the original method.
        """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return invoker


def call_history(method: Callable) -> Callable:
    """
    A decorator that logs the input arguments and output of a method call.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: A wrapped method that logs inputs and
        outputs before invocation.
    """
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """
        Logs the input and output of the method in Redis storage.

        Args:
            self: The Cache instance.
            *args: Positional arguments passed to the method.
            **kwargs: Keyword arguments passed to the method.

        Returns:
            Any: The result from the original method.
        """
        in_key = f'{method.__qualname__}:inputs'
        out_key = f'{method.__qualname__}:outputs'
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_key, output)
        return output
    return invoker


def replay(fn: Callable) -> None:
    """
    Displays the history of calls made to a method,
    including inputs and outputs.

    Args:
        fn (Callable): The method whose history is to be displayed.

    Output:
        None: Prints the call history, including
        method inputs and outputs, to the console.
    """
    if fn is None or not hasattr(fn, '__self__'):
        return
    redis_store = getattr(fn.__self__, '_redis', None)
    if not isinstance(redis_store, redis.Redis):
        return

    fxn_name = fn.__qualname__
    in_key = f'{fxn_name}:inputs'
    out_key = f'{fxn_name}:outputs'

    # Fetching the call count and details from Redis
    fxn_call_count = int(redis_store.get(fxn_name)
                         ) if redis_store.exists(fxn_name) != 0 else 0
    print(f'{fxn_name} was called {fxn_call_count} times:')

    fxn_inputs = redis_store.lrange(in_key, 0, -1)
    fxn_outputs = redis_store.lrange(out_key, 0, -1)

    # Displaying each input-output pair
    for fxn_input, fxn_output in zip(fxn_inputs, fxn_outputs):
        print(f'{fxn_name}(
              *{fxn_input.decode("utf-8")}) -> {fxn_output.decode(
                  "utf-8")}')


class Cache:
    """
    Represents a caching system using Redis for data persistence.

    Attributes:
        _redis (redis.Redis): Redis connection object for
        storing and retrieving data.
    """

    def __init__(self) -> None:
        """
        Initializes the Cache instance with a Redis connection.

        This also clears the Redis database to ensure a clean
        slate for storage.
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis and returns a unique key associated with it.

        The method is decorated with `call_history` and
        `count_calls` to log usage
        and track the number of calls.

        Args:
            data (Union[str, bytes, int, float]): The data to be
            stored in Redis.

        Returns:
            str: A unique key identifying the stored data.
        """
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key

    def get(self, key: str, fn: Callable = None) -> Union[
            str, bytes, int, float]:
        """
        Retrieves data from Redis based on a provided key and
        optionally transforms it.

        Args:
            key (str): The key associated with the data in Redis.
            fn (Callable, optional): A function that transforms the
            data before returning it.

        Returns:
            Union[str, bytes, int, float]: The retrieved data,
            optionally transformed by `fn`.
        """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """
        Retrieves a string value from Redis based on the provided key.

        Args:
            key (str): The key associated with the string data in Redis.

        Returns:
            str: The retrieved string data.
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        Retrieves an integer value from Redis based on the provided key.

        Args:
            key (str): The key associated with the integer data in Redis.

        Returns:
            int: The retrieved integer data.
        """
        return self.get(key, lambda x: int(x))
