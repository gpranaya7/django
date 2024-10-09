from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q
def access_record(request):
     no=input('enter id')
     wp=webpage.objects.get(id=no)
     d=input('enter date:')
     a=input('enter author')
     ar=accessrecord.objects.get_or_create(name=wp,author=a,date=d)
     return  HttpResponse('accessrecord data created')

from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# # # Create your views here.
def access_record(request):
      t=input('enter a topic name:')
      to=topic.objects.get_or_create(topic_name=t)
      n=input('enter name:')
      u=input('enter url')
      wp=webpage.objects.get_or_create(topic_name=to[0],name=n,url=u)
      a=input('enter author name:')
      d=input('enter date:')
      ar=accessrecord.objects.get_or_create(name=wp[0],author=a,date=d)

      if ar[1]:
           return HttpResponse('created')
      else:
           return HttpResponse('exists')

 #from app.models import *
def access_record(request):
     no=input('enter an id')
     wpo=webpage.objects.filter(id=no)
     if wpo:
        d=input('enter date:')
        a=input('enter author name:')
        ar=accessrecord.objects.get_or_create(name=wpo[0],date=d,author=a)
        return HttpResponse('accessrecord data created')
     else:
        return HttpResponse('name not found')
def display_topics(request):
     topics=topic.objects.all()
     d={'topics':topics}
     return render(request,'display_topics.html',d)
def insert_topic(request):
     return render(request,'display_topics.html')

def insert_topics(request):
    tn=input('enter topic name:')
    to=topic.objects.get_or_create(topic_name=tn)
    if to[1]:
            topics=topic.objects.all()
            d={'topics':topics}
            return render(request,'display_topics.html',d)
    else:
       return HttpResponse('tn already exists')
from app.models import *

def display_topics(request):
     topics=topic.objects.filter(topic_name__in=('cricket','hockey'))
     topics=topic.objects.all()
     topics=topic.objects.filter(topic_name__startswith='b',topic_name__endswith='l')
     topics=topic.objects.filter(Q(topic_name__startswith='b')| Q(topic_name__endswith='n'))
     d={'topics':topics}
     return render(request,'display_topics.html',d)

def display_access(request):
     access=accessrecord.objects.filter(date__week=5)
     
     d={'access':access}
     return render(request,'display_access.html',d)
def nametopic(request):
     nto=topic.objects.prefetch_related('webpage_set').all()
     d={'nto':nto}
     return render(request,'nametopic.html',d)