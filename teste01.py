#PDFminer
from io import StringIO
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter

import tabula

import pandas as pd

import json


pdf = ".\\PDFs\\Jogo17.pdf"

leitor = open(pdf, 'rb')

parser = PDFParser(leitor)
document = PDFDocument(parser,)

output_string = StringIO()
rsrcmgr = PDFResourceManager()
device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
interpreter = PDFPageInterpreter(rsrcmgr, device)

for page in PDFPage.create_pages(document):
        interpreter.process_page(page)
saida = output_string.getvalue()
#print(saida)

leitor = tabula.read_pdf(pdf, pages='all')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
'''
contador = 0
for i in leitor:
    df = pd.DataFrame(leitor[contador])
    print(df)
    contador += 1
'''
df = pd.DataFrame(leitor[0])
print(df)
