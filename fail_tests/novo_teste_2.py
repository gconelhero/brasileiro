import os
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

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

    output_string = StringIO()
    with open(pdf, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    print(output_string.getvalue())
