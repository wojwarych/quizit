from django.db import models

# Create your models here.
class Tennis(models.Model):


	question = models.CharField(max_length=200, default='some answ')
	first_answ = models.CharField(max_length=50, default='some answ')
	second_answ = models.CharField(max_length=50, default='some answ')
	third_answ = models.CharField(max_length=50, default='some answ')
	fourth_answ = models.CharField(max_length=50, default='some answ')
	good_answ = models.IntegerField(default=0)
	difficulty = models.IntegerField(default=0)


	def __str__(self):


		return "This is a question?"