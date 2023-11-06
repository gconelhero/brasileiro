from datetime import datetime, timedelta
import re

class ObjetoJogo:

    def __init__(self, cabecalho, arbitragem, cronologia, jogadores, comissao, gols, cartoes_amarelos, cartoes_vermelhos, substituicoes):
        self.cabecalho = cabecalho
        self.arbitragem = arbitragem
        self.cronologia = cronologia
        self.jogadores = jogadores
        self.comissao = comissao
        self.gols = gols
        self.cartoes_amarelos = cartoes_amarelos
        self.cartoes_vermelhos = cartoes_vermelhos
        self.substituicoes = substituicoes

    def transform(self):
        try:
            cabecalho = self.cabecalho
            jogo_num = self.cabecalho[0]
            campeonato = self.cabecalho[1]
            rodada = self.cabecalho[2]
            jogo = self.cabecalho[3]
            data = self.cabecalho[4].isoformat()
            hora = self.cabecalho[5].isoformat()
            estadio = self.cabecalho[6]
            cabecalho = {'jogo_n': jogo_num, 
                         'campeonato': campeonato, 
                         'rodada': rodada, 
                         'jogo': jogo, 
                         'data': data, 
                         'hora': hora, 
                         'estadio': estadio, 
                         }
            
            lista_arbitragem = self.arbitragem
            lista_cronologia = self.cronologia
            jogadores = self.jogadores
            comissao = self.comissao
            gols = self.gols
            cart_amar = self.cartoes_amarelos
            cart_ver = self.cartoes_vermelhos
            substituicao = self.substituicoes
        except Exception as erro:
            pass
        arbitragem = {}
        for i in range(len(lista_arbitragem)):
            arbitragem[lista_arbitragem[i].split(':')[0]] = lista_arbitragem[i].split(':')[-1]
            arbitragem['jogo_numero'] = cabecalho['jogo_n']
            arbitragem['data'] = cabecalho['data']
        lista_cronologia = self.cronologia
        cronologia = {}
        tmp_str = lista_cronologia[0].split('mandante:')[1].split('Atraso')[0].replace(' ', '') + ':00 -0300'
        cronologia['Entrada mandante 1T'] = datetime.strptime(tmp_str, "%H:%M:%S %z").timetz().isoformat()
        cronologia['Atraso mandante 1T'] = lista_cronologia[0].split('mandante:')[1].split('Atraso: ')[-1]
        lista_cronologia.pop(0)
        tmp_str = lista_cronologia[0].split('visitante:')[1].split('Atraso')[0].replace(' ', '') + ':00 -0300'
        cronologia['Entrada visitante 1T'] = datetime.strptime(tmp_str, "%H:%M:%S %z").timetz().isoformat()
        cronologia['Atraso visitante 1T'] = lista_cronologia[0].split('visitante:')[1].split('Atraso: ')[-1]
        lista_cronologia.pop(0)
        tmp_str = lista_cronologia[0].split('Tempo:')[1].split('Atraso')[0].replace(' ', '') + ':00 -0300'
        cronologia['Início 1T'] = datetime.strptime(tmp_str, "%H:%M:%S %z").timetz().isoformat()
        cronologia['Atraso início 1T'] = lista_cronologia[0].split('Tempo:')[1].split('Atraso: ')[-1]
        lista_cronologia.pop(0)
        tmp_str = lista_cronologia[0].split('Tempo:')[1].split('Acréscimo')[0].replace(' ', '') + ':00 -0300'
        cronologia['Término 1T'] = datetime.strptime(tmp_str, "%H:%M:%S %z").timetz().isoformat()
        if re.search(r'\d+', lista_cronologia[0].split('Acréscimo:')[1]):
            cronologia['Acréscimo 1T'] = re.search(r'\d+', lista_cronologia[0].split('Acréscimo:')[1]).group()
            cronologia['Acréscimo 1T'] = datetime.strptime(str(timedelta(minutes=int(cronologia['Acréscimo 1T']))), "%H:%M:%S").time().isoformat()
        else:
            cronologia['Acréscimo 1T'] = 'Não Houve'
        lista_cronologia.pop(0)
        tmp_str = lista_cronologia[0].split('mandante:')[1].split('Atraso')[0].replace(' ', '') + ':00 -0300'
        cronologia['Entrada mandante 2T'] = datetime.strptime(tmp_str, "%H:%M:%S %z").timetz().isoformat()
        cronologia['Atraso mandante 2T'] = lista_cronologia[0].split('mandante:')[1].split('Atraso: ')[-1]
        lista_cronologia.pop(0)
        cronologia['Entrada visitante 2T'] = datetime.strptime(tmp_str, "%H:%M:%S %z").timetz().isoformat()
        cronologia['Atraso visitante 2T'] = lista_cronologia[0].split('visitante:')[1].split('Atraso: ')[-1]
        lista_cronologia.pop(0)
        cronologia['Início 2T'] = datetime.strptime(tmp_str, "%H:%M:%S %z").timetz().isoformat()
        cronologia['Atraso início 2T'] = lista_cronologia[0].split('Tempo:')[1].split('Atraso: ')[-1]
        lista_cronologia.pop(0)
        tmp_str = lista_cronologia[0].split('Tempo:')[1].split('Acréscimo')[0].replace(' ', '') + ':00 -0300'
        cronologia['Término 2T'] = datetime.strptime(tmp_str, "%H:%M:%S %z").timetz().isoformat()
        if re.search(r'\d+', lista_cronologia[0].split('Acréscimo:')[1]):
            cronologia['Acréscimo 2T'] = re.search(r'\d+', lista_cronologia[0].split('Acréscimo:')[1]).group()
            cronologia['Acréscimo 2T'] = datetime.strptime(str(timedelta(minutes=int(cronologia['Acréscimo 2T']))), "%H:%M:%S").time().isoformat()
        else:
            cronologia['Acréscimo 2T'] = 'Não Houve'
        lista_cronologia.pop(0)
        tmp_str = lista_cronologia[0].split('Tempo: ')[-1].split('Resultado')[0].replace(' ', '')
        cronologia['Resultado 1T'] = {'Mandante': int(tmp_str.split('X')[0]),
                                      'Visitante': int(tmp_str.split('X')[-1])
                                      }
        tmp_str = lista_cronologia[0].split('Final: ')[-1].replace(' ', '')
        cronologia['Resultado Final'] = {'Mandante': int(tmp_str.split('X')[0]),
                                         'Visitante': int(tmp_str.split('X')[-1])
                                         }
        lista_cronologia.pop(0)
        cronologia['jogo_numero'] = cabecalho['jogo_n']
        cronologia['data'] = cabecalho['data']
        arbitragem['jogo_numero'] = cabecalho['jogo_n']
        arbitragem['data'] = cabecalho['jogo_n']
        mandante = cabecalho['jogo'].split(' X ')[0]
        visitante = cabecalho['jogo'].split(' X ')[-1]
        comissao[mandante]['equipe'] = mandante
        comissao[mandante]['jogo_numero'] = cabecalho['jogo_n']
        comissao[mandante]['data'] = cabecalho['data']
        comissao[visitante]['equipe'] = visitante
        comissao[visitante]['jogo_numero'] = cabecalho['jogo_n']
        comissao[visitante]['data'] = cabecalho['data']
        comissao = [comissao[mandante], comissao[visitante]]
        cronologia['Resultado 1T'] = cronologia['Resultado 1T']['Mandante'], cronologia['Resultado 1T']['Visitante']
        cronologia['Resultado Final'] = cronologia['Resultado Final']['Mandante'], cronologia['Resultado Final']['Visitante']
        jogadores_m = []
        for k, v in jogadores[mandante].items():
            jogador = {'id_cbf': v['id_cbf'], 
                        'nome': v['nome'], 
                        'apelido': v['apelido'], 
                        'numero': int(k), 
                        'equipe': mandante, 
                        'T/R': v['T/R'], 
                        'data': cabecalho['data'], 
                        'jogo_numero': cabecalho['jogo_n']
                       }
            jogadores_m.append(jogador)
        jogadores_v = []
        for k, v in jogadores[mandante].items():
            jogador = {'id_cbf': v['id_cbf'], 
                        'nome': v['nome'], 
                        'apelido': v['apelido'], 
                        'numero': int(k), 
                        'equipe': mandante, 
                        'T/R': v['T/R'], 
                        'data': cabecalho['data'], 
                        'jogo_numero': cabecalho['jogo_n']
                       }
            jogadores_v.append(jogador)
        for gol in gols:
            gol['jogo_numero'] = cabecalho['jogo_n']
            gol['data'] = cabecalho['data']
        for cartao in cart_amar:
            cartao['jogo_numero'] = cabecalho['jogo_n']
            cartao['data'] = cabecalho['data']
        for cartao in cart_ver:
            cartao['jogo_numero'] = cabecalho['jogo_n']
            cartao['data'] = cabecalho['data']
        for subs in substituicao:
            subs['jogo_numero'] = cabecalho['jogo_n']
            subs['data'] = cabecalho['data']
        jogo = {'campeonato': cabecalho['campeonato'], 
                'jogo_numero': cabecalho['jogo_n'], 
                'rodada': cabecalho['rodada'], 
                'mandante': mandante, 
                'visitante': visitante, 
                'data': cabecalho['data'], 
                'hora': cabecalho['hora'], 
                'estadio': cabecalho['estadio'],
                }
        jogadores_m.extend(jogadores_v)

        return {'jogo': jogo, 
                'arbitragem': arbitragem, 
                'cronologia': cronologia, 
                'jogadores': jogadores_m, 
                'gols': gols, 
                'cartoes_amarelos': cart_amar, 
                'cartoes_vermelhos': cart_ver, 
                'substituicoes': substituicao
                }