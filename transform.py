import json
import re

class ObjetoJogo:

    def transform(objeto):
        

        try:
            cabecalho = objeto[0]
            jogo_num = cabecalho[0]
            campeonato = cabecalho[1]
            rodada = cabecalho[2]
            jogo = cabecalho[3]
            data = cabecalho[4]
            hora = cabecalho[5]
            estadio = cabecalho[6]
            
            lista_arbitragem = objeto[1]
            lista_cronologia = objeto[2]
            jogadores = objeto[3]
            comissao = objeto[4]
            gols = objeto[5]
            cart_amar = objeto[6]
            cart_ver = objeto[7]
            obs = objeto[8]
            substituicao = objeto[9]

        except Exception as erro:
            print(erro)
            pass


        chave = 0
        valor = 1
        arbitragem = {}
        loop = int(len(lista_arbitragem) / 2)
        
        for i in range(loop):
            arbitragem[lista_arbitragem[chave].split(':')[0]] = lista_arbitragem[valor]
            chave += 2
            valor += 2
        
        chave = 0
        valor = 1
        cronologia = {}
        for i in range(len(lista_cronologia)):
            
            if re.search('Resultado do 1º Tempo', lista_cronologia[chave]):
                cronologia['Resultado 1º Tempo'] = lista_cronologia[chave].split(':')[-1]
                cronologia['Resultado Final'] = lista_cronologia[valor].split(':')[-1]
                break
            else:
                cronologia[lista_cronologia[chave].replace(':', '')] = lista_cronologia[valor]
                chave += 2
                valor += 2
        
        chave = 0
        valor = 0
        jogador = {}
        jogadores_mandante = {}
        jogadores_visitante = {}
        loop = int(len(jogadores) / 6)
        for i in range(len(jogadores) - valor): # ARRUMAR O RANGE... MUITO ALTO!
            try:
                jogador = {}
                if re.search('\D* / \D+', jogadores[valor]):
                    if jogadores_mandante != {}:
                        jogadores_visitante['Clube'] = jogadores[valor]
                        valor += 1
                    else:
                        jogadores_mandante['Clube'] = jogadores[valor]
                        valor += 1
                
                elif jogadores_visitante != {}:
                    jogador['Nº'] = int(jogadores[valor])
                    valor += 1
                    jogador['Apelido'] = jogadores[valor]
                    valor += 1
                    jogador['Nome'] = jogadores[valor]
                    valor += 1
                    jogador['T/R'] = jogadores[valor]
                    valor += 1
                    jogador['P/A'] = jogadores[valor]
                    valor += 1
                    jogador['CBF'] = int(jogadores[valor])
                    valor += 1
                    jogadores_visitante[len(jogadores_visitante)] = jogador
                    
                else:
                    jogador['Nº'] = int(jogadores[valor])
                    valor += 1
                    jogador['Apelido'] = jogadores[valor]
                    valor += 1
                    jogador['Nome'] = jogadores[valor]
                    valor += 1
                    jogador['T/R'] = jogadores[valor]
                    valor += 1
                    jogador['P/A'] = jogadores[valor]
                    valor += 1
                    jogador['CBF'] = int(jogadores[valor])
                    valor += 1
                    jogadores_mandante[len(jogadores_mandante)] = jogador
                            
            except:
                pass


        count = 0
        chave = 0
        valor = 1
        comissao_mandante = {}
        comissao_visitante = {}
        for i in comissao:
            if re.search('\D* / \D+', i):
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
            
            if re.search('\d+:\d+', i) or re.search('Cartões Vermelhos', i):
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
                    if re.search('\d+:\d+', cart_amar[valor]):
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
                if re.search('\d+:\d+', i) or re.search('Ocorrências / Observações', i):
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
                        if re.search('\d+:\d+', cart_ver[valor]):
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
        print(cartoes_vermelho)
        
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
                break # PADRÃO DE STRING PARA INTERROMPER O LOOP!! FUNCIONOU
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
                    'Mandante': {'Jogadores': jogadores_mandante, 
                    'Comissão': comissao_mandante},
                    'Visitante': {'Jogadores': jogadores_visitante,
                    'Comissão': comissao_visitante},
                    'Gols': obj_gols, 'Cacrtões amarelo': cartoes_amarelo,
                    'Cartões vermelho': cartoes_vermelho, 
                    'Substituições': substituicoes, 'OBS': observacoes,
                    'OBS eventuais': eventuais, 'OBS assistente': assistente,
                    }
                    }

        return jogo_model

