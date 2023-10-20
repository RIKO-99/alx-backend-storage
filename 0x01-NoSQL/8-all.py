#!/usr/bin/env python3
"""8-all module."""


from typing import List, Dict, Union, Any


def list_all(mongo_collection: Dict[str, str]) -> List[Dict[str, str]]:
    """list_all function."""
    return list(mongo_collection.find())
