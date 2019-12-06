# This script will get all relevant race data for each race session
# and store it in the app's database.

import os, requests, json
from datetime import timedelta, date
from dotenv import load_dotenv

#Load API key from .env file
load_dotenv()
API_KEY = os.getenv('CLUBSPEED_API_KEY')

race_ids = []
race_names = {} # {race_id:race_name}

# Finds all races on specified date
def findRaces(race_date): ##YYYY-MM-DD ## 2019-11-21
	end_date = race_date + timedelta(days=1)
	payload = {
		"start": race_date,
		"end": end_date,
		"key": API_KEY
	}
	response = requests.get("https://ssnewcaney.clubspeedtiming.com/api/index.php/races/races.json", params=payload)
	races = response.json()['races']
	for n in races:
		id = n["HeatNo"]
		race_ids.append(id)

# Find races relevant races using their names given to them in the clubspeed system.
def findRaceNames():
	payload = {
		"key": API_KEY
	}
	for n in race_ids:
		response = requests.get("https://ssnewcaney.clubspeedtiming.com/api/index.php/races/" + n + ".json", params=payload)
		race_name = response.json()['race']['race_name']
		if race_name in ('Qualifying', 'Heat 1', 'Heat 2', 'Main'):
			race_names[n] = race_name

#Returns list of race results in finishing order by driver_id
def getRaceResults(race_id):
	payload = {
		"key": API_KEY
	}
	response = requests.get("https://ssnewcaney.clubspeedtiming.com/api/index.php/races/" + race_id + ".json", params=payload)
	for n in response.json()['scoreboard']:
		return n['racer_id']

#get driver info from each race

### NOT FINISHED YET ###
def getDrivers(race_names):
	payload = {
		"key": API_KEY
	}
	for n in race_names:
		response = requests.get("https://ssnewcaney.clubspeedtiming.com/api/index.php/races/" + n + ".json", params=payload)
		for n in response.json()['race']['racers']:
			driver_id = n['id']
			first_name = n['first_name']
			last_name = n['last_name']


###To-Do###
#	Detirmine weight class racing in each race ????HOW???

#	get all drivers(name and id)
#	get fastest lap from main races