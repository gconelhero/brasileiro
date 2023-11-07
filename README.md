# brasileiro
Project related to the study of data analysis with Python and Mongo.

Objectives:
* Extract, transform and load the data contained in the Brazilian championship scores for further analysis.
* Create an API to share this data with other applications.

![2](https://github.com/gconelhero/brasileiro/assets/26088216/3ecf6a2f-5b07-4373-b933-8948e760b7f0)

Install and config MongoDB:<br>
`https://docs.mongodb.com/manual/installation/`<br>
`https://docs.mongodb.com/manual/reference/configuration-options/`<br>

Run:<br>
`git clone https://github.com/gconelhero/brasileiro`<br>
`cd brasileiro`<br>
`python3 -m pip install -r requirements.txt`<br>
`python3 et_main.py`<br>

## Some PDFs have ill-defined structures and irregular patterns. PDF documents that are poorly structured and fail data standards will go to the "pdf_fail" folder.

# CONFIG:
In et_main.py it is possible to change the value of the variables "jogo" (game) and "ano" (year), the structure and data type of PDF may vary depending on the season (year), in game 140 of the 2023 season the loop stops.
In mongo_load.py host=<IP_MongoDB>
