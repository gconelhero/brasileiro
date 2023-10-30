# Standard
import os
import shutil
import sys
import json
import traceback
# Internas
from scraper import Scraper
from extract import ExtractPdf
from transform import ObjetoJogo


class Etl:

    def __init__(self, ano, jogo):
        scraper = Scraper(ano, jogo)
        self.arquivo = scraper.pdf()

    def etMain(self):
        arquivo = self.arquivo
        try:
            print(arquivo) # TERMINAL
            sumula = ExtractPdf(f"./PDFs/{arquivo}")
            cabecalho = sumula.cabecalho()
            #print(cabecalho)
            #arbitragem = sumula.arbitragem()
            #print(arbitragem)
            #cronologia = sumula.cronologia()
            #print(cronologia)
            jogadores = sumula.jogadores()
            comissao = sumula.comissao()
            #gols = sumula.gols()
            cartoes_amarelos = sumula.cartoes()
            print(cartoes_amarelos)
            cartoes_vermelhos = sumula.cartoes_()
            print(cartoes_vermelhos)
            substituicoes = sumula.substituicoes()
            print(substituicoes)
            #jogo = ObjetoJogo(cabecalho, arbitragem, cronologia, jogadores)
            #jogo = jogo.transform()
            #objeto_jogo = json.dumps(jogo, 
            #                        ensure_ascii=False, sort_keys=False, 
            #                        indent=4, separators=(',', ': '))
            
#            with open(f'./json_files/{arquivo[:-4]}.json', 'w') as json_file:
#                json_file.write(objeto_jogo)
#            os.remove(f"./PDFs/{arquivo}")
            
        except:
            shutil.move(f'./PDFs/{arquivo}', f"./pdf_fail/{arquivo}")
            with open('./logs/log.txt',  'a') as log:
                log.write(f"\n{arquivo}:\n")
                traceback.print_exc(file=log)
                traceback.print_exc(file=sys.stdout)

import random
if __name__ == '__main__':
    jogo = 1
    ano = 2014
    while jogo < 140 and ano < 2023:
        etl = Etl(ano, jogo)
        if jogo == 380:
            jogo = 1
            ano += 1
        else:
            jogo += 1
        etl.etMain()
#    for i in range(100):
#        etl = Etl(2014, 1)
#        #etl = Etl(random.randint(2014, 2022), random.randint(1, 380))
        #etl.etMain()
