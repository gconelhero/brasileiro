import os
import re
import json
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
            'AT - Assistente TécnicoAT - Assistente Técnico','Página 2/3',
            'Entrou', 'Saiu', 'Substituições', 'Página 3/3', '3 / 3', 
            'Powered by TCPDF (www.tcpdf.org)',]

class ExtractJogo:

    def sumula(arquivo):
        pdf = PdfFileReader(arquivo)
        paginas = ''
        for i in range(pdf.getNumPages()):
            pagina = pdf.getPage(i)
            paginas += pagina.extractText()

        pag_um = pdf.getPage(0)

        jogo_num = int(pag_um.extractText().splitlines()[0].split(': ')[-1])
        campeonato = pag_um.extractText().splitlines()[4]
        rodada = int(pag_um.extractText().splitlines()[6])
        jogo = pag_um.extractText().splitlines()[8]
        data = pag_um.extractText().splitlines()[10]
        hora = pag_um.extractText().splitlines()[12]
        estadio = pag_um.extractText().splitlines()[14]

        cabecalho = [jogo_num, campeonato, rodada, jogo, data, hora, estadio]
        
        return ExtractJogo.extract(cabecalho, paginas)

    def extract(cabecalho, paginas):
        count = -1000
        lista_arbitragem = []
        lista_cronologia = []
        jogadores = []
        for i in paginas.splitlines():
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


        count = -1000
        comissao = []
        gols = []
        cart_amar = []
        cart_ver = []
        for i in paginas.splitlines():
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
                if i == flag[7]:
                    count = -1000
                if count == 6 and i not in reject:
                    if re.search('Publicação da Súmula:', i):
                        pass
                    elif re.search('Nada houve de anormal.', i):
                        pass
                    elif re.search('Emissão desta via:', i):
                        pass
                    elif re.search('2 / 3', i):
                        pass
                    else:
                        cart_ver.append(i)
            except: 
                pass
        

    
        count = -1000
        obs = []
        substituicao = []    
        for i in paginas.splitlines():
            try:
                if i == flag[7]:
                    count = 7
                if count == 7 and i not in reject:
                    obs.append(i)
                if i == flag[8]:
                    count = 8 
                if count == 8 and i not in reject:
                    substituicao.append(i)

            except:
                pass
        
        return [cabecalho, lista_arbitragem, lista_cronologia, jogadores, comissao, gols, cart_amar, cart_ver, obs, substituicao]