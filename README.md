# brasileiro
Projeto relacionado ao estudo de análise de dados com Python e Pandas

Objstivos:
* Extrair, transformar e carregar os dados contidos nas súmulas do campeonato brasileiro para análise posterior.
* Criar uma API para compartilhar esses dados com outras aplicações.



Radando o projeto:<br>
`git clone https://github.com/gconelhero/brasileiro`<br>
`cd brasileiro`<br>
`python3 -m pip install -r requirements.txt`<br>
`python3 scraper.py`<br>

Instalando e configurando o MongoDB:<br>
`https://docs.mongodb.com/manual/installation/`<br>
`https://docs.mongodb.com/manual/reference/configuration-options/`<br>

DataBase:<br>
`brasileiro`<br>
Collection:<br>
`jogos`<br>

Altere os parâmetros de conexão em `mongo_load.py`:<br>
`host='<IP DO SEU MongoDB>'`<br>

Inserindo os arquivos JSON na collection:<br>
`python3 mongo_load.py`<br>