import os
import sys
import requests
import re
from datetime import datetime
from unidecode import unidecode
import traceback

import filetype
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, ano, jogo):
        dirs = os.listdir(".")
        self.ano = ano
        self.jogo = jogo
        try:
            if "PDFs" not in dirs:
                os.mkdir("./PDFs")
            if "pdf_fail" not in dirs:
                os.mkdir("./pdf_fail")
            if "logs" not in dirs:
                os.mkdir("./logs")
        except Exception as erro:
            print(f'\n{erro}\n DIRETÓRIOS NÃO ENCONTRADOS')
            with open('./logs/log_scrap.txt',  'a') as log:
                log.write(f"\n{jogo}_{ano}_Scraper_init:\n")
                traceback.print_exc(file=log)
                traceback.print_exc(file=sys.stdout)

    def pdf(self):
        flag = True
        ano = self.ano
        jogo = self.jogo
        jogo_nulo = 0
        while flag:
            try:
                url = f'https://conteudo.cbf.com.br/sumulas/{ano}/142{jogo}se.pdf'
                response = requests.get(url)
                pdf_file = open(f'./PDFs/jogo_{jogo}_{ano}.pdf', 'wb')
                pdf_file.write(response.content)
                type_pdf = filetype.guess(f'./PDFs/jogo_{jogo}_{ano}.pdf')
                pdf_file.close()
                try:
                    if type_pdf.MIME == 'application/pdf':
                        arquivo = f'jogo_{jogo}_{ano}.pdf'
                        jogo_nulo = 0

                        return arquivo

                except:
                    jogo_nulo += 1
                    os.remove(f'./PDFs/jogo_{jogo}_{ano}.pdf')
                    with open('./logs/jogos_nao_existentes.txt', 'a') as ne:
                        ne.write(f'{url}\n')
                    if jogo > 380:
                        ano += 1
                        jogo = 0
                    elif jogo_nulo == 5:
                        flag = False
                    elif ano == 2023 and jogo > 160:
                        flag = False
                jogo += 1
            except:
                with open('./logs/log_scrap.txt',  'a') as log:
                        log.write(f"\n{jogo}_{ano}_Scraper_pdf:\n")
                        traceback.print_exc(file=log)
                        traceback.print_exc(file=sys.stdout)
                        jogo += 1
                flag = False

    def jogador(self, id_jogador, apelido, nome):
        clube = ''
        id_jogador = id_jogador
        ano_sumula = self.ano
        apelido_sumula = apelido.replace(' ...', '...')
        nome_sumula = nome.replace(' ...', '...')
        ano_sumula = datetime.strptime(str(ano_sumula), "%Y").date()
        url = f"https://www.cbf.com.br/futebol-brasileiro/atletas/{id_jogador}?exercicio={ano_sumula}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        apelido = soup.find('h3', class_='hidden-xs hidden-sm').text
        nome = soup.find('span', class_='nome_completo').text
        nascimento = datetime.strptime(soup.find_all('span', class_='valor')[1].text, "%d/%m/%Y").date()
        jogador_partidas = int(re.search(r'\d+', soup.find('div', class_='dentro-campo__item dentro-campo__item--partidas').text).group())
        jogador_gols = int(re.search(r'\d+', soup.find('div', class_='dentro-campo__item dentro-campo__item--gols').text).group())
        jogador_amarelos = int(re.search(r'\d+', soup.find('div', class_='dentro-campo__item dentro-campo__item--cartaoamarelo').text).group())
        jogador_vermelhos = int(re.search(r'\d+', soup.find('div', class_='dentro-campo__item dentro-campo__item--cartaovermelho').text).group())
        nome_split = ' '.join(nome_sumula.split(' '))
        nome_i = ''
        try:
            if re.search(unidecode(apelido_sumula).casefold(), unidecode(apelido).casefold()):
                flag = True
            elif re.search(unidecode(nome_sumula).casefold(), unidecode(nome).casefold()):
                flag = True
            else:
                for i in nome_split:
                    nome_i += i
                    nome_regex = re.search(unidecode(nome_i).casefold(), unidecode(nome).casefold())
                    if len(nome_regex.group().split(' ')) > 2 and nome_regex:
                        flag = True
                        break
            if flag:
                idade = ano_sumula.year - nascimento.year
                jogador = {'apelido': apelido, 
                            'nome': nome,
                            'nascimento': nascimento.isoformat(), 
                            'partidas': jogador_partidas, 
                            'gols': jogador_gols,
                            'amarelos': jogador_amarelos,
                            'vermelhos': jogador_vermelhos, 
                            'equipe': clube,
                            'ano': ano_sumula.isoformat(),
                            'idade': int(idade), 
                            'id_cbf': id_jogador
                            }
        except:
            with open('./logs/log_scrap.txt',  'a') as log:
                log.write(f"\n{self.jogo}_{self.ano}_Scraper_API:\n")
                traceback.print_exc(file=log)
                traceback.print_exc(file=sys.stdout)

        return jogador