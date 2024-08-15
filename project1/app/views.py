from django.shortcuts import render

# Create your views here.
from django.http  import httpresponse;
def starbucks(){
    return httpresponse("worst coffee")
}