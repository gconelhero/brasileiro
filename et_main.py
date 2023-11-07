import os
import shutil
import sys
import traceback

from scraper import Scraper
from extract import ExtractPdf
from transform import ObjetoJogo
from mongo_load import DataBase

class Etl:

    def __init__(self, ano, jogo):
        scraper = Scraper(ano, jogo)
        self.arquivo = scraper.pdf()

    def etMain(self):
        arquivo = self.arquivo
        try:
            print(arquivo)
            sumula = ExtractPdf(f"./PDFs/{arquivo}")
            cabecalho = sumula.cabecalho()
            arbitragem = sumula.arbitragem()
            cronologia = sumula.cronologia()
            jogadores = sumula.jogadores()
            comissao = sumula.comissao()
            gols = sumula.gols()
            cartoes_amarelos = sumula.cartoes()
            cartoes_vermelhos = sumula.cartoes_()
            substituicoes = sumula.substituicoes()
            jogo = ObjetoJogo(cabecalho, arbitragem, cronologia, jogadores, comissao, gols, cartoes_amarelos, cartoes_vermelhos, substituicoes)
            jogo = jogo.transform()
            for k, v in jogo.items():
                mongo_load = DataBase(k)
                objeto = v
                if type(objeto) == list:
                    for i in v:                        
                        mongo_load.insert(i)
                else:
                    mongo_load.insert(v)
            os.remove(f"./PDFs/{arquivo}")
        except:
            shutil.move(f'./PDFs/{arquivo}', f"./pdf_fail/{arquivo}")
            with open('./logs/log.txt',  'a') as log:
                log.write(f"\n{arquivo}:\n")
                traceback.print_exc(file=log)
                traceback.print_exc(file=sys.stdout)

if __name__ == '__main__':
    jogo = 1
    ano = 2018
    while jogo < 140 and ano < 2023:
        etl = Etl(ano, jogo)
        if jogo == 380:
            jogo = 1
            ano += 1
        else:
            jogo += 1
        etl.etMain()