#!/usr/bin/env python3
"""
Inserts a document in a collection based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection.
    Args:
        mongo_collection: pymongo collection object.
        **kwargs: key-value pairs representing document fields.
    Returns:
        The _id of the new document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
