from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
	#This is the basic respone for a request
	#return HttpResponse("<h1> Home Page </h1>")
	#This returns a html template
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	#This returns a html template
	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	#This returns a html template
	return render(request, "about.html", {})

def dashboard_view(request, *args, **kwargs):
	#This returns a html template
	contextforview = 
	return render(request, "dashboard.html", {})

def jobs_view(request, *args, **kwargs):
	#This returns a html template
	return render(request, "jobs.html", {})

def deals_view(request, *args, **kwargs):
	#This returns a html template
	return render(request, "deals.html", {})