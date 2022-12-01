from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, Context
from datetime import datetime
from .forms import NewUserForm
from django.contrib.auth import authenticate, login

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
        print('here')
        return render(request, 'nutritionTracker/login.html',context)
        # Return an 'invalid login' error message.

#Check to see if the browser contains a login cookie    
def checkLogin(request,route):
    if request.COOKIES.get('loggedIn'):
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
            userData = form.cleaned_data
            print(form.cleaned_data['password'])
            user = User.objects.create_user(username=userData['username'],password=userData['password'],first_name=userData['f_name'],last_name=userData['l_name'],email=userData['email'])
            user.save()
            return HttpResponseRedirect('/login')
    else:
        form = NewUserForm()
    return render(request, 'nutritionTracker/createaccount.html', {'form': form})


def indexPageView(request) :
    response = render(request, 'nutritiontracker/index.html') 
    
    return response

def loginPageView(request) :
    #if 'username' in request.COOKIES:
        #if request.COOKIES['validated'] == 'logged in':
            #return render(request, 'nutritionTracker/dashboard.html')
    #else:
    return render(request, 'nutritionTracker/login.html')

def ContactSupport(request) :
    return render(request, 'nutritionTracker/contactsupport.html')


def addPersonalInfo(request) :
    return render(request, 'nutritionTracker/addpi.html')

def createaccountPageView(request) :
    return render(request, 'nutritionTracker/createaccount.html')

def dashboardPageView(request) :
    return render(request, 'nutritionTracker/dashboard.html')

def journalPageView(request) :
    return render(request, 'nutritionTracker/journal.html')

def addmealPageView(request) :
    return render(request, 'nutritionTracker/addmeal.html')

def addAPPageView(request) :
    return render(request, 'nutritionTracker/addAP.html')