from django.shortcuts import render

# Create your views here.
def fooddelivery(request):
    return render(request,'fooddelivery.html')
def mapdirections(request):
    return render(request,'mapdirections.html')