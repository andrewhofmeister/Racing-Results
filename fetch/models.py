from django.db import models

class Race(models.Model):
	race_id = models.IntegerField(primary_key=True) #Clubspeed id number
	date = models.DateTimeField() #Scheduled Race Time
	race_name = models.CharField(max_length=30) # Heat 1, 2, Main
	
	def __str__(self):
		return self.race_name + ' ' + self.date

class Result(models.Model):
	race = models.ForeignKey(Race, on_delete=models.CASCADE)
	position = models.IntegerField()
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	racer_id = models.IntegerField()
	kart_num = models.IntegerField()
	gap = models.FloatField()
	fastest_lap_time = models.FloatField()