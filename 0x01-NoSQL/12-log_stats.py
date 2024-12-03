#!/usr/bin/env python3
"""
12-log_stats.py
This script retrieves statistics about Nginx logs from MongoDB.
"""

import pymongo
from pymongo import MongoClient


def log_nginx_stats(mongo_collection):
    """
    Provides statistics about Nginx logs stored in MongoDB.

    Returns:
    None
    """
    print('{} logs'.format(mongo_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(mongo_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))
    status_checks_count = len(list(
        mongo_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


def run():
    '''Provides some stats about Nginx logs stored in MongoDB.
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_nginx_stats(client.logs.nginx)


if __name__ == '__main__':
    run()
