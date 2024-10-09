from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_capital(request):
    no=input('enter id')
    cname=input('enter country name')
    co=country.objects.get_or_create(id=no,name=cname)
    cap=input('enter capital name')
    cn=capitals.objects.get_or_create(name=co[0],capital=cap)
    if cn[1]:
        return HttpResponse(' capital is created')
    else:
        return HttpResponse('capital already exists')

