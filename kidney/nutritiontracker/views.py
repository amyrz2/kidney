from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, Context
from datetime import datetime
from .forms import NewUserForm, APISearch
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
import requests
import json


#Functioning, logs user in
def loginAccount(request):
    sUsername = request.POST['uname']
    sPassword = request.POST['psw']
    user = authenticate(request, username=sUsername, password=sPassword)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        response = HttpResponseRedirect('/dashboard')
        response.set_cookie('loggedIn',True)
        return response
        
    else:
        context = {'failed':True}
        return render(request, 'nutritionTracker/login.html',context)
        # Return an 'invalid login' error message.

#Check to see if the browser contains a login cookie    
def checkLogin(request,route):
    if request.COOKIES['loggedIn']:
        print('good')
        return render(request, route)
    else:
        print('bad')
        return render(request, 'nutritionTracker/login.html')

def personalInformationPageView(request) :
    route = 'nutritionTracker/personalInformation.html'
    return checkLogin(request,route)
    #return render(request, 'nutritionTracker/personalInformation.html')

#Not associated with a URL, called by other views to check user before continuing
def authUser(sUsername,sPassword):
    bAuthorized = authenticate(username=sUsername,password=sPassword)
    if bAuthorized is not None:
        bAuthorized = True
    else:
        bAuthorized = False
    return bAuthorized

#Functioning Route
def CreateNewUser(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            try:
                print('trying')
                userData = form.cleaned_data
                user = User.objects.create_user(username=userData['username'],password=userData['password'],first_name=userData['f_name'],last_name=userData['l_name'],email=userData['email'])
                user.save()
                return HttpResponseRedirect('/login')
            except IntegrityError:
                print('duplicate')
                form = NewUserForm()
                context = {'message':'This user already exists'}
                return render(request,'nutritionTracker/createaccount.html',context)
       
    else:
        print("no post")
        form = NewUserForm()
        return render(request, 'nutritionTracker/createaccount.html', {'message':'none','form': form})


def indexPageView(request) :
    response = render(request, 'nutritiontracker/index.html') 
    return response

#this is run when the user clicks on mynutrition in the navbar, if logged in, it goes to the dash, otherwise, to login page
def loginPageView(request) :
    if 'loggedIn' in request.COOKIES:
        if request.COOKIES['loggedIn'] == 'True':
            return render(request, 'nutritionTracker/dashboard.html')
    #else:
    return render(request, 'nutritionTracker/login.html')

#logs user out (removes logged in cookie) and sends user to the login page
def logout(request):
    response = HttpResponseRedirect('/login')
    if ('loggedIn' in request.COOKIES) & (request.COOKIES['loggedIn'] == 'True') :
        #return render(request, 'nutritionTracker/dashboard.html')
        response = HttpResponseRedirect('/login')
        response.set_cookie('loggedIn',False)
        return response
    else:
        return response
def ContactSupport(request) :
    return render(request, 'nutritionTracker/contactsupport.html')


def addPersonalInfo(request) :
    return render(request, 'nutritionTracker/addpi.html')

def dashboardPageView(request) :
    labels = []
    data = []

    # queryset = City.objects.order_by('-population')[:5]
    # for city in queryset:
    #     labels.append(city.name)
    #     data.append(city.population)

 
    return render(request, 'nutritionTracker/dashboard.html', {
        'labels': labels,
        'data': data,
    })

def journalPageView(request) :
    return render(request, 'nutritionTracker/journal.html')

def addmealPageView(request) :
    return render(request, 'nutritionTracker/addmeal.html')

def addAPPageView(request) :
    return render(request, 'nutritionTracker/addAP.html')

def searchAPI(request):
    name = request.POST['searchQuery']
    url = 'https://api.nal.usda.gov/fdc/v1/foods/search?query='+name+'&api_key=nel7mrK7DgNjarXN7RhhZk4I2bRVJfeNUa0q7Dxy'
    response = requests.get(url)
    data = response.json()
    
    myResults = data['foods']
    foodObjects = []

    #returns all of the results from the API query, creates a list called foodObjects with the necessary attributes
    for item in myResults:
        food = {}
        if 'brandName' in item:
            food['brandName'] = item['brandName']
        if 'description' in item:
            food['description'] = item['lowercaseDescription']
        if 'ingredients' in item:
            food['ingredients'] = item['ingredients']
        if 'servingSizeUnit' in item:
            food['servingUnit'] = item['servingSizeUnit']
        if 'servingSize' in item:
            food['servingSize'] = round(item['servingSize'])
        if 'foodNutrients' in item:
            food['nutrients'] = item['foodNutrients']
        foodObjects.append(food)

        
    return render (request, 'nutritionTracker/addmeal.html', { "foodResults": 
    foodObjects})

def logFood(request):
    return render (request, 'nutritionTracker/logFood.html')