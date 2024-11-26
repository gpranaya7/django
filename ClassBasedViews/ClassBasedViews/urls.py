"""
URL configuration for ClassBasedViews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cbv_str/',cbv_str.as_view(),name='cbv_str'),
    path('cbv_html/',cbv_html.as_view(),name='cbv_html'),
    path('template_view/',TemplateView.as_view(template_name='template_view.html'),name='template_view'),
    path('insert_into_student/',insert_into_student.as_view(),name='insert_into_student'),

]
