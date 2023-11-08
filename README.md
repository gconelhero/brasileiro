# brasileiro
Project related to the study of data analysis with Python and Mongo.

Objectives:
* Extract, transform and load the data contained in the Brazilian championship summary for further analysis.
* Create an API to share this data with other applications.

![2](https://github.com/gconelhero/brasileiro/assets/26088216/3ecf6a2f-5b07-4373-b933-8948e760b7f0)

Install and config MongoDB:<br>
`https://docs.mongodb.com/manual/installation/`<br>
`https://docs.mongodb.com/manual/reference/configuration-options/`

MongoDB-6.0.11 for Ubuntu-22.04.03-LTS:
```
sudo apt-get install gnupg curl
```
```
curl -fsSL https://pgp.mongodb.com/server-6.0.asc |
sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```
```
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```
```
sudo apt-get update
```
```
sudo apt-get install -y mongodb-org
```
```
sudo systemctl daemon-reload &&
sudo systemctl enable mongod.service &&
sudo systemctl start mongod.service
```
Run MongoDB (terminal):
```
mongosh
```
Create "brasileiro" database:
```
use brasileiro
```
To use a graphical interface (MongoDB Compass):
```
https://www.mongodb.com/try/download/compass
```
Run brasileiro:
```
git clone https://github.com/gconelhero/brasileiro
```
```
cd brasileiro
```
```
python3 -m pip install -r requirements.txt```
```
```
python3 et_main.py
```

## Some PDFs have ill-defined structures and irregular patterns. PDF documents that are poorly structured and fail data standards will go to the "pdf_fail" folder.

# CONFIG:
In et_main.py it is possible to change the value of the variables "jogo" (game) and "ano" (year), the structure and data type of PDF may vary depending on the season (year), in game 140 of the 2023 season the loop stops.
In mongo_load.py host=<IP_MongoDB>

# RESULTS
![cabecalho_pdf](https://github.com/gconelhero/brasileiro/assets/26088216/5ea5d325-3b7c-4341-8362-7ed69d79f102)
```
{
  "_id": {
    "$oid": "65492bb4d89269d692f73eba"
  },
  "campeonato": "Campeonato Brasileiro - Série A/2018 ",
  "jogo_numero": 1,
  "rodada": 1,
  "mandante": "Cruzeiro / MG",
  "visitante": "Grêmio / RS",
  "data": "2018-04-14",
  "hora": "16:00:00-03:00",
  "estadio": "Magalhães Pinto / Belo Horizonte"
}
```
![arbitragem_pdf](https://github.com/gconelhero/brasileiro/assets/26088216/af029e3f-c842-45c5-9376-de293c05d013)
```
{
  "_id": {
    "$oid": "65492bb4d89269d692f73ebc"
  },
  "Arbitro": " Rodolpho Toski Marques (FIFA / PR)",
  "jogo_numero": 1,
  "data": "2018-04-14",
  "Arbitro Assistente 1": " Bruno Boschilia (FIFA / PR)",
  "Arbitro Assistente 2": " Victor Hugo Imazu dos Santos (AB / PR)",
  "Quarto Arbitro": " Rafael Trombeta (AB / PR)",
  "Arbitro Assist Adic 1": " Lucas Paulo Torezin (CD / PR)",
  "Arbitro Assist Adic 2": " Fabio Filipus (CD / PR)",
  "Inspetor": " Alicio Pena Junior (CBF / MG)"
}
```

![cronologia_pdf](https://github.com/gconelhero/brasileiro/assets/26088216/fc165508-cffb-4a6a-9667-731391dd06f7)
```
{
  "_id": {
    "$oid": "65492bb5d89269d692f73ebe"
  },
  "Entrada mandante 1T": "15:50:00-03:00",
  "Atraso mandante 1T": "Não Houve",
  "Entrada visitante 1T": "15:50:00-03:00",
  "Atraso visitante 1T": "Não Houve",
  "Início 1T": "16:00:00-03:00",
  "Atraso início 1T": "Não Houve",
  "Término 1T": "16:46:00-03:00",
  "Acréscimo 1T": "00:01:00",
  "Entrada mandante 2T": "16:58:00-03:00",
  "Atraso mandante 2T": "Não Houve",
  "Entrada visitante 2T": "16:58:00-03:00",
  "Atraso visitante 2T": "Não Houve",
  "Início 2T": "16:58:00-03:00",
  "Atraso início 2T": "Não Houve",
  "Término 2T": "17:53:00-03:00",
  "Acréscimo 2T": "00:07:00",
  "Resultado 1T": [
    0,
    0
  ],
  "Resultado Final": [
    0,
    1
  ],
  "jogo_numero": 1,
  "data": "2018-04-14"
}
```

![plantel_pdf](https://github.com/gconelhero/brasileiro/assets/26088216/2a035374-ddb6-4dd1-98a0-cee1926ce6fb)
```
{
  "_id": {
    "$oid": "65492bb5d89269d692f73ec0"
  },
  "id_cbf": 129292,
  "nome": "Fabio Deivson Lopes Maciel",
  "apelido": "FABIO",
  "numero": 1,
  "equipe": "Cruzeiro / MG",
  "T/R": "T(g)",
  "data": "2018-04-14",
  "jogo_numero": 1
}
...
```

![comissao_pdf](https://github.com/gconelhero/brasileiro/assets/26088216/9dfd01ee-a2b6-43f5-8151-91e177424964)
```
{
  "_id": {
    "$oid": "654a55361f073e6c2b7eb130"
  },
  "Técnico": "LUIZ ANTONIO VENKER MENEZES",
  "Auxiliar Técnico": "SIDNEI DE ESPIRITO",
  "Médico": "FREDERICO ZATTI LIMA DE SOUZA",
  "Treinador De Goleiros": "ROBERTO BARBOSA DOS SANTOS",
  "Preparador Físico": "EDUARDO LUIS DA SILVA",
  "Fisioterapeuta": "EDUESTER LOPES RODRIGUES",
  "equipe": "Cruzeiro / MG",
  "jogo_numero": 1,
  "data": "2018-04-14"
}
...
```

![gols_pdf](https://github.com/gconelhero/brasileiro/assets/26088216/5cc06c7f-b328-41ae-8ea7-9229f3134985)
```
{
  "_id": {
    "$oid": "65492bb5d89269d692f73eed"
  },
  "minuto": "00:09:00",
  "1T/2T": "2T",
  "tipo": "NR", 
  "id_cbf": 292942,
  "equipe": "Grêmio / RS",
  "jogo_numero": 1,
  "data": "2018-04-14"
}
...
```

![amarelos_pdf](https://github.com/gconelhero/brasileiro/assets/26088216/1237fd23-8a3f-4d4c-aeaf-06d6f71807e3)
```
{
  "_id": {
    "$oid": "65492bb6d89269d692f73eef"
  },
  "minuto": "00:26:00",
  "1T/2T": "2T",
  "id_cbf": 295418,
  "motivo": "A3. ",
  "equipe": "Grêmio / RS"
  "jogo_numero": 1,
  "data": "2018-04-14"
}
...
```

![vermelhos_pdf](https://github.com/gconelhero/brasileiro/assets/26088216/717274b4-2c67-4696-b1c7-2d883d2c5709)
```
{
  "_id": {
    "$oid": "65492bb6d89269d692f73ef4"
  },
  "minuto": "00:29:00",
  "1T/2T": "2T",
  "id_cbf": 554626,
  "condicao": "Cartão Vermelho Direto",
  "motivo": "V1.7.",
  "equipe": "Grêmio / RS",
  "jogo_numero": 1,
  "data": "2018-04-14"
}
...
```

![substituicoes_pdf](https://github.com/gconelhero/brasileiro/assets/26088216/5e771543-60a7-43e0-be01-b47ab9939d8d)
```
{
  "_id": {
    "$oid": "654a5ba515f3f5cfdae4e63c"
  },
  "minuto": "00:45:00",
  "1T/2T": "INT",
  "entrou": 337172,
  "saiu": 150549,
  "equipe": "Cruzeiro / MG",
  "jogo_numero": 1,
  "data": "2018-04-14"
}
...
```
