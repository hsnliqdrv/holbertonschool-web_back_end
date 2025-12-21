#!/usr/bin/env python3
"""10-update_topics.py"""


def update_topics(mongo_collection, name, topics):
    """Updates all topics of a school document based on the name."""
    mongo_collection.update_one(
        {"name": name},     # Filter: find document by name
        {"$set": {"topics": topics}}  # Update: set the topics field
    )
