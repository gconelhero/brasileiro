# brasileiro
Project related to the study of data analysis with Python, Pandas, Mongo and Metabase

Objectives:
* Extract, transform and load the data contained in the Brazilian championship scores for further analysis.
* Create an API to share this data with other applications.


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
