# This file is for funtions that get data from the Clubspeed API.
import os
import requests
from datetime import date, timedelta
from dotenv import load_dotenv

# Load API key from .env file.
load_dotenv()
API_KEY = os.getenv('CLUBSPEED_API_KEY')

api_url = 'https://ssnewcaney.clubspeedtiming.com/api/index.php'


# Input date and return a list of races from that day.
# Example - getRaces(2019, 11, 21)
def getRaces(year, month, day):
    url = api_url + '/races/races'
    race_date = date(year, month, day)
    end_date = race_date + timedelta(days=1)
    parameters = {
            "key": API_KEY,
            "start": race_date,
            "end": end_date
    }
    race_ids = []
    response = requests.get(url, params=parameters)
    races = response.json()['races']
    for n in races:
        id = n['HeatNo']
        race_ids.append(id)
    print('Races from ' + str(race_date) + ':' + str(race_ids))
    return race_ids


# Input a list of race_ids and return a dictionary of relevant races.
# In the form of {race_id : race_name}
# Example - getLeagueRaces(['21289', '21388', '21389', '21378', '21382'])
def getLeagueRaces(race_ids):
    url = api_url + '/races/'
    parameters = {
                  "key": API_KEY
    }
    league_races = {}
    for n in race_ids:
        response = requests.get(url + n, params=parameters)
        race = response.json()['race']
        if race['race_name'] in ('Qualifying', 'Heat 1', 'Heat 2', 'Main'):
            id = race['id']
            print(id + ' : ' + race['race_name'])
            league_races.update({id: race['race_name']})
    return(league_races)


# Test function - should return 8 total races. 2 of each race type.
# getLeagueRaces(getRaces(2019, 11, 21))


# Input a race_id and return a list of all racer_ids from that race.
def getRacers(race_id):
    pass


# Input a race_id and racer_id and return the results for that racer's race.
def getRaceResults(race_id, racer_id):
    pass
