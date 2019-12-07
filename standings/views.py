from django.shortcuts import render
from django.http import HttpResponse
import os, requests, json
from datetime import timedelta, date
from doenv import load_dotenv

def index(request):
	return HttpResponse("<h1>League Standings</h1>")

load_dotenv()
API_KEY = os.getenv('CLUBSPEED_API_KEY')

def findRaces(race_date):
	pass