from django.urls import include, path
from .views import *

urlpatterns = [
            
               #for iris
                path('iris',iris.as_view(), name="iris"),
             
                

              ]

