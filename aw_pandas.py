from pymongo import MongoClient
import pandas as pd
from pyspark import SparkContext, SparkConf
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)

connect = MongoClient(host='192.168.0.112')

data = list(connect.brasileiro.jogos.find(projection={'_id':False}))

df = pd.DataFrame(list(data))
jogos = pd.DataFrame(list(df['Jogo']))

arbitragem = pd.DataFrame(list(jogos['Arbitragem']))

arbitragem = pd.concat([jogos['No'], 
            pd.to_datetime(jogos['Data'], format='%d/%m/%Y'), 
            arbitragem], axis=1)

#print(arbitragem[arbitragem.columns[0:3]][0:10])
janeiro = arbitragem.loc[(arbitragem['Data'].dt.year==2020) & (arbitragem['Data'].dt.day==13)]
janeiro = janeiro[janeiro.columns[0:7]].iloc[0:10]
index_off = janeiro.set_index(['No', 'Data'])

mandante = pd.DataFrame(list(jogos['Mandante']))
mandante = pd.DataFrame(list(mandante['Jogadores']))

# Oriented for Column
lista_jogadores_mandantes = [i for i in mandante.iloc[0].dropna()]
print(pd.DataFrame.from_records(lista_jogadores_mandantes))    

lista_jogadores_mandantes = []

for i in mandante.index:    
    lista_jogadores_mandantes = [i for i in mandante.iloc[i].dropna()]
    
# From Records obrigatóriamente orientado à coluna
# From dict orientado às
print(pd.DataFrame.from_records(lista_jogadores_mandantes))