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

	question = models.CharField(max_length=200, default='some answ', blank=True)
	first_answ = models.CharField(max_length=50, default='some answ', blank=True)
	second_answ = models.CharField(max_length=50, default='some answ', blank=True)
	third_answ = models.CharField(max_length=50, default='some answ', blank=True)
	fourth_answ = models.CharField(max_length=50, default='some answ', blank=True)
	good_answ = models.IntegerField(default=0, blank=True)


	def __str__(self):


		return self.question



class MediumQuest(models.Model):


	objects = UsersManager()

	question = models.CharField(max_length=200, default='some answ', blank=True)
	first_answ = models.CharField(max_length=50, default='some answ', blank=True)
	second_answ = models.CharField(max_length=50, default='some answ', blank=True)
	third_answ = models.CharField(max_length=50, default='some answ', blank=True)
	fourth_answ = models.CharField(max_length=50, default='some answ', blank=True)
	good_answ = models.IntegerField(default=0)
	

	def __str__(self):


		return self.question



class HardQuest(models.Model):


	objects = UsersManager()

	question = models.CharField(max_length=200, default='some answ', blank=True)
	first_answ = models.CharField(max_length=50, default='some answ', blank=True)
	second_answ = models.CharField(max_length=50, default='some answ', blank=True)
	third_answ = models.CharField(max_length=50, default='some answ', blank=True)
	fourth_answ = models.CharField(max_length=50, default='some answ', blank=True)
	good_answ = models.IntegerField(default=0)
	

	def __str__(self):


		return self.question