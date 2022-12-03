from django.urls import path
from app2.views import *
app_name='anyname'
urlpatterns=[ 
    path('hello/',hello,name='hello')
]