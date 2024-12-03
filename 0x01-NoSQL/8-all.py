#!/usr/bin/env python3
"""
List all documents in the collection.
"""

import pymongo


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    Args:
        mongo_collection: pymongo collection object.
    Returns:
        List of documents or an empty list if no documents are found.
    """
    if not mongo_collection:
        return []
    docs = mongo_collection.find()
    return list(mongo_collection()) or [doc for doc in docs]
