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
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    # Total count of logs
    total_logs = logs_collection.count_documents({})

    # Count for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: logs_collection.count_documents(
        {"method": method}) for method in methods}

    # Count for GET /status
    status_check = logs_collection.count_documents(
        {"method": "GET", "path": "/status"})

    # Output
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
