# brasileiro
Project related to the study of data analysis with Python and Mongo.

Objectives:
* Extract, transform and load the data contained in the Brazilian championship scores for further analysis.
* Create an API to share this data with other applications.

![2](https://github.com/gconelhero/brasileiro/assets/26088216/561b8f9d-89b4-4cbe-affa-1a69c31eb367)

Run:<br>
`git clone https://github.com/gconelhero/brasileiro`<br>
`cd brasileiro`<br>
`python3 -m pip install -r requirements.txt`<br>
`python3 et_main.py`<br>

Install and config MongoDB:<br>
`https://docs.mongodb.com/manual/installation/`<br>
`https://docs.mongodb.com/manual/reference/configuration-options/`<br>

DataBase:<br>
`brasileiro`<br>
Collection:<br>
`jogos`<br>

Change connection parameters in `mongo_load.py`:<br>
`host='<IP DO SEU MongoDB>'`<br>

Inserting JSON files into the collection:<br>
`python3 mongo_load.py`<br>

# Unfortunately PDFs have ill-defined structures and irregular patterns.

![2](https://github.com/gconelhero/brasileiro/assets/26088216/8c482e73-7d39-40fa-bca2-cb5161eb5bf2)

{'Entrada mandante 1T': datetime.time(15, 50,)
 tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=75600))), 'Atraso mandante 1T': 'Não Houve', 'Entrada visitante 1T': datetime.time(15, 50, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=75600))), 'Atraso visitante 1T': 'Não Houve', 'Início 1T': datetime.time(16, 0, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=75600))), 'Atraso início 1T': 'Não Houve', 'Término 1T': datetime.time(16, 51, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=75600))), 'Acréscimo 1T': datetime.timedelta(seconds=360), 'Entrada mandante 2T': datetime.time(17, 4, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=75600))), 'Atraso mandante 2T': 'Não Houve', 'Entrada visitante 2T': datetime.time(17, 4, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=75600))), 'Atraso visitante 2T': 'Não Houve', 'Início 2T': datetime.time(17, 4, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=75600))), 'Atraso início 2T': 'Não Houve', 'Término 2T': datetime.time(17, 56, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=75600))), 'Acréscimo 2T': datetime.timedelta(seconds=300), 'Resultado 1T': {'Mandante': 2, 'Visitante': 0}, 'Resultado Final': {'Mandate': 2, 'Visitante': 1}}

