from django.urls import path
from grocery.views import *
app_name='ordering'

urlpatterns=[
    path('order/',order,name='order')
]