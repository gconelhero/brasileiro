import os
import pandas as pd
import json
import re
from datetime import datetime
from PyPDF2 import PdfFileReader


arquivos = os.listdir(".\\PDFs\\")
for arquivo in arquivos:
    pdf = PdfFileReader(f".\\PDFs\\{arquivo}")
    print(pdf.extractText())