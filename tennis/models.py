from django.db import models
from django.db.models.aggregates import Count

import random

# Create your models here.
class UsersManager(models.Manager):
	

	def get_questions(self, num_of_q=10):
		

		questions_data = (
			self.all().values_list('id', flat=True))
		questions_data = random.sample(list(questions_data), k=num_of_q)

		return questions_data



class EasyQuest(models.Model):


	objects = UsersManager()

	question = models.CharField(max_length=200, default='some answ')
	first_answ = models.CharField(max_length=50, default='some answ')
	second_answ = models.CharField(max_length=50, default='some answ')
	third_answ = models.CharField(max_length=50, default='some answ')
	fourth_answ = models.CharField(max_length=50, default='some answ')
	good_answ = models.IntegerField(default=0)


	def __str__(self):


		return self.question



class MediumQuest(models.Model):


	objects = UsersManager()

	question = models.CharField(max_length=200, default='some answ')
	first_answ = models.CharField(max_length=50, default='some answ')
	second_answ = models.CharField(max_length=50, default='some answ')
	third_answ = models.CharField(max_length=50, default='some answ')
	fourth_answ = models.CharField(max_length=50, default='some answ')
	good_answ = models.IntegerField(default=0)
	

	def __str__(self):


		return self.question



class HardQuest(models.Model):


	objects = UsersManager()

	question = models.CharField(max_length=200, default='some answ')
	first_answ = models.CharField(max_length=50, default='some answ')
	second_answ = models.CharField(max_length=50, default='some answ')
	third_answ = models.CharField(max_length=50, default='some answ')
	fourth_answ = models.CharField(max_length=50, default='some answ')
	good_answ = models.IntegerField(default=0)
	

	def __str__(self):


		return self.question