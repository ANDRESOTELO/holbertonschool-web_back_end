#!/usr/bin/env python3
"""
Insert a document in Python
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a document in Python
    """
    new_insert = mongo_collection.insert_one(kwargs)
    _id = new_insert.inserted_id
    return _id
