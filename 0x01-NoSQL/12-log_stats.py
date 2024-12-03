#!/usr/bin/env python3
"""
12-log_stats.py
This script retrieves statistics about Nginx logs from MongoDB.
"""

import pymongo
from pymongo import MongoClient


if __name__ == "__main__":
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    ng = client.logs.nginx
    print(f"{ng.count_documents({})} logs")
    print("Methods:")
    for met in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print("\tmethod {}: {}".format(met, ng.count_documents({
            "method": met
        })))
    print("{} status check".format(ng.count_documents(
        {"$and": [{"method": "GET"}, {"path": "/status"}]})))
