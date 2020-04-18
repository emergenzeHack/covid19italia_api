import urllib.request
import datetime
import json

# import Flask
from flask import Flask

# create a Flask app
# to run python3 app.py
app = Flask(__name__)

# poor man's cache, assumes concurrency using processes and not threads
CACHE_TIMEOUT = datetime.timedelta(hours=1)
CACHE = {}


def get_data_from_github(filename):
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    hit = CACHE.get(filename)
    if hit:
        t, data = hit
        if t + CACHE_TIMEOUT > now:
            return json.loads(data)

    data = urllib.request.urlopen(filename).read()
    CACHE[filename] = (now, data)
    return json.loads(data)


# establish a Flask route so that we can serve HTTP traffic on that route
# GET api is endpoint/reports/tag_of_data_array
# return JSON with data with all value of "data_field" (example "Provincia") where data_field exist
@app.route('/reports/<data_field>', methods=['GET'])
def reports_key(data_field):
    data = get_data_from_github(
        "https://raw.githubusercontent.com/emergenzeHack/covid19italia_data/master/issuesjson.json"
    )
    print("Started reading JSON data...")
    # We can then find the data for the requested and send it back as json
    filtered = [d['issue']['data'] for d in data if data_field in d['issue']['data']]
    return json.dumps(filtered)

# establish a Flask route so that we can serve HTTP traffic on that route
# GET api is endpoint/reports/data_field/data_value
# return JSON with data with all value of "data_field" (example "Provincia") where data_field exist 
# and take all reports with data_field=data_value
@app.route('/reports/<data_field>/<data_value>', methods=['GET'])
def reports_key_value(data_field,data_value):
    data = get_data_from_github(
        "https://raw.githubusercontent.com/emergenzeHack/covid19italia_data/master/issuesjson.json"
    )
    print("Started reading JSON data...")
    # We can then find the data for the requested and send it back as json
    filtered_by_field = (d['issue']['data'] for d in data if data_field in d['issue']['data'])
    filtered_by_value = [d for d in filtered_by_field if data_value in d[data_field]]
    return json.dumps(filtered_by_value)

#GET ALL reports
@app.route('/reports/', methods=['GET'])
def reports_all():
    data = get_data_from_github(
        "https://raw.githubusercontent.com/emergenzeHack/covid19italia_data/master/issuesjson.json"
    )
    print("Started reading JSON data...")
    # We can then find the data for the requested and send it back as json
    reports = [d['issue']['data'] for d in data]
    return json.dumps(reports)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to the Covid19Italia.Help API ! </h1> You can use the API to request specific data, consider that all data of the project are available <a href='https://raw.githubusercontent.com/emergenzeHack/covid19italia_data/master/issuesjson.json'>here</a>"

#error handler
@app.errorhandler(404) 
def invalid_route(e): 
    return "Invalid route."

# Get setup so that if we call the app directly (and it isn't being imported elsewhere)
# it will then run the app with the debug mode as True
# More info - https://docs.python.org/3/library/__main__.html
# data master here https://raw.githubusercontent.com/emergenzeHack/covid19italia_data/master/issuesjson.json
if __name__ == '__main__':
     # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
