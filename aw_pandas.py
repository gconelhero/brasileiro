from pymongo import MongoClient
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

connect = MongoClient(host='192.168.0.112')

data = list(connect.brasileiro.jogos.find(projection={'_id':False}))

df = pd.DataFrame(list(data))
jogos = pd.DataFrame(list(df['Jogo']))

arbitragem = pd.DataFrame(list(jogos['Arbitragem']))
print(arbitragem[arbitragem.columns[0:2]].iloc[0:2])
