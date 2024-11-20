from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def registration(request):
    eufo=UserForm()
    epfo=ProfileForm()
    d={'eufo':eufo,'epfo':epfo}
    if request.method=='POST' and request.FILES:
        nmufdo=UserForm(request.POST)
        nmpfdo=ProfileForm(request.POST,request.FILES)
        if nmufdo.is_valid() and nmpfdo.is_valid():
            mufdo=nmufdo.save(commit=False)
            pw=nmufdo.cleaned_data['password']
            mufdo.set_password(pw)
            mufdo.save()

            mpfdo=nmpfdo.save(commit=False)
            mpfdo.username=mufdo
            mpfdo.save()
            send_mail('registration','registration is succesful','pranayah17@gmail.com',[mufdo.email],fail_silently=False)




            return HttpResponse('successful')
        else:
            return HttpResponse('invalid data')




    return render(request,'registration.html',d)

def home(request):
    if request.session.get('username'):
        un=request.session.get('username')
        d={'un':un}
        return render(request,'home.html',d)

    return render(request,'home.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pw']
        auo=authenticate(username=username,password=password)
        if auo:
            if auo.is_active:
                login(request,auo)
                request.session['username']=username 
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('not an active user')
        return HttpResponse('invalid credentials')
    return render(request,'user_login.html')
@login_required
def user_logout(request):
    logout(request)


    return HttpResponseRedirect(reverse('home'))
@login_required
def profile_display(request):
    un=request.session.get('username')
    uo=User.objects.get(username=un)
    po=profile.objects.get(username=uo)
    d={'uo':uo,'po':po}
    return render(request,'profile_display.html',d)
@login_required
def change_password(request):
    if request.method=='POST':
        password=request.POST['pw']
        un=request.session.get('username')
        uo=User.objects.get(username=un)
        uo.set_password(password)
        uo.save()
        return HttpResponse('changed succesfully')
    return render(request,'change_password.html')
def reset_password(request):
    if request.method=='POST':
        username=request.POST['un']
        luo=User.objects.filter(username=username)
        if luo:
            uo=luo[0]

            password=request.POST['pw']
            uo.set_password(password)
            uo.save()
            return HttpResponse('password has been reset succesfully')
        return HttpResponse('user doesnt exist')
    return render(request,'reset_password.html')




    
