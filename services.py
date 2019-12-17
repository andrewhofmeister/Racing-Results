# working on moving these functions to more django friendly formats in other files
# will be deleting functions here as I move them to other files.
import os
import requests
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env file
API_KEY = os.getenv('CLUBSPEED_API_KEY')


def findRaces(race_date):
    # Search a date for all races and returns a list of race ids from that day
    url = 'https://ssnewcaney.clubspeedtiming.com/api/index.php/races/races.json'
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
    return race_ids


def findLeagueRaces(race_ids):
    # Takes a list of race ids and finds the relevant league races and returns a list of all relevant races
    url = "https://ssnewcaney.clubspeedtiming.com/api/index.php/races/"
    parameters = {
        "key": API_KEY
    }
    league_races = []
    for n in race_ids:
        response = requests.get(url + n, params=parameters)
        race = response.json()['race']
        if race['race_name'] in ('Qualifying', 'Heat 1', 'Heat 2', 'Main'):
            return league_races
        race_id = int(n)
        league_races.append(race_id)  # fix this TypeError: string indices must be integers


def getRaceResults(race_id):
    parameters = {
        "key": API_KEY,
    }
    response = requests.get("https://ssnewcaney.clubspeedtiming.com/api/index.php/races/" + race_id + ".json", params=parameters)['scoreboard']
    scoreboard = response.json()
    for n in scoreboard:
        result = Result(
            race=race_id,
            position=scoreboard[0]['position'],
            first_name=scoreboard[0]['first_name'],
            last_name=scoreboard[0]['last_name'],
            racer_id=scoreboard[0]['racer_id'],
            kart_num=scoreboard[0]['kart_num'],
            gap=scoreboard[0]['gap'],
            fastest_lap_time=scoreboard[0]['fastest_lap_time']
        )
        result.save()


def getRaceResults2(race_id):
    # Returns list of race results in finishing order by driver_id
    payload = {
        "key": API_KEY
    }
    response = requests.get("https://ssnewcaney.clubspeedtiming.com/api/index.php/races/" + race_id + ".json", params=payload)
    for n in response.json()['scoreboard']:
        return n['racer_id']
