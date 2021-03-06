from django.db import models

# Create your models here.
class Profile(models.Model):
	first_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=15)
	budget = models.PositiveIntegerField()

	def __str__(self):
		return self.first_name + ' ' + self.last_name

class Expense(models.Model):
	title = models.CharField(max_length=50)
	image_url = models.URLField()
	description = models.TextField(max_length=255)
	price = models.FloatField()

	def __str__(self):
		return self.title