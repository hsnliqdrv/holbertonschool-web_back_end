#!/usr/bin/env python3
"""12-log_stats.py"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017')
    db = client.logs
    collection = db.nginx

    # Total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Status check (GET /status)
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")
