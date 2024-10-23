#!/usr/bin/env python3
"""
102-log_stats.py
This script logs statistics for Nginx logs in a MongoDB collection.
"""

from pymongo import MongoClient


def log_stats():
    """Log the stats from the Nginx logs"""
    # Connect to the MongoDB server
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs  # Access the 'logs' database
    collection = db.nginx  # Access the 'nginx' collection

    # Count total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Count HTTP methods
    methods_count = {}
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        methods_count[method] = collection.count_documents({"method": method})

        print("Methods:")
        for method, count in methods_count.items():
            print(f"\tmethod {method}: {count}")

    # Count status checks
    status_check_count = collection.count_documents({"status": 200})
    print(f"{status_check_count} status check")

    # Count top 10 IPs
    ip_count = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    print("IPs:")
    for ip in ip_count:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    log_stats()
