# This script will get all relevant race data for each race session
# and store it in the app's database.

import os, requests, json
from datetime import timedelta, date
from dotenv import load_dotenv
from .models import Driver

#Load API key from .env file
load_dotenv()
API_KEY = os.getenv('CLUBSPEED_API_KEY')



# Search clubspeed for races on specified date
# and store all race ids in an array
race_date = date(2019, 11, 21) #Date value will be taken from user input once implemented
end_date = race_date + timedelta(days=1)
payload = {
	"start": race_date,
	"end": end_date,
	"key": API_KEY
}
response = requests.get("https://ssnewcaney.clubspeedtiming.com/api/index.php/races/races.json", params=payload)
races = response.json()['races']
race_ids = []

for n in races:
	id = n["HeatNo"]
	race_ids.append(id)


# Find races relevant races using their names given to them in the clubspeed system.
# Then store in values in a dictionary {ID:race_name}
payload = {
	"key": API_KEY
}
race_names = {}

for n in race_ids:
	response = requests.get("https://ssnewcaney.clubspeedtiming.com/api/index.php/races/" + n + ".json", params=payload)
	race_name = response.json()['race']['race_name']
	if race_name in ('Qualifying', 'Heat 1', 'Heat 2', 'Main'):
		race_names[n] = race_name

#Get driver, position, and fastest lap data
for n in race_names:
	response = requests.get("https://ssnewcaney.clubspeedtiming.com/api/index.php/races/" + n + ".json", params=payload)
	driver_id



###To-Do###
#	Detirmine weight class racing in each race ????HOW???
#	get all drivers(name and id) and finishing position
#	get fastest lap from main races