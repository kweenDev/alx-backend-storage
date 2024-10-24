#!/usr/bin/env python3
"""
web.py

A module that provides tools for caching HTTP request data and tracking
the number of times a URL has been requested using Redis.

Author: Your Name
Date: October 24, 2024

Features:
- `data_cacher`: A decorator that caches HTTP request responses and tracks
  the number of requests made to a specific URL.
- `get_page`: A function that fetches the content of a URL, using caching
  and request tracking to optimize repeated requests.

The Redis instance stores both the cached responses and the number of times
each URL has been requested, preventing unnecessary network calls.
"""

import redis
import requests
from functools import wraps
from typing import Callable


# Module-level Redis instance for caching and tracking purposes
redis_store = redis.Redis()
"""The Redis instance used for caching URL responses and tracking URL requests."""


def data_cacher(method: Callable) -> Callable:
    """
    A decorator that caches the output of a method and tracks URL requests.

    The decorator increments the request count for a URL and caches the
    response for a set amount of time to optimize repeated calls to the same
    URL.

    Args:
        method (Callable): The function to be decorated, typically fetching
        the content of a URL.

    Returns:
        Callable: A wrapped function that caches the response and tracks the
        number of times the URL has been requested.
    """
    @wraps(method)
    def invoker(url: str) -> str:
        """
        Tracks the number of requests and caches the result of the method.

        For each URL request:
        - The request count is incremented.
        - The response is fetched from Redis if cached.
        - If not cached, the result is fetched from the URL and stored with an
          expiration time.

        Args:
            url (str): The URL to fetch data from.

        Returns:
            str: The cached response or the fresh content of the URL.
        """
        # Increment the request count for the URL
        redis_store.incr(f'count:{url}')

        # Check if the URL response is cached in Redis
        cached_result = redis_store.get(f'result:{url}')
        if cached_result:
            return cached_result.decode('utf-8')

        # If not cached, fetch the result and cache it
        result = method(url)
        # Cache expires in 10 seconds
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    """
    Fetches the content of a given URL and caches the response.

    The function tracks how many times a particular URL has been requested
    and caches the result to avoid redundant requests.

    Args:
        url (str): The URL from which to fetch the content.

    Returns:
        str: The content of the URL, either cached or freshly fetched.
    """
    return requests.get(url).text
