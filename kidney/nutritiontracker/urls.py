from django.urls import path
from . import views 

urlpatterns = [
    path("", views.indexPageView, name="index"), 
    path("login/", views.loginPageView, name="login"), 
    path("personalInformation", views.personalInformationPageView, name="personalInformation"),
    path("createaccount", views.createaccountPageView, name="createaccount"),
    path("homepage", views.homePageView, name="homepage"),
    path("journal", views.journalPageView, name="journal"),
    path("addmeal", views.addmealPageView, name="addmeal"),
    path("dashboard", views.dashBoardPageView, name="dashboard"),
    path("addAP", views.addAPPageView, name="addAP"),
]    


#Ignore the line below for now
#path('<int:pk>/', views.DetailView.as_view(), name='detail'),