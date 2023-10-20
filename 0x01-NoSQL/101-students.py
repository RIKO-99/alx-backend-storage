#!/usr/bin/env python3
"""101-students module."""


def top_students(mongo_collection):
    """Return all students sorted by average score."""

    return mongo_collection.aggregate([
        {"$unwind": "$topics"},
        {"$group": {
            "_id": "$_id",
            "name": {"$first": "$name"},
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
