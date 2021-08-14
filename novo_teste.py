import os
from pdftables import PDFDocument

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
    teste = PDFDocument(pdf)

