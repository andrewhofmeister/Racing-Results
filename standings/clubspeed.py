#working on moving these functions to more django friendly formats in other files
# will be deleting functions here as I move them to other files.
import os, requests, json
from datetime import timedelta, date
from dotenv import load_dotenv

#Load API key from .env file
load_dotenv()
API_KEY = os.getenv('CLUBSPEED_API_KEY')


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

