#!/usr/bin/env python3
"""
10-update_topics.py
This script contains a function that updates school topics based on school name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Update all topics of a school document based on the name.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The MongoDB collection object
    name (str): The school name to update
    topics (list): A list of new topics to set for the school

    Returns:
    None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
