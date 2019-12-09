from django.db import models

class Driver(models.Model):
	driver_id = models.IntegerField(primary_key=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	weight_class = models.CharField(max_length=30)
	is_rookie = models.BooleanField(default=False)

	def __str__(self):
		return self.first_name + ' ' + self.last_name + ' ' + str(self.driver_id)

class Standings(models.Model):
	driver_id = models.IntegerField()
	driver_name =  models.CharField(max_length=60)
	position = models.IntegerField()
	total_points = models.IntegerField()
	wins = models.IntegerField()
	podiums = models.IntegerField()
	poles = models.IntegerField()
	fastest_laps = models.IntegerField()

class Results(models.Model):
	driver_id = models.IntegerField()
	round_id = models.IntegerField()
	race_id = models.IntegerField()
	position = models.IntegerField()
	fastest_lap = models.BooleanField(default=False)
	points = models.IntegerField()

class Round(models.Model):
	date = models.DateTimeField()


class Race(models.Model):
	race_id = models.IntegerField(primary_key=True) #Clubspeed id number
	date = models.DateTimeField() #Scheduled Race Time
	race_name = models.CharField(max_length=30) # Heat 1, 2, Main
	
	def __str__(self):
		return self.race_id + '-' + self.date

class Result(models.Model):
	race_id = models.IntegerField(primary_key=True)
	position = models.IntegerField()
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	racer_id = models.IntegerField()
	kart_num = models.IntegerField()
	gap = models.FloatField()
	fastest_lap_time = models.FloatField()