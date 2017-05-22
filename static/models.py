from django.db import models
# Create your models here.
class Data (models.Model):
	x = models.FloatField()
	#y = models.FloatField()
	def __str__(self):
		return (str(self.x))