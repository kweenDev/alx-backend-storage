#!/usr/bin/env python3
"""
11-schools_by_topic.py
This script contains a function that fetches schools based on a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Finds all schools that cover a specific topic.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The MongoDB
    collection object
    topic (str): The topic to search for

    Returns:
    list: A list of schools that cover the specified topic
    """
    return mongo_collection.find({"topics": topic})
