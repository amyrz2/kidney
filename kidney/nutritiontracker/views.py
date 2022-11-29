from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
#from django.views import generic
# Create your views here.

def indexPageView(request) :
    return render(request, 'nutritiontracker/index.html')   

def loginPageView(request) :
    return render(request, 'nutritionTracker/login.html')

def personalInformationPageView(request) :
    return render(request, 'nutritionTracker/personalInformation.html')

def createaccountPageView(request) :
    return render(request, 'nutritionTracker/createaccount.html')

def homePageView(request) :
    return render(request, 'nutritionTracker/homepage.html')

def journalPageView(request) :
    return render(request, 'nutritionTracker/journal.html')

def addmealPageView(request) :
    return render(request, 'nutritionTracker/addmeal.html')

def dashBoardPageView(request) :
    return render(request, 'nutritionTracker/dashboard.html')

def addAPPageView(request) :
    return render(request, 'nutritionTracker/addAP.html')