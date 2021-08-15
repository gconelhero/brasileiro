import re
from PyPDF2 import PdfFileReader

flag = ['Arbitragem', 'Cronologia', 'Relação de Jogadores', 'Comissão Técnica', 
            'Gols', 'Cartões Amarelos', 'Cartões Vermelhos', 'Ocorrências / Observações',
            'Substituições',]
    
reject = ['Arbitragem', 'Cronologia', '1º Tempo', '2º Tempo', 
                'Relação de Jogadores',
                'T = Titular | R = Reserva | P = Profissional | A = Amador | (g) = Goleiro',
                'TC - Técnico',
                'Confederação Brasileira de Futebol','Gols',
                'Nº', 'Apelido', 'Nome Completo', 'T/R', 'P/A', 'CBF','Página 1/3', 
                'NR = Normal | PN = Pênalti | CT = Contra | FT = Falta',
                'Tempo', '1T/2T', 'Nº', 'Tipo', 'Nome do Jogador', 'Equipe',
                'Cartões Amarelos', 'Cartões Vermelhos',
                'AT - Assistente TécnicoAT - Assistente Técnico','Página 2/3'
                'Entrou', 'Saiu',]

class ObjetoJogo:

    def parte_um(pag_um):
        jogo_num = int(pag_um.extractText().splitlines()[0].split(': ')[-1])
        campeonato = pag_um.extractText().splitlines()[4]
        rodada = int(pag_um.extractText().splitlines()[6])
        jogo = pag_um.extractText().splitlines()[8]
        data = pag_um.extractText().splitlines()[10]
        hora = pag_um.extractText().splitlines()[12]
        estadio = pag_um.extractText().splitlines()[14]

        count = -1000
        lista_arbitragem = []
        lista_cronologia = []
        jogadores = []
        for i in pag_um.extractText().splitlines():
            try:
                if i == flag[0]:
                    count = 0
                elif count == 0 and i not in reject:
                    lista_arbitragem.append(i)
                elif i == flag[1]:
                    count = 1
                elif count == 1 and i not in reject:
                    lista_cronologia.append(i)
                elif i == flag[2]:
                    count = 2
                elif count == 2 and i not in reject:
                    jogadores.append(i)
            except:
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
        loop = int(len(lista_cronologia) / 2)   
        for i in range(loop):
            cronologia[lista_cronologia[chave]] = lista_cronologia[valor]
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

    def parte_dois(pag_dois):
        count = -1000
        comissao = []
        gols = []
        cart_amar = []
        cart_ver = []
        for i in pag_dois.extractText().splitlines():
            try:
                if i == flag[3]:
                    count = 3
                if count == 3:
                    if re.search('(\D* / D+)', i):
                        comissao.insert(0, 'Clube')
                        comissao.append(i)
                    elif i != flag[3] and i not in reject:
                        comissao.append(i)
                if i == flag[4]:
                    count = 4
                if count == 4 and i not in reject:
                    gols.append(i)
                if i == flag[5]:
                    count = 5
                if count == 5 and i not in reject:
                    cart_amar.append(i)
                if i == flag[6]:
                    count = 6
                if count == 6 and i not in reject:
                    cart_ver.append(i)

            except:
                pass
        
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
        cartoes_vermelho = {}
        valor = 0
        motivo = []
        for i in cart_ver:
            try:
                cart = {}
                if re.search('\d+:\d+', i):
                    count = 0
                    if count == 0:
                        cart['Minuto'] = cart_ver[valor]
                        valor += 1
                        cart['Tempo'] = cart_ver[valor]
                        valor += 1
                        cart['Nº'] = cart_ver[valor]
                        valor += 1
                        cart['Nome'] = cart_ver[valor]
                        valor += 1
                        cart['Equipe'] = cart_ver[valor]
                        valor += 1
                if re.search('Motivo:', i):
                    count = 1
                if count == 1:
                    motivo.append(cart_ver[valor])
                    valor += 1
                if count == 0 and motivo != []:
                    cart['Motivo'] = ' '.join(motivo)
                    motivo = []
                    cartoes_vermelho[len(cartoes_vermelho) + 1] = cart
            except:
                pass

        
        count = -1
        cart = {}
        cartoes_amarelo = {}
        valor = 0
        motivo = []
        for i in cart_amar:
            #print(i)
            #sprint(valor)
            cart = {}
            if re.search('\d+:\d+', i):
                count = 0
                if count == 0:
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
            if count == 0 and motivo != []:
                cart['Motivo'] = ' '.join(motivo)
                motivo = []
                cartoes_amarelo[len(cartoes_amarelo) + 1] = cart
            
            
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
                        comissao_mandante[i] = ''    
                except:
                    comissao_mandante[i] = ''
            elif count == 2:
                try:
                    if list(comissao_visitante.values())[-1] == '':
                        comissao_visitante[list(comissao_visitante.keys())[-1]] = i
                    else:
                        comissao_visitante[i] = ''    
                except:
                    comissao_visitante[i] = ''

        print(comissao_mandante)
        print(comissao_visitante)