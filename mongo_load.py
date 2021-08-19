import sys, traceback, os
import json
from pymongo import MongoClient

class DataBase():

    def __init__(self, collection):
        try:
            self.mongo_ins = MongoClient(host='192.168.0.112',
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

    def insert(self, arquivo):
        try:
            with open(arquivo, 'r') as json_file:
                json_data = json.load(json_file)
                insert = self.database.insert_one(json_data)

            return insert
        except:
            with open('./logs/log_mongo_client.txt',  'a') as log:
                traceback.print_exc(file=log)
                traceback.print_exc(file=sys.stdout)


arquivos = os.listdir('./json_files/')
for arquivo in arquivos:
    DataBase('jogos').insert(f'./json_files/{arquivo}')