'Internacional / RS': {12: {'apelido': 'MARCELO LOMBA', 'nome': 'Marcelo Lomba do Nascimento', 'T/R': 'T(g)', 'P/A': 'P', 'id_cbf': 157264}, 4: {'apelido': 'MOLEDO', 'nome': 'Rodrigo Modesto da Silva Moledo', 'T/R': 'T', 'P/A': 'P', 'id_cbf': 173551}, 6: {'apelido': 'UENDEL', 'nome': 'Uendel Pereira Goncalves', 'T/R': 'T', 'P/A': 'P', 'id_cbf': 175320}, 8: {'apelido': 'EDENILSON', 'nome': 'Edenilson Andrade dos Santos', 'T/R': 'T', 'P/A': 'P', 'id_cbf': 306270}, 9: {'apelido': 'GUERRERO', 'nome': 'Jose Paolo Guerrero Gonzales', 'T/R': 'T', 'P/A': 'P', 'id_cbf': 420184}, 10: {'apelido': 'DALESSANDRO', 'nome': 'Andres Nicolas Dalessandro', 'T/R': 'T', 'P/A': 'P', 'id_cbf': 299481}, 15: {'apelido': 'VICTOR CUESTA', 'nome': 'Victor Leandro Cuesta', 'T/R': 'T', 'P/A': 'P', 'id_cbf': 567555}, 19: {'apelido': 'RODRIGO', 'nome': 'Rodrigo Oliveira Lindoso', 'T/R': 'T', 'P/A': 'P', 'id_cbf': 184455}, 31: {'apelido': 'HEITOR RODRIGUES', 'nome': 'Heitor Rodrigues da Fonseca', 'T/R': 'T', 'P/A': 'P', 'id_cbf': 464051}, 88: {'apelido': 'PATRICK', 'nome': 'Patrick Bezerra do Nascimento', 'T/R': 'T', 'P/A': 'P', 'id_cbf': 315585}, 99: {'apelido': 'POTTKER', 'nome': 'William de Oliveira Pottker', 'T/R': 'T', 'P/A': 'P', 'id_cbf': 301087}, 1: {'apelido': 'DANILO FERNANDES', 'nome': 'Danilo Fernandes Batista', 'T/R': 'R(g)', 'P/A': 'P', 'id_cbf': 165830}, 2: {'apelido': 'BRUNO', 'nome': 'Bruno Vieira do Nascimento', 'T/R': 'R', 'P/A': 'P', 'id_cbf': 172996}, 7: {'apelido': 'NICO LOPEZ', 'nome': 'Nicolas Federico Lopez Alonso', 'T/R': 'R', 'P/A': 'P', 'id_cbf': 554821}, 11: {'apelido': 'WELLINGTON SILVA', 'nome': 'Wellington Alves da Silva', 'T/R': 'R', 'P/A': 'P', 'id_cbf': 306146}, 16: {'apelido': 'RITHELY', 'nome': 'Francisco Rithely da Silva Sousa', 'T/R': 'R', 'P/A': 'P', 'id_cbf': 184833}, 17: {'apelido': 'NEILTON', 'nome': 'Neilton Meira Mestzk', 'T/R': 'R', 'P/A': 'P', 'id_cbf': 316754}, 21: {'apelido': 'BRUNO SILVA', 'nome': 'Bruno Cesar Pereira Silva', 'T/R': 'R', 'P/A': 'P', 'id_cbf': 169938}, 23: {'apelido': 'RAFAEL SOBIS', 'nome': 'Rafael Augusto Sobis', 'T/R': 'R', 'P/A': 'P', 'id_cbf': 150549}, 29: {'apelido': 'SARRAFIORE', 'nome': 'Martin Nicolas Sarrafiore', 'T/R': 'R', 'P/A': 'P', 'id_cbf': 632758}, 34: {'apelido': 'ERIK', 'nome': 'Erik Jorgens de Menezes', 'T/R': 'R', 'P/A': 'P', 'id_cbf': 535946}, 45: {'apelido': 'BRUNO FUCHS', 'nome': 'Bruno de Lara Fuchs', 'T/R': 'R', 'P/A': 'P', 'id_cbf': 401025}, 77: {'apelido': 'G. PAREDE', 'nome': 'Guilherme Parede Pinheiro', 'T/R': 'R', 'P/A': 'P', 'id_cbf': 411198}}, 'Fluminense / RJ': {27: {'apelido': 'MURIEL', 'nome': 'Muriel Gustavo Becker', 'T/R': 'R(g)', 'P/A': 'P', 'id_cbf': 165925}, 2: {'apelido': 'GILBERTO', 'nome': 'Gilberto Moraes Junior', 'T/R': 'T', 'P/A': 'P', 'id_cbf': 307134}, 6: {'apelido': 'YURI', 'nome': 'Yuri Oliveira Lima', 'T/R': 'T', 'P/A': 'P', 'id_cbf': 307979}, 11: {'apelido': 'YONY GONZALEZ', 'nome': 'Yony Alexander Gonzalez Copete', 'T/R': 'T', 'P/A': 'P', 'id_cbf': 646477}, 19: {'apelido': 'CAIO HENRIQUE', 'nome': 'Caio Henrique Oliveira Silva', 'T/R': 'T', 'P/A': 'P', 'id_cbf': 337823}, 20: {'apelido': 'DANIEL', 'nome': 'Daniel Sampaio Simoes', 'T/R': 'T', 'P/A': 'P', 'id_cbf': 308495}, 26: {'apelido': 'DIGÃO', 'nome': 'Rodrigo Junior Paula Silva', 'T/R': 'T', 'P/A': 'P', 'id_cbf': 172038}, 29: {'apelido': 'ALLAN', 'nome': 'Allan Rodrigues de Souza', 'T/R': 'T', 'P/A': 'P', 'id_cbf': 339266}, 32: {'apelido': 'MARCOS PAULO', 'nome': 'Marcos Paulo Costa do Nascimento', 'T/R': 'T', 'P/A': 'P', 'id_cbf': 526048}, 33: {'apelido': 'NINO', 'nome': 'Marcilio Florencio Mota Filho', 'T/R': 'T', 'P/A': 'P', 'id_cbf': 379386}, 77: {'apelido': 'NENE', 'nome': 'Anderson Luis de Carvalho', 'T/R': 'T', 'P/A': 'P', 'id_cbf': 150986}, 25: {'apelido': 'AGENOR', 'nome': 'Agenor Detofol', 'T/R': 'R(g)', 'P/A': 'P', 'id_cbf': 182631}, 4: {'apelido': 'LUCCAS CLARO', 'nome': 'Luccas Claro dos Santos', 'T/R': 'R', 'P/A': 'P', 'id_cbf': 291708}, 5: {'apelido': 'AIRTON', 'nome': 'Airton Ribeiro Santos', 'T/R': 'R', 'P/A': 'P', 'id_cbf': 186870}, 7: {'apelido': 'PABLO DYEGO', 'nome': 'Pablo Dyego da Silva Rosa', 'T/R': 'R', 'P/A': 'P', 'id_cbf': 315834}, 10: {'apelido': 'PH GANSO', 'nome': 'Paulo Henrique Chagas de Lima', 'T/R': 'R', 'P/A': 'P', 'id_cbf': 184364}, 12: {'apelido': 'LUCÃO DO BREAK', 'nome': 'Lucas Vinicius Goncalves Silva', 'T/R': 'R', 'P/A': 'P', 'id_cbf': 304035}, 15: {'apelido': 'DODI', 'nome': 'Douglas Moreira Fagundes', 'T/R': 'R', 'P/A': 'P', 'id_cbf': 354201}, 17: {'apelido': 'EVANILSON', 'nome': 'Francisco Evanilson de Lima Barbosa', 'T/R': 'R', 'P/A': 'P', 'id_cbf': 416790}, 18: {'apelido': 'WELLINGTON NEM', 'nome': 'Wellington Silva Sanches Aguiar', 'T/R': 'R', 'P/A': 'P', 'id_cbf': 293170}, 21: {'apelido': 'IGOR JULIÃO', 'nome': 'Igor de Carvalho Juliao', 'T/R': 'R', 'P/A': 'P', 'id_cbf': 307616}, 22: {'apelido': 'ORINHO', 'nome': 'Edilsom Borba de Aquino', 'T/R': 'R', 'P/A': 'P', 'id_cbf': 398393}, 28: {'apelido': 'GUILHERME', 'nome': 'Guilherme Milhomem Gusmao', 'T/R': 'R', 'P/A': 'P', 'id_cbf': 171975}}}

