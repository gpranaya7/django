from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models import Avg
# from decimal import Decimal 
# Create your views here.
# def insert_emp(request):
#      dno=int(input('enter deptno'))
#      dn=input('enter dept name')
#      dloc=input('enter loc')
#      do=Dept.objects.get_or_create(deptno=dno,dname=dn,loc=dloc)
#      eno=int(input('enter empno:'))
#      en=input('enter ename:')
#      j=input('enter job')
#      mgrno=input('enter mgr')
#      hd=input('enter hiredate')
#      com=input('enter comm')
#      s=Decimal(input('enter salary'))
#      eo=Emp.objects.get_or_create(empno=eno,ename=en,job=j,mgr=mgrno,hiredate=hd,comm=com,sal=s,deptno=do[0])
#      if eo[1]:
#          return  HttpResponse('emp data is created')
#      else:
#          return HttpResponse('emp data already exists')
    
def insert_emp(request):
    dno=int(input('enter deptno'))
    do=Dept.objects.get(deptno=dno)
    eno=input('enter empno:')
    en=input('enter ename:')
    j=input('enter job')
    mgrno=input('enter mgr')
    mo=Emp.objects.get(empno=mgrno)
    hd=input('enter hiredate')
    s=input('enter sal:')
    com=input('enter comm:')
    eo=Emp.objects.get_or_create(empno=eno,ename=en,job=j,mgr=mo,hiredate=hd,deptno=do ,sal=s,comm=com)
    return HttpResponse('emp data created')
def display_emp(request):
    emp=Emp.objects.filter(comm__isnull=True)
    emp=Emp.objects.all()
    emp=Emp.objects.all()
    edo=Emp.objects.all()
    edo=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=True,ename='smith')
    edo=Emp.objects.select_related('deptno').filter(deptno__loc__contains='w')
    edo=Emp.objects.select_related('deptno').filter(deptno__dname='accounting',sal__gte=20000)
    edo=Emp.objects.select_related('mgr').all()
    asoemp=Emp.objects.all().aggregate(Avg('sal'))
    print(asoemp)
    ldeo=Emp.objects.select_related('deptno').filter(sal__gt=asoemp['sal__avg'])
    

    d={'ldeo':ldeo}
    return render(request,'display_emp.html',d)
def display_empmgr(request):
    lemo=Emp.objects.select_related('mgr').all()
    d={'lemo':lemo}
    return render(request,'display_empmgr.html',d)
def display_empmgrdept(request):
    lemdo=Emp.objects.select_related('deptno','mgr').all()
    d={'lemdo':lemdo}
    return render(request,'display_empmgrdept.html',d)
def empvalues(request):
    leo=Emp.objects.values('ename','empno').all()
    d={'leo':leo}
    return render(request,'empvalues.html',d)
def deptemp(request):
    ldeo=Dept.objects.prefetch_related('emp_set').filter(dname='accounting')
    print(Emp.objects.all().aggregate(Avg('sal')))
    print(Emp.objects.values('deptno').annotate(Avg('sal')))
    print(Emp.objects.filter(deptno=20).aggregate(Avg('sal')))
    

    d={'ldeo':ldeo}
    return render(request,'deptemp.html',d)
def based_on_sal(request):
    asoemp=Emp.objects.all().aggregate(Avg('sal'))
    doed=Emp.objects.select_related('deptno').filter(sal__lt=asoemp['sal__avg'])
    d={'doed':doed}
    return render(request,'based_on_sal.html',d)


