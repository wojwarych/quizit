from django.db import models



class News(models.Model):


	title = models.CharField(max_length=200)
	article = models.TextField()
	pub_date = models.DateTimeField()


	def __str__(self):


		return self.title