import os
from dotenv import dotenv_values, load_dotenv
import pymongo
from bson.json_util import dumps
import json

load_dotenv()
DB_PASSWORD = os.getenv('DB_PASSWORD')
uri = "mongodb+srv://admin:" + str(DB_PASSWORD) + "@miloucluster.q8dhp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongo = pymongo.MongoClient(str(uri), maxPoolSize=50, connect=False)
db = pymongo.database.Database(mongo, 'myFirstDatabase')

def findStockBySymbol(symbol):
    col = pymongo.collection.Collection(db, 'datapoints')
    col_results = json.loads(dumps(col.find_one({"symbol": symbol})))
    return col_results