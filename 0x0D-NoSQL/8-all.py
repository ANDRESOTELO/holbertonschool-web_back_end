#!/usr/bin/env python3
"""
List all documents from mongo using Python
"""


def list_all(mongo_collection):
    """
    List all documents from mongo using Python
    """

    documents = mongo_collection.find()
    if documents is not None:
        return list(documents)
    return []
