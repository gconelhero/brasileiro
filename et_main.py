import os
import json
import shutil
import sys, traceback
from extract import ExtractJogo
from transform import ObjetoJogo


class Etl:
    
    def etMain(arquivo):
        try:
            print(arquivo) # TERMINAL
            sumula = ExtractJogo.sumula(f"./PDFs/{arquivo}")
            
            jogo = ObjetoJogo.transform(sumula)
            objeto_jogo = json.dumps(jogo, 
                                    ensure_ascii=False, sort_keys=False, 
                                    indent=4, separators=(',', ': '))

            
            with open(f'./json_files/{arquivo[:-4]}.json', 'w') as json_file:
                json_file.write(objeto_jogo)
            
            os.remove(f"./PDFs/{arquivo}")
                
        except:
            with open('./logs/log.txt',  'a') as log:
                log.write(f"\n{arquivo}:\n")
                traceback.print_exc(file=log)
                traceback.print_exc(file=sys.stdout)
            
            shutil.move(f'./PDFs/{arquivo}', f"./pdf_fail/{arquivo}")
