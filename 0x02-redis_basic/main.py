#!/usr/bin/env python3
"""
main.py - Test script for Redis caching system.
"""

from exercise import Cache, replay
import time

if __name__ == "__main__":
    # Initialize Cache instance
    cache = Cache()

    print("\n--- Test: Storing and Retrieving Data ---")
    # Store some data and get the key
    key = cache.store("Hello, Redis!")
    print(f"Stored data under key: {key}")

    # Retrieve the stored data
    data = cache.get(key)
    print(f"Retrieved data: {data.decode('utf-8')}")

    print("\n--- Test: Count Calls Decorator ---")
    # Test count_calls decorator

    @cache.count_calls
    def test_func():
        return "Function called!"

    # Call the function multiple times
    test_func()
    test_func()
    test_func()

    # Check how many times it was called
    print(
        f"test_func was called {cache.get_int(
            f'{test_func.__qualname__}:calls')} times.")

    print("\n--- Test: Call History Decorator ---")
    # Test call_history decorator

    @cache.call_history
    def add(a, b):
        return a + b

    # Call the function
    add(3, 5)
    add(10, 20)

    # Replay the function history
    replay(add)

    print("\n--- Test: Expiring Web Cache ---")
    from web import get_page

    # Fetch a webpage (this should cache the result)
    url = "http://example.com"
    print(f"Fetching {url} ...")
    page_content = get_page(url)
    print(f"Page content (truncated): {page_content[:100]}")

    # Wait for 10 seconds before fetching again (to test the cache expiration)
    print("Waiting 10 seconds...")
    time.sleep(10)

    # Fetch the page again (this should retrieve from
    # cache if within expiration, or re-fetch otherwise)
    print(f"Re-fetching {url} ...")
    page_content = get_page(url)
    print(f"Page content (truncated): {page_content[:100]}")
