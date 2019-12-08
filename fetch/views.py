import os, requests, json
from django.shortcuts import render
from datetime import date, timedelta
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('CLUBSPEED_API_KEY')

def findRaces(race_date):
	end_date = race_date + timedelta(days=1)
	parameters = {
		"key" : API_KEY,
		"start" : race_date,
		"end" : end_date
	}
	race_ids = []
	response = requests.get("https://ssnewcaney.clubspeedtiming.com/api/index.php/races/races.json", params=parameters)
	races = response.json()['races']
	for n in races:
		id = n['HeatNo']
		race_ids.append(id)
	parameters = {
		"key" : API_KEY
	}
	league_races = {}
	for n in race_ids:
		response=requests.get("https://ssnewcaney.clubspeedtiming.com/api/index.php/races/" + n + ".json", params=parameters)
		race = response.json()['race']
		if race['race_name'] in ('Qualifying', 'Heat 1', 'Heat 2', 'Main'):
			races = Races(race_id = n, date = race['starts_at'], race_name = race['race_name'])
			races.save()