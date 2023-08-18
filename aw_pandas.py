import requests
import re
from datetime import datetime

import pandas as pd
import fitz
import tabula
from bs4 import BeautifulSoup


arquivo = './pdf_fail/jogo_1_2018.pdf'
arquivo_fitz = fitz.open('./pdf_fail/jogo_1_2018.pdf')
coordenada = []
page = arquivo_fitz.load_page(0)
pdf = page.get_text()
teste = page.rect
num = page.search_for('Nº')
cbf = page.search_for('CBF')
bottom = page.search_for('T = Titular')
mandante_area = (int(num[0][1]), int(num[0][0])-5, int(bottom[0][1]), int(cbf[2][2])+9)
visitante_area = (int(num[1][1]), int(num[1][0])-5, int(bottom[0][1]), int(cbf[3][2])+9)
# fitz.area = (esquerda, altura, direita, baixo)
# tabula.area = (top, esquerda, baixo, direita)
mandante_plantel = tabula.read_pdf(arquivo, pages='1', area=mandante_area)
visitante_plantel = tabula.read_pdf(arquivo, pages='1', area=visitante_area)
mandante_df = pd.DataFrame(mandante_plantel[0]).dropna()
visitante_df = pd.DataFrame(visitante_plantel[0]).dropna()
for x, y