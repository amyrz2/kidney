from django.urls import path
from . import views 

urlpatterns = [
    path("", views.indexPageView, name="index"), 
    path("login/", views.login_request, name="login"),
    path("personalinfo/", views.personalInformationPageView, name="personalinfo"),
    #path("createaccount/", views.createaccountPageView, name="createaccount"),
    path("dashboard/", views.dashboardPageView, name="dashboard"),
    path("journal/", views.journalPageView, name="journal"),
    path("addmeal/", views.addmealPageView, name="addmeal"),
    path("addAP/", views.addAPPageView, name="addAP"),
    path("register/", views.register_request, name="register"),
    path("contactsupport/", views.ContactSupport, name="contactsupport"),
    path("loginAccount/",views.loginAccount, name='loginAccount'),
    path("logout/", views.logout, name='logout'),
    path("searchAPI/", views.searchAPI, name='searchAPI'),
    path("addpi/",views.addPersonalInfo, name='addpi'),
    path("logFood/",views.logFood, name='logFood')
]    
