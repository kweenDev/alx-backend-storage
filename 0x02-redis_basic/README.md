
# 0x02 Redis Basic

## Project Overview

This project dives into Redis, an in-memory data structure store, widely used as a database, cache, and message broker. You will explore Redis commands and implement Python functionalities that leverage Redis for basic operations, caching, and function call tracking. This project also covers implementing decorators to track function calls, storing lists in Redis, and setting up a simple expiring web cache.

## Learning Objectives

- Understand how to interact with Redis using Python.
- Learn to perform basic Redis operations: storing, retrieving, and manipulating data.
- Implement Redis as a caching system.
- Explore decorators in Python for tracking function calls and storing historical data.
  
## Technologies Used

- **Redis**: In-memory data structure store used for caching.
- **Python 3.7**: Primary language for interaction with Redis.
- **Pycodestyle**: Ensures code follows PEP 8 style guidelines.

## Requirements

- Files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files must end with a new line.
- A `README.md` file at the root of the project directory is mandatory.
- The first line of all Python files must be: `#!/usr/bin/env python3`.
- All code should follow `pycodestyle` guidelines.
- All functions, methods, and classes must include proper documentation.
- Type annotations are mandatory for all functions and coroutines.

## Installation

To install Redis and necessary Python dependencies, follow these steps:

1. Install Redis on Ubuntu 18.04:

   ```bash
   sudo apt-get -y install redis-server
    ```

2. Install the Redis Python client:

    ```bash
    pip3 install redis
    ```

3. Modify Redis configuration to bind to localhost:

    ```bash
    sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
    ```

4. Start the Redis server:

    ```bash
    service redis_server start
    ```

## Project Structure

- `exercise.py`: Core Python script implementing basic Redis operations.
- `web.py`: Script handling web caching and page tracking using Redis.

## Tasks Overview

### Task 0: **Writing Strings to Redis**

- **Description:** Create a `Cache` class that initializes a Redis client and implements a `store()` method to store data with a randomly-generated key.
- **Key Functionality:**
        - Store strings, bytes, int, or float in Redis
        - Returns a generated key for retrieval.

### Task 1: **Reading from Redis and Recovering Original Types**

- **Description:** Implement a `get()` method to retrieve data from Redis and an optional callable to convert the data to the original type.
- **Additional Methods:**
        - `get_str()` for strings.
        - `get_int` for integers.

### Task 2: ***Incrementing Values**

- **Description:** Implement a `count_calls` decorator to count how many times a method is called and store the count in Redis.
- **Key Functionality:**
        - Tracks method calls by storing the count in Redis using the method's qualified name.

### Task 3: **Storing Lists**

- **Description:** Implement a `call_history` decorator to store the history of function inputs and outputs in Redis.
- **Key Functionality:**
        - Inputs and outputs are stored as lists in Redis, with keys formatted using the function's qualified name.

### Task 4: **Retrieving Lists (Replay)**

- **Description:** Implement a `replay()` function to retrieve and display the call history of a function.
- **Key Functionality:**
        - Uses Redis lists to store and retrieve function inputs and outputs, displaying them in a human-readable format.

### Task 5: **Implementing an Expiring Web Cache (Advanced)**

- **Description:** Create a `get_page()` function to cache the result of a URL request for 10 seconds.
- **Key Functionality:**
        - Tracks the number of times a URL is accessed.
        - Caches the response for 10 seconds to avoid repeated requests.

## Usage

- **Running `exercise.py`**

    ```bash
    python3 exercise.py
    ```

### Examples

- **Store Data in Redis**

    ```python
    cache = Cache()
    data = b"hello"
    key = cache.store(data)
    print(key)
    print(cache.get(key))
    ```

- **Replay Function History**

    ```python
    cache = Cache()
    cache.store("foo")
    cache.store("bar")
    cache.store(42)
    replay(cache.store)
    ```

## Testing

- You can use the provided `main.py` scripts to test the functionality of the methods. Simply run:

    ```bash
    python3 main.py
    ```

## Author

- **Name:** Refiloe Radebe
- **Date:** 24 October 2024
