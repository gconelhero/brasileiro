import os
import json
from extract import ExtractJogo
from transform import ObjetoJogo

arquivos = os.listdir("./PDFs/")
for arquivo in arquivos:
    sumula = ExtractJogo.sumula(f"./PDFs/{arquivo}")
    jogo = ObjetoJogo.transform(sumula)
    objeto_jogo = json.dumps(jogo, 
                            ensure_ascii=False, sort_keys=False, 
                            indent=4, separators=(',', ': '))
    #print(objeto_jogo)
    print(objeto_jogo[0:35])
