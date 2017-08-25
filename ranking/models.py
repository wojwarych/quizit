from django.db import models



class RankingTennis(models.Model):


	username = models.CharField(max_length=50, unique=True)
	easyquest = models.PositiveSmallIntegerField(blank=True, null=True)
	mediumquest = models.PositiveSmallIntegerField(blank=True, null=True)
	hardquest = models.PositiveSmallIntegerField(blank=True, null=True)



class RankingLiterature(models.Model):


	username = models.CharField(max_length=50, unique=True)
	easyquest = models.PositiveSmallIntegerField(blank=True, null=True)
	mediumquest = models.PositiveSmallIntegerField(blank=True, null=True)
	hardquest = models.PositiveSmallIntegerField(blank=True, null=True)



class RankingMusic(models.Model):


	username = models.CharField(max_length=50, unique=True)
	easyquest = models.PositiveSmallIntegerField(blank=True, null=True)
	mediumquest = models.PositiveSmallIntegerField(blank=True, null=True)
	hardquest = models.PositiveSmallIntegerField(blank=True, null=True)