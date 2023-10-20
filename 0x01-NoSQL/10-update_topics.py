#!/usr/bin/env python3
"""10-update_topics module."""


from typing import List, Dict


def update_topics(
        mongo_collection, name: str, topics: List[str]):
    """
    update_topics: changes all topics of a school document based on the name.

    Args:
        mongo_collection (dict[str, str]): pymongo collection object.
        name (str): school name to update.
        topics (List[str]): list of topics approached in the school.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}})
