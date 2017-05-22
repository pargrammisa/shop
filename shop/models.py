from django.db import models

# Create your models here.
class Item(models.Model):
	item_name=models.CharField(max_length=20)
	price=models.IntegerField()
	def __str__ (self):
		return (self.item_name)
class Option(models.Model):
	item=models.ForeignKey(Item)
	color=models.CharField(max_length=20)
	number=models.IntegerField(default=0)
	def __str__(self):
		return (self.color)
