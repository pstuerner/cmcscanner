import os
import random
from pymongo import MongoClient
from coinmarketcapapi import CoinMarketCapAPI
from datetime import datetime as dt

MONGO_USER = os.environ['MONGO_USER']
MONGO_USER_PASSWD = os.environ['MONGO_USER_PASSWD']
MONGO_DB = os.environ['MONGO_DB']
CMC_KEY = os.environ['CMC_KEY']

def mongo_connect():
    client = MongoClient(f'mongodb://{MONGO_USER}:{MONGO_USER_PASSWD}@localhost:27017/{MONGO_DB}')
    db = client[MONGO_DB]
    col = db['listings']
    return (client, db, col)

def cmc_connect():
    cmc = CoinMarketCapAPI(CMC_KEY)
    return cmc

def latest_listings(drop_keys=['tags'], limit=2000):
    cmc = cmc_connect()
    listings = cmc.cryptocurrency_listings_latest(limit=limit)
    
    for listing in listings.data:
        for key in drop_keys:
            listing.pop(key, None)
    
    return listings.data

def scan():
    client, db, col = mongo_connect()
    listings = latest_listings()
    col.insert_one({'timestamp':dt.utcnow(),'listings':listings})
    print(f'Listings fetched at {dt.utcnow()}')

if __name__=='__main__':
    scan()