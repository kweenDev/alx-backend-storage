#!/usr/bin/env python3
"""
12-log_stats.py
This script retrieves statistics about Nginx logs from MongoDB.
"""

from pymongo import MongoClient


def log_stats():
    """
    Retrieves and displays statistics from the Nginx logs stored in MongoDB.
    """
    try:
        client = MongoClient('mongodb://127.0.0.1:27017')
        logs_collection = client.logs.nginx

        # Count total documents
        total = logs_collection.count_documents({})

        # Count documents by method
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        method_counts = {method: logs_collection.count_documents(
            {"method": method}) for method in methods}

        # Count specific GET requests for /status
        status_checks = logs_collection.count_documents(
            {"method": "GET", "path": "/status"})

        # Display statistics
        print(f"{total} logs")
        print("Methods:")
        for method in methods:
            print(f"\tmethod {method}: {method_counts[method]}")
        print(f"{status_checks} status check")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    log_stats()
