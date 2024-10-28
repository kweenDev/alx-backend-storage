#!/usr/bin/env python3
"""
web.py

A module that provides tools for caching HTTP request data and tracking
the number of times a URL has been requested using Redis.

Author: Refiloe Radebe
Date: October 24, 2024
"""

import redis
import requests
from functools import wraps
from typing import Callable

# Module-level Redis instance for caching and tracking purposes
redis_store = redis.Redis()


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
        request_count_key = f'count:{url}'
        result_key = f'result:{url}'

        # Increment the counter for the number of calls made to the URL
        redis_store.incr(request_count_key)

        # Check if the URL response is already cached
        cached_result = redis_store.get(result_key)
        if cached_result:
            return cached_result.decode('utf-8')

        # Fetch the data from the URL if not cached
        result = method(url)

        # Cache the result with a 10-second expiration
        redis_store.setex(result_key, 10, result)
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
