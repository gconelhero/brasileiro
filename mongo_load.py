import sys, traceback

from pymongo import MongoClient

class DataBase():

    def __init__(self, collection):
        try:
            self.mongo_ins = MongoClient(host='0.0.0.0',
                                        port=27017,
                                        maxPoolSize=200)
            self.database_name = 'brasileiro'
            self.collection_name = collection
            self.connect = self.mongo_ins[self.database_name]
            self.database = self.connect[self.collection_name]
        except:
            with open('log_mongo_client.txt',  'a') as log:
                traceback.print_exc(file=log)
                traceback.print_exc(file=sys.stdout)

    def insert(self, objeto):
        try:
            insert = self.database.insert_one(objeto)
            return insert
        except:
            with open('./logs/log_mongo_client.txt',  'a') as log:
                traceback.print_exc(file=log)
                traceback.print_exc(file=sys.stdout)