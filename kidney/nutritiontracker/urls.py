from django.urls import path
from . import views 

urlpatterns = [
    path("", views.indexPageView, name="index"), 
    path("login/", views.loginPageView, name="login"), 
    path("personalInformation/", views.personalInformationPageView, name="personalInformation"),
    #path("createaccount/", views.createaccountPageView, name="createaccount"),
    path("dashboard/", views.dashboardPageView, name="dashboard"),
    path("journal/", views.journalPageView, name="journal"),
    path("addmeal/", views.addmealPageView, name="addmeal"),
    path("addAP/", views.addAPPageView, name="addAP"),
    path("createNewUser/", views.CreateNewUser, name="createNewUser"),
    path("loginAccount",views.loginAccount, name='loginAccount')
]    


#Ignore the line below for now
#path('<int:pk>/', views.DetailView.as_view(), name='detail'),