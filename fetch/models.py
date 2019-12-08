from django.db import models

class Races(models.Model):
	race_id = models.IntegerField(primary_key=True) #Clubspeed id number
	date = models.DateTimeField() #Scheduled Race Time
	race_name = models.CharField(max_length=30) # Heat 1, 2, Main
	
	def __str__(self):
		return self.race_name + ' ' + self.date
