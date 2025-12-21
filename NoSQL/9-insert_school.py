#!/usr/bin/env python3
"""9-insert_school

Provides insert_school function
"""


def insert_school(mongo_collection, **kwargs):
    """Add function arguments as a document"""
    document = kwargs
    result = mongo_collection.insert_one(document)
    return result.inserted_id
