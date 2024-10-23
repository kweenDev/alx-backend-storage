#!/usr/bin/env python3
"""
101-students.py
This script contains a function that retrieves top students sorted by
average score.
"""


def top_students(mongo_collection):
    """
    Finds and returns all students sorted by their average score.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The MongoDB
    collection object

    Returns:
    list: A list of students sorted by average score with
    'averageScore' included
    """
    pipeline = [
        {"$project": {
            "name": 1,
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ]
    return list(mongo_collection.aggregate(pipeline))