![1](https://github.com/gconelhero/brasileiro/assets/26088216/348fe3c9-f535-4387-8283-ce061b93a4c8)

{'Internacional / RS': {'Técnico': 'Jose Ricardo Mannarino', 'Auxiliar Técnico': 'Cleber Dos Santos Almeida Junior', 'Médico': 'Rodrigo Hoffmeister Silva', 'Treinador De Goleiros': 'Daniel Da Fonseca Pavan', 'Preparador Físico': 'Cristiano Garcia Nunes', 'Massagista': 'Paulo Juarez Quintanilha Da Silva'}, 'Fluminense / RJ': {'Técnico': 'Marco Aurelio De Oliveira', 'Auxiliar Técnico': 'Ailton Dos Santos Ferraz', 'Médico': 'Jorge Lopes De Souza Costa', 'Treinador De Goleiros': 'Andre Carvalho Da Silva', 'Preparador Físico': 'Marcos De Seixas Correa', 'Massagista': 'Alex Soares Dos Santos'}}

{1: {'minuto': datetime.time(0, 35), '1T/2T': '1T', 'numero': 99, 'nome': 'William de Oliveira Pottker', 'equipe': 'Internacional / RS'}, 2: {'minuto': datetime.time(0, 40), '1T/2T': '1T', 'numero': 99, 'nome': 'William de Oliveira Pottker', 'equipe': 'Internacional / RS'}, 3: {'minuto': datetime.time(0, 27), '1T/2T': '2T', 'numero': 18, 'nome': 'Wellington Silva Sanches Aguiar', 'equipe': 'Fluminense / RJ'}}


{'Internacional / RS': {31: {'minuto': datetime.time(0, 21), '1T/2T': '2T', 'nome': 'Heitor Rodrigues da Fonseca', 'motivo': 'A1.2.'}, 99: {'minuto': datetime.time(0, 44), '1T/2T': '2T', 'nome': 'William de Oliveira Pottker', 'motivo': 'A1.2.'}, 9: {'minuto': datetime.time(0, 30), '1T/2T': '2T', 'nome': 'Jose Paolo Guerrero Gonzales', 'motivo': 'A2. '}}, 'Fluminense / RJ': {2: {'minuto': datetime.time(0, 40), '1T/2T': '2T', 'nome': 'Gilberto Moraes Junior', 'motivo': 'A2. '}, 10: {'minuto': datetime.time(0, 45), '1T/2T': '2T', 'nome': 'Paulo Henrique Chagas de Lima', 'motivo': 'A2. '}, 'Preparador Físico': {'minuto': datetime.time(0, 45), '1T/2T': '2T', 'nome': 'Marcos De Seixas Correa', 'motivo': 'A2. '}}}
