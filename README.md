# covid19italia_api
The api of covid19italia dataset

At the moment active here https://covid19italiahelp.herokuapp.com/
To use that  

## GET
(https://covid19italiahelp.herokuapp.com/reports)[https://covid19italiahelp.herokuapp.com/reports/] get ALL reports in JSON format

reports/data_field where "data_field" is one tag name of the reports list present in the issue dataset here
https://raw.githubusercontent.com/emergenzeHack/covid19italia_data/master/issuesjson.json
Example
https://host/reports/Provincia
gives all the "Provincia" values of all reports (where exist).

To start locally python3 app.py
