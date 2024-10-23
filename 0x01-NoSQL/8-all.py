#!/usr/bin/env python3
"""
List all documents in the collection.
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    Args:
        mongo_collection: pymongo collection object.
    Returns:
        List of documents or an empty list if no documents are found.
    """
    return list(mongo_collection()) or []
