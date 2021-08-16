import os
import json
from extract import ExtractJogo
from transform import ObjetoJogo

arquivos = os.listdir("./PDFs/")
for arquivo in arquivos:
    sumula = ExtractJogo.sumula(f"./PDFs/{arquivo}")
    jogo = ObjetoJogo.transform(sumula)
    #print(json.dumps(jogo, sort_keys=False, indent=4, separators=(',', ': ')))
