"""emp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_emp/',insert_emp,name='insert_emp'),
    path('display_emp',display_emp,name='display_emp'),
    path('display_empmgr/',display_empmgr,name='displayempmgr'),
    path('display_empmgrdept/',display_empmgrdept,name='display_empmgrdept'),
    path('empvalues/',empvalues,name='empvalues'),
    path('deptemp/',deptemp,name='deptemp'),
    path('based_on_sal/',based_on_sal,name='based_on_sal')
]
