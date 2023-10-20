#!/usr/bin/env python3
"""11-schools_by_topic module."""


def schools_by_topic(mongo_collection, topic: str):
    """
    schools_by_topic: returns the list of school having a specific topic.

    Args:
        mongo_collection (dict[str, str]): pymongo collection object.
        topic (str): topic searched.

    Returns:
        List[Dict[str, str]]: list of school having the topic.
    """
    return mongo_collection.find({"topics": topic})
