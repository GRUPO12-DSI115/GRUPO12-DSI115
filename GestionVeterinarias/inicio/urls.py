from django.urls import path


#implemetar views.py
from . import views
#from . import index

urlpatterns = [
    path('', views.home, name = "home"),
    
    
]

