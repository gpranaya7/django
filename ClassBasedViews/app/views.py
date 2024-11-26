from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *
# Create your views here.
class cbv_str(View):
    def get(self,request):
        return HttpResponse('cbv_str')
class cbv_html(View):
    def get(self,request):
        return render(request,'cbv_html.html')
class insert_into_student(View):
    def get(self,request):
        esfo=studentmf()
        d={'esfo':esfo}
        return render(request,'insert_into_student.html',d)
    def post(self,request):
        sfo=studentmf(request.POST)
        if sfo.is_valid:
            sfo.save()
            return HttpResponse('done')
        else:
            return HttpResponse('invalid data')

