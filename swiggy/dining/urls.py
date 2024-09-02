from django.urls import path
from dining.views import *
app_name='reserved'
urlpatterns=[
    path('restaurant/',restaurant,name='restaurant')
]