from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def StudentDetails(request):
    esdfo=StudentForm()
    d={'esdfo':esdfo}
    if request.method=='POST':
        sdfo=StudentForm(request.POST)
        if sdfo.is_valid():
            sdfo.save()
            return HttpResponse('data is inserted')
        else:
            return HttpResponse('invalid data')
    
    return render(request,'StudentDetails.html',d)