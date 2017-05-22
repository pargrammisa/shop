from django.db import models
# TravelersInput class is used to store users data directly.
class TravelersInput(models.Model):
	user=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=30)
	family=models.CharField(max_length=30)
	job=models.CharField(max_length=50)
	desire_arrival_time=models.TimeField(null=True)
	on_time_importance=models.IntegerField(null=True)
	late_dissatisfication=models.IntegerField(null=True)
	early_dissatisfication=models.IntegerField(null=True)
	destination_activity=models.CharField(max_length=50)
	no_late=models.IntegerField(null=True)
	no_early=models.IntegerField(null=True)
	#the next 3 fields are used to store the idea of users,
	#whether they are satisfied or not,if not what is their problem?
	#early arrival probability or late arrival probability?
	agree=models.IntegerField(null=True)
	late_prob=models.IntegerField(null=True)
	early_prob=models.IntegerField(null=True)
#InputConvert class is used to store converted users' input for applying in algorithms.
class InputConvert(models.Model):
	user=models.ForeignKey(TravelersInput)
	vo=models.FloatField()
	vt=models.FloatField()
	ve=models.FloatField()
	vd=models.FloatField()
	td=models.FloatField()
	m=models.FloatField()
#Feedback class is used to store users idea about the output of application at end of travel.
class Feedback(models.Model):
	user=models.ForeignKey(TravelersInput)
	arrival_time=models.TimeField()
	app_satisfication=models.IntegerField()
	comment=models.TextField()
#AlgorithmOutput is used to store the output of algorithm according to paper numerical example
class AlgorithmOutput(models.Model):
	user=models.ForeignKey(TravelersInput)
	total_cost=models.FloatField()
	optimal_f=models.FloatField()
	optimal_m=models.FloatField()
	c0=models.FloatField()
	c1=models.FloatField()
	c2=models.FloatField()
#TravelersOutput is used to store application outputs for showing to users.
class TravelersOutput(models.Model):
	user=models.ForeignKey(TravelersInput)
	departure_time=models.TimeField()
	late_prob=models.FloatField()
	early_prob=models.FloatField()
class TravelTimeDistributation(models.Model):
	user=models.ForeignKey(TravelersInput)
	mean=models.FloatField()
	sd=models.FloatField()
	#pt is extracted probability function from given sd and mean.
	pt=models.CharField(max_length=100)	
	tmin=models.FloatField()
	#required information, extracted from pt
	tmax=models.FloatField()
	tM=models.FloatField()
	to=models.FloatField()
	landa1=models.FloatField()
	landa2=models.FloatField()
	#td is user desire arrival time, need to convert to match with travel time distributation
	td=models.FloatField()
	