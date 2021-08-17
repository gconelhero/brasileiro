import requests
import sys, traceback, os
import filetype
from PyPDF2 import PdfFileReader
from et_main import Etl


flag = True
jogo = 1
ano = 2019
jogo_nulo = 0
while flag:
    try:
        url = f'https://conteudo.cbf.com.br/sumulas/{ano}/142{jogo}se.pdf'
        response = requests.get(url)
        pdf_content = response.content
        pdf_file = open(f'./PDFs/jogo_{jogo}_{ano}.pdf', 'wb')
        pdf_file.write(response.content)
        type_pdf = filetype.guess(f'./PDFs/jogo_{jogo}_{ano}.pdf')
        pdf_file.close()
        try:
            if type_pdf.MIME == 'application/pdf':
                Etl.etMain(f'jogo_{jogo}_{ano}.pdf')
                jogo_nulo = 0
                

        except:
            jogo_nulo += 1
            os.remove(f'./PDFs/jogo_{jogo}_{ano}.pdf')
            with open('jogos_n_existente.txt', 'a') as ne:
                ne.write(f'{url}\n')
            if jogo > 385:
                ano += 1
                jogo = 0
            if jogo_nulo == 5:
                flag = False
                

        jogo += 1
    
    except:
        with open('log_scrap.txt',  'a') as log:
                log.write(f"\n{jogo}_{ano}:\n")
                traceback.print_exc(file=log)
                traceback.print_exc(file=sys.stdout)
                jogo += 1
        
        flag = False