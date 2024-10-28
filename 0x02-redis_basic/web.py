#!/usr/bin/env python3
"""
web.py

A module for caching HTTP request data and tracking the number of requests
to each URL using Redis.

Author: Refiloe Radebe
Date: October 24, 2024
"""

import redis
import requests
from functools import wraps
from typing import Callable

# Redis instance for caching and request tracking
redis_store = redis.Redis()


def data_cacher(method: Callable) -> Callable:
    """
    A decorator to cache a method's output and track URL request counts.

    Args:
        method (Callable): The function to be decorated for caching and
        counting.

    Returns:
        Callable: A wrapped function that tracks request count and caches
        responses.
    """
    @wraps(method)
    def invoker(url: str) -> str:
        # Increment the request count for the URL
        request_count_key = f'count:{url}'
        result_key = f'result:{url}'

        # Increment counter each time URL is accessed
        redis_store.incr(request_count_key)

        # Check if the response is cached
        cached_result = redis_store.get(result_key)
        if cached_result:
            return cached_result.decode('utf-8')

        # Fetch the data if not cached
        result = method(url)

        # Cache the result with a 10-second expiration
        redis_store.setex(result_key, 10, result)
        return result

    return invoker


@data_cacher
def get_page(url: str) -> str:
    """
    Fetches and caches content from a URL.

    Args:
        url (str): The URL to fetch content from.

    Returns:
        str: The fetched content, either cached or freshly retrieved.
    """
    return requests.get(url).text
