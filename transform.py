from datetime import datetime, timezone, timedelta
import json
import re

class ObjetoJogo:

    def __init__(self, cabecalho, arbitragem, cronologia, jogadores):
        self.cabecalho = cabecalho
        self.arbitragem = arbitragem
        self.cronologia = cronologia
        self.jogadores = jogadores

    def transform(self):
        try:
            cabecalho = self.cabecalho

            jogo_num = self.cabecalho[0]
            campeonato = self.cabecalho[1]
            rodada = self.cabecalho[2]
            jogo = self.cabecalho[3]
            data = self.cabecalho[4]
            hora = self.cabecalho[5]
            estadio = self.cabecalho[6]

            lista_arbitragem = self.arbitragem
            lista_cronologia = self.cronologia
            jogadores = self.jogadores

            '''
            comissao = objeto[4]
            gols = objeto[5]
            cart_amar = objeto[6]
            cart_ver = objeto[7]
            obs = objeto[8]
            substituicao = objeto[9]
            '''
        except Exception as erro:
            pass

        arbitragem = {}
        for i in range(len(lista_arbitragem)):
            arbitragem[lista_arbitragem[i].split(':')[0]] = lista_arbitragem[i].split(':')[-1]
        
        cronologia = {}
        tmp_str = lista_cronologia[0].split('mandante:')[1].split('Atraso')[0].replace(' ', '') + ':00 -0300'
        cronologia['Entrada mandante 1T'] = datetime.strptime(tmp_str, "%H:%M:%S %z").timetz()
        cronologia['Atraso mandante 1T'] = lista_cronologia[0].split('mandante:')[1].split('Atraso: ')[-1]
        lista_cronologia.pop(0)
        tmp_str = lista_cronologia[0].split('visitante:')[1].split('Atraso')[0].replace(' ', '') + ':00 -0300'
        cronologia['Entrada visitante 1T'] = datetime.strptime(tmp_str, "%H:%M:%S %z").timetz()
        cronologia['Atraso visitante 1T'] = lista_cronologia[0].split('visitante:')[1].split('Atraso: ')[-1]
        lista_cronologia.pop(0)
        tmp_str = lista_cronologia[0].split('Tempo:')[1].split('Atraso')[0].replace(' ', '') + ':00 -0300'
        cronologia['Início 1T'] = datetime.strptime(tmp_str, "%H:%M:%S %z").timetz()
        cronologia['Atraso início 1T'] = lista_cronologia[0].split('Tempo:')[1].split('Atraso: ')[-1]
        lista_cronologia.pop(0)
        tmp_str = lista_cronologia[0].split('Tempo:')[1].split('Acréscimo')[0].replace(' ', '') + ':00 -0300'
        cronologia['Término 1T'] = datetime.strptime(tmp_str, "%H:%M:%S %z").timetz()
        if re.search(r'\d+', lista_cronologia[0].split('Acréscimo:')[1]):
            cronologia['Acréscimo 1T'] = re.search(r'\d+', lista_cronologia[0].split('Acréscimo:')[1]).group()
            cronologia['Acréscimo 1T'] = timedelta(minutes=int(cronologia['Acréscimo 1T']))
        else:
            cronologia['Acréscimo 1T'] = 'Não Houve'
        lista_cronologia.pop(0)
        tmp_str = lista_cronologia[0].split('mandante:')[1].split('Atraso')[0].replace(' ', '') + ':00 -0300'
        cronologia['Entrada mandante 2T'] = datetime.strptime(tmp_str, "%H:%M:%S %z").timetz()
        cronologia['Atraso mandante 2T'] = lista_cronologia[0].split('mandante:')[1].split('Atraso: ')[-1]
        lista_cronologia.pop(0)
        cronologia['Entrada visitante 2T'] = datetime.strptime(tmp_str, "%H:%M:%S %z").timetz()
        cronologia['Atraso visitante 2T'] = lista_cronologia[0].split('visitante:')[1].split('Atraso: ')[-1]
        lista_cronologia.pop(0)
        cronologia['Início 2T'] = datetime.strptime(tmp_str, "%H:%M:%S %z").timetz()
        cronologia['Atraso início 2T'] = lista_cronologia[0].split('Tempo:')[1].split('Atraso: ')[-1]
        lista_cronologia.pop(0)
        tmp_str = lista_cronologia[0].split('Tempo:')[1].split('Acréscimo')[0].replace(' ', '') + ':00 -0300'
        cronologia['Término 2T'] = datetime.strptime(tmp_str, "%H:%M:%S %z").timetz()
        if re.search(r'\d+', lista_cronologia[0].split('Acréscimo:')[1]):
            cronologia['Acréscimo 2T'] = re.search(r'\d+', lista_cronologia[0].split('Acréscimo:')[1]).group()
            cronologia['Acréscimo 2T'] = timedelta(minutes=int(cronologia['Acréscimo 2T']))
        else:
            cronologia['Acréscimo 2T'] = 'Não Houve'
        lista_cronologia.pop(0)
        tmp_str = lista_cronologia[0].split('Tempo: ')[-1].split('Resultado')[0].replace(' ', '')
        cronologia['Resultado 1T'] = {'Mandante': int(tmp_str.split('X')[0]),
                                      'Visitante': int(tmp_str.split('X')[-1])
                                      }
        tmp_str = lista_cronologia[0].split('Final: ')[-1].replace(' ', '')
        cronologia['Resultado Final'] = {'Mandate': int(tmp_str.split('X')[0]),
                                         'Visitante': int(tmp_str.split('X')[-1])
                                         }
        lista_cronologia.pop(0)
        
        print(cronologia)
        count = 0
        valor = 1
        comissao_mandante = {}
        comissao_visitante = {}
        for i in comissao:
            if re.search(r'\D* / \D+', i):
                count += 1
            elif count == 1:
                try:
                    if list(comissao_mandante.values())[-1] == '':
                        comissao_mandante[list(comissao_mandante.keys())[-1]] = i
                    else:
                        comissao_mandante[i.replace(':', '')] = ''    
                except:
                    comissao_mandante[i.replace(':', '')] = ''
            elif count == 2:
                try:
                    if list(comissao_visitante.values())[-1] == '':
                        comissao_visitante[list(comissao_visitante.keys())[-1]] = i
                    else:
                        comissao_visitante[i.replace(':', '')] = ''
                except:
                    comissao_visitante[i.replace(':', '')] = ''
    

        obj_gols = {}
        gol = {}
        valor = 0
        for i in range(int((len(gols) / 6))):
            gol = {}
            gol['Minuto'] = gols[valor]
            valor += 1
            gol['Tempo'] = gols[valor]
            valor += 1
            gol['Nº'] = gols[valor]
            valor += 1
            gol['Tipo'] = gols[valor]
            valor += 1
            gol['Nome'] = gols[valor]
            valor += 1
            gol['Equipe'] = gols[valor]
            valor += 1
            obj_gols[len(obj_gols) + 1] = gol


        count = -1
        cart = {}
        cartoes_amarelo = {}
        valor = 0
        motivo = []
        for i in cart_amar:
            
            if re.search(r'\d+:\d+', i) or re.search('Cartões Vermelhos', i):
                count = 0
                if count == 0 and motivo == []:
                    cart['Minuto'] = cart_amar[valor]
                    valor += 1
                    cart['Tempo'] = cart_amar[valor]
                    valor += 1
                    cart['Nº'] = cart_amar[valor]
                    valor += 1
                    cart['Nome'] = cart_amar[valor]
                    valor += 1
                    cart['Equipe'] = cart_amar[valor]
                    valor += 1
            if re.search('Motivo:', i):
                count = 1
            if count == 1:
                motivo.append(cart_amar[valor])
                valor += 1
                try:
                    if re.search(r'\d+:\d+', cart_amar[valor]):
                        count = 0
                except:
                    cart['Motivo'] = ' '.join(motivo).replace('Motivo:', '')
                    cartoes_amarelo[len(cartoes_amarelo) + 1] = cart
                    pass
            if count == 0 and motivo != []:
                cart['Motivo'] = ' '.join(motivo).replace('Motivo:', '')
                motivo = []
                cartoes_amarelo[len(cartoes_amarelo) + 1] = cart
                cart = {}
                

        count = -1
        cart = {}
        cartoes_vermelho = {}
        valor = 0
        motivo = []
        for i in cart_ver:
            try:
                if re.search(r'\d+:\d+', i) or re.search('Ocorrências / Observações', i):
                    count = 0
                    if count == 0:
                        cart['Minuto'] = cart_ver[valor]
                        valor += 1
                        cart['Tempo'] = cart_ver[valor]
                        valor += 1
                        cart['Nº'] = cart_ver[valor]
                        valor += 1
                        cart['Nome'] = cart_ver[valor].split(' - ')[0]
                        cart['Equipe'] = cart_ver[valor].split(' - ')[-1]
                        valor += 2
                if re.search('Motivo:', i) :
                    count = 1
                if count == 1:
                    motivo.append(cart_ver[valor])
                    valor += 1
                    try:
                        if re.search(r'\d+:\d+', cart_ver[valor]):
                            count = 0
                    except:
                        cart['Motivo'] = ' '.join(motivo).replace('Motivo:', '')
                        cartoes_vermelho[len(cartoes_vermelho) + 1] = cart
                        pass
                if count == 0 and motivo != []:
                    cart['Motivo'] = ' '.join(motivo).replace('Motivo:', '')
                    motivo = []
                    cartoes_vermelho[len(cartoes_vermelho) + 1] = cart
                    cart = {}
            except:
                pass

        
        try:
            observacoes_todas = ' '.join([elem for elem in obs[0:]])
            eventuais = observacoes_todas.split('Observações Eventuais')[1].split(' Relatório do Assistente')[0]
            assistente = observacoes_todas.split('Relatório do Assistente')[-1]
            observacoes = observacoes_todas.split('Observações Eventuais')[0].replace('Ocorrências / Observações', '')

        except:
            observacoes_todas = ''
            eventuais = ''
            assistente = ''
            observacoes = ''
        count = -1000
        valor = 0
        substituir = {}
        substituicoes = {}
        for i in range(len(substituicao)):
            if re.search('Publicação da Súmula', substituicao[valor].split(':')[0]):
                break # PADRÃO DE STRING PARA INTERROMPER O LOOP
            else:
                substituir['Minuto'] = substituicao[valor]
                valor += 1
                substituir['Tempo'] = substituicao[valor]
                valor += 1
                substituir['Equipe'] = substituicao[valor]
                valor += 1
                substituir['Entrou'] = substituicao[valor]
                valor += 1
                substituir['Saiu'] = substituicao[valor]
                valor += 1
            substituicoes[len(substituicoes) + 1] = substituir

            
        jogo_model = {'Jogo': {'No': jogo_num, 'Campeonato': campeonato, 'Rodada': rodada,
                    'Jogo': jogo, 'Data': data, 'Horário': hora, 'Estádio': estadio,
                    'Arbitragem': arbitragem, 'Cronologia': cronologia,
                    'Mandante':{'Clube': mandante,'Jogadores': jogadores_mandante, 
                    'Comissão': comissao_mandante},
                    'Visitante':{'Clube': visitante,'Jogadores': jogadores_visitante,
                    'Comissão': comissao_visitante},
                    'Gols': obj_gols, 'Cartões amarelo': cartoes_amarelo,
                    'Cartões vermelho': cartoes_vermelho,
                    'Substituições': substituicoes, 'OBS': observacoes,
                    'OBS eventuais': eventuais, 'OBS assistente': assistente,}}

        return jogo_model

