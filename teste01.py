import os
import tabula
import pandas as pd
import json
import re
from tabulate import tabulate

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

arquivos = os.listdir('.\\PDFs\\')
for arquivo in arquivos:

    pdf = f'.\\PDFs\\{arquivo}' #".\\PDFs\\Jogo17.pdf"

    leitor = open(pdf, 'rb')
    leitor = tabula.read_pdf(pdf, pages='all', multiple_tables = True)
    print(tabulate(leitor[3].iloc[1:], tablefmt="pretty"))

    df = pd.DataFrame(leitor[0])
    df2 = pd.DataFrame(leitor[1])
    df3 = pd.DataFrame(leitor[2])
    df4 = pd.DataFrame(leitor[3])
    df5 = pd.DataFrame(leitor[4])
    df6 = pd.DataFrame(leitor[5])
    df7 = pd.DataFrame(leitor[6])
    #print(df7)
    #print(list(df7.columns))
    #print(df4)

    
    count = 1
    gols = {}
    for i in df6[df6.columns[0]][1:]:
        try:
            gol = {}
            gol['Minuto'] = df6[df6.columns[0]].iloc[count]
            gol['Tempo'] = df6[df6.columns[1]].iloc[count]
            gol['Tipo'] = df6[df6.columns[3]].iloc[count]
            gol['jogador'] = f'No {df6[df6.columns[2]].iloc[count]} - {df6[df6.columns[4]].iloc[count]}'
            gol['Equipe'] = df6[df6.columns[6]].iloc[count]
            gols[count] = gol
            count += 1
        except Exception as erro:
            #print(f'{type(erro)}\n{erro}\n{pdf}, Gols')
            gols = {}
            pass

    # COMISSÃO
    count = 1
    comissao_mandante = {}
    for i in df5[df5.columns[0]][1:]:
        try:
            comissao_mandante[i] = df5[df5.columns[1]].iloc[count]
            count += 1
        except Exception as erro:
            print(f'{type(erro)}\n{erro}\n{pdf}, Comissão')
            pass

    count = 1
    comissao_visitante = {}
    for i in df5[df5.columns[2]][1:]:
        try:
            comissao_visitante[i] = df5[df5.columns[3]].iloc[count]
            count += 1
        except Exception as erro:
            print(f'{type(erro)}\n{erro}\n{pdf}, Comissão 2')
            pass

    # JOGADORES
    count = 2
    jogadores = {}
    jogadores_mandante = {}
    jogadores_mandante['Clube'] = df4[df4.columns[2]].iloc[0]
    for i in df4[df4.columns[0]][0:].iloc[2:]:
        try:
            jogador = {}
            try: 
                jogador['No'] = int(df4[df4.columns[0]].iloc[count])
            except:
                print(jogador)
            try:
                jogador['Apelido'] = df4[df4.columns[1]].iloc[count]
            except:
                print(jogador)
            try:
                jogador['Nome'] = df4[df4.columns[2]].iloc[count]               
                if jogador['Nome'][-1] in ['T', 'R']:
                    jogador['Nome'] = jogador['Nome'][0:-1]
                if jogador['Nome'][-4:] in ['T(g)', 'R(g)']:
                    jogador['Nome'] = jogador['Nome'][0:-4]
            except:
                jogador['Nome'] = jogador['Apelido']
            if jogador['Nome'] == '':
                jogador['Nome'] = jogador['Apelido']

            if count == 2:
                jogador['T/R'] = 'T(g)'
            elif count == 13:
                jogador['T/R'] = 'R(g)'
            elif count > 2 and count < 13:
                jogador['T/R'] = 'T'
            elif count > 13:
                jogador['T/R'] = 'R'
            jogador['P/A'] = df4[df4.columns[4]].iloc[count]
            jogador['CBF'] = int(re.search('(\d\d\d+)', df4[df4.columns[5]].iloc[count]).group())
            jogadores[count - 1] = jogador
            count += 1
        except Exception as erro:
            print(f'{type(erro)}\n{erro}\n{pdf}, Jogadores')
            pass

            jogador = {}
    jogadores_mandante['Jogadores'] = jogadores

    count = 2
    jogadores = {}
    jogadores_visitante = {}
    jogadores_visitante['Clube'] = df4[df4.columns[5]].iloc[0]
    if str(jogadores_visitante['Clube']) == 'nan':
        jogadores_visitante['Clube'] = df4[df4.columns[6]].iloc[0]
    for i in df4[df4.columns[5]][0:].iloc[2:]:
        try:
            jogador = {}
            try:
                jogador['No'] = int(re.search('\s\d{1,3}\s', df4[df4.columns[5]].iloc[count]).group())
            except:
                print(jogador)
                jogador['No'] = int(df4[df4.columns[5]].iloc[count].split(' ')[0])
                
            try:
                jogador['Apelido'] = df4[df4.columns[5]].iloc[count].split(' ')[2]
            except:
                print(jogador)
                if df4[df4.columns[6]].iloc[count] in ['T', 'R', 'T(g)', 'R(g)']:
                    jogador['Apelido'] = df4[df4.columns[5]].iloc[count].split(' ')[1]
                else:
                    jogador['Apelido'] = ' '.join(df4[df4.columns[5]].iloc[count].split(' ')[2:])
                    if jogador['Apelido'] == '':
                        jogador['Apelido'] = ' '.join(df4[df4.columns[5]].iloc[count].split(' ')[1:])
            try:
                if df4[df4.columns[7]].iloc[count] in ['T', 'R', 'T(g)', 'R(g)']:
                    jogador['Nome'] = df4[df4.columns[6]].iloc[count]
                else:
                    if len(df4[df4.columns[5]].iloc[count].split(' ')[3:]) >= 2:
                        jogador['Nome'] = ' '.join(df4[df4.columns[5]].iloc[count].split(' ')[3:])
                    else:
                        jogador['Nome'] = df4[df4.columns[6]].iloc[count]
            except:
                pass
            if jogador['Nome'] == '':
                jogador['Nome'] = jogador['Apelido']

            if jogador['Nome'][-1] in ['T', 'R']:
                jogador['Nome'] = jogador['Nome'][0:-1]
            if jogador['Nome'][-4:] in ['T(g)', 'R(g)']:
                jogador['Nome'] = jogador['Nome'][0:-4]
            
            if count == 2:
                jogador['T/R'] = 'T(g)'
            elif count == 13:
                jogador['T/R'] = 'R(g)'
            elif count > 2 and count < 13:
                jogador['T/R'] = 'T'
            elif count > 13:
                jogador['T/R'] = 'R'
            jogador['P/A'] = df4[df4.columns[8]].iloc[count]
            jogador['CBF'] = int(df4[df4.columns[9]].iloc[count])
            jogadores[count - 1] = jogador
        except Exception as erro:
            print(f'{type(erro)}\n{erro}\n{pdf}, Jogadores 2')
            pass
        count += 1
    jogadores_visitante['Jogadores'] = jogadores

    # CRONOLOGIA
    count = 0
    cronologia = {}
    primeiro = {}
    segundo = {}
    try:
        for i in df3[df3.columns[0]][0:-1].iloc[1:]:
            primeiro[i] = re.search('(\d+:\d+)', df3[df3.columns[1]][count + 1]).group()
            count += 1
        primeiro['Acrescimo'] = re.search('(\d+ min)', df3[df3.columns[3]][0:-1].iloc[4]).group()
        primeiro['Resultado'] = re.search('(\d+ X \d+)', df3[df3.columns[0]].iloc[-1]).group()
    except Exception as erro:
            print(f'{type(erro)}\n{erro}\n{pdf}')
            pass

    count = 0
    try:
        for i in df3[df3.columns[0]][0:-1].iloc[1:]:
            segundo[i] = re.search('(\d+:\d+)', df3[df3.columns[3]][count + 1]).group()
            count += 1
        segundo['Acrescimo'] = re.search('(\d+ min)', df3[df3.columns[6]][0:-1].iloc[4]).group()
        segundo['Resultado'] = re.search('(\d+ X \d+)', df3[df3.columns[3]].iloc[-1]).group()
        cronologia['1o Tempo'] = primeiro
        cronologia['2o Tempo'] = segundo
    except Exception as erro:
            print(f'{type(erro)}\n{erro}\n{pdf}, Cronologia')
            pass

    # ARBITRAGEM
    count = 0
    arbitragem = {}
    for i in df2[df2.columns[0]]:
        try:
            arbitragem[i] = df2[df2.columns[1]][count]
            count += 1
        except Exception as erro:
            print(f'{type(erro)}\n{erro}\n{pdf}, Arbitragem')
            pass

    # JSON_MODEL
    data_re = re.search('(\d+/\d+/\d+)', df.iloc[1][1])
    hora_re = re.search('(\d+:\d+)', df.iloc[1][1])
    json_model = {'Jogo': {'Campeonato': f'{df.columns[1]}', 'Jogo': f'{df.loc[0][1]}',
                    'Data:': data_re.group(), 'Horario': hora_re.group(), 
                    'Estadio': f'{df.iloc[1][2]}', 'Rodada': df.columns[-1], 
                    'Arbitragem': arbitragem, 'Cronologia': cronologia,
                    'Clube mandante': {'Jogadores': jogadores_mandante,
                    'Comissao': comissao_mandante, },
                    'Clube visitante': {'Jogadores': jogadores_visitante,
                    'Comissao': comissao_visitante}, 'Gols': gols}
                    }

    #print(json.dumps(json_model, sort_keys=False, indent=4, separators=(',', ': ')))
    print(pdf)