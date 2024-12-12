from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import requests
# Create your views here.
def register(request):
    umfo=userForm()
    emfo=profileForm()
    d={'emfo':emfo,'umfo':umfo}
    if request.method=='POST' and request.FILES:
        ufo=userForm(request.POST)
        pfo=profileForm(request.POST,request.FILES)
        if ufo.is_valid() and pfo.is_valid():
            mufo=ufo.save(commit=False)
            pw=ufo.cleaned_data['password']
            mufo.set_password(pw)
            mufo.save()

            mpfo=pfo.save(commit=False)
            mpfo.user=mufo
            mpfo.save()

            send_mail('registration','registration is successful','gpranaya9@gmail.com' ,[mufo.email],fail_silently=False)
            return HttpResponse('user is created')
        else:
            return HttpResponse('invalid data')







    return render(request,'register.html',d)
def home(request):
    if request.session.get('username'):
        un=request.session.get('username')
        d={'un':un}
        return render(request,'home.html',d)

    return render(request,'home.html')
def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        ao=authenticate(username=username,password=password)
        if ao:
            if ao.is_active:
                login(request,ao)
                request.session['username']=username
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('the user is not active')
        else:
            return HttpResponse('invalid credentials')       

        

    return render(request,'user_login.html')
@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect(reverse('home'))
@login_required
def check_weather(request):
    if request.method=='POST':
        city=request.POST['city']
        api_key='91d1f83bbfa9281a6524f847a2616847'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response=requests.get(url)
        data=response.json()
        temperature=data['main']['temp']
        humidity=data['main']['humidity']
        weather=data['main']['feels_like']
        speed=data['wind']['speed']
        username=request.session.get('username')
        uo=User.objects.get(username=username)
        weather_data=weatherData.objects.create(user=uo,city=city,temperature=temperature,humidity=humidity,weather=weather,speed=speed)
        weather_data.save()
        d={'weather_data':weather_data}
        return render(request,'check_weather.html',d)







    return render(request,'check_weather.html')
        