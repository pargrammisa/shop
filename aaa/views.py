from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return HttpResponse("It is a test")
# Create your views here.
