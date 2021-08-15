import os
import pandas as pd
import json
import re
from datetime import datetime
from PyPDF2 import PdfFileReader

class OjetoJogo:

    def pag_um(pag_um):
        jogo_num = int(pag_um.extractText().splitlines()[0].split(': ')[-1])
        campeonato = pag_um.extractText().splitlines()[4]
        rodada = int(pag_um.extractText().splitlines()[6])
        jogo = pag_um.extractText().splitlines()[8]
        data = pag_um.extractText().splitlines()[10]
        hora = pag_um.extractText().splitlines()[12]
        estadio = pag_um.extractText().splitlines()[14]

