# covid19italia_api
Le api del progetto covid19italia.help. Con queste puoi interrogare i nostri dataset ed usare i dati che più ti possono servire!

Al momento sono attive qui https://covid19italiahelp.herokuapp.com/

## GET
- [https://covid19italiahelp.herokuapp.com/reports/](https://covid19italiahelp.herokuapp.com/reports) Prende tutti i report accettati dal progetto e ne mostra i dati in formato JSON.

- [https://covid19italiahelp.herokuapp.com/reports/](https://covid19italiahelp.herokuapp.com/reports) + "/data_field"
dove "data_field" è uno dei campi che si possono trovare in ogni report [in questo datateset](https://raw.githubusercontent.com/emergenzeHack/covid19italia_data/master/issuesjson.json) mostra i report che hanno "data_field" specificato e tutte le informazioni relative
Ad esempio: [https://covid19italiahelp.herokuapp.com/reports/Provincia](https://covid19italiahelp.herokuapp.com/reports/Provincia) restituisce tutti i report con il campo Provincia.

- [https://covid19italiahelp.herokuapp.com/reports/](https://covid19italiahelp.herokuapp.com/reports) + "/data_field/data_value" dove "data_field" è uno dei campi che si possono trovare in ogni report [in questo datateset](https://raw.githubusercontent.com/emergenzeHack/covid19italia_data/master/issuesjson.json) mostra i report che hanno "data_field"="data_value" tutte le informazioni relative.
Ad esempio: [https://covid19italiahelp.herokuapp.com/reports/Provincia/Bergamo](https://covid19italiahelp.herokuapp.com/reports/Provincia/Bergamo) restituisce tutti i report della provincia di Bergamo.


### Per avviare in locale: python3 app.py
