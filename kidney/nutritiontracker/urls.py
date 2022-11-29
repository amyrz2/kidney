from django.urls import path
from . import views 

urlpatterns = [
    path("", views.indexPageView, name="index"), 
    path("about/", views.logEntryPageView, name="logEntry"),    
    path("login/", views.loginPageView, name="login"), 
    #path("profile/<str:person_name>", views.profilePageView, name="profile")

]    


#Ignore the line below for now
#path('<int:pk>/', views.DetailView.as_view(), name='detail'),