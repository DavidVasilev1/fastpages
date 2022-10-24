from contextlib import nullcontext
from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import time

# Blueprints enable python code to be organized in multiple files and directories https://flask.palletsprojects.com/en/2.2.x/blueprints/
flight_api = Blueprint('flight_api', __name__,
                   url_prefix='/api/flight')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(flight_api)

"""Time Keeper
Returns:
    Boolean: is it time to update?
"""
def updateTime():
    global last_run  # the last_run global is preserved between calls to function
    try: last_run
    except: last_run = None
    
    # initialize last_run data
    if last_run is None:
        last_run = time.time()
        return True
    
    # calculate time since last update
    elapsed = time.time() - last_run
    if elapsed > 86400:  # update every 24 hours
        last_run = time.time()
        return True
    
    return False

"""API Handler
Returns:
    String: API response
"""

def getAPI():
    global flight_data  # the flight_data global is preserved between calls to function
    try: flight_data
    except: flight_data = None

    """
    Preserve Service usage / speed time with a Reasonable refresh delay
    """
    if updateTime(): # request flight data
        # @app.route('/', methods=['GET', 'POST'])
        # def predict():
        #     if request.method == 'POST':
        #         # get the form data
        #         text = request.form['flight']
        #         text = request.form['date']
        #         # do your prediction here
        #         render_template('2022-10-23-plane-api.md', text=text)
        #     return render_template('2022-10-23-plane-api.md')
        # flight = input("Number: ")
        # date = input("Number: ")
        # url = "https://aerodatabox.p.rapidapi.com/flights/number/"+str(flight)+"/"+str(date)
        url = "https://aerodatabox.p.rapidapi.com/flights/number/DL47/2022-10-20"
        querystring = {"withAircraftImage":"false","withLocation":"false"}
        headers = {
            "X-RapidAPI-Key": "6b9dacaef5mshade649601d1255fp14c8c2jsn9aeceb731b2b",
            "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        flight_data = response
    else:  # Request flight Data
        response = flight_data
    return response


"""API with Country Filter
Returns:
    String: Filter of API response
"""   
def getCountry(filter):
    # Request Covid Data
    response = getflightAPI()
    # Look for Country    
    countries = response.json().get('departure')
    for country in countries:  # countries is a list
        if country["country_name"].lower() == filter.lower():  # this filters for country
            return country
    
    return {"message": filter + " not found"}


"""Defines API Resources 
  URLs are defined with api.add_resource
"""   
class flightAPI:
    """API Method to GET all flight Data"""
    class _Read(Resource):
        def get(self):
            return getflightAPI().json()
        
    """API Method to GET flight Data for a Specific Country"""
    class _ReadCountry(Resource):
        def get(self, filter):
            return jsonify(getCountry(filter))
    
    # resource is called an endpoint: base usr + prefix + endpoint
    api.add_resource(_Read, '/')
    api.add_resource(_ReadCountry, '/<string:filter>')


"""Main or Tester Condition 
  This code only runs when this file is "played" directly
"""        
if __name__ == "__main__": 
    """
    Using this test code is how I built the backend logic around this API.  
    There were at least 10 debugging session, on handling updateTime.
    """
    
    print("-"*30) # cosmetic separator

    # This code looks for "world data"
    response = getflightAPI()
    print("World Totals")
    world = response.json().get('world_total')  # turn response to json() so we can extract "world_total"
    for key, value in world.items():  # this finds key, value pairs in country
        print(key, value)

    print("-"*30)

    # This code looks for USA in "countries_stats"
    country = getCountry("USA")
    print("USA Totals")
    for key, value in country.items():
        print(key, value)
        
    print("-"*30)