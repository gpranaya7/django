from django.shortcuts import render
from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET','POST'])
def EmpData(request):
    leo=Emp.objects.all()
    serializedData=EmpDataSerializers(leo, many=True)
    return Response(serializedData.data)





