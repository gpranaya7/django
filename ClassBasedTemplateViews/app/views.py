from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from app.forms  import *
from django.http import HttpResponse
# Create your views here.
class RenderHtml(TemplateView):
    template_name='renderHTML.html'
    def get_context_data(self, **kwargs):
        ecdo=super().get_context_data(**kwargs)
        ecdo['name']='honey'
        ecdo['age']=24
        ecdo['efdo']=SchoolMF()
        return ecdo
    def post(self,request):
        sfdo=SchoolMF(request.POST)
        if sfdo.is_valid:
            sfdo.save()
            return HttpResponse('data inserted')
        
class SchoolFv(FormView):
    template_name='SchoolFv.html'
    form_class=SchoolMF
    def form_valid(self, form):
        form.save()
        return HttpResponse('data inserted')
