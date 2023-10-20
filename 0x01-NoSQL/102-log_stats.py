#!/usr/bin/env python3
""" 12-log_stats module."""


#import the mongo client
from pymongo import MongoClient

#connect to the mongo client
client = MongoClient('mongodb://localhost:27017/')
#create a variable for the logs collection. This is the collection instance
logs = client.logs.nginx


def get_logs_summary():
    """Get logs summary."""

    print(f'{logs.count_documents({})} logs')
    print('Methods:')
    print(f'\tmethod GET: {logs.count_documents({"method": "GET"})}')
    print(f'\tmethod POST: {logs.count_documents({"method": "POST"})}')
    print(f'\tmethod PUT: {logs.count_documents({"method": "PUT"})}')
    print(f'\tmethod PATCH: {logs.count_documents({"method": "PATCH"})}')
    print(f'\tmethod DELETE: {logs.count_documents({"method": "DELETE"})}')
    print(f'{logs.count_documents({"path": "/status"})} status check')
    print('IPs:')
    for ip in logs.aggregate([{"$group": {"_id": "$ip", "count": {"$sum": 1}}}, {"$sort": {"count": -1}}, {"$limit": 10}]):
        print(f'\t{ip.get("_id")}: {ip.get("count")}')


if __name__ == '__main__':
    get_logs_summary()
client.close()
