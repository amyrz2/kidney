from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
#from django.views import generic
# Create your views here.

def indexPageView(request) :
    return render(request, 'nutritiontracker/index.html')   

def loginPageView(request) :
    return render(request, 'nutritionTracker/login.html')

def dailyNutritionView(request) :
    return render(request, 'nutritionTracker/dailyBreakdown.html')

def logEntryPageView(request) :
    return render(request, 'nutritionTracker/logEntry.html')