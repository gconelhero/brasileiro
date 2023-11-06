import re
from datetime import datetime

from PyPDF2 import PdfFileReader
import pandas as pd
import fitz
import tabula

from scraper import Scraper

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

class ExtractPdf:
    
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.pdf = PdfFileReader(self.arquivo)
        self.paginas = ''
        for i in range(self.pdf.getNumPages()):
            pagina = self.pdf.getPage(i)
            self.paginas += pagina.extractText()
        
    def cabecalho(self):
        pag_um = self.pdf.getPage(0)
        jogo_num = int(re.findall(r'(Jogo+:?\s?)+([0-9]*)?', pag_um.extractText())[0][-1])
        campeonato = re.search('Campeonato (.+)', pag_um.extractText()).group().split('Rodada: ')
        rodada = int(campeonato[-1])
        campeonato = campeonato[0]
        jogo = re.findall('Jogo: (.+)', pag_um.extractText())[-1]
        self.mandante = jogo.replace(' X ', 'X').split('X')[0]
        self.visitante = jogo.replace(' X ', 'X').split('X')[-1]
        data_h_e = re.search('Data: (.+)', pag_um.extractText()).group().split('Horário: ')
        data = data_h_e[0].split('Data: ')[-1]
        data = data.replace(' ', '')
        self.data = datetime.strptime(data, "%d/%m/%Y").date()
        hora = data_h_e[-1].split('Estádio')[0].replace(' ', '') + ':00 -0300'
        hora = datetime.strptime(hora, "%H:%M:%S %z").timetz()
        estadio = data_h_e[-1].split('Estádio: ')[-1]
        cabecalho = [jogo_num, campeonato, rodada, jogo, self.data, hora, estadio]
        
        return cabecalho

    def arbitragem(self):
        lista_arbitragem = []
        paginas = self.paginas.splitlines()
        for i in paginas[paginas.index('Arbitragem'):]:
            if i != 'Cronologia' and i not in reject:
                lista_arbitragem.append(i)
            elif i == 'Cronologia':
                break

        return lista_arbitragem

    def cronologia(self):
        lista_cronologia = []
        paginas = self.paginas.splitlines()
        for i in paginas[paginas.index('Cronologia'):]:
            if i != 'Relação de Jogadores' and i not in reject:
                lista_cronologia.append(i)
            elif i == 'Relação de Jogadores':
                break

        return lista_cronologia
        
    def jogadores(self):
        arquivo = self.arquivo
        arquivo_fitz = fitz.open(arquivo)
        page = arquivo_fitz.load_page(0)
        pdf = page.get_text()
        # fitz.area = (left, top, right, bottom)
        num = page.search_for('Nº')
        cbf = page.search_for('CBF')
        bottom = page.search_for('T = Titular')
        # tabula.area = (top, left, bottom, right)
        mandante_area = (int(num[0][1]), int(num[0][0])-5, int(bottom[0][1]), int(cbf[-2][2])+18)
        visitante_area = (int(num[1][1]), int(num[1][0])-5, int(bottom[0][1]), int(cbf[-1][2])+18)
        mandante_plantel = tabula.read_pdf(arquivo, pages='1', area=mandante_area)
        visitante_plantel = tabula.read_pdf(arquivo, pages='1', area=visitante_area)
        mandante_df = pd.DataFrame(mandante_plantel[0]).dropna()
        visitante_df = pd.DataFrame(visitante_plantel[0]).dropna()
        self.jogadores = {self.mandante: {}, self.visitante: {}}
        for i, row in mandante_df.iterrows():
            numero = int(row['No'])
            apelido = row['Apelido']
            nome = row['Nome Completo']
            t_r = row['T/R']
            if 'g' in t_r:
                t_r = 'T(g)'
                for i in self.jogadores[self.mandante].values():
                    if 'T(g)' in i.values():
                        t_r = 'R(g)'
            elif 'R' in t_r:
                t_r = 'R'
            elif 'T' in t_r:
                t_r = 'T'
            p_a = row['P/A']
            cbf = int(row['CBF'])
            scraper = Scraper(self.data.year, None)
            jogador = scraper.jogador(cbf, apelido, nome)
            self.jogadores[self.mandante][numero] = {'apelido': jogador['apelido'], 
                                                    'nome': jogador['nome'], 
                                                    'T/R': t_r, 
                                                    'P/A': p_a, 
                                                    'id_cbf': jogador['id_cbf']
                                                    }
        for i, row in visitante_df.iterrows():
            numero = int(row['No'])
            apelido = row['Apelido']
            nome = row['Nome Completo']
            t_r = row['T/R']
            if 'g' in t_r:
                t_r = 'T(g)'
                for i in self.jogadores[self.mandante].values():
                    if 'T(g)' in i.values():
                        t_r = 'R(g)'
            elif 'R' in t_r:
                t_r = 'R'
            elif 'T' in t_r:
                t_r = 'T'
            p_a = row['P/A']
            cbf = int(row['CBF'])
            scraper = Scraper(self.data.year, None)
            jogador = scraper.jogador(cbf, apelido, nome)
            self.jogadores[self.visitante][numero] = {'apelido': jogador['apelido'], 
                                                    'nome': jogador['nome'], 
                                                    'T/R': t_r, 
                                                    'P/A': p_a, 
                                                    'id_cbf': jogador['id_cbf']
                                                    }

        return self.jogadores

    def comissao(self):
        self.comissao = {self.mandante: {}, self.visitante: {}}
        arquivo = self.arquivo
        arquivo_fitz = fitz.open(arquivo)
        page = arquivo_fitz.pages()
        paginas = ''
        for p in page:
            paginas += p.get_text()
        paginas = paginas.splitlines()
        paginas = paginas[paginas.index('Comissão Técnica')+1:paginas.index('Gols')]
        count = 1
        for i, s in enumerate(paginas):
            if re.search(r':\s?\S\D*', s):
                paginas[i] = s.split(': ')[-1]
                s = re.search(r'\D+: ', s).group()
                paginas.insert(i, s)
        for i, s in enumerate(paginas):
            if re.search(self.visitante, s):
                index = i + 1
                break
            else:
                if s != self.mandante:
                    if re.search(r'\w+:', s):
                        if s.split(': ')[0] in self.comissao[self.mandante].keys():
                            s = s.split(': ')[0]
                            for x in self.comissao[self.mandante].keys():
                                if s in x:
                                    count += 1
                            if '-' in paginas[i + 1]:
                                paginas[i + 1] = paginas[i + 1].split(' - ')[0]
                            self.comissao[self.mandante][s+f' {str(count)}'] = paginas[i + 1]
                            count = 1
                        else:
                            if '-' in paginas[i + 1]:
                                paginas[i + 1] = paginas[i + 1].split(' - ')[0]
                            self.comissao[self.mandante][s.split(':')[0]] = paginas[i + 1]
        count = 1
        for i, s in enumerate(paginas[index:], index):
            if re.search(r':\s?\S\D*', s):
                i = i + 1
            if re.search(r'\w+:', s):
                if s.split(': ')[0] in self.comissao[self.visitante].keys():
                    s = s.split(': ')[0]
                    for x in self.comissao[self.visitante].keys():
                        if s in x:
                            count += 1
                    if '-' in paginas[i + 1]:
                        paginas[i + 1] = paginas[i + 1].split(' - ')[0]
                    self.comissao[self.visitante][s+f' {str(count)}'] = paginas[i + 1]
                    count = 1
                else:
                    if '-' in paginas[i + 1]:
                        paginas[i + 1] = paginas[i + 1].split(' - ')[0]
                    self.comissao[self.visitante][s.split(':')[0]] = paginas[i + 1]

        return self.comissao

    def gols(self):
        gols = []
        arquivo = self.arquivo
        arquivo_fitz = fitz.open(arquivo)
        for i, p in enumerate(arquivo_fitz.pages()):
            page_tabula = i + 1
            tempo = p.search_for('Tempo')
            equipe = p.search_for('Equipe')
            bottom = p.search_for('NR = Normal')
            if tempo != [] and equipe != [] and bottom != []:
                break
        try:
            gols_area = (int(tempo[0][1]), int(tempo[0][0])-20, int(bottom[0][1]), int(equipe[0][2])+50)
            gols_tabela = tabula.read_pdf(arquivo, pages=f'{page_tabula}', area=gols_area)
            gols_df = pd.DataFrame(gols_tabela[0]).dropna()
        except:
            print('Não houve gols')
            return gols
        for i, row in gols_df.iterrows():
            if re.search(r'\+', row['Tempo']):
                minutos_acrescimo = re.search(r'\d+', row['Tempo']).group()
                minutos_acrescimo = 45 + int(minutos_acrescimo)
                minutos = datetime.strptime(f'{minutos_acrescimo}:00', "%M:%S").time()
            else:                
                minutos = datetime.strptime(row['Tempo'], "%M:%S").time()
            tempo = row['1T/2T']
            num = int(row['No'])
            tipo = row['Tipo']
            nome = ''
            equipe = row['Equipe']
            for x in self.jogadores.keys():
                re_equipe = re.search(equipe.split('/')[0], x)
                if re_equipe:
                    equipe = x
                    id_cbf = self.jogadores[equipe][num]['id_cbf']
            gols.append({'minuto': minutos.isoformat(), '1T/2T': tempo, 'id_cbf': id_cbf, 'equipe': equipe})

        return gols

    def cartoes(self):
        minutos = None
        tempo = None
        num = None
        nome = None
        equipe = None
        motivo = None
        cartoes_amarelos = []
        arquivo = self.arquivo
        arquivo_fitz = fitz.open(arquivo)
        page = arquivo_fitz.pages()
        paginas = ''
        for p in page:
            paginas += p.get_text()
        paginas = paginas.splitlines()
        paginas = paginas[paginas.index('Cartões Amarelos')+1:paginas.index('Cartões Vermelhos')]
        for index, i in enumerate(paginas):
            if re.search(r'^\d+:\d+', i) and len(i) < 7:
                minutos = i
                if re.search(r'^\+\d+:\d+', i):
                    minutos_acrescimo = re.search(r'\d+', i).group()
                    minutos_acrescimo = 45 + int(minutos_acrescimo)
                    minutos = datetime.strptime(f'{minutos_acrescimo}:00', '%M:%S').time()
                else:
                    minutos = datetime.strptime(minutos, '%M:%S').time()
                if re.search(r'\dT', paginas[index + 1]):
                    tempo = paginas[index + 1]
                if re.match(r'INT', paginas[index + 1]):
                    tempo = paginas[index + 1]
                if re.search(r'^\d{1,2}$', paginas[index + 2]):
                    num = int(re.search(r'^\d{1,2}$', paginas[index + 2]).group())
                    nome = paginas[index + 3]
                    if re.search(paginas[index + 4].split('/')[0], self.mandante):
                        nome = self.jogadores[self.mandante][num]['nome']
                        equipe = self.mandante
                    elif re.search(paginas[index + 4].split('/')[0], self.visitante):
                        nome = self.jogadores[self.visitante][num]['nome']
                        equipe = self.visitante
                elif re.search(r'^\D{1,2}$', paginas[index + 2]):
                    num = re.search(r'^\D{1,2}$', paginas[index + 2]).group()
                    nome = paginas[index + 3]
                    if re.search(paginas[index + 4].split('/')[0], self.mandante):
                        equipe = self.mandante
                    elif re.search(paginas[index + 4].split('/')[0], self.visitante):
                        equipe = self.visitante
                if equipe:        
                    for k, v in self.comissao[equipe].items():
                        if re.search(nome.casefold(), v.casefold()) or re.search(v.casefold(), nome.casefold()):
                            num = k
                            nome = v
            if re.search(r'^Motivo: A\d*\W?\d*\W?', i):
                motivo = re.search(r'^Motivo: A\d*\W?\d*\W?', i).group().split(': ')[-1]
            elif re.search(r'^Motivo: \D*', i):
                motivo = re.search(r'^Motivo: \D*', i).group().split(': ')[-1]
            if num and tempo and nome and motivo:
                if self.jogadores[equipe][num]:
                    cartoes_amarelos.append({'minuto': minutos.isoformat(), '1T/2T': tempo, 'id_cbf': self.jogadores[equipe][num]['id_cbf'], 'motivo': motivo})
                else:
                    cartoes_amarelos.append({'minuto': minutos.isoformat(), '1T/2T': tempo, 'id_cbf': num, 'motivo': motivo})
                num = None
            else:
                pass

        return cartoes_amarelos

    def cartoes_(self):
        minutos = None
        tempo = None
        num = None
        nome = None
        equipe = None
        motivo = None
        cartoes_vermelhos = []
        arquivo = self.arquivo
        arquivo_fitz = fitz.open(arquivo)
        page = arquivo_fitz.pages()
        paginas = ''
        for p in page:
            paginas += p.get_text()
        paginas = paginas.splitlines()
        paginas = paginas[paginas.index('Cartões Vermelhos')+1:paginas.index('Ocorrências / Observações')]
        for index, i in enumerate(paginas):
            if re.search(r'\d+:\d+', i) and len(i) < 7:
                minutos = i
                if re.search(r'\+\d+:\d+', i):
                    minutos_acrescimo = re.search(r'\d+', i).group()
                    minutos_acrescimo = 45 + int(minutos_acrescimo)
                    minutos = datetime.strptime(f'{minutos_acrescimo}:00', '%M:%S').time()
                else:
                    minutos = datetime.strptime(minutos, '%M:%S').time()
                if re.search(r'\dT', paginas[index + 1]):
                    tempo = paginas[index + 1]
                if re.match(r'INT', paginas[index + 1]):
                    tempo = paginas[index + 1]
                if re.search(r'^\d{1,2}$', paginas[index + 2]):
                    num = int(re.search(r'^\d{1,2}$', paginas[index + 2]).group())
                    nome = paginas[index + 3].split(' - ')[0]
                    condicao = paginas[index + 4]
                    if re.search(paginas[index + 3].split(' - ')[-1].split('/')[0], self.mandante):
                        nome = self.jogadores[self.mandante][num]['nome']
                        equipe = self.mandante
                    elif re.search(paginas[index + 3].split(' - ')[-1].split('/')[0], self.visitante):
                        nome = self.jogadores[self.visitante][num]['nome']
                        equipe = self.visitante
                elif re.search(r'^\w{1,2}$', paginas[index + 2]):
                    num = re.search(r'^\w{1,2}$', paginas[index + 2]).group()
                    if len(paginas) - 1 >= index + 2:
                        nome = paginas[index + 3]
                        condicao = paginas[index + 4]
                    if re.search(paginas[index + 3].split(' - ')[-1].split('/')[0], self.mandante):
                        equipe = self.mandante
                    elif re.search(paginas[index + 3].split(' - ')[-1].split('/')[0], self.visitante):
                        equipe = self.visitante
                if equipe:
                    for k, v in self.comissao[equipe].items():
                        if re.search(nome.casefold(), v.casefold()) or re.search(v.casefold(), nome.casefold()):
                            num = k
                            nome = v
            if re.search(r'^Motivo: V\d*\W?\d*\W?', i):
                motivo = re.search(r'^Motivo: V\d*\W?\d*\W?', i).group().split(': ')[-1]
            elif re.search(r'^Motivo: \D*', i):
                motivo = re.search(r'^Motivo: \D*', i).group().split(': ')[-1]
            if num and tempo and nome and motivo:
                if self.jogadores[equipe][num]:
                    cartoes_vermelhos.append({'minuto': minutos.isoformat(), '1T/2T': tempo, 'id_cbf': self.jogadores[equipe][num]['id_cbf'], 'condicao': condicao, 'motivo': motivo, 'equipe': equipe}) 
                else:
                    cartoes_vermelhos.append({'minuto': minutos.isoformat(), '1T/2T': tempo, 'id_cbf': num, 'condicao': condicao, 'motivo': motivo, 'equipe': equipe})
                num = None
            else:
                pass

        return cartoes_vermelhos
    
    def substituicoes(self):
        minutos = None
        tempo = None
        num_entrou = None
        num_saiu = None
        nome_entrou = None
        nome_saiu = None
        equipe = None
        substituicoes_ = []
        arquivo = self.arquivo
        arquivo_fitz = fitz.open(arquivo)
        page = arquivo_fitz.pages()
        paginas = ''
        for p in page:
            paginas += p.get_text()
        paginas = paginas.splitlines()
        paginas = paginas[paginas.index('Substituições')+1:]
        for index, i in enumerate(paginas):
            if re.search(r'^\d+:\d+', i) and len(i) < 7:
                minutos = i
                if re.search(r'\+\d+:\d+', i):
                    minutos_acrescimo = re.search(r'\d+', i).group()
                    minutos_acrescimo = 45 + int(minutos_acrescimo)
                    minutos = datetime.strptime(f'{minutos_acrescimo}:00', '%M:%S').time()
                else:
                    minutos = datetime.strptime(minutos, '%M:%S').time()
                if re.search(r'\dT', paginas[index + 1]):
                    tempo = paginas[index + 1]
                if re.match(r'INT', paginas[index + 1]):
                    tempo = paginas[index + 1]
                if minutos:
                    num_entrou = int(paginas[index + 3].split(' - ')[0])
                    nome_entrou = paginas[index + 3].split(' - ')[-1]
                    num_saiu = int(paginas[index + 4].split(' - ')[0])
                    nome_saiu = paginas[index + 4].split(' - ')[-1]
                if re.search(paginas[index + 2].split('/')[0], self.mandante):
                    nome_entrou = self.jogadores[self.mandante][num_entrou]['nome']
                    nome_saiu = self.jogadores[self.mandante][num_saiu]['nome']
                    equipe = self.mandante
                elif re.search(paginas[index + 2].split('/')[0], self.visitante):
                    nome_entrou = self.jogadores[self.visitante][num_entrou]['nome']
                    nome_saiu = self.jogadores[self.visitante][num_saiu]['nome']
                    equipe = self.visitante
            if equipe and num_entrou and tempo and nome_entrou:
                id_cbf = self.jogadores[equipe][num_entrou]['id_cbf']
                id_cbf_ = self.jogadores[equipe][num_saiu]['id_cbf']
                substituicoes_.append({'minuto': minutos.isoformat(), '1T/2T': tempo, 'entrou': id_cbf, 'saiu': id_cbf_, 'equipe': equipe})
                equipe = None
            else:
                pass
            
        return substituicoes_