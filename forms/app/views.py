from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def topicform(request):
    if request.method=='POST':
        tm=request.POST['tn']
        to=Topic.objects.get_or_create(topic_name=tm)


    return render(request,'topicform.html')

def insert_webpage(request):
    lwo=Topic.objects.all()
    d={'lwo':lwo}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        to=Topic.objects.get(topic_name=tn)
        wo=webpage.objects.get_or_create(topic_name=to,name=na,url=ur)




    return render(request,'insert_webpage.html',d)
from app.models import *

def select_multiple(request):

    lto=Topic.objects.all()
    d={'lto':lto}
    if request.method=='POST':
        mtn=request.POST.getlist('tn')
        for topic in mtn:
            eqs=webpage.objects.none()
            eqs=eqs|webpage.objects.filter(topic_name=topic)
            d1={'eqs':eqs}
            return render(request,'display_webpage.html',d1)


    

    return render(request,'select_multiple.html',d)

def checkbox(request):
    lto=Topic.objects.all()
    d={'lto':lto}
    return render(request,'checkbox.html',d)