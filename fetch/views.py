import os, requests, json
from django.shortcuts import render
from datetime import date, timedelta
from dotenv import load_dotenv

from .models import Race, Result

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
	for n in race_ids:
		response=requests.get("https://ssnewcaney.clubspeedtiming.com/api/index.php/races/" + n + ".json", params=parameters)
		race = response.json()['race']
		if race['race_name'] in ('Qualifying', 'Heat 1', 'Heat 2', 'Main'):
			races = Race(race_id = n,
				date = race['starts_at'],
				race_name = race['race_name']
				)
			races.save()

def getRaceResults(race_id):
	parameters = {
	"key" : API_KEY,
	}
	response = requests.get("https://ssnewcaney.clubspeedtiming.com/api/index.php/races/" + race_id + ".json", params=parameters)
	scoreboard = response.json()['scoreboard']
	for n in scoreboard:
		result = Result(
			race = race_id, 
			position = scoreboard['position'],
			first_name = scoreboard['first_name'],
			last_name = scoreboard['last_name'],
			racer_id = ['racer_id'],
			kart_num = scoreboard['kart_num'],
			gap = scoreboard['gap'],
			fastest_lap_time = scoreboard['fastest_lap_time']
			)
		result.save()