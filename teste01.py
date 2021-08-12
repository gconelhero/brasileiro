import os
import tabula
import pandas as pd
import json
import re

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

arquivos = os.listdir('.\\PDFs\\')
for arquivo in arquivos:

    pdf = f'.\\PDFs\\{arquivo}' #".\\PDFs\\Jogo17.pdf"

    leitor = open(pdf, 'rb')
    leitor = tabula.read_pdf(pdf, pages='all')

    df = pd.DataFrame(leitor[0])
    df2 = pd.DataFrame(leitor[1])
    df3 = pd.DataFrame(leitor[2])
    df4 = pd.DataFrame(leitor[3])
    print(df4)
    
    count = 0
    cronologia = {}
    primeiro = {}
    segundo = {}
    for i in df3[df3.columns[0]][0:-1].iloc[1:]:
        primeiro[i] = re.search('(\d+:\d+)', df3[df3.columns[1]][count + 1]).group()
        count += 1
    primeiro['Acrescimo'] = re.search('(\d+ min)', df3[df3.columns[3]][0:-1].iloc[4]).group()

    count = 0
    for i in df3[df3.columns[0]][0:-1].iloc[1:]:
        segundo[i] = re.search('(\d+:\d+)', df3[df3.columns[3]][count + 1]).group()
        count += 1
    segundo['Acrescimo'] = re.search('(\d+ min)', df3[df3.columns[6]][0:-1].iloc[4]).group()
    print(df3[df3.columns[0]][0:-1].iloc[4])

    #print(df3)
    cronologia['1o Tempo'] = primeiro
    cronologia['2o Tempo'] = segundo
    

    count = 0
    arbitragem = {}
    for i in df2[df2.columns[0]]:
       arbitragem[i] = df2[df2.columns[1]][count]
       count += 1

    data_re = re.search('(\d+/\d+/\d+)', df.iloc[1][1])
    hora_re = re.search('(\d+:\d+)', df.iloc[1][1])
    json_model = {'Jogo': {'Campeonato': f'{df.columns[1]}', 'Jogo': f'{df.loc[0][1]}',
                    'Data:': data_re.group(), 'Horario': hora_re.group(), 
                    'Estadio': f'{df.iloc[1][2]}', 'Rodada': df.columns[-1], 
                    'Arbitragem': arbitragem, 'Cronologia': cronologia}
                    }

#print(json_model)