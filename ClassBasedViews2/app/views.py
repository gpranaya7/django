from django.shortcuts import render
from django.views.generic import ListView,TemplateView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *
from django.urls import reverse_lazy
# Create your views here.
class SchoolList(ListView):
    model=School
    queryset=School.objects.all()
    context_object_name='schools'
    template_name='app/school_list.html'
    ordering=['scname']

class home(TemplateView):
    template_name='app/home.html'
class SchoolDetails(DetailView):
    model=School
    context_object_name='scobject'
class SchoolCreate(CreateView):
    model=School
    fields='__all__'
class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'
class SchoolDelete(DeleteView)    :
    model=School
    context_object_name='schoolObject'
    success_url=reverse_lazy('SchoolList')