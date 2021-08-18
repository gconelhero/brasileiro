from pymongo import MongoClient
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

connect = MongoClient(host='192.168.0.112')

data = list(connect.brasileiro.jogos.find(projection={'_id':False}))

df = pd.DataFrame(list(data))
jogos = pd.DataFrame(list(df['Jogo']))

# Construíndo um dataframe a partir do objeto arbitragem.
arbitragem = pd.DataFrame(list(jogos['Arbitragem']))
# Printando as 2 primeiras colunas e as 10 primeiras linhas do Data Frame.
print(arbitragem[arbitragem.columns[0:2]].iloc[0:10])

