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


# Input a list of race_ids and return a list of relveant races.
# Example - getLeagueRaces(['21289', '21388', '21389', '21378', '21382'])
def getLeagueRaces(race_ids):
    url = api_url + '/races/'
    parameters = {
                  "key": API_KEY
    }
    league_races = []
    for n in race_ids:
        response = requests.get(url + n, params=parameters)
        race = response.json()['race']
        if race['race_name'] in ('Qualifying', 'Heat 1', 'Heat 2', 'Main'):
            id = race['id']
            league_races.append(id)
    return(league_races)


# Input race_id number and returns some info about it in a dictionary
# Example - getRaceInfo('21385')
def getRaceInfo(race_id):
    url = api_url + '/races/'
    parameters = {
                  "key": API_KEY
    }
    response = requests.get(url + race_id, params=parameters)
    race = response.json()['race']
    id = race['id']
    date = race['starts_at'][0:10]
    name = race['race_name']
    race_info = [id, date, name]
    return(race_info)


# Input a race_id and return a list of all racer_ids from that race.
# Example - getRacers('21385')
def getRacers(race_id):
    url = api_url + '/races/'
    parameters = {
                  "key": API_KEY
    }
    racer_ids = []
    response = requests.get(url + race_id, params=parameters)
    race = response.json()['race']
    for index, n in enumerate(race['racers']):
        id = race['racers'][index]['id']
        racer_ids.append(id)
    return racer_ids


# Input a race_id and racer_id and return the results for that racer's race.
# Example - getRaceResults('21385', '1029414')
def getRaceResults(race_id, racer_id):
    url = api_url + '/races/'
    parameters = {
                  "key": API_KEY
    }
    race_results = []
    response = requests.get(url + race_id, params=parameters)
    race = response.json()['scoreboard']
    for index, n in enumerate(race):
        if race[index]['racer_id'] == racer_id:
            id = race[index]['racer_id']
            first_name = race[index]['first_name']
            last_name = race[index]['last_name']
            position = race[index]['position']
            gap = race[index]['gap']
            fastest_lap_time = race[index]['fastest_lap_time']
            kart_num = race[index]['kart_num']
            race_results = [id,
                            first_name,
                            last_name,
                            position,
                            gap,
                            fastest_lap_time,
                            kart_num]
        else:
            pass
    if race_results == {}:
        print('No Results Found')
    else:
        return race_results
