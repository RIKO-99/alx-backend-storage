#!/usr/bin/env python3
"""9-insert_school module."""

from typing import Dict, Any


def insert_school(mongo_collection: Dict[str, str], **kwargs: Any) -> str:
    """insert_school function."""
    new_obj = mongo_collection.insert_one(kwargs)
    return new_obj.inserted_id
