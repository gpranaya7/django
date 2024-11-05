from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def StudentDetails(request):
    sdfo=StudentForm()
    d={'sdfo':sdfo}
    if request.method=='POST':
        stud=StudentForm(request.POST)
        if stud.is_valid():
            sn=request.POST['sname']
            sno=request.POST['sid']
            se=request.POST['semail']
            so=Student.objects.get_or_create(sname=sn,sid=sno,semail=se)
            return HttpResponse(str(stud.cleaned_data))
        else:
            return HttpResponse('invalid data')

            
    return render(request,'StudentDetails.html',d)