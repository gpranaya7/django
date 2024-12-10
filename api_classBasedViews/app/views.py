from django.shortcuts import render
from rest_framework.decorators import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response
# Create your views here.
class productCRUD(APIView):
    def get(self,request,pk=None):
        #lo=products.objects.all()
        io=products.objects.get(pid=pk)
        spo=productsSerializedObj(io)
        #spo=productsSerializedObj(lo,many=True)
        #return Response(spo.data)
        return Response(spo.data)
    def post(self,request,pk=None):
        pdo=request.data
        spdo=productsSerializedObj(data=pdo)
        if spdo.is_valid():
            spdo.save()
            return Response({'insert':'data is inserted'})
        else:
            return Response({'error':'data is not inserted'})
    def put(self,request,pk=None):
        ipo=products.objects.get(pid=pk)
        updated=productsSerializedObj(ipo,data=request.data)
        if updated.is_valid():
            updated.save()
            return Response({'update':'the data is updated'})
        else:
            return Response({'error':'the date is not updated'})
    def patch(self,request,pk):
        ipo=products.objects.get(pid=pk)
        updatedPatch=productsSerializedObj(ipo,data=request.data,partial=True)
        if updatedPatch.is_valid():
            updatedPatch.save()
            return Response({"update":'date is updated'})
        else:
            return Response({'error':'the date isnt updated'})


    def delete(self,request,pk):
        ipo=products.objects.get(pid=pk)
        ipo.delete()
        return Response({'delete':'the data is deleted'})


