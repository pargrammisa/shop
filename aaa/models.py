from django.db import models
# Create your models here.
class Cat(models.Model):
	name=models.CharField(max_length=30)
	address=models.CharField(max_length=50)
	city=models.CharField(max_length=60)
	state_province=models.CharField(max_length=30)
	country=models.CharField(max_length=50)
	website=models.URLField()
class Dog(models.Model):
	salutation=models.CharField(max_length=10)
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=40)
	email=models.EmailField()
class Horse(models.Model):
	title=models.CharField(max_length=100)
	authors=models.ManyToManyField(Dog)
	publisher=models.ForeignKey(Cat)
	publication_date=models.DateField()