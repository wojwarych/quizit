from django.db import models

# Create your models here.
class Tennis(models.Model):

	EASY = 1
	MEDIUM = 2
	HARD = 3
	diff_choice = (
		(EASY, 'easy'),
		(MEDIUM, 'medium'),
		(HARD, 'hard'),)


	question = models.CharField(max_length=200, default='some answ')
	first_answ = models.CharField(max_length=50, default='some answ')
	second_answ = models.CharField(max_length=50, default='some answ')
	third_answ = models.CharField(max_length=50, default='some answ')
	fourth_answ = models.CharField(max_length=50, default='some answ')
	good_answ = models.IntegerField(default=0)
	difficulty = models.IntegerField(default=0, choices=diff_choice)


	def __str__(self):


		return "This is a question?"