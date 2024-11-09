from django.shortcuts import render

# Create your views here.
import datetime

def filters(request):
    dt=datetime.datetime.now
    d={'data':'django is python framewORk','dt':dt ,'c':2}
    return render(request,'filters.html',d)

def myfilters(request):
    d={'data':'hi Hello Bye bYe'}
    return render(request,'myfilters.html',d)