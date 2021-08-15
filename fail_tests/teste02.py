import os
import camelot
import json
import pandas
from pdftables.TableFinder import pdftoxml

pandas.set_option('display.max_columns', None)
pandas.set_option('display.max_rows', None)

arquivos = os.listdir('.\\PDFs\\')
count = 1
for arquivo in arquivos:
    count += 1
    '''
    tables = camelot.read_pdf(f'.\\PDFs\\{arquivo}', flavor='stream', pages='1', row_tol=1)
    print(tables)
    table_two = tables[1]
    print(table_two.df)
    #camelot.plot(tables[0], kind='contour').show()
    '''
    pdf = f'.\\PDFs\\{arquivo}'
    teste = pdf_document(pdf)

    page = teste.get_page(1)
    tables = page_to_tables(page)
    print(tables)