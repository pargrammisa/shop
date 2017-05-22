from django.shortcuts import render_to_response
from django.http import HttpResponse
import statistics
from static.models import Data
#import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Create your views here.
def central(request):
	data2=[]
	for i in range(10):
		d=input("enter data:")
		data2.append(float(d))
	ans1= statistics.mean(data2)
	ans2= statistics.median(data2)
	ans3=statistics.mode(data2)
	ans4=statistics.variance(data2)
	ans5=statistics.stdev(data2)
	return render_to_response("cent.html",{"data":data2,"mean":ans1,"median":ans2,"mode":ans3,"SD":ans5,"variance":ans4})
def reg(request):
	x=[]
	y=[]
	for i in range(10):
		d1=input("enter x: ")
		x.append(int(d1))		
		d2=input("enter y: ")
		y.append(int(d2))
	ans1 = np.polyfit(x, y, 1)
	ans2=ans1[0]
	ans3=ans1[1]
	x_var=input("enter one X to predict related Y: ")
	ans4=ans2*int(x_var)+ans3
	plt.plot(x,y,'ro',ans2*x+ans3,'--k')
	plt.axis([0,20,0,20])
	return render_to_response("regression.html",{"x_data":x,"y_data":y,"reg":ans1,"a":ans2,"b":ans3,"y":ans4,"x":x_var,"show":plt.show})
	
