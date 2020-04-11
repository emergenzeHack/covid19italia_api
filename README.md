# covid19italia_api
Le api del progetto covid19italia.help. Con queste puoi interrogare i nostri dataset ed usare i dati che più ti possono servire!

Al momento sono attive qui https://covid19italiahelp.herokuapp.com/

## GET
- [https://covid19italiahelp.herokuapp.com/reports/](https://covid19italiahelp.herokuapp.com/reports) Prende tutti i report accettati dal progetto e ne mostra i dati in formato JSON.

- [https://covid19italiahelp.herokuapp.com/reports/](https://covid19italiahelp.herokuapp.com/reports) + "/data_field"
dove "data_field" è uno dei campi che si possono trovare in ogni report [in questo datateset](https://raw.githubusercontent.com/emergenzeHack/covid19italia_data/master/issuesjson.json) e mostra i report che hanno "data_field" specificato e la descrizione del relativo report.
Ad esempio: [https://covid19italiahelp.herokuapp.com/reports/Provincia](https://covid19italiahelp.herokuapp.com/reports/Provincia) restituisce tutti i valori del campo Provincia (dove esiste) con la descrizione della relativa segnalazione

### Per avviare in locale: python3 app.py
